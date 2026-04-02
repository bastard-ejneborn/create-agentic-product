---
name: meeting-prep
description: Use when the user needs to prepare for a specific meeting — board meetings, 1:1s, steering committees, team syncs, vendor calls, or any meeting where they need relevant context pulled together quickly.
---

# Meeting Prep

Pull relevant context from strategy, budget, projects, risks, vendors, and decisions to create a focused brief for a specific meeting.

## Workflow

1. **Understand the meeting**: Ask:
   - What kind of meeting? (board, 1:1, steering committee, team sync, vendor call, etc.)
   - Who's attending?
   - What's on the agenda? (or what should be?)
   - Any specific topics or decisions expected?
   - How long is the meeting?

2. **Gather context**: Read relevant docs based on meeting type:

   | Meeting Type | Pull From |
   |-------------|-----------|
   | Board meeting | strategy, budget, projects (highlights), risks (top 5), recent decisions |
   | Steering committee | projects (status), budget (project spend), risks (project risks), decisions (pending) |
   | 1:1 with direct report | team-structure (their team), projects (their projects), any relevant decisions |
   | 1:1 with your manager | strategy (progress), budget (summary), key risks, your asks |
   | Vendor review | vendor-manager (that vendor), budget (their spend), SLA performance |
   | Team sync | projects (team's projects), upcoming milestones, blockers |
   | Strategy review | strategy, all OKR progress, market changes, decisions that shifted direction |

3. **Generate brief**: Create a focused prep document

4. **Suggest agenda**: If the user doesn't have one, suggest an agenda based on context

## Output Format

```markdown
# Meeting Prep: [Meeting Title]
> Date: [meeting date] | Duration: [time]
> Attendees: [who]
> Prepared: YYYY-MM-DD

## Agenda
1. [Topic] — [time allocation]
2. [Topic] — [time allocation]

## Context & Talking Points

### [Agenda Item 1]
**Background**: [Relevant context pulled from docs]

**Key points to raise**:
- [Point with supporting data]
- [Point with supporting data]

**Potential questions to expect**:
- [Question] → [Suggested response/data]

**Decision needed?** [Yes/No — if yes, what and from whom]

### [Agenda Item 2]
[Same structure]

## Numbers to Have Ready
| Metric | Value | Trend | Source |
|--------|-------|-------|--------|
| [metric] | [value] | Up/Down/Stable | [which doc] |

## Open Items from Previous Meeting
- [ ] [Action item from last meeting — status]

## Your Asks
- [What you need from attendees — decisions, resources, approvals]

## Risk Flags
- [Anything that might come up unexpectedly — from risk register or project status]
```

## Meeting-Specific Templates

### Board Meeting Prep
Focus on: strategic progress, financial overview, top risks, key decisions, forward outlook.
Tone: executive, data-driven, concise. No operational detail.

### 1:1 Prep
Focus on: their priorities, blockers, development, your feedback/asks.
Tone: personal, direct, actionable.

### Vendor Review Prep
Focus on: contract status, SLA performance, issues, renewal terms, alternatives.
Tone: prepared, fact-based, negotiation-ready.

### Steering Committee Prep
Focus on: project status, budget burn, risks, decisions needed, dependencies.
Tone: structured, status-oriented, decision-enabling.

## Tips

- Keep prep docs to 1-2 pages — if you can't brief in 5 minutes, it's too long
- Lead with decisions needed — don't save asks for the end
- Anticipate hard questions — prep responses for likely pushback
- Include "if asked" sections for topics that might come up but aren't on the agenda
- After the meeting, capture action items using meeting-notes skill (when available)

## Output Location

Save to `docs/briefings/prep/YYYY-MM-DD-{meeting-type}-prep.md`
