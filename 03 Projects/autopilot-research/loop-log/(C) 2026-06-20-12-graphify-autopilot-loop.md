# (C) Autopilot Loop — 2026-06-20-12 (graphify-codebase-graph)

> **Trigger:** interactive `/loop`-style operator request ("build knowledge from this video + double deep-dive the original resource, then show me many pilot methods")
> **Topic:** graphify-codebase-graph (NEW)
> **Source video:** [-L_faOE-H5g](https://www.youtube.com/watch?v=-L_faOE-H5g) — AI Stack Engineer, "OpenCode + Graphify: Stop Wasting Tokens" (2026-04-21, 10:11, 46,677 views)
> **Started:** 2026-06-20 ~12:20 (Saigon) · **Ended:** same session · **Mode:** main-loop direct-write + 1 research Workflow

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 video (transcript) + 5 originals (repo/PyPI/gist/OpenCode/lucasrosati) via Workflow | 1 (cold-start topic) | 0 (10-file topic + pilot doc) | ~1.0 |

## What ran

- **Path 5 yt-dlp** — pulled `en` auto-subs (ffmpeg absent → VTT parsed directly into a 1,753-word clean transcript; saved to `raw/2026-06-20-graphify-opencode.md`, read in full).
- **Workflow `wf_2f2a5052-7ac`** (11 agents, 384,949 subagent tokens, 123 tool uses, ~3.9 min): 7 deep-dive agents (graphify-repo / architecture / 71.5×-forensics / lucasrosati-memory / opencode-plugin / karpathy-attribution / security-posture) + 4 adversarial verifiers (71.5× / karpathy / cost-model / install-safety).

## Sources ingested

- `raw/2026-06-20-graphify-opencode.md` (yt-dlp VTT, 1,753 words, full transcript)
- Originals deep-dived (via Workflow, not stored as raw): Graphify repo + docs + PyPI; Karpathy LLM Wiki gist; OpenCode docs/repo; lucasrosati/claude-code-memory-setup; 71.5× forensic blogs (gitpicks/skillbloomer/dev.to/exchangepedia/medium/roborhythms).

## Wiki articles created (10 — NEW topic)

- `wiki/graphify-codebase-graph/_index.md` (NEW)
- `wiki/graphify-codebase-graph/overview.md` (NEW)
- `wiki/graphify-codebase-graph/three-pass-architecture.md` (NEW)
- `wiki/graphify-codebase-graph/cli-and-commands.md` (NEW)
- `wiki/graphify-codebase-graph/opencode-integration.md` (NEW)
- `wiki/graphify-codebase-graph/token-savings-reality.md` (NEW)
- `wiki/graphify-codebase-graph/karpathy-llm-wiki-lineage.md` (NEW)
- `wiki/graphify-codebase-graph/security-and-install-safety.md` (NEW)
- `wiki/graphify-codebase-graph/obsidian-graphify-memory-setup.md` (NEW)
- `wiki/graphify-codebase-graph/source-provenance.md` (NEW)
- `wiki/_master-index.md` (UPDATED — added `## graphify-codebase-graph`)
- `raw/_inventory.md` (UPDATED — +1 row + coverage bullet)

## Deliverable

- `output/(C) 2026-06-20-graphify-opencode-pilot-methods.md` — **16 ranked pilot methods** across 6 surfaces (autopilot-vault / Storm-Bear-vault / hireui-Goal-#2 / Claude-Code-harness / cost-local-inference / Scrum-coaching) + skip-list + critic reframe.

## Adversarial verification corrections (Rule 12 fail-loud)

1. **71.5× → "accurate-but-cherry-picked."** Real only for a 52-file mixed-media benchmark (Karpathy repos + 5 papers + 4 images). Independent: **7.3×** (Python codebase), **~7-8%** (browser-use). Expect **2-8×**. No Anthropic validation; absolute token counts unpublished.
2. **Karpathy attribution → overstated.** Karpathy *published the LLM Wiki pattern*; Safi Shamsi built Graphify ~48h later as an **independent** implementation. Karpathy **did not create/endorse** it. "pile of mixed content you can never fully reconstruct" = **Graphify marketing copy, NOT a Karpathy quote.**
3. **Cost model → verified accurate.** Passes 1-2 zero-API local; only Pass 3 paid, cached, incremental, skipped for code-only repos. Hidden costs flagged (first-build, local Whisper compute, per-query reads).
4. **Install safety → splits.** Safe for the knowledge vault (`uv tool install graphifyy`, hooks off, no PII); **risky for hireui** (typosquat `graphifyy`-vs-unclaimed-`graphify` Issue #280 → `.env.local`; Pass-3 → GDPR; auto-skill-injection → I-8 violation; no LLM → no urgency).

## Honest gaps / un-fetchable (flagged, not fabricated)

- aiopsschool.com blog — ECONNREFUSED.
- Karpathy's original X post — HTTP 402 (reconstructed from the gist + secondary sources; the gist itself confirmed).
- OpenCode raw README — 404 (used opencode.ai/docs).
- Some levelup.gitconnected content — paywall.
- Language count inconsistent across sources (20 / 25 / 36+) — recorded as "most mainstream languages."
- Note: this is an interactive deep-build the operator explicitly requested ("double deep-dive" + "many methods"); it intentionally exceeds the routine's autonomous per-task token guideline (Rule 6) — surfaced here rather than silently.

## Final metric

- `gaps_closed_ratio` ≈ 1.0 (cold-start topic fully compiled + pilot doc shipped).
- Stop reason: deliverables complete (wiki topic + verified provenance + 16-method pilot doc).

## Suggested next action

Operator: do **pilot A1** (~15 min, $0) — `graphify . --wiki` on a **copy** of `wiki/` and read `GRAPH_REPORT.md` to see an automated structural map of your own knowledge base (then A2: promote any genuine surprising-connection into a curated `[[link]]`). When you want the one real token number, run the **D9 → D10** harness pilot on a single stable repo and measure over a week (Anthropic dashboard). Consider the **branch-ship discipline** ([[feedback_branch_wiki_ships_not_main]]): commit this on `wiki/graphify-codebase-graph` off `main` for operator review, don't auto-merge.
