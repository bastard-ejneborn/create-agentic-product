---
name: project-planner
description: Use when starting a new project that needs a detailed plan — work breakdown, milestones, dependencies, resource allocation, and timeline. Different from project-portfolio which tracks the overview.
---

# Project Planner

Create detailed project plans with work breakdown, milestones, dependencies, and resource allocation for a single project.

## Workflow

1. **Define the project**: Ask:
   - What's the project goal? What does "done" look like?
   - What's the target completion date?
   - What's the budget?
   - Who's the sponsor? Who are the key stakeholders?
   - What teams/people are available?
   - Any hard constraints? (deadlines, dependencies, compliance)

2. **Break down the work**: Decompose into phases, then tasks
3. **Identify dependencies**: What blocks what?
4. **Assign resources**: Who does what?
5. **Build timeline**: Map tasks to dates, identify critical path
6. **Identify risks**: What could go wrong at each phase?

## Output Format

Save to `docs/projects/plans/YYYY-MM-DD-{project}-plan.md`:

```markdown
# Project Plan: [Project Name]
> Created: YYYY-MM-DD | Last updated: YYYY-MM-DD
> PM: [name] | Sponsor: [name]
> Target completion: [date] | Budget: [amount]

## Project Overview

**Goal**: [What we're building and why]

**Success criteria**:
- [Measurable outcome 1]
- [Measurable outcome 2]

**Scope**:
- **In scope**: [What's included]
- **Out of scope**: [What's explicitly excluded]

## Team

| Role | Person | Allocation | Notes |
|------|--------|-----------|-------|
| PM | [name] | [%] | |
| [role] | [name] | [%] | |

## Phases & Milestones

### Phase 1: [Name] — [start] to [end]

**Milestone**: [What marks completion of this phase]

| Task | Owner | Duration | Dependencies | Status |
|------|-------|----------|-------------|--------|
| [task] | [who] | [days] | — | Pending |
| [task] | [who] | [days] | Task 1 | Pending |

**Deliverables**: [What this phase produces]

### Phase 2: [Name] — [start] to [end]

[Same structure]

## Timeline Overview

```
Phase 1: [==========]
Phase 2:            [==========]
Phase 3:                        [==========]
                                             ↑ Launch
```

| Date | Milestone |
|------|-----------|
| [date] | [milestone] |
| [date] | [milestone] |
| [date] | [milestone — LAUNCH] |

## Critical Path

The following tasks are on the critical path — any delay directly impacts the launch date:
1. [Task] → [Task] → [Task] → [Milestone]

## Dependencies

### External Dependencies
| Dependency | Provider | Needed By | Status | Risk If Late |
|-----------|----------|-----------|--------|-------------|
| [what] | [team/vendor] | [date] | Confirmed/Pending | [impact] |

### Internal Dependencies
| Task | Blocks | Impact If Delayed |
|------|--------|------------------|
| [task] | [tasks] | [days of delay] |

## Risks

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|-----------|--------|-----------|-------|
| [risk] | H/M/L | H/M/L | [action] | [who] |

## Budget Breakdown

| Category | Estimated | Notes |
|----------|----------|-------|
| Personnel | [amount] | [detail] |
| Tools/Licenses | [amount] | [detail] |
| Infrastructure | [amount] | [detail] |
| Contingency (10-20%) | [amount] | |
| **Total** | **[amount]** | |

## Communication Plan

| Audience | Format | Frequency | Owner |
|----------|--------|-----------|-------|
| Team | Stand-up | Daily | PM |
| Stakeholders | Status report | Weekly | PM |
| Steering committee | Formal review | Biweekly | PM + Sponsor |

## Definition of Done

The project is complete when:
- [ ] [Success criterion 1 is met]
- [ ] [Success criterion 2 is met]
- [ ] Documentation is updated
- [ ] Handover to operations is complete
- [ ] Retrospective is done
```

## Tips

- Start with the end date and work backwards — this reveals whether the plan is realistic
- Add 20% buffer to estimates — things always take longer
- Identify the critical path first — everything else has float
- Smaller tasks (1-5 days) are more estimatable than large ones
- Every dependency is a risk — minimize external dependencies where possible
- Review the plan with the team before committing to it
