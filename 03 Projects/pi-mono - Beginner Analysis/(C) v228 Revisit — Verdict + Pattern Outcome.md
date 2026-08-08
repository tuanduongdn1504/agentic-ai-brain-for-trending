# Pi (earendil-works/pi) — v228 Verdict + Pattern Outcome

**Wiki:** v228 · **REVISIT** of v36 pi-mono · **Date:** 2026-08-08 · **Routine:** v2.7
**Verdict:** **GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) STRONG keys the tier · (c) STRONG · (d) STRONG]** · **NO MINT** · counts **46/11 UNCHANGED** · §C live standalones **47 unchanged**.

---

## 1. The four criteria

**(a) FAIL — cleanly.** `earendil-works/pi` is owned by **Earendil Inc.** (venture-backed public-benefit corp, co-founder **Armin Ronacher**), lead author **Mario Zechner** — **not Anthropic**. Routine **§41 (v2.7)** is decisive: a "famous framework author" (Ronacher/Flask, Zechner/libGDX) is **not an (a)-rescue**. First `earendil-works`-org author → **#19 19a** first-institution data-point. No inference-rescue attempted; the tier keys on (b) per §31.

**(b) STRONG — keys the tier.** Pi **is** an open-source coding agent for software development = **Goal #1 dead-center** + the agent-substrate the vault studies; it runs **Claude first-class** (subscription + API key); it is directly pilotable as the operator's **Claude-Code alternative + multi-provider escape-hatch**, and it ships four **borrowable engineering playbooks** (supply-chain hardening, agent containerization, an evals discipline, vendor-neutral telemetry contracts). **STRONG-not-STRONGEST** = it is a **competitor/peer harness** (third-party; provider-agnostic — Claude one of ~30; the goal centers Claude specifically), not Anthropic substrate. This calibrates exactly to the coding-agent-product cluster, all of which keyed (b) STRONG: **Kilo Code v177 / grok-build v215 / openinterpreter v223**. **§40 is not even needed** — this is cleanly GOAL-ALIGNED on (b) alone.

**(c) STRONG — with honest caveats.** Source-verified maturity at `e47b8e3` / v0.84.1: a ~10-package **client/server-architected** TS monorepo (transport-neutral CBOR protocol + client + experimental server + pluggable session backends + a built-in evals harness + vendor-neutral telemetry), ~30+ providers with automatic model discovery, **the corpus's most disciplined supply-chain hardening** (pinned + `min-release-age=2` + shrinkwrap + `--ignore-scripts` + scheduled audit + lifecycle-script allowlist), three containerization patterns (Gondolin micro-VM / Docker / OpenShell), an honest SECURITY.md, biome/vitest/tsgo tooling, active external-contributor PR flow (~7700+), ~85K★. **Caveats:** still effectively **Mario-led** (now under Earendil — the v36 solo-bus-factor is reduced by a company but concentration remains); `pi-server` is **experimental**; **no built-in sandbox/permission system by design** (containment is on the user); **EN-only**; **MCP-excluded** (real friction for MCP-heavy workflows). A MODERATE reading is defensible if one weights the "competitor harness, not Anthropic substrate" framing more heavily — recorded, but STRONG holds (it's a mature, widely-adopted, Claude-first coding agent).

**(d) STRONG.** Rich placement — see §5.

**Net: GOAL-ALIGNED INCLUDE 3/4.**

---

## 2. Pattern outcome: **NO MINT** (revisit)

- **No new top-level pattern.** Max stays **#85** — not exceeded.
- **No new §C standalone.** Counts **46 top-level / 11 CONFIRMED Library-vocab UNCHANGED**; §C live standalones **47 → 47**.
- This is a **corpus-recursive REVISIT** — the 3rd in wiki history (after **v78 ECC↺v1**, **v185 agency-agents↺v18**). Its job is to (i) refresh the v36 record with the ownership move + architecture evolution and (ii) strengthen the patterns Pi anchors/touches, **not** to mint.

### 2.1 The candidate §C mint — DECLINED

