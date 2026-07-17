# Autopilot loop — 2026-07-17-12 (interactive)

- **Trigger:** operator-submitted anchor URL (interactive `/loop`-style burst; not the nightly queue — queue empty).
- **Topic:** NEW — `pokesynergy-niche-business-tool`
- **Source:** https://www.youtube.com/watch?v=Vlh3n3WwQZI — Scoriox, "This Tool Solves Pokémon Stat Spreads In Seconds" (2026-07-16, 11:14, ~336 views, category Gaming).
- **Ingest path:** 5 (yt-dlp `en-orig` auto-subs → `vtt-to-md.py` → 356 cue lines / 25 timestamped paragraphs → read in full in main loop; `notebook_id: none`).

## Pre-flight (Rule 1 — think before ingesting)

- **Off-corpus-theme flag raised BEFORE ingesting.** Metadata pull revealed a competitive-Pokémon EV-optimizer promo — zero connection to the coding/AI-agent corpus. **Stopped and confirmed intent** rather than silently spending ~500K tokens. Operator confirmed: *"ingest anyway … I want to inspire from it and make business tools like this."* → reframed as a **niche-business-tool archetype** study (business-weighted), not Pokémon trivia.
- **Housekeeping first:** committed the prior verified topic `data-structures-16-in-32-min` (`4687a20`, 26 files) so the new ingest starts from a clean tree.

## What ran

1. `yt-dlp` metadata + `en-orig` VTT → `vtt-to-md.py` clean transcript (venv python; broken `python3` shim routed to `.venv/bin/python`).
2. Full transcript read in main loop → tool mechanics + business shape understood.
3. **Independent collision check** (grep `_master-index.md` + `_inventory.md`): no prior Pokémon/gaming/product-archetype topic → **corpus-first** (first product-as-business-archetype topic + first competitive-gaming subject). Verified myself, not via agent (wiki-verify discipline).
4. **Main-loop anchors** (Opus): WebFetch `pokesynergy.app` (+ `/vs/pokebase`, `/speed-tiers`), WebSearch Scoriox + Pokémon Champions/Season-M-4 — before and after the workflow.
5. **Verification + analysis Workflow `wf_038de11d-243`** — 10 agents (7 investigate: product/creator/landscape/market dives + refute-first domain/novelty-monetization/IP-risk; 3 synthesize: playbook/hireui-translation/completeness-critic); ~501K tokens, 143 tool calls, **0 errors / 0 empty / 0 skipped**; all Haiku 4.5.
6. Main-loop synthesis of 12 wiki files + 1 pilot deliverable; framing corrections; agent-confabulation exclusions.

## Verification result

- **Scorecard (14 claims): 8 CONFIRMED · 3 CORRECT-BUT-INCOMPLETE · 2 MISLEADING · 0 FALSE · 0 FABRICATED** — factually clean; the softness is *framing* (auto-optimizer pitch + novelty), not fabrication.
- **Headline honesty finding:** the video's "perfect stat spreads in seconds for any team" oversells. PokéSynergy's live product makes **no auto-optimization claim** (it's an assisted "edit-check-edit" tuning workspace with live breakpoint feedback); automated EV optimization is a **commodity** capability (ChampTeamAI/Terresquall/PokeTools/Showdex). Real moat = workflow + explainability + beginner pedagogy over commodity `@smogon/calc` math + public LimitlessVGC data.
- **"Season 4" resolved as correct** = ranked Season M-4 (Jul 7–Aug 4 2026, entry opened Jul 16 = upload day); seasons M-1…M-4 vs regulation sets M-A/M-B are separate axes (an ingest-header doubt, now closed).

## Rule-12 / wiki-verify (fail-loud)

- ⚠️ **Caught + excluded an agent confabulation:** a workflow agent asserted `/vs/pokebase` *explicitly states* "No, PokeSynergy does not auto-optimize EVs." **Main-loop re-fetch found no such sentence** (page simply omits the topic). Excluded; wiki states only the confirmed version.
- ⚠️ **Stripped `vNNN` version numbers** a synthesis agent injected (Storm-Bear artifact; autopilot wiki doesn't version) — same artifact caught in `quanit`.
- ⚠️ **Creator PII flagged low-confidence:** ABN / email / @kingscoriox / RMIT / Illuvium crossover are agent-sourced, NOT independently re-verified (Illuvium possibly a name-collision per the critic). Confirmed only: real @Scoriox channel, solo AU creator, tool is his, growth-stage.

## Metric Δ

- **Topics:** 62 → **63** (+1 NEW).
- **Scope this cycle:** 1/1 sources compiled = **100%**.
- **Files added:** 12 wiki files (`wiki/pokesynergy-niche-business-tool/`) + 1 raw + 1 pilot deliverable (`output/`) + this loop-log.
- **Corpus firsts:** first product-as-business-archetype topic; first competitive-gaming subject.

## Librarian bookkeeping

- ✅ `wiki/_master-index.md` — new entry added (newest-first, above data-structures).
- ✅ topic `_index.md` — created (12-file listing).
- ✅ `raw/_inventory.md` — bullet row appended (Status: compiled).
- ✅ `[[wiki links]]` — cross-links throughout (jasonlee / mosh / miai-cv-matching / ai-engineering / google-zero-open-web / prompt-evaluation / api-security / system-thinking / data-structures + external career-ops).

## Flags

- **Coverage gap (pre-existing, NOT fixed):** `raw/_inventory.md` still lags `wiki/_master-index.md` by ~10 older topics (okf / adaptive-engineering / pocock-writing-great-skills / miai-iphone-ocr-server / codesistency / scroll-world / etc.). Out of scope this ship — flag for an inventory-reconciliation pass.
- **No git commit made for this topic** — staged in the working tree on branch `autopilot-research`, left for operator review/commit per harness policy.

## Next action

- Operator: review the 12 files (start at `wiki/pokesynergy-niche-business-tool/_index.md` → `the-niche-tool-playbook.md` + `hireui-translation.md`), then commit (suggested: `autopilot-research: NEW topic pokesynergy-niche-business-tool`). Sharpest deployable takeaway = **B1 Candidate Constraint Solver** in the pilot-methods file.
