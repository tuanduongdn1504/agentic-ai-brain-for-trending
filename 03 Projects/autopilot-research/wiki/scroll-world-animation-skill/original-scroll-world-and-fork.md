# Original: Scroll World (oso95) + Chase AI's fork (cth9191)

## Source

`gh api repos/oso95/scroll-world` + `gh api repos/cth9191/scroll-world` (both fetched directly, 2026-07-14) + Workflow `wf_885d81d7-1a2` dives `scrollworld-original` / `scrollworld-fork` (README + FORK-CHANGES.md + commit-history reads).

## The original: `oso95/scroll-world`

- **Repo confirmed real** via direct GitHub API call: created 2026-07-06, MIT license, JavaScript, **1,552 stars**, 204 forks, 1 open issue, actively pushed as recently as 2026-07-10.
- **GitHub description (verbatim):** "A skill that turn any brand into a scrollable 3D world."
- **Author identity — do NOT repeat the video's name uncorrected.** The video's spoken audio credits the skill to "Peter Wing" (0:55) and later "Peter Wang" (9:19) — two different renderings in the same video. The GitHub API's own `name` field for the account is **`cyw`**, not either of those. Full profile: login `oso95`, bio *"Founder & CTO @hermai-ai"*, blog `hermai.ai`, X/Twitter handle `@the_cyw`. A direct fetch of the X profile returned an HTTP 402 (paywalled), so the display name there could not be independently confirmed either. **Verdict: the creator's verified identity is "cyw" / Hermai AI; "Peter Wang"/"Peter Wing" is an unconfirmed attribution and should be treated as such, not asserted as fact.**
- **Mechanism, as described in the repo (confirmed by the dive agent's README read):**
  1. Higgsfield (via GPT Image 2) generates a static scene image per "scene."
  2. Higgsfield (via Seedance) turns that image into a short "camera flight" video — the camera flies from outside the scene into its interior.
  3. FFmpeg/ffprobe extracts the video's individual frames.
  4. A portable, vanilla-JavaScript "scrub engine" binds the user's scroll position on the page to a specific frame/timestamp in that extracted sequence — scrolling plays the pre-rendered video frame-by-frame instead of a real-time video decode.
  5. "Connector" transitions bridge one scene's video to the next so the flight reads as one continuous, cut-free journey rather than a slideshow of separate clips.
- **Distribution:** ships as a Claude Code Skill (`SKILL.md`, installable via `/plugin marketplace add oso95/scroll-world`) and is also listed as installable for Codex and other skill-compatible agents via the third-party Vercel `skills` CLI (`npx skills add oso95/scroll-world`) — this specific install command comes from the dive agent's README read and was not independently re-fetched by the main loop; treat the *existence* of cross-agent support as confirmed (the repo is genuinely agent-agnostic JS + a skill wrapper) but the *exact command syntax* as agent-reported, not double-checked.
- Higgsfield is a hard dependency of the original repo, not something Chase added.

## Chase AI's fork: `cth9191/scroll-world`

- **Repo confirmed real and confirmed-as-fork** via direct GitHub API call: `"fork": true`, `"parent"` and `"source"` both point to `oso95/scroll-world`. Created 2026-07-09 — **3 days after** the original repo and **2 days before** this video was uploaded (2026-07-11), which matches the presenter's "brand new" framing of his own fork. MIT license, JavaScript, 271 stars, 41 forks.
- **GitHub description (verbatim):** "Claude Code skill/plugin: immersive scroll-scrubbed 'fly through the world' landing pages generated with Higgsfield (Emons-style diorama flights, seamless connectors, portable scrub engine)."
- **The video claims three specific improvements over the original.** A dive agent read the fork's `FORK-CHANGES.md` + commit history and a second agent adversarially verified it; both independently returned **CONFIRMED** on all three, and the level of detail (matching the presenter's *exact* spoken vocabulary — "crop-safe," "full portrait chain," "budget tiers" — rather than generic paraphrase) is a good corroboration signal:
  - **Budget tiers:** three named tiers — **Lean** (~8 generations / 4 scenes), **Standard** (~11–14 generations), **Showcase** (17+ generations, matching the original's un-tiered default of ~17 generations for a 6-scene site) — plus a spend-estimate-and-approval gate shown before any paid generation runs.
  - **Mobile:** four tiers — crop-safe / mobile encodes / hero reframe / full portrait chain — plus device-class clipping for screens ≤600px CSS short-side, an iOS Low Power Mode fallback (auto-switches to stills-with-crossfades), and a data-saver mode.
  - **SEO:** a `data-sw-seo` static copy block — crawlable headings and text that are hidden after the page mounts (so search crawlers see real text, human visitors see the animated scenes).
- These three additions are the only fork-specific claims the video makes; nothing else in the video is attributed to Chase's engineering rather than the original.

## What this means for reading the video

The "skill" the video demos is genuinely two layers: an open-source mechanism (frame-scrubbed AI video → scrollytelling site) invented by a third party whose real name isn't confirmed by any first-party profile, plus a real, dated, verifiable fork adding cost/mobile/SEO controls. Both repos are real, both are MIT-licensed, and the fork's added value is concrete and independently checkable — the identity confusion is the only soft spot, and it's a caption/spoken-audio problem, not a fabrication about the tooling itself.

## Cross-links

[[scroll-world-animation-skill/_index]] · [[scroll-world-animation-skill/original-higgsfield-platform]] · [[claude-code-plugins-stack/_index]] (same creator, prior video) · [[ai-web-design-workflow/_index]] (sibling "AI-generated design asset → coding-agent skill" pattern)
