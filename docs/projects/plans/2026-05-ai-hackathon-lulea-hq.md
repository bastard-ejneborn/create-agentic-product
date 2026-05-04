# AI Hackathon — Luleå HQ

> Status: **Planning** — pitch meeting with Johnny Bröms 2026-05-05 13:30 (Tue)
> Last updated: 2026-05-04
> Project lead: André Ejneborn (Senior IT Architect)
> Project sponsor: Johnny Bröms (CDTO)

---

## Mission

Replace the dissolved AI Operations Team's centralised "AI-Council" format with a bottom-up capability-building model. **This Hackathon is step 1**: teach Luleå HQ employees how to use AI in daily work so AI initiatives can emerge from anywhere — not be invented top-down.

**Goal per participant**: leave with one concrete personal AI use case they have actually tried, plus a written commitment to change one workflow within 4 weeks.

---

## Decisions

| Decision | Status | Value |
|---|---|---|
| Scope | ✅ Locked | **Luleå HQ only** (not whole-company; restaurants out of scope for this run) |
| Tooling | ✅ Locked | **ChatGPT Business** (BB-managed accounts — no rate-limit / personal-account issues) |
| Language | ✅ Locked | **Swedish** (all HQ staff speak Swedish) |
| Cost | ✅ Locked | Verified with CEO |
| Strategic framing | ✅ Locked | On-ramp for the new (post-AI-Operations-Team) AI format |
| Format | ✅ Locked | Half-day, cross-functional teams, Mentimeter voting, cumulative scoreboard |
| Round 1 length | ⚙️ Refined | Extended from 20 → 30 min |
| Round 2 length | ⚙️ Refined | Extended from 35 → 45 min |
| Follow-up cadence | ✅ Locked | **4-week regroup** — each participant returns with one changed workflow they actually applied |
| Date / time | ❓ Open | To confirm with Johnny in tomorrow's meeting |
| Beginner/advanced mix | ❓ Open | Mitigation: rotate "driver" role per team so less-experienced person types in some rounds |
| Facilitator ratio | ❓ Open | Suggested 1 facilitator per ~3 teams |
| Sensitive-data guardrails | ❓ Open | "Don't paste real customer/financial data" — to firm up before Round 2 launches |

---

## Schedule (refined)

Times anchor at 09:00; total run-time ~3h 30min including the commitment exercise.

