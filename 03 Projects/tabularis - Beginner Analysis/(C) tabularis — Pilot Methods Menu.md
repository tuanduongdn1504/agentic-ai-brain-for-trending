# (C) tabularis — Pilot Methods Menu

> 24 ways to apply `TabularisDB/tabularis` (v212), ranked from zero-risk reading to a real hireui Goal-#2 artifact.
> **⭐ One-thing path: A1 → C11 → D16.** (Read the MCP-bridge + safety model → connect it read-only to a scratch DB → give hireui's own future data layer a gated, read-only MCP access path for Claude — behind hireui's CONSTITUTION.)

tabularis is on-goal for **both** goals: it's a first-party MCP server (Goal #1 agent-capability substrate) *and* the operator is exactly its target user — a solo dev building a database-backed product (hireui) with Claude Code. It is also **directly, safely pilotable** — but the load-bearing risk is that its MCP server gives an *agent* SQL rights over your *real* databases, so every hands-on rung starts read-only + scratch/staging.

---

## A — Read & learn (zero install, zero risk)

- **A1 ⭐ — Read the MCP-bridge model + the safety machinery.** Internalize the design: connect once in the GUI → the agent reaches the DB through the *same* profile (no secret-pasting) → **per-connection read-only mode + approval gates + pre-flight EXPLAIN failing closed on stacked multi-statement payloads.** This is the reference design for "how do I give an agent database access without handing it a loaded gun." (`tabularis.dev/solutions/mcp-database-client`.)
- **A2 — Read the 4-tool surface as an MCP-design case study.** `list_connections` / `list_tables` / `describe_table` / `run_query` — four well-scoped tools cover the whole "let an agent explore + query a DB" job. Contrast with palmier-pro v192's 51-tool timeline surface: same product-first-MCP relationship, wildly different tool granularity. A lesson in scoping an MCP surface.
- **A3 — Read Debernardi's "solo-dev-with-Claude-Code" retrospective** (DEV/HackerNoon: "0→1000 stars in 10 weeks", "41 releases in 11 weeks, one person"). The honest division of labor — *human owns the decisions, AI collapses decision→implementation distance* — is a direct Goal-#1 case study for the operator's own build posture.
- **A4 — Read the plugin-as-growth-flywheel story.** JSON-RPC-2.0-over-stdin/stdout, language-agnostic, introduced at the ~1-month mark → converted users into contributors. A model for turning a solo tool into a community project.

## B — Borrow patterns (zero install; into the vault / hireui specs)

- **B5 — Steal the MCP safety model into hireui's LLM-integration ADR.** The "read-only-by-default + approval-gate + pre-flight-EXPLAIN + fail-closed-on-ambiguous" pattern is exactly what hireui's RATIFIED candidate-LLM legibility ADR needs for *any* agent/LLM path that touches a database with candidate PII. Write it in as a rule.
- **B6 — Steal the "expose the data TO the agent, don't put the agent IN the app" framing.** A crisp architectural principle for hireui's eventual agent features: a gated bridge (auditable, revocable) beats an in-app agent with ambient DB access.
- **B7 — Borrow the provider-agnostic text-to-SQL seam** (OpenAI/Anthropic/MiniMax/OpenRouter/Ollama/OpenAI-compat) as another data-point for hireui's vendor-seam (composes with the meetily v196 `generate_summary()` + mosh-ai A2 + AIRI v210 `xsAI` reference). One call path, many providers, a local option.
- **B8 — Borrow the language-agnostic JSON-RPC plugin pattern** as a reference for any "let contributors extend this in any language" surface you build.

## C — Hands-on (scratch install; read-only, scratch/staging DB)

- **C11 ⭐ — Install-snapshot → install the native app → connect a scratch DB read-only → enable MCP → point Claude Code at it → have Claude explore + query the scratch schema.** Prove the whole loop end-to-end on throwaway data. Use `winget install Debba.Tabularis` / `brew install --cask tabularis` / snap — native package install, not `curl|bash`.
- **C12 — Verify the safety gates actually fire.** On a read-only connection, ask the agent to run an `UPDATE`/`DROP`; confirm it's blocked. Feed a stacked multi-statement; confirm it fails closed. Don't trust the README — see the gate work before you trust it near real data.
- **C13 — Try text-to-SQL against a local model (Ollama).** Measure draft-SQL quality on your own schema entirely offline (privacy path) vs. a hosted model. A data-residency + quality anchor.
- **C14 — Use the SQL notebook + visual EXPLAIN on a real (read-only) query you already care about.** Evaluate it as a day-to-day tool independent of the AI angle — it's a genuinely good SQL workspace.

