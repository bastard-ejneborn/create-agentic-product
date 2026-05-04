# IT Policies — Bastard Burgers
> Last updated: 2026-05-04 (added Digital Council ↔ AI Operations Team governance flow + autonomy/escalation boundaries; AI Ops Team composition pending 2026-05-05 1:1)
> Owner: Johnny Bröms (CDTO)
> Review cycle: Annual

## Table of Contents
- [AI Policy](#ai-policy)
- [AI Initiatives Framework](#ai-initiatives-framework)

---

## AI Policy

> Version: 1.0 | Date: 2024-05-07 | Author: Johnny Bröms

### 1. Purpose

This AI policy defines the guidelines and standards for the use of artificial intelligence (AI) within Bastard Burgers operations and offices across all countries of operation.

We are committed to leveraging AI to enhance our service, streamline our operations, and promote sustainable growth. We will do it with curiosity and an open mind, trying to see the possibilities it could give us.

### 2. Principles for AI Use

- **Transparency**: We will strive to be open about how AI is used in our business and its impact.
- **Ethics**: AI solutions will be developed and implemented ethically, respecting customer privacy and data protection.
- **Security**: We will maintain the highest possible security standards to protect both customer data and our internal systems.
- **Inclusion**: AI technology will be used in a manner that promotes inclusion and prevents discrimination.

### 3. Areas of Application

AI technologies could be utilized in the following areas (examples):
- **Customer Service**: Chatbots to handle customer inquiries and bookings
- **Inventory Management**: Automation of stock and ordering processes to optimize inventory levels and reduce food waste
- **Marketing Strategies**: Analysis of customer data to create personalized marketing campaigns and improve customer engagement
- **Food Preparation**: Integration of automated solutions to streamline cooking and packaging processes

### 4. Collaborations and Suppliers

- Work closely with existing suppliers to integrate their AI solutions in a mutually beneficial manner
- Suppliers must adhere to our AI policy and meet requirements on transparency, ethics, and security

### 5. Monitoring and Reporting

- Regular review of the performance and impact of AI systems on the business
- Reporting on the effectiveness of AI initiatives is within the responsibility of the CIO/CDO, reporting to the management team and other stakeholders

### 6. Policy Updates

This policy will be regularly reviewed and updated to reflect new technological advances and changes in legislation.

### 7. Legal Compliance

All AI initiatives will be conducted in accordance with applicable laws and regulations in the countries where we operate.

> By adhering to this policy, we ensure that our use of AI supports our vision of sustainable growth and improved customer service, while protecting the privacy and security of our customers and employees.

---

## AI Initiatives Framework

> Version: 1.0 | Date: 2024-05-07 | Author: Johnny Bröms

### 1. Introduction

This document serves as a comprehensive guide to planning, executing, and reviewing AI initiatives within the organization, ensuring they are consistent with the corporate AI policy and strategic objectives.

### 2. Organization

**Mission**: Define and generate AI initiatives creating benefits in daily operation, operational efficiency, excellence, and ROI.

**Goal**: Find initiatives within normal daily business, kept within normal working hours.

**Reporting**: Initially to CDO, who brings initiatives to the management team. *(Evolution: AI-Council (2024) → AI Operations Team with Digital Council tasks → **dissolved 2026-05**, replacement meeting/members TBD.)*

**Team Lead**: André Ejneborn (during AI Operations Team era — through 2026-05)

**Status as of 2026-05-04**: The AI Operations Team has been **dissolved**. A new meeting with new members is planned but format / attendees / cadence are TBD. The tables below are preserved as **historical record** of the team that ran from May 2024 through April 2026.

**Original team members** (May 2024):
| Department | Members |
|-----------|---------|
| HR | TBD (Role) |
| Marketing | Annika Elworth |
| Procurement | Niklas Heinermark |
| Operations & Construction | Malin Hansegård, Johannes Norrblom, Caroline Pettersson |
| Finance | Emil Lundquist, Filip Forsling |

**Final team members** (as of dissolution, ~April 2026):
| Member | Department / Function | Role in Company |
|--------|----------------------|-----------------|
| **André Ejneborn** (Lead) | Digital & Tech / IT | Senior IT Architect |
| Caroline Johansson | Operations | Head of Project and Development |
| Malin Hansegård | Marketing | Head of Marketing |
| Johannes Norrblom | Operations | Regional Manager North |
| Annika Elworth | Brand | Brand & Creative Manager |
| Niklas Heinermark | Finance / Procurement | Head of Procurement |
| Therese Alm | People / HR | HR Business Partner |
| Erik Löfgren | Finance | Digital Sales, CRM & Commercial Controlling Manager |

**Changes from original to final**:
- Added: Therese Alm (HR — replaced Maja Lundqvist), Erik Löfgren (Finance)
- Removed: Filip Forsling, Emil Lundqvist, Maja Lundqvist

**Pending follow-up**: Composition + cadence of the new AI Operations Team to be decided in the André × Johnny Bröms 1:1 (2026-05-05). Governance flow with Digital Council captured below.

### 2b. Governance flow — Digital Council ↔ AI Operations Team (proposed, 2026-05)

> *Digitala rådet sätter riktning och tar besluten. AI Operations Team gör arbetet möjligt i praktiken.*

**Digitala rådet** är **styrforumet**. De avgör vilka AI-case som är viktiga, vilka som får gå vidare, vilka verktyg eller leverantörer som ska godkännas och när ett case är redo att gå från pilot till produktion. Ska särskilt in när ett AI-case:
- påverkar flera funktioner
- kräver integrationer
- använder intern eller känslig data
- innebär ny leverantör
- kan påverka gäst, varumärke, drift eller försäljning

**AI Operations Team** är den **operativa motorn**. De tar emot idéer, strukturerar case, ser till att syfte, ägare, data, risk, test, fallback, support och uppföljning finns på plats. De håller koll på use-case-listan: idé → pilot → produktion → parkerade.

**Flöde:**

1. **Idé uppstår** — någon i verksamheten ser ett problem eller en möjlighet där AI kan hjälpa.
2. **AI Operations Team kvalificerar caset** — Vad är problemet? Vilken nytta? Vilken data behövs? Persondata/känslig info? Påverkas gäst, drift, pengar eller varumärke?
3. **Caset klassas** — *individuell produktivitet* / *intern automation* / *affärskritisk eller gästpåverkande AI*. Ju högre påverkan, desto hårdare styrning.
4. **Lågrisk drivs operativt** — internt, avgränsat, ingen känslig data, inga större integrationer → AI Operations Team driver vidare som test/pilot.
5. **Högre risk lyfts till Digitala rådet** — integrationer, ny leverantör, känslig data, produktion, eller påverkan på gäst/drift/varumärke → Digitala rådet fattar beslut.
6. **CISO/Compliance kopplas in vid behov** — persondata, betaldata, access, loggning, avtal, GDPR, PCI-DSS, eller leverantörsrisk → Robert Beney (Head of Information Security and Compliance) involveras.
7. **Beslut → pilot → produktion → uppföljning** — när Digitala rådet godkänt ser AI Operations Team till att lösningen testas, dokumenteras, får ägare, fallback, supportväg och uppföljning.

**Hård regel**: inget AI-case bör gå till produktion om det inte går att förstå, testa, uppdatera, supporta och ta över av någon annan än byggaren.

**Sammanfattning för presentation**:
> *"Digitala rådet är inte byggteamet, utan besluts- och prioriteringsforumet. AI Operations Team är arbetsmaskinen som tar idéer till strukturerade, testbara och förvaltningsbara AI-case. När caset är lågrisk kan det drivas operativt. När det påverkar data, integrationer, gäst, drift, varumärke eller produktion lyfts det till Digitala rådet för beslut."*

### 2c. AI Operations autonomy — when to act vs when to escalate

**Guiding rule**: anything **local, internal, and reversible** can move forward without Digital Council. Everything that **scales, connects, exposes, or has business-critical impact** must be escalated.

#### What you CAN do without Digital Council

**1. Individual productivity (broad freedom)**
You can:
- Write texts, emails, presentations
- Summarise meetings
- Analyse material
- Draft decisions
- Structure ideas

As long as:
- You use approved tools
- You do not paste sensitive data
- You quality-check the output yourself

This is deliberately the *fast zone* in the model.

**2. Small internal use cases (within a team)**
You can usually:
- Test AI inside a workflow
- Build simple automations
- Build support for reports, analysis, support handling, etc.

Examples:
- *"Help us sort support tickets"*
- *"Compile weekly reports"*
- *"Help HR answer standard questions"*

As long as:
- It does not involve sensitive data (or it is properly controlled)
- It does not require integrations
- It does not broadly affect other teams
- It has a clear owner

This is AI Operations Team's home turf.

**3. Pilots (important)**
You can:
- Test ideas
- Run small pilots
- Validate value

But:
- At small scale
- With clear scope
- Without engaging the whole organisation

**Key principle**: it's fine to experiment — as long as the experiment doesn't become production by accident.

#### When you must NOT act alone

This is where the misunderstanding usually starts. **It is not the activity that determines — it is the consequence.**

Escalate (do not run alone) when you start to:

| # | Trigger | Why |
|---|---------|-----|
| 1 | **Connect systems** | Integrations require Digital Council approval |
| 2 | **Use sensitive or broad internal data** | HR, support, commercial data |
| 3 | **Affect multiple teams** | Becomes an organisational matter |
| 4 | **Go to production** | Almost always belongs in Digital Council |
| 5 | **Affect guest, money, or brand** | Always escalated |

#### The mental shift (good to repeat in meetings)

> *"It's not the activity that determines — it's the consequence."*

You can build a fair amount yourself. You can test a fair amount yourself. But you cannot **scale**, **connect**, **expose**, or cause **business-critical impact** without escalating.

#### Simple traffic-light model

**Green — run it yourselves**
- Local
- Internal
- Low risk
- No integration
- No sensitive data
- No guest impact

**Yellow — check with AI Operations Team**
- Affects one team
- Starting to look like a "real solution"
- Pilot with actual usage

**Red — escalate to Digital Council**
- Affects multiple teams
- Requires integration
- Uses sensitive data
- Going to production
- Affects guest / operations / money / brand

#### Easy to miss

Digital Council is **not there to approve ideas**. They engage when something is about to become:
- Standard
- Scalable
- A dependency in the business

#### Direct answer

You do **not** need to bring everything to Digital Council:
- You can experiment freely at small scale
- You can build internal support
- You can test and validate

But the moment it gets *real* — production-grade, scaled, integrated, sensitive, or guest/brand-touching — it goes up.

### 3. Way of Working

- Meet regularly (originally monthly, now weekly)
- Every member should come prepared
- Goal: regularly demonstrate an AI initiative in a department that follows the AI policy and delivers measurable benefits
- Team lead provides strategic overview and technical solutions, platforms, etc.
- **Each member is an ambassador** — responsible for driving AI adoption in their own department

### 4. AI Initiative Template

Every AI initiative should document:

**Project basics**: Name, description, objectives (primary + expected benefits), scope (inclusion/exclusion)

**AI Technology**: Type of AI (ML, NLP, robotics, etc.), provider/platform

**Policy Alignment** (mandatory):
- Transparency: How does the project uphold transparency?
- Ethics: What ethical considerations are addressed?
- Security: What security measures protect data and privacy?
- Inclusion: How does the project ensure fairness and prevent discrimination?

**Stakeholders**: Internal and external

**Timeline**: Start date, end date, key milestones

**Budget**: Estimated cost, funding source

**Expected ROI**: Quantitative (metrics) and qualitative (non-measurable benefits)

**Risks and Mitigation**: Identified risks with mitigation strategies

**Monitoring and Evaluation**: Performance metrics, reporting cadence, review points

**Approval**: Prepared by, reviewed by, approved by

---

## Version Log

| Date | Change | Responsible |
|------|--------|-------------|
| 2024-05-07 | AI Policy v1.0 initialized | Johnny Bröms |
| 2024-05-07 | AI Initiatives Framework v1.0 initialized | Johnny Bröms |
| 2026-04-08 | Imported into company policies framework | Company Policies skill |
