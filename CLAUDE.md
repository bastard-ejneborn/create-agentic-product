# CLAUDE.md — Creative Product Team

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

Memory is auto-loaded from `~/.claude/projects/<this-repo>/memory/`. The index (`MEMORY.md`) lists 8+ entries covering things like Annika's parental leave window, shared-mailbox Azure Automation, music hardware variance per restaurant, the dissolved AI Operations Team, and IT support routing rules.

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

## Vad det här projektet handlar om

Det här är ett ramverk för att snabbt sätta upp ett AI-drivet kreativt team som hjälper användaren ta en produktidé från koncept till lansering. Teamet består av specialiserade agenter som samarbetar i faser.

## Arbetsflöde

### Steg 1: Förstå användarens behov

Innan något annat — förstå vad användaren vill bygga. Ställ frågor om:

1. **Produkt**: Vad är det för produkt/tjänst? Fysisk, digital, hybrid?
2. **Målgrupp**: Vem är den för? Geografi, demografi, beteende?
3. **Marknader**: Vilka länder/regioner? En marknad eller flera?
4. **Ambition**: MVP/test eller full lansering?
5. **Budget**: Indikativ nivå — påverkar strategi och kanalval
6. **Tidplan**: När ska det vara klart?
7. **Befintligt material**: Finns det redan research, design, copy, kod?

Baserat på svaren, sätt ihop rätt team. Inte alla agenter behövs för varje projekt.

### Steg 2: Sätt ihop rätt team

Teamet ska skräddarsys för varje projekt. Baserat på användarens produkt, marknad och mål — föreslå vilka agenter som behövs. Var kreativ och tänk bortom standardrollerna.

#### Alltid med
- **project-lead** — Koordinerar allt, driver framåt, kvalitetssäkrar

#### Exempelroller (använd som inspiration, inte checklista)

**Research & Strategi**: competitor-analyst, market-researcher, cultural-analyst, legal-analyst
**Koncept & Design**: brand-strategist, product-designer, art-director, copywriter
**Digital**: frontend-dev, backend-dev
**Lansering & Tillväxt**: marketer, social-media-strategist

Men lägg gärna till agenter som passar projektet — t.ex. en **sustainability-advisor** för gröna produkter, en **pricing-strategist** för SaaS, en **packaging-designer** för fysiska varor, en **community-manager** för plattformsprodukter, eller helt nya roller som projektet kräver.

Förklara för användaren vilka agenter du föreslår och varför. Låt dem justera teamet innan arbetet börjar.

### Steg 3: Kör faserna

Varje fas bygger på den förra. Agenter inom en fas kan köra parallellt.

```
Fas 1: Research & Analys
         |
Fas 2: Koncept & Design
         |
Fas 3: Byggande (digital, fysisk, eller båda)
         |
Fas 4: Lansering & Tillväxt
```

Antalet faser och vilka agenter som ingår i varje fas anpassas efter projektet. Vissa projekt behöver fler faser, andra färre.

Mellan faserna: granska leveranser, stäm av med användaren, justera kursen.

### Steg 4: Generera kreativt material

Använd skills och agenter (se Skills-tabellen nedan) för att skapa bilder, musik och röst. Allt material sparas i `assets/` organiserat per typ.

## Projektstruktur

```
.claude/
  agents/          <- AI-agenter (en .md per agent)
  skills/          <- Automationsverktyg (bildgenerering, videogenerering, etc.)
docs/              <- All research, strategi, copy, planer
assets/
  images/
    reference/     <- Godkända referensbilder per produkt
  videos/          <- Genererade videor
  audio/           <- Musik, röster, dialoger
web/               <- Frontend (om det behövs)
server/            <- Backend (om det behövs)
scripts/           <- Hjälpscript
.env               <- API-nycklar (gitignored)
```

## Agenter

Alla agenter finns i `.claude/agents/`. Varje agent har:
- **YAML frontmatter**: name, description, tools, model
- **Tydlig roll**: Vad agenten ansvarar för
- **Arbetsprocess**: Steg-för-steg workflow
- **Samarbete**: Hur agenten interagerar med andra

### Kreativa agenter
- **image-creator** — Bildgenerering via Gemini (text-to-image, image-to-image)
- **elevenlabs-voice** — Röstdesign och dialoggenerering via ElevenLabs
- **suno-songwriter** — Musikskapande med stilbeskrivningar och lyrics för Suno AI

### C-level rådgivare
- **cio-advisor** — IT-strategi, leverantörshantering, säkerhet, compliance, budgetar, infrastruktur
- **cdo-advisor** — Digital strategi, datahantering, kundupplevelse, KPI:er, förändringsledning
- **cto-advisor** — Teknikstrategi, arkitektur, teknisk skuld, build vs buy, plattformstillförlitlighet

### IT-arkitektur
- **it-architect** — Systemarkitektur, integrationer, ADR:er, infrastruktur, teknikstack för multi-site QSR

### Projektledning
- **project-manager** — Projektplanering, statusrapportering, riskhantering, RACI, retrospektiv

### Marknadsföring
- **marketing-strategist** — Kampanjplanering, varumärkesutveckling, innehållsstrategi, positionering

### Operations
- **coo-advisor** — Restaurangdrift: KPI:er, prestanda per plats/distrikt/region, butiksbesök, operativa granskningar

### Gäststöd
- **guest-support-agent** — Ärenden från gäster/kunder: klagomål, fakturering, matsäkerhet, återbetalningar

Se `.claude/skills/agent-builder/SKILL.md` för att skapa nya agenter.

