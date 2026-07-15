# Source Provenance

## Primary source

- **Video:** Rajiv Chandegra, *"Beyond the Harness: A Journey Towards Adaptative Engineering"* — [youtube.com/watch?v=qdZzND79mcg](https://www.youtube.com/watch?v=qdZzND79mcg)
- **Channel:** AI Engineer (@aiDotEngineer) — the ai.engineer conference's official channel
- **Event:** **AI Engineer Europe 2026** (April 8–10, London) — *not* World's Fair (see [[caveats-and-corrections]] #1)
- **Uploaded:** 2026-07-07 (delayed publication) · **Duration:** 37:01 · **Views at ingest:** ~6,363
- **Speaker:** Rajiv Chandegra — practicing GP in London; founder/director, Annicha Labs ([annicha.co](https://annicha.co/), [rajivchandegra.com](https://rajivchandegra.com/), [@rajivchandegra](https://x.com/rajivchandegra))

## Capture method (path 5 — yt-dlp only, no NotebookLM)

- `yt-dlp --skip-download --print …` for metadata; `--write-auto-subs --sub-langs en.* --sub-format vtt` for captions.
- EN auto-captions → `bin/vtt-to-md.py` (system `python3`) → **894 unique cue lines → 78 timestamped `[mm:ss]` paragraphs**, deduped, word-timing tags stripped.
- Full transcript **read in full in the main loop** (Opus 4.8).
- Raw artifact: `raw/2026-07-15-adaptive-engineering-beyond-harness.md` (metadata header + video description + full transcript).
- Vault-shell notes: routed all shell output to scratchpad files and Read them back (flaky-shell workaround); one `python3` invocation was SIGKILLed on a bad arg-count call before the correct 2-arg run succeeded.

## Verification workflow — `wf_993219c1-885`

- **14 agents, all Haiku 4.5; 518,771 tokens, 123 tool calls, 0 errors, 0 empty.** Duration ~144s.
- **Phase 1 — Verify-facts (11 refute-first fact-checkers):** each verified one checkable claim via WebSearch/WebFetch, defaulting to CBI without independent evidence, FALSE/MISLEADING only with cited proof. Claims: event, speaker, hermes, pi-harness, harness-list, ackoff-mess, boids, cynefin, water-wetness, phase-transition, taylorism → **10 CONFIRMED / 1 MISLEADING** ([[claims-scorecard]]).
- **Phase 2 — Corpus xref (1 agent):** grepped/read the vault; returned 10 genuinely-related topics *each with a quoted evidence line from a real file* (harness-engineering, multi-agent-orchestration, agentic-analytics-harness, pocock-agentic-workflow, ai-operating-system, workflow-ai-coding, pocock-software-fundamentals, agent-development-lifecycle, autonomous-loops, pi-mono@v36). No invented topics.
- **Phase 3 — Thesis critique (1 agent):** steelman + 4 objections + corpus-tension + novelty verdict (verbatim-carried into [[failure-modes]] and [[caveats-and-corrections]]).
- **Phase 4 — Completeness critic (1 agent):** surfaced 3 more checkable claims (AGENTS.md/CLAUDE.md load, vendor system prompt, loop-engineering recency) + 3 integrity flags → folded into [[claims-scorecard]].

## Main-loop Opus ground-checks (independent of the Haiku agents)

Per the vault's "independently verify identity/collision claims" discipline, the two most consequential findings were re-checked by the main loop via WebSearch:

1. **Event = AI Engineer Europe 2026 (London).** Confirmed via `ai.engineer/europe/2026`, [StartupHub.ai](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/ai-s-future-from-fixed-to-adaptive-engineering), [BigGo Finance](https://finance.biggo.com/news/769403a199262394), Latent.Space AINews Europe recap. Overturned the ingest's initial "World's Fair" assumption.
2. **Pi repo move** `badlogic/pi-mono` → `earendil-works/pi` (npm `@earendil-works/pi-coding-agent`), ~Apr–May 2026, Earendil Inc. (Armin Ronacher co-founder). Confirmed via Mario Zechner's *"I've sold out"* post (2026-04-08), npm, and GitHub.

## Secondary coverage (corroborating)

- **StartupHub.ai** — *"AI's Future: From Fixed to Adaptive Engineering"* — written recap of this exact talk (corroborates the thesis summary; note it repeats the "Anitcha" misspelling).
- **BigGo Finance** — *"Rajiv Chandegra: AI's Limiting Factor Isn't Model Strength, It's Harness Adaptability"* — quotes the closing thesis directly.

## Agent-misfire log

- **None.** No verifier misfired; no fabricated corpus facts; no empty results. The corpus-xref agent's evidence lines were spot-checked against the real `harness-engineering/_index.md` and matched. The only correction to a *machine* claim was upgrading the completeness critic's "contradicts talk" framing on AGENTS.md to "correct-with-caveat" after re-reading the transcript (the speaker hedged "…or the Claude.md if you're using Claude code").

## Reproduce

```bash
cd "/Users/Cvtot/KJ-OS-autopilot/03 Projects/autopilot-research"
export PATH="/usr/local/bin:$PATH"
yt-dlp --skip-download --write-auto-subs --sub-langs "en.*" --sub-format vtt \
  --output "cap-%(id)s.%(ext)s" "https://www.youtube.com/watch?v=qdZzND79mcg"
python3 bin/vtt-to-md.py cap-qdZzND79mcg.en.vtt transcript.md
```
