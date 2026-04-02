---
name: decision-framework
description: Use when making strategic decisions like build vs buy, vendor selection, investment prioritization, architecture choices, or when you need to document a decision with rationale and trade-offs.
---

# Decision Framework

Structured decision-making for C-level choices with adaptive formality and a searchable decision log.

## When to Use

- Build vs. buy vs. open-source decisions
- Vendor or tool selection
- Investment prioritization
- Architecture or platform choices
- Organizational changes
- Risk acceptance decisions

## Formality Levels

### Lightweight (default)

For daily/weekly decisions with limited blast radius.

```markdown
# Decision: [Title]
> Date: YYYY-MM-DD | Status: Accepted | Author: [name]

## Context
[Why is this decision needed? What triggered it?]

## Options Considered
1. **[Option A]** — [Pros] | [Cons]
2. **[Option B]** — [Pros] | [Cons]
3. **[Option C]** — [Pros] | [Cons]

## Decision
[What was decided and why]

## Strategy Alignment
[How does this support company strategic priorities? Reference docs/strategy/company-strategy.md]

## Next Steps
- [ ] [Action item] — Owner: [who] — By: [when]
```

### Formal ADR

Escalate to formal ADR when any of these apply:
- Budget impact > significant threshold for the organization
- Decision is irreversible or very costly to reverse
- Affects 3+ teams or stakeholders
- Compliance or legal implications
- Sets a precedent for future decisions

```markdown
# ADR-[NNN]: [Title]
> Date: YYYY-MM-DD | Status: Proposed/Accepted/Deprecated/Superseded
> Author: [name] | Reviewers: [names]
> Supersedes: [ADR-NNN if applicable]
> Superseded by: [ADR-NNN if applicable]

## Context
[Detailed background — business context, technical context, constraints]

## Decision Drivers
- [Driver 1]
- [Driver 2]

## Options Considered

### Option A: [Name]
**Description**: [What this option entails]
**Pros**: [Advantages]
**Cons**: [Disadvantages]
**Cost estimate**: [If applicable]
**Risk level**: [Low/Medium/High]

### Option B: [Name]
[Same structure]

## Decision
[What was decided]

## Rationale
[Why this option was chosen over alternatives]

## Strategy Alignment
[Cross-reference with docs/strategy/company-strategy.md — which priorities does this support or conflict with?]

## Consequences
**Positive**: [Expected benefits]
**Negative**: [Known trade-offs]
**Risks**: [What could go wrong, mitigations]

## Review
- **Review date**: [When to revisit this decision]
- **Success criteria**: [How to know if the decision was right]

## Related Decisions
- [Links to related ADRs]
```

## Workflow

1. **Identify the decision**: What needs to be decided and why now?
2. **Assess formality**: Check the escalation signals above. Recommend level to user.
3. **Read strategy**: Check `docs/strategy/company-strategy.md` for relevant priorities and constraints
4. **Gather options**: Research and list realistic options (minimum 2, ideally 3)
5. **Analyze trade-offs**: Evaluate each option against strategy, constraints, and risk
6. **Recommend**: Present analysis with a clear recommendation and rationale
7. **Document**: Save decision to `docs/decisions/YYYY-MM-DD-{topic}.md`
8. **Update index**: Add entry to `docs/decisions/README.md`

## Decision Log Index

Maintain `docs/decisions/README.md`:

```markdown
# Decision Log

| Date | Decision | Status | Formality | Summary |
|------|----------|--------|-----------|---------|
| YYYY-MM-DD | [Title](YYYY-MM-DD-topic.md) | Accepted | Lightweight | [One-line summary] |
```

## Decision Types — Quick Reference

| Type | Key Questions | Typical Formality |
|------|--------------|-------------------|
| Build vs. buy | TCO, maintenance burden, team capability, time-to-market | Formal |
| Vendor selection | Cost, integration, lock-in, support, roadmap alignment | Formal |
| Investment priority | Business value, effort, risk, strategy alignment | Lightweight |
| Architecture choice | Scalability, team expertise, maintenance, migration cost | Formal |
| Org change | Impact on teams, communication, culture, reversibility | Formal |
| Risk acceptance | Probability, impact, mitigation options, compliance | Lightweight |
