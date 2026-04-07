---
name: system-architecture
description: Use when documenting the systems landscape, creating IT architecture decision records (ADRs), mapping integrations between systems, maintaining the technology stack, or reviewing infrastructure for a multi-location QSR environment.
---

# System Architecture

Document and maintain the IT architecture for a multi-location QSR restaurant chain. Five living documents covering systems, integrations, decisions, stack, and infrastructure.

## Documents

| Document | File | Purpose |
|----------|------|---------|
| Systems Landscape | `docs/tech/systems-landscape.md` | What systems exist, ownership, criticality |
| Integration Map | `docs/tech/integration-map.md` | How systems connect: APIs, data flows, patterns |
| IT ADRs | `docs/tech/decisions/ADR-NNN-title.md` | Architecture decisions for infrastructure, platforms, integrations |
| Technology Stack | `docs/tech/tech-stack.md` | Versions, hosting, licensing — complements tech-radar |
| Infrastructure Overview | `docs/tech/infrastructure.md` | Per-restaurant setup, central infra, network, DR/BCP |

## Systems Landscape

Save to `docs/tech/systems-landscape.md`:

### Two Input Paths

**Interview Mode**: Walk through systems one by one:
1. What is the system? What does it do?
2. Category? (POS, ITSM, HR, Food Safety, Finance, Digital Customer, Infrastructure)
3. Vendor and contract? (cross-reference vendor-manager)
4. Who owns it internally?
5. How critical is it? (Critical / High / Medium / Low)
6. Cloud, SaaS, or on-premise?
7. Which locations use it? (All 74, specific markets, HQ only)
8. What does it integrate with?

**Import Mode**: User provides existing system lists or diagrams — map to standard format.

### Template

```markdown
# Systems Landscape — Bastard Burgers
> Last updated: YYYY-MM-DD
> Total systems: [n] | Owner: [IT Architect name]

## Summary

| Category | Systems | Most Critical |
|----------|---------|--------------|
| POS & Restaurant Operations | [list] | [which one] |
| ITSM & IT Support | [list] | |
| HR & Internal Communication | [list] | |
| Food Safety & Compliance | [list] | |
| Finance & Accounting | [list] | |
| Digital Customer | [list] | |
| Infrastructure & Networking | [list] | |

## Systems Detail

### [System Name]
> Category: [category] | Criticality: **Critical / High / Medium / Low**
> Vendor: [name] | Contract ref: [link to vendor-manager]
> Owner: [person/team] | Users: [who]
> Hosting: Cloud / SaaS / On-prem / Hybrid
> Locations: All 74 / Sweden only / Finland only / HQ only / [specify]

**Purpose**: [What it does — one sentence]

**Key capabilities**:
- [capability]

**Integrations**: [list — links to integration-map entries]

**Data held**: [What data, classification level]

**Dependencies**:
- Depends on: [systems]
- Depended on by: [systems]

---
```

### Pre-populated Categories for Bastard Burgers

| Category | Known Systems |
|----------|-------------|
| POS & Restaurant Operations | Oracle Simphony, kiosks, payment terminals |
| ITSM & IT Support | FreshService |
| HR & Internal Communication | Ziik |
| Food Safety & Compliance | Get Compliant |
| Employee Engagement | Winningtemp |
| Finance & Accounting | Fortnox (planned) |
| Digital Customer | Bastard Burgers App, loyalty platform, delivery integrations |
| Infrastructure & Networking | Restaurant networking, cloud services, VPN |

## Integration Map

Save to `docs/tech/integration-map.md`:

