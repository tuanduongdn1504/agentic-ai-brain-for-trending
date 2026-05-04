# (C) Entity 3 — T5 personal-productivity-application sub-archetype + Storm Bear direct-peer-category

**Source scope:** T5 8-way comparison across all T5 entrants + Storm Bear vault structural parallel analysis + Karpathy implicit-touchpoint observation + sub-archetype formalization

## 1. T5 roster post-v43 (N=8 — largest 3-tier milestone after T1 N=13 and T4 N=8)

| # | Wiki | Name | Org archetype | Scale | Domain |
|---|---|---|---|---|---|
| 1 | v9 | deer-flow | Corporate (ByteDance) | 71K | Research/deep-agent |
| 2 | v10 | autoresearch | Solo (Karpathy) | 74K | ML research |
| 3 | v14 | paperclip | Community-platform (paperclipai) | 55.9K | Orchestration (zero-human framing) |
| 4 | v24 | Skyvern | Commercial-startup (Skyvern-AI) | 21K | Browser automation |
| 5 | v30 | OpenHands | Academic-commercial fusion (All Hands AI + UIUC/CMU) | 71.7K | SWE-agent |
| 6 | v38 | DeepTutor | Academic-lab (HKU/HKUDS) | ~10K | Education |
| 7 | v41 | browser-use | Commercial-startup (Zurich+SF 2-founder) | 89.9K | Browser automation |
| 8 | **v43** | **rowboat** | **YC-S24-commercial-startup (Rowboat Labs)** | **13K** | **Personal productivity** |

**100% archetype diversity preserved at N=8** — every T5 entrant has distinct organizational/product archetype.

## 2. NEW sub-archetype: personal-productivity-application

**Rowboat introduces 8th distinct T5 sub-archetype:**

| T5 sub-archetype | Entrants | Defining characteristic |
|---|---|---|
| Research-deep-agent | deer-flow v9 | Long-horizon autonomous research tasks |
| ML-research-framework | autoresearch v10 | Single-GPU overnight optimization |
| Orchestration-harness | paperclip v14 | Zero-human-companies multi-model orchestration |
| Browser-automation-vision | Skyvern v24 | Vision-based DOM-free browser automation |
| SWE-agent | OpenHands v30 | Code-writing software engineering agent |
| Education-application | DeepTutor v38 | Academic paper tutor/explainer |
| Browser-automation-hybrid | browser-use v41 | Hybrid DOM+vision browser automation |
| **Personal-productivity-application** | **rowboat v43** | **Local-first knowledge-graph-with-coworker-AI** |

**Sub-archetype formal definition:**
> T5 personal-productivity-application = application deployed to end-user device/OS, operates on user's personal data (emails, calendar, notes, meeting transcripts), maintains persistent knowledge artifact (markdown vault / knowledge graph / personal wiki), augments user's own work (not substitutes autonomous agent), local-first data stewardship. Distinguished from browser-automation-agents (external website interaction) and SWE-agents (code-writing focus) and research-agents (information-discovery focus) by operating-on-user's-own-data-for-user's-own-work scope.

**Structural-uniqueness-at-N=1:** rowboat is corpus-first at this sub-archetype. Future data points would strengthen (Mem0, Letta, MemGPT, Khoj if they become Storm Bear wiki subjects).

## 3. Storm Bear direct-peer-category analysis

**Structural parallel:**

| Dimension | Storm Bear vault | Rowboat |
|---|---|---|
| Storage | Plain Markdown + Obsidian properties | Plain Markdown + Obsidian-compatible backlinks |
| Maintainer | Human operator (Storm Bear) + Claude (LLM Wiki pattern) | AI coworker (Rowboat Copilot) + human oversight |
| Context accumulation | Explicit entity pages + cross-references + iteration logs | Knowledge graph + live-updating track blocks |
| Query pathway | Claude reads vault files + cross-references | Copilot reads local vault + MCP tools + scheduled tracks |
| Data sovereignty | Local Obsidian vault (operator-managed) | Local Markdown vault at `~/.rowboat/` (user-managed) |
| Update mechanism | Operator-invoked Claude skills + manual edits | Copilot + scheduled tracks + event-driven syncs + voice memos |
| Intellectual origin | Karpathy LLM Wiki pattern (explicit) | Knowledge-graph-as-Markdown + Obsidian parallel (implicit Karpathy) |