## D — hireui / Goal-#2 (behind hireui's CONSTITUTION: I-2 `agent-*` branch, I-8 operator-installs, GitNexus-first)

- **D16 ⭐ — Give a hireui *staging clone* a gated, read-only MCP access path for Claude.** Connect hireui's staging DB in tabularis **read-only**, enable MCP, and let Claude Code do schema-aware analysis (query shapes, index/EXPLAIN review, "which tables back the candidate pipeline?") — the exact use tabularis is built for, on the operator's own database-backed product. First real Goal-#2 artifact from this ship. **Never point it at production with real candidate PII until D17 passes.**
- **D17 — Data-residency + PII review FIRST.** Candidate PII in the schema means: read-only only, EXPLAIN-gated, local-or-no-training model for any text-to-SQL, and a written residency ADR before any non-staging connection (composes with the miai-cv-matching / OfficeCLI v206 D21 / PixelRAG v211 residency threads).
- **D18 — Use tabularis's MCP schema-introspection to accelerate hireui's own MCP-server design** (the palmier-pro v192 `ToolExecutor` template + D2). "Here's what a clean 4-tool DB MCP surface looks like" is a concrete template for hireui exposing its *own* domain objects (candidates, jobs, pipeline stages) to an agent later.
- **D19 — Prototype a read-only "ask hireui's data a question" recruiter feature** on a staging clone, gated exactly like tabularis's MCP (read-only + approval + EXPLAIN) — never-auto-write, never-auto-reject.

## E — Personal / off-goal

- **E20 — Adopt tabularis as your daily SQL client** across the databases you already touch (Postgres/MySQL/SQLite + plugins). Off-goal but a genuine quality-of-life win; a good open-source Apache-2.0 tool.
- **E21 — Contribute a plugin** for a database you use that isn't shipped yet (the JSON-RPC plugin system is language-agnostic) — a low-friction OSS contribution + a way to learn the plugin protocol hands-on.

## F — Vault-meta

- **F22 — File the v192 §C standalone N=1→N=2 + the promotion-to-CONFIRMED candidacy for the ~v212 audit.** tabularis is a *stronger* N=2 than OmniRoute v208's (fully independent, cross-domain, non-port) → the "Product-First Native App + First-Party MCP Server" standalone is a strong promotion-to-CONFIRMED candidate; also carry forward the "non-coding domain" clause-generalization recommendation.
- **F23 — Synthesize the "product-first-app-with-first-party-MCP" cluster** across palmier-pro v192 (video) + tabularis v212 (database) + watch for a 3rd (the Figma/Notion/Linear/Blender-class move the v192 row predicted). The N=3 that confirms the CONFIRMED promotion.
- **F24 — Log the corpus-recursive sponsorship** (Kilo Code v177 sponsors tabularis) as a NOT-#57 data-point + the first database-GUI-domain data-point, for the audit's collision map.

---

## Fence (mandatory for any hands-on rung)

- **`install-snapshot`** before installing (native app; winget/brew/snap — **not** `curl|bash`, but still snapshot).
- **Read-only connection + scratch/staging DB first.** The MCP server's whole risk is `run_query` rights for an agent. Read-only + approval gate + pre-flight EXPLAIN before anything else.
- **Never connect a production database with candidate PII** until D17 (residency + PII review) passes.
- **Local or no-training model** for text-to-SQL over any sensitive schema.
- **hireui rungs (D16–D19) run behind hireui's CONSTITUTION** — I-2 (`agent-*` branch), I-8 (operator installs, not the agent), GitNexus-first; no LLM spend yet → design/spec, staging clones only.
- **Pin the version** (`v0.15.0`) for reproducibility; review the one-click MCP config it writes into your agent's config files before trusting it.
