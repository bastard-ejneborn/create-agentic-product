---
name: freshservice
description: Use when the user needs helpdesk data, IT support metrics, ticket reports, SLA compliance, agent performance, asset inventory, or change/problem tracking from FreshService. Read-only access.
---

# FreshService Integration

Read-only access to FreshService ITSM data for C-level reporting and analysis.

## Requirements

1. **Python packages**:
   ```bash
   pip install requests python-dotenv
   ```

2. **Environment variables** in `.env`:
   ```bash
   FRESHSERVICE_DOMAIN=yourcompany          # yourcompany.freshservice.com
   FRESHSERVICE_API_KEY=your-api-key-here   # From Profile > API Key
   ```

   Get your API key: Log into FreshService → Profile picture → Profile Settings → Your API Key

## Commands

### Tickets

```bash
# List recent tickets
python .claude/skills/freshservice/scripts/freshservice.py tickets

# Filter tickets with FreshService query language
python .claude/skills/freshservice/scripts/freshservice.py tickets --query "priority:4 AND status:2"

# Tickets updated in last 7 days
python .claude/skills/freshservice/scripts/freshservice.py tickets --since 7d

# Tickets updated since specific date
python .claude/skills/freshservice/scripts/freshservice.py tickets --since 2026-01-01

# Limit results
python .claude/skills/freshservice/scripts/freshservice.py tickets --limit 50

# Get single ticket with details
python .claude/skills/freshservice/scripts/freshservice.py ticket 12345
```

**Query language examples**:
- `"priority:4"` — Urgent tickets
- `"status:2 AND group_id:3"` — Open tickets in group 3
- `"created_at:>'2026-01-01' AND type:'Incident'"` — Incidents since Jan 1
- `"tag:'VPN' OR tag:'Network'"` — Tickets tagged VPN or Network

**Priority values**: 1=Low, 2=Medium, 3=High, 4=Urgent

**Status values**: 2=Open, 3=Pending, 4=Resolved, 5=Closed

### Dashboard (C-Level Summary)

```bash
# Full dashboard — ticket volume, SLA, backlog, performance
python .claude/skills/freshservice/scripts/freshservice.py dashboard

# Dashboard for specific period
python .claude/skills/freshservice/scripts/freshservice.py dashboard --since 30d

# Dashboard as JSON (for further processing)
python .claude/skills/freshservice/scripts/freshservice.py dashboard --format json
```

Dashboard includes:
- **Ticket volume**: open, pending, resolved, closed counts
- **SLA compliance**: first response and resolution SLA % met
- **Backlog aging**: distribution by age (0-24h, 1-3d, 3-7d, 7-30d, 30d+)
- **By priority**: breakdown of open tickets by priority
- **By group**: ticket count and avg resolution time per group
- **Changes & problems**: open count and recent activity

### Agents & Groups

```bash
# List all agents
python .claude/skills/freshservice/scripts/freshservice.py agents

# List agent groups
python .claude/skills/freshservice/scripts/freshservice.py groups

# List departments
python .claude/skills/freshservice/scripts/freshservice.py departments
```

### Assets

```bash
# List all assets
python .claude/skills/freshservice/scripts/freshservice.py assets

# Search assets
python .claude/skills/freshservice/scripts/freshservice.py assets --search "MacBook"
```

### Problems & Changes

```bash
# List open problems
python .claude/skills/freshservice/scripts/freshservice.py problems

# List open changes
python .claude/skills/freshservice/scripts/freshservice.py changes
```

### SLA Policies

```bash
# List all SLA policies with targets
python .claude/skills/freshservice/scripts/freshservice.py sla-policies
```

## Script Arguments

| Argument | Short | Description |
|----------|-------|-------------|
| `--since` | `-s` | Time filter: `7d`, `30d`, `90d`, or `YYYY-MM-DD` |
| `--query` | `-q` | FreshService filter query (tickets only) |
| `--limit` | `-l` | Max records to return (default: all) |
| `--format` | `-f` | Output format: `table` (default), `json`, `summary` |
| `--search` | | Search term (assets only) |

## Use Cases for C-Levels

| Question | Command |
|----------|---------|
| "How's our helpdesk doing?" | `dashboard` |
| "Are we meeting SLAs?" | `dashboard` (check SLA section) |
| "What's our ticket backlog?" | `dashboard` (check backlog section) |
| "Show me all urgent open tickets" | `tickets --query "priority:4 AND status:2"` |
| "Which team has the most tickets?" | `dashboard` (check by-group section) |
| "What hardware assets do we have?" | `assets` |
| "Any open problems or changes?" | `problems` / `changes` |
| "Show me last month's ticket data" | `tickets --since 30d` |

## Integration with Other Skills

- **stakeholder-briefing**: Include helpdesk KPIs in board updates
- **meeting-prep**: Pull IT support stats before steering committees
- **risk-register**: Flag SLA breach trends as operational risk
- **budget-tracker**: Reference support costs when evaluating vendor changes
- **vendor-manager**: Correlate vendor issues with ticket volume

## Troubleshooting

**"FRESHSERVICE_DOMAIN not set"**
- Add `FRESHSERVICE_DOMAIN=yourcompany` to `.env` (just the subdomain, not the full URL)

**"FRESHSERVICE_API_KEY not set"**
- Add your API key to `.env`. Find it at Profile Settings in FreshService.

**"401 Unauthorized"**
- Check that your API key is correct and active
- Ensure the account has read permissions

**"429 Too Many Requests"**
- The script handles rate limits automatically with retry
- If persistent, you may be on a lower-tier plan (40 req/min)

**"No data returned"**
- Check your query syntax — field names and values are case-sensitive
- Verify the date format in `--since` (YYYY-MM-DD or Nd)