```markdown
# Integration Map — Bastard Burgers
> Last updated: YYYY-MM-DD
> Total integrations: [n] | Active: [n] | Planned: [n]

## Overview

| Source | Target | Type | Pattern | Direction | Status | Owner |
|--------|--------|------|---------|-----------|--------|-------|
| App | Simphony | Orders | REST API | One-way | Active | [who] |
| Kiosk | Simphony | Orders | REST API | One-way | Active | [who] |
| Simphony | Fortnox | Finance | TBD | One-way | Planned | [who] |

## Integration Details

### [Source] → [Target]
> Type: [what data/function] | Pattern: REST API / File / Event / Batch
> Direction: One-way / Bidirectional
> Frequency: Real-time / Hourly / Daily / On-demand
> Status: Active / Planned / Deprecated
> Owner: [person/team]

**Purpose**: [Why this integration exists]
**Data flow**: [What moves, format, volume]
**Authentication**: [API key / OAuth / Certificate / VPN]
**Error handling**: [Failure behavior, retry, alerting]
**SLA**: [Uptime, latency requirements]
**Dependencies**: [What must be running]

---

## Integration Patterns Used

| Pattern | Used For | Example |
|---------|---------|---------|
| REST API | Real-time operations | App → Simphony |
| Batch/File | Periodic sync | [example] |
| Webhook/Event | Notifications | [example] |

## Planned Integrations

| Integration | Priority | Target Date | ADR | Blocker |
|------------|----------|-------------|-----|---------|
```

## Architecture Decision Records (IT ADRs)

Save to `docs/tech/decisions/ADR-NNN-title.md`. Index at `docs/tech/decisions/README.md`.

**When to use IT ADRs vs. decision-framework:**
- **IT ADR** (`docs/tech/decisions/`): Infrastructure choices, integration patterns, platform decisions, security architecture, IT standards
- **Decision-framework** (`docs/decisions/`): Business/strategy decisions with technology implications

### ADR Template

```markdown
# ADR-[NNN]: [Title]
> Date: YYYY-MM-DD | Status: Proposed / Accepted / Deprecated / Superseded
> Author: [name] | Reviewers: [names]
> Category: Infrastructure / Integration / Platform / Security / Standard
> Impact: [which systems and locations affected]

## Context
[Why this decision is needed — business driver, technical trigger, or problem]

## Decision Drivers
- [Driver 1]
- [Driver 2]

## Options Considered

### Option A: [Name]
**Description**: [What this entails]
**Pros**: [Advantages]
**Cons**: [Disadvantages]
**Cost**: [Estimate]
**Risk**: [Low/Medium/High]

### Option B: [Name]
[Same structure]

## Decision
[What was decided]

## Rationale
[Why this option over others]

## Consequences
- **Positive**: [Benefits]
- **Negative**: [Trade-offs]
- **Affected systems**: [From systems-landscape]
- **Affected locations**: [All 74 / Sweden / Finland / Norway / specific]

## Implementation
- [ ] [Step] — Owner: [who] — By: [when]

## Review
- **Review date**: [When to revisit]
- **Success criteria**: [How to measure]
```

### ADR Index Template

```markdown
# IT Architecture Decision Log
> Last updated: YYYY-MM-DD

| # | Date | Decision | Category | Status | Impact |
|---|------|----------|----------|--------|--------|
| ADR-001 | YYYY-MM-DD | [Title] | [Category] | Accepted | [Scope] |
```

## Technology Stack

Save to `docs/tech/tech-stack.md`:

```markdown
# Technology Stack — Bastard Burgers
> Last updated: YYYY-MM-DD

## Stack Overview

| Layer | Technology | Version | Hosting | License | Owner |
|-------|-----------|---------|---------|---------|-------|
| POS | Oracle Simphony | [ver] | Cloud | [type] | Kim Axelsson |
| ITSM | FreshService | [tier] | SaaS | [type] | André Ejneborn |
| HR/Intranet | Ziik | [ver] | SaaS | [type] | [owner] |
| Food Safety | Get Compliant | [ver] | SaaS | [type] | [owner] |
| Engagement | Winningtemp | [ver] | SaaS | [type] | [owner] |
| Finance | Fortnox | [ver] | SaaS | [type] | Filip Forsling |

## By Layer

### Restaurant Technology
POS, kiosks, kitchen displays, payment terminals, self-ordering

### Business Applications
ITSM, HR, finance, food safety, engagement

### Digital Customer
App, web ordering, loyalty, delivery platform integrations

### Infrastructure
Cloud services, networking, security, monitoring, backup

## Version & Lifecycle

| Technology | Current | Latest Available | Upgrade Path | Next Review |
|-----------|---------|-----------------|-------------|-------------|
```

