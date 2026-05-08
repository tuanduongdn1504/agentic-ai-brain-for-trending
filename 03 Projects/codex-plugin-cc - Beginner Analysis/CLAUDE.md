# codex-plugin-cc — Beginner Analysis

> **Subject:** [`openai/codex-plugin-cc`](https://github.com/openai/codex-plugin-cc) — *"Use Codex from Claude Code to review code or delegate tasks."*
> **Wiki version:** v62
> **Build date:** 2026-05-08
> **Routine:** `llm-wiki-routine-v2.1` (Storm Bear vault)

---

## Phase 0 — Probe summary

### 12-axis classification

| Axis | Value |
|------|-------|
| **Tier** | **T4 (Bridge — competitor-platform-bridge-as-plugin: Codex platform ↔ Claude Code platform)** |
| **Archetype** | Corporate-official (OpenAI org; corpus 2nd corporate-org after Microsoft spec-kit v17 + markitdown v28; **CORPUS-FIRST competitor-cooperation observation** — OpenAI publishing plugin FOR Anthropic Claude Code rival platform) |
| **Scale tier** | medium (17.8K stars / 1K forks / 59 watchers / 104 open issues / 26 commits — high stars-per-commit ratio = recent viral attention; v1.0.4 latest 2026-04-18) |
| **Primary lang** | JavaScript 100% (npm-distributed plugin) |
| **Packaging tool** | Claude Code plugin marketplace (`/plugin marketplace add openai/codex-plugin-cc` + `/plugin install codex@openai-codex`) |
| **Origin story** | Corporate-strategic (OpenAI extends presence into competitor's IDE ecosystem) |
| **Methodology** | NONE explicit (no SDD / BMM / TDD); review-augmentation-shaped |
| **Governance file count** | 4 (README + LICENSE + NOTICE + CHANGELOG) |
| **Agent/skill count** | 7 slash commands (`/codex:review`, `/codex:adversarial-review`, `/codex:rescue`, `/codex:status`, `/codex:result`, `/codex:cancel`, `/codex:setup`); plugin structure includes agents/ + commands/ + hooks/ + prompts/ + schemas/ + skills/ subdirectories |
| **i18n coverage** | EN-only |
| **Intellectual influence cited** | None explicit; LLM-as-judge research patterns (adversarial-review framing) implicit |
| **Agent platforms supported** | 1 (Claude Code only; bridges to Codex backend via Codex app server + local authentication) |

### Tier placement decision

**T4 (Bridge — competitor-platform-bridge-as-plugin).**

Justified by:
- Subject is plugin INSIDE Claude Code (host platform) that bridges TO Codex (different platform owned by OpenAI)
- Function = cross-platform integration; not standalone agent (T1) or service (T2)
- 2-axis sub-taxonomy formalized at v60 audit: content-transformation (N=8 prior T4 entrants) vs protocol-translation (free-claude-code v60 N=1). codex-plugin-cc is **NEW T4 sub-archetype**: cross-vendor-tool-bridge-as-plugin (3rd axis emerging).

**Alternative considered:** T1 Augmentation (lives inside Claude Code surface). Rejected — surface vs function: surface in Claude Code, function = bridge to Codex platform. Bridge framing more honest.

### Phase 4b primary routing mode

**🎯 PRIMARY: Counter-evidence-driven refinement of Pattern #76 Adversarial Subagent Review Architecture**

Pattern #76 was registered N=1 stale-flagged at v63 EARLY mini-audit (1 wiki ago) with cc-sdd v61 evidence. Required for promotion: 2+ frameworks with adversarial-by-design subagent role separation as documented architectural primitive.

**codex-plugin-cc `/codex:adversarial-review` analysis:**

| Dimension | cc-sdd v61 (Pattern #76 N=1 baseline) | codex-plugin-cc v62 (potential N=2?) |
|---|---|---|
| **Reviewer role** | Separate `kiro-review` subagent (distinct from implementer `kiro-impl`) | **SAME review function** with adversarial framing |
| **Implementer role** | Separate (`kiro-impl` autonomous mode) | N/A (no implementer-role separation; review-only plugin) |
| **Auto-debug-on-rejection loop** | Yes (`kiro-debug` returns ROOT_CAUSE/CATEGORY/FIX_PLAN/NEXT_ACTION) | NO (review output goes back to user, not auto-debug pipeline) |
| **Fresh-evidence completion gate** | Yes (`kiro-verify-completion`) | NO (no completion verification primitive) |
| **Mechanism type** | **Architectural primitive (separate role)** | **Prompt-framing variant (reframed prompt within same function)** |

**Verdict:** codex-plugin-cc adversarial-review is **NOT N=2 evidence for Pattern #76 architectural-primitive scope.** It IS evidence for a distinct sub-mechanism: "adversarial-review-as-prompt-framing variant" (different category — prompt-engineering vs architectural).

**Counter-evidence-driven refinement candidate:** Pattern #76 scope NARROWS to "adversarial-by-design role separation as architectural primitive specifically — not adversarial-framed review prompts within same review function."

**Distinct N=1 candidate (sister to Pattern #76):** "Adversarial-review-as-prompt-framing variant" — at codex-plugin-cc v62 N=1 stale-flagged. Distinguished from Pattern #76 by mechanism type (prompt-engineering vs role-separation).

### Secondary routing modes

- **CORPUS-FIRST competitor-cooperation observation** — OpenAI publishing FOR Anthropic Claude Code rival platform; Apache-2.0 license; unprecedented cross-vendor plugin direction in corpus (no prior wiki had OpenAI publishing for Claude Code or Anthropic publishing for Codex)
- **T4 sub-taxonomy 3rd axis** — competitor-platform-bridge-as-plugin (distinct from content-transformation N=8 + protocol-translation N=1 prior T4 sub-types; v60 audit T4 2-axis becomes 3-axis)
- **Pattern #59 Claude Code Plugin Marketplace Native — corporate scale strengthening** (was OMC v27 solo + claude-hud v35 solo; now OpenAI corporate scale = N=3 corporate-included)
- **Pattern #19 corporate-strategic archetype N=3 strengthening** (Microsoft spec-kit v17 + Microsoft markitdown v28 + OpenAI codex-plugin-cc v62; 3 corporate-org observations now; Microsoft 2-product cluster + OpenAI 1-product = bigger-tech-OAI/MS-cluster emerges)
- **Pattern #18 Layer 2 protocol-translation strengthening** — codex-plugin-cc bridges between OpenAI Codex platform and Claude Code platform; runtime-bridge mechanism (not install-time format translation like cc-sdd v61 N=1 candidate; not protocol-translation-proxy like free-claude-code v60 N=1)
- **Pattern #57 Recursive Corpus Reference check** — does codex-plugin-cc cite Claude Code or anthropics/skills explicitly? Need verification. Plugin marketplace install path implies citation of Claude Code as host; explicit textual citation TBD.

### Phase 0.9 Storm Bear meta-entity check

**STRICT 1-of-4 inclusion check:**

| Criterion | Result | Evidence |
|---|---|---|
| (a) Author archetype peer | **FAIL** | OpenAI corporate org, not solo-Asian-diaspora / solo-engineer-coach / solo-product-lead-non-coder / etc. Corporate-org dispositive FAIL on archetype-peer criterion |
| (b) Operational tool for vault | **PASS** (strong) | `/codex:adversarial-review` directly deployable for Storm Bear Claude Code workflow as code-review augmentation; pre-shipping review use case fits vault software development; ChatGPT subscription requirement notable but Storm Bear has it |
| (c) Methodology-influence-node | **PASS** (marginal) | Adversarial-review framing has methodology lineage in LLM-as-judge research (constitutional AI / red-teaming); broader methodology than narrow tool |
| (d) In-corpus reference | **PASS** (implicit-strong) | Claude Code is plugin host (every install command references it); explicit cross-corpus citation: codex-plugin-cc requires Claude Code = N=1 corpus-product-citation. Anthropics/skills protocol implicitly invoked via Claude Code plugin marketplace mechanism. |

**Decision: 3-of-4 PASS** ((b)+(c)+(d) clean; (a) fails) → **INCLUDE Storm Bear meta-entity** as 4th entity slot.

**Streak counter:** Storm Bear meta-entity 2-consecutive post-v60-RESTART → v62 advances to **3** (v60 PASS + v61 PASS + v62 PASS).

**7-instance Phase 0.9 post-amendment window:** v56 PASS / v57 PASS / v58 PASS / v59 SKIP / v60 PASS / v61 PASS / v62 PASS = **6 PASS / 1 SKIP = 86% INCLUDE rate** validates STRICT amendment regularly satisfiable; criterion (a) Pattern #19 corporate-archetype FAIL doesn't preclude INCLUDE when (b)(c)(d) all PASS.

---

## Pattern Library implications (preview — Phase 5 will register)

**Direct candidates / counter-evidence:**

1. **Pattern #76 Adversarial Subagent Review Architecture COUNTER-EVIDENCE-DRIVEN REFINEMENT** — narrows scope from "adversarial review" to "adversarial-by-design role separation as architectural primitive specifically." NEW sister sub-variant candidate "adversarial-review-as-prompt-framing variant" N=1 stale-flagged.
2. **CORPUS-FIRST competitor-cooperation observation** — OpenAI plugin FOR Anthropic Claude Code; cross-vendor-cooperation-via-plugin-marketplace mechanism. Could register as new pattern candidate OR as Pattern #19 archetype-extension. Recommend: NEW Pattern #77 candidate (Cross-Vendor Cooperative Plugin Publication).
3. **Pattern #19 corporate-strategic archetype N=3 strengthening** — Microsoft (spec-kit v17 + markitdown v28 = 2 products, 1 org) + OpenAI (codex-plugin-cc v62 = 1 product) = **2 distinct corporate-orgs at corpus level**. NOT yet structural-N=2 across distinct sub-archetypes (Microsoft is 2-product but same org); needs 3rd corporate org to reach N=3 cross-org.
4. **Pattern #18 Layer 2 cross-vendor-bridge sub-archetype** N=1 stale-flagged (codex-plugin-cc only; distinct from runtime API protocol translation v60 free-claude-code + install-time per-platform format translation v61 cc-sdd). T4 sub-taxonomy 3rd axis.
5. **Pattern #59 Claude Code Plugin Marketplace Native at corporate scale** — was OMC v27 solo + claude-hud v35 solo + (vercel-labs v51?); now OpenAI corporate scale. **Strengthening candidate**: corporate-marketplace-publishing sub-variant N=1 (codex-plugin-cc); 2nd corporate-marketplace-publication would un-stale-flag.
6. **Pattern #57 Recursive Corpus Reference 57c** — codex-plugin-cc IS within Claude Code ecosystem; install commands reference Claude Code primitives. Likely 57c-implicit-citation observation; verify with full README cross-corpus check.

**Counter-evidence flags to confirmed patterns:**

- **Pattern #51 Vibe-Coding Spectrum** — codex-plugin-cc has NO explicit anti-vibe positioning; NEUTRAL / professional review-tool framing. Counter-evidence to "anti-vibe-pole correlated with commercial-educator T1 archetype" v60 narrowing — NEUTRAL position observed at corporate-T4 archetype too. May extend Pattern #51 NEUTRAL pole observations.
- **Pattern #66 Supply-Chain Awareness OBSERVATION-TRACK** — installing OpenAI plugin in Claude Code = trusting OpenAI runtime auth + Codex backend; cross-vendor supply chain. Within-OT observation strengthens cross-vendor-trust-boundary sub-category.

**Cross-wiki standards check:**

- **OpenClaw runtime:** NOT mentioned (Codex backend uses local auth + Codex app server, not OpenClaw)
- **Hermes runtime:** NOT mentioned
- **MCP:** NOT mentioned (Codex integration is direct API not MCP-mediated)
- **AGENTS.md:** NOT shipped (plugin uses Claude Code's CLAUDE.md primitive only)
- **anthropics/skills protocol:** Implicit (Claude Code plugin marketplace mechanism)

---

## Sources ingested (Phase 2 will write cluster summaries)

1. README.md — Codex integration overview + 7 slash commands + workflow examples + FAQ + configuration
2. plugins/codex/ structure — agents/ + commands/ + hooks/ + prompts/ + schemas/ + skills/ + CHANGELOG
3. .claude-plugin/ marketplace metadata
4. config.toml format documentation (user-level + project-level)
5. /codex:adversarial-review command detailed behavior

---

## Cross-wiki siblings (mandatory cross-references)

**Pattern #76 N=1 baseline + counter-evidence:**
- [cc-sdd v61](../cc-sdd%20-%20Beginner%20Analysis/) — Pattern #76 N=1 stale-flagged baseline (separate-role architectural primitive: kiro-review + kiro-impl + kiro-debug + kiro-verify-completion)

**T4 Bridge sub-archetype peers:**
- [free-claude-code v60](../free-claude-code%20-%20Beginner%20Analysis/) — T4 9th archetype api-protocol-translation-proxy (different mechanism: runtime API translation; codex-plugin-cc is plugin-bridge-to-rival-platform)
- [graphify v16](../graphify%20-%20Beginner%20Analysis/) — T4 content-transformation
- [markitdown v28](../markitdown%20-%20Beginner%20Analysis/) — T4 content-transformation (Microsoft corporate; sibling corporate-org-T4 to codex-plugin-cc)

**Corporate-org-archetype peers:**
- [spec-kit v17](../spec-kit%20-%20Beginner%20Analysis/) — Microsoft corporate T1 SDD
- [markitdown v28](../markitdown%20-%20Beginner%20Analysis/) — Microsoft corporate T4

**Claude Code plugin marketplace peers:**
- [oh-my-claudecode v27](../oh-my-claudecode%20-%20Beginner%20Analysis/) — Pattern #59 N=1 OMC marketplace + companion
- [claude-hud v35](../claude-hud%20-%20Beginner%20Analysis/) — Pattern #59 N=2 marketplace-only
- [agent-skills-of-vercel](../agent-skills-of-vercel%20-%20Beginner%20Analysis/) — Vercel Agent Skills marketplace publication

**Code-review-augmentation peers:**
- [shannon v45](../shannon%20-%20Beginner%20Analysis/) — AI-pentester (security-review specialist; different domain but adversarial-review-of-code DNA)
- [aidevops v47](../aidevops%20-%20Beginner%20Analysis/) — DevOps-augmentation T1

---

## Build status

| Phase | Status |
|---|---|
| Phase 0 (probe) | ✅ COMPLETE |
| Phase 1 (scaffold) | ✅ COMPLETE |
| Phase 2 (sources) | ⏳ in progress (3 cluster summaries) |
| Phase 3 (entities) | pending (4 entity pages) |
| Phase 4a (beginner guide) | pending |
| Phase 4b (counter-evidence-driven refinement deliverable) | pending |
| Phase 5 (iteration log + Pattern Library update) | pending |
| Phase 6 (vault sync) | pending |
