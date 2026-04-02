---
name: company-strategy
description: Use when the user wants to define, import, update, or reference their company's strategic vision, OKRs, priorities, or constraints. Also use when C-level agents need strategic context for recommendations.
---

# Company Strategy

Capture and structure a company's strategic vision so that all advisory agents can align recommendations to actual business priorities.

## Two Input Paths

### Interview Mode

When the user wants to build a strategy from scratch or doesn't have a written one:

1. **Company overview**: Industry, size, stage (startup/growth/enterprise), geography
2. **Vision & mission**: Where is the company heading? What's the core purpose?
3. **Strategic priorities**: What are the top 3-5 priorities for the coming year? Rank them.
4. **OKRs / key metrics**: What does success look like? How is it measured?
5. **Constraints**: Budget limits, team size, technical debt, compliance requirements, non-negotiables
6. **Competitive context**: Key competitors, differentiation, market position
7. **Timeline & milestones**: Key dates, deadlines, review cycles

Ask one topic at a time. Use multiple choice where possible. Summarize each answer back before moving on.

### Import Mode

When the user has existing strategy documents:

1. Read the provided document(s)
2. Extract and structure into the standard format below
3. Identify gaps — which sections are missing or unclear?
4. Ask targeted follow-up questions to fill gaps
5. Present the structured result for approval

## Output Format

Save to `docs/strategy/company-strategy.md`:

```markdown
# Company Strategy
> Last updated: YYYY-MM-DD

## Company Overview
- **Industry**:
- **Size**:
- **Stage**:
- **Geography**:

## Vision & Mission
**Vision**:
**Mission**:

## Strategic Priorities (ranked)
1. **[Priority]** — [Description] | Timeline: [when]
2. **[Priority]** — [Description] | Timeline: [when]
3. **[Priority]** — [Description] | Timeline: [when]

## OKRs & Key Metrics
### [Objective 1]
- KR: [Key Result] | Target: [value] | Current: [value]

## Constraints & Non-Negotiables
- [Constraint with context]

## Competitive Context
| Competitor | Strength | Our Differentiation |
|-----------|----------|-------------------|

## Timeline & Milestones
| Date | Milestone | Owner |
|------|-----------|-------|
```

## Updates

Support incremental updates without rewriting:
- User can update individual sections: "Update our Q3 priorities"
- Always update the `Last updated` date
- When a priority changes, flag downstream impacts: "This affects decisions X and Y in the decision log"

## Staleness Check

If `Last updated` is older than 90 days, flag it:
> "Your company strategy was last updated [date]. Strategic context may have shifted. Want to review and update?"

## How Agents Use This

Before making recommendations, C-level agents should:
1. Check if `docs/strategy/company-strategy.md` exists
2. Read it and identify relevant priorities and constraints
3. Align recommendations to stated strategy
4. Flag any recommendation that conflicts with a stated priority or constraint
