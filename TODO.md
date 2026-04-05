# TODO — Setup & Configuration Checklist

Things you need to do to fully activate all agents and skills.

## Priority 1: Core Setup (Do First)

- [x] **Define company strategy** — 2025 strategy uploaded ✅
  - `docs/strategy/company-strategy.md` — Bastard Burgers 2025 strategy
  - Update with 2026 version when available

- [ ] **Upload department policies** — Paste policies for each department:
  - [ ] Guest Support — compensation rules, refund procedures, escalation contacts, brand voice
  - [ ] IT — security, change management, acceptable use, BYOD, incident response
  - [~] **Operations** — 🟡 Partial: Shelf life ✅, Role descriptions (Sweden: RC/ARC/SL/Employee) ✅, Role descriptions (Finland: RM/ARM/SL) ✅. Still needed:
    - [ ] Food safety protocols (HACCP)
    - [ ] Hygiene and cleaning protocols
    - [ ] Opening/closing procedures
    - [ ] Quality standards
    - [ ] Allergen handling protocol
    - [ ] Food safety incident response
    - [ ] Food handling routine (referenced in shelf life meat section)
    - [ ] O.S.T. and L.A.S.T. service rules (referenced in restaurant employee role)
    - [ ] Get Compliant usage guidelines (referenced in role descriptions)
    - [ ] Crisis management routines (referenced in RC/ARC/SL roles)
    - [ ] Fire safety systematic work (referenced in RC/ARC/SL roles)
    - [ ] Temperature monitoring procedures
    - [ ] Delivery receiving standards
  - [ ] Marketing — brand usage, social media, campaign approval, local marketing rules
  - [ ] HR — hiring, onboarding, code of conduct, training
  - [ ] Finance — expense approval thresholds, procurement, budget process
  - Run: "Here's our [department] policy: [paste document]"
  - Saves to `docs/policies/{department}-policies.md`

- [ ] **Set up budget** — Run: "Help me set up our IT budget overview"
  - Creates `docs/finance/budget.md`

- [ ] **Register active projects** — Run: "Help me build our project portfolio"
  - Creates `docs/projects/portfolio.md`

## Priority 2: API Connections

### FreshService (Helpdesk)
- [ ] Get your FreshService API key (Profile → API Key)
- [ ] Add to `.env`:
  ```
  FRESHSERVICE_DOMAIN=yourcompany
  FRESHSERVICE_API_KEY=your-key
  ```
- [ ] Test: Run "Show me the helpdesk dashboard"

### Oracle Simphony (Restaurant POS)
- [ ] Create BI API account in R&A Back Office (Administration → System → API Accounts)
- [ ] Select type: **Business Intelligence API**
- [ ] Grant permissions: Sales & Operations, Employee Performance, Labor, Cash Management
- [ ] Note the Client ID, Authentication Server URL, Application Server URL
- [ ] Set API account password
- [ ] Add to `.env`:
  ```
  SIMPHONY_HOST=https://yourdomain.oracleindustry.com
  SIMPHONY_AUTH_HOST=https://yourdomain-idm.oracleindustry.com
  SIMPHONY_CLIENT_ID=your-client-id
  SIMPHONY_USERNAME=your-api-username
  SIMPHONY_PASSWORD=your-api-password
  SIMPHONY_ORG=your-org-short-name
  ```
- [ ] Run: `python .claude/skills/simphony/scripts/simphony_auth.py setup`
- [ ] Test: Run "Show me the Simphony dashboard for yesterday"
- [ ] **Map Simphony locRef IDs to restaurants** — pull location list from Simphony (`simphony.py locations`) and cross-reference with `docs/operations/hierarchy.md` so each of the 74 restaurants has its Simphony ID attached (needed for per-location data pulls)

### Google Stitch (UI Design) — Optional
- [ ] Get API key from stitch.withgoogle.com → Settings
- [ ] Add to `.env`: `STITCH_API_KEY=your-key`
- [ ] Install SDK: `npm install @google/stitch-sdk`
- [ ] Test: Run "Design a landing page for our restaurant"

### Creative Tools — Optional
- [ ] OpenRouter API key (image generation): Add `OPENROUTER_API_KEY` to `.env`
- [ ] ElevenLabs API key (voice): Add `ELEVENLABS_API_KEY` to `.env`

## Priority 3: Organizational Context

- [x] **Operations hierarchy** — Completed ✅
  - `docs/operations/hierarchy.md` — 2 regions, 6 districts, 74 restaurants
  - Restaurant Managers intentionally not tracked (change too often)

- [x] **Leadership team structure** — Documented in `docs/strategy/company-strategy.md` ✅
  - Executive team, Heads of Function, Team Members, reporting tree
  - 36 named people across all functions

- [ ] **Document full team structure** — Optional, broader than leadership — Run: "Help me document our full team structure"
  - Creates `docs/team/team-structure.md`
  - Enables capacity and feasibility assessments across all teams

- [ ] **Set up risk register** — Run: "Help me identify our top organizational risks"
  - Creates `docs/risk/risk-register.md`

- [ ] **Register vendors** — Run: "Help me set up our vendor register"
  - Creates `docs/vendors/vendor-register.md`
  - Especially important for contract renewal tracking

- [ ] **Define brand guidelines** — Run: "Help me create our brand guidelines"
  - Creates `docs/marketing/brand-guidelines.md`
  - Referenced by all marketing and creative work

- [ ] **Set up tech radar** (CTO) — Run: "Help me build our technology radar"
  - Creates `docs/tech/tech-radar.md`

