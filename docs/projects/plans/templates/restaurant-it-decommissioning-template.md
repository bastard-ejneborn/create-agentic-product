# Restaurant IT Decommissioning — Runbook Template

> **How to use this template:**
> 1. Copy this file to `docs/projects/plans/<YYYY-MM>-<location>-it-decommissioning.md`
> 2. Replace every placeholder in `<ANGLE BRACKETS>`
> 3. Fill the per-system disposition matrix and hardware inventory based on the actual restaurant
> 4. Track progress in the *Status* column of each table; log surprises in *Issues Log*
> 5. After closure, fill in *Lessons Learned* and feed any structural improvements back into this template
>
> Source-of-truth references this template depends on:
> - Systems Landscape: `docs/tech/systems-landscape.md`
> - Operations Hierarchy: `docs/operations/hierarchy.md`
> - Project Portfolio: `docs/projects/portfolio.md`
>
> Last template revision: 2026-05-04 (initial)

---

## Closure Profile

| Field | Value |
|------|-------|
| Restaurant | `<RESTAURANT_NAME>` (`<CITY>`, `<COUNTRY>`) |
| District / Region | `<DISTRICT>` / `<REGION>` (DM: `<DM_NAME>`, RM: `<RM_NAME>`) |
| Closure type | Permanent / Relocation / Consolidation / Franchise change — `<choose one>` |
| Decision date | `<YYYY-MM-DD>` |
| Last operating day (T-0) | `<YYYY-MM-DD>` |
| Final IT shutoff (T+N) | `<YYYY-MM-DD>` |
| Project lead (IT) | `<NAME>` |
| Project sponsor (Ops / Expansion) | `<NAME>` |
| Reason | `<Brief context: lease end, performance, relocation, etc.>` |

---

## Phases & Timeline

T-0 = last day of operation. All other dates are relative.

| Phase | Window | Owner | Goal |
|-------|--------|-------|------|
| **P0 Decision lock** | T-30 → T-21 | Sponsor + Legal | Confirm closure; freeze further IT investment at this location |
| **P1 Plan & notify** | T-21 → T-7 | IT + Ops + HR | Inventory; draft this runbook; staff comms; deliver vendor 30-day notices |
| **P2 Customer wind-down** | T-14 → T-0 | Marketing + Digital | Delist from app/loyalty/delivery; signage at restaurant |
| **P3 Data exports** | T-7 → T-0 | IT + Finance + HR | Sales/HR/finance/guest data exported and archived |
| **P4 Last day** | T-0 | RM + IT | Final close-down per Simphony; cash-up; physical lockout coordination |
| **P5 Hardware retrieval** | T+0 → T+7 | IT | Recover POS, KDS, kiosks, PCs, printers, screens, network gear |
| **P6 System deprovisioning** | T+0 → T+14 | IT | Per-system shutoff (matrix below) |
| **P7 Contract closeout** | T+0 → T+30 | IT + Procurement | Vendor termination per notice periods |
| **P8 Long-tail compliance** | T+30 → T+7yr | Finance + IT | Bokföring archival (7 yrs); GDPR purge windows |

---

## Per-System Disposition Matrix

One row per system in the systems landscape. **Action vocabulary**: Deactivate · Disable · Archive · Wipe · Return · Redistribute · Terminate · Transfer · N/A (central, no per-location action).

