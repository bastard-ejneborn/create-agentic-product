---
name: organisation
description: Use when the user asks about the company hierarchy, reporting lines, or who someone's manager is (e.g. "who is Lisa's manager?", "has Lisa's manager approved this?", "who needs to sign off on X?"). Also use to document team composition, assess capabilities and skill gaps, plan hiring, or review org structure. Agents should consult this skill whenever a question involves approvals, escalation paths, or organizational context.
---

# Organisation

Maintain a structured view of the organisation — hierarchy, reporting lines, team composition, capabilities, and capacity — so agents can answer questions about who reports to whom, who approves what, and ground recommendations in organisational reality.

## Bundled Data

This skill ships with pre-populated organisation data for **Bastard Burgers** in `organisation-data.md` (same folder as this file). That file contains:
- Full reporting hierarchy (CEO → C-level → Heads → team members)
- People Index with Manager / Skip-level / Department Head columns for every named person
- Operations footprint (2 Regions, 6 Districts, 74 restaurants)
- Known Approval Rules and Key Person Risks

**Read `organisation-data.md` first** whenever answering a hierarchy or approval question. If the data needs updating (new hire, departure, reorg), edit `organisation-data.md` directly and bump the `Last updated` date.

## When to Use

- **Hierarchy lookup**: "Who is Lisa's manager?", "Who does Erik report to?"
- **Approval routing**: "Has Lisa's manager approved this?", "Who needs to sign off on a €50k purchase in Marketing?"
- **Escalation paths**: "Who is Lisa's skip-level?", "Who is the department head for IT?"
- **Team context**: Capacity, skill gaps, hiring plans, key-person risks
- **Org changes**: New hires, departures, restructures, contractor engagements

## Two Input Paths

### Interview Mode

1. **Organisation overview**: How is the org structured? Departments, teams, reporting lines?
2. **Leadership**: CEO, C-level, and who reports to each
3. **Teams**: For each team, capture:
   - Team name and purpose
   - Team lead and who they report to
   - Members (name, role, manager)
   - Headcount (current and approved)
   - Key capabilities and technologies
   - Current workload (stretched/balanced/available)
4. **Key people**: Anyone whose departure would be a significant risk?
5. **Skill gaps**: Where is capability or depth lacking?
6. **Hiring plans**: Open positions, planned hires, timeline?
7. **External resources**: Contractors, consultants, outsourced teams?
8. **Approval rules**: Any known approval thresholds tied to roles? (e.g. "Department head approves >€10k", "CFO approves >€50k")

### Import Mode

If existing org data is available (org chart, HR export, spreadsheet):
1. Read and map to the standard format below
2. Identify gaps (missing managers, unclear reporting)
3. Ask follow-up questions to fill gaps

## Output Format

Save to `docs/organisation/organisation.md` (or wherever the host environment stores docs):

