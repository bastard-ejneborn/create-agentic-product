# Oracle Simphony Cloud — Integration Research

> Status: **Parked** — research complete, waiting for OHIP API access
> Date: 2026-04-02

## Summary

Oracle Simphony Cloud has comprehensive REST APIs via OHIP (Oracle Hospitality Integration Platform). Rich data available: sales, labor, product mix, menu, locations. Implementation blocked on getting developer portal access and sandbox credentials from Oracle.

## Next Steps to Unblock

1. Contact Oracle Hospitality account rep
2. Request OHIP developer access and sandbox environment
3. Get full Swagger/OpenAPI specs
4. Get client_id / client_secret for development
5. Then build the skill (Python CLI, read-only, like FreshService)

## Key Findings

### API
- Gateway: Oracle Hospitality Integration Platform (OHIP)
- Base URL: `https://hospitality-api.oracle.com/` (environment-specific)
- Simphony endpoints under: `/sim/v1/`
- Auth: OAuth 2.0 Client Credentials flow
- Bearer tokens, 1 hour expiry
- Rate limit: ~60-120 req/min (negotiable for enterprise)

### Multi-Location
Native enterprise hierarchy — designed for chains:
```
Enterprise (entire organization)
  └── Properties (individual restaurants)
        └── Revenue Centers (bar, dining, takeout)
              └── Order Types (dine-in, delivery, etc.)
```
All API calls are scoped — can query single location or aggregate across enterprise.

### Available Data (Read-Only)

| Data | Endpoint | Detail Level |
|------|----------|-------------|
| Sales/transactions | checks, check details | Line items, modifiers, payments, taxes, tips |
| Revenue reports | SRA / aggregated endpoints | Daily/weekly/monthly, by location/revenue center |
| Product mix (PMIX) | menu items + check data | Which items sell, when, where |
| Labor | employees, time entries | Clock in/out, hours, labor cost %, server performance |
| Menu items | menu items, classes, masters | Full hierarchy, prices, condiments, combos |
| Discounts/voids/comps | in check detail | Reason codes, manager authorization |
| Locations | organizations, properties, revenue centers | Full config, address, timezone |
| Inventory | limited | Basic only; most use third-party (MarketMan, CrunchTime) |

### Reporting

- **Simphony Reporting & Analytics (SRA)**: Built-in dashboards — sales summary, labor, PMIX, financial, speed of service
- **InMotion Mobile**: Manager app for KPIs on the go
- **Oracle Analytics Cloud**: Full BI platform, Simphony data can flow there
- **Exports**: Scheduled CSV/XML exports available

### MCP Server

Does not exist (no Oracle or community MCP server). Would need custom build wrapping the REST APIs.

### Cost

- Base API access included with Simphony Cloud subscription (~$55-155/workstation/month)
- SRA and Oracle Analytics may be add-on modules
- OHIP access may require partner agreement
- No per-API-call pricing

### Third-Party Middleware Options

| Platform | What It Does |
|----------|-------------|
| CrunchTime / Mirus | Aggregates Simphony data for reporting |
| Restaurant365 | Accounting + operations with Simphony integration |
| MarketMan / xtraCHEF | Inventory management with Simphony connectors |
| Oracle Integration Cloud (OIC) | Oracle's own iPaaS with Simphony adapters |
| MuleSoft / Workato / Boomi | iPaaS platforms connecting to Simphony REST APIs |

### Proposed Skill Architecture (when ready)

```
.claude/skills/simphony/
  SKILL.md                  ← Documentation
  scripts/
    simphony.py             ← Main CLI (read-only GET only)
```

Commands:
- `dashboard` — Revenue, labor cost %, product mix highlights across all locations
- `sales --property "Location Name" --since 7d` — Sales data by location
- `labor --property "Location Name"` — Labor hours, cost, scheduling
- `pmix --property "Location Name" --since 30d` — Product mix report
- `checks --property "Location Name" --since 1d` — Recent transactions
- `locations` — List all properties and revenue centers
- `menu` — Menu items and pricing

### Integration with Existing Skills

- **budget-tracker**: Compare restaurant revenue/costs against IT/digital budget
- **stakeholder-briefing**: Include restaurant performance in board updates
- **meeting-prep**: Pull sales and labor data for management meetings
- **project-portfolio**: Correlate technology projects with restaurant performance
- **local-marketing**: Measure marketing impact on sales by location
- **freshservice**: Cross-reference IT issues with POS downtime impact
