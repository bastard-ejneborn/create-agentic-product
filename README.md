# Create Agentic Product

A framework of AI agents and skills that helps C-level executives (CIO/CTO/CDO), project managers, and marketing teams in their daily work — plus creative agents for product development from concept to launch.

Works with **Claude Code**, **OpenAI Codex CLI**, or **ChatGPT** — pick the setup that matches your tools.

## What This Is

This project gives you a team of specialized AI agents that share context and collaborate. Instead of chatting with a single AI, you get purpose-built agents for strategy, decisions, communication, image generation, music, and more.

Think of it as having a team of specialized assistants that all know your company strategy, remember past decisions, and produce structured outputs you can actually use.

---

## Choose Your Setup

- [**Setup A: Claude Code**](#setup-a-claude-code) — Full experience. Agents run automatically, read/write files, collaborate.
- [**Setup B: OpenAI Codex CLI**](#setup-b-openai-codex-cli) — Similar terminal experience using OpenAI's CLI tool.
- [**Setup C: ChatGPT (browser)**](#setup-c-chatgpt-browser) — No installation needed. Manual but effective.

---

## Setup A: Claude Code

Best experience. Agents and skills work automatically.

### Prerequisites

- **Node.js 18+** — [Download here](https://nodejs.org/)
- **Git** — [Download here](https://git-scm.com/)
- A terminal (macOS Terminal, iTerm2, Windows Terminal, etc.)

### Step 1: Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

You'll need an Anthropic API key or a Claude Max subscription. Follow the setup prompts on first run.

### Step 2: Clone This Project

```bash
git clone https://github.com/ejneborn/create-agentic-product.git
cd create-agentic-product
```

### Step 3: Start Claude Code

```bash
claude
```

That's it. Claude Code automatically reads the project configuration (CLAUDE.md, agents, skills) and knows what's available.

### Step 4: Set Up API Keys (Optional)

Some skills require API keys. Copy the example and add the ones you need:

```bash
cp .env.example .env
```

| Key | Required For | Get It |
|-----|-------------|--------|
| `FRESHSERVICE_DOMAIN` | FreshService helpdesk data | Your subdomain (e.g., `yourcompany`) |
| `FRESHSERVICE_API_KEY` | FreshService helpdesk data | FreshService → Profile → API Key |
| `STITCH_API_KEY` | UI design generation | [stitch.withgoogle.com](https://stitch.withgoogle.com) → Settings → API Key |
| `SIMPHONY_*` (6 vars) | Oracle Simphony POS data | R&A Back Office → API Accounts |
| `OPENROUTER_API_KEY` | Image generation | [openrouter.ai/keys](https://openrouter.ai/keys) |
| `ELEVENLABS_API_KEY` | Voice generation | [elevenlabs.io/api](https://elevenlabs.io/api) |

Most agents work without any API keys. FreshService keys are only needed if you want to pull helpdesk data. Creative keys are only needed for image/voice/music generation.

---

## Setup B: OpenAI Codex CLI

If you use OpenAI and prefer a terminal-based workflow similar to Claude Code.

### Prerequisites

- **Node.js 18+** — [Download here](https://nodejs.org/)
- **Git** — [Download here](https://git-scm.com/)
- An **OpenAI API key** — [Get one here](https://platform.openai.com/api-keys)

### Step 1: Install Codex CLI

```bash
npm install -g @openai/codex
```

### Step 2: Clone This Project

```bash
git clone https://github.com/ejneborn/create-agentic-product.git
cd create-agentic-product
```

### Step 3: Create a Codex Instructions File

Codex CLI reads its instructions from `AGENTS.md` (similar to how Claude Code reads `CLAUDE.md`). Create one:

```bash
cp CLAUDE.md AGENTS.md
```

Then open `AGENTS.md` and adjust any Claude-specific references if needed. The content (strategy workflow, project structure, agent descriptions) applies to any AI tool.

### Step 4: Start Codex

```bash
codex
```

### How Agents Work in Codex

Codex CLI doesn't auto-discover `.claude/agents/` files, but you can use them manually:

**Option 1 — Reference agent files directly:**
```
Read .claude/agents/cto-advisor.md and follow its instructions. 
Then help me evaluate our cloud architecture.
```

**Option 2 — Create custom instructions:**
Copy the agent content you need into your `AGENTS.md` file or into Codex's system instructions.

**Option 3 — Paste agent context per session:**
At the start of each session, tell Codex which role to adopt:
```
You are a CTO advisor. Read .claude/agents/cto-advisor.md for your role 
and .claude/skills/company-strategy/SKILL.md for how to handle strategy. 
Our company strategy is in docs/strategy/company-strategy.md.
```

### Using Skills in Codex

Skills are markdown documentation files — any AI can follow them. Point Codex to the skill file:

```
Follow the process in .claude/skills/decision-framework/SKILL.md 
to help me evaluate build vs. buy for our CRM.
```

Codex can read and write files just like Claude Code, so all outputs (strategy docs, decisions, briefings) will be saved to `docs/` as described.

---

## Setup C: ChatGPT (Browser)

No installation required. You use ChatGPT as the AI and manage files manually.

### Step 1: Download the Project

**Option A — Git clone** (if you have git):
```bash
git clone https://github.com/ejneborn/create-agentic-product.git
```

**Option B — Download ZIP:**
Go to https://github.com/ejneborn/create-agentic-product and click **Code > Download ZIP**. Extract it somewhere on your computer.

### Step 2: Set Up Your ChatGPT

You have two approaches:

#### Approach 1: Custom GPT (Recommended)

Create a Custom GPT that knows your role and strategy:

1. Go to [ChatGPT](https://chat.openai.com) → **Explore GPTs** → **Create**
2. In the **Instructions** field, paste the contents of the agent file matching your role:

   | Role | Agent File |
   |------|-----------|
   | CIO | `.claude/agents/cio-advisor.md` |
   | CTO | `.claude/agents/cto-advisor.md` |
   | CDO | `.claude/agents/cdo-advisor.md` |
   | Project Manager | `.claude/agents/project-manager.md` |
   | Marketing | `.claude/agents/marketing-strategist.md` |
   | Guest Support | `.claude/agents/guest-support-agent.md` |

3. Add to the instructions:
   ```
   When I share my company strategy document, remember it and reference 
   it in all future advice. Always check recommendations against our 
   stated priorities and constraints.
   ```
4. In your first conversation, upload or paste the skill files relevant to your role:

   **For CIO/CTO/CDO** (core skills):
   - `.claude/skills/company-strategy/SKILL.md`
   - `.claude/skills/budget-tracker/SKILL.md`
   - `.claude/skills/project-portfolio/SKILL.md`
   - `.claude/skills/risk-register/SKILL.md`
   - `.claude/skills/vendor-manager/SKILL.md`
   - `.claude/skills/team-structure/SKILL.md`
   - `.claude/skills/decision-framework/SKILL.md`
   - `.claude/skills/stakeholder-briefing/SKILL.md`
   - `.claude/skills/meeting-prep/SKILL.md`

   **Additional for CTO**: `.claude/skills/tech-radar/SKILL.md`
   **Additional for CDO**: `.claude/skills/competitor-watch/SKILL.md`

   **For Project Managers**:
   - `.claude/skills/project-planner/SKILL.md`
   - `.claude/skills/status-report/SKILL.md`
   - `.claude/skills/raci-matrix/SKILL.md`
   - `.claude/skills/retro-facilitator/SKILL.md`
   - `.claude/skills/project-portfolio/SKILL.md`
   - `.claude/skills/budget-tracker/SKILL.md`
   - `.claude/skills/team-structure/SKILL.md`

   **For Marketing**:
   - `.claude/skills/campaign-planner/SKILL.md`
   - `.claude/skills/brand-guidelines/SKILL.md`
   - `.claude/skills/competitor-watch/SKILL.md`
   - `.claude/skills/google-stitch/SKILL.md`
   - `.claude/skills/local-marketing/SKILL.md`
   - `.claude/skills/company-strategy/SKILL.md`
   - `.claude/skills/budget-tracker/SKILL.md`

   **For Guest Support**:
   - `.claude/skills/guest-support/SKILL.md`
   - `.claude/skills/company-strategy/SKILL.md`

   > **Tip**: You don't need to paste all skills at once. Start with 2-3 and add more as needed. ChatGPT has context limits.

5. Name your GPT (e.g., "My CTO Advisor") and save

#### Approach 2: Per-Conversation Context

For each new ChatGPT conversation:

1. Start with a system message that sets the role. Copy-paste from the agent file:
   ```
   I want you to act as my CTO advisor. Here are your instructions:
   [paste content from .claude/agents/cto-advisor.md]
   ```

2. Share your company strategy:
   ```
   Here is our company strategy. Reference this in all your advice:
   [paste content from docs/strategy/company-strategy.md]
   ```

3. When you need a specific skill, paste the skill instructions:
   ```
   Follow this decision framework for our discussion:
   [paste content from .claude/skills/decision-framework/SKILL.md]
   ```

### Step 3: Build Your Strategy Document

Even without Claude Code, you can use the company-strategy skill:

1. Open `.claude/skills/company-strategy/SKILL.md` and read the interview questions
2. Start a ChatGPT conversation:
   ```
   Help me define my company strategy. Ask me the following questions 
   one at a time: company overview, vision & mission, strategic priorities, 
   OKRs, constraints, competitive context, and timeline.
   Then format the result using this template:
   [paste the output format from the skill file]
   ```
3. Save ChatGPT's output as `docs/strategy/company-strategy.md` on your computer
4. Use this document as context in future conversations

### Step 4: Managing Outputs

Since ChatGPT can't write files directly, you'll need to manually save outputs:

| What | Where to Save |
|------|--------------|
| Company strategy | `docs/strategy/company-strategy.md` |
| Budget overview | `docs/finance/budget.md` |
| Project portfolio | `docs/projects/portfolio.md` |
| Risk register | `docs/risk/risk-register.md` |
| Vendor register | `docs/vendors/vendor-register.md` |
| Team structure | `docs/team/team-structure.md` |
| Tech radar | `docs/tech/tech-radar.md` |
| Competitor watch | `docs/marketing/competitor-watch.md` |
| Decisions | `docs/decisions/YYYY-MM-DD-topic.md` |
| Briefings | `docs/briefings/YYYY-MM-DD-type-topic.md` |
| Meeting preps | `docs/briefings/prep/YYYY-MM-DD-type-prep.md` |
| Project plans | `docs/projects/plans/YYYY-MM-DD-project-plan.md` |
| Status reports | `docs/projects/reports/YYYY-MM-DD-project-status.md` |
| RACI matrices | `docs/projects/project-raci.md` |
| Retrospectives | `docs/projects/retros/YYYY-MM-DD-retro.md` |
| Campaigns | `docs/marketing/campaigns/YYYY-MM-DD-campaign.md` |
| Brand guidelines | `docs/marketing/brand-guidelines.md` |
| Department policies | `docs/policies/{department}-policies.md` |
| Policy index | `docs/policies/index.md` |
| Guest support tickets | `docs/support/tickets/YYYY-MM-DD-{id}.md` |
| Guest support summary | `docs/support/ticket-summary.md` |
| Local activity logs | `docs/marketing/local/{location}/activity-log.md` |
| Local area maps | `docs/marketing/local/{location}/area-map.md` |
| Local partnerships | `docs/marketing/local/{location}/partnerships.md` |
| Local marketing plan | `docs/marketing/local/local-marketing-plan.md` |

**Tip**: Keep the folder structure even without git. It makes everything findable and you can always add git later.

### Limitations vs. Claude Code / Codex

| Capability | Claude Code / Codex | ChatGPT |
|-----------|-------------------|---------|
| Auto-reads project files | Yes | No — you paste context manually |
| Writes output to files | Yes | No — you copy-paste to save |
| Remembers between sessions | Via files on disk | Via Custom GPT or re-pasting |
| Multiple agents collaborate | Automatic | One role per conversation |
| Decision log as context | Agents read `docs/decisions/` | You paste relevant decisions |
| Strategy always loaded | Automatic | You upload/paste each session |

Despite these limitations, the **agents, skills, and templates are fully usable** — you just provide the context manually instead of the tool doing it automatically.

---

## For CIO / CTO / CDO Users

### What You Get

Three advisory agents tailored to your role, powered by shared skills:

| Agent | Focus Areas |
|-------|-------------|
| **cio-advisor** | IT strategy, vendor management, security, compliance, budgets, infrastructure |
| **cdo-advisor** | Digital strategy, data governance, customer experience, KPIs, change management |
| **cto-advisor** | Tech strategy, architecture, technical debt, build vs. buy, reliability, R&D |

| Skill | What It Does |
|-------|-------------|
| **company-strategy** | Captures your company's strategic vision, priorities, and constraints |
| **budget-tracker** | Tracks IT/digital/tech budgets — allocated, spent, remaining, by category |
| **project-portfolio** | Tracks ongoing projects — status, owners, dependencies, capacity |
| **risk-register** | Tracks organizational risks — scored, owned, with mitigations |
| **vendor-manager** | Tracks vendor contracts, SLAs, renewals, costs, and lock-in |
| **team-structure** | Documents team composition, capabilities, skill gaps, and capacity |
| **decision-framework** | Helps you make and document structured decisions |
| **stakeholder-briefing** | Generates board updates, business cases, team updates, incident reports |
| **meeting-prep** | Pulls context from all docs to create focused meeting briefs |
| **tech-radar** | Technology landscape tracking (CTO) |
| **competitor-watch** | Competitive intelligence and battle cards (CDO) |
| **freshservice** | Live helpdesk data — tickets, SLA, dashboard (requires API key) |

### How the Skills Connect

```
company-strategy        ← Define what you want to achieve
       ↓
budget-tracker          ← Know what you can afford
       ↓
project-portfolio       ← Track what you're doing about it
       ↓
team-structure          ← Know who can do the work
       ↓
vendor-manager          ← Track external partners and contracts
       ↓
risk-register           ← Identify what could go wrong
       ↓
decision-framework      ← Make informed decisions (grounded in all of the above)
       ↓
stakeholder-briefing    ← Report to stakeholders (pulls from everything)
       ↓
meeting-prep            ← Prepare for any meeting (pulls relevant context)
```

Every skill cross-references the others. A board update includes budget status, project progress, and top risks. A build-vs-buy decision checks available budget, team capacity, and vendor alternatives. Meeting prep pulls exactly the context you need from all docs.

### Getting Started: Your First Session

Set up in this order — each step adds context for the next.

#### 1. Define your company strategy

The most impactful first step. Start Claude Code and say:

```
Help me define our company strategy
```

The agent will walk you through a structured interview:
- Company overview (industry, size, stage)
- Vision and mission
- Top strategic priorities
- OKRs and success metrics
- Constraints (budget, compliance, team size)
- Competitive landscape

This creates a living document at `docs/strategy/company-strategy.md` that all agents reference when giving advice. **This is what makes the advice specific to your company instead of generic.**

> **Tip**: If you already have a strategy document, paste it or point to the file. The agent will structure it and ask follow-up questions to fill gaps.

#### 2. Set up your budget

```
Help me set up our IT budget overview
```

The agent walks you through categories (infrastructure, licensing, personnel, projects, etc.), committed vs. discretionary spend, and forecasts. Output goes to `docs/finance/budget.md`.

#### 3. Register your active projects

```
Help me build our project portfolio
```

List your active initiatives — the agent captures status, owners, budgets, dependencies, and strategic alignment. Output goes to `docs/projects/portfolio.md`.

> **Tip**: Steps 2 and 3 can be done in any order, or skipped initially. The agents work without them but give better advice when budget and project context is available.

#### 3b. Connect FreshService (Optional)

If you use FreshService as your helpdesk, add your API key to `.env`:

```bash
FRESHSERVICE_DOMAIN=yourcompany
FRESHSERVICE_API_KEY=your-api-key
```

Then you can pull live helpdesk data:

```
Show me the helpdesk dashboard for the last 30 days
```

#### 4. Ask for advice in your domain

Once strategy is set, ask questions naturally:

```
We're evaluating whether to build or buy a customer data platform. 
Help me think through this decision.
```

The agent will:
- Read your company strategy for relevant priorities and constraints
- Present options with trade-offs
- Recommend a formality level (lightweight or formal ADR)
- Document the decision in `docs/decisions/`

More examples:

```
Review our cloud spending and suggest optimizations

What should our data governance framework look like?

We need to present our Q2 tech strategy to the board — 
help me prepare the update

We had a major outage yesterday. Help me write the incident report.

Compare Datadog vs Grafana Cloud for our observability stack
```

#### 5. Prepare stakeholder communications

```
Prepare a board update for Q1 covering our digital transformation progress
```

The agent generates a structured briefing with:
- Executive summary
- Strategic progress against OKRs
- Key wins and risks
- Decisions needed
- A slide-ready version you can adapt for presentations

Output goes to `docs/briefings/` — version-controlled and searchable.

### Daily Workflow

A typical day using the agents:

| Time | Activity | What to Say |
|------|----------|-------------|
| Morning | Review priorities | "What are our open decisions and their status?" |
| Pre-meeting | Prepare briefing | "Prepare a team update on the platform migration" |
| During work | Get advice | "Should we invest in a service mesh or keep our current setup?" |
| After incident | Document | "Help me write an incident report for today's outage" |
| Helpdesk check | Review SLA | "Are we meeting our helpdesk SLAs? Show me the dashboard" |
| Weekly | Strategic review | "Review our strategy — anything we should update based on recent decisions?" |

### Key Concepts

**Everything is a file.** Strategy docs, decisions, briefings — they all live in `docs/` as markdown files. This means:
- They're version-controlled in git (you can see what changed and when)
- They're searchable (agents can reference past decisions)
- They're portable (copy to Confluence, Notion, Google Docs, or email)

**Agents read your strategy.** Before giving advice, agents check `docs/strategy/company-strategy.md`. This is what prevents generic "best practice" answers and gives you advice grounded in your actual constraints and priorities.

**Decisions build institutional memory.** Every decision you document in `docs/decisions/` becomes context for future decisions. When you ask "should we use Kubernetes?", the agent can reference your past architecture decisions.

---

## For Project Managers

### What You Get

| Agent | Skills |
|-------|--------|
| **project-manager** | project-planner, project-portfolio, status-report, raci-matrix, retro-facilitator, budget-tracker, team-structure, risk-register, meeting-prep, decision-framework |

### Getting Started

```
Help me create a project plan for our platform migration
```

The agent will ask about goals, timeline, budget, team, and constraints — then produce a structured plan in `docs/projects/plans/`.

### Example Tasks

| Task | What to Say |
|------|-------------|
| Plan a project | "Create a project plan for the CRM implementation" |
| Weekly status | "Write this week's status report for the migration project" |
| Define responsibilities | "Build a RACI matrix for the data platform project" |
| Run a retro | "Facilitate a sprint retrospective for Team Alpha" |
| Check capacity | "Can we take on a new project? Check team capacity and active projects" |
| Prepare for steering | "Prep me for Thursday's steering committee — pull project status and risks" |

### Where Outputs Go

| Output | Location |
|--------|----------|
| Project plans | `docs/projects/plans/` |
| Status reports | `docs/projects/reports/` |
| RACI matrices | `docs/projects/` |
| Retrospectives | `docs/projects/retros/` |

---

## For Marketing Teams

### What You Get

| Agent | Skills |
|-------|--------|
| **marketing-strategist** | campaign-planner, brand-guidelines, competitor-watch, company-strategy, budget-tracker, stakeholder-briefing, meeting-prep, decision-framework |

### Getting Started

```
Help me define our brand guidelines
```

Or jump straight into a campaign:

```
Plan a product launch campaign for our new analytics platform
```

### Example Tasks

| Task | What to Say |
|------|-------------|
| Build brand guidelines | "Help me create our brand guidelines — tone, visual identity, messaging" |
| Plan a campaign | "Plan a lead-gen campaign for Q3 targeting enterprise CTOs" |
| Competitive analysis | "Set up our competitive watch — profile our top 5 competitors" |
| Review positioning | "How should we position against Competitor X? Build a battle card" |
| Campaign report | "Write the post-campaign analysis for the spring launch" |
| Design a landing page | "Generate a landing page design for our new product launch" |
| App mockup | "Design a mobile onboarding flow for our fitness app" |
| Local marketing plan | "Plan this week's local marketing for our Kungsholmen location" |
| Track local activity | "Log today's store visits — we hit 5 offices in the north zone" |
| Local suggestions | "What should we do next for local marketing at Södermalm?" |
| Budget allocation | "How should we split our Q3 marketing budget across channels?" |

### Where Outputs Go

| Output | Location |
|--------|----------|
| Brand guidelines | `docs/marketing/brand-guidelines.md` |
| Campaigns | `docs/marketing/campaigns/` |
| Competitor watch | `docs/marketing/competitor-watch.md` |
| Personas | `docs/marketing/personas/` |
| Local marketing logs | `docs/marketing/local/{location}/` |
| Local marketing plan | `docs/marketing/local/local-marketing-plan.md` |

---

## For Guest Support Teams

### What You Get

| Agent | Skills |
|-------|--------|
| **guest-support-agent** | guest-support, simphony, freshservice, company-strategy, risk-register, meeting-prep |

### Getting Started

1. **Upload your policies** (optional but recommended):
   ```
   Here are our guest support policies: [paste your compensation rules, 
   escalation contacts, refund procedures, brand voice guidelines]
   ```
   The agent structures them into `docs/support/policies.md`. Without policies, industry best practices are used as defaults.

2. **Handle a ticket**:
   ```
   A guest emailed: "I was charged twice for my order at your Kungsholmen 
   location yesterday. Order #4521, paid with Visa. Please refund."
   ```
   The agent triages (billing, MEDIUM), drafts a response using the HEARD model, suggests compensation, and presents the draft for your review.

### Example Tasks

| Task | What to Say |
|------|-------------|
| Handle a complaint | "A guest says their order was wrong and the staff was rude" |
| Double charge | "Guest reports double charge — order #4521 at Södermalm" |
| Food safety issue | "Guest found a piece of plastic in their burger at Kungsholmen" |
| Allergen concern | "Guest with nut allergy says they had a reaction after eating at our restaurant" |
| Review tickets | "Summarize this week's guest support tickets" |
| Spot trends | "Which locations have the most complaints this month?" |
| Draft a response | "Draft a reply to this guest email: [paste email]" |

### Where Outputs Go

| Output | Location |
|--------|----------|
| Guest support policies | `docs/policies/guest-support-policies.md` |
| Individual tickets | `docs/support/tickets/YYYY-MM-DD-{id}.md` |
| Ticket summary | `docs/support/ticket-summary.md` |

### Severity Levels

| Level | Examples | Response Time |
|-------|---------|--------------|
| **CRITICAL** | Allergen reaction, foreign object with injury, illness | Immediate escalation |
| **HIGH** | Foreign object (no injury), discrimination allegation | Within 1 hour |
| **MEDIUM** | Double charge, wrong order, food quality, rude staff | Within 4 hours |
| **LOW** | Menu questions, loyalty points, general inquiries | Within 24 hours |

---

## FreshService Integration

C-level agents can pull live helpdesk data from FreshService (read-only). Requires API key setup.

### Setup

Add to `.env`:
```bash
FRESHSERVICE_DOMAIN=yourcompany
FRESHSERVICE_API_KEY=your-api-key
```

### Example Usage

```
Show me the helpdesk dashboard for the last 30 days

Are we meeting our SLAs?

What are the current urgent open tickets?

Pull the helpdesk stats — I need them for the board update
```

The agent runs the FreshService script and returns ticket volume, SLA compliance, backlog aging, group performance, and open problems/changes. This data can feed directly into stakeholder briefings and meeting preps.

---

## Platform Comparison

| Feature | Claude Code | Codex CLI | ChatGPT |
|---------|------------|-----------|---------|
| Agent auto-discovery | Automatic | Manual reference | Copy-paste |
| File read/write | Automatic | Automatic | Manual save |
| Strategy always loaded | Yes | Yes (with setup) | Paste per session |
| Decision log as context | Automatic | Automatic | Paste relevant ones |
| Multi-agent collaboration | Built-in | One at a time | One per conversation |
| Requires installation | Yes (npm) | Yes (npm) | No |
| API key needed | Anthropic | OpenAI | OpenAI (or subscription) |
| Best for | Full automation | OpenAI users wanting CLI | Quick start, no setup |

---

## Project Structure

```
create-agentic-product/
├── .claude/
│   ├── agents/           # AI agents (one .md file per agent)
│   └── skills/           # Reusable skills (strategy, decisions, etc.)
├── docs/
│   ├── strategy/         # Company strategy (living document)
│   ├── finance/          # Budget tracking and financial overview
│   ├── projects/         # Project portfolio and status
│   ├── risk/             # Risk register
│   ├── vendors/          # Vendor register and contracts
│   ├── team/             # Team structure and capabilities
│   ├── decisions/        # Decision log (one file per decision)
│   ├── policies/         # Department policies (IT, Ops, Marketing, HR, Finance, Guest Support)
│   ├── briefings/        # Stakeholder communications and meeting preps
│   ├── marketing/        # Campaigns, brand guidelines, personas
│   └── tech/             # Technology radar
├── assets/               # Generated images, audio, video
├── CLAUDE.md             # Project instructions for Claude Code
├── .env.example          # Template for API keys
└── .gitignore
```

## All Available Agents

### C-Level Advisors
| Agent | Description |
|-------|-------------|
| `cio-advisor` | IT strategy, vendor management, security, compliance, budgets |
| `cdo-advisor` | Digital strategy, data governance, customer experience, KPIs |
| `cto-advisor` | Tech strategy, architecture, technical debt, build vs. buy |

### IT Architecture
| Agent | Description |
|-------|-------------|
| `it-architect` | System architecture, integrations, IT ADRs, infrastructure, tech stack documentation |

### Project Management
| Agent | Description |
|-------|-------------|
| `project-manager` | Project planning, status reports, risk tracking, RACI, retrospectives |

### Marketing
| Agent | Description |
|-------|-------------|
| `marketing-strategist` | Campaign planning, brand development, content strategy, positioning |

### Operations
| Agent | Description |
|-------|-------------|
| `coo-advisor` | Restaurant operations: KPIs, hierarchy, store visits, weekly/monthly reviews |

### Guest Support
| Agent | Description |
|-------|-------------|
| `guest-support-agent` | Guest tickets, complaints, refunds, food safety, billing issues |

### Creative Agents
| Agent | Description |
|-------|-------------|
| `image-creator` | AI image generation via Google Gemini |
| `elevenlabs-voice` | Voice design and dialogue generation |
| `suno-songwriter` | Music creation with style descriptions and lyrics |

## All Available Skills

| Skill | Description |
|-------|-------------|
| `company-strategy` | Define and maintain company strategic vision |
| `decision-framework` | Structured decision-making with decision log |
| `stakeholder-briefing` | Executive communications (5 templates) |
| `budget-tracker` | IT/digital/tech budget tracking and analysis |
| `project-portfolio` | Project portfolio management and capacity overview |
| `risk-register` | Organizational risk tracking with scoring and mitigations |
| `vendor-manager` | Vendor contracts, SLAs, renewals, and spend tracking |
| `team-structure` | Team composition, capabilities, gaps, and capacity |
| `meeting-prep` | Context-aware meeting preparation briefs |
| `project-planner` | Detailed project plans with WBS, milestones, dependencies |
| `status-report` | Weekly/biweekly operational status reports |
| `retro-facilitator` | Sprint retrospectives and project post-mortems |
| `raci-matrix` | Responsibility assignments (Responsible, Accountable, Consulted, Informed) |
| `campaign-planner` | Marketing campaign planning from brief to analysis |
| `brand-guidelines` | Brand identity — tone of voice, visual identity, messaging |
| `tech-radar` | Technology landscape — Adopt, Trial, Assess, Hold |
| `competitor-watch` | Competitive intelligence — profiles, activity log, battle cards |
| `freshservice` | FreshService helpdesk — tickets, SLA, dashboard, assets (read-only) |
| `google-stitch` | AI UI design — landing pages, app screens, dashboards from text prompts |
| `local-marketing` | Local/guerrilla marketing — store visits, sampling, partnerships, flyer drops, activity tracking |
| `simphony` | Oracle Simphony POS — sales, guest checks, product mix, labor, payments (read-only) |
| `guest-support` | Guest/customer support — triage, response drafting, compensation, escalation, ticket tracking |
| `company-policies` | Department policies — IT, Operations, Marketing, HR, Finance, Guest Support |
| `operations-dashboard` | Restaurant operations — KPIs by level, hierarchy, store visits, reviews |
| `system-architecture` | IT architecture — systems landscape, integrations, ADRs, tech stack, infrastructure |
| `agent-builder` | Create new custom agents |
| `gemini-imagegen` | Image generation via Google Gemini |
| `elevenlabs-skill` | Voice style descriptions for ElevenLabs |
| `suno-music-skill` | Song creation for Suno AI |

## Extending the Project

### Add a Custom Agent

Use the agent-builder skill:

```
I need an agent that helps with procurement and contract negotiation
```

The skill will guide you through designing and creating the agent.

### Update Your Strategy

Your strategy will evolve. Update it anytime:

```
Update our company strategy — we've shifted our Q3 priority 
from international expansion to product consolidation
```

The agent updates the living document and flags any decisions that may be affected.

---

## Troubleshooting

### Claude Code

**"Claude Code not found"**
- Make sure Node.js 18+ is installed: `node --version`
- Reinstall: `npm install -g @anthropic-ai/claude-code`

**"Permission denied" when running scripts**
- Run: `chmod +x .claude/skills/*/scripts/*.py`

### Codex CLI

**"Codex not found"**
- Make sure Node.js 18+ is installed: `node --version`
- Reinstall: `npm install -g @openai/codex`

**Codex doesn't know about the agents**
- Codex doesn't auto-discover `.claude/agents/`. Reference agent files explicitly:
  `Read .claude/agents/cto-advisor.md and follow its instructions.`

### ChatGPT

**ChatGPT forgets my strategy between sessions**
- Use a Custom GPT with the agent instructions built in
- Upload your strategy document at the start of each conversation
- Consider switching to Claude Code or Codex CLI for persistent context

### All Platforms

**Agents seem to give generic advice**
- Have you defined your company strategy? Create `docs/strategy/company-strategy.md`
- For Claude Code: say "Help me define our company strategy"
- For Codex/ChatGPT: follow the interview process in `.claude/skills/company-strategy/SKILL.md`

**API key errors for image/voice/music**
- Copy `.env.example` to `.env` and add your keys
- The C-level advisory agents don't need API keys — they work with just the base AI subscription

## License

MIT
