---
name: local-marketing
description: Use when planning, tracking, or analyzing local guerrilla marketing activities for restaurant locations — store visits, flyer drops, food sampling, local partnerships, and community events. Supports multi-location chains.
---

# Local Marketing

Plan, execute, and track ground-level marketing activities that drive guests to restaurant locations. Supports multi-location chains with per-location tracking, coverage mapping, and smart suggestions based on past results.

## Activity Types

### 1. Store & Business Visits
Visiting nearby offices, gyms, shops, hotels with menus, flyers, or coupons.

**Planning template**:
- Target businesses within [radius] of location
- What to bring (menus, flyers, coupons, samples)
- Best time to visit (lunch rush prep, morning drop-offs)
- Who to ask for (manager, front desk, break room access)
- Follow-up plan (revisit in X weeks)

### 2. Events & Sampling
Food sampling, pop-ups, local events, sponsorships, community days.

**Planning template**:
- Event type and date
- Location/venue
- Staff needed
- Menu items to sample (high-margin, signature dishes)
- Materials needed (signage, napkins, business cards, coupons)
- Offer tied to event (e.g., "Show this card for 10% off")
- Cost estimate
- Expected reach

### 3. Partnerships
Cross-promotions with local businesses, hotels, gyms, schools — ongoing relationships.

**Planning template**:
- Partner business and contact
- Partnership type (coupon exchange, co-branded flyer, employee discount, referral)
- What we offer them / what they offer us
- Duration and review date
- Materials needed
- Success metric

### 4. Street & Print
Flyer drops, poster placement, door hangers, car flyers, chalk signs.

**Planning template**:
- Material type and quantity
- Target area/streets
- Distribution method (door-to-door, car windshields, bulletin boards, hand-to-hand)
- Best timing (day of week, time of day)
- Offer/coupon code for tracking
- Legal considerations (permits, no-flyer zones)

## Multi-Location Structure

Each restaurant location gets its own directory:

```
docs/marketing/local/
  local-marketing-plan.md        ← Company-wide plan and calendar
  {location-name}/
    activity-log.md              ← History of all activities
    area-map.md                  ← Nearby businesses and coverage
    partnerships.md              ← Active local partnerships
```

## Activity Log

Save per location to `docs/marketing/local/{location}/activity-log.md`:

```markdown
# Activity Log: [Location Name]
> Last updated: YYYY-MM-DD
> Total activities: [n] | This month: [n]

## Log

| Date | Type | Where/What | Reach | Cost | Result | Notes |
|------|------|-----------|-------|------|--------|-------|
| YYYY-MM-DD | Store visit | [business name] | ~50 | $0 | Good | Left 20 menus, manager was receptive |
| YYYY-MM-DD | Flyer drop | [street/area] | ~200 | $30 | OK | Windy day, some blew away |
| YYYY-MM-DD | Sampling | [event/location] | ~150 | $80 | Good | 12 coupons redeemed same week |
| YYYY-MM-DD | Partnership | [business name] | ~100/mo | $0 | Good | Ongoing coupon exchange, 5 redemptions/week |

## Results Summary

### This Month
- Activities completed: [n]
- Estimated total reach: [n]
- Total cost: [amount]
- Coupons/offers distributed: [n]
- Known redemptions: [n]

### Top Performers (repeat these)
- [Activity that worked well — what, where, why it worked]

### Didn't Work (avoid or adjust)
- [Activity that underperformed — what, where, why it didn't work]
```

**Result scoring**:
- **Good** — clear positive response, redemptions, repeat interest, partnership established
- **OK** — completed but unclear impact, no negative signals
- **Bad** — negative reception, wasted materials, wrong audience, complaints

## Area Coverage Map

Save per location to `docs/marketing/local/{location}/area-map.md`:

```markdown
# Area Map: [Location Name]
> Last updated: YYYY-MM-DD
> Address: [restaurant address]

## Nearby Businesses & Coverage

| Business/Location | Type | Distance | Last Visited | Contact | Status | Notes |
|------------------|------|----------|-------------|---------|--------|-------|
| [Office building A] | Office (200 emp) | 300m | 2026-03-15 | Reception | Visited | Menus in break room |
| [Gym FitLife] | Gym | 500m | Never | — | Not visited | Good lunch crowd potential |
| [Hotel Cityview] | Hotel (120 rooms) | 400m | 2026-02-20 | Concierge | Partnership | Recommend us to guests |
| [School Westside] | School | 600m | Never | — | Not visited | Catering opportunity? |

## Area Zones

Divide the area around the restaurant into zones for systematic coverage:

| Zone | Area | Businesses | Status | Last Sweep |
|------|------|-----------|--------|-----------|
| North | [streets] | [n] | Covered | 2026-03-10 |
| East | [streets] | [n] | Partial | 2026-02-15 |
| South | [streets] | [n] | Not started | — |
| West | [streets] | [n] | Covered | 2026-03-20 |
```

