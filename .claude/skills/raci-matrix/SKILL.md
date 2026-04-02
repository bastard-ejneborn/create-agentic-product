---
name: raci-matrix
description: Use when clarifying roles and responsibilities for a project or process — who is Responsible, Accountable, Consulted, and Informed. Prevents ownership gaps and confusion.
---

# RACI Matrix

Define clear ownership for project activities to prevent the "I thought you were handling that" problem.

## Definitions

| Letter | Role | Meaning | Rule |
|--------|------|---------|------|
| **R** | Responsible | Does the work | Can be multiple people |
| **A** | Accountable | Owns the outcome, makes final call | Exactly ONE per activity |
| **C** | Consulted | Provides input before the work | Two-way communication |
| **I** | Informed | Told about progress/outcome | One-way communication |

## Workflow

1. **List activities**: What are the key deliverables, decisions, or processes?
2. **List roles/people**: Who is involved?
3. **Assign RACI**: For each activity × role, assign R, A, C, or I (or leave blank)
4. **Validate**: Check for common problems (see validation below)
5. **Review with team**: Get buy-in before it's final

## Output Format

Save to `docs/projects/{project}-raci.md`:

```markdown
# RACI Matrix: [Project/Process Name]
> Last updated: YYYY-MM-DD
> Project: [name] | PM: [name]

## Roles

| Abbreviation | Role | Person |
|-------------|------|--------|
| PM | Project Manager | [name] |
| TL | Tech Lead | [name] |
| PO | Product Owner | [name] |
| DEV | Development Team | [names] |
| QA | Quality Assurance | [name] |
| OPS | Operations | [name] |
| EXEC | Executive Sponsor | [name] |

## Matrix

| Activity | PM | TL | PO | DEV | QA | OPS | EXEC |
|----------|----|----|----|----|----|----|------|
| Requirements definition | R | C | A | C | I | I | I |
| Architecture design | C | A | C | R | I | C | I |
| Sprint planning | A | R | C | R | I | I | I |
| Development | I | C | I | R/A | I | I | I |
| Code review | I | A | I | R | I | I | I |
| Testing | I | C | I | C | R/A | I | I |
| Deployment | C | A | I | R | C | R | I |
| Go/no-go decision | C | C | C | I | C | C | A |
| Stakeholder reporting | R/A | C | I | I | I | I | I |

## Notes
- [Any clarifications about specific assignments]
```

## Validation Checklist

After building the matrix, check for these common problems:

| Problem | Symptom | Fix |
|---------|---------|-----|
| **No A** | Activity has no Accountable | Assign exactly one A |
| **Multiple A's** | More than one Accountable | Pick one — shared accountability = no accountability |
| **No R** | Activity has no Responsible | Someone needs to do the work |
| **Too many R's** | Everyone is Responsible | Clarify who actually does what |
| **A without R** | Accountable but no one doing work | A can also be R, or assign R |
| **Overloaded person** | One person is A on everything | Distribute accountability |
| **No I for stakeholders** | Key stakeholders not informed | Add I for relevant people |
| **C overload** | Too many Consulted | Only consult people whose input changes the outcome |

## Tips

- Start with the most contentious activities — that's where RACI adds the most value
- Keep activities at the right level — too detailed becomes unmanageable
- Review whenever team composition changes
- Post it where the team can see it — a forgotten RACI is useless
- Cross-reference with team-structure for role clarity
