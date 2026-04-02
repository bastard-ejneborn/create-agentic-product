---
name: google-stitch
description: Use when the user wants to create UI designs, wireframes, landing pages, app screens, or web design mockups. Also use when brainstorming visual designs for marketing, product pages, or dashboards. Generates HTML/Tailwind from text prompts.
---

# Google Stitch — AI UI Design

Generate high-fidelity UI designs from text descriptions using Google Stitch. Outputs HTML + Tailwind CSS, screenshots, and interactive prototypes.

## Requirements

### For Claude Code (MCP — Recommended)

Add the Stitch MCP server to your Claude Code settings for native tool access:

1. Get your API key from [stitch.withgoogle.com](https://stitch.withgoogle.com) → Settings → API Key
2. Add to `.env`:
   ```bash
   STITCH_API_KEY=your-stitch-api-key
   ```
3. Add the MCP server to `.claude/settings.local.json`:
   ```json
   {
     "mcpServers": {
       "stitch": {
         "url": "https://stitch.googleapis.com/mcp",
         "headers": {
           "Authorization": "Bearer ${STITCH_API_KEY}"
         }
       }
     }
   }
   ```
4. Restart Claude Code. Stitch tools will be available natively.

### For Codex / ChatGPT / CLI Fallback

Use the Node.js script:

1. Install the SDK:
   ```bash
   npm install @google/stitch-sdk
   ```
2. Add to `.env`:
   ```bash
   STITCH_API_KEY=your-stitch-api-key
   ```
3. Run the script (see Commands below)

## Commands (CLI Script)

```bash
# Generate a UI screen from a text prompt
node .claude/skills/google-stitch/scripts/stitch.js generate \
  --prompt "A modern SaaS pricing page with three tiers" \
  --device desktop \
  --output assets/images/pricing-page

# Generate with pro quality (uses Gemini 2.5 Pro, limited quota)
node .claude/skills/google-stitch/scripts/stitch.js generate \
  --prompt "Mobile onboarding flow with progress indicator" \
  --device mobile \
  --quality pro \
  --output assets/images/onboarding

# Generate variants (up to 5 alternatives)
node .claude/skills/google-stitch/scripts/stitch.js variants \
  --prompt "Hero section for a fintech landing page" \
  --count 3 \
  --output assets/images/hero-variants

# Edit an existing screen
node .claude/skills/google-stitch/scripts/stitch.js edit \
  --project PROJECT_ID \
  --screen SCREEN_ID \
  --prompt "Change the CTA button to green and make the headline larger"

# Extract HTML from a generated screen
node .claude/skills/google-stitch/scripts/stitch.js html \
  --project PROJECT_ID \
  --screen SCREEN_ID \
  --output web/pricing.html

# Create a multi-screen flow (up to 5 screens)
node .claude/skills/google-stitch/scripts/stitch.js flow \
  --prompt "E-commerce checkout: cart → shipping → payment → confirmation" \
  --device mobile \
  --output assets/images/checkout-flow
```

## Script Arguments

| Argument | Short | Description |
|----------|-------|-------------|
| `--prompt` | `-p` | Text description of the desired UI |
| `--output` | `-o` | Output directory (saves HTML + screenshot) |
| `--device` | `-d` | Target device: `desktop`, `mobile`, `tablet`, `agnostic` (default: `desktop`) |
| `--quality` | `-q` | Generation quality: `standard` (default) or `pro` |
| `--count` | `-c` | Number of variants to generate (max 5) |
| `--project` | | Project ID (for edit/html commands) |
| `--screen` | | Screen ID (for edit/html commands) |

## Prompt Tips

### Be Specific About Layout
```
A dashboard with a sidebar navigation on the left, a top header with 
user avatar, and a main content area showing 4 KPI cards followed by 
a line chart and a data table
```

### Reference Styles
```
A landing page in the style of Stripe.com — clean, modern, with a 
gradient hero section, feature grid with icons, and a dark footer
```

### Specify Content
```
A SaaS pricing page with three tiers: Starter ($9/mo, 5 users), 
Professional ($29/mo, 25 users), Enterprise (custom, unlimited). 
The Professional tier should be highlighted as "Most Popular"
```

### For Marketing Teams
```
A product launch landing page for an AI analytics tool. Hero with 
headline "See What Your Data is Telling You", subheadline about 
real-time insights, a demo video placeholder, and three benefit 
sections with icons below
```

## Use Cases

| Need | Prompt Example |
|------|---------------|
| Landing page | "Product landing page for a sustainable fashion brand with hero image, value props, and email signup" |
| App screen | "Mobile app home screen for a fitness tracker showing today's stats, activity rings, and quick-start workout buttons" |
| Dashboard | "Admin dashboard for an e-commerce platform with revenue chart, recent orders table, and inventory alerts" |
| Email template | "Marketing email template for a product launch — header with logo, hero image, feature highlights, CTA button" |
| Pricing page | "Three-tier pricing page with comparison table, FAQ accordion, and enterprise contact form" |
| Onboarding | "3-step mobile onboarding flow: welcome → select interests → enable notifications" |

## Integration with Other Skills

- **brand-guidelines**: Reference brand colors, fonts, and tone before generating designs
  ```
  Read our brand guidelines in docs/marketing/brand-guidelines.md, 
  then design a landing page that matches our visual identity
  ```
- **campaign-planner**: Generate landing pages and ad visuals for campaigns
- **stakeholder-briefing**: Generate mockups to include in presentations
- **competitor-watch**: "Design a landing page that differentiates us from Competitor X's approach"

## Output Structure

Each generation creates:
```
{output-dir}/
  screen-1.html          # Full HTML + Tailwind CSS
  screen-1.png           # Screenshot of the design
  screen-1-metadata.json # Project ID, screen ID (for editing)
```

For flows:
```
{output-dir}/
  screen-1.html + .png + -metadata.json
  screen-2.html + .png + -metadata.json
  ...
```

## Limitations

- **HTML + Tailwind only** — no React, Vue, or SwiftUI export (convert manually if needed)
- **No animations** — static designs only, no hover effects or transitions
- **Max 5 screens** per flow
- **Max 5 variants** per request
- **Free tier**: 350 standard + 50 pro generations/month
- **Responsiveness** may need manual CSS adjustments for multiple breakpoints

## Troubleshooting

**"STITCH_API_KEY not set"**
- Add your API key to `.env`. Get it from stitch.withgoogle.com → Settings → API Key.

**"@google/stitch-sdk not found"**
- Run: `npm install @google/stitch-sdk`

**"Rate limit exceeded"**
- Free tier: 350 standard + 50 pro per month. Check your usage at stitch.withgoogle.com.

**"Generation returned no screens"**
- Try a more descriptive prompt — include layout, content, and style details.
- Check that the prompt doesn't violate content policies.

**MCP server not connecting**
- Verify `.claude/settings.local.json` has the correct MCP config.
- Check that `STITCH_API_KEY` is set in `.env`.
- Restart Claude Code after adding the MCP server.
