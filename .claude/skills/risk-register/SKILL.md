---
name: risk-register
description: Use when the user wants to identify, track, or review organizational risks, prepare risk reporting for the board, assess risk impact of decisions, or when agents need risk context before making recommendations.
---

# Risk Register

Maintain a living register of organizational risks so agents can factor risk into recommendations and C-levels can report confidently to the board.

## Risk Categories

| Category | Examples |
|----------|---------|
| **Cybersecurity** | Data breach, ransomware, access control gaps, third-party vulnerabilities |
| **Technology** | Technical debt, platform obsolescence, single points of failure, scaling limits |
| **Vendor** | Vendor lock-in, service disruption, contract disputes, price increases |
| **Talent** | Key person dependency, skill gaps, attrition, hiring challenges |
| **Compliance** | GDPR, NIS2, ISO 27001, SOC 2, industry regulations, audit findings |
| **Financial** | Budget overruns, unexpected costs, currency exposure, funding gaps |
| **Operational** | Process failures, integration issues, disaster recovery gaps |
| **Strategic** | Market shifts, competitor moves, misaligned investments |

Adapt categories to the organization. Not all apply everywhere.

## Two Input Paths

### Interview Mode

Walk through each relevant category:
1. For each category, ask: "What keeps you up at night in [category]?"
2. For each identified risk, capture: description, likelihood, impact, current mitigation, owner
3. Ask about risk appetite: "How much risk is the organization willing to accept?"
4. Ask about existing risk processes: audits, reviews, insurance, compliance programs

### Import Mode

If the user has existing risk documentation:
1. Read provided documents
2. Map to the standard format
3. Identify gaps in coverage or scoring
4. Ask follow-up questions

## Output Format

Save to `docs/risk/risk-register.md`:

```markdown
# Risk Register
> Last updated: YYYY-MM-DD
> Total risks: [n] | Critical: [n] | High: [n] | Medium: [n] | Low: [n]

## Risk Matrix Summary

|  | Low Impact | Medium Impact | High Impact | Critical Impact |
|--|-----------|--------------|------------|----------------|
| **Very Likely** | | | | |
| **Likely** | | | | |
| **Possible** | | | | |
| **Unlikely** | | | | |

## Critical & High Risks

### RISK-001: [Risk Title]
> Category: [category] | Score: [Critical/High/Medium/Low]
> Likelihood: [1-4] | Impact: [1-4] | Risk Score: [L x I]
> Owner: [person] | Status: [Open/Mitigating/Accepted/Closed]
> Identified: [date] | Last reviewed: [date]

**Description**: [What could happen and why]

**Current controls**: [What's already in place]

**Mitigation plan**:
- [ ] [Action] — Owner: [who] — By: [when]

**Residual risk**: [Risk level after mitigations are in place]

**Trigger indicators**: [Early warning signs to watch for]

---

[Repeat for each risk, ordered by score descending]

## Risk Appetite Statement
[Organization's stated tolerance for risk by category]

## Review Schedule
| Review Type | Frequency | Next Review | Owner |
|------------|-----------|-------------|-------|
| Full register review | [Quarterly] | [date] | [who] |
| Critical risks check | [Monthly] | [date] | [who] |
| Board risk report | [Quarterly] | [date] | [who] |
```

## Scoring Guide

**Likelihood**: 1 = Unlikely | 2 = Possible | 3 = Likely | 4 = Very Likely

**Impact**: 1 = Low (minor disruption) | 2 = Medium (significant but recoverable) | 3 = High (major damage, lengthy recovery) | 4 = Critical (existential threat, regulatory action)

**Risk Score** = Likelihood x Impact (1-16)
- **Critical**: 12-16
- **High**: 8-11
- **Medium**: 4-7
- **Low**: 1-3

## Updates

- "We had a security audit — add the findings as risks" — create new risk entries
- "RISK-003 has been mitigated, close it" — update status to Closed
- "Increase the likelihood on RISK-005" — adjust scoring and re-sort
- Always update `Last updated` and summary counts
- When closing a risk, keep it in the register with Closed status (don't delete)

## How Agents Use This

Before making recommendations, agents should:
1. Check if `docs/risk/risk-register.md` exists
2. Identify risks relevant to the current topic
3. Flag when a recommendation could increase an existing risk
4. Flag when a recommendation could mitigate an existing risk
5. Reference risk register in stakeholder briefings and board updates
6. Cross-reference with vendor-manager for vendor-related risks

## Alerts

- **Overdue reviews**: Risk not reviewed in 90+ days
- **Unowned risks**: Risks without an assigned owner
- **Mitigation stalls**: Action items past their due date
- **Risk concentration**: Too many high risks in one category
- **New risk triggers**: When decisions or project changes introduce new risk exposure