## Skills

| Skill | Användning |
|-------|-----------|
| `agent-builder` | Skapa nya agenter |
| `gemini-imagegen` | Bildgenerering via Google Gemini (text-to-image, image-to-image) |
| `suno-music-skill` | Musikskapande — stilbeskrivning och lyrics för Suno AI |
| `elevenlabs-skill` | Röstdesign — 300-teckens röstbeskrivningar för ElevenLabs |
| `company-strategy` | Fånga och strukturera företagets strategi, vision, OKR:er och prioriteringar |
| `decision-framework` | Strukturerad beslutsprocess med adaptiv formalitet och beslutslogg |
| `stakeholder-briefing` | Exekutiv kommunikation — styrelseuppdateringar, business cases, incidentrapporter |
| `budget-tracker` | IT/digital/tech-budget — kategoriserad spend, committed vs discretionary, prognoser |
| `project-portfolio` | Projektportfölj — aktiva projekt, status, kapacitet, beroenden |
| `risk-register` | Riskregister — organisatoriska risker, scoring, mitigering, ägarskap |
| `vendor-manager` | Leverantörshantering — kontrakt, SLA:er, förnyelsekalender, kostnader |
| `team-structure` | Teamstruktur — kompetenser, kapacitet, nyckelrisker, rekryteringsplan |
| `meeting-prep` | Mötesförberedelser — samlar kontext och skapar fokuserade briefings |
| `project-planner` | Detaljerad projektplanering — WBS, milstolpar, beroenden, resursallokering |
| `status-report` | Operativa statusrapporter — veckovis team, styrgrupp, sponsor |
| `retro-facilitator` | Retrospektiv och post-mortems — insikter och uppföljning |
| `raci-matrix` | Ansvarsmatris — Responsible, Accountable, Consulted, Informed |
| `campaign-planner` | Kampanjplanering — mål, målgrupp, kanaler, budget, KPI:er |
| `brand-guidelines` | Varumärkesriktlinjer — tonalitet, visuell identitet, budskapsramverk |
| `tech-radar` | Teknikradar — Adopt/Trial/Assess/Hold för organisationens teknologier |
| `competitor-watch` | Konkurrensbevakning — profiler, aktivitetslogg, battle cards, feature-jämförelse |
| `freshservice` | FreshService helpdesk — ärenden, SLA, dashboard, assets, changes (read-only) |
| `google-stitch` | AI UI-design — generera wireframes, landningssidor, appskärmar från text (HTML/Tailwind) |
| `local-marketing` | Lokal marknadsföring — butiksbesök, sampling, partnerskap, flygblad, aktivitetslogg per restaurang |
| `simphony` | Oracle Simphony — försäljning, gästnotor, produktmix, personal, betalningar per restaurang (read-only) |
| `guest-support` | Gäststöd — triagering, svar, kompensation, eskalering, ärendelogg för QSR-restauranger |
| `company-policies` | Avdelningspolicyer — IT, operations, marknadsföring, HR, ekonomi, gäststöd i strukturerat format |
| `operations-dashboard` | Restaurangdrift — KPI:er, hierarki (COO→RM→DM→RM), butiksbesök, operativa granskningar |
| `system-architecture` | Systemarkitektur — systemlandskap, integrationer, ADR:er, teknikstack, infrastruktur |

## Teknik & Plattform

Inga fasta teknikval. Diskutera med användaren vad som passar bäst för projektet:

- Behövs en egen sajt, eller räcker en befintlig plattform (Shopify, Squarespace, WordPress, etc.)?
- Behövs ett eget backend, eller fungerar en BaaS (Supabase, Firebase, etc.)?
- Vilken tekniknivå har användaren — ska de kunna underhålla det själva?

Föreslå lösningar baserat på projektets behov, budget och tidplan. Dokumentera teknikvalen i `docs/`.

## API-nycklar & .env

Skills som bildgenerering, video och musik kräver API-nycklar. Innan generering kan börja:

1. Fråga användaren vilka nycklar de har (OpenRouter, ElevenLabs, etc.)
2. Fråga om de vill klistra in nycklarna så att `.env` skapas automatiskt, eller om de föredrar att lägga in dem själva
3. `.env`-filen ska ligga i projektroten (`/create-agentic-product/.env`) och är gitignored
4. Skapa aldrig `.env` utan användarens godkännande — berätta var filen ska ligga och vad som behövs

## Viktiga principer

### Produktbild som referens
- Tidigt i processen ska en **produktbild i studiokvalitet** tas fram (genererad eller uppladdad av användaren)
- Användaren måste **godkänna produktbilden** innan den används vidare
- Den godkända bilden sparas i `assets/images/reference/` och används som **referensbild** vid all efterföljande bildgenerering (via image-to-image i gemini-imagegen)
- **Videor**: Om videogenerering behövs, utvärdera aktuella verktyg (Runway, Kling AI, Google Veo) — OpenAI Sora är avvecklat

### Internationalisering
- Alltid analysera kulturella skillnader innan marknadsinträde
- Alltid kolla lokala lagar och certifieringskrav
- Anpassa copy och kampanjer per marknad — översätt inte bara, lokalisera
- Respektfull hantering av kulturella känsligheter

## Docs-katalogen

Alla strategidokument hamnar i `docs/`. Varje agent levererar sina dokument dit med beskrivande filnamn. Namnge filer efter innehåll, t.ex. `competitor-analysis.md`, `go-to-market.md`, `tone-of-voice.md`.