## Infrastructure Overview

Save to `docs/tech/infrastructure.md`:

```markdown
# Infrastructure Overview — Bastard Burgers
> Last updated: YYYY-MM-DD
> Restaurants: 74 | Countries: 3 (Sweden, Finland, Norway)

## Restaurant Standard Setup (per location)

| Component | Standard | Variations | Notes |
|-----------|----------|-----------|-------|
| POS terminals | [count/type] | | |
| Kiosks | [count/type] | | |
| Network connection | [ISP/type] | | |
| Back-office | [yes/no] | | |
| Payment terminals | [type] | | |

## Central Infrastructure

| Service | Provider | Type | Purpose |
|---------|----------|------|---------|
| [service] | [provider] | Cloud/On-prem | [purpose] |

## Network Architecture
[How restaurants connect to central systems — VPN, direct, redundancy]

## Environments

| Environment | Purpose | Access |
|------------|---------|--------|
| Production | Live restaurant operations | Restricted |
| Staging/Test | Pre-deployment testing | IT team |
| Development | Development work | Developers |

## Disaster Recovery & Business Continuity

| Scenario | Impact | Recovery Plan | RTO | RPO |
|----------|--------|--------------|-----|-----|
| POS outage (single restaurant) | Cannot take orders | [plan] | [time] | [time] |
| POS outage (chain-wide) | All restaurants affected | [plan] | [time] | [time] |
| Internet down at restaurant | [impact] | [plan] | [time] | [time] |
| Central system outage | [impact] | [plan] | [time] | [time] |
| Data breach | [impact] | [plan] | [time] | [time] |

## Capacity & Growth

| Metric | Current | 12-Month Projection | Scaling Action |
|--------|---------|-------------------|----------------|
| Restaurant count | 74 | [projected] | [implications] |
| Transaction volume | [current] | [projected] | [implications] |
```

## Consistency Check

When updating any document, check cross-references:

| If You Update... | Also Check... |
|-----------------|---------------|
| Systems Landscape (add/remove system) | Integration Map, Tech Stack, Tech Radar |
| Integration Map (add/change integration) | Systems Landscape (both endpoints exist?), ADR (decision documented?) |
| ADR (new decision) | Systems Landscape (affected systems noted?), Integration Map (if integration-related) |
| Tech Stack (version change) | Systems Landscape, ADR (upgrade decision documented?) |
| Infrastructure (change) | Systems Landscape, DR/BCP section (recovery plans still valid?) |

## How Agents Use This

Before making infrastructure or architecture recommendations:
1. Check `docs/tech/systems-landscape.md` — understand what systems exist
2. Check `docs/tech/integration-map.md` — understand how systems connect before suggesting changes
3. Check `docs/tech/decisions/README.md` — don't re-litigate settled architecture decisions
4. Cross-reference `docs/vendors/vendor-register.md` for contract/cost context
5. Cross-reference `docs/tech/tech-radar.md` for technology adoption status
6. Cross-reference `docs/projects/portfolio.md` for in-flight work affecting architecture

## QSR-Specific Considerations

- **POS is the heartbeat**: Oracle Simphony drives all restaurant operations. Never recommend changes that risk POS uptime without explicit risk assessment.
- **74 locations = 74x impact**: Every architecture decision affects multiple restaurants. A bad deploy doesn't hit one server — it hits 74 restaurants across 3 countries.
- **Lean team (8 people)**: Prefer managed services over self-hosted, SaaS over custom-built. The team can't operate complex infrastructure.
- **Cashflow & EBITDA focus**: Architecture recommendations must consider cost impact. Per 2025 strategy, this isn't the year for big infrastructure investments — it's the year to optimize what exists.
- **Multi-market compliance**: Sweden, Finland, and Norway have different regulatory requirements. Architecture must accommodate market-specific needs without fragmentation.
