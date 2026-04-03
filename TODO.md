# TODO — Setup & Configuration Checklist

Things you need to do to fully activate all agents and skills.

## Priority 1: Core Setup (Do First)

- [ ] **Define company strategy** — Run: "Help me define our company strategy"
  - Creates `docs/strategy/company-strategy.md`
  - This is the foundation — all agents reference it

- [ ] **Upload guest support policies** — Paste your company's policies for compensation, escalation, refund procedures, and brand voice
  - Creates `docs/support/policies.md`
  - Without this, the guest-support agent uses industry defaults

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

### Google Stitch (UI Design) — Optional
- [ ] Get API key from stitch.withgoogle.com → Settings
- [ ] Add to `.env`: `STITCH_API_KEY=your-key`
- [ ] Install SDK: `npm install @google/stitch-sdk`
- [ ] Test: Run "Design a landing page for our restaurant"

### Creative Tools — Optional
- [ ] OpenRouter API key (image generation): Add `OPENROUTER_API_KEY` to `.env`
- [ ] ElevenLabs API key (voice): Add `ELEVENLABS_API_KEY` to `.env`

## Priority 3: Organizational Context

- [ ] **Document team structure** — Run: "Help me document our team structure"
  - Creates `docs/team/team-structure.md`
  - Enables capacity and feasibility assessments

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
