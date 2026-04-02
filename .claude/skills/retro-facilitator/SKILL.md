---
name: retro-facilitator
description: Use when running sprint retrospectives, project post-mortems, or team reflection sessions. Helps structure the discussion, capture insights, and track action items across retros.
---

# Retro Facilitator

Structure retrospectives and post-mortems to capture what happened, what to improve, and ensure follow-through on action items.

## Retro Formats

### Standard Retro (What Went Well / What Didn't / Actions)

Best for: Sprint retros, regular team check-ins

```markdown
# Retrospective: [Sprint/Project Name]
> Date: YYYY-MM-DD | Facilitator: [name]
> Team: [team name] | Participants: [names]
> Period: [start] — [end]

## What Went Well
- [Positive observation] — raised by [who]
- [Positive observation]

## What Didn't Go Well
- [Issue or frustration] — raised by [who]
- [Issue or frustration]

## What We Learned
- [Insight]
- [Insight]

## Action Items
| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| [specific action] | [who] | [date] | Pending |

## Follow-Up from Previous Retro
| Action | Owner | Status | Notes |
|--------|-------|--------|-------|
| [action from last time] | [who] | Done / In progress / Not started | |
```

### Start / Stop / Continue

Best for: Process improvement, habit changes

```markdown
# Retro: Start / Stop / Continue
> Date: YYYY-MM-DD | Team: [team name]

## Start Doing
- [New practice to adopt] — Why: [reason]

## Stop Doing
- [Practice to drop] — Why: [reason]

## Continue Doing
- [Practice that's working] — Why: [what makes it valuable]

## Action Items
| Action | Owner | Due Date |
|--------|-------|----------|
```

### Project Post-Mortem

Best for: After completing a major project or initiative

```markdown
# Post-Mortem: [Project Name]
> Date: YYYY-MM-DD | PM: [name]
> Project duration: [start] — [end]
> Outcome: [Successful / Partially successful / Failed]

## Project Summary
[What the project aimed to do and what it achieved]

## Goals vs. Outcomes
| Goal | Target | Actual | Met? |
|------|--------|--------|------|
| [goal] | [target] | [actual] | Yes/No/Partial |

## What Went Well
- [Success factor with detail]

## What Didn't Go Well
- [Problem with detail and root cause]

## Surprises
- [Things we didn't anticipate — good or bad]

## Key Decisions Reviewed
| Decision | Was It Right? | What We'd Do Differently |
|----------|-------------|------------------------|
| [decision] | Yes/No/Partial | [alternative] |

## Recommendations for Future Projects
1. [Actionable recommendation]
2. [Actionable recommendation]

## Action Items
| Action | Owner | Due Date |
|--------|-------|----------|
```

## Workflow

1. **Before the retro**: 
   - Check previous retro for open action items
   - Prepare the template
   - Remind participants to think about the period

2. **During the retro**:
   - Ask each question, capture responses
   - For each issue raised, ask "Why?" to find root causes
   - Prioritize — not everything needs an action item
   - Ensure every action item has an owner and due date

3. **After the retro**:
   - Save to `docs/projects/retros/YYYY-MM-DD-{team/project}-retro.md`
   - Share with participants
   - Add action items to project tracking

## Pattern Detection

When reviewing multiple retros, look for:
- **Recurring themes**: Same issue showing up retro after retro = systemic problem
- **Stale actions**: Action items that never get done = capacity or priority issue
- **Mood trends**: Are things getting better or worse over time?

Flag these patterns when found:
> "This is the third retro mentioning deployment friction. Consider making this a dedicated improvement initiative rather than individual action items."

## Tips

- Timebox: 60 min for sprint retro, 90 min for post-mortem
- Start with positives — sets the right tone
- Focus on systems and processes, not blame
- Fewer, specific action items > many vague ones
- Review previous actions first — accountability matters
