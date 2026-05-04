# Rowboat - Beginner Analysis — CLAUDE.md

> **Project type:** LLM Wiki — v43 Storm Bear corpus
> **Source:** https://github.com/rowboatlabs/rowboat (cloned to `00 Source/rowboat/`)
> **Routine:** `llm-wiki-routine-v2.1.md` (5th v2.1-era + 7th in routine maturity arc)
> **Status:** ✅ v1 shipped 2026-04-24

---

## Phase 0: 12-axis classification

| Axis | Value |
|------|-------|
| **Tier** | **T5 Agent-as-application — 8TH T5 ENTRANT** + NEW personal-productivity-application sub-archetype |
| **Archetype** | YC-backed commercial-startup + OSS-Apache + privacy-first-local-first + multi-integration + Electron desktop + dual-product-in-monorepo (legacy SaaS `apps/rowboat` + new flagship Electron `apps/x` + `apps/rowboatx` CLI sibling) |
| **Scale tier** | Medium (13,056 stars / ~15.5 months ≈ 840 stars/month sustained-organic) |
| **Primary lang** | TypeScript 96.7% (Electron + React 19 + Vite 7 + Next.js multi-app monorepo + pnpm workspaces) |
| **Packaging** | 3-platform desktop binaries (Mac DMG / Windows .exe / Linux) + Docker compose (legacy SaaS) + npm `@rowboatlabs/rowboatx` v0.16.0 + PyPI `rowboat` v5.0.1 = **4-surface distribution corpus-first at T5** |
| **Origin story** | YC S24 batch startup (Rowboat Labs, 2025-01-13 GitHub creation) + product-pivot-in-monorepo (multi-agent SaaS → personal-AI-coworker) |
| **Methodology** | Knowledge-graph-as-Markdown (Obsidian-compatible) + local-first + bring-your-own-model + Track Blocks (live YAML-fenced auto-updating notes — corpus-first) |
| **Governance** | Light-medium (README + CLAUDE.md 5.4KB + LICENSE Apache-2.0 + google-setup.md 3.9KB + start.sh + build-electron.sh; absent CONTRIBUTING + SECURITY + CODE_OF_CONDUCT + AGENTS.md = standard YC-startup-early-stage) |
| **Agent/skill count** | Medium-high primitive-count: 6 user-configurable integrations + ~7 monorepo apps + ~35 knowledge-system modules + Track Blocks (4 trigger types) + Cmd+K Copilot + voice memo + meeting prep + PDF-deck-gen + 5 specialized agents (note_creation / labeling / inline_task / note_tagging / track-run) + Pass-1/Pass-2 routing classifier |
| **i18n** | EN-only (no VN/CN/JA/KO; notable absence at 13K T5 startup-stage) |
| **Intellectual influence** | Implicit Karpathy-LLM-Wiki + Obsidian-vault structural parallel ("Obsidian-compatible vault of plain Markdown notes with backlinks — a transparent working memory you can inspect and edit"). NOT explicitly cited. **Pattern #19 archetype 1 implicit-Karpathy-touchpoint** (observational; corpus-first implicit-not-explicit Karpathy structural parallel at T5) |
| **Agent platforms** | Bring-your-own-model (Ollama / LM Studio / OpenAI / Anthropic / Google / OpenRouter via Vercel AI SDK + Vercel AI Gateway) + MCP server bidirectional + Composio external tools + Klavis (cloud agent infra) + Auth0 (legacy SaaS) |

## Phase 0.5 Pattern pre-check

### Strengthening (target: 0 new active candidates — 7th consecutive streak)

1. **Pattern #17 Ecosystem-Layer variant 3 commercial-startup** — 14th data point (Rowboat Labs YC-S24 + 4-surface distribution + dual-product-in-monorepo). Within-pattern strengthening; do NOT register YC-S24 as sub-variant standalone.

