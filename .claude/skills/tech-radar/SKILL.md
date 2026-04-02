---
name: tech-radar
description: Use when evaluating new technologies, reviewing the technology landscape, preventing duplicate evaluations, or when agents need context about which technologies the organization is adopting, trialing, assessing, or holding.
---

# Tech Radar

Maintain a structured view of the organization's technology landscape — what's adopted, what's being evaluated, and what's being deprecated.

## Rings

| Ring | Meaning | Action |
|------|---------|--------|
| **Adopt** | Proven, recommended for use | Default choice for new projects |
| **Trial** | Worth pursuing, used in production on limited scope | Use on non-critical projects to gain experience |
| **Assess** | Worth exploring, not yet tried | Investigate through spikes or POCs |
| **Hold** | Not recommended for new projects | Don't start new work with this; plan migration |

## Quadrants

| Quadrant | Contains |
|----------|---------|
| **Languages & Frameworks** | Programming languages, frontend/backend frameworks, libraries |
| **Platforms & Infrastructure** | Cloud services, databases, container orchestration, CI/CD |
| **Tools** | Developer tools, monitoring, testing, productivity |
| **Techniques** | Practices, patterns, processes, methodologies |

## Output Format

Save to `docs/tech/tech-radar.md`:

```markdown
# Technology Radar
> Last updated: YYYY-MM-DD
> Owner: [CTO/Tech Lead name]

## Radar Overview

### Adopt
| Technology | Quadrant | Since | Notes |
|-----------|----------|-------|-------|
| [tech] | Languages & Frameworks | [date] | [why it's adopted] |
| [tech] | Platforms & Infrastructure | [date] | [why it's adopted] |

### Trial
| Technology | Quadrant | Since | Trial Project | Review Date |
|-----------|----------|-------|--------------|-------------|
| [tech] | [quadrant] | [date] | [where it's being tried] | [when to decide] |

### Assess
| Technology | Quadrant | Since | Champion | Next Step |
|-----------|----------|-------|----------|-----------|
| [tech] | [quadrant] | [date] | [who's evaluating] | [POC / spike / research] |

### Hold
| Technology | Quadrant | Since | Reason | Migration Path |
|-----------|----------|-------|--------|---------------|
| [tech] | [quadrant] | [date] | [why on hold] | [alternative / timeline] |

## Recent Changes

| Date | Technology | Change | Rationale |
|------|-----------|--------|-----------|
| [date] | [tech] | Assess → Trial | [why promoted] |
| [date] | [tech] | Trial → Adopt | [results from trial] |
| [date] | [tech] | Adopt → Hold | [why deprecated] |

## Evaluation Criteria

When assessing new technologies, consider:

| Criterion | Weight | Questions |
|-----------|--------|-----------|
| Strategic fit | High | Does it align with company strategy? |
| Team capability | High | Can our team learn/use it effectively? |
| Community & support | Medium | Active community? Commercial support available? |
| Maturity | Medium | Production-ready? Stable API? |
| Integration | Medium | Works with our current stack? |
| Total cost | High | Licensing + infrastructure + learning + maintenance |
| Lock-in risk | Medium | How hard is it to switch away? |
| Security | High | Meets our security requirements? |

## Pending Evaluations

| Technology | Proposed By | Date | Why | Status |
|-----------|------------|------|-----|--------|
| [tech] | [who] | [date] | [reason to evaluate] | Not started / In progress |
```

## Workflow

### Adding a New Technology

1. Check if it's already on the radar — prevent duplicate evaluations
2. Start in **Assess** with a champion and next step defined
3. Champion conducts evaluation (spike, POC, research)
4. Review findings and decide: promote to Trial, stay in Assess, or reject
5. Document the decision (cross-reference with decision-framework)

### Promoting a Technology

- **Assess → Trial**: Evaluation is promising, ready for limited production use
- **Trial → Adopt**: Trial succeeded, team is confident, ready for broad use
- Log every promotion in "Recent Changes" with rationale

### Deprecating a Technology

- Move to **Hold** with clear reason and migration path
- Never just remove — Hold signals "don't start new work, plan to move off"
- Link to migration plan or decision record

## How Agents Use This

Before recommending technologies, agents should:
1. Check if `docs/tech/tech-radar.md` exists
2. Recommend **Adopt** ring technologies as defaults
3. Suggest **Trial** ring technologies for appropriate contexts
4. Flag if a recommendation conflicts with **Hold** items
5. Check for existing evaluations before suggesting new assessments
6. Cross-reference with team-structure for capability fit
7. Cross-reference with vendor-manager for licensing implications

## Tips

- Review the radar quarterly — technology moves fast
- Every "Hold" needs a migration path, not just a label
- Keep the radar visible to the whole engineering org — not just leadership
- Champion model works: every Assess/Trial needs one person driving evaluation
- Document failures too — "we tried X and it didn't work because Y" prevents re-evaluation
