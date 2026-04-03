---
name: guest-support
description: Use when handling guest/customer tickets, emails, or complaints for QSR restaurants — wrong orders, double charges, food quality issues, allergen concerns, refund requests, or general inquiries. Triages, drafts responses, and tracks resolution.
---

# Guest Support

Handle guest/customer support tickets and emails for QSR restaurant operations. Triages by severity, drafts responses following best practices and company policies, tracks resolution, and escalates when needed.

## IMPORTANT: Company Policies

**Before using this skill, company-specific policies must be loaded from:**
`docs/policies/guest-support-policies.md`

If this file does not exist, the skill uses industry best practices (documented below). Once you upload your policies, they override the defaults.

**To set up**: Paste or describe your company's guest support policies and the agent will create `docs/policies/guest-support-policies.md` with your specific:
- Compensation tiers and approval limits
- Refund policies and procedures
- Escalation contacts and paths
- Brand-specific language and tone
- Store-specific procedures
- Legal disclaimers

## Ticket Triage

Every incoming ticket is categorized by **type** and **severity**:

### Severity Levels

| Level | Category | Response Time | Action |
|-------|----------|--------------|--------|
| **CRITICAL** | Allergen reaction, foreign object with injury, foodborne illness, injury on premises | Immediate | Escalate to legal/compliance. Do not resolve at Tier 1. |
| **HIGH** | Foreign object (no injury), allergen concern (no reaction), discrimination allegation, data privacy issue | Within 1 hour | Escalate to manager. Document thoroughly. |
| **MEDIUM** | Double charge, wrong order, food quality, rude staff, long wait time | Within 4 hours | Resolve at Tier 1 with approved compensation. |
| **LOW** | General inquiry, menu questions, hours, loyalty points, catering request | Within 24 hours | Resolve at Tier 1. Informational response. |

### Ticket Types

| Type | Examples | Default Severity |
|------|---------|-----------------|
| `food-safety` | Foreign object, allergen exposure, illness claim | CRITICAL or HIGH |
| `food-quality` | Wrong order, cold food, missing items, taste | MEDIUM |
| `billing` | Double charge, wrong amount, refund request | MEDIUM |
| `service` | Rude staff, long wait, cleanliness | MEDIUM |
| `digital` | App error, kiosk issue, online order problem | MEDIUM |
| `loyalty` | Points missing, reward not working, account issue | LOW |
| `inquiry` | Menu, hours, nutrition, catering, employment | LOW |

## Response Framework — HEARD Model

All responses follow the HEARD model:

1. **Hear**: Acknowledge what the guest experienced (reference their specific issue)
2. **Empathize**: Validate their frustration genuinely
3. **Apologize**: Sincere, specific apology — not generic
4. **Resolve**: Offer a concrete solution with options when possible
5. **Diagnose**: Flag the root cause for internal follow-up

### Response Tone

- **Warm and personal** — use the guest's name, reference their specific order/experience
- **Take ownership** — never deflect blame to delivery platforms, suppliers, or other departments
- **Solution-first** — lead with what you CAN do, not what you can't
- **Concise** — QSR guests expect speed everywhere, including support
- **Professional but not corporate** — avoid "per our policy" language

### Language Guide

| Never Say | Say Instead |
|-----------|-----------|
| "Calm down" | "I hear you, and I want to help" |
| "That's our policy" | "Here's what I can do for you" |
| "You should have..." | "Next time, we can..." |
| "I can't do that" | "What I can do is..." |
| "Are you sure?" | "Thank you for letting us know" |
| "It's not our fault" | "I'm sorry this happened" |
| "We've never heard that before" | "I appreciate you bringing this to our attention" |
| "Actually..." (correcting guest) | Acknowledge first, then clarify gently |

## Compensation Guidelines (Defaults)

**These are industry defaults. Override with your company policies in `docs/policies/guest-support-policies.md`.**

### Tier 1 — Minor Inconvenience
**When**: Missing sauce/condiment, slightly wrong order, short wait
**Action**: Free item coupon or small credit ($3-7)
**Approval**: Tier 1 agent

### Tier 2 — Moderate Issue
**When**: Entire wrong meal, significant wait, rude experience, cold food
**Action**: Full refund of order OR equivalent coupon (1.5x order value)
**Approval**: Tier 1 agent (within threshold)

### Tier 3 — Serious Issue
**When**: Repeated failures, significant food quality concern, loss of trust
**Action**: Full refund + additional coupon ($15-25) + personalized follow-up
**Approval**: Manager

### Tier 4 — Critical/Safety
**When**: Foreign object, allergen reaction, illness, injury
**Action**: Full refund + immediate escalation to legal/compliance
**Approval**: Legal/compliance team only. Do NOT set compensation at agent level.

### Billing Issues
- **Double charge**: Refund the duplicate charge. No coupon needed unless guest was significantly inconvenienced.
- **Wrong amount**: Refund the difference. Apologize for the error.
- **Delivery platform billing**: If the charge is from the delivery platform (Uber Eats, etc.), guide guest to the platform's support but still apologize for any restaurant-side issue.

## Escalation Paths

### Tier 1 → Tier 2 (Manager)
Escalate when:
- Guest is hostile after de-escalation attempt
- Complaint names a specific employee
- Repeat complaint (3+ contacts on same issue)
- Billing dispute exceeds threshold
- Guest requests manager
- Social media complaint gaining traction
- Service recovery offer rejected

