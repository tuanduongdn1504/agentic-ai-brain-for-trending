# (C) agency-agents — v185 Corpus-Recursive Revisit (Deep Dive + Delta + Verdict)

> **Type:** v185 ship — corpus-recursive revisit of v18 (the 2nd revisit in corpus history; v78 ECC was the 1st).
> **Subject:** [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) — *"A complete AI agency at your fingertips."*
> **Built:** 2026-06-30 · cloned + source-verified at commit `2448583` (2026-06-29, `docs: sync supported tool docs #625`).
> **Author of this doc:** Claude (Storm Bear vault). Verdict produced **inline + hand-verified** per `feedback_wiki_verify_independently_check_collisions`. A 10-agent read-only workflow did source-reading + upstream research only (safe/factual); all corpus-fact / collision / identity claims verified by hand.

---

## 0. Why this is a REVISIT, not a new subject (the collision)

`msitarzewski/agency-agents` is **already in the corpus** — wiki'd as **v18 (2026-04-19)** under the old routine v1 (T1/T2 tier framework; Patterns #19/#20/#25). Folder: `03 Projects/agency-agents - Beginner Analysis/` (12 v18 docs preserved, untouched). This v185 ship is the **delta-revisit**: capture what changed in ~2.5 months and re-evaluate under the **current routine v2.6** (GOAL-ALIGNED INCLUDE / §C standalones / 46 patterns / 11 Library-vocab). v18 docs are NOT overwritten.

---

## 1. The delta — what changed v18 → v185 (~72 days)

| Dimension | v18 (2026-04-19) | v185 (2026-06-30) | Δ |
|---|---|---|---|
| **Agents** | 144 | **232** | +88 (verified = exact sum of the 16 division dirs) |
| **Divisions** | 12 | **16** | +GIS, +others; integrations/ & strategy/ are NOT divisions |
| **Stars** | 82.9K | **119K** (page-stated) | +36.1K |
| **Forks** | 13.2K | **19.5K** (page-stated) | +6.3K |
| **Languages** | Shell 96.8% | Shell 84.8% / Python 13.9% / PowerShell 1.3% | +Python tooling |
| **Distribution** | shell scripts, ~11 platforms | **14 tools** (3 install-kinds) + a native **Desktop App** | richer |
| **Governance** | v18 framed as *"Light — no formal governance"* | **4 CI gates** (lint + semantic-originality + divisions-drift + tools-drift) | **MAJOR** |
| **Commits** | 291 | 353+ | active |
| **Releases** | none (main only) | none (main only) | unchanged |
| **License** | MIT | MIT | unchanged |

**The v18 framing that is now WRONG / stale:** (1) *"Shell 96.8% / shell-first"* — now multi-language with a Rust+Tauri desktop app; (2) *"Light — no formal governance"* — now a real CI discipline (see §4); (3) *"144 agents / 12 divisions"* — now 232/16; (4) the old routine-v1 Pattern #20 "solo-scale-ceiling" framing is obsolete (the modern routine doesn't track solo-scale-ceilings).

---

## 2. What it actually IS (the source-verified deep dive)

**Tagline (verbatim):** *"A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables."*

**Thesis (README "What Is This?"):** *"Born from a Reddit thread and months of iteration, The Agency is a growing collection of meticulously crafted AI agent personalities."* Each agent is **🎯 Specialized** (not generic prompt templates), **🧠 Personality-Driven** (unique voice), **📋 Deliverable-Focused** (real code + measurable outcomes), **✅ Production-Ready**. *"Assembling your dream team, except they're AI specialists who never sleep, never complain, and always deliver."*

