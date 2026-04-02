---
name: project-portfolio
description: Use when the user wants to track, update, or review ongoing projects and initiatives, assess capacity for new work, check project status, or when agents need context about what's currently in flight.
---

# Project Portfolio

Maintain a structured overview of ongoing projects and initiatives so agents can factor in current workload, dependencies, and progress when advising.

## Two Input Paths

### Interview Mode

When building a portfolio from scratch:

1. **Active projects**: What's currently in flight? List them.
2. For each project, ask:
   - What is it? (one-line description)
   - Who owns it? (person or team)
   - What's the status? (on track / at risk / blocked / completed)
   - When did it start? When is it expected to finish?
   - What's the budget? (cross-reference with budget-tracker)
   - Which strategic priority does it support? (cross-reference with company-strategy)
   - Any dependencies on other projects or teams?
   - What's the expected business outcome?
3. **Pipeline**: Any planned but not-yet-started initiatives?
4. **Capacity**: How would you describe current team capacity? (stretched / balanced / available)

Ask about one project at a time.

### Import Mode

When the user has existing project data (Jira, Linear, spreadsheets, PM tools):

1. Read the provided data
2. Map to the standard format below
3. Identify gaps — which fields are missing?
4. Ask follow-up questions to complete the picture
5. Present the structured result for approval

## Output Format

Save to `docs/projects/portfolio.md`:

```markdown
# Project Portfolio
> Last updated: YYYY-MM-DD
> Total active projects: [n] | At risk: [n] | Blocked: [n]

## Portfolio Summary

| Project | Owner | Status | Priority Alignment | Budget | Timeline | Health |
|---------|-------|--------|-------------------|--------|----------|--------|
| [name] | [who] | On track | [strategic priority] | [amount] | Q1-Q3 | Green |
| [name] | [who] | At risk | [strategic priority] | [amount] | Q2-Q4 | Yellow |

Health: Green = on track | Yellow = at risk | Red = blocked/failing

## Active Projects

### [Project Name]
> Status: [On track / At risk / Blocked] | Health: [Green/Yellow/Red]
> Owner: [person/team] | Started: [date] | Target completion: [date]

**Description**: [What this project is and what it aims to achieve]

**Strategic alignment**: [Which priority from company-strategy this supports]

**Budget**: [Allocated] | [Spent] | [Remaining]
*(Cross-reference: docs/finance/budget.md)*

**Key milestones**:
| Milestone | Date | Status |
|-----------|------|--------|
| [milestone] | [date] | Done / On track / Delayed |

**Dependencies**:
- [Depends on / Blocks] [other project or team]

**Risks**:
- [Risk with current mitigation]

**Expected outcome**: [Business value when complete]

---

[Repeat for each active project]

## Pipeline (Planned, Not Started)

| Initiative | Priority Alignment | Estimated Budget | Target Start | Dependencies |
|-----------|-------------------|-----------------|-------------|-------------|
| [name] | [strategic priority] | [amount] | [date] | [what needs to happen first] |

## Capacity Overview

| Team / Area | Active Projects | Capacity | Notes |
|-------------|----------------|----------|-------|
| [team] | [n] | Stretched / Balanced / Available | |

## Cross-References
- Company strategy: `docs/strategy/company-strategy.md`
- Budget: `docs/finance/budget.md`
- Decisions: `docs/decisions/`
```

## Updates

Support incremental updates:
- "Project X is now at risk due to staffing" — update status and add risk
- "We completed the data migration milestone" — update milestone status
- "Add a new project: API platform rebuild" — add to active projects
- Always update `Last updated` date and portfolio summary counts
- When a project completes, move it to a "Completed" section (don't delete)

## How Agents Use This

Before advising on new initiatives or priorities, agents should:
1. Check if `docs/projects/portfolio.md` exists
2. Read it to understand what's currently in flight
3. Assess capacity before recommending new work
4. Identify dependencies and conflicts with existing projects
5. Cross-reference with budget (`docs/finance/budget.md`) for financial feasibility
6. Cross-reference with strategy (`docs/strategy/company-strategy.md`) for alignment

## Alerts

Flag these situations proactively:
- **At risk / blocked projects**: Surface these immediately when reviewing portfolio
- **Resource conflicts**: Multiple projects competing for the same team or resource
- **Strategic drift**: Projects that don't clearly align with any stated strategic priority
- **Budget overruns**: Project spend exceeding allocation (cross-reference budget-tracker)
- **Stale projects**: Projects with no milestone progress in 30+ days
- **Overloaded teams**: Teams assigned to more projects than capacity allows
- **Missing outcomes**: Projects without a defined expected business outcome
- **Dependency chains**: Flag when Project A blocks B blocks C — fragile chains need attention