| Time | Block | Length | Voting? |
|------|-------|--------|---------|
| 09:00 | Welcome + intro (what AI is / isn't, one honest example) | 30 min | — |
| 09:30 | **Warm-up: Mötet från helvetet** | 20 min | No points |
| 09:50 | **Round 1: Promptmakeovern** | 30 min | Yes |
| 10:20 | **Round 2: Spegla ditt arbete** | 45 min | Yes |
| 11:05 | **Final: Målgruppsflippet** | 30 min | Audience votes |
| 11:35 | Show & tell — what surprised you? | 20 min | — |
| 11:55 | **Commitment exercise** — write your one workflow change | 15 min | — |
| 12:10 | Wrap-up + 4-week regroup date confirmed | 15 min | — |
| 12:25 | End | | |

Bonus tasks (use only if a round finishes early or as a fallback):
- **Gummianksdebuggern** — describe a stuck problem, use AI as thinking partner
- **3-mejlsutmaningen** — write same message formal / informal / brutally short, pick one
- **Kunskapsöverföringen** — teach AI a niche role-specific process, ask for an onboarding guide

---

## Tasks

### Mötet från helvetet (warm-up, no points)
Fictional Swedish meeting transcript (handwritten-notepad style, margin notes, crossed-out words, passive-aggressive comments). Cast: Magnus (chair, leaves early), Linda (budget owner), Dev (late, takes last coffee), Sara (only competent one), Tomas (phone with static, Magnus agrees with him anyway). Topics: launch date 22nd vs 29th, budget overrun 85k SEK, missing data-migration owner, Nordavind contract by Thursday. Each team uses AI to extract action points, write a clean summary, and draft a follow-up email.

### Round 1 — Promptmakeovern (30 min, vote)
All teams get the same badly written prompt; iterate it until output is genuinely useful. Easy to judge because everyone starts from an identical baseline. Trains the highest-leverage AI skill: improving instructions. Judging: clarity of final output, usefulness, quality of iteration.

### Round 2 — Spegla ditt arbete (45 min, vote — heart of the day)
Teams pick a shared cross-functional task (curated list of 4–5 patterns provided, e.g. department intro for a new hire, cross-functional FAQ, shared-process summary). Use AI; **at least 3 follow-up prompts before submitting**. Judging: personal relevance, output usefulness, iteration quality.

### Final — Målgruppsflippet (30 min, audience votes)
Pick an internal concept/process/term; use AI to explain it for three audiences (new hire, customer, sceptical executive). Teams divide and combine. Requires real collaboration and reasoning, not just prompting.

---

## Team composition

- Cross-functional only — **no two people from the same department on the same team**
- Reason: same-department teams solve only same-department tasks and miss the point that AI is broadly applicable
- Mitigation for beginner/advanced gap: rotate a "driver" role each round so less-experienced people type at least once

---

## Voting

- **Mentimeter** (free tier sufficient), no participant accounts needed, anonymous, live results on screen
- Three votes total: after Round 1, Round 2, Final
- Rule: **cannot vote for own team** (set up Mentimeter so this is enforceable, e.g. team-tagged voting links)
- Cumulative scoreboard updated after every vote

---

## Ground rules (printed + on a slide)

- No bad prompts; weird outputs are part of learning
- Not technical — you just need to know your own job
- **Sensitive data**: do not paste real customer, financial, employee, or vendor data into any AI tool. Use anonymised or fictional stand-ins. Round 2 task patterns are designed so this is doable.
- Goal is one useful insight, not perfection
- Ask your neighbour, the facilitator, or the AI itself

---

## Prompting guidance (taught in welcome block)

A weak prompt: *"Write an email."* A strong prompt: *"Write a short, professional follow-up email to a client who has not responded to our quote since last week. The tone should be friendly but clear."*

The three things that improve any prompt:
1. **Context** — who you are, who the recipient is, what the purpose is
2. **Specificity** — length, tone, format, exactly what you want
3. **Iteration** — follow-up prompts always improve the result; the first answer is never the last

---

## Materials (already prepared)

- `inbjudan.html` — digital invitation (dark navy + teal card, bracketed placeholders for date / location / contact)
- `hackathon_presentation.pptx` — 9 slides for the event itself
- `hackathon_handout.docx` — A4 participant handout, colour-coded sections
- *Mötet från helvetet* — handwritten-notepad transcript widget, Swedish, ready to print/display
- `pitch_hackathon.pptx` — 7-slide pitch deck for tomorrow's meeting with Johnny

---

## Risks

| # | Risk | Severity | Mitigation |
|---|------|----------|-----------|
| 1 | Sensitive data pasted into ChatGPT (real customer/financial info) | High | Pre-defined fictional task patterns for Round 2; reinforced ground rule; anonymisation called out in welcome |
| 2 | Advanced ChatGPT users dominate teams; beginners spectate | Medium | Rotate "driver" role per round; deliberate mixing of experience levels in team composition |
| 3 | Single host can't facilitate + Mentimeter + unstick teams | Medium | 1 facilitator per ~3 teams; brief them in advance |
| 4 | Energy drops in the 3.5-hour run | Medium | Coffee break after Round 1 if needed; live scoreboard reveal moment after each vote |
| 5 | "One workflow change" commitments collected but never followed up on | Medium | 4-week regroup date set at the wrap-up, calendar invite sent in the same week |

---

## Pitch meeting prep — 2026-05-05 13:30 with Johnny Bröms

Lead the pitch with these in order:

1. **Mission frame** (1 line): teach the company to use AI well so initiatives emerge from the bottom up — replacing top-down AI-Council with bottom-up capability.
2. **What's locked** (above table) — short.
3. **The four open questions** that should be decided in the meeting:
   - Date / time
   - Sensitive-data guardrails (firm-up)
   - Facilitator support (who, how many)
   - Beginner/advanced mix (mitigation acceptable, or different format?)
4. **Materials handed over** — pitch deck as backup, don't read from it.

Hand-off goal: leave with all four open decisions made, then we move to scheduling the date and sending invitations.

---

## Issues Log

| # | Issue | Severity | Resolution | Status |
|---|-------|----------|-----------|--------|
| | | | | |

---

## Lessons Learned

Filled in after the event. Capture: what worked, what didn't, which tasks landed, sensitive-data near-misses, energy curve. Feed into a "Hackathon — second iteration" template if BB rolls this out to restaurants or other markets later.

| Theme | What happened | Action |
|-------|---------------|--------|
| | | |

---

## 4-week regroup (placeholder)

- Date: TBD (target: 4 weeks after event date)
- Format: 30-min meeting, each participant shares one workflow they actually changed
- Output: short write-up captured here as Lessons Learned input + portfolio status update
