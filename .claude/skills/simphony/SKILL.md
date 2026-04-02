---
name: simphony
description: Use when the user needs restaurant POS data — sales, revenue, guest checks, product mix, labor, payments, discounts, voids, or multi-location performance from Oracle Simphony. Read-only access via the BI API.
---

# Oracle Simphony BI API

Read-only access to Oracle Simphony restaurant data for C-level reporting and analysis. Pulls sales, labor, product mix, payments, and guest checks across multiple restaurant locations.

## Requirements

1. **Python packages**:
   ```bash
   pip install requests python-dotenv
   ```

2. **API account**: Created in R&A Back Office (Administration → System → API Accounts)
   - Type: **Business Intelligence API**
   - Permissions: Sales & Operations, Employee Performance, Labor, Cash Management

3. **Environment variables** in `.env`:
   ```bash
   SIMPHONY_HOST=https://yourdomain.oracleindustry.com
   SIMPHONY_AUTH_HOST=https://yourdomain-idm.oracleindustry.com
   SIMPHONY_CLIENT_ID=your-client-id
   SIMPHONY_USERNAME=your-api-username
   SIMPHONY_PASSWORD=your-api-password
   SIMPHONY_ORG=your-org-short-name
   ```

4. **First-time authentication**:
   ```bash
   python .claude/skills/simphony/scripts/simphony_auth.py setup
   ```
   Tokens are saved locally and auto-refresh (valid 14 days, refresh up to 28 days).

## Commands

### Authentication

```bash
# First-time setup (or when tokens expire)
python .claude/skills/simphony/scripts/simphony_auth.py setup

# Check token status
python .claude/skills/simphony/scripts/simphony_auth.py status

# Manually refresh tokens
python .claude/skills/simphony/scripts/simphony_auth.py refresh
```

### Dashboard (Enterprise-Wide)

```bash
# Today's dashboard across all locations
python .claude/skills/simphony/scripts/simphony.py dashboard

# Dashboard for a specific date
python .claude/skills/simphony/scripts/simphony.py dashboard --date 2026-04-01

# JSON output
python .claude/skills/simphony/scripts/simphony.py dashboard --date 2026-04-01 --format json
```

Shows: net sales per location, checks, guests, avg check, discounts, voids, enterprise totals, and anomaly flags.

### Sales

```bash
# Today's sales for a location
python .claude/skills/simphony/scripts/simphony.py sales --location 1234

# Specific date
python .claude/skills/simphony/scripts/simphony.py sales --location 1234 --date 2026-04-01

# Date range (last 7 days)
python .claude/skills/simphony/scripts/simphony.py sales --location 1234 --since 7d
```

Shows: net sales, tax, checks, guests, avg check, discounts, voids — broken down by revenue center.

### Product Mix

```bash
python .claude/skills/simphony/scripts/simphony.py pmix --location 1234 --date 2026-04-01
```

Shows: menu item sales totals — what's selling, how much.

### Labor

```bash
python .claude/skills/simphony/scripts/simphony.py labor --location 1234 --date 2026-04-01
```

Shows: time card details — clock in/out, hours worked.

### Payments

```bash
python .claude/skills/simphony/scripts/simphony.py payments --location 1234 --date 2026-04-01
```

Shows: payment method breakdown (cash, card, etc.).

### Discounts & Voids

```bash
python .claude/skills/simphony/scripts/simphony.py discounts --location 1234 --date 2026-04-01
```

### Employee Performance

```bash
python .claude/skills/simphony/scripts/simphony.py employees --location 1234 --date 2026-04-01
```

### Guest Checks

```bash
python .claude/skills/simphony/scripts/simphony.py checks --location 1234 --date 2026-04-01
```

### Locations

```bash
python .claude/skills/simphony/scripts/simphony.py locations
```

Lists all restaurant locations with reference numbers. Use the location reference in other commands.

## Use Cases for C-Levels

| Question | Command |
|----------|---------|
| "How did all restaurants do yesterday?" | `dashboard --date 2026-04-01` |
| "Show me sales for Kungsholmen last week" | `sales --location 1234 --since 7d` |
| "What's our best-selling item?" | `pmix --location 1234 --date 2026-04-01` |
| "Are we overstaffed on Mondays?" | `labor --location 1234 --date 2026-03-31` |
| "Any unusual void patterns?" | `dashboard` (check void flags) |
| "How do our locations compare?" | `dashboard` (cross-location comparison) |
| "Cash vs card split?" | `payments --location 1234 --date 2026-04-01` |
| "Pull restaurant data for the board update" | `dashboard --format json` → feed into stakeholder-briefing |

## Integration with Other Skills

- **stakeholder-briefing**: Include restaurant KPIs in board updates and management reports
- **meeting-prep**: Pull sales and labor data before steering committees
- **budget-tracker**: Compare actual restaurant revenue against budgets
- **local-marketing**: Measure marketing impact — compare sales before/after campaigns by location
- **project-portfolio**: Correlate technology projects with restaurant performance changes
- **freshservice**: Cross-reference IT issues with POS downtime or sales dips

## Token Management

| Token | Lifetime | Auto-refresh |
|-------|----------|-------------|
| id_token | 14 days | Yes — refreshes when >10 days old |
| refresh_token | 28 days | Used to get new id_token |
| Password | 60 days | Must be reset manually in R&A |

The script auto-refreshes tokens when they're aging. If both tokens expire, run `simphony_auth.py setup` again.

## Troubleshooting

**"SIMPHONY_HOST not set"**
- Add all 6 environment variables to `.env`. See Requirements above.

**"401 Unauthorized"**
- Token expired. Run: `python .claude/skills/simphony/scripts/simphony_auth.py setup`

**"400 Bad Request"**
- Check `locRef` — use `locations` command to find valid location references.
- Check date format — must be `YYYY-MM-DD`.

**"No data returned"**
- The location may have no transactions for that date.
- Check that the API account has the correct data access permissions.

**"Token aging — refreshing..."**
- Normal. The script auto-refreshes tokens older than 10 days.

**Password expired (60 days)**
- Reset the API account password in R&A Back Office, update `.env`, run `setup` again.