**Corpus-first observation:** Rowboat is the **most direct peer-category match in 43 wikis** for Storm Bear vault's core architecture. Both maintain local Markdown knowledge graphs with LLM-augmented workflows. Divergence is in **who maintains the graph**:
- Storm Bear: human-maintainer-driven (operator curates, Claude assists via skills)
- Rowboat: AI-maintainer-driven (Copilot curates, human reviews/edits)

**This divergence encodes the empirical test:** Does automated AI-coworker compound knowledge faster than manually-curated LLM Wiki pattern? Rowboat is empirical test of "automate the wiki maintainer role" thesis.

## 4. Karpathy implicit-touchpoint observation (Pattern #19 strengthening)

**Explicit Karpathy touchpoints in corpus (6 prior):**
1. v1 ECC Beginner Analysis — Karpathy LLM Wiki pattern as vault foundation
2. v2 Superpowers — Karpathy-adjacent methodology
3. v10 autoresearch — Karpathy's own repo
4. v16 graphify — explicit Karpathy `/raw folder` citation
5. v8 build-your-own-x — Feynman alignment adjacent to Karpathy
6. (various project-level CLAUDE.md references)

**Rowboat (implicit, 7th+):**
- Verbatim README: *"Under the hood, Rowboat maintains an **Obsidian-compatible vault of plain Markdown notes with backlinks** — a transparent 'working memory' you can inspect and edit."*
- Verbatim: *"The result is **memory that compounds**, rather than retrieval that starts cold every time."*

**Structural parallel without explicit citation:**
- Knowledge-graph-as-Markdown = Karpathy /raw folder primitive
- Memory-compounds framing = Karpathy LLM Wiki pattern claim
- Obsidian-compatible = Storm Bear vault choice

**No explicit Karpathy citation** in README / CLAUDE.md / repo docs. Rowboat Labs may have arrived at architecture independently or implicitly-from-Karpathy-influence-in-broader-zeitgeist.

**Pattern #19 archetype 1 observational refinement** (within-pattern, no standalone registration):
- Sub-observation: implicit-structural-parallel (rowboat v43) vs explicit-citation (autoresearch v10 / graphify v16 / ECC v1)
- **Corpus-first implicit-not-explicit Karpathy structural parallel at T5**

## 5. T5 8-way comparison matrix (20 axes)

| Axis | deer-flow v9 | autoresearch v10 | paperclip v14 | Skyvern v24 | OpenHands v30 | DeepTutor v38 | browser-use v41 | rowboat v43 |
|---|---|---|---|---|---|---|---|---|
| Stars (K) | 71 | 74 | 55.9 | 21 | 71.7 | ~10 | 89.9 | 13 |
| License | MIT | MIT | MIT | AGPL-3.0 | MIT core + separate enterprise | MIT | MIT | Apache-2.0 |
| Primary lang | Python + TS | Python | TS 97.4% | Python + TS | Python 71% + TS 27% | Python | Python | TS 96.7% |
| Org archetype | Corporate | Solo (Karpathy) | Community-platform | Commercial | Academic-commercial fusion | Academic-lab | Commercial (2-founder) | YC-S24 startup |
| YC connection | No | No | No | Unclear | Through founders | No | No | **S24 batch (corpus-first explicit)** |
| Scale-archetype | Corporate-backed | Solo-specialist | Community-viral | Commercial-proprietary | Academic-commercial | Academic-research | Commercial-duo-founder | YC-startup-community |
| Primary surface | Docker + Web | Single GPU script | Docker | Cloud + OSS | SDK + CLI + GUI + Cloud + Enterprise (5) | Streamlit web | pip + Cloud | Desktop binary + Docker + npm + PyPI (4 OSS) |
| Distribution surfaces | 2 | 1 | 1 | 2 | 5 | 1 | 2 | 4 |
| AI providers | Multiple (~10) | Custom | Multiple | OpenAI/Anthropic primary | Multiple (~8) | OpenAI primary | 15+ native + LiteLLM | 6 native + Vercel AI Gateway + Ollama + LM Studio |
| MCP integration | No | No | No | No | Yes (built-in) | No | Yes (bidirectional + DXT packaging) | Yes (implied bidirectional) |
| Autonomy framing | Long-horizon research | Overnight-ML | "Zero-human companies" | Commercial browser-agent | Software engineering | Academic-tutor | Browser-task-automation | **AI-coworker (human-augmentation)** |
| Data location | Cloud + local | Local GPU | User-controlled | Cloud primary | User-controlled | Cloud | Cloud or user | **Local Markdown vault** |
| i18n | EN | EN | EN | EN + some | EN | **9 languages** | EN | EN |
| Age (months) | ~18 | ~15 | ~14 | ~14 | ~25 | ~6 | ~18 | ~15.5 |
| Velocity (stars/mo) | ~3.9K | ~4.9K | ~4K | ~1.5K | ~2.9K | ~1.6K | ~5K | ~840 |
| Karpathy touchpoint | No | **Source (explicit)** | No | No | No | No | No | **Implicit structural parallel** |
| Governance files | Medium | Light | Heavy (5 invariants + 4 governance) | Light | Heavy (academic+corporate) | Academic | Heavy | Light (CLAUDE.md only) |
| AGENTS.md | No | No | No | No | No | No | Yes (37.4KB) | **No (CLAUDE.md only)** |
| Commercial funnel | Corporate | None | Community | Commercial Cloud | Open-core enterprise | Academic-lab | Commercial Cloud | **7-surface YC-amplified** |
| Storm Bear relevance | LOW | MEDIUM (lineage) | LOW | LOW | MEDIUM (workflows) | LOW | LOW | **HIGH #1 (direct peer-category)** |

