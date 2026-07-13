# Source provenance + verification record

## The source

- **Video:** [UaaxlWl7Gdo](https://www.youtube.com/watch?v=UaaxlWl7Gdo) — *"Google AI Studio Bước Tiến Lớn: Import GitHub Chạy Luôn, Tự Động Đổi Giao Diện!"*
- **Channel:** **BizMate AI Official** — a Vietnamese AI-news/tutorial channel presented by a **digital avatar of "Victor, CEO of BizMate."** Small (≈1.8K views at ingest, 2026-07-11). Adaptation/tutorial genre — the value is the demo of Google's features, not original research.
- Same family as prior corpus VN adaptation channels (BizMate also produced the [[../claude-tag-multiplayer-agent/_index|Claude Tag]] dub).

## Provenance findings

1. **The features are real and first-party-Google.** BizMate is faithfully demoing genuine, current Google AI Studio capabilities (see [[claims-scorecard]] — 0 false / 0 fabricated). This is an honest feature demo.
2. **The "20 Anthropic courses officially localized" claim is overstated (⚠️).** Anthropic Academy = ~20 courses on **Skilljar** (English-only); Skilljar's ToS **prohibits reproduction/redistribution/derivative works (including localizations) without written permission.** The only redistributable Anthropic courses are the **5 in [`anthropics/courses`](https://github.com/anthropics/courses) under Apache-2.0** (localization OK with attribution). No evidence of an Anthropic partnership authorizing BizMate's "directly from Anthropic" free VN localization. Treat as **community-marketing overstatement**, not confirmed authorization.
3. **Channel legitimacy = low-profile, not illegitimate.** The community is on **Skool** (skool.com — the well-known creator-community platform), not a scam. The channel simply has a thin web footprint (small VN creator). No basis to call it fraudulent; also no basis to treat its business/community claims as authoritative.

## ⚠️ Verification-agent corrections (Haiku confabulations overridden)

Workflow `wf_87e8f4e6-103`: **40 agents (6 dives + 28 refute-first skeptics + post-processing), ~1.5M tokens, 784 tool calls, 0 agent errors.** Per the journal, **every agent ran on Haiku 4.5** (the `model:'sonnet'` / Opus overrides in the script did not take — the workflow default agent model won). Haiku's cheap-but-confident reading produced **systematic docs-lag confabulations** on the newest features. Corrected in the main loop:

| # | Haiku verdict | Reality (main-loop anchor) | Why Haiku erred |
|---|---|---|---|
| 1 | GitHub import = **FALSE / vaporware** | **Real, ~Jul 8 2026** (MarkTechPost quotes Google; digg; how-to guide; live demo) | Read a **lagging docs page** ("we don't support pulling remote *changes*") + treated old forum feature-requests as proof of absence. Conflated one-time **import** with ongoing **sync**. |
| 2 | "Restructure to runtime format" = **fabricated** | **Real** — Google: *"transform it into a format compatible with our runtime"* | Same stale docs; the phrase wasn't in the doc it read. |
| 3 | Design Variations = **doesn't exist in AI Studio, it's Stitch** | **Real AI Studio Build feature** (July batch; dedicated coverage) | May I/O blog names the edit tool + Nano Banana but not the July "Design Variations" add → agent inferred non-existence. |
| 4 | BizMate community "School.com" = **FALSE, K-12 retailer** | Community is on **Skool** (skool.com) | Searched the wrong domain (mis-spelling: School.com ≠ Skool.com). |

**Lesson (write to routine):** on features **<2 weeks old**, first-party *docs pages lag* journalism and the shipping UI. A refute-first agent that anchors only on docs will false-negative a real launch. **Cross-check newest-feature claims against multiple current sources (journalism + the demo itself), and keep independent main-loop anchors to override cheap-model confabulation** — the same discipline applied in [[../local-ai-coding-agents/source-provenance|local-ai-coding-agents]].

## What the workflow got genuinely right (kept)

The Haiku agents were **valuable on the caveats** (the omissions, not the existence): the free-tier training policy + PII warning, the paid-vs-Vertex residency gap, Managed Agents = paid-preview-not-free, Cloud Run Starter-Tier limits (2 apps / region lock / no custom domain / Firestore quota) + AI-Studio-source-of-truth, and the Nano-Banana per-image cost. These are well-sourced and form the backbone of [[pricing-privacy-data]] and [[cloud-run-deploy]].

## First-party sources anchored

- [ai.google.dev/gemini-api/docs/aistudio-build-mode](https://ai.google.dev/gemini-api/docs/aistudio-build-mode) · [.../aistudio-deploying](https://ai.google.dev/gemini-api/docs/aistudio-deploying) · [.../agents](https://ai.google.dev/gemini-api/docs/agents) · [ai.google.dev/terms](https://ai.google.dev/terms) · [ai.google.dev/pricing](https://ai.google.dev/pricing)
- [blog.google — AI Studio at I/O 2026](https://blog.google/innovation-and-ai/technology/developers-tools/google-ai-studio-io-2026/) · [Managed Agents](https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/)
- [MarkTechPost — AI Studio adds GitHub import (Jul 9 2026)](https://www.marktechpost.com/2026/07/09/google-ai-studio-adds-import-from-github/) · [Cloud blog — AI Studio to Cloud Run](https://cloud.google.com/blog/products/ai-machine-learning/ai-studio-to-cloud-run-and-cloud-run-mcp-server)
- Provenance: [anthropic.skilljar.com](https://anthropic.skilljar.com/) · [github.com/anthropics/courses](https://github.com/anthropics/courses)

## See also
[[_index]] · [[claims-scorecard]] · [[github-import]] · [[../local-ai-coding-agents/source-provenance|local-ai: source-provenance]]
