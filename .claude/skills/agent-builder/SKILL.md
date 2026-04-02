---
name: agent-builder
description: Use when the user wants to build a new agent, create a team of agents, add an agent to .claude/agents/, or design agent roles for a project.
---

# Agent Builder

Build specialized AI agents for Claude Code projects. Each agent becomes a `.md` file in `.claude/agents/` that Claude Code can delegate to.

## Workflow

### Step 1: Understand the Need

Ask (if not already clear):
1. **Project type** — What are you building? (app, product, content, etc.)
2. **Agent role** — What should the agent do?
3. **Collaboration** — What other agents exist or are planned?

### Step 2: Design the Agent

Every agent file follows this format:

```markdown
---
name: agent-name-with-hyphens
description: Short description. Use PROACTIVELY when [trigger]. Handles [responsibility].
tools: [choose from list below]
model: [sonnet|opus|haiku]
---

# Agent content here
```

### Step 3: Choose Tools

| Need | Tools |
|------|-------|
| Read/research only | `Read, Grep, Glob` |
| Read + terminal | `Read, Grep, Glob, Bash` |
| Write/edit code | `Read, Write, Edit, Grep, Glob, Bash` |
| Web research | `Read, WebSearch, WebFetch` |
| Full access | `Read, Write, Edit, Bash, Grep, Glob, WebSearch, WebFetch` |

### Step 4: Choose Model

| Model | Use for |
|-------|---------|
| `opus` | Complex creative/strategic thinking, architecture |
| `sonnet` | Balance of speed and quality, good default |
| `haiku` | Fast simple tasks, searches, validation |

### Step 5: Write the Agent Prompt

Follow this structure:

```markdown
# [Role Name]

[1-2 sentences about who the agent is and what it does]

## Your Role

You are responsible for:
- **[Responsibility 1]**: Short description
- **[Responsibility 2]**: Short description

## Workflow

### On start
1. [What the agent does first — e.g., read context, understand task]
2. [Analyze the task]
3. [Begin work]

### During work
- [Principle 1]
- [Quality requirement]

### On delivery
- [Output format]
- [Verification steps]

## Guidelines
- [Important rule 1]
- [Limitations]

## Collaboration with Other Agents
[If relevant — describe how the agent interacts with the team]
```

### Step 6: Save the Agent

Save to: `.claude/agents/{agent-name}.md`

Verify:
1. YAML frontmatter has name, description, tools, model
2. Description contains "Use PROACTIVELY when" or "Use when"
3. Tools are minimal for the task
4. Prompt has clear structure and workflow

## Agent Team Patterns

### Creative Production (podcast, book, video)
```
project-lead       — Coordinates, prioritizes, quality assurance
writer             — Creates main content
researcher         — Finds facts, background, inspiration
editor             — Reviews, improves, consistency
designer           — Visual material and layout
```

### Product Development (app, SaaS)
```
product-lead       — Vision, prioritization, roadmap
frontend-dev       — UI/UX implementation
backend-dev        — API, database, logic
ux-researcher      — User needs, testing
growth-hacker      — Viral loops, marketing
```

### Research/Analysis Team
```
lead-analyst       — Synthesizes, draws conclusions
data-collector     — Gathers data, scraping, APIs
domain-expert      — Deep domain knowledge
fact-checker       — Verifies claims
presenter          — Packages results
```

## Tips

- **Start small**: Begin with 3-5 agents, expand as needed
- **Clear boundaries**: Each agent should have ONE clear area of responsibility
- **Minimal toolset**: Don't give more access than necessary
- **Testable output**: Agents producing verifiable output work best
- **Iterate**: Update agent prompts based on results
