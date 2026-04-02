#!/usr/bin/env python3
"""
FreshService API client — read-only access for C-level reporting.
Supports tickets, agents, groups, assets, problems, changes, SLA policies,
and a computed dashboard with key metrics.
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timedelta, timezone

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


# --- Configuration ---

def get_config():
    domain = os.getenv("FRESHSERVICE_DOMAIN")
    api_key = os.getenv("FRESHSERVICE_API_KEY")
    if not domain:
        print("ERROR: FRESHSERVICE_DOMAIN not set.")
        print("Add to .env: FRESHSERVICE_DOMAIN=yourcompany")
        sys.exit(1)
    if not api_key:
        print("ERROR: FRESHSERVICE_API_KEY not set.")
        print("Add to .env: FRESHSERVICE_API_KEY=your-key")
        print("Find your key at: FreshService → Profile → API Key")
        sys.exit(1)
    return {
        "base_url": f"https://{domain}.freshservice.com/api/v2",
        "auth": (api_key, "X"),
    }


# --- API Client ---

class FreshServiceClient:
    def __init__(self):
        config = get_config()
        self.base_url = config["base_url"]
        self.session = requests.Session()
        self.session.auth = config["auth"]
        self.session.headers.update({"Content-Type": "application/json"})

    def _request(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        for attempt in range(3):
            resp = self.session.get(url, params=params)
            if resp.status_code == 429:
                retry_after = int(resp.headers.get("Retry-After", 30))
                print(f"Rate limited. Retrying in {retry_after}s...", file=sys.stderr)
                time.sleep(retry_after)
                continue
            if resp.status_code == 401:
                print("ERROR: 401 Unauthorized — check your API key.")
                sys.exit(1)
            if resp.status_code == 404:
                print(f"ERROR: 404 Not found — {endpoint}")
                sys.exit(1)
            resp.raise_for_status()
            return resp.json()
        print("ERROR: Rate limit retries exhausted.")
        sys.exit(1)

    def _paginate(self, endpoint, params=None, key=None, limit=None):
        if params is None:
            params = {}
        params["per_page"] = 100
        params["page"] = 1
        all_items = []

        while True:
            data = self._request(endpoint, params)
            items = data.get(key) if key else data
            if isinstance(items, list):
                all_items.extend(items)
            else:
                return data

            if limit and len(all_items) >= limit:
                return all_items[:limit]

            if len(items) < 100:
                break
            params["page"] += 1

        return all_items

    # --- Tickets ---

    def list_tickets(self, since=None, query=None, limit=None):
        if query:
            params = {"query": f'"{query}"'}
            if since:
                params["query"] = f'"{query} AND updated_at:>\'{since}\'"'
            return self._paginate("/tickets/filter", params, "tickets", limit)
        else:
            params = {"include": "stats"}
            if since:
                params["updated_since"] = since + "T00:00:00Z"
            return self._paginate("/tickets", params, "tickets", limit)

    def get_ticket(self, ticket_id):
        return self._request(f"/tickets/{ticket_id}", {"include": "stats,conversations"})

    # --- Agents, Groups, Departments ---

    def list_agents(self, limit=None):
        return self._paginate("/agents", {}, "agents", limit)

    def list_groups(self, limit=None):
        return self._paginate("/groups", {}, "groups", limit)

    def list_departments(self, limit=None):
        return self._paginate("/departments", {}, "departments", limit)

    # --- Assets ---

    def list_assets(self, search=None, limit=None):
        params = {}
        if search:
            params["search"] = search
        return self._paginate("/assets", params, "assets", limit)

    # --- Problems & Changes ---

    def list_problems(self, limit=None):
        return self._paginate("/problems", {}, "problems", limit)

    def list_changes(self, limit=None):
        return self._paginate("/changes", {}, "changes", limit)

    # --- SLA Policies ---

    def list_sla_policies(self):
        return self._request("/sla_policies").get("sla_policies", [])

    # --- Dashboard ---

    def dashboard(self, since=None):
        tickets = self.list_tickets(since=since)
        groups = self.list_groups()
        problems = self.list_problems()
        changes = self.list_changes()

        group_map = {g["id"]: g["name"] for g in groups}

        # Status counts
        status_names = {2: "Open", 3: "Pending", 4: "Resolved", 5: "Closed"}
        status_counts = {}
        for name in status_names.values():
            status_counts[name] = 0
        for t in tickets:
            status = status_names.get(t.get("status"), "Other")
            status_counts[status] = status_counts.get(status, 0) + 1

        # Priority counts (open only)
        priority_names = {1: "Low", 2: "Medium", 3: "High", 4: "Urgent"}
        priority_counts = {}
        for t in tickets:
            if t.get("status") in (2, 3):  # Open or Pending
                pname = priority_names.get(t.get("priority"), "Unknown")
                priority_counts[pname] = priority_counts.get(pname, 0) + 1

        # SLA compliance
        sla_met = 0
        sla_total = 0
        fr_met = 0
        fr_total = 0
        for t in tickets:
            stats = t.get("stats", {})
            if stats:
                # Resolution SLA
                if t.get("due_by"):
                    sla_total += 1
                    if not t.get("is_escalated"):
                        sla_met += 1
                # First response SLA
                if t.get("fr_due_by"):
                    fr_total += 1
                    if not t.get("fr_escalated"):
                        fr_met += 1

        # Backlog aging (open + pending tickets)
        now = datetime.now(timezone.utc)
        aging = {"0-24h": 0, "1-3d": 0, "3-7d": 0, "7-30d": 0, "30d+": 0}
        for t in tickets:
            if t.get("status") not in (2, 3):
                continue
            created = t.get("created_at", "")
            if not created:
                continue
            try:
                created_dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
                age = (now - created_dt).total_seconds() / 86400
                if age < 1:
                    aging["0-24h"] += 1
                elif age < 3:
                    aging["1-3d"] += 1
                elif age < 7:
                    aging["3-7d"] += 1
                elif age < 30:
                    aging["7-30d"] += 1
                else:
                    aging["30d+"] += 1
            except (ValueError, TypeError):
                pass

        # By group
        group_stats = {}
        for t in tickets:
            gid = t.get("group_id")
            gname = group_map.get(gid, f"Group {gid}") if gid else "Unassigned"
            if gname not in group_stats:
                group_stats[gname] = {"total": 0, "open": 0}
            group_stats[gname]["total"] += 1
            if t.get("status") in (2, 3):
                group_stats[gname]["open"] += 1

        # Open problems and changes
        open_problems = [p for p in problems if p.get("status") not in (4, 5)]
        open_changes = [c for c in changes if c.get("status") not in (4, 5)]

        return {
            "total_tickets": len(tickets),
            "status": status_counts,
            "priority_open": priority_counts,
            "sla": {
                "resolution": {
                    "met": sla_met,
                    "total": sla_total,
                    "pct": round(sla_met / sla_total * 100, 1) if sla_total else None,
                },
                "first_response": {
                    "met": fr_met,
                    "total": fr_total,
                    "pct": round(fr_met / fr_total * 100, 1) if fr_total else None,
                },
            },
            "backlog_aging": aging,
            "by_group": group_stats,
            "open_problems": len(open_problems),
            "open_changes": len(open_changes),
        }


# --- Output Formatting ---

def format_table_tickets(tickets):
    if not tickets:
        print("No tickets found.")
        return
    print(f"{'ID':>7}  {'Status':<10} {'Priority':<10} {'Subject':<60} {'Created':<12}")
    print("-" * 105)
    status_map = {2: "Open", 3: "Pending", 4: "Resolved", 5: "Closed"}
    priority_map = {1: "Low", 2: "Medium", 3: "High", 4: "Urgent"}
    for t in tickets:
        tid = t.get("id", "")
        status = status_map.get(t.get("status"), str(t.get("status", "")))
        priority = priority_map.get(t.get("priority"), str(t.get("priority", "")))
        subject = (t.get("subject") or "")[:60]
        created = (t.get("created_at") or "")[:10]
        print(f"{tid:>7}  {status:<10} {priority:<10} {subject:<60} {created:<12}")
    print(f"\nTotal: {len(tickets)} tickets")


def format_table_simple(items, fields):
    if not items:
        print("No results found.")
        return
    header = "  ".join(f"{f['label']:<{f['width']}}" for f in fields)
    print(header)
    print("-" * len(header))
    for item in items:
        row = ""
        for f in fields:
            val = item.get(f["key"], "")
            if isinstance(val, bool):
                val = "Yes" if val else "No"
            val = str(val or "")[:f["width"]]
            row += f"{val:<{f['width']}}  "
        print(row)
    print(f"\nTotal: {len(items)}")


def format_dashboard(data):
    print("=" * 60)
    print("  FRESHSERVICE DASHBOARD")
    print("=" * 60)

    print(f"\nTotal tickets: {data['total_tickets']}")
    print("\n--- Ticket Status ---")
    for status, count in data["status"].items():
        print(f"  {status:<12} {count}")

    print("\n--- Open Tickets by Priority ---")
    for priority, count in data["priority_open"].items():
        bar = "█" * min(count, 40)
        print(f"  {priority:<10} {count:>5}  {bar}")

    print("\n--- SLA Compliance ---")
    sla = data["sla"]
    if sla["first_response"]["total"]:
        pct = sla["first_response"]["pct"]
        print(f"  First Response:  {pct}%  ({sla['first_response']['met']}/{sla['first_response']['total']})")
    else:
        print("  First Response:  No data")
    if sla["resolution"]["total"]:
        pct = sla["resolution"]["pct"]
        print(f"  Resolution:      {pct}%  ({sla['resolution']['met']}/{sla['resolution']['total']})")
    else:
        print("  Resolution:      No data")

    print("\n--- Backlog Aging (Open + Pending) ---")
    for bucket, count in data["backlog_aging"].items():
        bar = "█" * min(count, 40)
        print(f"  {bucket:<8} {count:>5}  {bar}")

    print("\n--- By Group ---")
    print(f"  {'Group':<30} {'Total':>7} {'Open':>7}")
    print(f"  {'-'*30} {'-'*7} {'-'*7}")
    for group, stats in sorted(data["by_group"].items(), key=lambda x: x[1]["total"], reverse=True):
        print(f"  {group:<30} {stats['total']:>7} {stats['open']:>7}")

    print(f"\n--- ITIL ---")
    print(f"  Open Problems: {data['open_problems']}")
    print(f"  Open Changes:  {data['open_changes']}")
    print("=" * 60)


# --- Date parsing ---

def parse_since(since_str):
    if not since_str:
        return None
    if since_str.endswith("d"):
        days = int(since_str[:-1])
        dt = datetime.now(timezone.utc) - timedelta(days=days)
        return dt.strftime("%Y-%m-%d")
    return since_str


# --- CLI ---

def main():
    parser = argparse.ArgumentParser(
        description="FreshService read-only API client for C-level reporting",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  tickets        List/filter tickets
  ticket <id>    Get single ticket details
  dashboard      C-level summary with computed metrics
  agents         List agents
  groups         List agent groups
  departments    List departments
  assets         List/search assets
  problems       List problems
  changes        List changes
  sla-policies   List SLA policies

Examples:
  python freshservice.py dashboard --since 30d
  python freshservice.py tickets --query "priority:4 AND status:2"
  python freshservice.py tickets --since 7d --limit 20
  python freshservice.py ticket 12345
  python freshservice.py assets --search "MacBook"

Environment:
  FRESHSERVICE_DOMAIN   Your FreshService subdomain (required)
  FRESHSERVICE_API_KEY  Your API key (required)
        """
    )
    parser.add_argument("command", help="Command to run")
    parser.add_argument("args", nargs="*", help="Command arguments (e.g., ticket ID)")
    parser.add_argument("--since", "-s", help="Time filter: 7d, 30d, 90d, or YYYY-MM-DD")
    parser.add_argument("--query", "-q", help="FreshService filter query (tickets only)")
    parser.add_argument("--limit", "-l", type=int, help="Max records to return")
    parser.add_argument("--format", "-f", choices=["table", "json", "summary"], default="table",
                        help="Output format (default: table)")
    parser.add_argument("--search", help="Search term (assets only)")

    args = parser.parse_args()
    client = FreshServiceClient()
    since = parse_since(args.since)

    if args.command == "tickets":
        tickets = client.list_tickets(since=since, query=args.query, limit=args.limit)
        if args.format == "json":
            print(json.dumps(tickets, indent=2, default=str))
        else:
            format_table_tickets(tickets)

    elif args.command == "ticket":
        if not args.args:
            print("ERROR: Ticket ID required. Usage: freshservice.py ticket <id>")
            sys.exit(1)
        data = client.get_ticket(args.args[0])
        print(json.dumps(data, indent=2, default=str))

    elif args.command == "dashboard":
        data = client.dashboard(since=since)
        if args.format == "json":
            print(json.dumps(data, indent=2, default=str))
        else:
            format_dashboard(data)

    elif args.command == "agents":
        agents = client.list_agents(limit=args.limit)
        if args.format == "json":
            print(json.dumps(agents, indent=2, default=str))
        else:
            format_table_simple(agents, [
                {"key": "id", "label": "ID", "width": 10},
                {"key": "first_name", "label": "First Name", "width": 15},
                {"key": "last_name", "label": "Last Name", "width": 15},
                {"key": "email", "label": "Email", "width": 35},
                {"key": "active", "label": "Active", "width": 6},
            ])

    elif args.command == "groups":
        groups = client.list_groups(limit=args.limit)
        if args.format == "json":
            print(json.dumps(groups, indent=2, default=str))
        else:
            format_table_simple(groups, [
                {"key": "id", "label": "ID", "width": 10},
                {"key": "name", "label": "Name", "width": 30},
                {"key": "description", "label": "Description", "width": 50},
            ])

    elif args.command == "departments":
        departments = client.list_departments(limit=args.limit)
        if args.format == "json":
            print(json.dumps(departments, indent=2, default=str))
        else:
            format_table_simple(departments, [
                {"key": "id", "label": "ID", "width": 10},
                {"key": "name", "label": "Name", "width": 30},
                {"key": "description", "label": "Description", "width": 50},
            ])

    elif args.command == "assets":
        assets = client.list_assets(search=args.search, limit=args.limit)
        if args.format == "json":
            print(json.dumps(assets, indent=2, default=str))
        else:
            format_table_simple(assets, [
                {"key": "display_id", "label": "ID", "width": 10},
                {"key": "name", "label": "Name", "width": 30},
                {"key": "asset_type_id", "label": "Type", "width": 10},
                {"key": "assigned_on", "label": "Assigned", "width": 12},
            ])

    elif args.command == "problems":
        problems = client.list_problems(limit=args.limit)
        if args.format == "json":
            print(json.dumps(problems, indent=2, default=str))
        else:
            format_table_simple(problems, [
                {"key": "id", "label": "ID", "width": 10},
                {"key": "subject", "label": "Subject", "width": 50},
                {"key": "status", "label": "Status", "width": 10},
                {"key": "priority", "label": "Priority", "width": 10},
            ])

    elif args.command == "changes":
        changes = client.list_changes(limit=args.limit)
        if args.format == "json":
            print(json.dumps(changes, indent=2, default=str))
        else:
            format_table_simple(changes, [
                {"key": "id", "label": "ID", "width": 10},
                {"key": "subject", "label": "Subject", "width": 50},
                {"key": "status", "label": "Status", "width": 10},
                {"key": "priority", "label": "Priority", "width": 10},
            ])

    elif args.command in ("sla-policies", "sla_policies", "sla"):
        policies = client.list_sla_policies()
        if args.format == "json":
            print(json.dumps(policies, indent=2, default=str))
        else:
            format_table_simple(policies, [
                {"key": "id", "label": "ID", "width": 10},
                {"key": "name", "label": "Name", "width": 30},
                {"key": "description", "label": "Description", "width": 50},
                {"key": "is_default", "label": "Default", "width": 8},
            ])

    else:
        print(f"ERROR: Unknown command '{args.command}'")
        print("Available: tickets, ticket, dashboard, agents, groups, departments, assets, problems, changes, sla-policies")
        sys.exit(1)


if __name__ == "__main__":
    main()