2. **Pattern #19 Intellectual Lineage archetype 1 (Karpathy implicit)** — observational data point. Knowledge-graph-as-Markdown structurally parallel to Karpathy /raw folder + Storm Bear LLM-Wiki vault, but NOT explicitly cited. Document as **observational Karpathy-touchpoint at T5 + corpus-first implicit-not-explicit lineage observation** within Pattern #19 (do NOT register standalone).

3. **Pattern #31 Open-Core Commercial Entity** — N=7 strengthening (Rowboat Labs commercial entity + OSS Apache-2.0 + free downloads landing — open-core-with-undeclared-paid-tier observed; commercial entity exists but landing page minimal so can't confirm SaaS tier yet).

4. **Pattern #50 Commercial-Funnel Companion Platform** — N=6 strengthening (rowboatlabs.com + downloads page + Discord + YouTube demo + Twitter @rowboatlabshq + Trendshift badge + YC badge — 5+ funnel surfaces).

5. **Pattern #18 MCP Agent Runtime** — Tier-1-basic data point (1-5 tools per v42-mini-audit codification). MCP support documented but tool-count not surfaced. **Bidirectional**: MCP server (rowboat exposes tools) + MCP client (rowboat consumes external MCP servers).

6. **Pattern #28 Multi-Provider AI Support** — 11th data point. Vercel AI SDK + Anthropic + OpenAI + Google + OpenRouter + Ollama + LM Studio + Vercel AI Gateway. ~7+ providers. Strong native + abstraction-layer hybrid.

7. **Pattern #27 Community-Viral Scale Path** — 19th observation (T5 sustained-organic ~840 stars/month over 15.5 months; YC-amplified-community sub-path).

8. **Pattern #22 AGENTS.md** — observation: CLAUDE.md present (5.4KB), AGENTS.md ABSENT. T5 YC-startup-early CLAUDE-only convention. Counter-evidence to "AGENTS.md as industry standard."

9. **Pattern #12 Governance-Depth (refined v42)** — YC-startup-early-stage minimal-governance data point (no SECURITY / CODE_OF_CONDUCT / CONTRIBUTING). Refined formulation post-v42: governance-depth correlates with maturity-ambition + maintainer-philosophy + scale-tier. Rowboat's 13K-medium-scale + early-startup-ambition + 3-engineer-team = light governance fits refined formulation.

10. **Pattern #58 Branding-Package Divergence (CONFIRMED v42)** — 3rd data point candidate? Repo is `rowboat` but contains 3 distinct npm packages: `@rowboatlabs/rowboatx` (v0.16.0 CLI) + `rowboat` (PyPI v5.0.1 SDK) + Electron app `x` (no published name yet). Different from 58a (oh-my-claudecode rename) + 58b (ruflo rebrand-with-transitional). **Observational — product-pivot-divergence sub-variant observation.**

### Counter-evidence checks

- **Pattern #22 AGENTS.md** — CLAUDE.md present, AGENTS.md absent. T5 YC-startup data point. Ruflo v42 had AGENTS.md (Codex-primary), pi-mono v36 had AGENTS.md. Rowboat's CLAUDE.md-only choice = Anthropic-aligned-runtime (consistent with `claude-code` + `claude-cowork` topics).
- **Pattern #12 Governance-Depth (refined)** — YC-startup-early data point reinforces refined formulation.

### Un-stale check

- **#45 Dual-Licensing Strategy** (stale v33) — NEGATIVE (rowboat single Apache-2.0)
- **#52 Extreme-Viral-Velocity** (stale v36) — NEGATIVE (rowboat 13K/15.5mo = 840/mo organic, not extreme)
- **#71 Interactive Self-Assessment** (stale-risk v37) — NEGATIVE
- **#72 PolyForm Noncommercial** (stale-risk v38) — NEGATIVE (Apache-2.0 confirmed)
- All retired-revivals — NEGATIVE

### Overlap pre-check potential observations

