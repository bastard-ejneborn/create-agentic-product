---
name: brand-guidelines
description: Use when defining or referencing brand identity — tone of voice, visual identity, messaging framework, naming conventions. Also use before creating any marketing or creative content to ensure brand consistency.
---

# Brand Guidelines

Define and maintain a living brand guide that all creative and marketing agents reference before producing content.

## Two Input Paths

### Interview Mode

1. **Brand essence**: What does your brand stand for? How do you want to be perceived?
2. **Tone of voice**: How does the brand sound? (formal/casual, serious/playful, authoritative/friendly)
3. **Visual identity**: Colors, typography, logo usage rules, imagery style
4. **Messaging**: Key messages, value propositions, taglines, elevator pitch
5. **Audience**: Who are you talking to? (reference audience-personas if available)
6. **Competitors**: How do you differentiate visually and verbally?
7. **Do's and Don'ts**: What should the brand never do or say?

### Import Mode

If the user has existing brand materials (style guide, brand book):
1. Read provided documents
2. Structure into standard format
3. Identify gaps
4. Ask follow-up questions

## Output Format

Save to `docs/marketing/brand-guidelines.md`:

```markdown
# Brand Guidelines
> Last updated: YYYY-MM-DD
> Brand: [company/product name]

## Brand Essence

**Mission**: [Why we exist]
**Vision**: [Where we're going]
**Values**: [3-5 core values with one-line explanations]
**Brand personality**: [3-5 adjectives that describe the brand as a person]
**Positioning statement**: [For [audience], [brand] is the [category] that [differentiator] because [reason to believe]]

## Tone of Voice

### Voice Attributes

| Attribute | We Are | We Are NOT |
|-----------|--------|-----------|
| [e.g., Confident] | [example] | [counter-example] |
| [e.g., Approachable] | [example] | [counter-example] |
| [e.g., Clear] | [example] | [counter-example] |

### Writing Style

- **Sentence length**: [Short and direct / Varied / Long-form]
- **Vocabulary**: [Simple and accessible / Technical when needed / Industry jargon OK]
- **Perspective**: [We/Our / You/Your / Third person]
- **Contractions**: [Yes/No]
- **Humor**: [When appropriate / Sparingly / Never]
- **Emojis**: [Yes, limited / No]

### Tone Adjustments by Context

| Context | Tone Shift | Example |
|---------|-----------|---------|
| Marketing website | Confident, aspirational | "Transform how your team works" |
| Support docs | Helpful, patient | "Here's how to fix that" |
| Social media | Casual, engaging | "We just shipped something cool" |
| Crisis comms | Serious, transparent | "We take this seriously" |
| Sales materials | Professional, value-focused | "Reduce costs by 40%" |

## Messaging Framework

### Elevator Pitch
[30-second version of what you do and why it matters]

### Key Messages
1. **Primary**: [Core message]
2. **Supporting**: [Message 2]
3. **Supporting**: [Message 3]

### Value Propositions
| Audience | Key Value | Proof Point |
|---------|-----------|-------------|
| [segment] | [what they get] | [evidence] |

### Words We Use / Words We Don't

| Use | Don't Use | Why |
|-----|----------|-----|
| [preferred term] | [avoided term] | [reason] |

## Visual Identity

### Colors
| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| Primary | #[hex] | [r,g,b] | Main brand color, CTAs |
| Secondary | #[hex] | [r,g,b] | Accents, highlights |
| Neutral | #[hex] | [r,g,b] | Text, backgrounds |

### Typography
| Usage | Font | Weight | Size |
|-------|------|--------|------|
| Headings | [font] | [weight] | [size range] |
| Body | [font] | [weight] | [size range] |
| UI/Buttons | [font] | [weight] | [size] |

### Logo Usage
- **Minimum size**: [px/mm]
- **Clear space**: [rule]
- **Backgrounds**: [approved backgrounds]
- **Never**: [list of logo misuses]

### Imagery Style
- **Photography**: [style — lifestyle, product, abstract, etc.]
- **Illustrations**: [style — flat, 3D, hand-drawn, etc.]
- **Icons**: [style — outlined, filled, rounded, etc.]
- **People**: [diverse, professional, candid, etc.]

## Do's and Don'ts

### Do
- [Brand-consistent behavior]
- [Brand-consistent behavior]

### Don't
- [Brand violation]
- [Brand violation]

## Examples

### Good Example
> [Real or mock example of on-brand content with annotation]

### Bad Example
> [Real or mock example of off-brand content with annotation explaining why]
```

## How Agents Use This

Before creating any content (copy, images, campaigns, social posts), agents should:
1. Check if `docs/marketing/brand-guidelines.md` exists
2. Reference tone of voice for all written content
3. Use approved messaging and value propositions
4. Follow visual identity for any design work
5. Check "Words We Use / Don't Use" for terminology
6. Flag when requested content might violate brand guidelines

## Updates

- "We're repositioning from enterprise to SMB" — update positioning, tone, messaging
- "New brand colors approved" — update visual identity
- "Add 'AI-powered' to words we don't use" — update word list
- Always update `Last updated` date