**The crucial primitive (verified against Anthropic docs):** agency-agents ships **SUBAGENTS**, not skills. A subagent = an isolated worker with its **own context window + own system prompt**, model-invocable, returning a summary to the main conversation. A *skill* = injected markdown knowledge/workflow. agency-agents installs persona `.md` files to **`~/.claude/agents/`** (Claude Code's subagent dir; install order 1, `format: identity`). You activate one by talking: *"Use the Frontend Developer agent to review this component."* (Nuance: `convert.sh` renders the SAME persona to `SKILL.md` format for Osaurus/Antigravity — so on those harnesses it lands as a skill; but the canonical primitive is the subagent.)

### 2a. The 16 divisions (232 agents)

| Division | Agents | Flavor |
|---|---|---|
| Engineering | 33 | frontend/backend/mobile/AI/devops + long tail (solidity, embedded-firmware, wechat-mini-program, drupal/woo carts, filament-PHP) + **code-reviewer, prompt-engineer, minimal-change-engineer, codebase-onboarding-engineer, multi-agent-systems-architect** |
| Marketing | 31 | content, growth-hacker, **reddit-community-builder** (anti-astroturfing ethic) |
| Specialized | 60+ | catch-all (largest); the "doesn't fit a box" long tail |
| Game Development | 20+ | engines, level/narrative/combat design |
| GIS | 13 | **NEW since v18** — geospatial / mapping / built-world intelligence |
| Security | 10 | secure-by-design → breach response |
| Sales | 10 | discovery, deal strategy |
| Design | 9 | UI/UX + **Whimsy Injector** + **Brand Guardian** + persona-walkthrough |
| Testing | 8 | QA + **Reality Checker** (the signature governance agent) |
| Paid Media | 7 | PPC, paid-social, tracking/measurement |
| Project Management | 7 | sprint-prioritizer, project-shepherd |
| Spatial Computing | 6 | AR/VR |
| Support | 6 | tiers, onboarding |
| Academic | 5 | research rigor / world-building |
| Finance | 5 | accounting, tax, investment research |
| Product | 5 | PM, product strategy |

**NOT divisions** (per `divisions.json` `_note` + `check-divisions.sh`): `integrations/` (generated conversion OUTPUTS written by convert.sh), `strategy/` (playbooks/runbooks, no agent frontmatter), `examples/`, `scripts/`.

### 2b. The agent file format (the reusable template)

```yaml
---
name: Reality Checker                 # REQUIRED
description: Stops fantasy approvals…  # REQUIRED
color: red                            # REQUIRED (named or #hex)
emoji: 🧐                              # optional
vibe: Defaults to "NEEDS WORK"…       # optional — one-line personality hook
services:                             # optional — declared external deps (name/url/tier free|freemium|paid)
---
# <Persona> Personality
## 🧠 Identity & Memory        → (soul)
## 🎯 Core Mission             → (agents)
## 🚨 Mandatory Process / Critical Rules
## Workflow / Deliverables / Success Metrics
```
Real files run ~150–250 lines. The lint requires `name`/`description`/`color` (ERROR if missing) + ≥50 body words + ≥1 "soul" section + ≥1 "agents" section (WARN).

### 2c. Signature agents (the personality-driven differentiator)

- **Reality Checker** (testing, 236 lines, `vibe: Defaults to "NEEDS WORK"`): *"Stops fantasy approvals… requires overwhelming evidence before production certification. No more '98/100 ratings' for basic dark themes. Every system claim needs visual proof. First implementations typically need 2-3 revision cycles."* → a built-in adversarial QA gate. **This is the most directly useful agent for the operator's own `verify-independently` discipline.**
- **Whimsy Injector** (design): *"Every playful element must serve a functional or emotional purpose."*
- **Brand Guardian** (design): reviews other agents' outputs for brand consistency.
- **Reddit Community Builder** (marketing): *"You're becoming a valued community member who happens to represent a brand"* — explicit anti-astroturfing/anti-hard-sell ethic (notable given the repo's own Reddit-viral origin).

### 2d. Multi-agent WORKFLOWS (`examples/` — the most pilot-relevant part)

- **`workflow-startup-mvp.md`** — a 7-agent SEQUENCED pipeline to ship an MVP in 4 weeks: Sprint Prioritizer → UX Researcher (parallel) → Backend Architect → Frontend Developer + Rapid Prototyper → **Reality Checker (midpoint gate)** → Growth Hacker → **Reality Checker (GO/NO-GO)**. Explicit "Key Patterns": sequential handoffs, parallel work, quality gates, **context passing** (*"agents don't share memory — paste the full previous output into the next prompt"*).
- **`nexus-spatial-discovery.md`** — 8 agents run **in parallel** to produce a full product blueprint (market validation + architecture + brand + GTM + support + UX + 35-week plan + spatial spec) *"without coordination overhead."*
- `workflow-landing-page.md`, `workflow-book-chapter.md`, `workflow-with-memory.md` (memory/persistence usage).

### 2e. The 14-tool conversion + install engine

One canonical `.md` source → 14 harness-native formats via `convert.sh` (3 `installKind`s):
- **per-agent** (one file/dir per agent): Claude Code (`.claude/agents/{slug}.md`, `identity`), Codex (`.codex/agents/{slug}.toml`), Gemini CLI, Copilot, Qwen, Cursor (`.cursor/rules/{slug}.mdc`), OpenCode (`mode: subagent`, **caps ~119** per upstream bug), Osaurus (`SKILL.md`), Antigravity (`SKILL.md`), Kimi (`agent.yaml`+`system.md`), OpenClaw (splits into **SOUL.md + AGENTS.md + IDENTITY.md**).
- **roster** (one combined file): Aider (`CONVENTIONS.md`), Windsurf (`.windsurfrules`).
- **plugin** (built artifact): Hermes — a **lazy-router** (`build-hermes-plugin.py`) exposing 4 tools (`search`/`inspect`/`load`/`delegate`) over an on-disk `agents.json`, so you don't preload 232 agents into context.

### 2f. The Desktop App (`msitarzewski/agency-agents-app`)

Native **Rust + Tauri 2 + SvelteKit/Svelte 5** (macOS 13+/Linux/Windows; signed builds). A "control surface" GUI to browse / install / track agents across 8+ tools: agent browsing by division, cross-platform install, an **install ledger**, **file-modification detection**, team/project organization, update management.

---

## 3. Author identity (hand-verified)

**Michael "Mike" Sitarzewski** (`msitarzewski`) — a **disclosed individual**: 30+ years in tech, Techstars alum, EIR at the Dallas Entrepreneur Center, currently **VP of Innovation & Technology at Tandem Theory** (a marketing agency — hence "agency-agents") in Dallas, TX. GitHub: 4.6k followers, 27 repos. Prior projects: **AGENT-ZERO** (AI-assisted dev framework, 230★), **brew-browser** (Rust Homebrew GUI, 913★), **duh** (multi-model LLM consensus engine, Python), **glas.sh** (visionOS terminal), **openstudio** (broadcast studio). A serious multi-product builder.

---

## 4. Governance evolution (the headline finding) — how a near-solo maintainer scales to 232 agents

v18 said "no formal governance." v185 has **4 CI gates** (the load-bearing infrastructure):

1. **`lint-agents.sh`** — required frontmatter `name`/`description`/`color` (ERROR), LF endings (ERROR), ≥50 words + soul/agents sections (WARN). Path-filtered to the 16 divisions.
2. **`check-agent-originality.sh`** *(novel mechanism)* — **entity-neutralized 8-word-shingle Jaccard similarity** against the entire roster + same-PR candidates. Strips frontmatter, neutralizes proper nouns (Vietnam/China/TikTok/WeChat/…), so a swapped country/platform name can't disguise a copy. **FAIL ≥40%** (blocks merge), **WARN ≥20%**; existing-library baseline ~1.5% worst-pair. → catches "find-replace re-skins."
3. **`check-divisions.sh`** — 5-way consistency: `divisions.json` ↔ on-disk dirs ↔ `convert.sh` AGENT_DIRS ↔ `lint-agents.sh` AGENT_DIRS ↔ `lint-agents.yml` path filters. Runs every PR + push to main.
4. **`check-tools.sh`** — 3-way consistency: `tools.json` ↔ `install.sh` ALL_TOOLS ↔ `convert.sh` valid_tools. Runs every PR + push to main.

PR discipline: one agent per PR (fast path); originality check mandatory; "re-skins" closed; build output never committed (run `convert.sh` locally).

---

## 5. Security posture (source-read; benign — a key pilot fact)

`install.sh` (51KB) + `convert.sh` (20KB) are **pure bash + awk + embedded Python**, ShellCheck-clean:
- **ZERO network calls. No `curl|bash`. No `sudo`. No telemetry. No precompiled binaries. No package-manager installs.**
- Writes only to user config dirs (`~/.claude/agents/` etc.) or project-scoped dirs (`.cursor/`, `.opencode/`, `CONVENTIONS.md`, `.windsurfrules`).
- Safeguards: `--dry-run`, `--agents-file <path>` (curate which agents), `--division`/`--agent` filters, `--path <dir>` override, `--link` (symlink), an interactive TUI with confirmation, `--no-convert`.
- The only "writes-outside" beyond agent dirs: Hermes modifies `~/.hermes/config.yaml` (with a `.bak` backup) — **skip Hermes unless you use it**.
- Agent `.md` files are **non-executable prompts** (SECURITY.md forbids executable code in agent markdown + asks to report prompt-injection attempts).

**→ This is the SAFEST recent pilot candidate** — far below cortex-hub v181 (`curl|bash` + 5-service compose), camofox v179 (postinstall binary download), or devspace v171 (remote execute). The real risk is *bloat + prompt-surface*, not supply-chain: don't dump all 232 personas into `~/.claude/agents/`; install ~10 curated, `--dry-run` first, read the ones you install.

---

## 6. Peers (so we don't over-claim "first")

| Collection | Count | Stars | Distinguisher |
|---|---|---|---|
| **agency-agents** | **232 / 16 div** | **119K** | broadest, personality-first, most viral |
| wshobson/agents | 194 + 158 skills + 88 plugins + 106 cmds | — | most architecturally sophisticated (1 source → 6 harnesses, respects Codex 8KB cap) |
| VoltAgent/awesome-claude-code-subagents | 154+ / 10 cat | 22.6K | Claude-native subagent primitive, isolation-first |
| contains-studio/agents | — | — | (not detailed) |

→ agency-agents is the **largest by count + the most viral**, NOT a world-first-of-class (subagent-collections are a populated genre). It IS the corpus's clear exemplar of the class (and historically its v18 anchor).

---

## 7. VERDICT (routine v2.6, inline + hand-verified)

**GOAL-ALIGNED INCLUDE 3/4** — `[(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG]`.

- **(a) FAIL** — Michael Sitarzewski = a disclosed notable individual industry builder (VP at an agency, Techstars, multi-product OSS author), **not Anthropic** ((a)-7 is Anthropic-only); "notable framework/repo author" is not a registered (a) axis (the exact v184 Addy Osmani / v183 Evan Bacon precedent). First Sitarzewski author → **#19 19a**. Touches the disclosed-individual-builder (a)-axis question held **operator-reviewable at N=3** per the v182 audit (Waishnav v171 / Neo Reid v174 / Jack Le v181) — Sitarzewski is a *more prominent* disclosed individual; this **reinforces but does NOT reopen** that axis. Clean FAIL, no heritage rescue.
- **(b) STRONG — keys the tier.** A library of **232 personality-driven SUBAGENTS for AI coding agents, Claude-Code-first**, dead-center on Goal #1 AND on the vault's own `05 Skills/`/`~/.claude/agents/` substrate; **immediately + safely pilotable** (local markdown file-copies, no spend/tunnel/binary/network) into both the vault and hireui (directly relevant agents: code-reviewer, frontend-developer, backend-architect, security, sprint-prioritizer, reality-checker, prompt-engineer). STRONG-not-STRONGEST = third-party + Claude one of 14 harnesses + persona-prompt-collection (not Anthropic substrate, not deep engineering). Above ponytail v168 (single ruleset); a peer to agent-skills v184 (skill collection) on the *subagent* primitive.
- **(c) STRONG** — 232 agents × ~10K+ lines / 16 divisions / a sophisticated 14-tool conversion engine (3 install-kinds; SOUL/AGENTS/IDENTITY split, SKILL.md render, TOML, roster, lazy-router plugin) / **4 CI governance gates incl. a novel semantic-originality detector** / a native Tauri Desktop App / multi-agent workflow examples / bilingual zh-CN. Caveat: the "engineering" is prompt-authoring + shell/Python tooling, and quality varies across 232 personas (niche long tail) — but at this scale + the governance machinery, STRONG-for-genre is fair.
- **(d) STRONG** — dense cross-refs (see §8).

### Pattern outcome: **1 NEW §C standalone (CORPUS-FIRST for the §C surface, N=1)**

**"Multi-Domain Personality-Driven Subagent-Persona Library"** — a large curated collection of *character-driven AI-agent personas* (name + voice/`vibe` + workflow + deliverables + success-metrics), spanning many business + engineering divisions, installed as **native subagents** (`~/.claude/agents/`) across many harnesses.

- **Why a mint, and why corpus-first for the §C surface:** the §C registry has skill-collection standalones (§C #4 Multi-Domain Skill Collection N=2 [CodexKit v121 + agent-skills v184]; khazix personal-daily-driver; Odysseus; book-to-skill) + the CONFIRMED Domain-Vertical-**Skill**-Collection (N=4) — but **no standalone for an agent/PERSONA collection**. The primitive is genuinely distinct (subagent = isolated context + own system prompt + model-invocable, per Anthropic docs; ≠ skill = injected knowledge). This is **not** a "draw-the-circle-to-make-it-first" move — the primitive boundary is real and documented. agency-agents is the corpus's clear exemplar (and its historical v18 "largest agent library" anchor), filed at **N=1 per the Kilo-Code-v177 precedent** ("mint N=1 for a recurring world-class exemplar"). The world-class **recurs** (wshobson/agents, VoltAgent) but is unrepresented by another corpus subject → cleaner instances later become credited prior data-points.
- **The mint = the CONJUNCTION:** (multi-domain / cross-functional breadth) × (personality-DRIVEN persona design, not functional skills) × (the SUBAGENT primitive specifically) × (one canonical source rendered to many harnesses). This formalizes, under the modern framework, what v18 observed as the now-defunct routine-v1 "Pattern #25 Personality-Driven Agent Design" candidate.
- **DISTINCT from:** §C #4 Multi-Domain **Skill** Collection (agent-skills v184 / CodexKit v121 — *skills*, not subagent personas) · Domain-Vertical-**Skill**-Collection N=4 (single-vertical, skills) · khazix v138 personal-daily-driver (eclectic skills) · codymaster v12 (79 functional *skills*, the prior "largest library") · ECC v1 (~12 subagents as a *harness*, not a curated multi-domain persona library). **⚠️ Audit-reviewable boundary:** whether this persona-library standalone and §C #4 (skill collection) should ever merge into one "agent-extension collection" family (they should NOT yet — the subagent-vs-skill primitive distinction is load-bearing). Recorded, deferred.

### §28 ≤2-cap honored (1 mint).

### SECONDARY observations (recorded, NOT minted)

- **Pattern #81 Manifest-Drift-as-First-Class-CI-Concern (v64 claude-seo)** — clean instance-strengthening: `check-divisions.sh` (5-way) + `check-tools.sh` (3-way) are textbook manifest-drift consistency gates. (N-bump = audit bookkeeping; recorded as a cross-reference, not self-promoted.)
- **Novel mechanism — automated semantic-originality CI gate** (`check-agent-originality.sh`: entity-neutralized 8-word-shingle Jaccard, FAIL ≥40%) — a genuinely novel anti-duplication gate for a curated agent library; possibly corpus-first as a *mechanism*. Recorded as an **audit-watch sub-observation**, NOT a separate mint (§28 ≤2 cap + it's a feature-of-the-subject, not yet a recurring class).
- **Library-vocab #22 Tauri-Desktop Management-GUI for a Coding Agent (N=3)** — the Desktop App (`agency-agents-app`, Rust+Tauri 2) is a Tauri desktop GUI, **but** #22's tight claim is "manage/control the OPERATION of another coding agent — its provider/session/account." agency-agents-app manages the **persona-catalog install/tracking**, a *different axis* → **ADJACENT, NOT a clean N+1** (the v118 OpenHuman honest-downgrade precedent). Recorded as a cross-reference + audit-reviewable; **NO N-bump**.
- **Library-vocab #20 Token-Economy-Quantification** QUALIFIED-ADJACENT — the Hermes lazy-router (search/inspect/load/delegate over on-disk JSON, avoids preloading 232 agents) is a token-economy move but no quantified benchmark → **N stays 4** (the v168/v172/v175 precedent).
- **#84 84c Provider-Agnostic-By-Design** — one canonical `.md` → 14 harness-native formats via `convert.sh` = a clean 84c instance (generator renders native formats; cross-ref ponytail v168 + wshobson). **NO N-bump** per v86; NOT the "14-platform rule-distribution contamination."
- **#12 LLM-routing-artifacts** — the agents ARE the routing artifacts (`.claude/agents/*.md`, `.cursor/rules/*.mdc`, SOUL/AGENTS/IDENTITY) + `divisions.json`/`tools.json` manifests. Incidental instance; **NO N-bump**.
- **#66 supply-chain/dual-use** — install is benign (no network/binary/curl|bash) but writes up to 232 files into config dirs + modifies `~/.hermes/config.yaml`; personas are non-executable prompts but reviewable for prompt-injection surface → balanced cross-reference + pilot fence (install selectively).

### NON-claims

NOT a new top-level pattern (max stays **#85**) · NOT **#52** (119K★/19.5K forks page-stated, **NOT API-verified §37.4** → velocity unestablishable; the "10K★ in 7 days" / "+23.2K★/week" / "fastest-growing" reports are page-stated, recorded as remarkable engagement, not a verified-velocity #52 claim) · NOT **#18 B1-MCP** (a persona library + shell installer + Tauri app + a Hermes-specific router *plugin* — not an MCP server) · NOT corpus-first-of-class globally (wshobson/agents + VoltAgent peers; claim scoped to the corpus §C surface) · NOT **#57** (Reddit origin + peer mentions; cites no corpus subjects as influences).

### Tier: **T1 — Agent/Persona/Skill Collection** (the karpathy-skills v63 / mattpocock v57 / CodexKit v121 / khazix v138 / agent-skills v184 family — the *subagent-persona* flavor).

### Counts + streak
- Confirmed top-level patterns **46** (unchanged); CONFIRMED Library-vocab **11** (unchanged).
- §C live standalones **30 → 31** (+1 mint); tracked PROVISIONAL surface **≈37 → ≈38**.
- Streak **`GA:45 · OG:11 [7 ov]` → `GA:46 · OG:11 [7 ov]`** (GOAL-ALIGNED ship; v176-OFF-GOAL reading → GA:45·OG:12).
- §35 CLEAR — window {v183 GA, v184 GA, **v185 GA**} = 0 OG (v182 audit excluded). **31 consecutive goal-aligned ships v153→v185** (GA reading).
- **inflation_check = discipline HELD** — 1 mint (≤2 cap), N=1 (corpus-first §C surface, world-class recurs), max #85, counts 46/11 unchanged, no double-count, primitive-distinction defeats draw-the-circle.

---

## 8. Cross-references

Skill/agent-collection family: agent-skills v184 · CodexKit v121 · karpathy-skills v63 · mattpocock v57 · khazix v138 · Superpowers · agent-skills-standard v76 · codymaster v12 (prior "largest library", functional skills). Subagent peers (landscape, not corpus): wshobson/agents · VoltAgent/awesome-claude-code-subagents. Manifest-drift CI: claude-seo v64 (#81). Tauri management-GUI: cc-switch v73 / CodexPlusPlus v117 / ai-switcher v153 (LV#22). Multi-agent orchestration: the operator's `multi-agent-orchestration` pilot thread. Code-minimalism: ponytail v168 (the `minimal-change-engineer` agent echoes it). Quality-gate: the Reality Checker ↔ the operator's `feedback_wiki_verify_independently` + `prompt-evaluation` threads.

→ **Pilot Methods:** see `(C) agency-agents — Pilot Methods Menu.md` (24 methods).
