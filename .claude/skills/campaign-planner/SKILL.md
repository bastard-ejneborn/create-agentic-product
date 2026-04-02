---
name: campaign-planner
description: Use when planning marketing campaigns — defining objectives, target audience, channels, timeline, budget, KPIs, and A/B test plans. From brief through execution to post-campaign analysis.
---

# Campaign Planner

Structure marketing campaigns from brief to post-campaign analysis.

## Workflow

1. **Define the campaign**: Ask:
   - What's the objective? (awareness, leads, conversion, retention, launch)
   - What's the product/offer?
   - Who's the target audience? (reference audience-personas if available)
   - What's the budget?
   - What's the timeline?
   - Any brand constraints? (reference brand-guidelines if available)

2. **Design the campaign**: Channels, messaging, creative needs
3. **Plan execution**: Timeline, owners, assets needed
4. **Define measurement**: KPIs, tracking, A/B tests
5. **Post-campaign**: Results, learnings, recommendations

## Output Format

Save to `docs/marketing/campaigns/YYYY-MM-DD-{campaign-name}.md`:

```markdown
# Campaign: [Campaign Name]
> Created: YYYY-MM-DD | Last updated: YYYY-MM-DD
> Status: Planning / Active / Completed / Paused
> Owner: [name] | Budget: [amount]

## Brief

**Objective**: [What this campaign aims to achieve]
**Type**: Awareness / Lead Generation / Conversion / Retention / Product Launch
**Product/Offer**: [What we're promoting]
**Target audience**: [Who — reference personas if available]
**Key message**: [One sentence core message]
**Timeline**: [start] — [end]

## Audience

| Segment | Description | Size Estimate | Priority |
|---------|------------|--------------|----------|
| [segment] | [description] | [size] | Primary / Secondary |

**Pain points we're addressing**: [List]
**Value proposition for this audience**: [Statement]

## Channels & Tactics

| Channel | Tactic | Budget | Timeline | Owner | KPI |
|---------|--------|--------|----------|-------|-----|
| Email | Nurture sequence (5 emails) | [amount] | Week 1-4 | [who] | Open rate, CTR |
| LinkedIn | Sponsored posts + InMail | [amount] | Week 1-6 | [who] | Impressions, leads |
| Google Ads | Search + retargeting | [amount] | Week 1-6 | [who] | CPC, conversions |
| Content | Blog posts (3) + whitepaper | [amount] | Week 1-3 | [who] | Downloads, traffic |
| [channel] | [tactic] | [amount] | [when] | [who] | [metric] |

## Messaging Framework

**Headline options**:
1. [Option A]
2. [Option B]
3. [Option C]

**Key messages** (adapt per channel):
- **Primary**: [Main message]
- **Supporting**: [Evidence/benefit 1]
- **Supporting**: [Evidence/benefit 2]
- **CTA**: [What we want the audience to do]

**Tone**: [Reference brand-guidelines if available]

## Creative Assets Needed

| Asset | Specs | Owner | Due Date | Status |
|-------|-------|-------|----------|--------|
| [e.g., Hero banner] | [dimensions, format] | [who] | [date] | Pending |
| [e.g., Email templates] | [count, format] | [who] | [date] | Pending |
| [e.g., Landing page] | [specs] | [who] | [date] | Pending |

## A/B Tests

| Test | Variable | Variant A | Variant B | Success Metric | Duration |
|------|---------|-----------|-----------|---------------|----------|
| [test] | [what varies] | [A] | [B] | [metric] | [days] |

## Budget Breakdown

| Category | Amount | % of Total |
|----------|--------|-----------|
| Paid media | [amount] | |
| Content creation | [amount] | |
| Tools/platforms | [amount] | |
| Creative/design | [amount] | |
| Contingency | [amount] | |
| **Total** | **[amount]** | **100%** |

## Timeline

| Week | Activities | Milestones |
|------|-----------|-----------|
| Week 1 | [activities] | Campaign launch |
| Week 2 | [activities] | |
| Week 3 | [activities] | Mid-campaign review |
| Week 4+ | [activities] | Campaign end |

## KPIs & Targets

| KPI | Target | Tracking Method |
|-----|--------|----------------|
| [e.g., Leads generated] | [number] | [CRM/GA/platform] |
| [e.g., Cost per lead] | [amount] | [calculation] |
| [e.g., Conversion rate] | [%] | [funnel tracking] |
| [e.g., ROI] | [ratio] | [revenue / spend] |

## Post-Campaign Analysis

*(Fill in after campaign ends)*

| KPI | Target | Actual | Met? |
|-----|--------|--------|------|
| | | | |

**What worked**: [Key wins]
**What didn't**: [Shortfalls with reasons]
**Key learnings**: [Insights for future campaigns]
**Recommendations**: [What to do next]
```

## Tips

- Start with the objective, not the channel — channels serve goals
- Budget split: 60-70% to best-performing channels, 20-30% to test new ones
- Every campaign needs a control — you can't improve what you don't measure
- Plan creative early — it's always the bottleneck
- Set up tracking before launch, not after