```markdown
# Organisation
> Last updated: YYYY-MM-DD
> Total headcount: [n] (FTE: [n] | Contractors: [n])
> Open positions: [n] | Planned hires: [n]

## Organisation Overview

[Brief description — flat, matrix, functional, etc. Name the top of the hierarchy.]

## Reporting Lines (Hierarchy)

Use indentation to show reporting chain. Every person must have a manager listed (except the top).

- **[CEO Name]** — CEO
  - **[Name]** — CTO
    - **[Name]** — Head of Platform
      - [Name] — Platform Engineer
      - [Name] — Platform Engineer
    - **[Name]** — Head of Product Engineering
      - [Name] — Frontend Dev
      - [Name] — Backend Dev
  - **[Name]** — CMO
    - **[Name]** — Marketing Manager
      - [Name] — Content Lead
      - Lisa Svensson — Social Media Specialist

## People Index (quick lookup)

| Name | Role | Team | Manager | Skip-level | Department Head |
|------|------|------|---------|-----------|----------------|
| Lisa Svensson | Social Media Specialist | Marketing | [Marketing Manager name] | CMO | CMO |
| [Name] | [role] | [team] | [manager] | [skip] | [dept head] |

## Teams

### [Team Name]
> Lead: [person] | Reports to: [person]
> Headcount: [current] / [approved] | Contractors: [n]
> Workload: Stretched / Balanced / Available

**Purpose**: [What this team is responsible for]

**Capabilities**:
- [Skill/technology 1]
- [Skill/technology 2]

**Current focus**: [What they're working on]

**Members**:
| Name | Role | Manager | Key Skills | Notes |
|------|------|---------|-----------|-------|
| [name] | [role] | [manager] | [skills] | [key person risk, part-time, etc.] |

---

[Repeat for each team]

## Approval Rules

Document known approval thresholds and routing so agents can answer "who needs to approve X?".

| Scenario | Approver | Notes |
|----------|----------|-------|
| Purchase < €1,000 | Line manager | |
| Purchase €1k–€10k | Department head | |
| Purchase > €10k | CFO + CEO | |
| PTO / vacation | Line manager | |
| Hiring | Department head + HR | |
| Architecture change | CTO | Cross-ref tech-radar |

## Skill Matrix

| Capability | Team(s) | Depth | Gap? | Notes |
|-----------|---------|-------|------|-------|
| [e.g., Cloud infrastructure] | Platform | Deep | No | |
| [e.g., Machine learning] | — | None | Yes | Need to hire or outsource |

Depth: Deep (multiple experts) | Moderate (1-2 capable) | Shallow (learning) | None

## Key Person Risks

| Person | Role | Risk If They Leave | Mitigation |
|--------|------|--------------------|-----------|
| [name] | [role] | [impact] | [knowledge sharing, documentation, backup] |

## Open Positions & Hiring Plan

| Position | Team | Reports to | Priority | Status | Target Start |
|----------|------|-----------|----------|--------|-------------|
| [role] | [team] | [manager] | High/Medium/Low | Open / Interviewing / Offer | [date] |

## External Resources

| Provider | Type | Team/Project | Monthly Cost | Contract End |
|----------|------|-------------|-------------|-------------|
| [company/person] | Contractor / Consultancy / Outsource | [what] | [cost] | [date] |

## Capacity Summary

| Team | Headcount | Active Projects | Capacity | Can Take New Work? |
|------|----------|----------------|----------|-------------------|
| [team] | [n] | [n] | Stretched/Balanced/Available | Yes / Partial / No |
```

## Lookup Logic (for answering questions)

When the user asks an org question, resolve in this order:

1. **"Who is X's manager?"** → Look up X in the People Index, return the `Manager` column. If not in the index, fall back to the hierarchy tree.
2. **"Has X's manager approved this?"** → Identify X's manager (step 1), then check the context/conversation for whether that person has approved. If no approval evidence, state that explicitly and suggest asking the manager directly.
3. **"Who needs to approve X?"** → Check the Approval Rules table. If the rule references a role (e.g. "Department head"), resolve the role to a named person using the hierarchy.
4. **"Who is the skip-level / department head?"** → Walk up the reporting tree from the person until reaching the requested level.
5. **If the person isn't in the data** → Say so; don't guess. Offer to add them via interview mode.

## Updates

- "We hired a new data engineer on the platform team reporting to [name]" — add to hierarchy, people index, team members, update headcount
- "Sarah is leaving end of month" — flag key person risk, mark as departing in the people index
- "Erik now reports to the CTO instead of the Head of Platform" — update reporting line in both hierarchy and people index
- "We're bringing in contractors for the migration" — add to external resources
- Always update `Last updated` and summary counts

## How Agents Use This

Before making recommendations or answering approval/routing questions, agents should:

1. Check if `docs/organisation/organisation.md` exists
2. For hierarchy questions, use the Lookup Logic above
3. For capacity/capability recommendations, check the skill matrix and team workload
4. Flag when a recommendation requires skills the team doesn't have
5. Suggest build (hire/train) vs. buy (outsource/SaaS) based on team reality
6. Check capacity before recommending new projects
7. Never guess a manager or approver — if the data isn't present, say so

## Alerts

- **Missing manager**: Person in the index without a manager entry — flag for cleanup
- **Key person risk**: Single point of failure without documented mitigation
- **Skill gaps blocking strategy**: Strategic priority requires a capability the team lacks
- **Capacity overload**: Team marked as "Stretched" with new projects assigned
- **Stale hiring**: Open position without movement in 60+ days
- **Contractor dependency**: External resources on critical path without transition plan
- **Broken reporting line**: Someone's listed manager no longer exists in the org
