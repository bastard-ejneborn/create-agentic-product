---
name: company-policies
description: Use when the user wants to upload, update, or reference department-specific policies — IT, Operations, Marketing, HR, Finance, or Guest Support. Also use when agents need policy context before making recommendations or decisions.
---

# Company Policies

Manage department-specific policies in a structured format. When a user provides a policy, the skill identifies the department, structures it using a standard template, and saves it so all relevant agents can reference it.

## Department Files

| Department | File | Agents That Reference It |
|-----------|------|------------------------|
| IT | `docs/policies/it-policies.md` | cio-advisor, cto-advisor |
| Operations | `docs/policies/operations-policies.md` | cio-advisor, cdo-advisor, guest-support-agent |
| Marketing | `docs/policies/marketing-policies.md` | marketing-strategist, cdo-advisor |
| HR | `docs/policies/hr-policies.md` | cio-advisor, cdo-advisor, cto-advisor |
| Finance | `docs/policies/finance-policies.md` | cio-advisor, cto-advisor, cdo-advisor |
| Guest Support | `docs/policies/guest-support-policies.md` | guest-support-agent |

Master index: `docs/policies/index.md`

## How to Upload Policies

### Option 1: Paste a policy document
```
Here's our IT security policy: [paste document]
```
The agent will:
1. Identify the department(s) — in this case, IT
2. Structure the content using the standard template
3. Save to `docs/policies/it-policies.md`
4. Update `docs/policies/index.md`

### Option 2: Describe policies verbally
```
Our refund policy is: full refund within 24 hours for wrong orders, 
coupon only for quality complaints, manager approval needed above 500 SEK
```
The agent structures this into the correct department file.

### Option 3: Point to existing documents
```
Our HR policies are in this PDF: [upload or describe location]
```
The agent reads and structures the content.

### Cross-Department Policies
If a policy spans departments (e.g., data privacy affects IT, HR, and Guest Support), the agent:
1. Places the full policy in the primary department file
2. Adds a cross-reference in the other department files
3. Notes the overlap in the index

## Policy Template

Every department policy file follows this structure:

```markdown
# [Department] Policies
> Last updated: YYYY-MM-DD
> Owner: [person/role]
> Review cycle: [Annual / Quarterly / As needed]

## Table of Contents
- [Policy Area 1](#policy-area-1)
- [Policy Area 2](#policy-area-2)

---

## [Policy Area]

### Purpose
[Why this policy exists — one sentence]

### Scope
[Who and what this policy applies to]

### Policy
[The actual rules — clear, specific, actionable]

### Procedures
[Step-by-step: how to follow this policy]

### Approval & Escalation
[Who approves exceptions? Who to contact?]

### Exceptions
[Known exceptions or special cases]

### Related Policies
[Links to related policies in other departments]

---
```

## Policy Index

Maintain `docs/policies/index.md`:

```markdown
# Company Policies Index
> Last updated: YYYY-MM-DD

## By Department

| Department | File | Last Updated | Owner | Policies Covered |
|-----------|------|-------------|-------|-----------------|
| IT | [it-policies.md](it-policies.md) | YYYY-MM-DD | [CIO/IT Manager] | Security, change management, acceptable use, BYOD |
| Operations | [operations-policies.md](operations-policies.md) | YYYY-MM-DD | [Ops Director] | Food safety, hygiene, opening/closing, quality |
| Marketing | [marketing-policies.md](marketing-policies.md) | YYYY-MM-DD | [Marketing Lead] | Brand usage, social media, campaigns, local marketing |
| HR | [hr-policies.md](hr-policies.md) | YYYY-MM-DD | [HR Director] | Hiring, onboarding, code of conduct, training |
| Finance | [finance-policies.md](finance-policies.md) | YYYY-MM-DD | [CFO/Finance] | Expenses, procurement, budgets, approval limits |
| Guest Support | [guest-support-policies.md](guest-support-policies.md) | YYYY-MM-DD | [Support Lead] | Compensation, refunds, escalation, communication |

## Cross-Department Policies

| Policy | Departments | Primary File |
|--------|-----------|-------------|
| [e.g., Data Privacy/GDPR] | IT, HR, Guest Support | it-policies.md |
| [e.g., Social Media Conduct] | Marketing, HR | marketing-policies.md |
```

## Common Policy Areas by Department

### IT Policies
- Information security (access control, passwords, encryption)
- Change management (approval process for system changes)
- Acceptable use (company devices, internet, email)
- BYOD (personal devices on company network)
- Incident response (security breaches, system outages)
- Data backup and recovery
- Vendor/third-party access
- Software licensing

### Operations Policies
- Food safety and hygiene (HACCP, temperature control, allergen handling)
- Opening/closing procedures
- Quality standards (food preparation, presentation, timing)
- Equipment maintenance
- Health and safety
- Waste management
- Supplier receiving procedures
- Mystery shopper / quality audit procedures

### Marketing Policies
- Brand usage guidelines (logo, colors, tone — cross-ref with brand-guidelines skill)
- Social media policy (who posts, approval process, crisis response)
- Campaign approval workflow
- Local marketing guidelines (what's allowed, budget, materials)
- PR and media handling
- Influencer/partnership guidelines
- Photography/video usage rights

### HR Policies
- Recruitment and hiring process
- Onboarding program
- Code of conduct
- Anti-discrimination and harassment
- Compensation and benefits
- Training and development
- Performance management
- Termination procedures
- Workplace safety

### Finance Policies
- Expense reporting and approval thresholds
- Procurement process (who can buy what, approval levels)
- Budget ownership and accountability
- Invoice processing
- Cash handling (restaurant-specific)
- Petty cash
- Capital expenditure approval
- Financial reporting requirements

### Guest Support Policies
- Compensation tiers and approval limits
- Refund procedures and timelines
- Escalation paths and contacts
- Response time targets
- Communication tone and templates
- Food safety incident handling
- Legal/compliance escalation triggers
- Data privacy in complaint handling

## How Agents Use This

Before making recommendations or decisions, agents should:
1. Check if `docs/policies/index.md` exists
2. Read the relevant department policy file for their domain
3. Ensure recommendations comply with stated policies
4. Flag when a recommendation would require a policy exception
5. Reference specific policies in decisions and briefings
6. Flag when policies are outdated (review cycle exceeded)

## Updates

- "Update our refund policy — max is now 300 SEK without manager approval" → update guest-support-policies.md
- "Here's our new IT security policy" → create/update it-policies.md
- "Add a social media policy for marketing" → update marketing-policies.md
- Always update the `Last updated` date in the department file and index
- If a policy change affects other departments, update cross-references

## Alerts

- **Missing policies**: Department file doesn't exist but agent needs it — prompt user to provide
- **Stale policies**: Last updated date older than the review cycle — flag for review
- **Policy conflicts**: Recommendation conflicts with a stated policy — flag explicitly
- **Cross-department impact**: Policy change in one department affects another — flag and update
