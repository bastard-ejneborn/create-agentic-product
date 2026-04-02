# Create Agentic Product

A framework of AI agents and skills for Claude Code that helps you take a product idea from concept to launch — or supports C-level executives (CIO/CTO/CDO) in their daily strategic work.

## What This Is

This project gives you a team of specialized AI agents that work together inside [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Instead of chatting with a single AI, you get purpose-built agents for strategy, decisions, communication, image generation, music, and more.

**If you're coming from ChatGPT or Codex**: Think of this as having a team of GPTs that share context and collaborate — but running locally in your terminal with full access to your files, git, and tools.

---

## Quick Start

### Prerequisites

- **Node.js 18+** — [Download here](https://nodejs.org/)
- **Git** — [Download here](https://git-scm.com/)
- A terminal (macOS Terminal, iTerm2, Windows Terminal, etc.)

### Step 1: Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

You'll need an Anthropic API key or a Claude Max subscription. Follow the setup prompts on first run.

> **Coming from ChatGPT?** Claude Code runs in your terminal, not a browser. You type commands and have conversations directly in the terminal. It can read and write files on your computer, run commands, and search the web.

### Step 2: Clone This Project

```bash
git clone https://github.com/ejneborn/create-agentic-product.git
cd create-agentic-product
```

### Step 3: Start Claude Code

```bash
claude
```

That's it. Claude Code will automatically read the project's configuration (CLAUDE.md and the agents/skills directories) and know what agents and skills are available.

### Step 4: Set Up API Keys (Optional)

Some skills (image generation, voice, music) require API keys. If you plan to use them:

1. Copy the example file: `cp .env.example .env`
2. Add your keys to `.env`:
   - `OPENROUTER_API_KEY` — for image generation ([get key](https://openrouter.ai/keys))
   - `ELEVENLABS_API_KEY` — for voice generation ([get key](https://elevenlabs.io/api))

The C-level advisory agents (CIO/CTO/CDO) don't require any API keys — they work out of the box.

---

## For CIO / CTO / CDO Users

### What You Get

Three advisory agents tailored to your role, powered by three shared skills:

| Agent | Focus Areas |
|-------|-------------|
| **cio-advisor** | IT strategy, vendor management, security, compliance, budgets, infrastructure |
| **cdo-advisor** | Digital strategy, data governance, customer experience, KPIs, change management |
| **cto-advisor** | Tech strategy, architecture, technical debt, build vs. buy, reliability, R&D |

| Skill | What It Does |
|-------|-------------|
| **company-strategy** | Captures your company's strategic vision, priorities, and constraints |
| **decision-framework** | Helps you make and document structured decisions |
| **stakeholder-briefing** | Generates board updates, business cases, team updates, incident reports |

### Getting Started: Your First Session

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

#### 2. Ask for advice in your domain

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

#### 3. Prepare stakeholder communications

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
| Weekly | Strategic review | "Review our strategy — anything we should update based on recent decisions?" |

### Key Concepts

**Everything is a file.** Strategy docs, decisions, briefings — they all live in `docs/` as markdown files. This means:
- They're version-controlled in git (you can see what changed and when)
- They're searchable (agents can reference past decisions)
- They're portable (copy to Confluence, Notion, Google Docs, or email)

**Agents read your strategy.** Before giving advice, agents check `docs/strategy/company-strategy.md`. This is what prevents generic "best practice" answers and gives you advice grounded in your actual constraints and priorities.

**Decisions build institutional memory.** Every decision you document in `docs/decisions/` becomes context for future decisions. When you ask "should we use Kubernetes?", the agent can reference your past architecture decisions.

---

## How It Compares to ChatGPT / Codex

| Feature | ChatGPT / Codex | This Project |
|---------|----------------|-------------|
| Context | Conversation-based, resets each chat | Persistent files, git history, strategy docs |
| Specialization | One general-purpose AI | Multiple specialized agents |
| File access | Upload/download | Direct read/write on your machine |
| Decision history | Lost after conversation | Versioned in `docs/decisions/` |
| Strategy alignment | You re-explain each time | Agents read `docs/strategy/` automatically |
| Output | Copy-paste from chat | Files committed to git, ready to share |
| Collaboration | Share chat links | Share the git repo, PRs, docs |

---

## Project Structure

```
create-agentic-product/
├── .claude/
│   ├── agents/           # AI agents (one .md file per agent)
│   └── skills/           # Reusable skills (strategy, decisions, etc.)
├── docs/
│   ├── strategy/         # Company strategy (living document)
│   ├── decisions/        # Decision log (one file per decision)
│   └── briefings/        # Generated stakeholder communications
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

**"Claude Code not found"**
- Make sure Node.js 18+ is installed: `node --version`
- Reinstall: `npm install -g @anthropic-ai/claude-code`

**"Permission denied" when running scripts**
- Run: `chmod +x .claude/skills/*/scripts/*.py`

**Agents seem to give generic advice**
- Have you defined your company strategy? Run: "Help me define our company strategy"
- Check that `docs/strategy/company-strategy.md` exists and is up to date

**API key errors for image/voice/music**
- Copy `.env.example` to `.env` and add your keys
- The C-level advisory agents don't need API keys

## License

MIT
