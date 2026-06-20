# (C) Autopilot Loop — 2026-06-20-08

> **Trigger:** /loop (manual, interactive — operator submitted a single YouTube URL with "build knowledge + double deep-dive the original resource + show me many pilot methods")
> **Topic:** cowork-third-party-inference (Cowork on 3P — free/private local + cheap cloud models)
> **Started:** 2026-06-20 ~07:55 (local)
> **Ended:** 2026-06-20 ~08:30 (local)
> **Duration:** ~35m wall-clock (incl. ~12.5m Workflow run + recovery of 2 failed synthesis agents)

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 video (+ 6 original-resource research dossiers) | 1 (cold-start NEW topic) | 0 (11 articles + index + pilot) | ~1.0 |

Cold-start single-cycle compile. `gaps_closed_ratio ≈ 1.0` (topic created from nothing → fully compiled).

## Method

- Path 5 (yt-dlp-only): `yt-dlp --write-auto-subs --sub-langs en` → `bin/vtt-to-md.py` dedup → full transcript (24K / ~4.5K words), **read in full**.
- Grounding: 3 operator WebSearches confirmed the feature is real + first-party documented before committing compute.
- Deep-dive: Workflow `wf_4de40f38-856` — 28 agents, 1.73M subagent tokens, 274 tool uses:
  - **6 original-resource research agents** (Cowork-3P gateway docs / Ollama / OpenRouter / Tailscale / skills-MCP-harness / ecosystem-evolution) → tiered, cited dossiers (138 verified facts).
  - **9 draft→verify pipelines** (each article adversarially fact-checked against transcript + first-party docs).
  - **crosswalk + provenance + pilot + pilot-critic** synthesis.

## Sources ingested

- `raw/(C) 2026-06-20-cowork-ollama-3p-local-private.md` (yt-dlp en captions, ME4flXK_6tQ — Bart Slodyczka)
- 6 original-resource research dossiers (in-workflow; first-party: claude.com/docs/cowork/3p, docs.ollama.com, openrouter.ai, tailscale.com, github.com/anthropics/skills, github.com/brave/brave-search-mcp-server)

## Wiki articles created (11 + index)

- `wiki/cowork-third-party-inference/_index.md` (NEW topic)
- overview.md · setup-local-ollama.md · setup-cloud-openrouter.md
- gateway-protocol-deep-dive.md · ollama-deep-dive.md · openrouter-deep-dive.md · tailscale-https-bridge.md (the 4 original-resource deep-dives)
- skills-mcp-websearch-byom.md · tradeoffs-and-when-to-use.md
- video-to-original-crosswalk.md · source-provenance.md
- `wiki/_master-index.md` (UPDATED — added cowork-third-party-inference)
- `raw/_inventory.md` (UPDATED — +1 row)

## Pilot deliverable

- `output/(C) 2026-06-20-cowork-3p-local-models-pilot-methods.md` — **18 ranked pilot methods** across 4 surfaces (autopilot pipeline / hireui Goal-#2 / Claude-Code harness / Scrum coaching). Headline: **hireui candidate-PII → data-sovereignty via a BYOM gateway + local model**.

## Fail-loud notes (Rule 12)

- **2 synthesis agents failed by returning meta-descriptions instead of article bodies** (the `source-provenance` writer returned "Word count: 288 lines | Size: 19.2 KB…"; the `pilot-critic` returned a review of its own 6 fixes instead of the corrected document). Both were **recovered from the underlying structured data** rather than shipped:
  - Pilot: recovered the real 27K-char 18-method draft from agent transcript `agent-a7fdb9af3003b2116.jsonl`; applied the critic's 6 legitimate fixes by hand (Gemma size / Brave MCP package / qualitative-slowness / Claude-Code-3P scope / "Omni" attribution removed / Tailscale-now-optional).
  - Provenance: rewritten by the librarian directly from the 138 structured provenance entries + research corrections.
- This is the kind of agent-output-shape failure worth codifying in the routine: **synthesis/critic prompts must demand "return the full document as `body_markdown`, NOT a description of it"** + a post-workflow sanity check on body length/shape before writing to disk.

## Final metric

- `gaps_closed_ratio ≈ 1.0` (cold-start NEW topic fully compiled in 1 cycle)
- Stop reason: target reached (topic compiled; operator's 3-part ask — build / deep-dive / pilot — all delivered)

## Top unclosed gaps (carry-forward)

1. **Live price/size verification** — OpenRouter per-model pricing + exact Gemma tags/sizes were intermittently unreachable on 2026-06-20; flagged as dated in [[cowork-third-party-inference/source-provenance]]. Re-verify before relying on cost numbers.
2. **The local-no-bridge path needs hands-on confirmation** — whether a given Cowork build accepts a plain `http://localhost:11434` gateway URL (Ollama v0.14.0 native API) vs still wanting HTTPS. Best closed by an actual pilot (method B3/C13/C14).
3. **Claude-Code-in-Desktop vs Claude-Code-CLs nuance** — the 3P gateway UI is Cowork/Desktop; the standalone CLI uses `ANTHROPIC_BASE_URL`. Articles capture the actionable truth; a single explicit disambiguation note could be added if it confuses on re-read.

## Suggested next action

The operator's headline path to Goal #2: do **pilot B1 + B2 this week** (90 min, no code) — a `DATA_SOVEREIGNTY.md` contract + a `gateway-api-spec` in `hireui/_bmad-output/runbooks/`, so hireui is built model-agnostic from day one (recruitment PII never leaves a private model). Then **A1 + B4** (set up Ollama locally + eval a candidate-screen on the local model vs Opus). Offer to scaffold either on request. Also: this topic is a strong **promotion candidate** to the Storm Bear curated wiki (pairs with the existing claude-cowork promotion candidate) — consider at the next mini-audit cadence.
