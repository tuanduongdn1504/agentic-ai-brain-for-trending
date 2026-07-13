# Overview — the demo, corrected

## Source
Video [UaaxlWl7Gdo](https://www.youtube.com/watch?v=UaaxlWl7Gdo) (BizMate AI, VN). Raw transcript: [../../raw/2026-07-13-google-ai-studio-github-import.md](../../raw/2026-07-13-google-ai-studio-github-import.md).

## What the presenter demonstrates (in order)

1. **New App → Build → Add files → Import from GitHub.** Link your GitHub account, pick a repo. He forks a nice-looking agency-website repo to his account first ("BMAT Award Web"), then imports it.
2. **Auto-build.** AI Studio "restructures the code to its runtime format," auto-detects the framework (**Next.js**), picks the package manager (**npm**), installs dependencies, adds missing components, and produces a live **Preview** — "no terminal, no config, no code editor."
3. **Rebrand via prompt.** He prompts: *keep the layout/structure, change the copy + branding to mine.* The content changes; he claims the motion/animation cards survive.
4. **Design Variations.** An edit/annotate tool lets him mark a region and generate multiple UI variants (fonts, themes, colors); he types *"change to YouTube-style theme"* and previews variants before applying.
5. **Publish → Cloud Run.** One click → *Publish your app* → connects his linked Google Cloud project → auto-configures API keys/access → the app is live on a public URL, visible as a Cloud Run service.
6. **Teaser.** Mentions **Managed Agents API** "arriving in the free tier" with "4 updates" — an "agent orchestration framework" — deferred to a future video.

## What's true vs what's omitted (the 30-second read)

- **Every feature is real and current.** GitHub import shipped ~**July 8 2026**; Design Variations + Cloud Run deploy + Managed Agents are all real. The demo is a legitimate screen recording of working Google features. See [[claims-scorecard]].
- **The demo's failure mode is OMISSION, not fabrication.** It never mentions:
  - the free tier **trains on your inputs** and forbids PII ([[pricing-privacy-data]]);
  - there is **no round-trip GitHub sync** — import is a one-time snapshot ([[github-import]]);
  - **cost beyond free** and **region lock / no custom domain** on Cloud Run Starter Tier ([[cloud-run-deploy]]);
  - Managed Agents is **paid preview**, not "free tier" ([[managed-agents]]).
- **Two claims are overstated:** the community's "20 Anthropic courses officially localized" ([[source-provenance]]) and Managed Agents "in the free tier."

## The honest framing for an operator

AI Studio Build is a **fast, real prototyping surface** — point it at a repo, explore designs, deploy a demo in minutes. It is **not** a production path for a codebase with a strict constitution and PII: the training policy, the absence of data-residency guarantees, the one-way sync, and the "AI-Studio-is-source-of-truth" deploy model all fight [[../../CLAUDE|hireui's rules]]. Treat it as a **sketchpad**, harvest ideas/patterns, build the real thing under your own harness. See the [pilot menu](../../output/(C)%202026-07-13-google-ai-studio-pilot-menu.md).

## See also
[[_index]] · [[github-import]] · [[claims-scorecard]] · [[pricing-privacy-data]]
