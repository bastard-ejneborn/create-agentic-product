#!/usr/bin/env node
/**
 * Google Stitch CLI — Generate UI designs from text prompts.
 * Uses the @google/stitch-sdk for programmatic access.
 *
 * Commands:
 *   generate  - Create a UI screen from a text prompt
 *   variants  - Generate multiple design alternatives
 *   edit      - Edit an existing screen
 *   html      - Extract HTML from a generated screen
 *   flow      - Create a multi-screen flow
 */

const fs = require("fs");
const path = require("path");

// Load .env
try {
  require("dotenv").config();
} catch {
  // dotenv is optional
}

let Stitch;
try {
  ({ Stitch } = require("@google/stitch-sdk"));
} catch {
  console.error("ERROR: @google/stitch-sdk not installed.");
  console.error("Run: npm install @google/stitch-sdk");
  process.exit(1);
}

const API_KEY = process.env.STITCH_API_KEY;
if (!API_KEY) {
  console.error("ERROR: STITCH_API_KEY not set.");
  console.error("Add to .env: STITCH_API_KEY=your-key");
  console.error("Get your key at: stitch.withgoogle.com → Settings → API Key");
  process.exit(1);
}

const DEVICE_MAP = {
  desktop: "DESKTOP",
  mobile: "MOBILE",
  tablet: "TABLET",
  agnostic: "AGNOSTIC",
};

function parseArgs() {
  const args = process.argv.slice(2);
  const command = args[0];
  const opts = {};

  for (let i = 1; i < args.length; i++) {
    const arg = args[i];
    if (arg === "--prompt" || arg === "-p") opts.prompt = args[++i];
    else if (arg === "--output" || arg === "-o") opts.output = args[++i];
    else if (arg === "--device" || arg === "-d") opts.device = args[++i];
    else if (arg === "--quality" || arg === "-q") opts.quality = args[++i];
    else if (arg === "--count" || arg === "-c") opts.count = parseInt(args[++i]);
    else if (arg === "--project") opts.project = args[++i];
    else if (arg === "--screen") opts.screen = args[++i];
  }

  return { command, ...opts };
}

async function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

async function saveScreen(screen, outputDir, index) {
  await ensureDir(outputDir);
  const prefix = `screen-${index + 1}`;

  // Save HTML
  try {
    const html = await screen.getHtml();
    const htmlPath = path.join(outputDir, `${prefix}.html`);
    fs.writeFileSync(htmlPath, html);
    console.log(`  HTML: ${htmlPath}`);
  } catch (e) {
    console.error(`  Warning: Could not get HTML — ${e.message}`);
  }

  // Save screenshot
  try {
    const imageUrl = await screen.getImage();
    if (imageUrl) {
      const resp = await fetch(imageUrl);
      const buffer = Buffer.from(await resp.arrayBuffer());
      const imgPath = path.join(outputDir, `${prefix}.png`);
      fs.writeFileSync(imgPath, buffer);
      console.log(`  Image: ${imgPath}`);
    }
  } catch (e) {
    console.error(`  Warning: Could not get image — ${e.message}`);
  }

  // Save metadata
  const metadata = {
    projectId: screen.projectId || null,
    screenId: screen.id || null,
    createdAt: new Date().toISOString(),
  };
  const metaPath = path.join(outputDir, `${prefix}-metadata.json`);
  fs.writeFileSync(metaPath, JSON.stringify(metadata, null, 2));

  return metadata;
}

async function cmdGenerate(opts) {
  if (!opts.prompt) {
    console.error("ERROR: --prompt is required.");
    process.exit(1);
  }

  const outputDir = opts.output || "assets/images/stitch-output";
  const device = DEVICE_MAP[opts.device || "desktop"] || "DESKTOP";

  console.log(`Generating UI design...`);
  console.log(`  Prompt: ${opts.prompt.substring(0, 100)}...`);
  console.log(`  Device: ${device}`);
  console.log(`  Quality: ${opts.quality || "standard"}`);

  const stitch = new Stitch({ apiKey: API_KEY });
  const project = await stitch.createProject();

  const generateOpts = { device };
  if (opts.quality === "pro") {
    generateOpts.model = "gemini-2.5-pro";
  }

  const screens = await project.generate(opts.prompt, generateOpts);

  if (!screens || screens.length === 0) {
    console.error("ERROR: No screens generated. Try a more descriptive prompt.");
    process.exit(1);
  }

  console.log(`\nGenerated ${screens.length} screen(s):`);
  for (let i = 0; i < screens.length; i++) {
    console.log(`\n  Screen ${i + 1}:`);
    await saveScreen(screens[i], outputDir, i);
  }

  console.log(`\nSUCCESS: Output saved to ${outputDir}`);
}

