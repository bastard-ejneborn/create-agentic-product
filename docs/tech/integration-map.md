# Integration Map — Bastard Burgers
> Last updated: 2026-04-08
> Total integrations: 19 active | 1 planned | Owner: André Ejneborn, Senior IT Architect

## Overview

| # | Source | Target | Type | Pattern | Direction | Status | Owner |
|---|--------|--------|------|---------|-----------|--------|-------|
| 1 | Future Ordering | Simphony | Digital orders | Simphony Transaction Services API | One-way | Active | Simon Brännström |
| 2 | Deliverect | Simphony | Delivery orders | Simphony Transaction Services API | One-way | Active | Kim Axelsson |
| 3 | Planet Terminals | Simphony | Payments | Ethernet/IP (per POS) | Bidirectional | Active | Johnny Bröms |
| 4 | Future Ordering | Como | Loyalty | API (TBD) | Bidirectional | Active | Simon Brännström |
| 5 | Como | Simphony | Loyalty redemption | TBD | TBD | Active | TBD |
| 6 | Delivery platforms | Deliverect | Delivery orders | Platform APIs | Bidirectional | Active | Kim Axelsson |
| 7 | Future Ordering | Planet/Payment | Digital payments | API | One-way | Active | Simon Brännström |
| 8 | Caspeco | Ziik | User account creation | API/Automation | One-way | Active | TBD |
| 9 | Entra ID | NinjaOne | SSO (SAML) | SAML 2.0 | Bidirectional | Active | André Ejneborn |
| 10 | Entra ID | Google Workspace/Cloud Identity | SSO + Provisioning | SAML 2.0 + SCIM | Bidirectional | Active | TBD |
| 10b | Google Cloud Identity | FO Navigator | User authentication | Google Sign-In | One-way | Active | Simon Brännström |
| 11 | Entra ID | Exchange Online | Identity + Email | Native M365 | Bidirectional | Active | TBD |
| 12 | Entra ID | Intune | Device management | Native M365 | Bidirectional | Active | TBD |
| 13 | Entra ID | FreshService | SSO (SAML) | SAML 2.0 | Bidirectional | Active | André Ejneborn |
| 14 | Entra ID | Dropbox Business | SSO | SAML 2.0 | Bidirectional | Active | TBD |
| 15 | Caspeco | Como | Staff pricing import | File/API | One-way | Active | TBD |
| 16 | FreshService | n8n Cloud | Ticket data (Helpdesk AI) | REST API | One-way | Active | André Ejneborn |
| 17 | n8n Cloud | OpenAI | LLM + Embeddings | REST API | Bidirectional | Active | André Ejneborn |
| 18 | n8n Cloud | Supabase | Knowledge store | REST API | Bidirectional | Active | André Ejneborn |
| 19 | n8n Cloud | FreshService | Solutions sync | REST API | Bidirectional | Active | André Ejneborn |
| 20 | Simphony | Fortnox | Finance data | TBD | One-way | Planned | TBD |

## Integration Details

### 1. Future Ordering → Simphony
> Type: Digital orders (app, kiosk, web) | Pattern: **Simphony Transaction Services API (Gen 2)**
> Direction: One-way (FO → Simphony)
> Frequency: Real-time (per order)
> Status: **Active**
> Owner: Simon Brännström

**Purpose**: Orders placed through the Bastard Burgers app, self-service kiosks, and web ordering are injected into Simphony for kitchen preparation and fulfillment.

**Data flow**: Order details (items, modifiers, quantities, customer info) → Simphony check/order

**Authentication**: TBD (verify — API key, OAuth, or certificate)

**Error handling**: TBD (verify — what happens if Simphony is unreachable? Queue? Retry? Fail?)

**SLA**: TBD (verify — expected latency, uptime requirement)

**Dependencies**: Simphony must be running and accepting orders. Restaurant must have internet.

---

### 2. Deliverect → Simphony
> Type: Delivery platform orders | Pattern: **Simphony Transaction Services API (Gen 2)**
> Direction: One-way (Deliverect → Simphony)
> Frequency: Real-time (per order)
> Status: **Active**
> Owner: Kim Axelsson

**Purpose**: Orders from third-party delivery platforms (Uber Eats, Foodora, Wolt, etc.) are aggregated by Deliverect and injected into Simphony for kitchen preparation.

**Data flow**: Delivery order details (items, modifiers, delivery info) → Simphony check/order

**Authentication**: TBD (verify — same as FO or separate credentials?)

