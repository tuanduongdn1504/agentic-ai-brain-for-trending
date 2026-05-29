# (C) Pattern Library OT proposal — Cost-Discipline Enforcement Primitive

> **Status:** PROPOSAL — awaiting operator decision to fold into canonical Pattern Library state.
> **Date:** 2026-05-29
> **Author:** Claude (wiki-maintainer role)
> **Type:** Observation-Track registration (NOT active candidate — see §6 classification rationale)
> **Trigger:** Operator-elected wiki→product→wiki loop ("file the cost-discipline architecture back to the wiki"). First Pattern Library contribution sourced from the operator's own product rather than a corpus wiki subject.

---

## 1. TL;DR

The corpus (v1–v61) contains **zero subjects that implement monetary-spend-cap *enforcement* as a dispatch-time primitive** — verified by corpus-grep (§4). The operator's own product, **Command Center** (`build-your-own-dashboard-prompt`), implements exactly this across three releases (§5). Because Command Center is a *non-corpus* source, this cannot be a standard cross-wiki candidate (which requires ≥1 corpus *presence* observation, of which there are zero). It is registered as an **Observation-Track**: a verified corpus-*absence* plus one motivating *non-corpus* instance, wired to **promote to candidate** the moment any future wiki subject implements spend-cap enforcement.

## 2. Why this exists

Per the vault prime directive ("file valuable answers back into the wiki") and GOALS.md's acknowledged "pattern-observation ≫ operator-deployment imbalance," this is the first contribution flowing *from* the operator's product *into* the wiki — inverting the usual external-subject→wiki direction. The valuable insight: the corpus has been mined for 61 wikis without surfacing a cost-discipline pattern, while the operator was independently building one.

## 3. Provenance & admissibility caveat (read first)

