# Cluster 2 — Contributor-facing docs (CLAUDE.md + AGENTS.md + PLAN.md)

## CLAUDE.md / AGENTS.md identity discipline

CLAUDE.md fetches with content: `IMPORTANT: Ensure you've thoroughly reviewed the AGENTS.md file before beginning any work.`

AGENTS.md opens with: `> This file is identical to CLAUDE.md. Keep them in sync.`

**Cross-wiki observation: corpus-first explicit AGENTS↔CLAUDE sync-discipline-via-comment.** Most prior CLAUDE.md/AGENTS.md repos (Pattern #22) ship one or both files but rarely declare sync-discipline overtly. free-claude-code has CLAUDE.md as a 1-line redirect + AGENTS.md as canonical with sync-comment header. **Sub-variant of Pattern #22 22c (governance-file-sync-discipline-via-explicit-comment).**

## AGENTS.md content (faithful summary, ≤30-word displacive limit)

The file lays out:

1. **Coding environment requirements** — uv 0.x + Python 3.14 + ruff py314 + ty type-checker + Pytest + 5 mandatory CI checks (format / check / type-check / pytest / smoke)
2. **Identity claim** — "expert Software Architect and Systems Engineer" framing; goal stated as "zero-defect, root-cause-oriented engineering"
3. **Architecture principles** — 9 enumerated principles: shared utilities in neutral core / DRY / encapsulation / provider-specific config isolation / no dead code / performance discipline / platform-agnostic naming / no type-ignores / complete migrations / max test coverage with smoke-test preference
4. **Cognitive workflow (5 steps)** — ANALYZE → PLAN → EXECUTE → VERIFY → SPECIFICITY → PROPAGATION
5. **Summary standards** — 4-section template ([Files Changed] / [Logic Altered] / [Verification Method] / [Residual Risks])
6. **Tools preference** — built-in (grep, read_file) over manual workflows

## PLAN.md content

Architecture spine: `config → providers → api`, with `core.anthropic` neutral foundation.

5 primary domains:
- **api/** — HTTP routes, orchestration, model routing, authentication
- **providers/** — upstream adapters, request translation, rate limiting, error mapping
- **messaging/** — Discord/Telegram, command handling, session persistence
- **cli/** — Claude subprocess management, package entrypoints
- **config/** — environment-backed settings, logging

Import-boundary rules (encoded constraints):
- `api/` may import only `providers.base`, `providers.exceptions`, `providers.registry` (facade pattern)
- `core/` isolated from all downstream packages
- `messaging/` cannot import `api`, `cli`, `smoke`

Testing discipline:
- Default CI = deterministic unit tests
- Live smoke tests require `FCC_LIVE_SMOKE=1` env flag
- Smoke tests may skip ONLY on `missing_env` or `upstream_unavailable` (no arbitrary skips)
- ASGI factory: `api.app:create_app` for production deployment

## Cluster-level corpus-first observations

| # | Observation | Cross-wiki implication |
|---|---|---|
| 1 | AGENTS.md identical-to-CLAUDE-with-sync-comment-header | Pattern #22 22c sub-variant explicit-sync-discipline; corpus-first observation |
| 2 | "Expert Software Architect and Systems Engineer" identity claim WITHOUT methodology citation | Pattern #19 archetype-4 first-mover-claims-authority-without-methodology-lineage variant; sister to v59 AutoGPT first-mover-no-lineage; N=2 STRUCTURAL within Pattern #19 archetype-4 family |
| 3 | 5 mandatory CI checks (format / lint / type-check / unit-test / smoke) | Pattern #12 Governance-Depth solo-medium-governance data point; non-EXTREME but more disciplined than typical solo-T4 |
| 4 | Encoded import-boundary rules in PLAN.md | Architectural-discipline-via-prose corpus-first observation; possibly observational-track candidate |
| 5 | Smoke-test-as-required (FCC_LIVE_SMOKE flag) | Pattern #8 Research-Benchmark adjacent — empirical-validation-via-smoke at T4 (vs Pattern #8 SWE-bench at T4 claude-context v40) |

## Architectural-discipline observations

PLAN.md encodes import boundaries as explicit prose (not just code). This is **architectural-discipline-via-encoded-rules** — a sub-variant of Pattern #12 governance-depth where governance content is *architecture rules*, not just process rules. **N=1 observational at v60.** Companion to Pattern #69 EXTREME-tier governance maximalism but at YELLOW/medium scale.

## Cross-references

- Pattern #22 AGENTS.md sub-variants: claude-howto v32 (TS) / spec-kit v17 (corporate) / aidevops v47 / OpenSpec v58
- Pattern #19 archetype-4 first-mover-no-lineage: AutoGPT v59 (paradigm-foundational), free-claude-code v60 (utility-tool-no-methodology-citation) — N=2 STRUCTURAL but distinct sub-types (corpus-historical-foundational vs utility-no-citation)
- Pattern #12 Governance-Depth: claude-hud v35 + ruflo v42 (heavy-solo) vs free-claude-code v60 (medium-solo) — refinement evidence

## Verbatim short quote (≤15 words)

> "This file is identical to CLAUDE.md. Keep them in sync."

(AGENTS.md header — corpus-first explicit sync-discipline declaration.)
