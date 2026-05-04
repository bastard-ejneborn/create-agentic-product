# Systems Landscape — Bastard Burgers
> Last updated: 2026-05-04 (Kamppi soft open Fri 2026-05-08; restaurant counts 74→75, company-operated 73→74; added Kitchen Printer entry)
> Total systems: 43 | Owner: André Ejneborn, Senior IT Architect

## Summary

> **Footprint**: 75 restaurants (74 company-operated + 1 franchise — Landvetter Airport).
> **Most recent opening**: Kamppi (Helsinki, Finland) — soft open Fri 2026-05-08. IT install completed week 17 (Apr 20–24, 2026): 6 Express kiosks, 2 POS workstations, 2 Planet payment terminals, 3 KDS units, 2 kitchen printers, Office Desktop PC + monitor + multi-function printer, restaurant laptop, kitchen iPad, Barix RetailPlayer (via Effektgruppen). Grassfish screens (14) + bookable-room TV streaming pending Week 19. See `docs/projects/plans/2026-04-kamppi-it-installation.md` for the full retrospective.

| Category | Systems | Most Critical |
|----------|---------|--------------|
| POS & Restaurant Operations | Oracle Simphony, Planet Payment Terminals | Oracle Simphony |
| Digital Ordering | Future Ordering (app, kiosk, web), FO Navigator (admin portal) | Future Ordering |
| Loyalty | Como | Como |
| Delivery | Deliverect | Deliverect |
| ITSM & IT Support | FreshService (Pro + Asset) | FreshService |
| Endpoint Management | NinjaOne RMM | NinjaOne |
| Identity & Access | Microsoft Entra ID | Entra ID |
| Collaboration & Email | Microsoft 365 / Exchange Online | M365 |
| Collaboration & Chat | Microsoft Teams | Teams |
| Device Management | Microsoft Intune | Intune |
| Endpoint Security | Microsoft Defender for Endpoint | Defender |
| Apple Device Management | Jamf NOW | Jamf NOW |
| File Sharing (Marketing) | Dropbox Business | Dropbox |
| IT Documentation | Atlassian Confluence | Confluence |
| IT Project/Issue Tracking | Atlassian Jira | Jira |
| AI / Helpdesk Automation | n8n Cloud, Supabase, OpenAI | n8n (orchestration) |
| AI / Productivity | Anthropic Claude AI, Perplexity | Claude AI |
| Identity (Google) | Google Workspace / Cloud Identity | — |
| Network | Global Connect | Global Connect |
| Backup | Druva Backup | Druva |
| DNS | Cloudflare | Cloudflare |
| Cloud Platform | Microsoft Azure | Azure |
| Cloud Compute | Linode (Akamai) | Linode |
| Expense Management | Pleo, Juni | — |
| Restaurant Music | Barix RetailPlayer / Royal Streaming | — |
| Digital Signage | Grassfish | Grassfish |
| Restaurant Devices | iPads (Caspeco/GetCompliant), PCs (larger locations) | — |
| HR & Internal Communication | Ziik | Ziik |
| Food Safety & Compliance | Get Compliant | Get Compliant |
| Workforce Management | Caspeco | Caspeco |
| Training | Learnifier | Learnifier |
| Employee Engagement | Winningtemp | Winningtemp |
| Operations Platform (PILOT) | MapalOS | — (pilot phase) |
| Finance & Accounting | Fortnox | Fortnox |

## Systems Detail

### Oracle Simphony
> Category: POS & Restaurant Operations | Criticality: **Critical**
> Vendor: Oracle | Contract ref: TBD (see vendor-manager when set up)
> Owner: Johnny Bröms (CDTO) | Managed by: Petron Fernandes, Roopneet Bhalla
> Hosting: **Cloud (Oracle shared environment)**
> Locations: **All 75 restaurants**

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
> Locations: **All 75 restaurants** (app, kiosk, web ordering)

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

