---
name: status-report
description: Use when preparing weekly or biweekly project status reports for stakeholders, steering committees, sponsors, or team leads. Different from stakeholder-briefing which is executive-level.
---

# Status Report

Generate operational status reports for projects — the PM's core communication deliverable.

## Templates

### Team Status (Weekly)

**Audience**: Team members, direct stakeholders
**Frequency**: Weekly

```markdown
# Status Report: [Project Name]
> Week of: YYYY-MM-DD | Author: [PM name]
> Overall status: On Track / At Risk / Blocked

## TL;DR
[2-3 bullet summary of the week]

## Completed This Week
- [x] [Task/deliverable] — [who]
- [x] [Task/deliverable] — [who]

## In Progress
- [ ] [Task] — [who] — Expected: [date]
- [ ] [Task] — [who] — Expected: [date]

## Planned Next Week
- [ ] [Task] — [who]
- [ ] [Task] — [who]

## Blockers & Risks
| Blocker/Risk | Impact | Owner | Action Needed |
|-------------|--------|-------|--------------|
| [issue] | [impact] | [who] | [what needs to happen] |

## Key Metrics
| Metric | Target | Actual | Trend |
|--------|--------|--------|-------|
| [metric] | [value] | [value] | Up/Down/Stable |

## Dependencies
- **Waiting on [team/person]**: [what] — needed by [date]

## Notes
[Anything else worth flagging]
```

### Steering Committee Status

**Audience**: Project sponsors, steering committee
**Frequency**: Biweekly or monthly

```markdown
# Steering Committee Report: [Project Name]
> Period: YYYY-MM-DD to YYYY-MM-DD
> PM: [name] | Sponsor: [name]
> Overall: On Track / At Risk / Blocked

## Executive Summary
[3-5 sentences: progress, key achievements, concerns]

## Milestone Progress
| Milestone | Target Date | Status | Notes |
|-----------|------------|--------|-------|
| [milestone] | [date] | Done / On track / Delayed | |

## Budget Status
| | Allocated | Spent | Remaining | % Used |
|--|----------|-------|-----------|--------|
| Total | | | | |

*(Cross-reference: docs/finance/budget.md)*

## Risks & Issues
| # | Description | Impact | Likelihood | Mitigation | Owner |
|---|-----------|--------|-----------|------------|-------|
| 1 | [risk] | H/M/L | H/M/L | [action] | [who] |

## Decisions Needed
| Decision | Context | Recommendation | Deadline |
|----------|---------|---------------|----------|
| [what] | [why] | [recommendation] | [when] |

## Next Period Plan
- [Key activities and milestones]
```

### Sponsor Update (Brief)

**Audience**: Project sponsor, one person
**Frequency**: As needed

```markdown
# [Project Name] — Quick Update
> Date: YYYY-MM-DD

**Status**: On Track / At Risk / Blocked

**Progress**: [2-3 sentences]

**Need from you**: [Specific ask, or "No action needed"]

**Heads up**: [Anything coming that they should know about]
```

## Workflow

1. **Identify audience and template**: Who is this for?
2. **Gather data**: Read project-portfolio, check completed/pending tasks, review risks
3. **Draft report**: Fill the template with current information
4. **Highlight changes**: What changed since last report? Lead with that.
5. **Save**: Write to `docs/projects/reports/YYYY-MM-DD-{project}-status.md`

## Tips

- Lead with changes, not repetition — don't repeat unchanged items
- Be honest about status — "at risk" early prevents "blocked" later
- Every blocker should have a proposed action — don't just report problems
- Include metrics even when they're bad — trust comes from transparency
- Keep team status to 1 page, steering committee to 2 pages max