- [ ] **Set up competitor watch** — Run: "Help me profile our top competitors"
  - Creates `docs/marketing/competitor-watch.md`

## Priority 4: Per-Location Setup

For each restaurant location:

- [ ] **Local marketing area map** — Run: "Set up the local marketing area map for [location]"
  - Creates `docs/marketing/local/{location}/area-map.md`
  - Maps nearby businesses for store visits and partnerships

- [ ] **Local partnerships** — Document existing local partnerships
  - Creates `docs/marketing/local/{location}/partnerships.md`

## Issues & Gaps to Resolve

Items flagged during document uploads and setup — need verification, correction, or follow-up.

### Documents

- [ ] **⚠️ Finland RM invoice authorization currency** — Finland Restaurant Manager job description lists supplier invoice authorization limit as "SEK 2,000". This is almost certainly a currency carryover from the Swedish template. For Finland operations it should be **EUR**. Verify with COO Johnny Klippmark and Finance, then update the Finland document.
  - File: `docs/policies/operations-policies.md` (Finland Variants section)

- [ ] **⚠️ Norway RM invoice authorization currency** — Norway Restaurant Manager job description also lists "SEK 2,000" — should be **NOK** for Norway operations. Same carryover issue as Finland.
  - File: `docs/policies/operations-policies.md` (Norway Variants section)

- [ ] **⚠️ Norway RM document untranslated Swedish word** — Norway Restaurant Manager document contains "Kvalitetsresultat" (Swedish) in an otherwise English document. Translation glitch that should be fixed to "Quality results".
  - File: Norway Restaurant Manager PDF (source), will need re-import after fix

- [ ] **📋 Finland Restaurant Employee role description missing** — Three Finland job descriptions provided (RM, ARM, SL) but no Restaurant Employee version. Clarify:
  - Does Finland use the Swedish document as-is?
  - Is there a separate English version that wasn't shared?
  - Should one be created based on the Swedish template?
  - Owner: COO + HR (Finland)

- [ ] **📋 Sweden/Finland/Norway cadence alignment** — Finland and Norway RM documents specify "staff meetings every two months" and "performance appraisals 2 times per year". Swedish RM document just says "per routine". Sweden RM doc also says "per routine" for cadences. Consider aligning cadences across all markets for consistency.
  - Files: All three variants in `docs/policies/operations-policies.md`

- [ ] **📋 Daglig Leder vs Restaurant Manager clarification** — Norway has both roles defined with overlapping responsibilities. Clarify:
  - Is Daglig Leder a separate role from Restaurant Manager, or the same person with additional legal responsibilities?
  - Daglig Leder has 75% operational work vs RM's 80% — is this intentional?
  - Which title do Norwegian restaurant leaders actually hold?
  - Does each Norwegian restaurant need both roles filled separately?
  - Owner: COO + HR (Norway)

- [ ] **📋 Norway operations not in hierarchy** — Norway job descriptions exist but Norway restaurants are not in `docs/operations/hierarchy.md`. Current structure only has Sweden + Finland (Helsinki in Central 2/Finland). Clarify:
  - Are there active Norway restaurants not yet documented?
  - Which district/region do they belong to?
  - Who is the District Manager for Norway?
  - Should Norway be its own region or part of existing regions?
  - File: `docs/operations/hierarchy.md`

- [ ] **📋 Norway documents inconsistent "Bolag" labeling** — Only the Daglig Leder document says "Storage: Bastard Burgers Norway". The other 4 Norway documents (RM, ARM, SL, Co-worker) just say "Bolag: Bastard Burgers" without Norway specification. Should all Norway documents be clearly labeled as Norway-specific?
  - File: Norway PDFs (source documents)

### Technical

- [ ] **POS permission note for Petron and Roopneet** — Both listed as "Technical Product Owner POS" — verify if they have different focus areas (e.g., Sweden vs Finland, hardware vs software) or are genuinely duplicate titles
  - File: `docs/strategy/company-strategy.md` (IT Team)

### Organizational

- [ ] **Kamppi project scope clarification** — Kamppi is listed as an existing restaurant in `docs/operations/hierarchy.md` (District Central 2/Finland) but was also set up as a new project opening Spring 2026. Clarify whether:
  - This is a new location replacing a previous one
  - It's a renovation/reopening
  - The original listing was aspirational
  - Files: `docs/operations/hierarchy.md` + `docs/projects/portfolio.md`

### Cross-References Needed

- [ ] **HR overlap with Operations role descriptions** — Role descriptions in operations-policies.md also belong in HR. When HR policies are uploaded:
  - Decide whether to duplicate, move, or cross-reference
  - Shared Values & Behaviors likely belong in HR culture section

## Future — Parked Integrations

These are researched and ready to build when access is available:

- [ ] **Fortnox Finance** — OAuth2 integration for accounting data
  - Blocker: Need to register Fortnox developer app
  - Research: `docs/superpowers/specs/2026-04-02-fortnox-integration-research.md`

## Ongoing Maintenance

- [ ] **Review strategy quarterly** — "Review our strategy — anything to update?"
- [ ] **Refresh risk register quarterly** — "Review our risk register"
- [ ] **Check vendor renewals monthly** — "Any vendor contracts coming up for renewal?"
- [ ] **Update tech radar quarterly** — "Review our technology radar"
- [ ] **Review competitor watch monthly** — "Any new competitor activity to log?"
- [ ] **Simphony password reset** — Every 60 days, reset API password in R&A and update `.env`
- [ ] **FreshService dashboard review** — Weekly: "Show me the helpdesk dashboard"
- [ ] **Guest support summary** — Weekly: "Summarize this week's guest support tickets"
