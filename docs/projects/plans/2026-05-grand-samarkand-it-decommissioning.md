# Grand Samarkand IT Decommissioning — Plan

> **Status: Planning (T-0 not yet set).** Copy of `docs/projects/plans/templates/restaurant-it-decommissioning-template.md` filled with what's known. Placeholders in `<ANGLE BRACKETS>` need input from sponsor.
> Last updated: 2026-05-04

---

## Closure Profile

| Field | Value |
|------|-------|
| Restaurant | Grand Samarkand (Växjö, Sweden) |
| District / Region | District South / Region South (DM: Björn Nicklasson, RM: Ricardo Moses) |
| Closure type | **Permanent** |
| Decision date | TBD |
| Last operating day (T-0) | TBD |
| Final IT shutoff (T+N) | TBD |
| Project lead (IT) | André Ejneborn (Senior IT Architect) |
| Project sponsor (Ops) | Johnny Klippmark (COO) — confirm with sponsor |
| Reason | Performance — underperforming location |

> **Note**: Växjö is the city; Grand Samarkand Galleria is the shopping-centre location. District South has another "Växjö" restaurant — that location stays open; Grand Samarkand closure is permanent (not a relocation), so Como members and customers should be guided to the other Växjö store.

---

## Phases & Timeline

T-0 = last day of operation. Dates filled in once T-0 is confirmed.

| Phase | Window | Owner | Goal | Status |
|-------|--------|-------|------|--------|
| **P0 Decision lock** | T-30 → T-21 | Johnny Klippmark + Legal | Confirm closure; freeze further IT investment | |
| **P1 Plan & notify** | T-21 → T-7 | André + Operations + HR | Inventory; staff comms; vendor 30-day notices | In progress (this doc) |
| **P2 Customer wind-down** | T-14 → T-0 | Marketing (Malin Hansegård) + Digital | Delist from app/loyalty/delivery; signage | |
| **P3 Data exports** | T-7 → T-0 | André + Finance + HR | Sales/HR/finance/guest data exported | |
| **P4 Last day** | T-0 | Restaurant Manager + André | Final close-down per Simphony; cash-up | |
| **P5 Hardware retrieval** | T+0 → T+7 | André | Recover POS, KDS, kiosks, PCs, printers, screens, network gear | |
| **P6 System deprovisioning** | T+0 → T+14 | André + IT Helpdesk | Per-system shutoff (matrix below) | |
| **P7 Contract closeout** | T+0 → T+30 | André + Niklas Heinermark (Procurement) | Vendor termination per notice periods | |
| **P8 Long-tail compliance** | T+30 → T+7yr | Filip Forsling (Finance) + André | Bokföring archival; GDPR purge windows | |

---

## Per-System Disposition Matrix

**Action vocabulary**: Deactivate · Disable · Archive · Wipe · Return · Redistribute · Terminate · Transfer · N/A.

