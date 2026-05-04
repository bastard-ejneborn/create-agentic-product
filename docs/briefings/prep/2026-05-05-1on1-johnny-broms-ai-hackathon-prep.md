# Meeting Prep: AI Hackathon + New AI Ops Team — 1:1 with Johnny Bröms

> Date: **2026-05-05 13:30** (Tue) | Duration: **90 min**
> Attendees: André Ejneborn, Johnny Bröms (CDTO)
> Prepared: 2026-05-04
> Plan references:
> - Hackathon: `docs/projects/plans/2026-05-ai-hackathon-lulea-hq.md`
> - Governance flow: `docs/policies/it-policies.md` § 2b
> - AI Ops autonomy / escalation boundaries: `docs/policies/it-policies.md` § 2c
> - Portfolio: `docs/projects/portfolio.md`

---

## TL;DR — at-a-glance (read 10 minutes before the meeting)

### Anchor line
> *"Hackathon → AI Ops Team → Digital Council. One programme, three layers."*

Hackathon teaches the company to use AI. AI Ops Team turns ideas into structured cases. Digital Council decides which cases scale.

### 9 decisions to walk out with

**Hackathon (Part A, 40 min):**

| # | Decision | Recommendation |
|---|---|---|
| 1 | Date / time | Week 21 or 22 (after Kamppi week) |
| 2 | Sensitive-data guardrails | Pre-defined fictional task patterns + anonymisation training |
| 3 | Facilitator support | 2–3 ex-AI-Ops members, briefed 3 days before |
| 4 | Beginner / advanced mix | Rotating "driver" role per round (don't split tracks) |

**AI Ops Team (Part B, 45 min):**

| # | Decision | Recommendation |
|---|---|---|
| 5 | Composition | **Model A**: small operator core (André + Erik + Therese + 1–2 ex-Hackathon facilitators) |
| 6 | Cadence | Bi-weekly + async triage channel |
| 7 | Use-case list home | Jira project: Idea → Qualifying → Pilot → Production → Parked |
| 8 | CISO trigger | Robert Beney pulled-in (not seated); fixed checklist |
| 9 | Hackathon → AI Ops handoff | 4-week regroup is the case-intake moment |

### Three lines you'll repeat

- *"Digital Council is not the build team — it's the decision and prioritisation forum."*
- *"It's not the activity that determines — it's the consequence."* (green/yellow/red model)
- *"We trade breadth-on-paper for speed-in-practice."* (the small-team trade-off)

### Three asks you must not forget

1. **Sponsor endorsement in writing** — short Teams/Slack message you can quote in the Hackathon invite
2. **4-week regroup calendared today** — without that booking, the commitments evaporate
3. **First Digital Council touchpoint calendared today** — ~6 weeks out, where you bring the new format and first batch of cases

### Don't get pulled into

- Grand Samarkand details (different sponsor — Klippmark)
- Reopening the *locked* Hackathon items (scope, tooling, language, cost) unless Johnny does
- If AI Ops composition stalls: *"Lock the lead and one or two operators today; the rest within a week."*

---

---

## Two-topic meeting

| Topic | Time | Goal |
|-------|------|------|
| **Part A — AI Hackathon** | ~40 min | Lock the four open decisions (date, sensitive-data, facilitators, beginner/advanced mix) |
| **Part B — New AI Operations Team** | ~45 min | Agree on composition, cadence, intake, Digital Council interface |
| **Wrap** | ~5 min | Action items, owners, next checkpoint |

The two topics are connected: the **Hackathon's 4-week regroup** is the natural intake for the new AI Ops Team's case-pipeline. Frame them as one programme of work, not two unrelated things.

---

## Suggested agenda (90 min)

| # | Topic | Time |
|---|-------|------|
| 1 | One-line framing: Hackathon + new AI Ops Team are one programme | 5 |
| 2 | Hackathon: locked items quick run-through | 5 |
| 3 | Hackathon Decision 1: Date / time | 5 |
| 4 | Hackathon Decision 2: Sensitive-data guardrails | 5 |
| 5 | Hackathon Decision 3: Facilitator support | 5 |
| 6 | Hackathon Decision 4: Beginner/advanced mix | 5 |
| 7 | Hackathon → AI Ops Team handoff (4-week regroup as intake) | 5 |
| 8 | **Transition** — review Digital Council ↔ AI Ops governance flow | 5 |
| 9 | AI Ops composition — who's on it? | 15 |
| 10 | AI Ops cadence + intake mechanism | 10 |
| 11 | Use-case list — where does it live? Who owns it? | 10 |
| 12 | CISO/Compliance trigger — Robert Beney involvement model | 5 |
| 13 | Wrap: action items + next checkpoint | 5 |

---

## Lead with this (one-line framing for the whole 90 min)

> *"Hackathon teaches the company to use AI; the new AI Ops Team turns the resulting ideas into structured, tested, supportable cases; Digital Council decides which cases get to production. One programme, three layers."*

Sub-pitch for the Hackathon specifically:
> *"The dissolved AI Operations Team was a top-down model — a small group finding initiatives. This Hackathon flips that: we teach the whole HQ to use AI well, then initiatives emerge from any function. It's the on-ramp for the new format, not a one-off event."*

That framing is the key — it positions the Hackathon as the **strategy replacement**, not extra work on top of an unclear gap.

---

## What's locked (don't open these up unless Johnny does)

| Item | Value |
|---|---|
| Scope | Luleå HQ only |
| Tooling | ChatGPT Business (already in place) |
| Language | Swedish |
| Cost | Verified with CEO |
| Format | Half-day, cross-functional teams, Mentimeter voting, cumulative scoreboard |
| Round structure | Warm-up (no points) + 3 voted rounds (Promptmakeover 30 min, Spegla ditt arbete 45 min, Målgruppsflippet 30 min) |
| Follow-up | 4-week regroup — each participant returns with one workflow they actually changed |
| Materials | All 5 deliverables ready (invitation HTML, presentation PPTX, handout DOCX, Meeting From Hell transcript, pitch deck PPTX) |

---

## Decisions to extract (with your recommendations)

### Decision 1 — Event date / time
**Your recommendation**: A morning slot 2–4 weeks out (gives time to send invites + set up Mentimeter + prep facilitators).

**Constraints to check with Johnny**:
- Avoid the **week of Kamppi soft-open** (week 19, May 4–8) — André bandwidth is committed to Grassfish + streaming follow-up.
- Annika Elworth on parental leave from **Fri May 8 → 2027-05-08**. If you want Brand represented, schedule before Friday — but that's not realistic for a hackathon. Accept Brand absence and let Marketing (Malin Hansegård) cover the function.
- Avoid month-end / payroll runs.

**Concrete proposal**: Tuesday or Wednesday in **week 21 or 22** (May 19–22 or May 26–28, 2026). Avoids Kamppi week, gives 2–3 weeks lead time.

---

### Decision 2 — Sensitive-data guardrails
**Risk**: Round 2 (Spegla ditt arbete) asks people to bring real cross-functional work. Someone could paste a real customer email, real Caspeco roster, real Fortnox data into ChatGPT Business.

**Mitigation options to discuss**:
- (a) **Pre-defined fictional task patterns** — provide 4–5 cross-functional task templates (e.g. "department intro for a new hire", "FAQ that spans 2 functions") that don't require real data. *Recommended*.
- (b) **Anonymisation training in the welcome block** — 5-minute block on how to scrub data before pasting. Useful regardless.
- (c) **ChatGPT Business contractually doesn't train on inputs** — does this lower the bar? Verify with Johnny before relying on it; legally it's still company data leaving the M365 boundary.

**Your recommendation**: do (a) + (b). Don't rely solely on (c).

**Decision needed**: confirm (a) + (b), and confirm whether Round 2 task patterns can include any real-data scenarios at all.

---

### Decision 3 — Facilitator support
**The problem**: One host can't simultaneously present, run Mentimeter voting + scoreboard, and unstick teams when they're stuck on a prompt.

**Your recommendation**: 1 floating facilitator per ~3 teams. With Luleå HQ headcount, that's likely 2–3 facilitators total.

**Decision needed**: who facilitates, and when do they get briefed? Suggest a 60-min briefing session ~3 days before the event.

**Candidate facilitators** (pulling from the dissolved AI Ops Team — they already know the material): Caroline Johansson, Niklas Heinermark, Therese Alm, Erik Löfgren, Johannes Norrblom (RM North — likely not at HQ). Worth asking 2–3 of them. Note: Annika and Malin are being repositioned and unavailable; Annika on leave from Friday.

---

### Decision 4 — Beginner / advanced mix
**The problem**: Brief targets "complete beginners" but also "everyone who currently uses ChatGPT". Risk: advanced users dominate teams; beginners spectate.

**Your recommendation**: Keep the format. Mitigate via **rotating "driver" role** per round (different team member types each round, ensuring less-experienced people get hands-on time).

**Decision needed**: accept this mitigation, or propose a different split (e.g., separate beginner / advanced tracks)? Different tracks would double facilitator load and undercut the cross-functional team principle — not recommended.

---

---

## Part B — New AI Operations Team (45 min)

The full governance flow is now documented in `docs/policies/it-policies.md` § 2b. Bring it up on screen during this part of the meeting.

### Recap (1 min)

- **Digital Council** = decision/prioritisation forum (not a build team). Decides which cases proceed, vendors, pilot→production gating.
- **AI Operations Team** = operational engine. Takes ideas → structured/testable/supportable cases. Drives low-risk operationally; lifts higher-risk to Digital Council.
- **CISO/Compliance** (Robert Beney) engaged when persondata, betaldata, GDPR, PCI-DSS, vendor risk, access/logging.
- **Autonomy boundary** (per § 2c): green = run yourselves (local/internal/reversible); yellow = check with AI Ops; red = escalate to Digital Council. The shift to repeat: *"It's not the activity that determines — it's the consequence."*

### B-Decision 1 — Composition (15 min, biggest discussion)

The dissolved team had 8 members, all heads/seniors from each function (Caroline, Malin, Annika, Niklas, Therese, Erik, Johannes + André as lead). That model didn't work — too senior, too broad, schedules collided.

**Two models to discuss with Johnny**:

**Model A — Small operator core** (recommended):
- 3–5 people, all hands-on operators (not function heads)
- Lead: André Ejneborn
- Members: e.g. Erik Löfgren (Finance/CRM operator mindset), Therese Alm (HR/People), one or two ex-Hackathon facilitators who showed interest
- Function heads consulted, not seated — they get briefed on cases that affect their function
- Pros: faster, less calendar friction, cases actually move
- Cons: less broad organisational coverage; relies on consultation discipline

**Model B — Function-rep team** (the old model, refined):
- 6–8 people, one per function, all able to make decisions for their function
- Same risk that killed the previous team — meetings drift, hard to schedule

**Your recommendation**: A. State the trade-off explicitly: "we trade breadth-on-paper for speed-in-practice."

**Decision needed**: Model A or B; if A, who are the 3–5?

**Note on ex-team members**: Annika is on parental leave from Friday — naturally out. Malin Hansegård just moved to Marketing under CEO — different reporting line, may want a different relationship to AI Ops. Caroline and Johannes are stretched on Operations. **The natural continuing operators are André, Erik, Therese — confirm.**

### B-Decision 2 — Cadence (10 min)

**Three options**:
- **Weekly** — old format, didn't work, full meetings drag
- **Bi-weekly with async case-triage in between** — recommended; meeting is for harder calls, async handles the obvious ones
- **On-demand only** — nothing happens unless someone forces it

**Your recommendation**: bi-weekly 30-min standing meeting, async triage in a Teams/Slack channel between meetings.

**Decision needed**: cadence locked; channel/tool for async triage.

### B-Decision 3 — Use-case list mechanism (10 min)

The flow says AI Ops Team "håller koll på use case-listan: idé, pilot, produktion och sådant som bör stoppas." Where does this list live?

**Options**:
- **Confluence page** — easy to start, hard to query, no audit trail
- **Jira project** — issue-per-case, lifecycle states map to idea/pilot/production/parked, full history. Already in the BB stack.
- **Dedicated tracker** — overkill at this stage

**Your recommendation**: Jira project ("AIOPS" or similar) with a custom workflow: *Idea → Qualifying → Pilot → Production → Parked*. One issue per case. Confluence pages link from the Jira issues for any deep documentation.

**Decision needed**: where the list lives; who maintains it (default: AI Ops Team lead).

### B-Decision 4 — CISO/Compliance trigger (5 min)

Robert Beney (Head of Information Security and Compliance) is named in the flow as the involvement point. Concrete questions:

- Does Robert sit on AI Ops Team, or only get pulled in?
- What's the trigger checklist? (PII, payment data, vendor contracts, GDPR DPIA, etc.) — should be a fixed list in the case-qualification form, not ad-hoc.
- Does CISO have veto on cases, or advisory only?

**Your recommendation**: pulled in (not seated); fixed trigger checklist baked into the case-qualification step; advisory + escalation to Digital Council if AI Ops disagrees.

**Decision needed**: Robert's involvement model; trigger checklist owner.

### B-Decision 5 — Hackathon → AI Ops handoff (already in the flow — confirm)

The Hackathon's 4-week regroup will produce 30+ workflow-change reports. Each report classifies naturally per the governance flow:
- **Individual productivity** (most reports) — no AI Ops involvement; just personal capability win
- **Internal automation** (some reports) — AI Ops Team takes them, qualifies, runs as pilot
- **Business-critical / guest-facing** (rare from a Hackathon) — escalate to Digital Council

**Your recommendation**: at the regroup, classify every report into one of those three buckets on the spot. AI Ops Team picks up the middle bucket as their first cases.

**Decision needed**: confirm this is the intended handoff. If yes, the regroup serves a dual purpose (capability check + AI Ops case intake).

### B-Open questions (for either now or follow-up)

- Tooling beyond ChatGPT Business — does AI Ops need access to anything else (e.g., ChatGPT Team workspace shared, Anthropic API for specific cases, Microsoft Copilot for M365 integration)?
- Budget envelope — does AI Ops have a discretionary spend, or every case goes through normal procurement?
- Reporting cadence to Digital Council — quarterly status? On-demand when a case needs decision?

---

## Anticipated hard questions (and your answers)

| Likely question | Suggested answer |
|----------------|------------------|
| **"What's the measurable success criterion?"** | At the 4-week regroup: % of participants who report an actual workflow change they're still doing. Target ≥60%. Below that, the format failed and we redesign. |
| **"What if attendance is poor?"** | HQ-only scope keeps it small enough that Simon (CEO) endorsing the date should drive attendance. We can also frame it as "skill-building time, not optional". |
| **"Why now and not later when the new AI format is fully designed?"** | This *is* part of designing the new format. We can't define a bottom-up format without first building the bottom-up capability. Hackathon → 4-week regroup → from those 30+ workflow-changes we identify themes for the ongoing format. |
| **"What about Norway/Finland/restaurants?"** | Out of scope this run. Luleå HQ is the pilot; if it lands, we adapt the format for restaurants (different shape — shift-friendly, shorter, in-restaurant) and roll out next iteration. |
| **"Why ChatGPT and not Microsoft Copilot in M365?"** | Already settled at AI-Council Meeting 1 (June 2024) — every department picked ChatGPT. Use what people already have working accounts for. (If Johnny pushes Copilot now, accept and adjust — neither blocks the format.) |
| **"How do we know participants apply this back at their desks?"** | The 4-week commitment exercise — written, not verbal — is the main lever. Plus the regroup is on the calendar from day one, not announced after. |
| **"What's the cost?"** | Already verified with CEO (per locked decisions). 50-ish people × 3.5h = ~175 person-hours, ~one Mentimeter free tier, no facilitator cost (internal). |
| **"Why a smaller AI Ops Team than before?"** | The previous 8-person team's calendar problem killed momentum. A small operator core moves faster; function heads get consulted on cases that touch their domain, not seated by default. |
| **"Where does the new AI Ops Team get its authority?"** | From the governance flow — Digital Council delegates operational running of low-risk cases; lifts everything else for decision. AI Ops Team isn't deciding strategy, it's executing on the structured process. |
| **"What if a case is borderline — low risk operationally but ambiguous?"** | Default: AI Ops escalates to Digital Council. Cheaper to ask than to be wrong on guest/data exposure. |
| **"Who classifies a case at qualification?"** | AI Ops Team lead (André, then whoever takes the lead role over time). Documented criteria from the flow — not subjective. |
| **"Can a department run an AI case without going through AI Ops?"** | If it's pure individual productivity (personal ChatGPT use, no integration, no shared data) — yes, that's not what AI Ops is for. Anything that touches more than one person's workflow goes through AI Ops. |

---

## Numbers to have ready

| Metric | Value | Source |
|---|---|---|
| Luleå HQ headcount | ~40 people leadership tracked + others | `exports/organisation-skill/organisation-data.md` (~40 in HQ/leadership) |
| Final AI Operations Team size (dissolved ~April 2026) | 8 (André + 7 members) | `docs/policies/it-policies.md` |
| Cost validation | Verified with CEO | (confidential — Johnny aware) |
| Total event run-time | ~3.5 h | Plan schedule |
| 4-week regroup target attendance | 100% of original participants | Plan |

---

## Your asks (state these clearly)

**Hackathon-specific**:
1. **Decisions on the four Hackathon open items** — primary purpose of Part A.
2. **Sponsor endorsement in writing** — short Slack/Teams message you can quote in the invite, so it lands as a CDTO-backed initiative not an IT-team project.
3. **Permission to ask 2–3 ex-AI-Ops-Team members to facilitate** (Erik / Therese / Niklas / Caroline are likely yeses; you want Johnny's nod before approaching).
4. **Calendar slot from Johnny for the 4-week regroup** — book it now; without a forced regroup the commitments evaporate.

**AI Ops Team-specific**:
5. **Lock composition** (Model A / B; if A, the 3–5 names).
6. **Lock cadence** (recommend bi-weekly + async triage channel).
7. **Lock the use-case list home** (recommend Jira project).
8. **Robert Beney's involvement model** — pulled-in vs seated; trigger checklist owner.
9. **First Digital Council touchpoint** — when does Johnny want to take the new format and the first batch of cases (post-regroup) to the Digital Council? Calendar that too.
10. **Documentation handoff** — the governance flow you brought in is now in `docs/policies/it-policies.md` § 2b; any wording Johnny wants changed before it's the canonical version.

---

## Risk flags (things that might come up unexpectedly)

- **Annika starts parental leave Friday May 8** — Brand isn't represented in the Hackathon. Acknowledge once, move on.
- **Kamppi soft-open week** is also this week — André's bandwidth is split. The Hackathon date should not collide with Kamppi week 19 follow-up.
- **AI Ops Team members may feel demoted** — they were the centralised group; now everyone gets the capability. Frame the Hackathon as them becoming **internal coaches** (facilitator role), not getting their special status removed.
- **Grand Samarkand decommissioning** is also active and waits on Johnny Klippmark for T-0 — flag this as a separate thing if the meeting drifts. Don't let it derail the Hackathon pitch.

---

## Concrete next steps (after the meeting)

**Hackathon track**:
1. Update `docs/projects/plans/2026-05-ai-hackathon-lulea-hq.md` — move the four open-decision rows to ✅ Locked with their values.
2. Send the invitation (`inbjudan.html`) — fill in the bracketed date/location/contact placeholders with the agreed values.
3. Brief facilitators (60-min session 3 days before the event).
4. Calendar-block the event date + the 4-week regroup date.
5. Set up Mentimeter (5-min job — do this 1 week before).
6. Prep coffee/snacks logistics (HR or office manager).

**AI Ops Team track**:
7. Update `docs/policies/it-policies.md` — replace "**Pending follow-up**" line with the locked composition + cadence + intake details.
8. Save a memory entry for the new AI Ops Team format (replacing the dissolved one).
9. Reach out to the chosen members; confirm in writing.
10. Set up the case-list (Jira project) and async-triage channel.
11. Schedule the first Digital Council touchpoint (~6 weeks out — gives time for Hackathon + regroup + first batch of qualified cases).

---

## Open items from previous meeting

n/a — this is the first meeting on this topic.

---

**Bring to the meeting**: this brief (printed or on-screen), `pitch_hackathon.pptx` as backup material, and the plan link. Do not read from the slides — drive the conversation through the four decisions.