### Future Ordering Navigator (FO Navigator)
> Category: Digital Ordering (Admin) | Criticality: **High**
> Vendor: Future Ordering | Contract ref: TBD
> Owner: Simon Brännström (IT Architect)
> Hosting: **SaaS** (Future Ordering's platform)
> Locations: **HQ + All restaurants** (POS team + RM/ARM access)

**Purpose**: Admin portal for managing the digital ordering platform. Used by the POS team centrally and by Restaurant Managers / Assistant Restaurant Managers at each location for day-to-day operations.

**Key capabilities**:
- Stock-in / Stock-out (product availability management per restaurant)
- Customer account management (remove app/web user accounts)
- Menu and product configuration
- Restaurant-level settings and overrides

**Users**:
- **POS team** (Petron Fernandes, Roopneet Bhalla, Kim Axelsson) — central administration
- **Restaurant Managers + Assistant Restaurant Managers** — per-location stock management

**Authentication**: Requires a **Google account** to log in (Google Cloud Identity Free accounts provisioned via Entra ID → Google provisioning)

**Integrations**:
- FO Navigator ↔ Future Ordering platform (native — same vendor)
- Google Cloud Identity → FO Navigator (Google Sign-In authentication)

**Confluence ref**: [FO - Notifications](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/10321933)

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
> Locations: **All 75 restaurants**

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
> Locations: **All 75 restaurants** (via app + POS)

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
- Asset management (hardware tracking across 75 locations)
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
> Locations: **All 75 restaurants** (manages on-site hardware)

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
> Locations: **All 75 restaurants**

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

### Learnifier
> Category: Training | Criticality: **Medium**
> Vendor: Learnifier | Contract ref: TBD
> Owner: HR (Maja Lundqvist, CPO)
> Hosting: **SaaS**
> Locations: **All restaurants + HQ**

**Purpose**: Training and e-learning platform for all Bastard Burgers staff. Used for onboarding, certifications, operational training, and continuous learning.

**Key capabilities**:
- Course creation and management
- Employee training tracking
- Onboarding programs
- Certifications and compliance training

**Note**: May potentially be replaced by **MapalOS** if the current pilot succeeds (MapalOS combines training + food safety + internal communication in one platform).

---

### MapalOS (PILOT)
> Category: Operations Platform | Criticality: **N/A — Pilot phase**
> Vendor: Mapal | Contract ref: TBD
> Owner: Operations — **Johannes Norrblom** (Regional Manager North)
> Hosting: **SaaS**
> Locations: **Pilot restaurants** (scope TBD)
> Status: **🟡 Pilot in progress**

**Purpose**: All-in-one restaurant operations platform covering training, food safety, and internal communication. If adopted, would potentially replace three current systems.

**Key capabilities**:
- Training and e-learning (replaces **Learnifier**)
- Food safety checklists and compliance (replaces **Get Compliant**)
- Internal communication and document sharing (replaces **Ziik**)

**Systems potentially replaced**:
| Current System | Owner | MapalOS Equivalent |
|---------------|-------|-------------------|
| Get Compliant | Jonas Ylinenjärvi (F&B) | Food safety module |
| Learnifier | HR (Maja Lundqvist) | Training module |
| Ziik | HR (Maja Lundqvist) | Communication module |

**Impact if adopted**: Major platform consolidation — 3 systems → 1. Would affect:
- All restaurant staff (daily users of these three systems)
- Identity architecture (current separate logins could potentially be unified)
- Caspeco → Ziik integration (would need to redirect to MapalOS)
- Operations policies and role descriptions (all reference Ziik and Get Compliant)

**Decision pending**: Pilot results will determine whether to proceed with full rollout. No timeline or budget committed yet.

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

### Microsoft Entra ID
> Category: Identity & Access | Criticality: **Critical**
> Vendor: Microsoft | Contract ref: TBD (part of M365 licensing)
> Owner: TBD (verify — André Ejneborn? Robert Beney?)
> Hosting: **Cloud (Microsoft Azure)**
> Locations: **All (central identity platform)**

**Purpose**: Central identity provider for the organization. Manages user identities, SSO to connected applications, conditional access policies, and ID governance.

**Account & Licensing Structure**:
| User Group | Entra ID Account | M365 License | Notes |
|-----------|-----------------|-------------|-------|
| HQ employees (Luleå) | Yes | **Microsoft 365 E3** | Full M365 experience |
| Restaurant Managers (RM) | Yes | **Microsoft 365 F3** | Frontline worker license |
| Assistant Restaurant Managers (ARM) | Yes | **Microsoft 365 F3** | Frontline worker license |
| Other restaurant staff (SL, employees) | **No** | None | No Entra ID / M365 account |

**Note**: Shift Leaders and Restaurant Employees do NOT get Microsoft accounts. They access systems via other means (Caspeco for time mgmt, Ziik for communication, Get Compliant for food safety — all with separate logins).

**Future vision**: Extend Entra ID with SCIM provisioning and SSO to all restaurant employee systems (Caspeco, Ziik, Get Compliant) so that all staff — not just RM/ARM — have a unified identity. **Currently not planned or budgeted** — noted as a future architectural direction.

**Key capabilities**:
- User identity management
- Single Sign-On (SAML/OIDC) to connected applications
- Conditional access policies
- ID Governance (access packages, entitlement management)
- Dynamic distribution lists for districts (via Exchange Online)
- User provisioning to downstream apps

**Integrations**:
- Entra ID → NinjaOne (SAML SSO)
- Entra ID → Google Workspace (SAML SSO — legacy, post-migration)
- Entra ID → Exchange Online (native M365)
- Entra ID → Intune (native M365)
- Caspeco → Ziik (account provisioning — simple, not via Entra)

**Data held**: User identities, group memberships, access policies, sign-in logs, audit logs. **Highly sensitive identity data**.

**Dependencies**:
- Depends on: Microsoft Azure cloud
- Depended on by: NinjaOne SSO, Google Workspace SSO, Exchange Online, Intune, all M365 services

**Confluence ref**: [Microsoft Entra ID](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/196905), [NinjaOne SSO](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/135036935), [Google Workspace SSO](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/134643727), [ID Governance](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/157843457)

---

### Microsoft 365 / Exchange Online
> Category: Collaboration & Email | Criticality: **High**
> Vendor: Microsoft | Contract ref: TBD
> Owner: TBD (verify — IT?)
> Hosting: **Cloud (Microsoft 365)**
> Locations: **All staff (HQ + restaurants)**

**Purpose**: Primary email and collaboration platform. Exchange Online provides email, shared mailboxes per restaurant, and dynamic distribution lists organized by district and role.

**Key capabilities**:
- Email (user mailboxes, shared mailboxes)
- Dynamic Distribution Lists per district for RMs and ARMs
- Calendar and scheduling
- SharePoint (document collaboration)
- Teams (if in use — verify)

**Integrations**:
- Microsoft Entra ID → Exchange Online (native identity)
- Dynamic Distribution Lists auto-populated based on department, title, and office attributes in Entra ID

**Data held**: Email, calendar, shared documents. **Business communications**.

**Note**: Fully migrated from Google Workspace. Restaurant mailboxes moved to shared mailboxes in Exchange Online.

**Confluence ref**: [Shared Mailboxes](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/6717455), [Dynamic Distribution Lists](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/234192897), [Migrate restaurant mailboxes](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/13303809)

---

### Microsoft Intune
> Category: Device Management | Criticality: **High**
> Vendor: Microsoft | Contract ref: TBD (part of M365 licensing)
> Owner: TBD (verify — André Ejneborn? Christian Ling?)
> Hosting: **Cloud (Microsoft 365)**
> Locations: **All restaurants (laptops) + HQ Luleå (computers)**

**Purpose**: Endpoint management for company-managed laptops and computers. Manages restaurant laptops and HQ workstations. Complements NinjaOne (which manages restaurant-specific POS hardware — kiosks, POS workstations, KDS).

**Key capabilities**:
- Device enrollment and management
- Policy deployment
- Application management
- Compliance policies
- BitLocker management
- OS update management

**Managed device types**:
- **Windows 11 Pro** laptops (restaurants + HQ)
- **MacBooks** (HQ Luleå)
**HQ Luleå employee equipment policy**: Every HQ employee gets:
- **Laptop** of their choice: MacBook or Windows (managed by Intune)
- **Mobile phone** of their choice: iPhone (managed by Jamf NOW) or Samsung (**currently unmanaged** — too few devices to justify MDM, future plan to add to Intune)

**Device management split with NinjaOne**:
| Device Type | Managed By |
|-------------|-----------|
| Restaurant laptops | **Intune** |
| HQ computers (Luleå) | **Intune** |
| MacBooks (HQ) | **Intune** |
| POS Workstations | **NinjaOne** |
| Express Kiosks | **NinjaOne** |
| KDS Units | **NinjaOne** |

**Integrations**:
- Microsoft Entra ID → Intune (native M365)

**Data held**: Device inventory, compliance status, policy assignments, BitLocker keys.

**Confluence ref**: [Adding Win 11 Home to Intune](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/62029854)

---

### Google Workspace / Cloud Identity
> Category: Identity & AI Platform | Criticality: **Medium**
> Vendor: Google | Contract ref: TBD
> Owner: TBD (verify — André Ejneborn?)
> Hosting: **Cloud (Google)**
> Locations: **HQ (3 licensed users) + All restaurants (Cloud Identity free accounts)**

**Purpose**: Two distinct use cases:

**1. Google Workspace (Full licenses — 3 users)**
- Licensed users: André Ejneborn, Simon Brännström, Simon Wanler
- Primary use: **Google Gemini AI features**
- Full Workspace capabilities for these 3 users

**2. Google Cloud Identity (Free tier — RM + ARM)**
- Free Cloud ID accounts for Restaurant Managers and Assistant Restaurant Managers
- Primary use: **Access to Future Ordering's FO Navigator platform**
- FO Navigator requires a Google account for login
- No-cost license (Google Cloud Identity Free)
- **Note**: Only RM and ARM get Google accounts (same users who get M365 F3). Other restaurant staff do NOT get Google accounts.

**Key capabilities**:
- AI features via Gemini (3 licensed users)
- Google account provisioning for FO Navigator access (all restaurant users)

**Integrations**:
- Entra ID → Google Workspace/Cloud Identity (SAML SSO)
- Entra ID → Google Workspace (user provisioning/sync)
- Google accounts → FO Navigator (authentication requirement from Future Ordering)

**Data held**: User accounts, limited — no email or Drive for Cloud Identity users.

**Dependencies**:
- Depends on: Microsoft Entra ID (for SSO and provisioning)
- Depended on by: Future Ordering FO Navigator (requires Google accounts for restaurant user login)

**Note**: Email has been fully migrated to M365/Exchange Online. Google Workspace is NOT used for email or document collaboration (except by the 3 licensed users). The primary driver for keeping Google is FO Navigator's Google login requirement.

**Confluence ref**: [Google Workspace SSO](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/134643727), [Google Workspace Provisioning](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/134512645)

---

### Global Connect
> Category: Network | Criticality: **Critical**
> Vendor: Global Connect | Contract ref: TBD
> Owner: TBD (verify — André Ejneborn? Johnny Bröms?)
> Hosting: **On-premise (restaurant networking) + WAN**
> Locations: **All 75 restaurants**

**Purpose**: Network provider for all restaurant locations. Provides internet connectivity, switching infrastructure, and IP management for each restaurant.

**Key capabilities**:
- Internet connectivity per restaurant
- Network switching (managed switches)
- IP address management (Site IP Lists)
- Network deployment for new restaurants

**Integrations**:
- All restaurant systems depend on Global Connect networking (Simphony, kiosks, KDS, Planet terminals, NinjaOne agents)

**Data held**: Network configuration, IP assignments, switch configurations.

**Dependencies**:
- Depends on: ISP backbone
- Depended on by: **Every restaurant system** — if the network is down, the restaurant cannot operate POS, kiosks, payments, KDS, or any cloud-connected system

**Confluence ref**: [Deploy of new restaurants, Global Connect](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/24576001)

---

### Microsoft Teams
> Category: Collaboration & Chat | Criticality: **High**
> Vendor: Microsoft | Contract ref: TBD (part of M365 licensing)
> Owner: André Ejneborn (Senior IT Architect)
> Hosting: **Cloud (Microsoft 365)**
> Locations: **All staff**

**Purpose**: Primary chat, meetings, and real-time collaboration platform.

**Key capabilities**:
- Chat and channels
- Video meetings
- File sharing (via SharePoint)
- Teams/groups per department and function

**Integrations**:
- Microsoft Entra ID → Teams (native M365)
- Potential: n8n → Teams (error notifications from Helpdesk AI)

**Confluence ref**: [Microsoft Teams](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/65784), [Teams Inventory](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/2097159)

---

### Jamf NOW
> Category: Apple Device Management | Criticality: **Medium**
> Vendor: Jamf | Contract ref: TBD
> Owner: TBD (verify — André Ejneborn? Christian Ling?)
> Hosting: **SaaS**
> Locations: **All restaurants (iPads) + HQ Luleå (iPhones)**

**Purpose**: Mobile Device Management (MDM) for Apple iOS/iPadOS devices. Manages restaurant iPads and HQ employee iPhones.

**Managed devices**:
- **Restaurant iPads** — all 75 locations (clock-in/out, Get Compliant, backup music)
- **HQ iPhones** — Luleå HQ employees who choose iPhone

**Note**: Jamf NOW manages Apple devices specifically. The full device management split is:

| Device Type | Managed By |
|-------------|-----------|
| Restaurant iPads | **Jamf NOW** |
| HQ iPhones | **Jamf NOW** |
| HQ Samsung phones | **Unmanaged** (future: Intune) |
| Restaurant laptops (Win 11 Pro) | **Intune** |
| HQ laptops — Windows | **Intune** |
| HQ laptops — MacBook | **Intune** |
| POS Workstations | **NinjaOne** |
| Express Kiosks | **NinjaOne** |
| KDS Units | **NinjaOne** |

---

### Microsoft Defender for Endpoint
> Category: Endpoint Security | Criticality: **High**
> Vendor: Microsoft | Contract ref: TBD (part of M365 licensing)
> Owner: André Ejneborn (Senior IT Architect) / Robert Beney (InfoSec)
> Hosting: **Cloud (Microsoft 365)**
> Locations: **All managed devices (MacBooks + Windows laptops)**

**Purpose**: Endpoint protection and security across all company-managed laptops and computers. Deployed via Intune with Microsoft-recommended default configuration.

**Key capabilities**:
- Real-time antivirus / anti-malware protection
- Endpoint Detection and Response (EDR)
- Threat & vulnerability management
- Attack surface reduction
- Security dashboard and alerts (security.microsoft.com)

**Deployed to**:
- All **Windows 11 Pro** laptops (restaurants + HQ)
- All **MacBooks** (HQ Luleå)
- Deployed and managed via **Microsoft Intune**
- Configuration: **Microsoft recommended defaults**

**Integrations**:
- Microsoft Intune → Defender (policy deployment)
- Microsoft Entra ID → Defender (identity-aware protection)
- Microsoft 365 Defender portal (security.microsoft.com)

**Health check (Mac)**:
```bash
mdatp health
# Verify: healthy = true
```

**Confluence ref**: [Microsoft Defender](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/11862018), [MS Defender Knowledge](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/11960322)

---

### Dropbox Business
> Category: File Sharing | Criticality: **Medium**
> Vendor: Dropbox | Contract ref: TBD
> Owner: André Ejneborn (Senior IT Architect)
> Hosting: **SaaS**
> Locations: **Marketing team**

**Purpose**: File sharing and storage platform used primarily by the Marketing team for creative assets.

**Integrations**:
- Entra ID → Dropbox Business (SSO)

**Confluence ref**: [ID Governance Access Packages](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/157843457) (Marketing access package includes Dropbox SSO)

---

### Atlassian Confluence
> Category: IT Documentation | Criticality: **Medium**
> Vendor: Atlassian | Contract ref: TBD
> Owner: André Ejneborn (Senior IT Architect)
> Instance: bastardburgers.atlassian.net
> Hosting: **Cloud (Atlassian)**
> Locations: **IT team + Support**

**Purpose**: IT documentation, runbooks, architecture documentation, system documentation, and knowledge base for the Digital & Tech team.

**Key capabilities**:
- Wiki-style documentation
- Templates (ITSM runbook, IT project poster, IT change management)
- Spaces: Digital & Tech (DT), Support (SUP)

**Integrations**:
- Part of Atlassian suite (shared with Jira)

---

### Atlassian Jira
> Category: IT Project/Issue Tracking | Criticality: **Medium**
> Vendor: Atlassian | Contract ref: TBD
> Owner: André Ejneborn (Senior IT Architect)
> Hosting: **Cloud (Atlassian)**
> Locations: **IT team**

**Purpose**: Issue tracking and project management for IT projects and tasks.

**Integrations**:
- Part of Atlassian suite (shared with Confluence)

---

### n8n Cloud
> Category: AI / Helpdesk Automation | Criticality: **High**
> Vendor: n8n | Contract ref: TBD
> Owner: André Ejneborn (Senior IT Architect)
> Hosting: **Cloud (n8n)**
> Locations: **Central (orchestrates Helpdesk AI)**

**Purpose**: Workflow automation and integration orchestration engine. Powers the Helpdesk AI system — ingests tickets from FreshService, processes them through OpenAI, and stores curated knowledge in Supabase.

**Key capabilities**:
- Workflow orchestration
- API integrations (FreshService, OpenAI, Supabase)
- Batch processing with rate limit handling
- Error handling and notifications

**Part of Helpdesk AI stack** (in production):

```
FreshService (tickets/solutions) → n8n (orchestration) → OpenAI (LLM) → Supabase (knowledge store)
```

**Confluence ref**: [Helpdesk AI architecture](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/227344385), [Component Catalogue](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/228163585)

---

### Supabase
> Category: AI / Knowledge Store | Criticality: **High**
> Vendor: Supabase | Contract ref: TBD
> Owner: André Ejneborn (Senior IT Architect)
> Hosting: **Cloud (Supabase)**
> Locations: **Central**

**Purpose**: Knowledge hub and vector store for the Helpdesk AI system. Stores curated knowledge from historical tickets and FreshService Solutions articles. Uses pgvector for semantic search (RAG).

**Key capabilities**:
- PostgreSQL database with pgvector extension
- Semantic search via embeddings
- Knowledge base storage (published articles)
- Review queue (items needing human curation)
- RLS/policies for access control

**Data structures**:
- `knowledge_base` — published knowledge with embeddings
- `review_queue` — flagged items for human review

---

### OpenAI API
> Category: AI / LLM | Criticality: **High**
> Vendor: OpenAI | Contract ref: TBD
> Owner: André Ejneborn (Senior IT Architect)
> Hosting: **Cloud (OpenAI)**
> Locations: **Central**

**Purpose**: LLM and embeddings provider for the Helpdesk AI system. Classifies tickets, extracts problem/solution pairs, anonymizes PII, and generates semantic embeddings.

**Models used**:
- `gpt-4o-mini` — ticket analysis (classification, extraction, PII scrubbing)
- `text-embedding-3-small` — 1536-dim embeddings for semantic search

---

### Anthropic Claude AI
> Category: AI / Productivity | Criticality: **Medium**
> Vendor: Anthropic | Contract ref: TBD
> Owner: André Ejneborn (Senior IT Architect)
> Hosting: **Cloud (Anthropic)**
> Users: André Ejneborn

**Purpose**: AI assistant for architecture documentation, coding, strategic analysis, and productivity. Powers this project (create-agentic-product) with Claude Code.

**Key capabilities**:
- Claude Code (CLI agent for software engineering)
- Architecture documentation and analysis
- Research and decision support

---

### Perplexity
> Category: AI / Productivity | Criticality: **Low**
> Vendor: Perplexity AI | Contract ref: TBD
> Owner: André Ejneborn (Senior IT Architect)
> Hosting: **Cloud (Perplexity)**
> Users: André Ejneborn, Simon Wanler

**Purpose**: AI-powered search and research tool for quick factual lookups, market research, and technology evaluation.

---

### Druva Backup
> Category: Backup | Criticality: **High**
> Vendor: Druva | Contract ref: TBD
> Owner: TBD (verify — André Ejneborn? Robert Beney?)
> Hosting: **Cloud (Druva)**
> Locations: **Central (backs up M365 tenant)**

**Purpose**: Cloud backup solution for Microsoft 365 environment. Protects against data loss, accidental deletion, and ransomware for core M365 services.

**Backed up services**:
- Microsoft Entra ID (identity data)
- OneDrive (user files)
- SharePoint (team sites, documents)
- Exchange Online (email, calendars)

**Note**: Replaced the previous M365 native backup trial. Druva is the production backup solution.

---

### Cloudflare
> Category: DNS | Criticality: **High**
> Vendor: Cloudflare | Contract ref: TBD
> Owner: André Ejneborn (Senior IT Architect)
> Hosting: **Cloud (Cloudflare)**
> Locations: **Central (DNS for bastardburgers.se)**

**Purpose**: DNS management for the primary domain bastardburgers.se. Other domains managed via Loopia, Markmonitor, GoDaddy, and Punktum DK.

**Note**: Domain registrar landscape:
- **Cloudflare** — DNS for bastardburgers.se
- **Loopia** — DNS + registry for most other domains (managed by André Ejneborn)
- **Markmonitor** — Premium domain protection for .com and international domains
- **GoDaddy** — .co, .info, .net, .online domains (managed by Simon Wanler)
- **Punktum DK** — bastardburgers.dk

**Confluence ref**: [Domain names](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/11567120)

---

### Microsoft Azure
> Category: Cloud Platform | Criticality: **High**
> Vendor: Microsoft | Contract ref: TBD
> Owner: André Ejneborn (Senior IT Architect)
> Hosting: **Cloud (Microsoft Azure)**
> Locations: **Central**

**Purpose**: Cloud platform hosting various services — Logic Apps, Azure Functions, Table Storage, Automation Accounts, and Azure AD/Entra ID backend. Also hosts M365 Backup trial.

**Key services in use**:
- Azure Logic Apps (automation workflows)
- Azure Functions (custom APIs)
- Azure Table Storage (data store)
- Azure Automation (runbooks for Entra ID operations)
- ~~M365 Backup~~ (replaced by Druva Backup)
- Break Glass account monitoring (Log Monitor Alerts)

**Note**: Azure is the underlying platform for many Entra ID and M365 automations. It's not a standalone application but a platform layer.

**Confluence ref**: [Automations within M365](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/64684033), [Break glass configuration](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/66486273), [M365 Backup](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/52166657)

---

### Linode (Akamai)
> Category: Cloud Compute | Criticality: **Medium**
> Vendor: Linode / Akamai | Contract ref: TBD
> Owner: André Ejneborn (Senior IT Architect)
> Hosting: **Cloud (Linode EU Central)**
> Locations: **Central**

**Purpose**: Ubuntu server running Docker containers for the DPIA tool. IP-restricted to Luleå office access only.

**Server details**:
- OS: Ubuntu 22.04
- Label: docker-eu-central
- DNS: dpia.bastardburgers.se
- IP: 143.42.18.149
- Firewall: Cloud Firewall rules enabled
- Monitoring: Longview enabled
- Access: IP-filtered (Luleå office only)

**Confluence ref**: [Linode server documentation](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/10780697)

---

### Pleo
> Category: Expense Management | Criticality: **Medium**
> Vendor: Pleo | Contract ref: TBD
> Owner: TBD (verify — Finance? André Ejneborn?)
> Hosting: **SaaS**
> Locations: **HQ + staff with corporate cards**

**Purpose**: Corporate card and expense management platform. Used for company expenses, purchases, and reimbursements.

**Note**: May be replaced by Juni in the future. Both currently in use.

---

### Juni
> Category: Expense Management | Criticality: **Medium**
> Vendor: Juni | Contract ref: TBD
> Owner: TBD (verify — Finance?)
> Hosting: **SaaS**
> Locations: **HQ + staff with corporate cards**

**Purpose**: Corporate card and expense management platform. Planned to replace Pleo in the future — both currently running in parallel.

---

### Barix RetailPlayer / Royal Streaming
> Category: Restaurant Music | Criticality: **Low**
> Vendor: Royal Streaming (playlist management) + Barix (hardware) + **Effektgruppen** (speakers/amplifiers + on-site install for new openings)
> Owner: TBD
> Hosting: **On-premise** (dedicated Barix RetailPlayer per restaurant)
> Locations: **All 75 restaurants** (some still on iPad/Sonos legacy, migration ongoing)

**Purpose**: Background music at each restaurant. Royal Streaming manages playlists and device management. Barix RetailPlayer is the dedicated hardware device. Effektgruppen handles speaker/amplifier hardware and on-site sound install at new openings.

**Note**: Music hardware varies by restaurant — older locations still on Sonos or iPad as music player; new openings (e.g., Kamppi 2026-05-08) use the **Effektgruppen + Barix** pattern. Always verify which hardware a given restaurant has before troubleshooting.

**Confluence ref**: [IT in restaurants](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/11600008)

---

### Grassfish Digital Signage
> Category: Digital Signage | Criticality: **Medium**
> Vendor: Grassfish | Contract ref: TBD
> Owner: TBD (verify — Marketing? IT? Operations?)
> Hosting: **SaaS (CMS) + On-premise (player units + screens)**
> Locations: **Restaurants** (Kamppi: 14 screens — install pending Week 19, May 4–8 2026; verify rollout to other locations)

**Purpose**: Commercial digital signage system displaying menu offerings, promotions, and advertising content within restaurants. Managed centrally via Grassfish CMS for content scheduling and remote updates.

**Key capabilities**:
- Commercial screen display (menus, offers, campaigns, ads)
- Cloud CMS for content management and scheduling
- Remote content updates per location
- **Player built into the screens** (no separate player unit needed)

**Note**: Kamppi has 14 Grassfish screens — install pending Week 19 (May 4–8 2026), depends on network patching + Grassfish-side networking docs. Verify if other restaurants already have Grassfish or if this is a new rollout starting with Kamppi.

---

### ORS — Order Ready Screen
> Category: Restaurant Equipment | Criticality: **High**
> Vendor: Grassfish (managed alongside digital signage screens)
> Owner: TBD (verify)
> Hosting: **On-premise** (screen, built-in player) + **SaaS** (Grassfish CMS)
> Locations: **All 74 company-operated restaurants**

**Purpose**: Displays order status to guests — shows when their order is ready for pickup. Managed by Grassfish alongside the commercial digital signage screens.

**Key capabilities**:
- Real-time order ready notifications for guests
- Managed through Grassfish CMS

**Dependencies**:
- Depends on: Grassfish CMS, Simphony (order data), internet, local network
- Depended on by: Guest experience (pickup flow)

---

### Restaurant iPad
> Category: Restaurant Equipment | Criticality: **Medium**
> Vendor: Apple | Contract ref: TBD
> Owner: TBD
> Hosting: **On-premise** (one per restaurant)
> Locations: **All 75 restaurants**

**Purpose**: Multi-purpose tablet at each restaurant:
- **Primary**: Clock-in / clock-out device for **Caspeco** (time management)
- **Secondary**: Runs **Get Compliant** (food safety checklists)
- **Backup**: Can act as backup music player (Royal Streaming) if Barix RetailPlayer fails

**Dependencies**:
- Depends on: Wi-Fi, Caspeco (time management), Get Compliant (food safety)

---

### Restaurant Multi-Function Printer
> Category: Restaurant Equipment | Criticality: **Low**
> Vendor: TBD (verify — brand/model)
> Owner: TBD
> Hosting: **On-premise**
> Locations: **All 75 restaurants**

**Purpose**: Multi-function printer at each restaurant providing copy and scan functionality for daily operations (printing schedules, reports, documents, scanning delivery notes, etc.).

---

### Restaurant PC (Larger Locations)
> Category: Restaurant Equipment | Criticality: **Low**
> Vendor: TBD
> Owner: TBD
> Hosting: **On-premise**
> Locations: **Some larger restaurants** (those with a proper office space)

**Purpose**: Desktop PC with 27" screen, camera, and sound for video conferencing (Teams) and education/training. Only at larger restaurants that have a dedicated office.

**Note**: Not all 75 restaurants have this — only locations with proper office space.

**Confluence ref**: [IT in restaurants](https://bastardburgers.atlassian.net/wiki/spaces/DT/pages/11600008)

---

### Kitchen Printer
> Category: Restaurant Equipment | Criticality: **High** (kitchen ticket printing)
> Vendor: TBD (verify brand/model)
> Owner: Johnny Bröms (CDTO) | Managed by: Petron Fernandes, Roopneet Bhalla (same ownership chain as POS workstations and KDS)
> Hosting: **On-premise** (network-attached, driven by Simphony POS)
> Locations: **All 75 restaurants** — 1 unit at most locations; 2 units at larger restaurants (e.g., Kamppi, Mikonkatu)

**Purpose**: Prints kitchen tickets for orders coming in from POS / Express kiosks. Works alongside (and in some kitchens redundantly with) the KDS units, providing a physical paper backup of orders.

**Dependencies**: Oracle Simphony (order routing), Global Connect (network).

---

### External Partners

| Partner | Role | Contact | Access |
|---------|------|---------|--------|
| **Atea** | External IT support (L1/L2), restaurant deployments, terminal configuration | Emil Vikström, Stephen Ryan | FreshService (via Entra SSO), Major Incident team |
| **Global Connect** | Network provider, all 75 restaurants (replaced Xite) | Filip Serdarevic | Network infrastructure |

| **Royal Streaming** | Restaurant music — playlist management + Barix RetailPlayer device management | Via Barix devices | Playlists and device management for all 75 restaurants |
| **Cloudspin** | Software licensing distributor — Adobe, Microsoft 365, SnagIT | Self-service web portal | License add/remove + invoicing |
| **Effektgruppen** | Music hardware — speakers, amplifiers for restaurants | On-site hardware | Speaker/amplifier installations and support |
| **Grassfish** | Digital signage — commercial screens, player units, CMS for content management | Grassfish CMS | Screens, players, content management per restaurant |
| **Future Ordering** | Digital ordering platform provider — Express kiosk software, web ordering, mobile app | FO Navigator (admin), Simphony TX Services API | Software, solution, and support for all digital ordering channels |

**Note**: Xite was the previous networking partner, now replaced by Global Connect. Some Confluence documentation may still reference Xite — those references are historical.

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
- [ ] **Network management** — any centralized network management for 75 locations?
- [ ] **Storebrand Bedriftsportal** — referenced in Norway Daglig Leder role. Norway-specific benefits system?
- [ ] **NAV integration** — Norway sick leave system referenced in Daglig Leder role. Manual or integrated?