| System | Action | Data Retention | Contract Notice | Owner | Status |
|--------|--------|----------------|-----------------|-------|--------|
| Oracle Simphony | Deactivate Grand Samarkand location; export sales data | 7 yrs (bokföring) | Per Oracle contract | Petron Fernandes / Roopneet Bhalla | |
| Future Ordering (FO) | Disable kiosks at location | n/a | n/a | Kim Axelsson | |
| FO Navigator | Remove location config | n/a | n/a | Simon Brännström | |
| Deliverect | Disable location | n/a | n/a | Kim Axelsson | |
| Planet Payment Terminals | Return to vendor / decommission | 7 yrs (financial) | Per contract | Johnny Bröms (CDTO) | |
| Como (Loyalty) | Block accruals at location; preserve member data | Per GDPR / member opt-in | n/a | Marketing (Malin Hansegård) | |
| FreshService | Mark Grand Samarkand assets as decommissioned | Internal log | n/a | IT Helpdesk (Christian Ling) | |
| NinjaOne RMM | Remove kiosk/POS/KDS/PC endpoints | n/a | n/a | André Ejneborn | |
| Ziik | Remove restaurant team space; transfer users | Per HR retention | n/a | HR (Therese Alm) | |
| Get Compliant | Deactivate location | Per food-safety retention | Per contract | Operations | |
| Caspeco | Deactivate location; archive HR records | 7–10 yrs (HR) | Per contract | HR (Therese Alm) | |
| Learnifier | Disable training plans for location; transfer users | Per HR retention | n/a | HR | |
| MapalOS (PILOT) | Confirm whether Grand Samarkand was in pilot scope; deactivate if so | n/a | n/a | Operations | |
| Winningtemp | Remove location | n/a | Per contract | HR | |
| Fortnox | Close cost centre; finalize accounting | 7 yrs (bokföring) | n/a | Finance (Filip Forsling) | |
| Microsoft Entra ID | Disable RM/ARM/SL accounts (or transfer if redeployed) | Per HR offboarding | n/a | IT Helpdesk | |
| Microsoft 365 / Exchange | Disable user mailboxes; convert shared mailbox to archive | Per legal hold | n/a | IT Helpdesk | |
| Microsoft Intune | Wipe / retire endpoints | n/a | n/a | André Ejneborn | |
| Microsoft Teams | Remove location-specific channels (covered by Entra) | n/a | n/a | IT Helpdesk | |
| Microsoft Defender | Removed via Intune retire | n/a | n/a | André Ejneborn | |
| Jamf NOW | Wipe iPad(s); remove enrollment | n/a | n/a | André Ejneborn | |
| Google Workspace / Cloud Identity | Remove RM/ARM Cloud Identity accounts | Per HR offboarding | n/a | IT Helpdesk | |
| Global Connect | Terminate per-location internet contract | n/a | Per contract notice (verify) | Johnny Bröms (CDTO) | |
| Druva Backup | Verify final backup of any retained data; decommission | Per backup retention | n/a | André Ejneborn | |
| Cloudflare DNS | Remove location-specific records (if any) | n/a | n/a | André Ejneborn | |
| Dropbox Business | N/A (central) — verify no Grand Samarkand-specific shared folders | n/a | n/a | Marketing | |
| Atlassian Confluence | Mark Grand Samarkand page status "Closed"; do not delete | Indefinite (history) | n/a | André Ejneborn | |
| Atlassian Jira | N/A (central) | n/a | n/a | — | |
| n8n Cloud | Review automations referencing Grand Samarkand; update flows | n/a | n/a | André Ejneborn | |
| Supabase | Review database/queries referencing this location | n/a | n/a | André Ejneborn | |
| OpenAI API | N/A (central) | n/a | n/a | — | |
| Anthropic Claude AI | N/A (central) | n/a | n/a | — | |
| Perplexity | N/A (central) | n/a | n/a | — | |
| Microsoft Azure | N/A (central tenant) | n/a | n/a | — | |
| Linode (Akamai) | N/A (central infra) | n/a | n/a | — | |
| Pleo | Deactivate cards for closed-location users | Per finance retention | n/a | Finance | |
| Juni | Deactivate cards for closed-location users | Per finance retention | n/a | Finance | |
| Barix RetailPlayer / Royal Streaming | Return Barix; coordinate Effektgruppen speaker/amp recovery (if Effektgruppen-equipped) | n/a | Per contract | TBD | |
| Grassfish Digital Signage | Remove screens from CMS; reclaim/redistribute physical screens | n/a | n/a | TBD | |
| ORS — Order Ready Screen | Remove from Grassfish CMS; reclaim/redistribute screen | n/a | n/a | TBD | |
| Restaurant iPad | Wipe; return to Luleå HQ | n/a | n/a | IT Helpdesk | |
| Restaurant Multi-Function Printer | Return / redistribute | n/a | Verify lease | IT Helpdesk | |
| Restaurant PC (Larger Locations) | Wipe (Intune retire); return to Luleå HQ — only if Grand Samarkand has one | n/a | n/a | André Ejneborn | |
| Kitchen Printer | Return / redistribute (Grand Samarkand: 1 unit assumed unless flagged otherwise) | n/a | n/a | IT Helpdesk | |

> **Music hardware uncertainty**: Setup unknown — could be Effektgruppen + Barix (new) or older Sonos/iPad. Verify on-site during P5 retrieval; the disposition action depends on which.

---

## Hardware Inventory & Disposition

**Disposition vocabulary**: Return to Luleå HQ · Redistribute to `<restaurant>` · Sell · Scrap · Donate · Vendor return.

| Asset | Count | Disposition | Destination | Status |
|-------|-------|-------------|-------------|--------|
| Express Kiosks | `<n>` | | | |
| POS Workstations | `<n>` | | | |
| Planet Payment Terminals | `<n>` | | | |
| KDS Units | `<n>` | | | |
| Kitchen Printers | `<n>` (1 assumed unless flagged) | | | |
| Grassfish Screens | `<n>` | | | |
| ORS Screens | `<n>` | | | |
| Office Desktop PC | `<n>` (only if larger-location office space) | | | |
| Restaurant Laptop | `<n>` | | | |
| Restaurant iPad | `<n>` | | | |
| Multi-Function Printer | `<n>` | | | |
| Barix RetailPlayer | `<n>` | | | |
| Speakers / Amplifiers (Effektgruppen) | `<n>` (only if Effektgruppen setup) | | | |
| Network switch(es) | `<n>` | | | |
| Other (cables, mounts, etc.) | — | | | |

---

## Data Archival Plan

