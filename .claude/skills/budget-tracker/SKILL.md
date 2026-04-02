---
name: budget-tracker
description: Use when the user wants to define, update, or reference IT/digital/tech budgets, analyze spending, check available funds for new initiatives, or when agents need budget context for recommendations.
---

# Budget Tracker

Capture and maintain a structured view of IT/digital/tech budgets so agents can ground financial recommendations in actual numbers.

## Two Input Paths

### Interview Mode

When building a budget overview from scratch:

1. **Fiscal period**: What's the budget year/period? When does it reset?
2. **Total budget**: What's the overall IT/digital/tech budget?
3. **Categories**: Break down by category (see standard categories below)
4. **Committed vs. discretionary**: Which costs are locked in (contracts, salaries) vs. flexible?
5. **Actuals**: How much has been spent so far this period?
6. **Forecast**: Any expected changes (new hires, contract renewals, planned projects)?

Ask one topic at a time. Summarize each answer before moving on.

### Import Mode

When the user has existing budget data (spreadsheets, finance reports):

1. Read the provided data
2. Map to the standard format below
3. Identify gaps — which categories are missing or unclear?
4. Ask follow-up questions to fill gaps
5. Present the structured result for approval

## Standard Categories

| Category | Includes |
|----------|---------|
| **Infrastructure** | Cloud hosting, on-prem hardware, networking, data centers |
| **Licensing & SaaS** | Software licenses, SaaS subscriptions, platform fees |
| **Personnel** | Salaries, contractors, consultants, training |
| **Services** | Managed services, support contracts, outsourcing |
| **Projects** | Dedicated project budgets (cross-reference with project-portfolio) |
| **Security** | Security tools, audits, compliance, certifications |
| **Innovation / R&D** | Experimentation, prototyping, technology evaluation |
| **Other** | Miscellaneous, contingency, reserves |

Adapt categories to the organization. Not all categories apply to every company.

## Output Format

Save to `docs/finance/budget.md`:

```markdown
# IT/Digital/Tech Budget
> Fiscal period: [YYYY or YYYY-Qn] | Last updated: YYYY-MM-DD
> Currency: [SEK/EUR/USD/etc.]

## Summary

| | Allocated | Committed | Spent | Remaining | % Used |
|---|----------|-----------|-------|-----------|--------|
| **Total** | | | | | |

## Budget by Category

### Infrastructure
| Item | Annual Cost | Type | Notes |
|------|------------|------|-------|
| [e.g., AWS] | [amount] | Committed | [contract until date] |

**Subtotal**: [amount] allocated | [amount] spent | [amount] remaining

### Licensing & SaaS
| Item | Annual Cost | Type | Renewal Date | Notes |
|------|------------|------|-------------|-------|

**Subtotal**: [amount] allocated | [amount] spent | [amount] remaining

### Personnel
| Role/Team | Headcount | Annual Cost | Type | Notes |
|-----------|----------|------------|------|-------|

**Subtotal**: [amount] allocated | [amount] spent | [amount] remaining

### Projects
| Project | Budget | Spent | Status | Link |
|---------|--------|-------|--------|------|
| [name] | [amount] | [amount] | On track | [docs/decisions/ or project-portfolio ref] |

**Subtotal**: [amount] allocated | [amount] spent | [amount] remaining

[Repeat for remaining categories as applicable]

## Committed vs. Discretionary

| Type | Amount | % of Total |
|------|--------|-----------|
| **Committed** (contracts, salaries, locked) | | |
| **Discretionary** (can be reallocated) | | |
| **Unallocated** (available for new initiatives) | | |

## Upcoming Changes
| Date | Change | Impact | Notes |
|------|--------|--------|-------|
| [date] | [e.g., contract renewal] | [+/- amount] | |

## Notes & Assumptions
- [Any caveats, exchange rate assumptions, or pending approvals]
```

## Updates

Support incremental updates:
- "Update: we spent 50k on the new monitoring tool" — update the relevant category
- "Add a new project budget of 200k for platform migration" — add to Projects
- Always update `Last updated` date and recalculate totals
- Flag when remaining budget drops below 20% in any category
- Flag when a spending item doesn't align with strategic priorities

## How Agents Use This

Before making financial recommendations, agents should:
1. Check if `docs/finance/budget.md` exists
2. Read it to understand available budget and constraints
3. Reference specific numbers when recommending investments
4. Flag when a recommendation would exceed available budget
5. Suggest reallocation options when budget is tight
6. Cross-reference with `docs/strategy/company-strategy.md` for priority alignment

## Alerts

Flag these situations proactively:
- **Over budget**: Category spend exceeds allocation
- **Low runway**: Less than 20% remaining in a category with months left in the period
- **Uncommitted renewals**: Contracts approaching renewal without a decision
- **Misalignment**: Spending pattern doesn't match strategic priorities
- **Hidden costs**: Identify costs that may be growing unnoticed (SaaS sprawl, cloud waste)