**Key observations from matrix:**

1. **rowboat is smallest scale among T5 commercials** (13K vs 21-89.9K range) — YC-stage pre-critical-mass
2. **rowboat is only T5 with 4-OSS-only-surfaces** (distinct from OpenHands' commercial-heavy 5)
3. **rowboat is only T5 where "personal-productivity-application" applies** (vs research/ML/SWE/browser/education domains)
4. **rowboat is only T5 with explicit YC-batch acknowledgment** (corpus-first)
5. **rowboat is only T5 with "AI coworker" primary noun** (vs agent/assistant common framing)
6. **rowboat is 2nd T5 with Karpathy touchpoint** (after autoresearch v10), but implicit-not-explicit (corpus-first)
7. **rowboat has most-direct Storm Bear structural parallel** of all T5 wikis

## 6. Storm Bear pilot evaluation framework

**Pilot ranking post-v43 update:**

| Rank | Project | Relevance | Reason |
|---|---|---|---|
| **1** 🆕 | **rowboat v43** | **HIGH direct peer-category** | Knowledge-graph-as-Markdown structural parallel; empirical test of "automate wiki maintenance" thesis; 5-min install; 1-week evaluation |
| 2 | claude-hud v35 | HIGH | Claude Code statusline utility |
| 3 | spec-kit v17 | HIGH methodology | SDD discipline for Scrum workflows |
| 4 | claude-howto v32 | HIGH self-onboarding | VN-diaspora tutorial |
| 5 | OMC v27 | HIGH | Multi-runtime orchestration |
| 6 | pi-mono v36 | MEDIUM-HIGH | Claude-Code alternative |
| 7-10 | Various | Various | Existing rankings |

**Why rowboat ranks #1:**

1. **Direct architectural peer** — both maintain local Markdown knowledge graphs
2. **Zero-commitment evaluation** — Apache-2.0, no subscription, 5-minute install, uninstallable
3. **Empirical value regardless of outcome:**
   - If rowboat-better: adopt for vault maintenance (paradigm shift in Storm Bear workflow)
   - If rowboat-similar: validates LLM Wiki pattern against pivoted industry approach
   - If Storm Bear-better: confirms manual curation discipline's value; observations compound pattern library
4. **Non-disruptive testing** — can point at test vault, not Storm Bear primary vault

**Pilot evaluation protocol (proposed):**

Week 1:
- Install Mac DMG
- Connect Gmail + Calendar
- Point at fresh test vault (not Storm Bear primary)
- Observe knowledge-graph build: how does rowboat organize entities?
- Compare to Storm Bear entity-page format (13-section canonical)

Week 2:
- Test Track Blocks: create 3 scheduled tracks + 2 event-driven tracks
- Compare to manual Storm Bear iteration logs + update cadence
- Test voice memo workflow: does voice-to-knowledge-graph match Storm Bear manual note entry?
- Test "prep me for meeting" query: quality of brief generation

Week 3-4 (if evaluation continues):
- Point rowboat at Storm Bear primary vault (read-only test)
- Does rowboat respect Storm Bear naming conventions + cross-references?
- Does rowboat's auto-tagging conflict with Obsidian property syntax?
- Decision point: adopt / hybrid / reject

## 7. Comparison axis: human-maintainer vs AI-maintainer knowledge graph

**Storm Bear (human-maintainer):**
- Pro: Quality-controlled, intentional, cross-references deliberate
- Pro: Operator develops domain expertise through curation
- Pro: No false-positive knowledge claims
- Pro: Pattern Library (Storm Bear meta-structure) emerges from human cognition
- Con: Slow — velocity bottlenecked by operator time (~2h per wiki)
- Con: Doesn't compound during operator's off-hours
- Con: Operator-bus-factor = 1

**Rowboat (AI-maintainer):**
- Pro: Fast — knowledge graph auto-updates continuously
- Pro: Compounds 24/7 (scheduled tracks + event-driven syncs)
- Pro: Scales with integration count (more data sources → richer graph)
- Con: Quality variable — LLM hallucinations enter graph
- Con: No intentional cross-reference discipline (entity extraction ≠ pattern observation)
- Con: Operator loses domain expertise development (outsources thinking)
- Con: Dependent on Rowboat Labs product continuity (YC-stage bus-factor)

**Hybrid possibility:** Use rowboat for continuous-integration knowledge (emails / calendar / meetings auto-graph) + Storm Bear LLM Wiki pattern for deliberate-research (projects / entity pages / iteration logs). Track Blocks could live in Storm Bear vault via manual convention if proved valuable.

## 8. Corpus-first observations (Entity 3 tally)

| # | Observation |
|---|---|
| 1 | T5 8-way + 100% archetype diversity preserved at N=8 |
| 2 | Personal-productivity-application = NEW 8th T5 sub-archetype |
| 3 | Corpus-first implicit-not-explicit Karpathy structural parallel at T5 |
| 4 | Most-direct Storm Bear peer-category in 43 wikis |
| 5 | Corpus-first YC-S24-batch explicit project-level acknowledgment |
| 6 | Corpus-first "AI coworker" primary noun at T5 |
| 7 | Corpus-first 4-OSS-only-surfaces at T5 |
| 8 | Empirical test pathway: automated-AI-wiki-maintainer vs human-LLM-Wiki-pattern |

## 9. Pattern cross-references

- **Pattern #17 variant 3 commercial-startup** — 14th data point with YC-S24-batch sub-observation (observational, within-pattern)
- **Pattern #19 archetype 1 (Karpathy)** — 7th+ touchpoint; corpus-first implicit-not-explicit sub-observation
- **Pattern #27 Community-Viral** — 19th observation, YC-S24-amplified-community sub-path
- **Pattern #50 Commercial-Funnel** — 6th data point, 7-surface ties ruflo v42
- **Pattern #28 Multi-Provider** — 11th data point, 6 native + abstraction + local
- **Pattern #31 Open-Core** — 7th data point, sub-classification 31c (undeclared-monetization)
- **Pattern #22 AGENTS.md** — counter-evidence (CLAUDE.md-only at T5 YC-startup)

## 10. Strategic implications for Storm Bear vault

1. **Evaluate rowboat as parallel-pilot** (not replacement) — 1-week test-vault experiment = LOW cost, HIGH information value
2. **Track Blocks as YAML-fenced-live-updating-notes convention** could be adapted manually in Storm Bear vault if rowboat's approach proves valuable (even without adopting rowboat itself)
3. **Standardized config format** (`{ "apiKey": "<key>" }`) — lesson for Storm Bear skill library: standardize integration interfaces
4. **2-pass LLM classifier** (liberal Pass 1 + strict Pass 2 veto) = pattern template for Storm Bear event-driven workflows (e.g., auto-audit trigger for Pattern Library)
5. **Product-pivot-in-monorepo observation** — lesson for any Storm Bear future products: how to preserve legacy while shipping new

## Cross-references

- **v10 autoresearch** — Karpathy explicit origin; rowboat implicit
- **v1 ECC / v2 Superpowers** — foundational corpus context
- **v8 build-your-own-x** — Feynman alignment lineage; rowboat structural parallel
- **v16 graphify** — explicit Karpathy `/raw folder` citation; rowboat implicit Obsidian-parallel