| System | Action | Data Retention | Contract Notice | Owner | Status |
|--------|--------|----------------|-----------------|-------|--------|
| Oracle Simphony | Deactivate location; export sales data | 7 yrs (bokföring) | Per Oracle contract | Petron Fernandes / Roopneet Bhalla | |
| Future Ordering (FO) | Disable kiosks at location | n/a | n/a | Kim Axelsson | |
| FO Navigator | Remove location config | n/a | n/a | Simon Brännström | |
| Deliverect | Disable location | n/a | n/a | Kim Axelsson | |
| Planet Payment Terminals | Return to vendor / decommission | 7 yrs (financial) | Per contract | Johnny Bröms (CDTO) | |
| Como (Loyalty) | Block accruals at location; preserve member data | Per GDPR / member opt-in | n/a | Marketing | |
| FreshService | Mark restaurant assets as decommissioned | Internal log | n/a | IT Helpdesk (Christian Ling) | |
| NinjaOne RMM | Remove kiosk/POS/KDS/PC endpoints | n/a | n/a | André Ejneborn | |
| Ziik | Remove restaurant team space; transfer users | Per HR retention | n/a | HR (Therese Alm) | |
| Get Compliant | Deactivate location | Per food-safety retention | Per contract | Operations | |
| Caspeco | Deactivate location; archive HR records | 7–10 yrs (HR) | Per contract | HR (Therese Alm) | |
| Learnifier | Disable training plans for location; transfer users | Per HR retention | n/a | HR | |
| MapalOS (PILOT) | If pilot included this location: deactivate | n/a | n/a | Operations | |
| Winningtemp | Remove location | n/a | Per contract | HR | |
| Fortnox | Close cost centre; finalize accounting | 7 yrs (bokföring) | n/a | Finance (Filip Forsling) | |
| Microsoft Entra ID | Disable RM/ARM/SL accounts (or transfer if redeployed) | Per HR offboarding | n/a | IT Helpdesk | |
| Microsoft 365 / Exchange | Disable user mailboxes; convert shared mailbox to archive | Per legal hold | n/a | IT Helpdesk | |
| Microsoft Intune | Wipe / retire endpoints | n/a | n/a | André Ejneborn | |
| Microsoft Teams | Remove location-specific channels (covered by Entra) | n/a | n/a | IT Helpdesk | |
| Microsoft Defender | Removed via Intune retire | n/a | n/a | André Ejneborn | |
| Jamf NOW | Wipe iPads; remove enrollment | n/a | n/a | André Ejneborn | |
| Google Workspace / Cloud Identity | Remove RM/ARM Cloud Identity accounts | Per HR offboarding | n/a | IT Helpdesk | |
| Global Connect | Terminate per-location internet contract | n/a | Per contract notice (verify) | CDTO | |
| Druva Backup | Verify final backup of any retained data; decommission | Per backup retention | n/a | André Ejneborn | |
| Cloudflare DNS | Remove location-specific records (if any) | n/a | n/a | André Ejneborn | |
| Dropbox Business | N/A (central) — verify no location-specific shared folders | n/a | n/a | Marketing | |
| Atlassian Confluence | Mark restaurant page status "Closed"; do not delete | Indefinite (history) | n/a | André Ejneborn | |
| Atlassian Jira | N/A (central) | n/a | n/a | — | |
| n8n Cloud | Review automations referencing this location; update flows | n/a | n/a | André Ejneborn | |
| Supabase | Review database/queries referencing this location | n/a | n/a | André Ejneborn | |
| OpenAI API | N/A (central) | n/a | n/a | — | |
| Anthropic Claude AI | N/A (central) | n/a | n/a | — | |
| Perplexity | N/A (central) | n/a | n/a | — | |
| Microsoft Azure | N/A (central tenant) | n/a | n/a | — | |
| Linode (Akamai) | N/A (central infra) | n/a | n/a | — | |
| Pleo | Deactivate cards for closed-location users | Per finance retention | n/a | Finance | |
| Juni | Deactivate cards for closed-location users | Per finance retention | n/a | Finance | |
| Barix RetailPlayer / Royal Streaming | Return Barix; coordinate Effektgruppen speaker/amp recovery | n/a | Per contract | TBD | |
| Grassfish Digital Signage | Remove screens from CMS; reclaim/redistribute physical screens | n/a | n/a | TBD | |
| ORS — Order Ready Screen | Remove from Grassfish CMS; reclaim/redistribute screen | n/a | n/a | TBD | |
| Restaurant iPad | Wipe; return to Luleå HQ | n/a | n/a | IT Helpdesk | |
| Restaurant Multi-Function Printer | Return / redistribute | n/a | Verify lease | IT Helpdesk | |
| Restaurant PC (Larger Locations) | Wipe (Intune retire); return to Luleå HQ | n/a | n/a | André Ejneborn | |
| Kitchen Printer | Return / redistribute (1–2 units depending on size) | n/a | n/a | IT Helpdesk | |

---

## Hardware Inventory & Disposition

**Disposition vocabulary**: Return to Luleå HQ · Redistribute to `<restaurant>` · Sell · Scrap · Donate · Vendor return.

| Asset | Count | Disposition | Destination | Status |
|-------|-------|-------------|-------------|--------|
| Express Kiosks | `<n>` | | | |
| POS Workstations | `<n>` | | | |
| Planet Payment Terminals | `<n>` | | | |
| KDS Units | `<n>` | | | |
| Kitchen Printers | `<n>` (1 or 2) | | | |
| Grassfish Screens | `<n>` | | | |
| ORS Screens | `<n>` | | | |
| Office Desktop PC | `<n>` | | | |
| Restaurant Laptop | `<n>` | | | |
| Restaurant iPad | `<n>` | | | |
| Multi-Function Printer | `<n>` | | | |
| Barix RetailPlayer | `<n>` | | | |
| Speakers / Amplifiers (Effektgruppen) | `<n>` | | | |
| Network switch(es) | `<n>` | | | |
| Other (cables, mounts, etc.) | — | | | |