**Error handling**: TBD (verify — what happens if order injection fails? Delivery platform shows accepted but kitchen doesn't get order?)

**SLA**: TBD

**Dependencies**: Simphony must be running. Delivery platforms must be connected to Deliverect.

---

### 3. Planet Terminals ↔ Simphony
> Type: Payment processing | Pattern: **Ethernet/IP (direct connection per POS terminal)**
> Direction: Bidirectional
> Frequency: Real-time (per transaction)
> Status: **Active**
> Owner: Johnny Bröms

**Purpose**: Payment terminals communicate with the POS to receive transaction amounts and send payment confirmations. Each Planet terminal is physically connected to its Simphony POS workstation via ethernet.

**Data flow**:
- Simphony → Planet: Transaction amount, order reference
- Planet → Simphony: Payment confirmation, card type, approval code

**Authentication**: Local network (ethernet cable, no internet required for POS ↔ terminal communication)

**Error handling**: TBD (verify — what happens if terminal disconnects? Can POS still operate? Manual payment fallback?)

**SLA**: Hardware-level — dependent on physical connection and terminal health

**Dependencies**: Local network functioning. Planet processing infrastructure (for card authorization).

---

### 4. Future Ordering ↔ Como
> Type: Loyalty program | Pattern: **API** (details TBD)
> Direction: Bidirectional
> Frequency: Real-time (per order/member action)
> Status: **Active**
> Owner: Simon Brännström

**Purpose**: Loyalty program integration — FO sends customer/order data to Como for points accrual, and reads member data/offers from Como to display in the app.

**Data flow**:
- FO → Como: Customer identification, order details (for point earning)
- Como → FO: Member profile, points balance, available offers/rewards

**Authentication**: TBD

**Error handling**: TBD (verify — what happens if Como is down? Can customers still order without loyalty? Do they lose points?)

**SLA**: TBD

**Dependencies**: Both FO and Como must be operational for loyalty features.

---

### 5. Como ↔ Simphony
> Type: Loyalty redemption at POS | Pattern: TBD
> Direction: TBD
> Frequency: Per transaction (when loyalty is used)
> Status: **Active** (verify)
> Owner: TBD

**Purpose**: When guests redeem loyalty rewards or earn points at the POS (not through the app), Como needs to communicate with Simphony.

**Data flow**: TBD — verify if Como integrates directly with Simphony at the POS level, or only via Future Ordering.

**Open question**: Does Como connect directly to Simphony, or does all loyalty flow through Future Ordering? If a guest shows their loyalty code at the counter (not via app), how is it processed?

---

### 6. Delivery Platforms → Deliverect
> Type: Delivery orders | Pattern: **Platform APIs**
> Direction: Bidirectional
> Frequency: Real-time
> Status: **Active**
> Owner: Kim Axelsson

**Purpose**: Third-party delivery platforms send orders to Deliverect, which normalizes them before injecting into Simphony.

**Connected platforms** (verify complete list):
- Uber Eats
- Foodora
- Wolt
- Others? (verify)

**Data flow**:
- Platforms → Deliverect: Orders, menu updates, availability changes
- Deliverect → Platforms: Order confirmations, status updates, menu sync

**Authentication**: Per-platform API credentials managed in Deliverect

**Error handling**: Deliverect handles platform-specific error formats and normalizes

**Dependencies**: Each delivery platform's API availability

---

### 7. Future Ordering → Payment Processing
> Type: Digital payments | Pattern: **API**
> Direction: One-way (payment request)
> Frequency: Per digital order
> Status: **Active**
> Owner: Simon Brännström

**Purpose**: When customers pay through the app or web ordering, Future Ordering processes the payment.

**Data flow**: FO sends payment request → payment processor → confirmation back to FO

**Open question**: Does FO use Planet for digital payments too, or a different payment processor (e.g., Adyen, Stripe, Nets)? Digital payments may route differently than in-store terminal payments.

---

### 8. Caspeco → Ziik
> Type: User account provisioning | Pattern: **API/Automation** (details TBD)
> Direction: One-way (Caspeco → Ziik)
> Frequency: On employee creation/change
> Status: **Active**
> Owner: TBD

**Purpose**: When a new employee is created in Caspeco (workforce management), a user account is automatically created in Ziik (internal communication platform). **Not SSO** — this is account provisioning only. Employees have separate credentials for each system.

**Data flow**: Employee name, email, role/location → Ziik user account

**Authentication**: TBD

**Error handling**: TBD (verify — what happens if Ziik account creation fails? Manual fallback?)

**SLA**: TBD

**Dependencies**: Caspeco must have employee data. Ziik must be accessible.

**Note**: No SSO exists between any systems. This is a one-way account creation integration, not authentication federation.

---

### 9. Simphony → Fortnox (PLANNED)
> Type: Finance/accounting data | Pattern: TBD
> Direction: One-way (Simphony → Fortnox)
> Frequency: TBD (daily batch? real-time?)
> Status: **Planned**
> Owner: TBD

**Purpose**: Automate the flow of sales data from Simphony into Fortnox for accounting — replacing manual entry or reconciliation.

**Data flow**: Daily sales totals, tax collected, payment method breakdown → Fortnox journal entries

**Research**: Full Fortnox API research documented at `docs/superpowers/specs/2026-04-02-fortnox-integration-research.md`. Integration parked due to OAuth2 multi-company complexity.

**Dependencies**: Fortnox API access (multi-company token management), Simphony BI API (data source)

---

## Integration Architecture

```
                    ┌─────────────────┐
                    │   Delivery      │
                    │   Platforms     │
                    │ (Uber, Foodora, │
                    │  Wolt, etc.)    │
                    └────────┬────────┘
                             │ Platform APIs
                             ▼
┌──────────┐    ┌────────────────────┐    Simphony TX    ┌──────────────────┐
│          │    │                    │    Services API    │                  │
│   Como   │◄──►│  Future Ordering   │──────────────────►│                  │
│ (Loyalty)│    │  (App/Kiosk/Web)   │                   │  Oracle Simphony │
│          │    └────────────────────┘                   │     (POS)        │
└──────────┘                                            │                  │
                 ┌────────────────────┐    Simphony TX   │   All 74         │
                 │                    │    Services API   │   Restaurants    │
                 │    Deliverect      │─────────────────►│                  │
                 │  (Delivery mgmt)   │                  │                  │
                 └────────────────────┘                  │                  │
                                                        │                  │◄──► Planet Terminals
                                                        │                  │     (Ethernet/IP)
                                                        └────────┬─────────┘
                                                                 │
                                                                 │ Planned
                                                                 ▼
                                                        ┌──────────────────┐
                                                        │     Fortnox      │
                                                        │   (Finance)      │
                                                        └──────────────────┘

                 ┌──────────────┐
                 │   Caspeco    │
                 │ (Workforce)  │
                 └──────┬───────┘
                        │ User account creation
                        ▼
                 ┌──────────────┐
                 │     Ziik     │
                 │  (Intranet)  │
                 └──────────────┘

                 ┌──────────────────────────────────────────────┐
                 │          Microsoft Entra ID                  │
                 │        (Central Identity Provider)           │
                 └──┬──────────┬──────────┬──────────┬─────────┘
                    │          │          │          │
                    ▼          ▼          ▼          ▼
              ┌──────────┐ ┌────────┐ ┌────────┐ ┌──────────┐
              │ NinjaOne │ │Exchange│ │ Intune │ │ Google   │
              │ (SSO)    │ │ Online │ │ (MDM)  │ │Workspace │
              └──────────┘ │(Email) │ └────────┘ │(legacy)  │
                           └────────┘            └──────────┘

Standalone Systems (no integrations documented):
┌────────────┐  ┌───────────────┐  ┌──────────────┐
│ FreshService│  │ Get Compliant │  │  Winningtemp │
│   (ITSM)   │  │ (Food Safety) │  │ (Engagement) │
└────────────┘  └───────────────┘  └──────────────┘

Infrastructure (underlies everything):
┌──────────────────────────────────────────────────┐
│          Global Connect (Network Provider)        │
│  All 74 restaurants — internet, switching, IPs    │
└──────────────────────────────────────────────────┘
```

## Integration Patterns Used

| Pattern | Used For | Systems |
|---------|---------|---------|
| Simphony Transaction Services API (Gen 2) | Order injection into POS | FO → Simphony, Deliverect → Simphony |
| Ethernet/IP (local) | Payment terminal communication | Planet ↔ Simphony |
| Platform APIs | Delivery platform aggregation | Uber/Foodora/Wolt → Deliverect |
| API (details TBD) | Loyalty | FO ↔ Como |
| SAML 2.0 | Single Sign-On | Entra ID → NinjaOne, Entra ID → Google Workspace |
| Native M365 | Microsoft platform integration | Entra ID ↔ Exchange Online, Entra ID ↔ Intune |
| API/Automation | User provisioning | Caspeco → Ziik |

## Planned Integrations

| Integration | Priority | Target Date | ADR | Blocker |
|------------|----------|-------------|-----|---------|
| Simphony → Fortnox | Medium | TBD | None yet | Fortnox OAuth2 multi-company complexity |

## Gaps & Questions

- [ ] **Como ↔ Simphony direct integration** — does Como connect directly to Simphony at the POS, or does all loyalty flow through Future Ordering only?
- [ ] **FO digital payment processor** — does Future Ordering use Planet for digital payments, or a different processor (Adyen, Stripe, Nets)?
- [ ] **FO → Simphony error handling** — what happens when Simphony is unreachable? Queue, retry, or fail?
- [ ] **Deliverect → Simphony error handling** — same question. Failed injection = delivery platform shows accepted but kitchen has no order?
- [ ] **Planet fallback** — if a terminal disconnects, can the POS still operate? Manual payment fallback process?
- [ ] **Delivery platforms complete list** — which platforms exactly? Uber Eats, Foodora, Wolt — any others?
- [ ] **FO ↔ Como authentication** — API key, OAuth, or other?
- [ ] **Simphony → Fortnox data mapping** — what specific data should flow? Daily totals only, or transaction-level?
- [ ] **Any system sending data to Winningtemp?** — e.g., employee lists from an HR system?
- [ ] **Any system sending data to Get Compliant?** — e.g., restaurant/location master data?
- [ ] **FreshService → any monitoring integration?** — auto-created tickets from system alerts?
- [ ] **NinjaOne → FreshService integration?** — do hardware alerts in NinjaOne auto-create FreshService tickets?
