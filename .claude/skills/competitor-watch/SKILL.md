---
name: competitor-watch
description: Use when tracking competitor activity, analyzing market moves, monitoring pricing changes, evaluating competitive positioning, or when agents need competitive context for strategy and marketing decisions.
---

# Competitor Watch

Maintain ongoing competitive intelligence — track what competitors are doing, how the market is shifting, and what it means for your strategy and positioning.

## Two Input Paths

### Interview Mode

1. **Competitors**: Who are your top competitors? (direct and indirect)
2. For each competitor:
   - What do they offer? How do they position themselves?
   - What are their strengths and weaknesses?
   - How do they price? What's their model?
   - Who are their target customers?
   - What's their recent activity? (launches, funding, partnerships, hires)
3. **Market context**: What market trends are relevant?
4. **Your differentiation**: How do you win against each competitor?
5. **Monitoring priorities**: What matters most to track? (pricing, features, messaging, hiring)

### Import Mode

If the user has existing competitive analysis, battle cards, or market research:
1. Read provided documents
2. Structure into standard format
3. Identify gaps
4. Ask follow-up questions

## Output Format

Save to `docs/marketing/competitor-watch.md`:

```markdown
# Competitor Watch
> Last updated: YYYY-MM-DD
> Competitors tracked: [n]
> Market: [market/industry]

## Competitive Landscape Summary

| Competitor | Positioning | Strength | Weakness | Threat Level |
|-----------|------------|----------|----------|-------------|
| [name] | [one-line positioning] | [key strength] | [key weakness] | High/Medium/Low |

## Our Positioning

**How we win**: [Core differentiation statement]

**Where we're strongest**: [Areas of clear advantage]

**Where we're vulnerable**: [Areas where competitors have the edge]

## Competitor Profiles

### [Competitor Name]
> Threat level: High/Medium/Low | Last reviewed: YYYY-MM-DD
> Website: [url]

**Overview**: [What they do, company size, funding, market position]

**Target audience**: [Who they sell to]

**Positioning**: [How they describe themselves]

**Products/Services**:
| Product | Description | Comparable To (ours) |
|---------|------------|---------------------|
| [product] | [description] | [our equivalent] |

**Pricing**:
| Tier | Price | Includes |
|------|-------|---------|
| [tier] | [price] | [features] |

**Strengths**:
- [Strength with evidence]

**Weaknesses**:
- [Weakness with evidence]

**How we win against them**: [Specific differentiators and talking points]

**How we lose to them**: [Where they beat us and why]

---

[Repeat for each competitor]

## Activity Log

Track notable competitor moves in reverse chronological order:

| Date | Competitor | Activity | Impact | Our Response |
|------|-----------|---------|--------|-------------|
| YYYY-MM-DD | [who] | [what they did] | High/Medium/Low | [what we should do] |
| YYYY-MM-DD | [who] | [what they did] | High/Medium/Low | [what we should do] |

### Activity Types to Track
- Product launches and feature updates
- Pricing changes
- Funding rounds and acquisitions
- Key hires and departures
- Partnership announcements
- Marketing campaigns and messaging shifts
- Customer wins and losses
- Technology changes (stack, platforms)
- Geographic expansion
- Regulatory or compliance moves

## Market Trends

| Trend | Impact on Us | Impact on Competitors | Timeframe |
|-------|-------------|----------------------|-----------|
| [trend] | [how it affects us] | [how it affects them] | [when] |

## Battle Cards

Quick reference for sales and leadership conversations:

### vs. [Competitor A]

**They'll say**: "[Their pitch]"
**We say**: "[Our counter]"

**Their best feature**: [What they're known for]
**Our advantage**: [Where we clearly win]

**Watch out for**: [Traps or FUD they use]

**When we lose**: [Typical loss scenario]
**When we win**: [Typical win scenario]

## Feature Comparison Matrix

| Feature | Us | Competitor A | Competitor B | Competitor C |
|---------|-----|-------------|-------------|-------------|
| [feature] | Yes/No/Partial | Yes/No/Partial | Yes/No/Partial | Yes/No/Partial |

## Review Schedule

| Review Type | Frequency | Next Review | Owner |
|------------|-----------|-------------|-------|
| Full competitive review | Quarterly | [date] | [who] |
| Activity log update | Monthly | [date] | [who] |
| Battle card refresh | Quarterly | [date] | [who] |
| Pricing check | Monthly | [date] | [who] |
```

## Updates

- "Competitor X just launched a new pricing tier" — add to activity log, update pricing
- "We lost a deal to Competitor Y" — add to activity log, update "when we lose" in battle cards
- "New competitor entered the market" — add full competitor profile
- Always update `Last updated` date

## How Agents Use This

Before making strategic, marketing, or positioning recommendations, agents should:
1. Check if `docs/marketing/competitor-watch.md` exists
2. Reference competitive positioning when advising on strategy
3. Check competitor pricing when building business cases
4. Use battle cards when preparing sales or leadership materials
5. Flag when a recommendation creates competitive exposure
6. Cross-reference with company-strategy for positioning alignment
7. Cross-reference with brand-guidelines for messaging consistency
8. Feed activity log insights into campaign-planner for reactive campaigns

## Alerts

- **New competitor activity**: High-impact moves that need a response
- **Pricing undercut**: Competitor significantly changes pricing
- **Feature parity lost**: Competitor launches something we don't have that customers want
- **Stale data**: Profile not reviewed in 90+ days
- **Market shift**: Trend that changes competitive dynamics