| Potential standalone | Decision | Routing |
|---|---|---|
| YC-S24-batch explicit acknowledgment as project-level badge | NOT registered | Within-Pattern-#17 variant 3 strengthening data point |
| Knowledge-graph-as-Markdown = Karpathy/Storm-Bear peer | NOT registered | Within-Pattern-#19 archetype 1 implicit-touchpoint observation |
| 3-platform desktop-binary distribution at T5 | NOT registered | Within-Pattern-#2 Distribution Evolution observation |
| Composio integration = external-tool-marketplace | NOT registered | Within-Pattern-#18 (external-tool-marketplace observational layer) |
| Qdrant vector DB | NOT registered | Architectural detail (vector-DB choice, not structural pattern) |
| Track Blocks (YAML-fenced live-updating notes) | NOT registered | Architectural primitive within knowledge-graph entity; novel-but-N=1 |
| Product-pivot-in-monorepo (legacy rowboat → x Electron) | NOT registered | Observational variant of Pattern #58 (3rd data point candidate; observational) |
| 4-surface distribution at T5 (desktop + Docker + npm + PyPI) | NOT registered | Within-Pattern-#2 corpus-first 4-surface T5 observation |

**Outcome target:** 0 new active candidates → 7th consecutive zero-registration wiki (unprecedented streak v37+v38+v39+v40+v41+v42+v43).

## Phase 0.9 Primitive-count probe