## Partnerships Tracker

Save per location to `docs/marketing/local/{location}/partnerships.md`:

```markdown
# Local Partnerships: [Location Name]
> Last updated: YYYY-MM-DD
> Active partnerships: [n]

## Active Partnerships

### [Partner Business Name]
> Type: [Coupon exchange / Employee discount / Referral / Co-promotion]
> Contact: [name, phone/email]
> Started: [date] | Review: [date]
> Status: Active / Paused / Ended

**What we offer them**: [e.g., 10% discount card for their employees]
**What they offer us**: [e.g., our menus at their front desk, mention to hotel guests]
**Results**: [e.g., ~5 redemptions per week, worth maintaining]

---

[Repeat for each partnership]

## Partnership Ideas (Not Yet Approached)
| Business | Idea | Priority | Notes |
|----------|------|----------|-------|
| [business] | [partnership concept] | High/Medium/Low | [why] |
```

## Weekly/Monthly Planning

Save company-wide plan to `docs/marketing/local/local-marketing-plan.md`:

```markdown
# Local Marketing Plan
> Period: [month/quarter] | Last updated: YYYY-MM-DD

## Company-Wide Goals
- [e.g., Visit 20 new businesses per location per month]
- [e.g., Establish 2 new partnerships per location per quarter]
- [e.g., Run 1 sampling event per location per month]

## Weekly Calendar Template

| Day | Location | Activity | Target | Who | Materials |
|-----|----------|----------|--------|-----|-----------|
| Mon | [location A] | Store visits (3-5) | [area/zone] | [person] | Menus, coupons |
| Tue | [location B] | Flyer drop | [streets] | [person] | 200 flyers |
| Wed | [location A] | Partnership follow-up | [partner] | [person] | — |
| Thu | [location B] | Store visits (3-5) | [area/zone] | [person] | Menus, coupons |
| Fri | [location A] | Sampling prep | [event Saturday] | [person] | Ingredients, signage |
| Sat | [location A] | Food sampling | [location/event] | [2 people] | Samples, coupons |

## Per-Location Plans

### [Location Name]
**This month's focus**: [e.g., Cover the north zone, renew gym partnership]
**Activities planned**: [n]
**Budget**: [amount]

Priority activities:
1. [Activity with details]
2. [Activity with details]
3. [Activity with details]
```

## Smart Suggestions

When reviewing the activity log and area map, suggest:

### Coverage Gaps
Look at the area map for each location:
- Businesses marked "Not visited" — prioritize high-potential ones (offices, hotels, gyms)
- Zones marked "Not started" or last swept 60+ days ago
- "Visit [business] — 200 employees, 300m away, never visited"

### Repeat Winners
Look at the activity log for "Good" results:
- "Sampling at [location] worked well last time (12 redemptions). Schedule another?"
- "Store visits to offices generated the most reach. Do more of these."

### Partnership Follow-Ups
Look at partnerships tracker:
- Partnerships approaching review date
- Partnership ideas not yet approached
- "Partnership with [gym] is 3 months old — check in on results"

### Seasonal Opportunities
Flag based on time of year:
- Summer: outdoor sampling, local festivals, tourist areas
- Back-to-school: school partnerships, student discounts
- Holidays: corporate catering flyers to offices, holiday specials
- Sports seasons: game day promotions with nearby venues

### Underperforming Areas
- Locations with fewer activities than company average
- Locations with more "Bad" results — may need different approach
- Partnerships with no measurable results after 2+ months

## Workflow

1. **Setup**: Create location directories and initial area maps
2. **Plan**: Build weekly/monthly activity calendar per location
3. **Execute**: Team runs activities, logs results in activity-log
4. **Review**: Weekly check — what worked, what's next, coverage gaps
5. **Suggest**: Agent analyzes logs and suggests next actions
6. **Repeat**: Update plan based on results and suggestions

## How Agents Use This

Before planning local marketing activities, agents should:
1. Check `docs/marketing/local/{location}/activity-log.md` for past results
2. Check `docs/marketing/local/{location}/area-map.md` for coverage gaps
3. Check `docs/marketing/local/{location}/partnerships.md` for relationship status
4. Reference `docs/marketing/brand-guidelines.md` for brand consistency
5. Reference `docs/finance/budget.md` for available marketing budget
6. Suggest activities based on what's worked and what's uncovered
