---
name: operations-dashboard
description: Use when tracking restaurant operations performance, reviewing KPIs across locations, managing the operations hierarchy (COO → Regional Managers → District Managers → Restaurant Managers), analyzing operational issues, or preparing operations reviews.
---

# Operations Dashboard

Track and analyze QSR restaurant operations across the full management hierarchy. Provides the COO, Regional Managers, and District Managers with structured views of performance, issues, and action items at every level.

## Operations Hierarchy

```
COO (Chief Operations Officer)
  └── Regional Manager (2 regions)
        └── District Manager (multiple per region)
              └── Restaurant Manager (multiple per district)
                    └── Restaurant (individual location)
```

## Setup

### Define the Hierarchy

Save to `docs/operations/hierarchy.md`:

```markdown
# Operations Hierarchy
> Last updated: YYYY-MM-DD

## Structure

### Region: [Region Name]
> Regional Manager: [name]

#### District: [District Name]
> District Manager: [name]

| Restaurant | Location | Manager | Status |
|-----------|----------|---------|--------|
| [name] | [city/area] | [name] | Open / Renovating / Closing |
| [name] | [city/area] | [name] | Open |

#### District: [District Name]
> District Manager: [name]

| Restaurant | Location | Manager | Status |
|-----------|----------|---------|--------|
| [name] | [city/area] | [name] | Open |

---

### Region: [Region Name]
> Regional Manager: [name]

[Same structure]
```

## KPIs by Level

### COO Level — Enterprise Operations Overview

| KPI | Description | Target | Source |
|-----|------------|--------|--------|
| Total revenue | All locations combined | Per strategy | Simphony |
| EBITDA margin | Profitability across chain | 23.5% (long-term) | Finance |
| Same-store sales growth | YoY comparison per location | Positive | Simphony |
| Guest count trend | Total guests across chain | Growing | Simphony |
| Average check | Enterprise-wide | Growing | Simphony |
| Food cost % | Cost of goods / revenue | Target TBD | Operations |
| Labor cost % | Labor / revenue | Target TBD | Simphony + Finance |
| Speed of service | Avg time from order to handoff | Target TBD | Simphony/KDS |
| Guest satisfaction | Complaint rate, CSAT, NPS | Improving | Guest support |
| FreshService SLA | IT support responsiveness | Per SLA targets | FreshService |
| Employee turnover | Staff retention rate | Decreasing | HR |
| Locations at risk | Restaurants flagged for performance | 0 | Operations |

### Regional Manager Level — Regional Performance

| KPI | Description |
|-----|------------|
| Revenue per restaurant (region avg) | Compared to enterprise avg |
| Underperforming locations | Restaurants below target |
| District Manager performance | Aggregate of their districts |
| Regional labor cost % | Compared to enterprise target |
| Regional food cost % | Compared to enterprise target |
| Guest complaints per location (region) | Compared to enterprise avg |
| New openings / closings in region | Portfolio changes |

### District Manager Level — District Operations

| KPI | Description |
|-----|------------|
| Revenue per restaurant (district avg) | Compared to region and enterprise avg |
| Restaurant-level scorecards | Individual location performance |
| Staff scheduling compliance | Proper coverage vs plan |
| Food safety audit results | Per restaurant |
| Mystery shopper scores | Per restaurant |
| Training completion | Staff certification status |
| Maintenance issues | Open work orders per restaurant |
| Local marketing activity | Activities completed vs planned |

### Restaurant Manager Level — Individual Location

| KPI | Description |
|-----|------------|
| Daily/weekly sales | Actual vs target |
| Labor vs revenue | Shift-level efficiency |
| Food waste | Tracked via POS waste reports |
| Speed of service | Order-to-handoff time |
| Guest complaints | Tickets for this location |
| Staff attendance | Call-outs, no-shows |
| Food safety compliance | Daily checklists |
| Inventory accuracy | Actual vs theoretical |

## Operations Review Templates

### Weekly COO Review

```markdown
# COO Weekly Operations Review
> Week of: YYYY-MM-DD | Prepared by: [name]

## Enterprise Summary
| Metric | This Week | Last Week | Trend | Target |
|--------|----------|-----------|-------|--------|
| Total revenue | | | | |
| Guest count | | | | |
| Average check | | | | |
| Labor cost % | | | | |
| Food cost % | | | | |

## By Region
| Region | Revenue | Guests | Avg Check | Labor % | Flags |
|--------|---------|--------|-----------|---------|-------|
| [Region A] | | | | | |
| [Region B] | | | | | |

## Locations at Risk
| Restaurant | District | Issue | Action | Owner |
|-----------|----------|-------|--------|-------|

## Key Decisions Needed
- [Decision with context]

## Guest Support Summary
- Total tickets: [n] | Trend: [up/down]
- Top issue: [category]
- Locations with most complaints: [list]

## Action Items from Last Week
| Action | Owner | Status |
|--------|-------|--------|
```

