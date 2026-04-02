#!/usr/bin/env python3
"""
Oracle Simphony BI API — Read-only CLI for C-level restaurant reporting.
Pulls sales, labor, product mix, payments, discounts, and guest checks
across multiple restaurant locations.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timedelta

try:
    import requests
except ImportError:
    print("ERROR: requests package not installed. Run: pip install requests")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Import auth helper
sys.path.insert(0, os.path.dirname(__file__))
from simphony_auth import get_valid_token


def get_config():
    host = os.getenv("SIMPHONY_HOST")
    org = os.getenv("SIMPHONY_ORG")
    if not host:
        print("ERROR: SIMPHONY_HOST not set. Add to .env.")
        sys.exit(1)
    if not org:
        print("ERROR: SIMPHONY_ORG not set. Add to .env.")
        sys.exit(1)
    return {"host": host, "org": org}


class SimphonyClient:
    def __init__(self):
        config = get_config()
        self.base_url = f"{config['host']}/bi/v1/{config['org']}"
        self.token = get_valid_token()
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def _post(self, endpoint, payload):
        url = f"{self.base_url}/{endpoint}"
        resp = self.session.post(url, json=payload)
        if resp.status_code == 401:
            print("ERROR: 401 Unauthorized — token may be expired. Run: python simphony_auth.py setup")
            sys.exit(1)
        if resp.status_code == 400:
            print(f"ERROR: 400 Bad Request — {resp.text[:300]}")
            sys.exit(1)
        if resp.status_code != 200:
            print(f"ERROR: {resp.status_code} — {resp.text[:300]}")
            sys.exit(1)
        return resp.json()

    # --- Dimensions (reference data) ---

    def get_locations(self):
        return self._post("getLocationDimensions", {})

    def get_revenue_centers(self, loc_ref):
        return self._post("getRevenueCenterDimensions", {"locRef": loc_ref})

    def get_menu_items(self, loc_ref):
        return self._post("getMenuItemDimensions", {"locRef": loc_ref})

    def get_employees(self, loc_ref):
        return self._post("getEmployeeDimensions", {"locRef": loc_ref})

    def get_latest_business_date(self, loc_ref):
        return self._post("getLatestBusDt", {"locRef": loc_ref})

    # --- Daily aggregations ---

    def get_operations_daily(self, loc_ref, bus_dt):
        return self._post("getOperationsDailyTotals", {"locRef": loc_ref, "busDt": bus_dt})

    def get_menu_item_daily(self, loc_ref, bus_dt):
        return self._post("getMenuItemDailyTotals", {"locRef": loc_ref, "busDt": bus_dt})

    def get_discount_daily(self, loc_ref, bus_dt):
        return self._post("getDiscountDailyTotals", {"locRef": loc_ref, "busDt": bus_dt})

    def get_employee_daily(self, loc_ref, bus_dt):
        return self._post("getEmployeeDailyTotals", {"locRef": loc_ref, "busDt": bus_dt})

    def get_job_code_daily(self, loc_ref, bus_dt):
        return self._post("getJobCodeDailyTotals", {"locRef": loc_ref, "busDt": bus_dt})

    def get_tender_daily(self, loc_ref, bus_dt):
        return self._post("getTenderMediaDailyTotals", {"locRef": loc_ref, "busDt": bus_dt})

    def get_order_type_daily(self, loc_ref, bus_dt):
        return self._post("getOrderTypeDailyTotals", {"locRef": loc_ref, "busDt": bus_dt})

    # --- Transactions ---

    def get_guest_checks(self, loc_ref, bus_dt):
        return self._post("getGuestChecks", {"locRef": loc_ref, "busDt": bus_dt})

    # --- Labor ---

    def get_time_cards(self, loc_ref, bus_dt):
        return self._post("getTimeCardDetails", {"locRef": loc_ref, "busDt": bus_dt})

    # --- Cash ---

    def get_cash_management(self, loc_ref, bus_dt):
        return self._post("getCashManagementDetails", {"locRef": loc_ref, "busDt": bus_dt})


# --- Date helpers ---

def parse_date_arg(date_str):
    """Parse date argument: YYYY-MM-DD or Nd (days ago)."""
    if not date_str:
        return datetime.now().strftime("%Y-%m-%d")
    if date_str.endswith("d"):
        days = int(date_str[:-1])
        return (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    return date_str


def date_range(since_str, until_str=None):
    """Generate list of dates from since to until (or today)."""
    start = datetime.strptime(parse_date_arg(since_str), "%Y-%m-%d")
    end = datetime.strptime(parse_date_arg(until_str), "%Y-%m-%d") if until_str else datetime.now()
    dates = []
    current = start
    while current <= end:
        dates.append(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1)
    return dates


# --- Output formatting ---

def fmt_currency(val):
    if val is None:
        return "—"
    return f"{val:,.2f}"


def cmd_locations(client, args):
    data = client.get_locations()
    locations = data.get("locationDimensions", data.get("locations", []))
    if isinstance(data, dict) and not locations:
        # Try to find location data in response
        for key in data:
            if isinstance(data[key], list):
                locations = data[key]
                break

    if args.format == "json":
        print(json.dumps(data, indent=2, default=str))
        return

    print(f"{'Loc Ref':<12} {'Name':<40} {'Status':<10}")
    print("-" * 65)
    if isinstance(locations, list):
        for loc in locations:
            ref = loc.get("locRef", loc.get("locationRef", ""))
            name = loc.get("locName", loc.get("locationName", loc.get("name", "")))
            status = loc.get("status", "")
            print(f"{str(ref):<12} {str(name)[:40]:<40} {str(status):<10}")
        print(f"\nTotal: {len(locations)} locations")
    else:
        print(json.dumps(data, indent=2, default=str))


def cmd_sales(client, args):
    loc_ref = args.location
    dates = date_range(args.since, args.date) if args.since else [parse_date_arg(args.date)]

    all_data = []
    for dt in dates:
        data = client.get_operations_daily(loc_ref, dt)
        if args.format == "json":
            all_data.append(data)
            continue

        rvc_list = data.get("revenueCenters", [])
        total_net = sum(r.get("netSlsTtl", 0) for r in rvc_list)
        total_tax = sum(r.get("taxCollTtl", 0) for r in rvc_list)
        total_checks = sum(r.get("chkCnt", 0) for r in rvc_list)
        total_guests = sum(r.get("gstCnt", 0) for r in rvc_list)
        total_voids = sum(r.get("vdTtl", 0) for r in rvc_list)
        total_discounts = sum(r.get("itmDscTtl", 0) + r.get("subDscTtl", 0) for r in rvc_list)

        avg_check = total_net / total_checks if total_checks else 0

        print(f"\n{'='*50}")
        print(f"  Location: {loc_ref} | Date: {dt}")
        print(f"{'='*50}")
        print(f"  Net Sales:     {fmt_currency(total_net)}")
        print(f"  Tax Collected:  {fmt_currency(total_tax)}")
        print(f"  Checks:        {total_checks}")
        print(f"  Guests:        {total_guests}")
        print(f"  Avg Check:     {fmt_currency(avg_check)}")
        print(f"  Discounts:     {fmt_currency(total_discounts)}")
        print(f"  Voids:         {fmt_currency(total_voids)}")

        if len(rvc_list) > 1:
            print(f"\n  By Revenue Center:")
            print(f"  {'RVC':<8} {'Net Sales':>12} {'Checks':>8} {'Guests':>8}")
            print(f"  {'-'*8} {'-'*12} {'-'*8} {'-'*8}")
            for r in rvc_list:
                print(f"  {r.get('rvcNum',''):<8} {fmt_currency(r.get('netSlsTtl',0)):>12} {r.get('chkCnt',0):>8} {r.get('gstCnt',0):>8}")

    if args.format == "json":
        print(json.dumps(all_data, indent=2, default=str))


def cmd_pmix(client, args):
    loc_ref = args.location
    dt = parse_date_arg(args.date)
    data = client.get_menu_item_daily(loc_ref, dt)

    if args.format == "json":
        print(json.dumps(data, indent=2, default=str))
        return

    print(f"\nProduct Mix — Location: {loc_ref} | Date: {dt}")
    print(json.dumps(data, indent=2, default=str))


def cmd_labor(client, args):
    loc_ref = args.location
    dt = parse_date_arg(args.date)
    data = client.get_time_cards(loc_ref, dt)

    if args.format == "json":
        print(json.dumps(data, indent=2, default=str))
        return

    print(f"\nLabor — Location: {loc_ref} | Date: {dt}")
    print(json.dumps(data, indent=2, default=str))


def cmd_payments(client, args):
    loc_ref = args.location
    dt = parse_date_arg(args.date)
    data = client.get_tender_daily(loc_ref, dt)

    if args.format == "json":
        print(json.dumps(data, indent=2, default=str))
        return

    print(f"\nPayments — Location: {loc_ref} | Date: {dt}")
    print(json.dumps(data, indent=2, default=str))


def cmd_discounts(client, args):
    loc_ref = args.location
    dt = parse_date_arg(args.date)
    data = client.get_discount_daily(loc_ref, dt)

    if args.format == "json":
        print(json.dumps(data, indent=2, default=str))
        return

    print(f"\nDiscounts — Location: {loc_ref} | Date: {dt}")
    print(json.dumps(data, indent=2, default=str))


def cmd_employees(client, args):
    loc_ref = args.location
    dt = parse_date_arg(args.date)
    data = client.get_employee_daily(loc_ref, dt)

    if args.format == "json":
        print(json.dumps(data, indent=2, default=str))
        return

    print(f"\nEmployee Performance — Location: {loc_ref} | Date: {dt}")
    print(json.dumps(data, indent=2, default=str))


def cmd_checks(client, args):
    loc_ref = args.location
    dt = parse_date_arg(args.date)
    data = client.get_guest_checks(loc_ref, dt)

    if args.format == "json":
        print(json.dumps(data, indent=2, default=str))
        return

    print(f"\nGuest Checks — Location: {loc_ref} | Date: {dt}")
    print(json.dumps(data, indent=2, default=str))


def cmd_dashboard(client, args):
    dt = parse_date_arg(args.date)

    print(f"\nFetching locations...")
    loc_data = client.get_locations()
    locations = loc_data.get("locationDimensions", loc_data.get("locations", []))
    if isinstance(loc_data, dict) and not locations:
        for key in loc_data:
            if isinstance(loc_data[key], list):
                locations = loc_data[key]
                break

    if not isinstance(locations, list) or not locations:
        print("Could not retrieve locations. Returning raw data:")
        print(json.dumps(loc_data, indent=2, default=str))
        return

    print(f"{'='*70}")
    print(f"  SIMPHONY DASHBOARD — {dt}")
    print(f"{'='*70}")

    enterprise_net = 0
    enterprise_checks = 0
    enterprise_guests = 0
    enterprise_voids = 0
    enterprise_discounts = 0
    loc_summaries = []

    for loc in locations:
        loc_ref = str(loc.get("locRef", loc.get("locationRef", "")))
        loc_name = loc.get("locName", loc.get("locationName", loc.get("name", loc_ref)))

        try:
            data = client.get_operations_daily(loc_ref, dt)
            rvc_list = data.get("revenueCenters", [])

            net = sum(r.get("netSlsTtl", 0) for r in rvc_list)
            checks = sum(r.get("chkCnt", 0) for r in rvc_list)
            guests = sum(r.get("gstCnt", 0) for r in rvc_list)
            voids = sum(r.get("vdTtl", 0) for r in rvc_list)
            discounts = sum(r.get("itmDscTtl", 0) + r.get("subDscTtl", 0) for r in rvc_list)
            avg_check = net / checks if checks else 0

            enterprise_net += net
            enterprise_checks += checks
            enterprise_guests += guests
            enterprise_voids += voids
            enterprise_discounts += discounts

            loc_summaries.append({
                "name": loc_name,
                "ref": loc_ref,
                "net": net,
                "checks": checks,
                "guests": guests,
                "avg_check": avg_check,
                "voids": voids,
                "discounts": discounts,
            })
        except Exception as e:
            loc_summaries.append({"name": loc_name, "ref": loc_ref, "error": str(e)})

    # Enterprise totals
    enterprise_avg = enterprise_net / enterprise_checks if enterprise_checks else 0

    print(f"\n--- Enterprise Totals ---")
    print(f"  Net Sales:     {fmt_currency(enterprise_net)}")
    print(f"  Checks:        {enterprise_checks}")
    print(f"  Guests:        {enterprise_guests}")
    print(f"  Avg Check:     {fmt_currency(enterprise_avg)}")
    print(f"  Discounts:     {fmt_currency(enterprise_discounts)}")
    print(f"  Voids:         {fmt_currency(enterprise_voids)}")

    # Per location
    print(f"\n--- By Location ---")
    print(f"  {'Location':<30} {'Net Sales':>12} {'Checks':>8} {'Guests':>8} {'Avg Chk':>10}")
    print(f"  {'-'*30} {'-'*12} {'-'*8} {'-'*8} {'-'*10}")
    for loc in sorted(loc_summaries, key=lambda x: x.get("net", 0), reverse=True):
        if "error" in loc:
            print(f"  {loc['name'][:30]:<30} {'ERROR':>12}")
        else:
            print(f"  {loc['name'][:30]:<30} {fmt_currency(loc['net']):>12} {loc['checks']:>8} {loc['guests']:>8} {fmt_currency(loc['avg_check']):>10}")

    # Void/discount flags
    if enterprise_voids > 0 or enterprise_discounts > 0:
        void_pct = (enterprise_voids / enterprise_net * 100) if enterprise_net else 0
        disc_pct = (enterprise_discounts / enterprise_net * 100) if enterprise_net else 0
        print(f"\n--- Flags ---")
        if void_pct > 2:
            print(f"  ⚠ Voids at {void_pct:.1f}% of net sales")
        if disc_pct > 10:
            print(f"  ⚠ Discounts at {disc_pct:.1f}% of net sales")

    print(f"{'='*70}")

    if args.format == "json":
        print(json.dumps({
            "date": dt,
            "enterprise": {
                "netSales": enterprise_net,
                "checks": enterprise_checks,
                "guests": enterprise_guests,
                "avgCheck": enterprise_avg,
                "voids": enterprise_voids,
                "discounts": enterprise_discounts,
            },
            "locations": loc_summaries,
        }, indent=2, default=str))


# --- CLI ---

def main():
    parser = argparse.ArgumentParser(
        description="Simphony BI API — read-only restaurant reporting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  locations     List all restaurant locations
  sales         Daily operations summary for a location
  dashboard     Enterprise-wide summary across all locations
  pmix          Product mix (menu item sales)
  labor         Time card / labor data
  payments      Payment method breakdown
  discounts     Discount analysis
  employees     Employee performance
  checks        Guest check details

Examples:
  python simphony.py locations
  python simphony.py sales --location 1234 --date 2026-04-01
  python simphony.py sales --location 1234 --since 7d
  python simphony.py dashboard --date 2026-04-01
  python simphony.py pmix --location 1234 --date 2026-04-01

Environment (in .env):
  SIMPHONY_HOST        Application server URL
  SIMPHONY_AUTH_HOST   Authentication server URL
  SIMPHONY_CLIENT_ID   Client ID
  SIMPHONY_USERNAME    API account username
  SIMPHONY_PASSWORD    API account password
  SIMPHONY_ORG         Organization short name
        """
    )
    parser.add_argument("command", help="Command to run")
    parser.add_argument("--location", "-l", help="Location reference (store number)")
    parser.add_argument("--date", "-d", help="Business date (YYYY-MM-DD, default: today)")
    parser.add_argument("--since", "-s", help="Date range start (YYYY-MM-DD or Nd)")
    parser.add_argument("--format", "-f", choices=["table", "json"], default="table")

    args = parser.parse_args()
    client = SimphonyClient()

    location_required = ["sales", "pmix", "labor", "payments", "discounts", "employees", "checks"]

    if args.command in location_required and not args.location:
        print(f"ERROR: --location required for '{args.command}'. Use 'locations' to list available locations.")
        sys.exit(1)

    commands = {
        "locations": cmd_locations,
        "sales": cmd_sales,
        "dashboard": cmd_dashboard,
        "pmix": cmd_pmix,
        "labor": cmd_labor,
        "payments": cmd_payments,
        "discounts": cmd_discounts,
        "employees": cmd_employees,
        "checks": cmd_checks,
    }

    if args.command in commands:
        commands[args.command](client, args)
    else:
        print(f"ERROR: Unknown command '{args.command}'")
        print("Available: " + ", ".join(commands.keys()))
        sys.exit(1)


if __name__ == "__main__":
    main()
