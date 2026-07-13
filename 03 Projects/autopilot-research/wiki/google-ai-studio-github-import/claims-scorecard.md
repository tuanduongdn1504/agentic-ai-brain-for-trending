# Claims scorecard — all 11 claims graded

> Reconciled in the main loop from the [[source-provenance|40-agent workflow]] + independent anchors. **All agents ran on Haiku 4.5** and produced docs-lag confabulations on the newest features; where that happened, the **main-loop anchor wins** (marked ⟲ override).
> **Legend:** ✅ CONFIRMED · ◐ CORRECT-BUT-INCOMPLETE · ⚠️ MISLEADING/OMISSION · ❌ FALSE/FABRICATED

| # | Claim (paraphrased) | Grade | One-line verdict |
|---|---|---|---|
| C1 | Import a GitHub repo directly into AI Studio Build; auto-pulls + runs, no config/terminal/editor | ✅ ⟲ | Real, launched **~Jul 8 2026** (MarkTechPost quotes Google + live demo). Haiku called it FALSE off a lagging docs page — **overridden**. [[github-import]] |
| C2 | Must fork someone else's repo to your account first | ◐ | Practically true (need write access to import + push back); not a hard rule for repos you own. |
| C3 | Auto-detects framework (Next.js), configures runtime, installs deps, **restructures to runtime format** | ✅ ⟲ | Google's words: *"transform it into a format compatible with our runtime."* Haiku called restructure "fabricated" — **overridden**. Caveat: exact mechanics undisclosed; **no round-trip sync**. |
| C4 | Rebrand via prompt: keep layout, change content; motion cards survived, no code touched | ◐ | Prompt-editing real; structure/animation preservation on real components **not guaranteed** — demo happy-path. [[design-variations]] |
| C5 | Design Variations: auto-generate styles in seconds; annotate a region; "YouTube-style"; preview before apply | ◐ ⟲ | Real AI Studio Build feature + annotate tool (Google's blog). Haiku deflected it to "Stitch/doesn't exist" — **overridden**. Prompt-driven (no template library); fidelity-on-existing-components unverified. |
| C6 | Publish → deploy A-Z to Cloud Run, no terminal, auto-configures keys/access | ✅ | Real + key stays server-side. **Omits:** Starter Tier 2-app/region-lock/no-custom-domain, ~$50-200/mo real cost, AI-Studio-source-of-truth, no container export. [[cloud-run-deploy]] |
| C7 | Managed Agents API "just arrived in the **free tier**"; agents auto-write code/images/video | ⚠️ | It's **paid public preview** — only sandbox *compute* free during preview; inference billed. Code native; image/video via separate APIs. Preview **forbids PII**. [[managed-agents]] |
| C8 | (implied) AI Studio is free | ⚠️ | Unpaid tier **trains on you + human-review**; ToS forbids PII on Unpaid Services. Billing-attached = paid/no-training; **no residency even paid**. [[pricing-privacy-data]] |
| C9 | Whole flow with no code editor + no terminal | ✅ | True for the vibe-coding/prototype path. "No code" ≠ production-ready. |
| C10 | Community: 20 Anthropic courses "officially Vietnamese-localized," free on Skool | ⚠️ | Anthropic Academy = ~20 courses (Skilljar, English-only, ToS **forbids** redistribution/localization); only 5 GitHub `anthropics/courses` (Apache-2.0) are redistributable. "Directly from Anthropic" authorization not evidenced. [[source-provenance]] |
| C11 | These are "July 2026" features | ◐ | GitHub import + Design Variations = genuinely new (~Jul 8). The rest (Android/Workspace/Antigravity export/Nano Banana/edit tool) = **I/O 2026 (May 19)**. |

## Tally (reconciled)

- ✅ CONFIRMED: **4** (C1, C3, C6, C9)
- ◐ CORRECT-BUT-INCOMPLETE: **4** (C2, C4, C5, C11)
- ⚠️ MISLEADING / OMISSION: **3** (C7, C8, C10)
- ❌ FALSE / FABRICATED: **0**
- **⟲ main-loop overrides of Haiku confabulation: 3** (C1, C3, C5) + 1 provenance (Skool≠School.com)

## Reading of the video

**Real tools, omitted caveats.** Every feature demonstrated is genuine, current, and works on screen — this is a legitimate hands-on demo, not vaporware and not fabrication (0 false / 0 fabricated). The failure mode is **omission**: it never mentions the training policy, the absence of data residency, the cost beyond free, the one-way sync, or the lock-in — precisely the things a regulated SaaS operator must know. Plus one **overstated community-marketing claim** (the "Anthropic courses," C10) and one **misleading teaser** (Managed Agents "free tier," C7).

**Genre placement:** more honest than the [[../jasonlee-claude-mobile-app/_index|Jason Lee "$80K/Mo"]] video (which fabricated the business), less rigorous than [[../local-ai-coding-agents/claims-scorecard|Code with Beto's local-AI video]] (which actively hedged its own claims). A useful teaching example of *"demo shows the magic, hides the compliance bill."*

## See also
[[_index]] · [[source-provenance]] · [[overview]] · [[pricing-privacy-data]]
