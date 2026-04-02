---
name: stakeholder-briefing
description: Use when preparing executive communications — board updates, team updates, business cases, incident reports, or any structured briefing for stakeholders at different levels.
---

# Stakeholder Briefing

Generate executive-level communications tailored to different audiences and formats.

## Templates

### Board Update

**Audience**: Board of directors, investors
**Tone**: Formal, metrics-heavy, concise
**When**: Quarterly reviews, fundraising updates, major milestones

```markdown
# Board Update — [Period]
> Date: YYYY-MM-DD | Prepared by: [name]

## Executive Summary
[3-5 sentences: progress, key wins, risks, asks]

## Strategic Progress
| Priority | Status | Key Metric | Target | Actual |
|----------|--------|-----------|--------|--------|

## Financial Overview
[Revenue, burn rate, runway, key financial metrics]

## Key Wins
- [Win with impact]

## Risks & Mitigations
| Risk | Impact | Likelihood | Mitigation | Owner |
|------|--------|-----------|------------|-------|

## Decisions Needed
- [Decision with context and recommendation]

## Next Quarter Outlook
[Key initiatives, expected milestones]
```

**Slide-ready version**: Each `##` section maps to one slide. Executive Summary = title slide. Tables become simple charts or bullet points.

---

### C-Suite Peer Update

**Audience**: Fellow C-level executives
**Tone**: Direct, actionable, peer-to-peer
**When**: Weekly/biweekly syncs, cross-functional alignment

```markdown
# [Department] Update — [Period]
> Date: YYYY-MM-DD

## TL;DR
[2-3 bullets: what matters this week]

## Progress
- [Initiative]: [Status] — [One-line detail]

## Dependencies & Asks
- **Need from [team]**: [What and by when]

## Decisions Made
- [Decision with link to decision log if applicable]

## Heads Up
- [Upcoming changes, risks, or shifts that affect other teams]
```

---

### Team Update

**Audience**: Direct reports, broader team
**Tone**: Transparent, motivational, contextual
**When**: All-hands, team meetings, kick-offs

```markdown
# Team Update — [Period]
> Date: YYYY-MM-DD

## Where We're Headed
[Strategic context — why the work matters]

## What We Accomplished
- [Achievement with recognition]

## What's Next
- **Priority 1**: [What and why]
- **Priority 2**: [What and why]

## Changes & Context
[Org changes, new initiatives, process updates — with the "why"]

## Open Questions
[Things still being figured out — transparency builds trust]
```

---

### Business Case

**Audience**: Decision makers (C-suite, board, budget owners)
**Tone**: Persuasive, data-driven, structured
**When**: New initiatives, large purchases, strategic pivots

```markdown
# Business Case: [Initiative]
> Date: YYYY-MM-DD | Author: [name] | Status: Draft/Under Review/Approved

## Problem Statement
[What problem are we solving? Who is affected? What's the cost of inaction?]

## Proposed Solution
[What we want to do, at a high level]

## Options Considered
| Option | Cost | Timeline | Risk | Recommendation |
|--------|------|----------|------|----------------|

## Cost-Benefit Analysis
**Investment required**: [One-time and ongoing costs]
**Expected return**: [Revenue, savings, risk reduction — quantified where possible]
**Break-even**: [When]

## Implementation Plan
| Phase | Timeline | Deliverable | Owner |
|-------|----------|-------------|-------|

## Risks
| Risk | Mitigation |
|------|-----------|

## Strategy Alignment
[How this supports stated strategic priorities]

## Ask
[Specific decision or approval needed]
```

**Slide-ready version**: Problem (1 slide) -> Solution (1 slide) -> Options (1 slide) -> Cost-Benefit (1 slide) -> Plan (1 slide) -> Ask (1 slide). Speaker notes contain the detailed prose from each section.

---

### Incident Report

**Audience**: Leadership, affected stakeholders, post-mortem participants
**Tone**: Factual, structured, blameless
**When**: After outages, security incidents, major bugs, process failures

```markdown
# Incident Report: [Title]
> Date: YYYY-MM-DD | Severity: P1/P2/P3/P4
> Duration: [start] — [end] ([total duration])
> Author: [name]

## Summary
[One paragraph: what happened, impact, resolution]

## Timeline
| Time | Event |
|------|-------|

## Impact
- **Users affected**: [number/scope]
- **Revenue impact**: [if applicable]
- **Data impact**: [if applicable]

## Root Cause
[Technical and process root cause — blameless]

## Resolution
[What was done to resolve the incident]

## Prevention
| Action Item | Owner | Due Date | Status |
|-------------|-------|----------|--------|

## Lessons Learned
- [What we learned]
```

## Workflow

1. **Identify audience and template**: Who is this for? Pick the matching template.
2. **Check strategy**: Read `docs/strategy/company-strategy.md` for relevant priorities and metrics to reference.
3. **Gather content**: Ask the user for key data points, or pull from existing docs/decisions.
4. **Draft**: Fill the template, adapting sections to the specific situation.
5. **Review**: Present draft, iterate based on feedback.
6. **Save**: Write to `docs/briefings/YYYY-MM-DD-{type}-{topic}.md`
7. **Slide version** (if applicable): Generate slide-ready version as a separate section at the bottom of the document.

## Tips

- Lead with what the audience cares about most — don't bury the lead
- Quantify everything you can — "improved performance" vs. "reduced latency by 40%"
- Every risk should have a mitigation — don't present problems without paths forward
- Match length to audience attention — board updates should be scannable in 2 minutes
- Reference strategy and decisions — link to `docs/strategy/` and `docs/decisions/` where relevant
