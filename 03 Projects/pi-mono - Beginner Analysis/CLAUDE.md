# pi-mono - Beginner Analysis — Claude Context

**Project type:** LLM Wiki v36 (v2.1 routine, 5th v2.1-era execution)
**Subject:** `badlogic/pi-mono`
**Tagline:** *"AI agent toolkit: coding agent CLI, unified LLM API, TUI & web UI libraries, Slack bot, vLLM pods"*
**Status:** v1 in progress (2026-04-23)
**Operator:** Storm Bear (Cvtot, VN Scrum coach / software developer)

---

## Phase 0 probe (2026-04-23)

| Field | Value |
|-------|-------|
| Repo | `badlogic/pi-mono` |
| Stars | **38,950** (~#9 in corpus; between awesome-design-md v25 60.5K and graphify 30K / agency-agents 82.9K bucket) |
| Forks | 4,542 (11.7%) |
| Watchers (subscribers) | 153 |
| Open issues | **10** (very low for 38.9K-star T1 — tight maintainer control via auto-close gate) |
| License | **MIT** |
| Primary lang | **TypeScript 96.3%** + JavaScript 2.8% + Other 0.9% |
| Default branch | `main` |
| Created | 2025-08-09 (~8.5 months old) |
| Pushed | 2026-04-23 (today — actively maintained) |
| Latest release | v0.69.0 (2026-04-22) — **lockstep-versioned monorepo** |
| Total releases | **200+** across 8.5 months = ~23 releases/month velocity |
| Size | 42,499 KB (42 MB) |
| Homepage | **pi.dev** (domain donated by exe.dev) |
| Topics | not explicitly set on repo |
| README langs | **EN only** (no i18n) |

## Author

- **Mario Zechner (`badlogic` / `@mariozechner`)** — **Austrian solo author**
- **libGDX creator** (25K-star Java game framework; top pinned after pi-mono)
- Website: mariozechner.at
- Twitter/X: @badlogicgames
- Mastodon: @badlogic@mastodon.gamedev.place
- Bluesky: @badlogic.bsky.social
- GitHub: 253 repos, 5.1K followers, 3,728 commits on pi-mono
- Associated with `libgdx` organization
- Publishes OSS coding agent session data to Hugging Face dataset `badlogicgames/pi-mono`
- **Ecosystem-layer portfolio:**
  - `pi-mono` (38.9K) — this wiki
  - `pi-skills` (1.3K) — Skills for pi coding agent (Claude Code + Codex CLI compatible)
  - `pi-share-hf` (154) — Hugging Face dataset uploader for pi sessions
  - `libgdx/libgdx` (25K) — prior flagship
  - `r96` (158), `lilray` (13) — smaller personal projects

**Contributors observed** (CHANGELOG + issue-gate model): solo maintainer with gated PR contributions via `lgtm` / `lgtmi` approval protocol.

## 12-axis v2.1 classification

| Axis | Value |
|------|-------|
| **Tier** | **T1 Agent-as-assistant (primary via pi-coding-agent) — 13TH T1 ENTRANT** + MULTI-TIER-MONOREPO OBSERVATION: pi-mono itself spans T1 (coding-agent flagship) + T4-adjacent (pi-ai unified LLM abstraction library, pi-tui TUI library, pi-web-ui components) + T2-adjacent (pi-mom Slack bot) + outside-scope-adjacent (pi-pods GPU infra). **First multi-tier-monorepo-under-single-flagship in corpus** — observational; Phase 4b deliverable will examine whether this warrants new sub-pattern registration (see Phase 0.5 analysis). |
| **Archetype** | **Solo-flagship-with-monorepo-portfolio (NEW T1 sub-variant)** — distinct from prior 12 T1 entrants. Closest analog: agency-agents v18 (solo msitarzewski + 144-agent library at 82.9K) and oh-my-claudecode v27 (Yeachan ecosystem portfolio with sibling `oh-my-codex`). But pi-mono is singular: 1 owner, 1 flagship, 7 co-published packages, lockstep versioning, 200+ releases in 8.5 months. |
| **Scale tier** | Medium-large (38.9K, ~4.6K/month velocity over 8.5 months — sustained-community-viral per Pattern #27 sub-path) |
| **Primary lang** | TypeScript (strict; no `any` rule per AGENTS.md) |
| **Packaging** | **npm multi-package monorepo** — 7 npm packages under `@mariozechner/*` scope (`pi-ai`, `pi-agent-core`, `pi-coding-agent`, `pi-mom`, `pi-tui`, `pi-web-ui`, `pi-pods`). Install via `npm install -g @mariozechner/pi-coding-agent`. **NO Claude Code `/plugin marketplace` integration** (contrast OMC v27 + claude-hud v35 Pattern #59). |
| **Origin story** | Individual-author (Mario Zechner, libGDX lineage) — author brings 15+ years OSS framework-maintainer experience from game-dev into AI agent space |
| **Methodology** | **Anti-methodology** — README explicitly frames tagline "Adapt pi to your workflows, not the way around." Minimal defaults + deep extensibility. Contrast spec-kit v17 / BMAD v11 / GSD v5 methodology-forward approach. |
| **Governance** | **HEAVY + UNIQUE gate** — AGENTS.md 182+ lines + CONTRIBUTING.md quality-bar + 3 GitHub Actions workflows (`issue-gate`, `pr-gate`, `approve-contributor`) + `lgtm`/`lgtmi` maintainer-approval protocol (corpus-first) + CRITICAL parallel-agent git rules + auto-close-by-default for new contributors |
| **Agent/skill count** | **~25 CLI flags + ~20 slash commands + ~15 keybindings + 7 built-in tools (read/write/edit/bash/grep/find/ls) + 4 resource types (extensions / skills / prompt-templates / themes) + ~38 config settings** — dense primitive surface |
| **i18n** | **EN-only** (1 language — contrast OMC v27 7-lang, claude-howto v32 4-lang, HuggingFace agents-course v26 ecosystem) |
| **Intellectual influence** | **No explicit AI-agent lineage** cited (no Karpathy / John Lam / Boris Cherny / research-paper citations). Implicit lineage: author's own libGDX 15-year game-framework maintenance experience. Pattern #19 archetype 4 (no-lineage) — 13th T1 data point for archetype 4. |
| **Agent platforms** | **Pi as standalone runtime** (Claude Code-equivalent, not Claude-Code-dependent). Consumes Claude/OpenAI/Google/etc. subscriptions + 20+ API providers via own pi-ai abstraction. **Does NOT integrate with Claude Code native plugin marketplace.** pi-skills sibling repo is **Claude Code + Codex CLI compatible** (interop, not dependency). |

## Primitive-count probe (v2.1 Phase 5 informal discipline — 2ND USE after v35 GREEN inaugural)

Per v2.1 Phase 5 informal discipline introduced session 41 and validated at v35 (GREEN result on narrow target), counting distinct primitives from 6 signals:

| Signal | Source | Count |
|--------|--------|-------|
| 1. README TOC top-level sections (monorepo root) | README.md | **~6** (badge row / share-sessions ask / packages table / contributing / development / license) |
| 2. Repo folder structure top-level | GitHub contents | **6 dirs + 12 files** (.github / .husky / .pi / packages / scripts + 7 config files) |
| 3. Packages (monorepo children) | `packages/` | **7** (ai / agent / coding-agent / mom / pods / tui / web-ui) |
| 4. Coding-agent CLI surface | coding-agent README | **~25 CLI flags + ~20 slash commands + ~15 keybindings + 7 built-in tools + 4 resource types + ~38 config settings = ~110 user-facing primitives** |
| 5. pi-ai providers | pi-ai README | **20+ providers** (Anthropic + OpenAI + Google + Vertex + Mistral + Groq + Cerebras + xAI + OpenRouter + Vercel + Bedrock + Copilot + Azure + ZAI + OpenCode Zen + OpenCode Go + HuggingFace + Fireworks + Kimi + MiniMax + OpenAI-compatible) |
| 6. pi-mom + pi-pods + pi-tui + pi-web-ui primitives | respective READMEs | **~30+ more primitives** (Slack bot events + scheduling; GPU provider integrations; TUI components; web-ui components) |

**Probed primitive-count summary:**
- **Product-level primitives:** **~7** (7 packages)
- **User-level primitives (coding-agent alone):** **~110** dense surface
- **Provider-level primitives (pi-ai alone):** **20+**
- **Total monorepo primitive surface:** **~150-200** across all 7 packages

**Fits 4-entity format cleanly:** **NO — YELLOW flag.** The pi-mono product surface is **~3-4× denser than claude-hud v35** (which was GREEN). A single 4-entity wiki will need to **lossily compress**: either (a) treat coding-agent as primary product + other 6 packages as "ecosystem" in 1 entity, or (b) split across multiple wikis.

**Flagging outcome:** **YELLOW — 4-entity format requires deliberate scope compression.**

**Decision for v36:** **Compress via hierarchical focus** — Entity 1 = pi-coding-agent (CLI + interactive flagship); Entity 2 = pi-ai + pi-agent-core (foundation libraries); Entity 3 = Mario Zechner solo-flagship + ecosystem-portfolio archetype (author-centric, covers monorepo context + pi-pods/pi-mom/pi-tui/pi-web-ui as side-ecosystem); Entity 4 = Storm Bear meta-entity. **Accept lossy compression of pi-pods / pi-mom / pi-tui / pi-web-ui detail** — cite their READMEs as primary sources rather than replicate.

**Follow-up deep-dive wikis (future options, NOT triggered now):**
- pi-ai as standalone wiki when LiteLLM counter-evidence needs N≥3 data points (currently N=3 abstraction libs: LiteLLM v19 + markitdown `llm_client` v28 + pi-ai v36)
- pi-pods as standalone wiki if GPU-agent-infrastructure-archetype emerges (currently N=1 in corpus)

**Operator-decision recommended:** Accept lossy compression at v36. Future Pattern Library pressure may warrant pi-ai standalone deep-dive; defer to user.

## v2.1 Phase 0.5 pattern pre-check results

### Overlap pre-check for proposed new candidates

Initial candidate inventory (pre-discipline):
1. **"Multi-tier monorepo under single flagship"** (pi-mono 7 packages spanning T1+T4-adjacent+T2-adjacent)
2. **"Austrian regional T1 archetype"** (Mario Zechner Austrian)
3. **"MCP-exclusion-by-design at scale"** (pi deliberately excludes MCP at 38.9K T1)
4. **"lgtm/lgtmi maintainer approval gate"** (gate syntax corpus-first)
5. **"Lockstep monorepo versioning with 200+ releases in 8.5 months"** (release velocity)

Applying v2.1 70% overlap threshold:
- **#1 Multi-tier monorepo** — overlap with Pattern #17 Ecosystem-Layer Orgs (which covers ecosystem-portfolio solo variants). Overlap ~60-70% (both describe solo with multiple published products). **Borderline.** Consolidation-forward: strengthen Pattern #17 as **solo-flagship-with-monorepo-scope variant** rather than register standalone. Decision: **REJECT standalone; strengthen #17.**
- **#2 Austrian regional** — Pattern #73 Regional-Archetype-Registry T1 Meta-Pattern (CANDIDATE v34; 3 existing sub-variants 73a Korean / 73b VN / 73c Pakistani). Austrian = potential 73d at N=1. Per v2.1 consolidation-forward + N=1 stale-risk-flagging: **strengthen #73 with 4th sub-variant observation** rather than register standalone. Decision: **Add as observational #73d sub-variant (N=1 stale-risk-flagged); #73 now has 4 sub-variants at N=1-each; promotion for #73 itself was already proposed at v34 as meta-pattern-at-N=3-consolidation criterion**. Note: Austrian ≠ European (Germany/France/Italy not in corpus yet — would need N=2 European for regional cluster).
- **#3 MCP-exclusion-by-design at scale** — Pattern #18 Agent Runtime Standardization (CONFIRMED v15; 9+ MCP-consumer data points post-awesome-mcp-servers v31). pi-mono is **first COUNTER-EVIDENCE at T1 scale for Pattern #18** — a 38.9K-star T1 coding agent that deliberately rejects MCP-as-primary. Strengthens the EXTENSION-POINT-alternative pathway (claude-hud v35 extension-point-consumer variant). **Decision: Observational counter-evidence; NOT registered as new candidate. Note for Pattern #18 refinement watch (if 2nd MCP-exclusion T1 emerges, formalize as "MCP-optional-via-extension" sub-variant).**
- **#4 lgtm/lgtmi maintainer approval gate** — Pattern #69 Agent-PR Fast-Track Governance Protocol (CANDIDATE v31; `🤖🤖🤖` suffix). pi-mono `lgtm` / `lgtmi` is **a different mechanism** (human-to-bot approval keyword vs agent-authored PR suffix), but both are agent-era governance-gate innovations. Overlap 40-60% (shared theme: maintainer-facing gate protocol). **Borderline.** Consolidation-forward: strengthen #69 as "maintainer-approval-gate-protocol" meta-pattern at N=2 via pi-mono + `🤖🤖🤖`-style. Decision: **Strengthen #69 to N=2 with sub-variant framing** — 69a `🤖🤖🤖` suffix (agent-authored opt-in at PR-time) + 69b `lgtm`/`lgtmi` (maintainer-authored approval at comment-time). **Promotes #69 from N=1 stale-risk to N=2 structurally-unambiguous; promotion-candidate at next mini-audit.**
- **#5 Lockstep monorepo versioning 200+ releases in 8.5 months** — no direct corpus precedent. Velocity is exceptional (~23 releases/month). But is this a PATTERN or an AUTHOR-specific quirk? Single-author-specific (Mario's own release cadence). **Decision: REJECT as standalone candidate — insufficient generalizability at N=1.** Note as author-archetype observation; file under Mario's entity page.

**Net candidate registration at v36: 0 NEW standalone candidates.**

Strengthening decisions:
- **Pattern #17** Ecosystem-Layer Orgs — **11th data point** (Mario solo-flagship-with-monorepo-scope variant; distinct from variant 1 Luong/OMC ecosystem-portfolio via tighter single-flagship focus)
- **Pattern #18** Agent Runtime Standardization — **MCP-exclusion counter-evidence at T1 scale** (observational; not refined at N=1)
- **Pattern #19** Intellectual Lineage Archetypes — **13th T1 data point for archetype 4** (no-lineage) — cross-domain lineage from game-dev (libGDX) is nominally present but not cited in README
- **Pattern #20** Solo-Scale Ceiling — **NEW ROW** "solo-Austrian + multi-package-monorepo + npm-distribution T1" (38.9K/8.5mo ≈ 4.6K/month sustained)
- **Pattern #27** Community-Viral Scale Path — **13th data point; sustained-community-viral-with-cross-domain-founder-equity sub-path** (Mario brought libGDX-era follower base; not purely AI-agent-space virality)
- **Pattern #69** Agent-PR Fast-Track Governance Protocol — **STRENGTHENS to N=2** (2 sub-variants: 69a `🤖🤖🤖` agent-suffix + 69b `lgtm`/`lgtmi` maintainer-keyword) — **PROMOTION-CANDIDATE at next mini-audit** under Criterion 2 (structurally-unambiguous-at-N=2); un-stales from stale-risk
- **Pattern #73** Regional-Archetype-Registry T1 Meta-Pattern — **4th sub-variant 73d Austrian** added (observational N=1-in-registry; #73 itself is a meta-pattern already at N=3 promotion-ready per v34 registration)

### Un-stale check

- **#52 Extreme-Viral-Velocity** (stale since v31 mini-audit, retroactive from v30) — pi-mono ~4.6K/month is **not extreme** (#52 threshold ≥1K/day = ~30K/month). **Does NOT un-stale.**
- **#55 Korean Regional** (stale since v32 mini-audit) — Austrian ≠ Korean. **Does NOT un-stale.**
- **#45 Dual-Licensing** / **#46 Duo-Founder** (stale since v29 audit; retire threshold v33 passed; NO retirement decision taken at v33/v34/v35) — pi-mono is single-MIT + solo. Does NOT un-stale. **⚠️ Retirement now overdue** — flag for next mini-audit.
- **Retired revivals** (#14 / #16 / #23 / #25 / #49 / #60) — no revival evidence in pi-mono.

### Counter-evidence observations

- **Pattern #18 Agent Runtime Standardization (CONFIRMED v15)** — pi-mono is **first T1-scale MCP-exclusion counter-evidence**. Observational; not refined at N=1 (need 2nd T1 MCP-exclusion to formalize "MCP-optional-via-extension-only" sub-variant). Notable for watch.
- **Pattern #22 AGENTS.md T1 absence** (CANDIDATE v17) — pi-mono **HAS AGENTS.md at 182+ lines** (uncommon at solo T1). Continues refinement of #22 (AGENTS.md is becoming solo-T1-adopted, not just corporate-T4). 5+ data points now.
- **Pattern #12 Governance-Depth Correlation** (CONFIRMED v13) — pi-mono has **EXTREMELY heavy governance** for solo project: 3 GitHub Actions gates + AGENTS.md 182 lines + CONTRIBUTING quality-bar + lgtm protocol. **Mirrors claude-hud v35 counter-evidence (solo-heavy-governance)**. N=2 now. **If N=3, Pattern #12 refinement needed: governance correlates with MAINTAINER-PHILOSOPHY more than organization.** Flagged for watch.
- **Pattern #28 Multi-Provider AI Support** (CONFIRMED v25 audit; N=6 prior data points) — pi-ai 20+ providers is **new corpus record for single abstraction library** (prior: LiteLLM 100+ but that's pure abstraction library outside corpus; markitdown `llm_client` DI had ~4 providers; crawl4ai LiteLLM-fork had 100+ via inheritance). pi-ai is **20+ providers built-in at T1-coding-agent scope** — different scope from pure abstraction libraries. **Refinement candidate: Pattern #28 sub-variant "native-built-in multi-provider at T1" distinct from "abstraction-library-dependency multi-provider."** Defer to mini-audit.

### Consolidation-forward discipline applied

**5 potential candidates considered, 0 registered standalone. Instead:**
- 1 strengthening (Pattern #17 variant)
- 1 counter-evidence observation (Pattern #18)
- 1 cross-reference strengthening (Pattern #20 new row)
- 1 sub-variant addition (Pattern #73d Austrian)
- 1 candidate promotion-path (Pattern #69 N=1 → N=2 structurally-unambiguous)

**Net candidate count: +0. Ratio stays 0.79:1. Consolidation-forward discipline preserved ratio.**

### Storm Bear meta-entity applicability (Phase 0.9)

**YES — include 4th entity as Storm Bear meta.** Reasons:
1. pi-coding-agent is a **direct alternative to Claude Code** as a standalone terminal coding harness — Storm Bear operator already uses Claude Code, so pi is a comparison/substitute evaluation
2. **pi-ai 20+ providers** = potential Storm Bear operator escape-hatch from vendor lock-in (currently Claude Code-only; pi-ai offers multi-provider option)
3. **pi-skills ecosystem** (1.3K stars, Claude Code + Codex CLI compatible) = Storm Bear could import pi-skills into Claude Code workflow
4. **`pi-share-hf` open-source OSS session data ethos** = aligns with Storm Bear "compounding knowledge" philosophy (Mario shares work-sessions publicly on HF; Storm Bear shares wiki pages publicly-ish)
5. **Mario's libGDX lineage** = cross-domain-expertise-transfer case study (game framework → AI agent framework); interesting for Storm Bear's Scrum-coach-to-AI-tooling transition

**25th consecutive Storm Bear meta-entity** (v10-v36). Per v2.1 Phase 0.9 per-wiki applicability affirmed.

## Phase 4b routing mode

**Primary:** **T1 monorepo-under-single-flagship archetype + Pattern #69 N=2 promotion + Pattern #18 MCP-exclusion counter-evidence Phase 4b deliverable.**

**Rationale:** T1 now at N=13 entrants post-pi-mono. Full N-way comparison (13-way) is unwieldy and low-value. Instead, **narrow-focus deliverable** on:

1. **T1 monorepo-under-single-flagship archetype introduction** — pi-mono is 1st in corpus to publish 7 packages under a single solo-author flagship with lockstep versioning. Distinct from:
   - OMC v27 (4 runtimes, 1 package `oh-my-claude-sisyphus` — different structure)
   - Mario's libGDX (which was multi-library but under organizational umbrella, not solo)
   - markitdown v28 (corporate-Microsoft monorepo, 1 package per monorepo)
2. **Pattern #69 N=2 promotion analysis** — first agent-era maintainer-approval-gate protocol meta-pattern (69a agent-suffix + 69b maintainer-keyword)
3. **Pattern #18 MCP-exclusion counter-evidence at T1 scale** — what does deliberate MCP-exclusion at 38.9K T1 reveal about Pattern #18's formal statement? Does it warrant "MCP-optional-via-extension" sub-variant? (answer: wait for N=2 T1 MCP-exclusion)
4. **Cross-domain founder-equity observation** — Mario brought libGDX-era follower base (~25K stars worth of Java game-dev community trust) into agent space; how does this interact with Pattern #27 Community-Viral Scale Path? Compare with Anthropic/GitHub corporate-amplified sub-path.
5. **Primitive-count flagging 2nd run — YELLOW outcome + scope-compression decision** — documents 4-entity format under primitive-density pressure; establishes precedent for future YELLOW-flagged wikis.

~550-650 lines Phase 4b deliverable focusing on the above 5 dimensions.

## Scope and boundaries

- **In-scope:** 13th T1 entrant + multi-tier-monorepo observation + Pattern #17/18/19/20/22/27/28/69/73 strengthening-or-promotion + primitive-count 2nd-run YELLOW outcome + Storm Bear pilot viability
- **Out-of-scope:** Full 7-package deep-dive (lossy compression accepted); full 13-way T1 matrix (unwieldy — scope-axis sub-classification used instead); exhaustive provider-by-provider pi-ai documentation (cite README); exhaustive coding-agent CLI flag enumeration (cite README); pi-mom Slack-bot + pi-pods GPU-infra deep-dive (out-of-scope for this compression cycle)

## Pilot ranking preview

**Very HIGH pilot relevance — potentially NEW #3 after spec-kit + OMC:**

**Pro:**
1. **pi-coding-agent is a Claude-Code-grade standalone harness** — if Storm Bear ever hits Claude Code vendor friction, pi is a ready alternative with comparable feature surface (slash commands, sessions, tool-use, extensions)
2. **pi-ai unlocks multi-provider independence** — currently Storm Bear is Anthropic-subscription-locked; pi-ai allows mixing Claude + OpenAI + Gemini + local-vLLM seamlessly
3. **Mario's minimal-defaults philosophy aligns with Storm Bear "adapt tool to workflow"** — per README tagline match
4. **MIT + npm install one-liner** = zero-friction technical install (albeit npm global requires nodejs)
5. **pi-skills Claude Code + Codex CLI compatible** = interop pathway if Storm Bear wants skills without full pi switch
6. **Session export as HTML + Hugging Face share via `pi-share-hf`** = publishable workflow for sharing Scrum-AI-coaching sessions publicly

**Con / Caveats:**
1. **Solo bus factor** (Mario is entire project) — 3,728 commits, 200+ releases in 8.5 months = velocity healthy but concentration-risk high
2. **EN-only** — no Vietnamese interface for VN client demos
3. **No MCP integration** — if Storm Bear's existing MCP server investments matter, pi is incompatible out-of-box (requires writing MCP extension)
4. **Heavy learning curve vs Claude Code** — 110+ primitive surface; not a zero-friction switch
5. **Unproven at enterprise scale** — 38.9K stars is large but project is 8.5 months old; Claude Code / pi production-track-record asymmetry favors Claude Code
6. **`lgtm`/`lgtmi` gate** — contributing back to pi-mono requires upfront maintainer approval; higher friction than typical OSS

**Recommended pilot mode:** Low-commitment parallel-evaluation — install `npm install -g @mariozechner/pi-coding-agent`, run one Scrum-doc session, export HTML, compare output quality with Claude Code baseline. ~2 hours.

## Cross-references (sibling wikis)

Primary peers (to cite in 02 Wiki + 03 Published):
- `../claude-hud - Beginner Analysis/` (v35) — most recent T1, display-layer plugin sub-variant contrast
- `../claude-code-best-practice - Beginner Analysis/` (v34) — Pakistani T1 meta-reference
- `../oh-my-claudecode - Beginner Analysis/` (v27) — Korean T1 ecosystem-portfolio closest architectural cousin (multi-runtime orchestration vs multi-package monorepo)
- `../claude-howto - Beginner Analysis/` (v32) — VN-diaspora T1 tutorial contrast
- `../agency-agents - Beginner Analysis/` (v18) — solo-at-enterprise-scale precedent (82.9K solo) + 144-agent-library precedent
- `../spec-kit - Beginner Analysis/` (v17) — GitHub-corporate T1 methodology contrast
- `../Everything Claude Code - Beginner Analysis/` (v1) — US T1 baseline
- `../Superpowers - Beginner Analysis/` (v2) — Jesse Vincent US T1 methodology peer
- `../markitdown - Beginner Analysis/` (v28) — **T4 corporate-monorepo-narrow-utility** — architectural contrast (corporate monorepo with 1 package vs solo monorepo with 7 packages)
- `../crawl4ai - Beginner Analysis/` (v29) — solo-enterprise-scale precedent (64K solo, LiteLLM integration for multi-provider)
- `../TrendRadar - Beginner Analysis/` (v19) — LiteLLM multi-provider 100+ precedent (abstraction-library variant of Pattern #28)

## Next action (Phase 1)

Build `02 Wiki/(C) index.md` + `(C) log.md` + `01 Analysis/(C) open questions.md`, then proceed to Phase 2 (3 cluster summaries).

---

*(C) Claude-generated 2026-04-23 under routine v2.1 execution 5 (v36 fifth v2.1-era wiki after claude-howto v32 + GitNexus v33 + claude-code-best-practice v34 + claude-hud v35).*
