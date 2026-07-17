# Source & creator

## Video metadata

- **Title:** "Kimi K3 Just Revealed The Worlds Most Powerful AI (Beats Fable 5 and GPT-5.6)"
- **ID / URL:** [`DAKnynuGyy4`](https://www.youtube.com/watch?v=DAKnynuGyy4)
- **Channel:** TheAIGRID ([@TheAiGrid](https://www.youtube.com/@TheAiGrid))
- **Published:** 2026-07-17 (one day after K3's 2026-07-16 launch)
- **Length / views:** 36:46 / ~12.6K views, 399 likes at ingest
- **Category / language:** Science & Technology / English

## Creator — TheAIGRID

- UK-based AI-news YouTube channel, **~360K subscribers**, 60M+ total views, founded ~Jan 2023; near-daily AI-demo/news content (~18 min/video).
- **Editorial posture: hype-leaning.** Titles/thumbnails follow the sensationalist AI-YouTube convention ("Just Revealed The World's Most Powerful AI," "Game OVER?"). The verifier found **no fabrication red flags** — it's a legitimate, established channel — but it is **reaction/aggregation content, not critical analysis or primary research.** Read accordingly: the specs it relays are usually accurate; the framing (superlatives, availability, geopolitics) is where it over-reaches, as this topic documents.
- **PII discipline:** the channel's public About page names an individual; held as **low-confidence and not load-bearing**, so this wiki identifies the creator by the **@TheAiGrid** handle only (cf. the corpus' @anonystick and pokesynergy PII handling). [[caveats-and-corrections]]

## Ingest & verification method

- **Path 5** — `yt-dlp` `en-orig` auto-captions → `bin/vtt-to-md.py` → **1,031 cue lines / 80 timestamped paragraphs** (~7,200 words), read in full in the main loop. `notebook_id: none` (no NotebookLM). Raw at `raw/2026-07-17-kimi-k3-worlds-most-powerful-ai.md`.
- **Main-loop anchors (Opus, before the workflow):** 6 WebSearch + 2 WebFetch calls locking the factual spine and the load-bearing corrections (release date, params, pricing, benchmarks, open-weights timing, export-control facts) against primary/multiple sources — Moonshot blog, Artificial Analysis, arena.ai, Simon Willison, the-decoder, CNBC/Fortune/WaPo (export controls), ArXiv.
- **Independent collision check:** grep of `wiki/_master-index.md` + `raw/_inventory.md` — no prior Kimi/Moonshot/model-landscape topic → **corpus-first** (verified by main loop, not delegated, per wiki-verify discipline).
- **Verification + synthesis Workflow `wf_74ace947-2b5`:** **11 agents** = 6 dives (architecture / benchmarks / pricing / open-weights / reception / cyber+creator) → 3 refute-first verifiers (12 claims across weights-price-index-export / narrow-halluc-winrate-debug / writing-gdpval-demos-creator) → 2 synthesizers (corrected scorecard + hireui translation & completeness critic). ~568K tokens, 161 tool calls, **0 errors / 0 empty / 0 skipped**. **All 7 flagged corrections returned UPHELD at high confidence.**
- ⚠️ **Model-override limitation (disclosed):** per-agent `opus`/`sonnet` overrides in the workflow were **silently ignored by the runtime** — all 11 agents ran **Haiku 4.5** (same as the OKF ship). Because of this, every load-bearing correction was **independently re-verified in the main loop on Opus** before ship; the workflow served as adversarial breadth, not sole authority.

## Key sources (verification)

- Moonshot: `kimi.com/blog/kimi-k3`, `platform.kimi.ai`
- Benchmarks: `artificialanalysis.ai/models/kimi-k3`, `arena.ai` (X @arena), Vals; Simon Willison `simonwillison.net/2026/Jul/16/kimi-k3/`
- Architecture: ArXiv 2510.26692 (Kimi Linear / KDA), ArXiv 2603.15031 (Attention Residuals), MarkTechPost
- Pricing / weights: the-decoder, cryptobriefing (July-27 weights), modemguides (hardware reality)
- Export controls: CNBC / Fortune / Washington Post / Al Jazeera / CyberScoop (Fable 5 & Mythos 5, Jun–Jul 2026); CyberGym ArXiv 2506.02548 + K2.5 eval ArXiv 2604.03121

## Key Takeaways

- A **hype-channel reaction video** one day post-launch — accurate on specs, inflated on framing.
- Verified by **main-loop Opus anchors + an 11-agent refute-first workflow**; all corrections held.
- Creator identity held to the **handle**; the one context-bleed ("13 languages") and the model-override limitation are disclosed in [[caveats-and-corrections]].