- README TOC top-level: 9 sections (Demo / Installation / What it does / Integrations / How it's different / What you can do / Live notes / Bring your own model / Extend with MCP / Local-first)
- Repo folder top-level apps: 7 (cli / docs / experimental / python-sdk / rowboat / rowboatx / x) — but only 3 are flagship-relevant (`x` Electron + `rowboatx` CLI + `python-sdk`)
- `apps/x/packages/core/src/` declared modules: 22 sub-systems (account / agent-schedule / agents / application / auth / billing / composio / config / di / knowledge / local-sites / mcp / models / pre_built / runs / search / services / slack / voice / workspace + index)
- `apps/x/packages/core/src/knowledge/` files: 35 TypeScript modules
- 6 user-configurable integrations (Google / Deepgram / ElevenLabs / Exa / Composio / MCP)
- Track Blocks subsystem: 4 trigger types + 8 prompts in catalog + 5+ files

**Probed primitive-count:** ~30-50 distinct primitives (similar to GitNexus v33 / OpenHands v30 zone; below ruflo v42 EXTREME ~500+ but above pi-mono v36 YELLOW ~150-200 baseline)

**Outcome: YELLOW (2nd YELLOW after pi-mono v36)** — 4-entity format with strategic compression:
- Entity 1: Core product (rowboat knowledge-graph-personal-AI-coworker = `apps/x` Electron flagship + Track Blocks + voice + integrations)
- Entity 2: Architecture + Distribution (4-surface + dual-product-in-monorepo + Rowboat Labs YC-S24 commercial)
- Entity 3: T5 8-way comparison + personal-productivity-application sub-archetype + Storm Bear direct-peer-category analysis
- Entity 4: 32nd consecutive Storm Bear meta-entity (Karpathy implicit-touchpoint extends to N=7+; vault peer-category)

**Lossy compression accepted:** apps/rowboat (legacy SaaS) covered briefly in Entity 2; apps/cli + apps/docs + apps/experimental cited not enumerated; apps/rowboatx CLI specifics cited not deeply explored. Track Blocks given dedicated Section in Entity 1 (corpus-first scheduling architecture warrants depth).

**Velocity overhead estimate:** ~2h 30min (YELLOW preserves plateau as pi-mono v36 demonstrated).

## Phase 4b routing mode

**Primary mode:** T5 N-way extension (N=7 → N=8) + new sub-archetype emergence (personal-productivity-application)

**Secondary modes:**
- Storm Bear direct-peer-category analysis (knowledge-graph-as-Markdown structurally parallel to vault)
- Karpathy implicit-touchpoint at T5 (within-Pattern-#19 observation; first implicit-not-explicit Karpathy structural parallel)
- Pattern #17 variant 3 13th-14th strengthening data point (YC-S24 commercial-startup observation)

**Single deliverable:** `(C) T5 8-way + personal-productivity-application + Storm Bear direct-peer.md`

## Cross-references

**Closest peers:**
- **v38 DeepTutor** — T5 education-application academic-lab; 9-language i18n contrast (rowboat EN-only)
- **v14 paperclip** — T5 orchestration; 55.9K community-platform; "zero-human companies" autonomy-max contrast (rowboat human-augmentation framing)
- **v15 multica** — 1st Electron in corpus T2 managed-agents-platform; rowboat 2nd Electron + T5 personal-productivity
- **v3 gstack** — Garry Tan YC-individual-context (NOT YC-batch); rowboat Rowboat-Labs YC-S24-batch (corpus-first explicit YC-batch project-level signal)
- **v30 OpenHands** — T5 SWE-agent + commercial-entity + open-core; rowboat T5 personal-productivity + commercial + open-core
- **v8 build-your-own-x** — implicit Karpathy alignment lineage; rowboat implicit Karpathy structural parallel (no citation)

**T5 8-way roster post-v43:**
1. v9 deer-flow (corporate research T5)
2. v10 autoresearch (solo Karpathy ML T5; explicit Karpathy)
3. v14 paperclip (community-platform orchestration T5)
4. v24 Skyvern (commercial browser-agent T5)
5. v30 OpenHands (academic-commercial SWE-agent T5)
6. v38 DeepTutor (academic-lab education T5)
7. v41 browser-use (commercial browser-agent T5)
8. **v43 rowboat (YC-S24 personal-productivity-application T5 — NEW)**

**100% archetype diversity preserved at N=8** — every T5 entrant has distinct organizational/product archetype.

## Phase 5 Pattern Library targets

- 0 new active candidates (7-streak target)
- 0 new OBSERVATION-TRACKs
- ~10 strengthening data points across confirmed patterns
- Implicit-Karpathy-touchpoint observation documented within Pattern #19 (do NOT register standalone)
- Maintain ratio at 0.54:1 (UNPRECEDENTED post-v42-deferred mini-audit baseline)

## Storm Bear pilot relevance

**HIGH — NEW #1** (displaces claude-howto v32 and claude-hud v35):

Knowledge-graph-as-Markdown architecture is the **most direct peer-category match in 43 wikis**. Rowboat IS structurally what Storm Bear vault is, automated with personal AI. Direct evaluation pathway:

1. Install Mac DMG (5-minute zero-friction)
2. Connect Gmail + Calendar
3. Point at existing Storm Bear vault OR fresh test vault
4. Run 1-week parallel comparison: rowboat-managed knowledge-graph vs Storm-Bear-curated wiki
5. Decision: adopt / hybrid / reject

**Key strategic question:** Does automated AI-coworker compound knowledge faster than manually-curated LLM Wiki pattern? Rowboat is empirical test of "automate the wiki maintainer role" thesis.

**Caveats:** Apache-2.0 OK / 3-engineer-team bus-factor / YC-startup-stage-instability / EN-only (VN client docs untested) / model-cost-management / data-leaves-machine-via-LLM-API (mitigated by Ollama local-model option).

---

## Project deliverables checklist

- [x] Phase 0 — 12-axis + pattern pre-check + primitive-count YELLOW
- [x] Phase 1 — Scaffold (8 subfolders + foundational files)
- [x] Phase 2 — 3 cluster summaries
- [x] Phase 3 — 4 entity pages (32nd Storm Bear meta-entity)
- [x] Phase 4a — Bilingual VN+EN beginner guide (HIGH Storm Bear relevance framing)
- [x] Phase 4b — T5 8-way + personal-productivity-application + Storm Bear direct-peer-category deliverable
- [x] Phase 5 — Iteration log v43 + Pattern Library updates (target 0 new active)
- [x] Phase 6 — Vault sync (root CLAUDE / GOALS / PATTERN_LIBRARY) + fact-verification

---

**Routine:** v2.1 | **Routine execution #:** 7th v2.1-era | **Wiki #:** 43 (Storm Bear corpus) | **Velocity target:** ~2h 30min YELLOW
