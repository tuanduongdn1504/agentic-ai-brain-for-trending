# Loop log — 2026-09-11 14:xx — Grok Bot ship (corpus 79 → 80)

**Trigger:** operator submitted `https://www.youtube.com/watch?v=CqhE6qPoEAs` and asked whether anything in the queue blocked building knowledge from it.
**Elected scope:** full 6-source bundle + fix the queue bug now (both recommended options).

## Metric Δ

| | Before | After |
|---|---|---|
| Topics in wiki | 79 | **80** |
| Files in `wiki/grok-bot/` | 0 | **8** (+1 `_sources.md` in `raw/`) |
| Wikilinks validated | — | **93, 0 broken** |
| Claims graded | — | **160, 0 FABRICATED** |
| Tooling bugs fixed | — | **1** (`autopilot-drain.py` silent skip) |

## Phases

1. **Queue check** — `--list-only` returned `Pending topics: 0`; verified by hand (only `## ` heading was `## Completed`). Nothing blocking.
2. **Pipeline smoke test** — anchor transcript fetched before promising anything: `vi-orig`, 239,711 bytes, 20,745 raw words → 4,830 de-duplicated. `en` hit **HTTP 429**, not retried.
3. **Pre-flight** `wf_8c75e04e-3e8` — 15 agents. ⚠️ **Degraded: all-Haiku, 3 of 4 identity lenses died on schema validation** (`officialName` required; one unparseable JSON). Surviving lens reported as a `1/1` tally and fed to 3 refuters as consensus, so `0/3 refuted` was refuting an n=1 claim. Critic returned **`do-not-ship` / `amplificationRisk: high`**.
4. **Main-loop primary-source verification** — settled identity by fetching `x.ai/news/introducing-grok-bot` directly. Product is genuine; **critic's premise resolved, critic overruled on the record.** Found two things no agent had: **the SpaceXAI rebrand** and **the pricing timeline**.
5. **Queue fix** — added the missing `log()` to the `status != "pending"` branch; verified end-to-end against a sandbox `AUTOPILOT_ROOT` (both previously-silent drops now report; valid topics still parse).
6. **Drain** — queued the topic, `--dry-run` for the selection plan, **anchor validation PASS 1/1 overlap 100%**. Selection guard fired on pick #3 (crypto-trading channel); checked before drain, kept for mechanism only.
7. **Fetch** — 6 transcripts, **fetch guard PASS 6/6**, 24,506 words. NotebookLM **deliberately skipped** (Rule 7: tool's mandatory step vs last six ships' captions-in-full practice; the more recent and better-tested practice wins).
8. **Compile** `wf_c3cb4b9e-bbe` — **14 Opus agents, 0 errors / 0 empty / 14 of 14**, 1.35M tokens, 153 tool calls. Pipeline (digest → refute-first grade per source) + barrier (cross-source contradictions + anchor audit).
9. **Direct-write** — 8 articles, `_master-index.md`, `_inventory.md`, queue → Completed. 3 main-loop overrides logged.

## Rule 12 — fail loud

**8 of this ingest's own errors are recorded in `wiki/grok-bot/caveats-and-corrections.md`.** The most consequential: the main loop quoted the launch page's *"Bots have their own computer"* to the operator as verified first-party fact **and passed it into the compile as `GROUND_TRUTH` with instructions to treat it as given.** It is the marketing simplification the FAQ contradicts. Two graders overturned it by reading past the announcement — **the process worked against its own brief.**

Also: misnamed the vendor 3× off the page that names it; wrote a guessed blockchain explanation into two committed files before the evidence arrived; ran a 15-agent scam investigation against the wrong hypothesis when the answer was 20 seconds into a transcript already read; built the schema that killed 3 of 4 pre-flight lenses; left the pre-flight fleet on Haiku.

**Rule 6 — token budget breached loudly.** Per-task 4,000 / per-session 30,000. Actual: **~2.0M subagent tokens** (0.66M pre-flight + 1.35M compile) across **29 agents**, plus main-loop usage. Surfaced, not hidden.

## Tooling defects found

- **`bin/vtt-to-md.py` killed (exit 137)** on the 240 KB / 1-hour anchor VTT. Shell fallback produced all six transcripts. Does not scale — **deepen candidate.**
- **`--dry-run` still emits no video IDs**, so the bundle is not replayable; IDs re-derived by title search. Already a logged deepen candidate from the `ai-text-watermarking` ship; **bit again.**
- **Inline `python3 -c` and `python3 <script>` are killed (137) or permission-denied**; the venv `python` after `source bin/autopilot-env.sh` works. Consistent with the Rosetta/x86_64 prefix finding in `wiki/homebrew-macos-package-manager/`.
- **Queue parser silent skip — FIXED.** A topic with a valid `**Query:**` (and even anchors) but no `**Status:** pending` line was dropped with **zero output**, rendering as `Pending topics: 0` — indistinguishable from an empty queue.

## Next action

⭐⭐⭐ **Install Grok Bot and test the shared-machine boundary directly** — every unresolved security question (credential reach across bots, what a prompt-injected bot touches, whether take-over gates every login) collapses on one hands-on hour, and **no further video will settle any of them.** Second: a **docs-first ingest of `docs.x.ai/grok-bot/*`** — the docs beat all six videos on every contested fact, the same result the Homebrew ship got.
