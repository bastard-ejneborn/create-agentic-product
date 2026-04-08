# Systems Landscape — Bastard Burgers
> Last updated: 2026-04-08
> Total systems: 13 | Owner: André Ejneborn, Senior IT Architect

## Summary

| Category | Systems | Most Critical |
|----------|---------|--------------|
| POS & Restaurant Operations | Oracle Simphony, Planet Payment Terminals | Oracle Simphony |
| Digital Ordering | Future Ordering (app, kiosk, web) | Future Ordering |
| Loyalty | Como | Como |
| Delivery | Deliverect | Deliverect |
| ITSM & IT Support | FreshService (Pro + Asset) | FreshService |
| Endpoint Management | NinjaOne RMM | NinjaOne |
| HR & Internal Communication | Ziik | Ziik |
| Food Safety & Compliance | Get Compliant | Get Compliant |
| Workforce Management | Caspeco | Caspeco |
| Employee Engagement | Winningtemp | Winningtemp |
| Finance & Accounting | Fortnox | Fortnox |

## Systems Detail

### Oracle Simphony
> Category: POS & Restaurant Operations | Criticality: **Critical**
> Vendor: Oracle | Contract ref: TBD (see vendor-manager when set up)
> Owner: Johnny Bröms (CDTO) | Managed by: Petron Fernandes, Roopneet Bhalla
> Hosting: **Cloud (Oracle shared environment)**
> Locations: **All 74 restaurants**

**Purpose**: Core POS system — handles all restaurant transactions, order management, menu configuration, and reporting across the entire chain.

**Key capabilities**:
- Order entry and management (dine-in, takeout, delivery)
- Menu and product configuration
- Price management
- Revenue center management
- Employee time and attendance
- Sales reporting and BI (via BI API)
- Kitchen display integration

**Integrations**:
- Future Ordering → Simphony (digital orders from app, kiosks, web)
- Deliverect → Simphony (delivery platform orders)
- Planet terminals ↔ Simphony (payment processing, ethernet/IP per POS)
- Simphony → BI API (reporting data, read-only — integrated via `simphony` skill)

**Data held**: All transaction data, menu configuration, employee records, sales history, guest check details. **Business-critical data**.

**Dependencies**:
- Depends on: Internet connectivity (per restaurant), Oracle Cloud infrastructure
- Depended on by: Future Ordering, Deliverect, Planet payments, BI reporting, all restaurant operations

**Known issues / upcoming**:
- ⚠️ **Product redesign planned** — current product configuration is not built/configured optimally. Redesign work being scoped.

---

