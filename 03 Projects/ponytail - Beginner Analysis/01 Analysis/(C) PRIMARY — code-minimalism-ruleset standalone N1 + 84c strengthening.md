# (C) PRIMARY — 1 NEW §C standalone (code-minimalism ruleset) + clean #84 84c strengthening (v168)

**Outcome:** the **v158 ai-token-monitor / v165 lazyagent shape** — a clean instance of an existing class **plus** one corpus-first capability standalone. ZERO new top-level patterns. **46 patterns / 10 Library-vocab CONFIRMED UNCHANGED.** Tracked PROVISIONAL surface ≈26 → ≈27 (+1 §C standalone).

## The mint — NEW Library-vocab §C standalone N=1

**"Quantified Anti-Over-Engineering / Code-Minimalism Agent-Behavior Ruleset (decision-ladder + review-tooling + agentic benchmark)."**

An opinionated, cross-harness ruleset whose function is to constrain an AI coding agent toward **less code**: a sequential **decision-ladder** (YAGNI → stdlib → native → installed-dependency → one-line → minimum-that-works) with explicit **NOT-lazy carve-outs** (validation / error-handling / security / accessibility / hardware-calibration), shipped with **review-tooling** (`/ponytail-review` delete-list, `/ponytail-audit` repo scan, `/ponytail-debt` marker ledger, `/ponytail-gain` scoreboard) and an **agentic LOC/token/cost/time benchmark** that measures the intervention's effect.

**Why CORPUS-FIRST:** no prior corpus subject is a **code-quantity** minimalism methodology. The nearest relatives are different *dimensions* of "make the agent produce less/cleaner output":
- **Anti-Slop-Design-Curation** (v81/v85 taste-skill, *"The Anti-Slop Frontend Framework"*) — OC-layer PROVISIONAL N=1 — is **design-aesthetics**.
- **voice-calibration personalization** (v108 humanizer / v138 khazix-writer; §C N=2) — its de-AI sub-flavor is **human-voice**, not code.
- **v75 impeccable** (27 anti-pattern rules, 14-harness) is the closest **SIBLING** — but it is **design-quality**, ponytail is **code-quantity**. **NOT counted as N=2** (different dimension). Recording it as N=2 would repeat the "generalize-the-definition-to-fit-the-2nd-instance" error the v158/v162 discipline warns against.

**Forming meta-theme (WATCH, do NOT pre-merge):** *"opinionated cross-harness rulesets that constrain the agent toward LESS"* spans code-quantity (ponytail) / design-aesthetics (taste-skill, impeccable) / human-voice (humanizer). The vault has historically tracked these dimensions **separately**; a future audit may decide whether they form one cluster. For now: ONE new standalone at the code-quantity dimension; the cross-dimension class is a watch.

**Filing:** registry `06` §C row added (rule-5 "filing is an ACT"). §28: **1 new standalone (≤2 cap honored).** Promotion-eligible at a genuine 2nd **code-minimalism** ruleset. Time-aware stale-watch (≥15 wikis AND ≥30 days, §39).

## Clean strengthening (NO mint) — Pattern #84 84c "Provider-Agnostic-By-Design"

Ponytail is a **premium 84c instance**: 14 declared platforms (Claude Code, Codex, Copilot CLI, Cursor, Windsurf, Cline, OpenCode, Gemini/Antigravity CLI, OpenClaw, Kiro, Aider, Zed, CodeWhale, Pi). Its distribution mechanism is a **hybrid** that strengthens both registered sub-sub-mechanisms:
- **84c.1 repo-stored** — 6 hand-maintained native rule copies (`.cursor`/`.windsurf`/`.clinerules`/`.agents` rules + `.github/copilot-instructions.md` + `.kiro/steering`) kept aligned by a **byte-for-byte drift-checker** (`scripts/check-rule-copies.js`) + a **7-rule-phrase-invariant validator**, **CI-gated** on every push/PR.
- **84c.2 CLI-generated** — the `.openclaw/skills/` package auto-generated from `skills/` via `scripts/build-openclaw-skills.js`, freshness-enforced by `tests/openclaw-skills.test.js`.

This continues the v71→v72→v73→v75→v76 84c arc. The **CI invariant-validation discipline** is a more rigorous take on multi-target alignment than v75 impeccable's plain repo replicas — recorded as an **observation**, not a mint. Filing: `02b` 84c instance-note.