### Weekly District Manager Review

```markdown
# District Review: [District Name]
> Week of: YYYY-MM-DD | DM: [name]

## District Summary
| Metric | This Week | Last Week | Trend |
|--------|----------|-----------|-------|

## By Restaurant
| Restaurant | Revenue | Guests | Avg Check | Labor % | Issues |
|-----------|---------|--------|-----------|---------|--------|

## Store Visits This Week
| Restaurant | Date | Focus | Findings | Actions |
|-----------|------|-------|----------|---------|

## Staff Issues
- [Scheduling gaps, call-outs, training needs]

## Maintenance / Facility
- [Open work orders, equipment issues]

## Action Items
| Action | Restaurant | Owner | Due |
|--------|-----------|-------|-----|
```

### Monthly Regional Review

```markdown
# Regional Review: [Region Name]
> Month: YYYY-MM | RM: [name]

## Regional Performance vs Target
| Metric | Actual | Target | Variance |
|--------|--------|--------|----------|

## District Comparison
| District | DM | Revenue | Guests | Labor % | Food % | Score |
|----------|----|---------|---------|---------|---------|----|

## Top 3 Performers
1. [Restaurant] — why it's working

## Bottom 3 — Action Plans
1. [Restaurant] — issue and plan

## Portfolio Updates
- New openings: [list]
- Closings/changes: [list]

## People
- Turnover rate: [%]
- Open positions: [n]
- Training completion: [%]

## Recommendations to COO
- [What needs escalation or decision]
```

## Store Visit Log

District Managers track their restaurant visits:

Save to `docs/operations/visits/YYYY-MM-DD-{restaurant}-visit.md`:

```markdown
# Store Visit: [Restaurant Name]
> Date: YYYY-MM-DD | Visited by: [DM name]
> Type: Routine / Follow-up / Audit / Support

## Observations
### Positives
- [What's working well]

### Issues Found
| Issue | Severity | Action | Owner | Due |
|-------|----------|--------|-------|-----|
| [issue] | High/Medium/Low | [what to do] | [who] | [when] |

## Checklist
- [ ] Food safety standards met
- [ ] Cleanliness acceptable
- [ ] Staff in proper uniform
- [ ] Equipment functioning
- [ ] Speed of service acceptable
- [ ] Guest experience positive
- [ ] Menu items available (no 86'd items)
- [ ] Marketing materials current

## Discussion with Manager
- [Key topics discussed, manager's concerns, support needed]

## Follow-Up
- Next visit: [date]
- Open items from previous visit: [status]
```

## Integration with Other Skills

- **simphony**: Pull actual sales, labor, guest count, product mix data per location
- **freshservice**: IT issues affecting restaurant operations (POS down, network issues)
- **guest-support**: Guest complaints per location — operational quality signal
- **budget-tracker**: Actual costs vs budget per location/region
- **team-structure**: Staff levels, key person risks per location
- **risk-register**: Operational risks (food safety, equipment failure, staffing)
- **local-marketing**: Marketing activities and their impact on traffic per location
- **company-policies**: Operations policies (food safety, hygiene, opening/closing)
- **stakeholder-briefing**: Include operations KPIs in board/management updates
- **meeting-prep**: Pull operations data for weekly/monthly reviews
- **project-portfolio**: Track operations improvement projects
- **vendor-manager**: Equipment vendors, food suppliers, service contracts

## Workflow

1. **Set up hierarchy**: Define regions, districts, restaurants, and managers
2. **Connect data**: Simphony for sales/labor, FreshService for IT, guest-support for complaints
3. **Weekly rhythm**: District reviews, COO summary, action tracking
4. **Monthly rhythm**: Regional reviews, performance comparisons, portfolio decisions
5. **Store visits**: Log visits, track issues, follow up
6. **Escalation**: Issues flow up — restaurant → district → region → COO

## Alerts

- **Underperforming location**: Revenue or margins below threshold for 2+ consecutive weeks
- **Labor cost spike**: Location exceeds labor % target by >3 points
- **Guest complaint surge**: Location complaint rate doubles week-over-week
- **Food safety risk**: Failed audit or food safety complaint at any location
- **Staffing crisis**: Location below minimum staffing for scheduled shifts
- **Equipment failure**: Critical equipment down (POS, fryer, grill, cooler) reported via FreshService
- **Speed of service degradation**: Average order time exceeds target consistently