A tempting new §C surface exists: **"Remotely-drivable open coding-agent runtime with a formal (CBOR) wire protocol + pluggable session backends"** (the `pi-protocol`/`pi-client`/`pi-server`/`session-backends` spine). It is arguably corpus-first in *that specific shape*.

**DECLINED**, for four reasons (the camofox v179 "don't draw the circle" + §28 anti-inflation discipline, applied to a revisit):
1. **It is a within-subject architecture evolution, not a new capability class the corpus lacks a home for.** Pi is already represented (v36, + the coding-agent-product cluster). Minting a fresh standalone *because a known subject added a client/server split* is the over-generalize error.
2. **Adjacency.** Remote-agent-session/bridge is adjacent to **devspace v171** §C ("self-hosted bridge that turns a hosted chat host into a local coding agent") and the **orchestration-platform §C** (Paseo v150 / ai-maestro v163). "Drivable over a wire" is a *feature/architecture*, not a distinct agent-capability the §C registry is missing.
3. **Revisits mint only on a genuinely-new corpus-first surface** (the v185 test: agency-agents *had become* a subagent-persona library the corpus lacked → mint; v78 ECC did *not* → no new top-level). Pi's coding-agent surface is well-represented and Pi is its OG.
4. **§28 + the recent-ships discipline** (v223/v224 "leaned MINT but recorded the NO-MINT alt + flagged to audit"; here the balance tips the other way): the honest call on a revisit is **NO MINT + record as a DEFERRED watch axis**.

→ **Recorded as a DEFERRED watch axis** ("remotely-drivable open coding-agent runtime / CBOR-wire-protocol remote sessions") and **flagged to the OVERDUE ~v221 audit**, which already carries the **coding-agent-products cluster** question (Kilo Code v177 / grok-build v215 / openinterpreter v223 / larksuite-cli v143 / CodePilot v161). Pi is the **OG member of that cluster** (v36, predating all) — the audit should reconcile the cluster *with Pi as the anchor* and decide (a) whether the cluster becomes a §C standalone and (b) Pi's tier label.

### 2.2 Instance-strengthening (the real revisit deliverable)

- **#18 Agent Runtime Standardization / MCP layer.** Pi's MCP-exclusion — logged at v36 as *"first T1-scale MCP-exclusion counter-evidence, watch for N=2"* — is now, at ~85K★, an **explicit, philosophy-backed, blog-defended stance** ("No MCP" + the "what if you don't need MCP?" essay) with an alternative primitive stack (CLI-tools-with-READMEs + Skills + extensions). This is the **corpus's strongest MCP-exclusion counter-pole**, standing against the MCP-heavy §C#23 code-graph family + the B1-MCP running set. Instance-strengthening, **not** a #18 refinement mint (the "MCP-optional-via-extension" sub-variant the v36 wiki proposed remains *watch*, not active — the corpus's MCP-adopters vastly outnumber the deliberate rejectors, so Pi is the notable pole, not evidence of an ecosystem shift).
- **#66 Supply-chain.** Pi is a rare **positive exemplar** — pinned deps + `min-release-age=2` + shrinkwrap + `--ignore-scripts` + scheduled `npm audit` + lockfile pre-commit gate + lifecycle-script allowlist + isolated release smoke-tests. The strongest supply-chain discipline observed in the corpus; a directly-borrowable playbook (see Pilot Menu B).
- **#69 Agent-era maintainer-gate.** `lgtm`/`lgtmi` + auto-close-new-contributors-by-default persist and are the pattern's anchor; still active at company scale.
- **#28 / #84 Multi-provider.** ~20+ → **~30+** providers + **automatic model discovery** + a model-catalog; Claude first-class. Instance-strengthening (NO N-bump on #84 — provider-agnosticism is inherited/native, not the ponytail v168 rule-file-generator mechanism).
- **#17 / #20 / #27 solo→company trajectory.** v36 recorded Pi as the corpus-first *"T1 monorepo-under-single-flagship"* solo archetype + a cross-domain-founder-equity #27 sub-path (libGDX → AI). v228 records the **next step: a solo OSS flagship absorbed into an open-core public-benefit corporation while staying MIT** — a corpus-first *trajectory* observation (recorded, **not** a new pattern; max #85). Watch for N=2 (another solo flagship acquired-but-kept-open) before any registration.