**Command Center is NOT a corpus wiki subject.** All 76 existing patterns derive from external subjects analyzed as wikis. This observation's only *presence* evidence is the operator's own product. That is explicitly labeled here and must not be laundered into corpus-derived evidence. The **corpus contribution** of this OT is the *absence* (a legitimate, verifiable corpus observation — see the Pattern #57 BIDIRECTIONAL-ABSENCE precedent at v60); Command Center is cited as the *non-corpus N=1* that motivates a forward-watch, not as a corpus data point.

## 4. The corpus observation — VERIFIED ABSENCE

**Method:** corpus-grep across project-entry chapter files (`_state/03a`/`03b`/`04`/`05`, covering v1–v61; v62 not yet chaptered) + `_patterns/*.md`.

**Strict regex** (`cost.cap | cost.budget | token.budget | spend.cap | daily.cost | budget.*usd | cost.limit | spend.limit | cost.control | cost.discipline | cost.guard | cost.ceiling`): **0 hits.**

**Looser cost/budget/token sweep** surfaced only ADJACENT-but-DISTINCT concepts — none of which is spend-cap enforcement:

| Subject | Concept found | Why it is NOT this pattern |
|---|---|---|
| gsd-2 (v54) | `token_profile: budget\|balanced\|quality` (40-60% savings); cost/token bar charts in HTML reports | Token *optimization* + cost *visibility/reporting* — no enforcement gate that refuses work at a $ ceiling |
| claude-hud / statusline (v35) | "context-budget visibility" | Context-*window* budget *display* — not monetary, not enforced |
| autoresearch / Karpathy (v29-ish) | "5-min experiment budget"; "hard budget" | *Time*-boxed experiment budget, not monetary spend-cap |
| Storm Bear self-note (v29-ish) | "no budget enforcement" listed as a Storm Bear *gap* vs Karpathy | The vault already recognized this gap in its own tooling — corroborates the absence |

**Sharpened claim (falsification-resistant):** No corpus subject implements **monetary-spend-cap enforcement** (refuse-to-dispatch at a $ ceiling). The corpus has *visibility*, *optimization*, and *time-box* approaches only.

## 5. The non-corpus N=1 instance — Command Center cost-discipline architecture

Three releases, one architectural signature (all version facts verified against `CHANGELOG.md`):

1. **Global daily cost cap (v0.2.0)** — `MISSION_CONTROL_DAILY_COST_CAP_USD`. Dispatcher refuses to claim tasks once today's spend ≥ cap. Post-hoc shape (operator can over-spend by at most one in-flight task). Safety floor.
2. **Cost-source disambiguation (v0.6.0)** — every spend tagged `api_pool` (real $) / `max_sub` (notional subscription) / `unknown` / `codex_api` (reserved). Enforcement counts **api_pool only** — the cap reads real dollars, not notional subscription usage. This is the conceptual core: *not all "cost" is enforceable cost.*
3. **Per-skill daily budgets (v0.6.7)** — `skills.daily_budget_usd`; `NULL`=unlimited / `0`=blocked / `>0`=post-hoc cap. Sums api_pool spend across all accounts (per-account × per-skill matrix deliberately deferred to v0.7+). Global cap still wins when both could trigger.

**Enforcement chain (dispatcher pre-claim order):** back-pressure → hard risk gate → **global daily cap** → **per-skill budget** → autonomy gate.

## 6. Classification rationale — why Observation-Track, NOT candidate

Per the Library's own definitions:
- **Candidate** = "1-2 observations OR confined to single tier" — implies ≥1 *corpus* observation of the pattern's *presence*. **Count of corpus presence-observations = 0.** Registering as a candidate would misrepresent N.
- **Observation-Track** = "observation worth tracking but not active candidate; may evolve to candidate or stay as historical observation." Exact fit: a verified absence + one non-corpus instance + a forward-watch.

This is the disciplined landing. It still lives *in* the Pattern Library (honoring "file back to the wiki") and has a defined promotion path.

## 7. Overlap pre-check (<70% required for standalone)

- **Pattern #13 Autonomy-Framing Spectrum** — autonomy is an organizational *design* choice (human-amplification ↔ autonomy-max). Cost-discipline is a *resource-enforcement* mechanism, orthogonal. <70%.
- **Pattern #18 Agent Runtime Standardization** — protocol/format translation layers. No cost dimension. <70%.
- **gsd-2 token_profile** — optimization (reduce tokens), not enforcement (refuse at $ ceiling). Distinct mechanism class. <70%.

No >70% overlap with any existing pattern → standalone OT justified.

## 8. Forward-watch / promotion path

- **Corroboration trigger:** any future wiki subject implementing monetary-spend-cap *enforcement* (refuse-to-dispatch at a $ ceiling) — distinct from token-optimization or cost-visibility.
- **At N=1 corpus presence** → promote OT to active candidate (then the standard candidate discipline applies).
- **At N=2 structural** (2 distinct orgs with the same enforce-at-ceiling signature) → promotion-eligible under criterion #2.
- **Stale-check window:** +5 wikis from fold-in (per the v27 N=1 stale-flag protocol).
- **Retirement-check window:** +10 wikis. If no corpus subject ever corroborates, the OT stays as a *historical observation* documenting that cost-enforcement was a product-led, not corpus-led, primitive in this era.

## 9. Falsification note

This absence claim was corpus-grep-verified (§4), explicitly because the Pattern #57 BIDIRECTIONAL-ABSENCE OT was *rejected* at the v60 audit when a corpus-grep found 53 falsifying files. If a future corpus-grep surfaces a spend-cap-enforcement subject missed here (e.g., in v62+ or in chapter content not matched by the regex), downgrade/correct this OT per the audit-layer fact-verification protocol. The claim is deliberately narrowed to *monetary-spend-cap enforcement* precisely so it survives the looser cost/budget mentions that DO exist (§4 table).

## 10. Proposed canonical state entries (for operator to fold in — NOT yet applied)

If accepted, fold these into PATTERN_LIBRARY.md state + the relevant `_patterns/` chapter (operator authority — ask-before-editing-existing-notes):

- **Observation-tracks: 6 → 7.** New OT:
  > **OT — Cost-Discipline Enforcement Primitive (corpus-absence + non-corpus N=1).** Corpus (v1–v61) implements zero monetary-spend-cap *enforcement* primitives (grep-verified 2026-05-29; adjacent token-optimization/cost-visibility/time-box concepts exist but are distinct). Operator product Command Center implements enforce-at-$-ceiling across v0.2.0 global cap + v0.6.0 cost-source disambiguation + v0.6.7 per-skill budgets. Non-corpus N=1 — NOT a candidate (zero corpus presence). Promote to candidate on first corpus subject implementing spend-cap enforcement. Stale-check +5 wikis / retirement +10. First wiki←product contribution in corpus history.

- **Provenance flag:** mark as the corpus's first **product-sourced** observation — a new evidence-provenance class (corpus-subject vs operator-product) worth noting for routine v2.2 if a second product-sourced observation ever appears.

---

End of proposal. Doc-only; no canonical Pattern Library file touched. Awaiting operator decision (§10).