### Future Ordering (FO)
> Category: Digital Ordering | Criticality: **Critical**
> Vendor: Future Ordering (third-party) | Contract ref: TBD
> Owner: Simon Brännström (IT Architect)
> Hosting: **SaaS** (Future Ordering's platform)
> Locations: **All 74 restaurants** (app, kiosk, web ordering)

**Purpose**: Digital ordering platform powering the Bastard Burgers mobile app, self-service kiosks, and web ordering. Orders flow through FO into Simphony.

**Key capabilities**:
- Mobile app (Bastard Burgers branded app)
- Self-service kiosk ordering
- Web ordering
- Menu sync with Simphony
- Loyalty program integration
- Digital payment processing

**Integrations**:
- Future Ordering → Simphony (order injection)
- Future Ordering ↔ Loyalty platform (member data, points, offers)
- Future Ordering ↔ Planet/payment provider (digital payments)

**Data held**: Digital order history, customer accounts, loyalty data, app usage analytics.

**Dependencies**:
- Depends on: Simphony (order destination), internet connectivity
- Depended on by: Mobile app users, kiosk users, web ordering users

---

### Deliverect
> Category: Delivery | Criticality: **High**
> Vendor: Deliverect | Contract ref: TBD
> Owner: Kim Axelsson (POS Architect)
> Hosting: **SaaS**
> Locations: **All locations with delivery** (verify scope)

**Purpose**: Middleware that aggregates all third-party delivery platform orders (Uber Eats, Foodora, Wolt, etc.) and pushes them into Simphony.

**Key capabilities**:
- Multi-platform delivery aggregation
- Menu sync to delivery platforms
- Order injection to POS (Simphony)
- Delivery platform management (pricing, availability, hours)

**Integrations**:
- Delivery platforms (Uber Eats, Foodora, Wolt, etc.) → Deliverect
- Deliverect → Simphony (order injection)

**Data held**: Delivery order data, platform configuration, menu mappings.

**Dependencies**:
- Depends on: Simphony (order destination), delivery platform APIs
- Depended on by: All third-party delivery operations

---

### Planet Payment Terminals
> Category: POS & Restaurant Operations | Criticality: **Critical**
> Vendor: Planet | Contract ref: TBD
> Owner: Johnny Bröms (CDTO)
> Hosting: **On-premise** (physical terminals in each restaurant)
> Locations: **All 74 restaurants**

**Purpose**: Payment processing terminals at each POS station. Handles card payments, contactless, and mobile pay.

**Key capabilities**:
- Card payments (chip, contactless, swipe)
- Mobile payments (Apple Pay, Google Pay)
- Integration with POS for amount and receipt

**Integrations**:
- Planet ↔ Simphony (ethernet/IP connection per POS terminal)

**Data held**: Transaction records, payment data (PCI-compliant — Planet handles sensitive card data).

**Dependencies**:
- Depends on: Simphony POS, local network (ethernet), Planet processing infrastructure
- Depended on by: All payment processing at all restaurants

---

### Como
> Category: Loyalty | Criticality: **High**
> Vendor: Como | Contract ref: TBD
> Owner: TBD (verify — Simon Brännström? Marketing?)
> Hosting: **SaaS**
> Locations: **All 74 restaurants** (via app + POS)

**Purpose**: Loyalty program platform powering Bastard Burgers' customer loyalty — member management, points accrual, rewards, offers, and engagement campaigns.

**Key capabilities**:
- Member registration and management
- Points accrual and redemption
- Offers, rewards, and campaigns
- Customer segmentation
- Analytics and reporting

**Integrations**:
- Como ↔ Future Ordering (loyalty in app/kiosk/web — points, offers, redemption)
- Como ↔ Simphony (POS-level loyalty — verify if direct or via FO only)

**Data held**: Customer profiles, loyalty points, transaction history, offer redemptions, engagement data. **Customer personal data — GDPR relevant**.

**Dependencies**:
- Depends on: Future Ordering (for digital loyalty), potentially Simphony (for POS loyalty)
- Depended on by: App loyalty features, customer retention strategy

**Strategic context**: Loyalty program was flagged as underperforming in Year 1 (red status). 2025 priority: drive loyalty growth (members and visit frequency).

---

### FreshService
> Category: ITSM & IT Support | Criticality: **High**
> Vendor: Freshworks | Contract ref: TBD
> Owner: Johnny Bröms (CDTO)
> Hosting: **SaaS**
> Plan: **Pro + Asset Management add-on**
> Locations: **HQ + all restaurants** (for ticket submission)

**Purpose**: IT Service Management platform for helpdesk tickets, asset tracking, change management, and IT support across the organization.

**Key capabilities**:
- Incident management (IT tickets)
- Asset management (hardware tracking across 74 locations)
- Change management
- Problem management
- SLA tracking and reporting
- Self-service portal
- BI API integration (read-only, via `freshservice` skill)

**Integrations**:
- FreshService API → reporting skill (read-only dashboard, SLA metrics)

**Data held**: IT tickets, asset inventory, change records, SLA data, agent performance.

**Dependencies**:
- Depends on: Internet, Freshworks cloud
- Depended on by: IT support operations, asset tracking, change management processes

---

### NinjaOne RMM
> Category: Endpoint Management | Criticality: **High**
> Vendor: NinjaOne | Contract ref: TBD
> Owner: TBD (verify — André Ejneborn? Christian Ling? IT Support?)
> Hosting: **SaaS**
> Locations: **All 74 restaurants** (manages on-site hardware)

**Purpose**: Remote Monitoring and Management (RMM) platform for managing restaurant hardware endpoints — Express kiosks, POS workstations, and Kitchen Display System (KDS) units across all locations.

**Key capabilities**:
- Device inventory (kiosks, POS workstations, KDS units)
- OS and software patching
- Remote access and troubleshooting
- Endpoint monitoring and alerting
- Software deployment
- Hardware health monitoring

**Managed device types**:
- **Express kiosks** — self-service ordering terminals
- **POS Workstations** — Simphony POS hardware at each restaurant
- **KDS units** — Kitchen Display Systems showing orders to kitchen staff

**Integrations**:
- None documented (standalone — manages hardware directly via agent installed on endpoints)
- Potential: NinjaOne → FreshService? (verify — auto-create tickets on hardware alerts?)

**Data held**: Device inventory, hardware specs, patch status, software versions, remote access logs. **Infrastructure management data**.

**Dependencies**:
- Depends on: Internet (for cloud management), NinjaOne agent installed on each endpoint
- Depended on by: IT Support (for remote troubleshooting), patching/security compliance

**Note**: This answers the open question about KDS — Bastard Burgers does use Kitchen Display Systems, managed alongside kiosks and POS workstations through NinjaOne.

---

### Ziik
> Category: HR & Internal Communication | Criticality: **Medium**
> Vendor: Ziik | Contract ref: TBD
> Owner: HR (Maja Lundqvist, CPO)
> Hosting: **SaaS**
> Locations: **All restaurants + HQ**

**Purpose**: Internal social media platform and document storage for all Bastard Burgers staff. Used for communication (weekly newsletters), policy distribution, how-to guides, and operational handbooks.

**Key capabilities**:
- Internal social feed (company news, updates)
- Document storage (policies, handbooks, how-to guides)
- Weekly newsletter distribution
- HR Toolbox (workplace policies, employment documents)
- Operations manuals and checklists

**Integrations**:
- None documented (standalone platform)

**Data held**: Internal communications, company documents, policy documents, employee-facing content.

**Dependencies**:
- Depends on: Internet
- Depended on by: All staff for internal communication, policy access, onboarding materials

**References in policies**:
- Operations role descriptions reference Ziik extensively (handbooks, HR Toolbox, weekly newsletters)
- O.S.T. and L.A.S.T. service rules stored in Ziik → Handböcker → Operations
- Employment documents signed and stored in Ziik → Handböcker → HR Toolbox

---

### Get Compliant
> Category: Food Safety & Compliance | Criticality: **High**
> Vendor: Get Compliant | Contract ref: TBD
> Owner: Jonas Ylinenjärvi (F&B Manager)
> Hosting: **SaaS**
> Locations: **All 74 restaurants**

**Purpose**: Digital food safety and compliance platform. Used for daily checklists, temperature monitoring, hygiene audits, and regulatory compliance at all restaurants.

**Key capabilities**:
- Food safety checklists (daily, opening, closing)
- Temperature logging
- Hygiene audit tracking
- Compliance scoring (target: 100% per restaurant)
- Deviation reporting

**Integrations**:
- None documented (standalone platform)

**Data held**: Food safety records, audit results, compliance scores, temperature logs. **Regulatory data** — may need retention per food safety regulations.

**Dependencies**:
- Depends on: Internet, restaurant staff completing checklists
- Depended on by: Food safety compliance, operations reviews (DMs and RMs track Get Compliant scores)

**References in policies**:
- All leadership role descriptions (RC, ARC, SL) reference "ensure 100% in Get Compliant"

---

### Caspeco
> Category: Workforce Management | Criticality: **Critical**
> Vendor: Caspeco | Contract ref: TBD
> Owner: TBD (verify — HR? Operations? IT?)
> Hosting: **SaaS** (verify)
> Locations: **All restaurants + HQ**

**Purpose**: Workforce management platform handling salaries, scheduling, time management, and employee records across the organization.

**Key capabilities**:
- Salary/payroll processing
- Operations scheduling (shift planning)
- Time management (clock in/out, hours tracking)
- Employee records and master data

**Integrations**:
- Caspeco → Ziik (user account creation — not SSO, just account provisioning)
- Caspeco → Fortnox? (verify — salary data to accounting?)

**Data held**: Employee personal data, salary information, work schedules, time records, employment history. **Highly sensitive HR/payroll data — GDPR critical**.

**Dependencies**:
- Depends on: Internet
- Depended on by: Payroll processing, scheduling, Ziik (for user account creation), restaurant operations (shift schedules)

---

### Winningtemp
> Category: Employee Engagement | Criticality: **Medium**
> Vendor: Winningtemp | Contract ref: TBD
> Owner: HR (Maja Lundqvist, CPO / Therese Alm, HR Business Partner)
> Hosting: **SaaS**
> Locations: **All restaurants + HQ**

**Purpose**: Employee engagement survey platform. Measures staff satisfaction, engagement trends, and provides insights for management.

**Key capabilities**:
- Regular pulse surveys
- Engagement scoring and trends
- Anonymous feedback
- Manager dashboards
- Action recommendations

**Integrations**:
- None documented (standalone platform)

**Data held**: Employee survey responses, engagement scores, trend data. **Sensitive HR data** — anonymous by design.

**Dependencies**:
- Depends on: Internet, employee participation (response rate)
- Depended on by: HR for engagement tracking, Restaurant Managers for team insights

**References in policies**:
- Restaurant Manager role description: "Use and follow up on the results of Winningtemp, as well as promote usage and response rates"

---

### Fortnox
> Category: Finance & Accounting | Criticality: **High**
> Vendor: Fortnox | Contract ref: TBD
> Owner: Finance (Lisa Wanler, CFO / Filip Forsling, Head of Finance)
> Hosting: **SaaS**
> Locations: **All companies** (one or more restaurants per company)

**Purpose**: Accounting and ERP platform for financial management — invoicing, bookkeeping, accounts payable/receivable, and financial reporting.

**Key capabilities**:
- Bookkeeping and accounting
- Invoicing (customer and supplier)
- Accounts payable and receivable
- Financial reporting (SIE export)
- Payroll integration
- Cost center and project accounting

**Integrations**:
- Simphony → Fortnox (planned/TBD — sales data for accounting)
- Integration research documented at `docs/superpowers/specs/2026-04-02-fortnox-integration-research.md`

**Data held**: All financial data — invoices, journal entries, accounts, payroll data. **Highly sensitive financial data**.

**Dependencies**:
- Depends on: Internet, Fortnox cloud
- Depended on by: Finance team, management reporting, tax/compliance

**Note**: API integration researched but parked due to OAuth2 complexity (multi-company token management). See research doc for full details.

---

## System Lifecycle

| System | Status | Introduced | Next Review | Notes |
|--------|--------|-----------|-------------|-------|
| Oracle Simphony | Active | Pre-2024 | Ongoing | Product redesign planned |
| Future Ordering | Active | ~2024 (Year 1) | TBD | App, kiosk, web ordering |
| Deliverect | Active | ~2024 (Year 1) | TBD | Delivery platform aggregation |
| Planet | Active | TBD | TBD | Payment terminals |
| FreshService | Active | ~2024 (Year 1) | TBD | Pro + Asset plan |
| Ziik | Active | Pre-2024 | TBD | Internal comms + docs |
| Get Compliant | Active | ~2024 (Year 1) | TBD | Food safety compliance |
| Winningtemp | Active | TBD | TBD | Employee engagement |
| Fortnox | Active | Pre-2024 | TBD | Finance — API integration parked |

## Gaps & Questions

- [x] **Deliverect ownership** — Kim Axelsson (POS Architect) ✅
- [x] **Planet ownership** — Johnny Bröms (CDTO) ✅
- [x] **FreshService ownership** — Johnny Bröms (CDTO) ✅
- [x] **Ziik ownership** — HR (Maja Lundqvist, CPO) ✅
- [ ] **Loyalty platform** — is this part of Future Ordering or a separate system?
- [x] **Kitchen Display System (KDS)** — Yes, KDS units in use. Managed via NinjaOne RMM. ✅
- [x] **Scheduling system** — Caspeco handles operations scheduling. ✅
- [ ] **Recruitment system** — any ATS (Applicant Tracking System) in use?
- [ ] **Email/collaboration** — Google Workspace? Microsoft 365? What do HQ staff use?
- [ ] **Monitoring/alerting** — any system health monitoring across restaurants?
- [ ] **Network management** — any centralized network management for 74 locations?
- [ ] **Storebrand Bedriftsportal** — referenced in Norway Daglig Leder role. Norway-specific benefits system?
- [ ] **NAV integration** — Norway sick leave system referenced in Daglig Leder role. Manual or integrated?