### 2.3 Corpus-recursive / secondary (NOT minted)

- **#57 downstream:** **llm-space v221** is built on + credits `pi-agent-core` → Pi is a *cited* corpus dependency (recorded at v221 as the #57; nothing to re-mint here).
- **Widely-cited harness:** Pi appears as a supported/cited harness in **cc-switch v73, open-design v83, i-have-adhd v225, openinterpreter v223**, the **harness-engineering** flagship, and the **adaptive-engineering-beyond-harness** memory. Cross-references, not recursions.
- **`@anthropic-ai/sandbox-runtime` dependency** (Gondolin) — a data-point (even the MCP-rejecting harness reaches for an Anthropic isolation primitive); not a pattern.

### 2.4 NON-claims

- **NOT #52** (~85K★ page-stated §37.4; the GitHub API is mocked here → velocity unestablishable).
- **NOT world-first / corpus-first coding-agent** (OpenHands v30 / AutoGPT precede; Pi itself was v36).
- **NOT #18 B1-MCP** (Pi ships no MCP server — it's the counter-pole).
- **NOT a new top-level pattern** (max #85).
- **NOT a fresh subject** (REVISIT of v36; no collision — no `pi`/`earendil` subject folder exists v201→v227).

---

## 3. Tier

**Coding-agent-product** (the Kilo Code v177 / grok-build v215 / openinterpreter v223 / larksuite-cli v143 / CodePilot v161 cluster). v36 label was **T1 "Agent-as-assistant."** Pi is the **OG member** (predating the whole cluster by 141+ wikis). Tier-label reconciliation is deferred to the overdue ~v221 audit (do not re-tier unilaterally on a revisit).

---

## 4. Counts / streak / ceiling

- **Counts:** 46 top-level patterns / 11 CONFIRMED Library-vocab — **UNCHANGED**.
- **§C live standalones:** 47 → **47** (NO MINT).
- **Streak:** v227 **GA:85 → v228 `GA:86 · OG:13 [7 ov]`** (9 consecutive GA post the v219 OG break). Under §40 this is simply GOAL-ALIGNED; no OFF-GOAL alternative needed (cleanly GA on (b) STRONG).
- **§35:** **CLEAR** — window {v226 GA, v227 GA, **v228 GA**} = 0 OG.
- **Overrides:** 0 consumed (goal-aligned per §31; §40 not invoked because (b) is STRONG not MODERATE).

---

## 5. (d) cross-references

Coding-agent-product cluster: **Kilo Code v177, grok-build v215, openinterpreter v223** (harness-emulation — a peer that *emulates* other harnesses, incl. minimal), **larksuite-cli v143, CodePilot v161, OpenHands v30**, AutoGPT · provider-routing cousins **cc-switch v73, DeepSeek-TUI v72** · remote-agent-bridge cousin **devspace v171** §C (opposite MCP stance) · **#57 downstream llm-space v221** (built on pi-agent-core) · the **harness-engineering** flagship + **adaptive-engineering-beyond-harness** (Pi as the minimal-extensible exemplar) · multi-provider/eval threads **prompt-eval, mosh-ai vendor-seam, CC-observability/OTel** · supply-chain #66 · MCP counter-pole vs §C#23 code-graph family + B1-MCP set.

---

*(C) Claude-generated 2026-08-08 under routine v2.7. Verdict produced INLINE + hand-verified per `feedback_wiki_verify_independently_check_collisions` (no workflow/subagent — the ~1MB shim overflows subagents; source hand-read from a real clone; ownership move independently WebSearch-confirmed; collision hand-grepped against the v227 tip tree). inflation_check HELD: 0 mints, max #85, counts 46/11 unchanged, §C 47 unchanged, candidate mint DECLINED + recorded as a DEFERRED watch axis, no N-bumps.*