### Tier 2 → Tier 3 (Legal/Compliance)
Escalate immediately when:
- Foreign object in food (potential injury or lawsuit)
- Allergen incident with medical symptoms
- Foodborne illness claim
- Injury on premises
- Discrimination or harassment allegation
- Data breach or privacy violation
- Guest mentions contacting health authorities, media, or attorney
- Any incident involving a minor's safety

### Health/Safety Immediate Protocol
1. Ask if guest needs medical attention — if yes, advise calling emergency services
2. Log incident with timestamp, location, full details
3. Notify store manager for evidence preservation (receipt, camera footage, food sample)
4. Escalate to food safety / quality team
5. **Never** minimize symptoms or say "it's probably fine"
6. **Never** admit liability — express concern and care, not legal responsibility

## Drafting Responses

When drafting a response to a guest ticket/email:

### Step 1: Classify
- Identify ticket type and severity
- Check if guest is a repeat complainant (search ticket log)
- Identify the location/store involved

### Step 2: Gather Context
- Check order details if available (Simphony data)
- Check if this location has similar recent complaints
- Check company policies in `docs/policies/guest-support-policies.md`

### Step 3: Draft Response
Follow the HEARD model. Include:
- Personal greeting using guest's name
- Specific reference to their issue (not generic)
- Sincere apology
- Concrete resolution with options
- Clear next steps and timeline
- Warm closing

### Step 4: Review
Before sending, check:
- [ ] Tone is warm and empathetic, not corporate
- [ ] Resolution matches the severity and company policy
- [ ] No language from the "Never Say" list
- [ ] No admission of legal liability (for safety issues)
- [ ] Personal details handled per GDPR/privacy requirements
- [ ] Correct store/location referenced

### Step 5: Log
Save interaction to `docs/support/tickets/YYYY-MM-DD-{ticket-id}.md`

## Ticket Log Format

Save to `docs/support/tickets/YYYY-MM-DD-{ticket-id}.md`:

```markdown
# Ticket: [ID or subject line]
> Date: YYYY-MM-DD | Channel: Email / Phone / Social / In-store
> Guest: [name] | Location: [store/location]
> Type: [food-safety|food-quality|billing|service|digital|loyalty|inquiry]
> Severity: [CRITICAL|HIGH|MEDIUM|LOW]
> Status: Open / Pending / Resolved / Escalated

## Guest Message
[Original message or summary of complaint]

## Order Details
- Order #: [if available]
- Date/time of visit: [date]
- Items: [what was ordered]
- Amount: [total charged]

## Response
[Our response — drafted or sent]

## Resolution
- Action taken: [refund/coupon/replacement/escalation]
- Compensation: [amount/type]
- Approved by: [agent/manager]

## Internal Notes
- [Root cause if identified]
- [Store notified: yes/no]
- [Follow-up needed: yes/no]

## Escalation (if applicable)
- Escalated to: [person/team]
- Reason: [why]
- Date: [when]
```

## Ticket Summary / Reporting

Maintain `docs/support/ticket-summary.md`:

```markdown
# Guest Support Summary
> Last updated: YYYY-MM-DD
> Period: [month/quarter]

## Volume
| Metric | Value | Trend |
|--------|-------|-------|
| Total tickets | [n] | Up/Down/Stable |
| Tickets per store/week | [avg] | |
| Top category | [type] | |

## By Type
| Type | Count | % of Total | Avg Resolution Time |
|------|-------|-----------|-------------------|
| food-quality | [n] | [%] | [time] |
| billing | [n] | [%] | [time] |
| service | [n] | [%] | [time] |
| food-safety | [n] | [%] | [time] |

## By Location
| Location | Tickets | Per 1000 Transactions | Top Issue |
|----------|---------|----------------------|-----------|
| [store] | [n] | [rate] | [category] |

## Escalation Summary
- Tier 2 escalations: [n] ([%])
- Tier 3 escalations: [n] ([%])

## Compensation Spend
- Total: [amount]
- Per ticket avg: [amount]
- Refunds: [amount]
- Coupons issued: [n] (value: [amount])

## Flags
- [Stores with above-average complaint rates]
- [Categories trending up]
- [Repeat complainants requiring attention]
```

## Integration with Other Skills

- **simphony**: Pull order details, check data, and store transaction history when investigating complaints
- **freshservice**: Create internal IT tickets for digital/app issues reported by guests
- **stakeholder-briefing**: Include guest support KPIs in management reports
- **meeting-prep**: Pull complaint trends for operations meetings
- **local-marketing**: Correlate marketing campaigns with complaint volume changes
- **risk-register**: Escalate recurring safety complaints as organizational risks
- **budget-tracker**: Track compensation spend against support budget

## Company Policy Upload

To configure this skill with your company's specific policies, provide:

1. **Compensation rules**: What can Tier 1 agents approve? What requires manager sign-off?
2. **Refund procedures**: How are refunds processed? Which systems? Timeline?
3. **Escalation contacts**: Who handles Tier 2? Tier 3? Legal? Food safety?
4. **Response templates**: Any mandatory language, disclaimers, or sign-offs?
5. **Brand voice**: How should we sound? More formal or casual? Any brand-specific phrases?
6. **Store procedures**: How are stores notified of complaints? What evidence preservation is expected?
7. **Regulatory specifics**: Any local/national regulations beyond GDPR and food safety basics?
8. **Channel-specific rules**: Different handling for email vs social vs phone?

The agent will structure your policies into `docs/policies/guest-support-policies.md` and reference them in all future responses.
