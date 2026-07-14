# Video-to-original crosswalk

Every concrete claim in the video, mapped to its verified original and a verdict. Verdicts use this corpus's house vocabulary: CONFIRMED / CORRECT-BUT-INCOMPLETE / MISLEADING / FALSE / FABRICATED / UNVERIFIABLE.

| # | Video claim | Verified original | Verdict |
|---|---|---|---|
| 1 | "Scroll World" is an open-source skill, credited to its original creator, found on Twitter | `oso95/scroll-world`, real, MIT, 1,552★ | CONFIRMED (repo) / **UNVERIFIABLE** (creator's real name — GitHub lists "cyw," not "Peter Wang/Wing") |
| 2 | The skill works by: single image → AI video → FFmpeg frame extraction → frames bound to scroll position → scenes stitched with connectors | Confirmed from `oso95/scroll-world`'s own README | CONFIRMED |
| 3 | Chase forked it and added budget tiers, mobile improvements, and SEO improvements | `cth9191/scroll-world`, real fork (GitHub API `fork:true`, parent confirmed), `FORK-CHANGES.md` documents all three specifically | CONFIRMED |
| 4 | Generation happens through "the Higgs Field MCP," usable from both Claude Code and Codex, "never have to leave the terminal" | Higgsfield MCP server real, confirmed via direct fetch of `higgsfield.ai/mcp`; explicitly supports Claude Code/Codex/OpenClaw/Hermes | CONFIRMED |
| 5 | Images come from "GPT image 2," videos from "Seed Dance" | Both confirmed as real models explicitly listed on Higgsfield's own MCP page | CONFIRMED |
| 6 | Connecting the tools is "copy the URL... do the authentication process" | Real flow, but the *exact* mechanism is Settings→Connectors (a UI flow), not a documented slash-command; a separate CLI path exists for terminal agents | CORRECT-BUT-INCOMPLETE |
| 7 | The six-scene reference example "cost me about 800" Higgsfield credits | Higgsfield's credits system is real; exact per-generation costs and this specific figure could not be independently confirmed (pricing page did not render for direct fetch) | UNVERIFIABLE |
| 8 | Demoing "the brand new GPT-5.6 Sol" inside Codex | GPT-5.6 Sol/Terra/Luna real, GA 2026-07-09, 2 days before upload — genuinely brand new | CONFIRMED |
| 9 | Codex/GPT-5.6 "has image generation" natively, so Higgsfield only needs to be called for video; Claude Code has no image generation, so Higgsfield carries the full load there | Consistent with Codex's native multimodal image generation and Claude Code's text/tool-only interface; not independently re-verified line-by-line but architecturally plausible and uncontested by any source found | CORRECT-BUT-INCOMPLETE (plausible, not independently re-confirmed) |
| 10 | "This entire website was one-shot by Claude Fable 5 in a single skill" | Claude Fable 5 real, launched 2026-06-09; genuinely one skill invocation per the repo's design | CONFIRMED (model + single-invocation mechanism); **omits** that Fable 5 had only been continuously available again for ~10 days after a 19-day export-control outage |
| 11 | Fable 5's scene transitions are "definitely a bit more sleeker" than GPT-5.6 Sol's | Both models real; comparison itself is a single uncontrolled run, not a controlled test | **Presenter's subjective opinion — not verifiable as an objective capability claim either way** |
| 12 | The video is not sponsored (implied by omission — no disclosure anywhere in the 9:49 transcript) | The description's very first link is a structurally sponsor/referral-shaped Higgsfield URL (`/s/cli-chase-h-ai-ejnlNI`) | **MISLEADING-BY-OMISSION** (likely undisclosed sponsor relationship) |

## Cross-links

[[scroll-world-animation-skill/_index]] · [[scroll-world-animation-skill/overview]] · [[scroll-world-animation-skill/source-provenance]]