## Clean strengthening (NO mint) — Library-vocab #12 LLM-routing artifacts

Ponytail generates/maintains the whole routing-artifact family in one repo: `AGENTS.md` + `.cursor`/`.windsurf`/`.clinerules`/`.agents` rules + `.github/copilot-instructions.md` + `.kiro/steering` + `.openclaw/skills` + `gemini-extension.json` + `.claude-plugin/plugin.json` + `opencode.json`. A high-density multi-artifact instance of CONFIRMED #12. Filing: `06` §A #12 anchor note.

## SECONDARY observations (NOT minted)

- **Pattern #83 83b methodology-disclosure** — a genuine instance (honest benchmark caveats: small n=4, Haiku-only, "floor not comprehensive proof," explicit recommendation to narrow the headline claim, cross-provider "picture flips" + reasoning-model cost increase; `/ponytail-gain` **forbids per-repo savings claims**). Instance-strengthening of CONFIRMED #83 at 83b; recorded, not minted.
- **Library-vocab #20 Token-Economy-Quantification** — *qualified-adjacent*: the agentic benchmark explicitly quantifies token/cost impact (−22% tokens, −20% cost), but it is **model-scoped** (Haiku-agentic; flips on reasoning models) and measures *intervention-effect* not *artifact-footprint* → recorded as a qualified instance with caveat, **not** a clean N+1 bump (anti-inflation; the verifier flagged narrower-not-broader applicability).
- **`ponytail-mcp` is a distribution surface, NOT Pattern #18** (REFUTED): a stateless, read-only MCP facade (`ponytail_instructions` tool + `ponytail` prompt resource, deterministic per-call, no persistent state) = another channel for the same ruleset, **not** a shared-backend service with runtime coordination. No #18 / no protocol-variant registration.
- **NO corpus-recursion — Pattern #57 does NOT apply** (REFUTED): ponytail cites **zero** corpus subjects (no impeccable, agent-skills-standard, Anthropic skills, Karpathy, LLM-wiki). Only external references = `tiangolo/full-stack-fastapi-template` (benchmark testbed) + `JuliusBrussee/caveman` (the agentic benchmark's control-arm skill — a cataloguing-adjacent minimalism skill, **not** conflated with ponytail).
- **page-stated ≈40k★ / 1.9k forks / 9 releases (Jun 12–16 launch burst)** — **NOT API-verified** (§37.4: env mocks the GitHub API); **creation date not shown** → age/velocity unestablishable → **explicitly NOT a Pattern #52 claim** (40k★ on a ~8-day-old repo would be extreme launch-week virality IF accurate, but it is unverifiable; in a mocked-API sandbox the figure may be synthetic).

## Why no new top-level pattern (the §28 discipline, applied against two over-reaching verifiers)

Two adversarial verifiers over-reached: one recommended minting a brand-new top-level **Pattern #86** ("Deterministic-Decision-Ladder Code-Generation Constraint"); another filed ponytail into a **"Pattern #88 Anti-Slop-Curation, 88d sub-mechanism."** Both rejected at synthesis after verification:
- **No Pattern #86–#99 exists** in `_patterns/` (the highest registered numbers are ≤#85) — minting a new top-level pattern for a single N=1 subject is exactly the over-minting §28 guards against.
- **No top-level Pattern #88 exists.** "Anti-Slop-Design-Curation" is an **OC-layer PROVISIONAL track at N=1** (v81/v85), explicitly registered *for later evaluation* as a separate pattern OR Library-vocab item — and it is *design-aesthetics*, not code-quantity. Filing ponytail as "88d" would have anchored to a confabulated pattern.

The disciplined home for ponytail's genuinely-novel content is therefore **one Library-vocab §C standalone (code-minimalism ruleset)**, with the distribution structure recorded as a **clean #84 84c strengthening** — exactly the v158/v165 "clean instance + 1 corpus-first standalone" shape.

## Filing checklist (rule-5)
- `_patterns/06-library-vocab-registry.md` §C: NEW standalone row added; §A #12 + #20 anchor notes; §F count updated.
- `_patterns/02b-confirmed-patterns-v42-plus.md`: Pattern #84 84c ponytail instance-note (premium 14-platform hybrid 84c.1+84c.2).
- `_state/03c-projects-…md`: v168 entry appended.
- `CLAUDE.md` shim: Pattern Library state head + Weekly Update + streak + project index updated.