async function cmdVariants(opts) {
  if (!opts.prompt) {
    console.error("ERROR: --prompt is required.");
    process.exit(1);
  }

  const outputDir = opts.output || "assets/images/stitch-variants";
  const count = Math.min(opts.count || 3, 5);

  console.log(`Generating ${count} design variants...`);
  console.log(`  Prompt: ${opts.prompt.substring(0, 100)}...`);

  const stitch = new Stitch({ apiKey: API_KEY });
  const project = await stitch.createProject();

  const screens = await project.generate(opts.prompt, {
    device: DEVICE_MAP[opts.device || "desktop"] || "DESKTOP",
  });

  if (!screens || screens.length === 0) {
    console.error("ERROR: No screens generated.");
    process.exit(1);
  }

  // Generate variants from the first screen
  const variants = await screens[0].variants(count);

  console.log(`\nGenerated ${variants.length} variant(s):`);
  for (let i = 0; i < variants.length; i++) {
    console.log(`\n  Variant ${i + 1}:`);
    await saveScreen(variants[i], outputDir, i);
  }

  console.log(`\nSUCCESS: Variants saved to ${outputDir}`);
}

async function cmdEdit(opts) {
  if (!opts.project || !opts.screen) {
    console.error("ERROR: --project and --screen are required.");
    process.exit(1);
  }
  if (!opts.prompt) {
    console.error("ERROR: --prompt is required (the edit instruction).");
    process.exit(1);
  }

  console.log(`Editing screen ${opts.screen}...`);
  console.log(`  Edit: ${opts.prompt.substring(0, 100)}...`);

  const stitch = new Stitch({ apiKey: API_KEY });
  const project = await stitch.getProject(opts.project);
  const screen = await project.getScreen(opts.screen);

  const edited = await screen.edit(opts.prompt);

  const outputDir = opts.output || "assets/images/stitch-edited";
  console.log(`\n  Edited screen:`);
  await saveScreen(edited, outputDir, 0);

  console.log(`\nSUCCESS: Edited screen saved to ${outputDir}`);
}

async function cmdHtml(opts) {
  if (!opts.project || !opts.screen) {
    console.error("ERROR: --project and --screen are required.");
    process.exit(1);
  }

  const stitch = new Stitch({ apiKey: API_KEY });
  const project = await stitch.getProject(opts.project);
  const screen = await project.getScreen(opts.screen);

  const html = await screen.getHtml();

  if (opts.output) {
    await ensureDir(path.dirname(opts.output));
    fs.writeFileSync(opts.output, html);
    console.log(`SUCCESS: HTML saved to ${opts.output}`);
  } else {
    process.stdout.write(html);
  }
}

async function cmdFlow(opts) {
  if (!opts.prompt) {
    console.error("ERROR: --prompt is required.");
    process.exit(1);
  }

  const outputDir = opts.output || "assets/images/stitch-flow";
  const device = DEVICE_MAP[opts.device || "desktop"] || "DESKTOP";

  console.log(`Generating multi-screen flow...`);
  console.log(`  Prompt: ${opts.prompt.substring(0, 100)}...`);
  console.log(`  Device: ${device}`);

  const stitch = new Stitch({ apiKey: API_KEY });
  const project = await stitch.createProject();

  // Generate flow — Stitch interprets multi-screen prompts automatically
  const screens = await project.generate(opts.prompt, { device });

  if (!screens || screens.length === 0) {
    console.error("ERROR: No screens generated.");
    process.exit(1);
  }

  console.log(`\nGenerated ${screens.length} screen(s) in flow:`);
  for (let i = 0; i < screens.length; i++) {
    console.log(`\n  Screen ${i + 1}:`);
    await saveScreen(screens[i], outputDir, i);
  }

  console.log(`\nSUCCESS: Flow saved to ${outputDir}`);
}

async function main() {
  const opts = parseArgs();

  switch (opts.command) {
    case "generate":
      await cmdGenerate(opts);
      break;
    case "variants":
      await cmdVariants(opts);
      break;
    case "edit":
      await cmdEdit(opts);
      break;
    case "html":
      await cmdHtml(opts);
      break;
    case "flow":
      await cmdFlow(opts);
      break;
    default:
      console.log("Google Stitch CLI — AI UI Design Generator\n");
      console.log("Commands:");
      console.log("  generate   Create a UI screen from a text prompt");
      console.log("  variants   Generate multiple design alternatives");
      console.log("  edit       Edit an existing screen");
      console.log("  html       Extract HTML from a generated screen");
      console.log("  flow       Create a multi-screen flow\n");
      console.log("Examples:");
      console.log('  node stitch.js generate -p "A SaaS pricing page" -d desktop -o assets/images/pricing');
      console.log('  node stitch.js variants -p "Hero section for fintech" -c 3 -o assets/images/hero');
      console.log('  node stitch.js flow -p "Checkout: cart → shipping → payment" -d mobile\n');
      console.log("Environment:");
      console.log("  STITCH_API_KEY  Your Google Stitch API key (required)");
      process.exit(opts.command ? 1 : 0);
  }
}

main().catch((e) => {
  console.error(`ERROR: ${e.message}`);
  process.exit(1);
});