---

## Data Archival Plan

| Domain | Source | Destination / Retention | Owner | Status |
|--------|--------|------------------------|-------|--------|
| Sales | Oracle Simphony | Fortnox archival, 7 yrs (bokföring) | Finance | |
| Financial records | Fortnox | Fortnox + accountant archive, 7 yrs | Finance | |
| HR records | Caspeco | HR archive, 7–10 yrs | HR | |
| Guest data | Como | Per GDPR / member opt-in (do NOT delete without legal review) | Marketing | |
| Email — shared mailbox | Exchange Online | Convert to archive mailbox; legal-hold per case | IT Helpdesk | |
| Files | M365 / SharePoint | Move to org-wide archive folder | IT Helpdesk | |
| Marketing assets | Dropbox / Drive | Move to archive folder; retain | Marketing | |
| Confluence pages | Atlassian | Mark "Closed"; do not delete (historical reference) | André Ejneborn | |
| Backups | Druva | Verify retention; mark final | André Ejneborn | |

---

## External Communications

- [ ] **Google Maps / Google Business Profile** — mark "Permanently closed"
- [ ] **Bastard Burgers website** — remove location from store finder
- [ ] **Bastard Burgers app** — remove location
- [ ] **Como members** — opt-out / migration notice to nearest store
- [ ] **Delivery platforms** — disable location on Foodora, Wolt, Bolt Food, Uber Eats (verify which apply per market)
- [ ] **Suppliers** — final-order coordination + return of any consigned stock
- [ ] **Effektgruppen** — equipment recovery scheduling
- [ ] **Global Connect** — contract termination + circuit decommission
- [ ] **Landlord / property manager** — IT-side handover (network demarc, holes patched, etc.)
- [ ] **Local press / community partners** — courtesy notice (if any)
- [ ] **Internal staff comms** — company-wide notice (HR-led)

---

## People Flow

| Person | Role | Action | Destination | Status |
|--------|------|--------|-------------|--------|
| `<RM_NAME>` | Restaurant Manager | Transfer / Leave / Terminate | `<destination>` | |
| `<ARM_NAME>` | Assistant Restaurant Manager | | | |
| `<SL_NAMES>` | Shift Leader(s) | | | |
| Co-workers (`<n>` total) | | | | |

> Note: HR drives this. IT's role is to disable accounts (Entra, Caspeco, Google Workspace, etc.) per HR's offboarding signal — not before, not after.

---

## Compliance Gates

- [ ] **Legal review** — employment law, lease termination, vendor contracts
- [ ] **Finance review** — asset write-down, final accounts, financial holds
- [ ] **HR review** — employment law per market, severance/redeployment, retention periods
- [ ] **CDTO sign-off** — IT decommissioning plan
- [ ] **CFO sign-off** — financial closure plan
- [ ] **CEO + Board notification** — strategic decision logged

---

## Pre-Closure Verification (T-7)

Final-go gate before T-0. All of these must be ✅ before the last day of operation:

- [ ] All data exports staged and verified (Sales, HR, Finance, Guest)
- [ ] Hardware retrieval logistics confirmed (transport booked)
- [ ] Staff redeployment / offboarding confirmed
- [ ] Vendor 30-day notices delivered
- [ ] Customer-facing comms scheduled (Google Maps, app, delivery platforms)
- [ ] Compliance sign-offs collected
- [ ] Runbook reviewed end-to-end with sponsor

---

## Post-Closure Verification (T+30)

Final closeout gate. Must be ✅ before the closure is considered "done":

- [ ] All systems decommissioned per matrix (every row green)
- [ ] All hardware accounted for (every row in inventory has a destination + status)
- [ ] Vendor contracts confirmed terminated (or final invoices received)
- [ ] **`docs/operations/hierarchy.md`** — restaurant removed from district list, district restaurant count decremented
- [ ] **`docs/projects/portfolio.md`** — closure project marked complete
- [ ] **`docs/tech/systems-landscape.md`** — restaurant footprint counts decremented (and company-operated count if applicable)
- [ ] **FreshService** — all assets at this location marked decommissioned
- [ ] Final P&L impact captured by Finance
- [ ] Closure runbook archived in `docs/projects/plans/`

---

## Issues Log

| # | Issue | Severity | Resolution | Status |
|---|-------|----------|-----------|--------|
| | | | | |

---

## Lessons Learned

Filled in after closure. Capture: surprises, what worked, what didn't, items the template missed, vendor friction, retention edge cases, hardware gotchas. Feed structural improvements back into this template (`docs/projects/plans/templates/restaurant-it-decommissioning-template.md`).

| Theme | What happened | Action / template revision |
|-------|---------------|---------------------------|
| | | |
