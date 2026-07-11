# Claude Design 2.0 and the Design→Code Handoff

## Verdict on the video's claim
"Claude Design got a massive upgrade recently — left-side edit controls, export zip, designs both web and iOS" → **CORRECT-BUT-INCOMPLETE** (high confidence).

## What Claude Design is (first-party, as of 2026-07-11)
- Anthropic beta product at **claude.ai/design**; included in **Pro, Max, Team, Enterprise** plans; usage **shares rate limits** with Claude chat, Cowork, and Claude Code (claude.com/product/design).
- Creates prototypes, wireframes, mockups, decks, marketing collateral; **design-system import** from GitHub repos, design files, or local codebases.
- Launched via Anthropic Labs **2026-04-17** (verified in the corpus' open-design pass, then powered by Opus 4.7); the current product page no longer states launch date or model.
- Bidirectional Claude Code integration: **`/design-sync`** (pull design systems) and **`/design`** commands.

## The "massive upgrade" = 2026-06-17 overhaul (verified)
- Confirmed by VentureBeat ("design system imports, code round-trips, and a fix for its token-burning problem"), Engadget, Fast Company, and Anthropic support docs; Jason Lee's own reaction video "Anthropic just dropped Claude Design 2.0" is 2026-06-30 (`jQOSIPgGqY0`).
- **WYSIWYG canvas editing**: click, drag, resize, reorder, align elements directly; adjustment sliders for spacing/color — exactly the "don't waste tokens re-prompting" feature the video demonstrates with the color tweak.
- **Geography correction**: chat is on the LEFT; the editable canvas + property inspector are on the RIGHT. The video says "left side" — minor error.
- **Export**: `.zip`, PDF, PPTX, standalone HTML via project menu → Export (support.claude.com article 14604416) — the video's zip flow is real and documented.

## Scope correction: "iOS app design" ≠ native iOS
- Claude Design outputs **responsive web designs** (mobile/tablet/desktop breakpoints). The "Track Rabbit iOS app" the video selects from a dropdown is a **mobile-shaped responsive mockup**, not a native iOS artifact.
- The actual iOS app is built by **Claude Code** (Expo React Native) *from* those mockups. Two tools, two scopes: Claude Design = UI mockups; Claude Code = the running app. The video elides this, which matters if you expect the exported zip to contain React Native components — it doesn't.

## Corpus context
- Claude Design's existence and lineage were verified in [[external|Storm Bear: open-design]] (2026-07-01 pass), which also mapped the OSS alternative (nexu-io/open-design, BYOA + DESIGN.md). This video is the corpus' first sighting of the **post-June-17 editor** in a real workflow.
- Design-quality gating (anti-slop checklists) lives in [[external|Storm Bear: ai-web-design-workflow]] — composable with this pipeline: generate in Claude Design, gate with Taste-Skill-style checks.

## Key Takeaways
- The reference-image + creative-freedom prompt pattern produced a coherent 2-surface design in one pass — the strongest tool demo in the video.
- Manual canvas edits for pixel tweaks, prompts only for structural changes: that's the post-June-17 token economy.
- Expect **HTML/responsive mockups** out of the zip; budget Claude Code time to translate to React Native.
- Plan-gated: Claude Design consumes the same rate limits as your Claude Code work — heavy design iteration competes with build capacity.

## Sources
- https://claude.com/product/design · https://support.claude.com/en/articles/14604416-get-started-with-claude-design · https://venturebeat.com/technology/anthropic-ships-major-claude-design-overhaul-with-design-system-imports-code-round-trips-and-a-fix-for-its-token-burning-problem · https://www.engadget.com/2196329/anthropics-design-assistant-now-works-better-with-its-coding-agent/ · https://www.fastcompany.com/91561193/anthropics-updated-claude-design-gives-vibe-coders-and-their-design-overlords-more-control · https://docs.expo.dev/agents/claude/
