---
name: vendor-manager
description: Use when the user wants to track vendor contracts, review SLA performance, prepare for renewals, assess vendor consolidation, or when agents need vendor context for technology and budget decisions.
---

# Vendor Manager

Track vendor relationships, contracts, and performance so agents can factor in existing commitments and upcoming renewals when advising.

## Two Input Paths

### Interview Mode

1. **Active vendors**: List your current technology vendors/SaaS tools
2. For each vendor, capture:
   - What do they provide?
   - Contract value (annual)
   - Contract dates (start, end, renewal)
   - Payment terms (monthly/annual, auto-renew?)
   - Key SLAs and their current performance
   - Satisfaction level (1-5)
   - Lock-in risk (low/medium/high)
   - Who manages the relationship?
3. **Upcoming renewals**: Anything coming up in the next 90 days?
4. **Pain points**: Any vendors you're unhappy with? Considering switching?

### Import Mode

If the user has existing vendor data (spreadsheets, procurement systems):
1. Read and map to standard format
2. Identify gaps
3. Ask follow-up questions

## Output Format

Save to `docs/vendors/vendor-register.md`:

```markdown
# Vendor Register
> Last updated: YYYY-MM-DD
> Total vendors: [n] | Annual spend: [total]
> Upcoming renewals (90 days): [n]

## Spend Summary

| Category | Vendor Count | Annual Spend | % of Total |
|----------|-------------|-------------|-----------|
| Infrastructure / Cloud | | | |
| SaaS / Licensing | | | |
| Security | | | |
| Services / Consulting | | | |
| Development Tools | | | |
| Other | | | |

## Upcoming Renewals

| Vendor | Product | Renewal Date | Annual Cost | Action Needed | Owner |
|--------|---------|-------------|------------|--------------|-------|
| [name] | [product] | [date] | [cost] | Review / Renew / Cancel | [who] |

## Vendor Details

### [Vendor Name]
> Category: [category] | Status: Active
> Annual cost: [amount] | Contract: [start] — [end]
> Auto-renew: Yes/No | Notice period: [days]
> Owner: [person/team] | Satisfaction: [1-5 stars]

**What they provide**: [Description of services/products used]

**Contract terms**:
- Payment: [Monthly/Annual/Multi-year]
- Commitment: [Amount or minimum]
- Exit terms: [Notice period, penalties, data export]

**SLAs**:
| SLA | Target | Actual | Status |
|-----|--------|--------|--------|
| Uptime | 99.9% | [actual] | Met / Missed |
| Response time | [target] | [actual] | Met / Missed |

**Lock-in assessment**:
- Data portability: [Easy/Moderate/Difficult]
- Integration depth: [Low/Medium/High]
- Switching cost estimate: [Low/Medium/High]
- Alternatives considered: [list]

**Notes**: [History, issues, escalations, relationship quality]

---

[Repeat for each vendor]

## Vendor Overlap Analysis
| Capability | Vendors Providing It | Consolidation Opportunity? |
|-----------|---------------------|--------------------------|
| [capability] | [vendor A, vendor B] | [Yes/No — rationale] |
```

## Updates

- "We signed a new contract with Datadog" — add vendor entry
- "Our AWS contract renews next month" — flag and update renewal status
- "Slack uptime has been terrible" — update SLA actuals and satisfaction
- Always update `Last updated`, spend summary, and renewal list

## How Agents Use This

Before making technology or budget recommendations, agents should:
1. Check if `docs/vendors/vendor-register.md` exists
2. Check for overlapping vendors before recommending new tools
3. Factor in contract commitments when discussing budget changes
4. Flag upcoming renewals as decision points
5. Reference vendor lock-in when evaluating alternatives
6. Cross-reference with budget-tracker for spend validation
7. Cross-reference with risk-register for vendor-related risks

## Alerts

- **Renewal approaching**: 90, 60, and 30 days before contract end
- **Auto-renew warning**: Contracts with auto-renew approaching notice deadline
- **SLA violations**: When actual performance misses SLA targets
- **Spend concentration**: Single vendor representing >30% of total vendor spend
- **Satisfaction drops**: Vendor satisfaction below 3/5
- **Orphaned vendors**: Active contracts without an assigned relationship owner
- **Overlap detected**: Multiple vendors providing the same capability
