# C-Level Support Skills Design

## Context

The project has three C-level advisory agents (cio-advisor, cdo-advisor, cto-advisor) that currently give generic advice. To make them effective, they need skills that ground their recommendations in the user's actual company context. Three skills are needed.

## Skills Overview

### 1. company-strategy

**Purpose**: Capture, structure, and make queryable the company's strategic vision so all C-level agents can align recommendations to actual business priorities.

**Input paths**:
- **Interview mode**: Guided structured conversation covering vision, OKRs, priorities, constraints, timelines. For users who don't have a written strategy or want to build one from scratch.
- **Import mode**: User provides existing strategy documents (paste, file path, or description). Skill parses and structures into standard format, then asks follow-up questions to fill gaps.

**Output**: Structured strategy document saved to `docs/strategy/company-strategy.md` with sections:
- Company overview (industry, size, stage)
- Vision & mission
- Strategic priorities (ranked, with time horizons)
- OKRs / key metrics
- Constraints & non-negotiables (budget, compliance, team size, tech debt)
- Competitive context
- Timeline & milestones

**How agents use it**: Before giving advice, agents read `docs/strategy/company-strategy.md` and filter recommendations through the stated priorities and constraints. A recommendation that conflicts with a strategic priority gets flagged.

**Update mechanism**: The skill supports incremental updates — user can update individual sections without rewriting the whole document. Strategy docs include a `last-updated` date so agents can flag staleness.

### 2. decision-framework

**Purpose**: Provide structured decision-making templates for recurring C-level decisions, and maintain a searchable decision log for institutional memory.

**Decision types** (each with a tailored template):
- Build vs. buy vs. open-source
- Vendor/tool selection
- Investment prioritization
- Architecture/platform choice
- Organizational change
- Risk acceptance

**Formality levels** (adaptive):
- **Lightweight** (default): One-page markdown — context, options considered, decision, rationale, next steps. For daily/weekly decisions.
- **Formal ADR**: Full record with status (Proposed/Accepted/Deprecated/Superseded), links to related decisions, impact assessment, review date. For major decisions (large budget, irreversible, cross-team).
- The skill recommends formality level based on signals: budget impact, reversibility, number of stakeholders affected.

**Output**: Decision records saved to `docs/decisions/YYYY-MM-DD-{topic}.md`. Index maintained in `docs/decisions/README.md`.

**Strategy integration**: Every decision template includes a "Strategy alignment" section that cross-references `docs/strategy/company-strategy.md` — does this decision support or conflict with stated priorities?

### 3. stakeholder-briefing

**Purpose**: Generate executive-level communications tailored to different audiences and formats.

**Templates**:
- **Board update**: High-level progress, risks, asks. Formal tone, metrics-heavy.
- **C-suite peer update**: Cross-functional status, dependencies, decisions needed. Direct, actionable.
- **Team update**: Direction, priorities, context. Motivational, transparent.
- **Business case**: Problem, proposed solution, costs, benefits, risks, timeline. Persuasive, data-driven.
- **Incident report**: What happened, impact, root cause, remediation, prevention. Factual, structured.

**Output format**: Markdown documents in `docs/briefings/` with:
- Clean prose version (for email/Slack/docs)
- Slide-ready version (one section per slide, with speaker notes) for presentation-heavy templates (board update, business case)

**Strategy integration**: Briefings automatically reference relevant strategic priorities and metrics from `docs/strategy/company-strategy.md` when available.

## File Structure

```
docs/
  strategy/
    company-strategy.md        <- Living strategy document
  decisions/
    README.md                  <- Decision log index
    YYYY-MM-DD-{topic}.md      <- Individual decisions
  briefings/
    YYYY-MM-DD-{type}-{topic}.md  <- Generated briefings
```

## Skill Wiring

All three C-level agents (cio-advisor, cdo-advisor, cto-advisor) get all three skills added to their frontmatter. The skills are also usable standalone.

## Design Decisions

- **Strategy as a file, not memory**: Strategy lives in `docs/strategy/` as a readable markdown file rather than in agent memory. This makes it versionable, reviewable, and shareable.
- **Adaptive formality**: Decision framework defaults to lightweight. Agents recommend escalation to formal ADR based on impact signals rather than requiring the user to choose.
- **Templates over free-form**: Stakeholder briefings use structured templates because C-level communication follows predictable patterns, and consistency builds trust with audiences.
