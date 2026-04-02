# Fortnox Finance Integration — Research Notes

> Status: **Parked** — research complete, implementation deferred
> Date: 2026-04-02

## Summary

Fortnox integration is feasible but more complex than other API skills due to OAuth2 token management and multi-company architecture. Keeping this research for future implementation.

## Key Findings

### API
- Base URL: `https://api.fortnox.se/3/`
- Auth: OAuth2 Authorization Code flow
- Access tokens expire every 1 hour, refresh tokens every 45 days
- Rate limit: 300 req/min per company
- No built-in P&L/balance sheet endpoints — use SIE4 export or aggregate vouchers

### Multi-Company
- Each restaurant company = separate Fortnox tenant
- Each needs its own OAuth consent flow + token pair
- One registered app (client_id/client_secret) can serve all companies
- Need a token store (encrypted JSON or DB) mapping company → tokens

### Read-Only Endpoints Available
- Invoices, supplier invoices
- Accounts, chart of accounts
- Cost centers, projects
- Vouchers / journal entries
- SIE4 file export (for P&L, balance sheet)
- Company information
- Customers, suppliers

### Scopes Needed
`invoice supplierinvoice bookkeeping costcenter project companyinformation customer supplier settings`

Note: Fortnox has no read-only scopes — must enforce GET-only in code.

### Proposed Architecture
- `fortnox.py` — main CLI (read-only)
- `fortnox_auth.py` — OAuth setup helper (one-time per company)
- `tokens.json` — encrypted token store (gitignored)
- Dashboard command aggregating across all companies

### Integration Points
- budget-tracker: compare actuals vs budget
- stakeholder-briefing: real financial data in board updates
- meeting-prep: financial context for meetings
- project-portfolio: actual project costs from Fortnox

## Prerequisites Before Implementation
1. Register a Fortnox app in Developer Portal
2. Decide on token storage approach
3. Determine which companies to connect
4. Decide if dashboard should compare restaurants against each other