| Domain | Source | Destination / Retention | Owner | Status |
|--------|--------|------------------------|-------|--------|
| Sales | Oracle Simphony | Fortnox archival, 7 yrs (bokföring) | Filip Forsling (Finance) | |
| Financial records | Fortnox | Fortnox + accountant archive, 7 yrs | Maria Tornéus (Accounting) | |
| HR records | Caspeco | HR archive, 7–10 yrs | Therese Alm (HR) | |
| Guest data | Como | Per GDPR / member opt-in (do NOT delete without legal review) | Marketing | |
| Email — shared mailbox | Exchange Online | Convert to archive mailbox; legal-hold per case | IT Helpdesk | |
| Files | M365 / SharePoint | Move to org-wide archive folder | IT Helpdesk | |
| Marketing assets | Dropbox / Drive | Move to archive folder; retain | Marketing | |
| Confluence pages | Atlassian | Mark "Closed"; do not delete (historical reference) | André Ejneborn | |
| Backups | Druva | Verify retention; mark final | André Ejneborn | |

---

## External Communications

- [ ] **Google Maps / Google Business Profile** — mark "Permanently closed"
- [ ] **Bastard Burgers website** — remove Grand Samarkand from store finder
- [ ] **Bastard Burgers app** — remove location
- [ ] **Como members** — opt-out / migration notice (nearest store: Växjö or Nova Lund — confirm)
- [ ] **Delivery platforms** — disable on Foodora, Wolt, Bolt Food, Uber Eats (Sweden)
- [ ] **Suppliers** — final-order coordination + return of any consigned stock
- [ ] **Effektgruppen** — equipment recovery scheduling (if Effektgruppen setup)
- [ ] **Global Connect** — contract termination + circuit decommission
- [ ] **Grand Samarkand Galleria management** — IT-side handover (network demarc, etc.)
- [ ] **Local press / community partners** — courtesy notice (if any)
- [ ] **Internal staff comms** — company-wide notice (HR-led)

---

## People Flow

| Person | Role | Action | Destination | Status |
|--------|------|--------|-------------|--------|
| Louai Bajes | Restaurant Manager | Transfer / Leave / Terminate `<choose>` | `<destination>` | |
| — | Assistant Restaurant Manager | n/a — **no ARM at this location** | — | — |
| `<SL_NAMES>` | Shift Leader(s) | | | |
| Co-workers (`<n>` total) | | | | |

> Note: HR drives this section; IT disables accounts (Entra, Caspeco, Google Workspace) per HR's offboarding signal. Louai's accounts include Entra ID, Caspeco, Get Compliant, and possibly Google Cloud Identity (FO Navigator access). **Shared mailbox access is automated via Entra ID** (dynamic group based on Title + Office location), so when his Entra attributes change or his account is disabled, shared mailbox access drops automatically — no separate manual step. The restaurant's shared mailbox itself is handled via the M365 row in the disposition matrix (convert to archive).

---

## Compliance Gates

- [ ] **Legal review** — employment law, lease termination with Grand Samarkand Galleria, vendor contracts
- [ ] **Finance review** — asset write-down, final accounts
- [ ] **HR review** — employment law (Sweden), severance/redeployment per collective agreement
- [ ] **CDTO sign-off** (Johnny Bröms) — IT decommissioning plan
- [ ] **CFO sign-off** (Lisa Wanler) — financial closure plan
- [ ] **CEO + Board notification** (Simon Wanler) — strategic decision logged

---

## Pre-Closure Verification (T-7)

- [ ] All data exports staged and verified (Sales, HR, Finance, Guest)
- [ ] Hardware retrieval logistics confirmed (transport from Växjö → Luleå booked)
- [ ] Staff redeployment / offboarding confirmed
- [ ] Vendor 30-day notices delivered
- [ ] Customer-facing comms scheduled (Google Maps, app, delivery platforms)
- [ ] Compliance sign-offs collected
- [ ] Runbook reviewed end-to-end with Johnny Klippmark

---

## Post-Closure Verification (T+30)

- [ ] All systems decommissioned per matrix (every row green)
- [ ] All hardware accounted for (every row in inventory has a destination + status)
- [ ] Vendor contracts confirmed terminated (or final invoices received)
- [ ] **`docs/operations/hierarchy.md`** — Grand Samarkand removed from District South; district count 19 → 18
- [ ] **`docs/projects/portfolio.md`** — closure project marked complete
- [ ] **`docs/tech/systems-landscape.md`** — restaurant footprint 75 → 74; company-operated 74 → 73
- [ ] **`exports/organisation-skill/organisation-data.md`** — District South footnote updated
- [ ] **FreshService** — all assets at this location marked decommissioned
- [ ] Final P&L impact captured by Finance
- [ ] This runbook archived with retrospective filled in

---

## Issues Log

| # | Issue | Severity | Resolution | Status |
|---|-------|----------|-----------|--------|
| | | | | |

---

## Lessons Learned

Filled in after closure. Feed structural improvements back into `docs/projects/plans/templates/restaurant-it-decommissioning-template.md`.

| Theme | What happened | Action / template revision |
|-------|---------------|---------------------------|
| | | |
