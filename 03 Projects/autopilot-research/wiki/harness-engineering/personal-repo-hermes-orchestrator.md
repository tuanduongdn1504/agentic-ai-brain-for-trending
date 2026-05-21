# Personal-repo extension — orchestrator-mediated cross-vendor (Hermes + Codex + Claude)

> **Source:** Nemanja Mirkovic — [Codex Builds. Claude Reviews. Hermes Agent Runs It.](https://www.youtube.com/watch?v=O-PEeD7fymo), 2026-05-20, 13:48, 2175 views at fetch
> **Raw:** `raw/2026-05-21-nemanja-codex-claude-hermes-orchestrator-transcript.md`
> **Compiled:** 2026-05-21
> **Status:** N=1 single-source extension to [[personal-repo-overview|individual-scale layer]]; not a new anchor. Distinct contribution: **orchestrator-mediated cross-vendor composition** with **subscription-arbitrage motivation**. Sibling to [[personal-repo-router-multimodel]] (router-mediated cross-vendor).

---

## The pattern in one line

> A 3rd-party agent (Hermes) acts as the operator's single touchpoint, delegating BUILD to Codex CLI as a subprocess and REVIEW to Claude Code CLI as a subprocess, looping until spec-match, with **each worker CLI preserving its native subscription auth instead of going through Hermes' billing layer**.

The mechanism is **process-level subprocess delegation through an external orchestrator**, not in-process model routing. This distinguishes it cleanly from [[personal-repo-router-multimodel|the router-mediated variant]].

---

## Architectural distinction — 3 axes vs prior sources

| Axis | [[personal-repo-router-multimodel|howznguyen 2026-05-19]] | This video (Nemanja 2026-05-20) | [[anthropic-large-codebases-anchor|Anthropic anchor 2026-05-14]] |
|---|---|---|---|
| Mediator | Router process (9Router) | Orchestrator agent (Hermes) | None — single-agent (Claude Code) |
| Mechanism | In-process model routing via Claude Code's 3-slot config | Out-of-process CLI subprocess delegation | First-party 7-component decomposition inside one agent |
| Cross-vendor surface | Opus (Kiro) + GPT-5.5 (Codex) appearing as opus/sonnet slots | Codex CLI + Claude Code CLI both invoked as subprocesses | Single vendor |
| Roles | Supervisor (Opus) + Sub-agent default (GPT) | Orchestrator (Hermes) + Builder (Codex) + Reviewer (Claude) | Implicit via subagents |
| Native ecosystem retained? | Partial (Claude Code's plugins/MCPs but model is foreign) | **YES — both CLIs keep their full ecosystem** (Claude's plugins/skills/MCPs + Codex's tools) | Yes (one ecosystem) |
| Subscription billing | Pay router + provider subs | **Native CLI subs for both Codex and Claude; Hermes orchestrates without consuming API balance** | Single sub |
| Operator touchpoints | 1 (Claude Code) | 1 (Hermes) | 1 (Claude Code) |

The orchestrator-mediated approach is **the only N=1 variant in the corpus that preserves both worker harnesses' native ecosystems intact**. Router-mediated swaps the model but inherits Claude Code's harness; orchestrator-mediated lets each worker stay a full harness.

---

## Load-bearing innovation: *conditional* subscription-arbitrage

Host's stated reason for the architecture (not just role-splitting):

> "Codex actually works well with Hermes, but Claude doesn't. So, if you want to use Claude with your subscription, and if you connect it through a Hermes profile, then it'll just pull your extra balance. It'll not use the actual subscription limits and credits."

Interpretation: Hermes Profiles bill through Hermes' API-key path; Hermes-invoked-CLI bills through the CLI's own subscription auth. The video does not name the underlying mechanism, but the practical implication asserted is concrete: **wrapping CLIs as subprocesses bypasses the orchestrator's billing layer entirely**, so Anthropic Pro / ChatGPT Plus subscriptions stay the cost ceiling.

This is the **first source in the autopilot wiki corpus where subscription-billing geometry is the architectural driver**, not a side observation. Prior sources optimized for capability split or context preservation; this one is cost-first.

### Verification (2026-05-21) — directionally correct, operationally fragile

The billing claim was independently verified against 6 sources (Anthropic Help Center, Hermes-agent issue #12905, MindStudio analysis, Hermes' own bundled Claude Code SKILL.md, Claude Code issue #37686, Claude Code issue #20976) and corroborated by YouTube comment evidence on the source video. See `output/(C) 2026-05-21-subscription-billing-verification.md` for the full audit.

**Confirmed:** Hermes Profile (Anthropic OAuth provider) **does not** consume Pro/Max subscription quota — it routes to a separate `extra_usage` billing pool that is "effectively empty for most users."

**Caveated:** CLI-subprocess invocation **can** preserve subscription quota, but only when **3 conditions hold simultaneously**:
1. `ANTHROPIC_API_KEY` is NOT set in the environment Hermes inherits.
2. The reviewer is NOT invoked via `claude -p` headless mode (per documented `-p`/`--bare` API-key dependency).
3. The `claude` CLI was previously OAuth-logged-in.

If any one condition fails, the CLI silently prefers API billing and the orchestrator burns API credits at standard rates. A real Max subscriber was charged $1,800 in 2 days hitting exactly this footgun (Claude Code issue #37686).

**Critical: the SOUL-claudereviewer.md profile in Nemanja's companion repo explicitly prescribes `claude -p`** — see [[hermes-goal-mechanics]] for the verbatim invocation. This means **adopting the published reviewer profile triggers condition 2 failure by design.**

**Host's actual mitigation** (verified from YouTube comments 2026-05-21): Nemanja set Anthropic "extra usage" billing cap to $0 in his account. This is an **operational hard-cap**, not architectural subscription preservation. A pilot must apply the same cap. Independent commenter `@kikserthg233` raised the technical objection: *"claude -p will be billed same as if api is used."* — and Nemanja's response was the $0 cap, not a rebuttal.

The cost advantage is real but **not automatic** — it requires both environment hygiene AND a billing-cap safeguard. Treat the architecture as "free-lunch with operator-installed safety net" rather than "free-lunch by construction."

---

## Components shipped (per host)

- **Hermes orchestrator** with built-in `/goal` command (= "Ralph loop, which runs internally in Hermes agent" per host's prior video).
- **Two Hermes skills**, one for Codex CLI and one for Claude CLI — "it knows exactly how to use these two CLIs."
- **`coder` and `reviewer` profiles** — specialized agents instructed to use the CLI rather than Hermes' native tools/models. Profiles act as triggers for subprocess invocation. (Contents not shown in video; host offers to attach in comments.)
- **Built-in Kanban app** for task/subtask tracking — visible to operator mid-loop, but task assignment lagged in the demo.
- **Mid-loop vision check** — Hermes uses vision to analyze rendered pages before declaring done.
- **Final verification** by Hermes against the original spec file.

---

## Demo run characteristics (Kanban Next.js + SQLite)

| Aspect | Observed |
|---|---|
| Build model | Codex CLI fallback **GPT-5.5** (host: anomaly — usual default unclear) |
| Review model | Claude Code CLI, **Sonnet** (host explicitly rejects Opus: *"I don't use Opus cell"*) |
| Loop terminator | Spec-match + visual check pass |
| Outcome | Functional Kanban app with working drag-and-drop, card create/edit/delete |
| Comparison baseline | "Much better than the Ralph loop one" (plain Ralph = Codex 5.5 alone) |
| Operator-attended time | Step away 1-2 hours, return either done or blocked |
| Unresolved anomalies | Codex `/go` unavailable; Kanban cards initially unassigned |

The host's comparative claim — orchestrator-mediated trio outperforms single-model Ralph loop — is **N=1 anecdotal**. No metrics, no repetitions, no controlled variation.

---

## Mapping to [[core-claims|harness-engineering core claims]]

| Lopopolo claim | This source's evidence |
|---|---|
| #1 Humans steer, agents execute | **Strengthens** — operator only types `/goal <prompt>`; rest is autonomous |
| #2 Pre-merge review is wasted | **Mixed** — Claude reviews Codex output **inside the loop** (pre-handoff), which IS pre-merge review BUT done by an agent, not a human. Reinterprets the claim: human pre-merge review is wasted, but agent pre-merge review is the architecture |
| #4 Throughput scales with parallel agents | **Silent** — sequential build→review loop, no parallelism shown |
| #6 Skills > prompts | **Strengthens** — Hermes ships pre-built skills for Codex and Claude CLIs; the skills are what make orchestration tractable |
| #7 Adversarial evaluation | **Strengthens** — explicit BUILDER vs REVIEWER role split is exactly Pattern #76 territory (Storm Bear corpus) |
| #8 Ralph loop primitive | **Strengthens** — `/goal` is named explicitly as Ralph loop |

Net assessment: 5 strengthening signals, 1 reinterpretation, 1 silent. Consistent with the individual-scale layer broadly.

---

## What's load-bearing vs what's flavor

| Load-bearing | Flavor |
|---|---|
| Subprocess delegation preserving native auth (cost) | Hermes specifically (any orchestrator could fill the slot) |
| BUILDER/REVIEWER role split inside the loop | Hermes' specific Kanban UI |
| Pre-built skills for each worker CLI | Vision-based visual check (nice-to-have) |
| `/goal` = first-class Ralph-loop primitive | The Next.js+SQLite demo (substitutable) |
| Spec-match as loop terminator | The specific model picks (GPT-5.5 + Sonnet) |

The pattern would survive Hermes being replaced by any orchestrator that (a) can shell out to CLIs and (b) ships skills for the workers. The pattern would not survive losing native CLI auth — that's the cost claim's whole basis.

---

## Gaps / unverified claims (research surface)

1. **Subscription-billing claim — VERIFIED 2026-05-21 with caveats.** Hermes Profile does route to a separate `extra_usage` pool (not subscription). CLI-subprocess CAN preserve subscription, but only under 3 simultaneous environment conditions; if any fails, API billing kicks in silently. Full audit in `output/(C) 2026-05-21-subscription-billing-verification.md`. Implication: the pattern generalizes to any subprocess-wrapping orchestrator, but ONLY with env-hygiene discipline.
2. **No corroborating source on Hermes yet** in the autopilot wiki. This is the first ingest.
3. **No comparison to [[personal-repo-router-multimodel|router-mediated]] in either direction.** Worth a Tier-A pilot run: same task, both architectures, measure quality + cost + operator-time.
4. **Codex `/go` anomaly** — host flagged, didn't investigate. Could indicate Codex CLI feature gaps when invoked as subprocess vs interactive.
5. **Generalization claim ("any workflow")** is asserted, not demonstrated.
6. **3rd-party-wrapper vendor-platform risk.** Hermes depends on stable Codex CLI + Claude Code CLI APIs. Mitigation strategy not discussed.
7. **No CLAUDE.md / agents.md hierarchy** discussion — does Hermes' orchestration override each worker's project memory? Unclear.

---

## Relationship to Storm Bear Pattern Library

This source is candidate evidence for **two** active patterns in the parent corpus:

- **Pattern #76 Adversarial Subagent Review Architecture** (registered v63 audit 2026-05-07; N=1 baseline = cc-sdd v61). This video adds a structurally distinct N=2 evidence point: the adversarial review here is **across-vendor and across-CLI**, not within a single framework's subagent system. Whether it qualifies as same-pattern-N=2 or a sibling pattern depends on Pattern Library audit interpretation at next mini-audit cadence.
- **Pattern #18 Layer 2 cross-vendor-bridge** (3rd sub-archetype at v62 codex-plugin-cc). This is a 4th sub-archetype: **3rd-party orchestrator wrapping rival vendor CLIs as subprocesses**, distinct from (a) runtime API-protocol translation (v60 free-claude-code), (b) install-time skill-format translation (v61 cc-sdd), and (c) plugin-bridge published by one vendor for the other's platform (v62 codex-plugin-cc).

Flag for inclusion in `output/promotion-candidates.md` once N≥2 corroborating sources land on Hermes specifically OR on orchestrator-mediated cross-vendor more broadly.

---

## Cross-references

- [[personal-repo-overview]] — individual-scale layer overview
- [[personal-repo-router-multimodel]] — sibling cross-vendor pattern via router instead of orchestrator
- [[personal-repo-patterns]] — 12 individual-scale techniques (sub-agents technique closest cousin)
- [[personal-repo-vs-org-scale]] — Lopopolo axis-by-axis comparison
- [[anthropic-large-codebases-anchor]] — first-party 7-component decomposition (note: this video sits outside that single-agent frame entirely)
- [[helpline-worked-example]] — worked-example for the single-vendor variant
- [[tejas-kumar-anchor]] — 5-component harness decomposition; useful lens for asking "which Hermes components map to which primitives?"
- External: [[external|Storm Bear v62 codex-plugin-cc wiki]] for cross-vendor cooperation observation (different mechanism stratum)
- External: [[external|Storm Bear Pattern #76 / Pattern #18 Layer 2]] for pattern-library mapping
