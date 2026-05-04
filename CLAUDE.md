# CLAUDE.md — Bastard Burgers ops + Creative Product Team

## Working in this repo

Beyond the creative-product workflow below, this repo is also an operational toolkit for Bastard Burgers (Swedish QSR chain, 75 locations). Most current work is org/IT/ops updates, not new-product launches. Both are valid.

### Source-of-truth files (consult before answering domain questions)

| Question | File |
|----------|------|
| Who reports to whom; titles; departments | `docs/strategy/company-strategy.md` + `exports/organisation-skill/organisation-data.md` |
| Restaurant footprint; districts; status | `docs/operations/hierarchy.md` |
| Systems, integrations, owners | `docs/tech/systems-landscape.md` (43 systems) |
| Operational runbooks | `docs/tech/runbooks/` |
| Active projects + portfolio | `docs/projects/portfolio.md` |
| Project plans + retrospectives | `docs/projects/plans/` |
| Reusable plan templates (e.g., restaurant decommissioning) | `docs/projects/plans/templates/` |
| IT / Ops / HR policies | `docs/policies/` |
| Open follow-ups | `TODO.md` |

When making changes, sweep the relevant files together — e.g., an org change typically touches `company-strategy.md` + `organisation-data.md`; a restaurant opening/closing touches `hierarchy.md` + `portfolio.md` + `systems-landscape.md` (footprint counts). Bump the `> Last updated:` header in any file you edit.

### Memory — when to consult, when to update

Memory is auto-loaded from `~/.claude/projects/<this-repo>/memory/`. The index (`MEMORY.md`) currently has 8 entries covering things like Annika's parental leave window, shared-mailbox Azure Automation, music hardware variance per restaurant, the dissolved AI Operations Team, and IT support routing rules.

- **Consult memory** before answering questions about people, time-bound facts, or non-obvious org rules — but treat it as point-in-time; verify against the source-of-truth files above when stakes are high.
- **Update memory** when the user shares a non-obvious rule, a corrected mechanism (e.g., "actually it's Azure Automation, not Entra dynamic groups"), or a fact with a decay date (parental leave, project sponsorship windows).
- **Don't save** facts already captured in the source-of-truth files — those are the canonical store; memory is for the things that aren't.

### Git workflow conventions

- Edit, commit, and push are explicit, separate user requests. Don't auto-push.
- Commit messages: imperative subject, body explains *why* not just *what*, trailer `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`.
- When staging, prefer naming files explicitly over `git add -A` — protects pre-existing unstaged work the user is iterating on.

### QSR domain conventions

- **Restaurant Managers (per-location) are intentionally not tracked centrally** — they change too often. Get current names from the relevant District Manager when needed for a specific closure / event.
- **Counts**: "75 restaurants" = 74 company-operated + 1 franchise (Landvetter Airport). Use both numbers when the distinction matters; sweep all references together when the count changes.
- **IT support routing**: always direct issues to the IT Helpdesk via FreshService. Never name a specific person as the support contact.
- **Music hardware** varies per restaurant: legacy Sonos, iPad-as-player, or the newer Effektgruppen + Barix setup (used at new openings like Kamppi). Check before troubleshooting or planning.

---

## Secondary purpose: Creative-product workflow

The repo can also be used to take a product idea from concept to launch with a configurable agent team in phases. Use only when the user explicitly asks for it — not as default.

**Steps in brief** (see the relevant agent/skill for details):

1. **Understand the need** — product / audience / markets / ambition / budget / timeline / existing material.
2. **Assemble the team** — pick from the 11 existing agents; create new ones via `agent-builder` if needed. Most example roles like *competitor-analyst*, *brand-strategist*, *frontend-dev*, etc. do **not** exist today and must be created.
3. **Run the phases** — Research & Analysis → Concept & Design → Build → Launch & Growth. Phase count and participants adapt per project; review between phases.
4. **Generate creative material** — `gemini-imagegen`, `suno-music-skill`, `elevenlabs-skill`. Output lands in `assets/` organised by type.

## Project structure

- `.claude/agents/` — AI agents (11 today)
- `.claude/skills/` — skills (auto-loaded into the prompt)
- `docs/` — operational documentation (see the Source-of-truth table above)
- `assets/` — generated images, videos, audio
- `exports/` — exportable skills (e.g. `organisation-skill/`)
- `.env` — API keys (gitignored, project root)

## Agents

Agents live in `.claude/agents/` (one .md per agent, auto-discovered with YAML frontmatter for `name`, `description`, `tools`, `model`). 11 agents currently:

- **C-level advisors**: `cio-advisor`, `cdo-advisor`, `cto-advisor`, `coo-advisor`
- **Functional**: `it-architect`, `project-manager`, `marketing-strategist`, `guest-support-agent`
- **Creative**: `image-creator`, `elevenlabs-voice`, `suno-songwriter`

Use the `agent-builder` skill to create new ones. Authoritative role/process per agent lives in its own .md file.

## Skills

Skills are auto-loaded into the system prompt at session start (name + description visible in the available-skills list). Authoritative descriptions live in each skill's `.claude/skills/<skill>/SKILL.md`. Notable cross-cutting ones:

- `agent-builder` — create new agents
- `system-architecture` — read/update `docs/tech/systems-landscape.md`
- `operations-dashboard` — KPIs across the 75 restaurants
- `project-portfolio` / `project-planner` / `status-report` / `retro-facilitator` — project lifecycle
- `freshservice` / `simphony` — read-only data from those external systems
- `gemini-imagegen` / `suno-music-skill` / `elevenlabs-skill` — creative-asset generation

## Creative-work principles (only when the creative-product flow is in use)

- **Studio-quality product image** taken early; user must approve; approved image saved to `assets/images/reference/` and used as the reference for subsequent image-to-image generation (gemini-imagegen).
- **Videos**: evaluate Runway / Kling AI / Google Veo (OpenAI Sora is retired).
- **API keys** (`.env` in project root, gitignored): never create without explicit user approval.
- **Internationalization**: localize, don't just translate; check local laws and certification requirements.
- Strategy documents go in `docs/` with descriptive filenames.
