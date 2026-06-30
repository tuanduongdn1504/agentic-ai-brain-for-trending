# NEW deep-dive: Ponytail (`DietrichGebert/ponytail`)

> "Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote." The fastest-growing repo in the whole set — and the cost-discipline pick for hireui.

## Verified facts (gh api, 2026-06-29)

- **Repo:** `DietrichGebert/ponytail` · **65,885★** · **MIT** · JavaScript · created **2026-06-12** · pushed 2026-06-29 · not archived.
- **Age:** 17 days old at ingest → **~3,876 stars/day**. That's 8–40× the velocity of a "normal" viral repo (100–500/day); it is in the **extreme** growth tier. Chase's "one of the fastest-growing AI repos in the world right now" is **CONFIRMED**.
- Requires **Node.js ≥ 22.22.0** on PATH for the Claude Code lifecycle hooks (optional but recommended).

## What it is

A plugin/skill for **16+ AI agent platforms** (Claude Code, Codex, GitHub Copilot CLI, Cursor, Windsurf, Cline, Devin, OpenCode, Gemini, Kiro, OpenClaw…) that makes the agent write *less* code by forcing a discipline check **before** it writes anything — and then writing only the minimum that works.

## How it works — the 7-rung decision ladder

Run **after** the agent has read the code and traced the real flow (lazy about the *solution*, never about *reading*):

1. **Does this need to exist?** → no: skip it (YAGNI)
2. **Already in this codebase?** → reuse it, don't rewrite
3. **Stdlib does it?** → use it
4. **Native platform feature?** → use it
5. **Installed dependency?** → use it
6. **One line?** → one line
7. **Only then:** the minimum that works

The video quotes 6 questions; the repo documents **7 rungs** (it omits the explicit step 7). **Safety is never optimized away** — trust-boundary validation, data-loss handling, security, and accessibility are explicitly off-limits to the minimizer.

**Commands:** `/ponytail` (check/set level), `/ponytail-review` (find over-engineering in a diff), `/ponytail-audit` (scan the repo), `/ponytail-debt` (harvest deferred shortcuts), `/ponytail-gain` (impact scoreboard). **Intensity modes:** `lite` / `full` / `ultra` / `off` (via `/ponytail` or `PONYTAIL_DEFAULT_MODE`).

**Install (Claude Code):** `/plugin marketplace add DietrichGebert/ponytail` then `/plugin install ponytail@ponytail` (two prompts). Cursor/Windsurf/Cline: copy the matching rules file.

## The benchmark — what's real, what's not

**CONFIRMED** (from the repo's own `benchmarks/results/2026-06-18-agentic.md`, an agentic benchmark on a real FastAPI+React repo, 12 feature tasks, n=4, **Haiku 4.5**):

| Metric | Video says | Repo measured | Verdict |
|---|---|---|---|
| Less code (LOC) | 50% | **−54%** mean (up to −94% on over-build cases, ~0% on already-minimal code) | rounded down |
| Fewer tokens | 22% | **−22%** | exact |
| Cheaper | 20% | **−20%** | exact |
| Faster | 27% | **−27%** | exact |
| Safe | — | **100% safe** (vs 95% for a bare "one-liner" prompt) | confirmed |

**UNVERIFIED — flag this:** Chase says "these numbers are with Haiku; with Opus they're *even more drastic*." **No agentic Opus benchmark exists.** The repo explicitly states it "stopped at Haiku for cost" — the harness *supports* Sonnet/Opus but no results were published. An *older single-shot* benchmark tested 3 models, but it is not the agentic benchmark and makes no "Opus is more drastic" claim. **Treat the Opus claim as speculation; run your own test before promoting cost savings on larger models.**

## Why it matters here (cost-discipline)

Ponytail is the single **highest-leverage NEW pilot** in the set for the operator's Goal-#2 cost thread:

- It's the **complement to cc-sdd** inside Claude Code — cc-sdd is the *methodology* layer (spec-driven), Ponytail is the *code-generation discipline* layer. They compose orthogonally.
- At hireui's eventual LLM scale, **−22% tokens / −20% cost per feature** compounds across a sprint — and hireui's zero-LLM baseline means *any* reduction is pure win once it ships.
- The 100%-safe guarantee (it won't strip validation on auth/PII paths) matters for a recruitment SaaS where candidate-data leaks = legal liability.

**Pilot path:** `/plugin install ponytail` on a hireui `agent-*` branch (per I-2) → run one feature with Ponytail on vs off → measure the LOC/token delta on the actual git diff. ~1h install + 1 sprint. Orthogonal to (and composable with) the cc-sdd #1 pilot. Compose the measurement with [[claude-api-cost-optimization/_index]] + `ccusage` from [[claude-code-observability/_index]].

## Cross-links

- [[claude-api-cost-optimization/_index]] — the cost levers Ponytail operationalizes at the code-gen layer
- [[claude-code-skills-stack/_index]] — cc-sdd / SDD frameworks (methodology layer Ponytail complements)
- [[harness-engineering/_index]] — Ponytail as an individual-scale discipline skill (Zen van Riel's `/smell` is a sibling "prompt-as-engineering-artifact")
- [[claude-code-observability/_index]] — `ccusage` to measure the token delta
- [[claude-code-plugins-stack/source-provenance]] — the Opus-claim flag
