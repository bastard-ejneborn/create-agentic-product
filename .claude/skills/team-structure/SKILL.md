---
name: team-structure
description: Use when the user wants to document team composition, assess capabilities and skill gaps, plan hiring, review org structure, or when agents need team context for capacity and feasibility assessments.
---

# Team Structure

Maintain a structured view of team composition, capabilities, and capacity so agents can ground recommendations in organizational reality.

## Two Input Paths

### Interview Mode

1. **Organization overview**: How is your tech/digital org structured? Departments, teams, reporting lines?
2. **Teams**: For each team, capture:
   - Team name and purpose
   - Team lead
   - Headcount (current and approved)
   - Key capabilities and technologies
   - Current workload (stretched/balanced/available)
3. **Key people**: Anyone whose departure would be a significant risk?
4. **Skill gaps**: Where do you lack capability or depth?
5. **Hiring plans**: Open positions, planned hires, timeline?
6. **External resources**: Contractors, consultants, outsourced teams?

### Import Mode

If the user has existing org data (org chart, HR system, spreadsheets):
1. Read and map to standard format
2. Identify gaps
3. Ask follow-up questions

## Output Format

Save to `docs/team/team-structure.md`:

```markdown
# Team Structure
> Last updated: YYYY-MM-DD
> Total headcount: [n] (FTE: [n] | Contractors: [n])
> Open positions: [n] | Planned hires: [n]

## Organization Overview

[Brief description of org structure — flat, matrix, functional, etc.]

## Teams

### [Team Name]
> Lead: [person] | Reports to: [person]
> Headcount: [current] / [approved] | Contractors: [n]
> Workload: Stretched / Balanced / Available

**Purpose**: [What this team is responsible for]

**Capabilities**:
- [Skill/technology 1]
- [Skill/technology 2]

**Current focus**: [What they're working on — cross-ref project-portfolio]

**Members**:
| Name | Role | Key Skills | Notes |
|------|------|-----------|-------|
| [name] | [role] | [skills] | [key person risk, part-time, etc.] |

---

[Repeat for each team]

## Skill Matrix

| Capability | Team(s) | Depth | Gap? | Notes |
|-----------|---------|-------|------|-------|
| [e.g., Cloud infrastructure] | Platform | Deep | No | |
| [e.g., Machine learning] | — | None | Yes | Need to hire or outsource |
| [e.g., Frontend (React)] | Product | Moderate | Partial | Only 2 devs, need more |

Depth: Deep (multiple experts) | Moderate (1-2 capable) | Shallow (learning) | None

## Key Person Risks

| Person | Role | Risk If They Leave | Mitigation |
|--------|------|--------------------|-----------|
| [name] | [role] | [impact] | [knowledge sharing, documentation, backup] |

## Open Positions & Hiring Plan

| Position | Team | Priority | Status | Target Start |
|----------|------|----------|--------|-------------|
| [role] | [team] | High/Medium/Low | Open / Interviewing / Offer | [date] |

## External Resources

| Provider | Type | Team/Project | Monthly Cost | Contract End |
|----------|------|-------------|-------------|-------------|
| [company/person] | Contractor / Consultancy / Outsource | [what] | [cost] | [date] |

## Capacity Summary

| Team | Headcount | Active Projects | Capacity | Can Take New Work? |
|------|----------|----------------|----------|-------------------|
| [team] | [n] | [n] | Stretched/Balanced/Available | Yes / Partial / No |
```

## Updates

- "We hired a new data engineer on the platform team" — update headcount and members
- "Sarah is leaving end of month" — flag key person risk, update team
- "We're bringing in contractors for the migration" — add to external resources
- Always update `Last updated` and summary counts

## How Agents Use This

Before making recommendations, agents should:
1. Check if `docs/team/team-structure.md` exists
2. Assess if the team has the capability to execute a recommendation
3. Flag when a recommendation requires skills the team doesn't have
4. Suggest build (hire/train) vs. buy (outsource/SaaS) based on team reality
5. Check capacity before recommending new projects
6. Cross-reference with project-portfolio for workload validation
7. Cross-reference with budget-tracker for hiring budget availability

## Alerts

- **Key person risk**: Single point of failure without documented mitigation
- **Skill gaps blocking strategy**: Strategic priority requires a capability the team lacks
- **Capacity overload**: Team marked as "Stretched" with new projects assigned
- **Stale hiring**: Open position without movement in 60+ days
- **Contractor dependency**: External resources on critical path without transition plan
