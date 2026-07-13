# google-ai-studio-github-import

> **Topic:** The July-2026 "Build glow-up" in **Google AI Studio** — import a GitHub repo and run it with no setup, auto-generate **Design Variations** of the UI, and one-click **deploy to Cloud Run** — plus the teased **Managed Agents API**. What's real, what the demo omits, and where a Next.js recruitment SaaS can (and can't) touch it.
> **Compiled:** 2026-07-13 from a single operator-submitted YouTube video (path 5, yt-dlp-only, full transcript read in the main loop) + a double-dive into the FIRST-PARTY Google originals beneath every feature.
> **Source video:** [UaaxlWl7Gdo](https://www.youtube.com/watch?v=UaaxlWl7Gdo) — **BizMate AI Official** (VN adaptation/tutorial channel; "avatar of Victor, CEO of BizMate"), *"Google AI Studio Bước Tiến Lớn: Import GitHub Chạy Luôn, Tự Động Đổi Giao Diện!"* (2026-07-11, 13:51, ~1.8K views at ingest).
> **Raw:** [../../raw/2026-07-13-google-ai-studio-github-import.md](../../raw/2026-07-13-google-ai-studio-github-import.md)
> **Verification:** Workflow `wf_87e8f4e6-103` — 40 agents (6 first-party dives + 28 refute-first skeptics), ~1.5M tokens, 784 tool calls. **All agents ran on Haiku 4.5** and produced several **docs-lag confabulations** (they trusted a lagging docs page over a 6-day-old feature). Those were **overridden with independent main-loop anchors** (fresh journalism + the live on-screen demo). See [[source-provenance]] for every override.

---

## The one-sentence thesis

Google AI Studio's **Build** mode is now a genuinely capable *prototyping* surface — **GitHub import** (real, shipped ~July 8 2026), **one-click Design Variations**, **Nano Banana** asset generation, and **one-click deploy to Cloud Run** — and every feature the video shows is real and works. But the demo **omits the entire enterprise story**: the free tier **trains on your inputs** and forbids PII, there's **no guaranteed data residency** (only Vertex AI enterprise), there's **no round-trip GitHub sync**, and AI Studio is the **source of truth** (Cloud Run edits are lost on redeploy). For **hireui** that makes AI Studio a **prototyping-only tool, never a production path** — the extractable value is *design exploration* and a *deploy-layer datapoint*, not shipping candidate-facing code.

## What actually shipped (feature table)

| Feature | Real? | The catch the video skipped | Article |
|---|---|---|---|
| **GitHub import → Build** | ✅ Real (~Jul 8 2026) | One-time import *snapshot*; **no round-trip sync** ("we don't support pulling remote changes") | [[github-import]] |
| **Design Variations + annotate + Nano Banana** | ✅ Real | Prompt-driven (not a template library); fidelity on *existing* animated components unverified; Nano Banana is **paid** per-image | [[design-variations]] |
| **Publish → Cloud Run** | ✅ Real | Starter Tier = **2 apps, region-locked, no custom domain**; real prod cost ~$50-200/mo; **no container export** | [[cloud-run-deploy]] |
| **Managed Agents API** | ✅ Real (preview) | **NOT "free tier"** — paid public preview, only sandbox *compute* free; **preview forbids PII** | [[managed-agents]] |
| **"It's free" (implied)** | ⚠️ Misleading | Unpaid tier **trains on you + human-reviews**; ToS: *"do not submit personal information to the Unpaid Services"* | [[pricing-privacy-data]] |

## Articles in this topic

- [[overview]] — the demo walkthrough, corrected step-by-step
- [[github-import]] — the headline feature: what it does, the docs-lag correction, the one-way-sync limit
- [[design-variations]] — Design Variations + Annotation Mode + Nano Banana; the code-fidelity risk
- [[cloud-run-deploy]] — Publish → Cloud Run: tiers, real cost, region lock, lock-in
- [[managed-agents]] — Managed Agents / Interactions API / the Antigravity agent; the "free tier" pin
- [[pricing-privacy-data]] — **the decisive hireui section**: training, ToS, residency, the safe boundary
- [[source-provenance]] — BizMate provenance, the "20 Anthropic courses" claim, and the Haiku-override record
- [[claims-scorecard]] — all 11 video claims graded (0 false / 0 fabricated; failure mode = omission)

## Pilot menu (apply it to real work)

The operator-facing **"many methods to apply this to my workflow"** deliverable lives in **[../../output/(C) 2026-07-13-google-ai-studio-pilot-menu.md](../../output/(C)%202026-07-13-google-ai-studio-pilot-menu.md)** — 11 ranked methods across 4 tiers (try-it-this-week → deploy-layer eval → Managed-Agents watch → governance fences). Headliner: **A2 Design-Variations on a *sanitized* Candidate-Detail clone** (feeds the active refactor spike) + **D1 the AI-Studio fence ADR** (so juniors don't follow the video literally into a PII/lock-in trap).

## Why this matters for Storm Bear

- **Goal #2 (ship hireui):** a concrete deploy-layer datapoint (one-click Cloud Run vs the [[../fullstack-docker-cicd/_index|fullstack-docker-cicd]] SSH path) + a reference for the **keys-never-client** pattern.
- **Data-residency thread:** this is the mirror image of [[../local-ai-coding-agents/privacy-data-residency|local-ai]] — where local inference = *strongest* residency, AI Studio free tier = *weakest* (trains + no residency). Same lens, opposite pole.
- **Harness portability thread:** Google's Managed Agents use the **same AGENTS.md / SKILL.md** declarative format as Anthropic Skills and [[../google-antigravity-skills/anthropic-agent-skills-portability|Antigravity Skills]] — reinforcing "author harness rules once, stay portable."

## Cross-links to existing corpus

- [[../google-antigravity-skills/_index|google-antigravity-skills]] — the **Antigravity agent** that powers Managed Agents is the same harness; AGENTS.md/SKILL.md convergence
- [[../fullstack-docker-cicd/_index|fullstack-docker-cicd]] — the deploy-layer bake-off partner (managed Cloud Run vs self-hosted SSH)
- [[../ai-web-design-workflow/_index|ai-web-design-workflow]] — Design Variations is a sibling of the Taste-Skill anti-slop gate for the hireui frontend
- [[../mosh-ai-powered-apps/_index|mosh-ai-powered-apps]] — the vendor seam Managed Agents would slot behind as one provider
- [[../miai-cv-matching-agent/_index|miai-cv-matching-agent]] — the Match-Explain feature Managed Agents is a candidate provider for
- [[../local-ai-coding-agents/privacy-data-residency|local-ai-coding-agents: data residency]] — the opposite pole of the residency spectrum
- [[../jasonlee-claude-mobile-app/_index|jasonlee-claude-mobile-app]] — same genre (revenue/hype demo of real tools); the keys-never-client ADR
