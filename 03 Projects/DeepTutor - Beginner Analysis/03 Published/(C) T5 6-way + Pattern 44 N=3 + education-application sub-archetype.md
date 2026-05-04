# (C) T5 6-way comparison + Pattern #44 Academic-Lab N=3 strengthening + education-application T5 sub-archetype formalization

> **Deliverable type:** Phase 4b primary output for v38 wiki build.
> **Primary mode:** Tier extension + Pattern strengthening + new sub-archetype formalization.
> **Secondary mode:** Bilateral runtime-and-skill corpus-first + 9-language top-tier T5.
> **Length target:** ~700 lines.

---

## Part 1 — Tier 5 Agent-as-application 6-way comparison

T5 "Agent-as-application" is the standalone-runnable-agent-platform tier. DeepTutor v38 is the 6th entrant. **T5 preserves 100% archetype-diversity-per-wiki** across all 6 entrants (each is a distinct organizational archetype + scope combination).

### 1.1 T5 entrant table

| # | Wiki | Framework | Stars | Created | Scope | Organizational archetype |
|---|------|-----------|-------|---------|-------|--------------------------|
| 1 | v9 | deer-flow | 62,000 | 2025 | Research-assistant (long-horizon autonomous) | Corporate (ByteDance) |
| 2 | v10 | autoresearch | 74,000 | 2026-early | Autonomous ML research (nanochat training) | Solo-known (Karpathy) |
| 3 | v14 | paperclip | 55,900 | 2025 | Orchestration platform ("zero-human companies") | Community-platform (no disclosed backing) |
| 4 | v24 | Skyvern | 21,281 | 2024-02 | Browser-automation | Commercial-entity (Skyvern-AI; AGPL + Cloud) |
| 5 | v30 | OpenHands | 71,704 | 2024-03 | SWE-agent (code-generation) | Academic-commercial (UIUC+CMU + All Hands AI + ICLR 2025) |
| 6 | **v38** | **DeepTutor** | **21,230** | **2025-12** | **Education-application (personalized tutoring)** | **Academic-lab-ecosystem-portfolio (HKUDS + arXiv-pending)** |

**Total T5 combined:** ~306K stars (previously ~285K at v30); DeepTutor adds 21.2K.

### 1.2 20-axis comparison

| Axis | deer-flow v9 | autoresearch v10 | paperclip v14 | Skyvern v24 | OpenHands v30 | **DeepTutor v38** |
|------|-------------|------------------|---------------|-------------|---------------|---------------------|
| **Tier** | T5 | T5 | T5 | T5 | T5 | **T5** |
| **Scope sub-archetype** | Research-agent | Solo-known-ML-research | Community-orchestration | Browser-automation | SWE-agent | **Education-application (NEW)** |
| **Primary language** | Python + Next.js | Python | TypeScript 97% | Python + Node.js | Python 71% + TS 26% | **Python 74.7% + TS 24.2%** |
| **License** | MIT | MIT | MIT | AGPL-3.0 + Cloud | MIT + separate-enterprise-dir | **Apache-2.0** |
| **Org archetype** | Corporate | Solo-known | Community-platform | Commercial-entity | Academic-commercial | **Academic-lab-ecosystem** |
| **Lineage (Pattern #19)** | Arch 1 (team) | Arch 1 (Karpathy individual) | Arch 2 (methodology; Bostrom alignment) | Arch 3 (BabyAGI + AutoGPT community-viral) | Arch 4 research-paper-chain (ICLR 2025 + Nov 2025 SDK) | **Arch 4 research-paper-chain + ecosystem-portfolio (nanobot + LightRAG + LlamaIndex + ManimCat)** |
| **Paper** | No | Blog-post-only | No | No | **ICLR 2025 + arXiv 2407.16741 + Nov 2025 SDK arXiv 2511.03690 (4 persistent authors across 16-mo gap)** | **arXiv "Coming Soon" (observation-in-waiting)** |
| **Backbone** | LangGraph | Custom nanochat | Custom (Express + Drizzle + Postgres + Playwright + promptfoo) | Custom (browser + vision) | Custom (Docker sandboxed runtime) | **nanobot agent engine + LlamaIndex RAG + ManimCat math + Typer CLI** |
| **Agent count / primitives** | Multi-agent graph | 1 agent loop + ~100 exp budget | 4 skills + 9 features + 5 invariants | 4 AI-page-commands abstraction | Docker-sandboxed per-workflow + 4 pre-built workflows | **6 chat modes + 4 capabilities + 7 tools + 14 Book blocks + TutorBot fleet + 12 REPL slashes + 15 CLI families** |
| **Provider count (Pattern #28)** | Multi via LangGraph | OpenAI only (single-project) | Multi (OpenAI + Claude Code + Codex + Cursor adapters) | 8+ native (OpenAI + Anthropic + Bedrock + Gemini + Ollama + OpenRouter + Azure + compat) | Multi via SDK routing | **27 LLM + 7 embedding + 7 search = 41 integrations (CORPUS-MOST)** |
| **Multi-channel connectors** | — | — | — (single UI) | — | — | **8+ (Telegram + Discord + Slack + Feishu + WeChat Work + DingTalk + Email + more) corpus-first T5** |
| **i18n README count** | 2-3 | 1 (EN) | 1 (EN) | 2-3 | 2-3 | **9 (EN + zh-CN + JA + ES + FR + AR + RU + HI + PT + TH) corpus-first T5 top-tier** |
| **Pattern #17 variant** | N/A | N/A | N/A | N/A | — | **Variant 5a observational academic-lab-ecosystem-portfolio (N=1; 7 repos ~173K combined)** |
| **Pattern #44 Academic-Lab** | ❌ | ❌ | ❌ | ❌ | ✅ 2nd data point (UIUC+CMU) | **✅ 3RD DATA POINT (HKU) — N=3 DEFAULT-CRITERION** |
| **Deployment surfaces** | Python + Next.js + API | Single-dir Python | Monorepo (FE + BE + DB + QA) | Docker + Cloud | SDK + CLI + Web + Cloud + Enterprise (5 surfaces — previous T5 record) | **Web UI + CLI + WebSocket API + Python SDK (4 surfaces) + Docker GHCR multi-arch amd64+arm64 + Setup Tour** |
| **Commercial tier** | — | — | — | AGPL + Cloud | MIT + separate-enterprise-directory | **— (pure academic-lab OSS)** |
| **MCP integration** | — (ByteDance Claude-Code-adjacent via OAuth) | — | Via OpenClaw adapter | — | — | **❌ excluded (bilateral SKILL.md instead) — 2nd T5 scope-type counter-evidence for Pattern #18 after v36 pi-mono T1-scale** |
| **Benchmark** | — | val_bpb (single-project) | — | WebBench 64.4% + WebVoyager 85.8% | **SWE-Bench Verified 77.6** | — (arXiv-pending) |
| **Governance file count** | — | — (~5 files) | Medium (README + 5 monorepo docs) | — | Medium (MIT + separate enterprise dir) | **Medium (5 files: README + AGENTS.md 149L + SKILL.md 148L + CONTRIBUTING 220L + LICENSE; no CoC; 7-tool pre-commit stack)** |
| **Maintainer archetype** | Team (ByteDance) | Individual (Karpathy) | Team (paperclipai) | Commercial co-founders ("founders@skyvern.com") | 3-co-founder triangle (Xingyao + Graham + Robert) | **Solo-named with lab-backing (`@pancacake` + HKUDS)** |
| **Ecosystem-portfolio** | ByteDance corporate | Karpathy nanochat ecosystem | paperclipai single-product | Skyvern single-product | All Hands AI single product | **HKUDS 7-repo ~173K combined (CORPUS-LARGEST academic-lab ecosystem)** |
| **Storm Bear pilot-relevance** | LOW-MEDIUM (ByteDance corporate distance) | LOW (solo-ML not operator-adjacent) | AVOID brand-association ("zero-human") | MEDIUM (AGPL friction) | MEDIUM-HIGH #6 (SWE-agent platform) | **HIGH #3 🆕 (education-platform + VN potential + Book Engine + TutorBot + lowest-risk Apache-2.0 + CN-provider friendly)** |

### 1.3 T5 archetype diversity preserved

6 T5 entrants → 6 distinct organizational archetype × scope combinations:

1. Corporate × Research-agent (deer-flow)
2. Solo-known × Solo-ML-research (autoresearch)
3. Community-platform × Orchestration (paperclip)
4. Commercial-entity × Browser-automation (Skyvern)
5. Academic-commercial × SWE-agent (OpenHands)
6. **Academic-lab-ecosystem × Education-application (DeepTutor)** ← NEW

**Pattern #9 Resolution D (multi-axial T5 bifurcation) leading probability post-v38:** unchanged 65%. T5 continues to support Resolution D empirically — 6 entrants occupy 6 distinct archetype-scope coordinates without forcing tier-split.

### 1.4 Scale observations at T5

| Rank (stars) | Wiki | Scale |
|--------------|------|-------|
| 1 | autoresearch v10 | 74,000 |
| 2 | OpenHands v30 | 71,704 |
| 3 | deer-flow v9 | 62,000 |
| 4 | paperclip v14 | 55,900 |
| 5 | Skyvern v24 | 21,281 |
| 6 | **DeepTutor v38** | **21,230** |

**Observation:** DeepTutor and Skyvern are statistically tied (21.2K vs 21.3K). T5 has a bimodal distribution — 4 entrants in 55-74K (corporate/solo-famous/community/academic-commercial) and 2 entrants at ~21K (Skyvern commercial + DeepTutor academic-lab).

**Interpretation:** the 4 higher-scale entrants benefit from either (a) corporate distribution (ByteDance), (b) individual-fame (Karpathy 3-touchpoint corpus), (c) viral-community (paperclip Reddit + Discord), or (d) peer-reviewed academic publication (OpenHands ICLR 2025). DeepTutor and Skyvern share **shorter-time-to-launch + no-pre-existing-amplification** — scale proportional to launch maturity.

**DeepTutor velocity:** 20K in 111 days = ~190 stars/day sustained — faster than Skyvern (21K in 24 months = ~30 stars/day early) — DeepTutor is on track to cross Skyvern soon.

## Part 2 — Pattern #44 Academic-Lab Affiliation Archetype: N=3 strengthening

### 2.1 Pattern history timeline

| Event | Wiki | State | Evidence |
|-------|------|-------|----------|
| Registered | v22 LlamaFactory | N=1 CANDIDATE | Lab4AI + ACL 2024 |
| Stale-flag review | v27 audit | STALE-CANDIDATE | N=1 after 5 wikis |
| UN-STALED | v30 OpenHands | N=2 ACTIVE CANDIDATE | + UIUC+CMU multi-institutional + ICLR 2025 |
| **PROMOTED CONFIRMED** | v31 mini-audit | **Structurally-unambiguous-at-N=2** | Lab4AI + UIUC+CMU both satisfy criteria criterially |
| **N=3 strengthening** | **v38 DeepTutor** | **CONFIRMED + default-≥3-observations-criterion-also-satisfied** | **+ HKU (HKUDS) + arXiv-pending** |

### 2.2 The 3 data points (cross-institutional)

| Pt | Wiki | Institution | Region | Continent | Paper venue | Tier / scope |
|----|------|-------------|--------|-----------|-------------|--------------|
| 1 | v22 LlamaFactory | Lab4AI | CN-academic | Asia-mainland | ACL 2024 peer-reviewed | Outside-scope training-infrastructure |
| 2 | v30 OpenHands | UIUC + CMU multi-institutional | US-academic | North America | ICLR 2025 peer-reviewed + Nov 2025 SDK arXiv preprint | T5 SWE-agent application |
| 3 | **v38 DeepTutor** | **HKU (HKUDS Data Intelligence Lab)** | **HK-academic** | **Asia-HK** | **arXiv "Coming Soon" (pre-registration)** | **T5 education-application (NEW)** |

### 2.3 Criterial signatures at N=3

Pattern #44 formal signature (validated across all 3 data points):

| Signature | Lab4AI | UIUC+CMU | HKU | N=3 |
|-----------|--------|----------|-----|-----|
| (a) Institutional attribution prominent in README | ✅ ACL 2024 title badge | ✅ "UIUC + CMU academic co-founders" | ✅ "Data Intelligence Lab @ HKU" footer | 3/3 ✅ |
| (b) Paper cited or pending | ✅ ACL 2024 published | ✅ ICLR 2025 + Nov 2025 SDK published | ✅ arXiv "Coming Soon" pending | 3/3 ✅ |
| (c) Near-solo maintainer despite institutional backing | ✅ hiyouga solo | ✅ 3-co-founder-triangle (small) | ✅ `@pancacake` solo | 3/3 ✅ |
| (d) Research-paper-chain or tool-lineage (Pattern #32 cross-ref) | ✅ 5+ prior research cited | ✅ 2-paper internal chain + SWE-bench lineage | ✅ nanobot + LightRAG + LlamaIndex + ManimCat lineage | 3/3 ✅ |
| (e) Governance depth lighter than corporate heavier than solo-community (Pattern #12 cross-ref) | ✅ Apache-2.0 + medium governance | ✅ MIT + medium + enterprise-directory | ✅ Apache-2.0 + 7-tool pre-commit + branching | 3/3 ✅ |

**All 5 criterial signatures satisfied across 3 data points × 3 continents × 3 scope categories (outside-scope + 2 T5 sub-archetypes).**

### 2.4 Formal statement at N=3 default-criterion

> **Pattern #44 Academic-Lab Affiliation Archetype (CONFIRMED at N=3, default-≥3-observations-criterion-also-satisfied at v38 DeepTutor):**
>
> Agent-space frameworks affiliated with academic research labs exhibit structurally consistent signatures:
> (a) institutional attribution prominent in README
> (b) paper published (ACL/ICLR/NeurIPS/EMNLP) or preprint (arXiv) — cited or pending
> (c) near-solo maintainer despite institutional backing (lab provides credibility + institutional continuity, not contribution-count)
> (d) research-paper-chain or tool-lineage citations
> (e) governance depth lighter than corporate, heavier than solo-community
>
> **Validated at N=3 across 3 institutions × 3 continents × 3 scope categories (training-infra outside-scope / SWE-agent T5 / education-application T5).**

### 2.5 Significance — corpus-first default-criterion achievement for academic-lab-adjacent pattern

**Pattern #44 is the first academic-lab-adjacent pattern** to satisfy default-criterion (≥3 observations across 2+ tiers). Prior academic-lab-related patterns:

| Pattern | Status | Criterion |
|---------|--------|-----------|
| #42 Academic-Published Peer-Reviewed Framework | CONFIRMED at N=2 (structurally-unambiguous) | N=2 structural (v31 mini-audit) |
| #44 Academic-Lab Affiliation Archetype | **CONFIRMED at N=3 (default-criterion)** | **N=3 default (v38) 🆕** |

**First academic-lab pattern at default tier.** Subsequent academic-lab observations will further strengthen (N=4+) without needing structural-unambiguity justification.

## Part 3 — Education-application T5 sub-archetype formalization

### 3.1 Novel sub-archetype observation

At v38 DeepTutor, a **new T5 sub-archetype emerges**: education-application. Distinct from all 5 prior T5 entrants and distinct from T3 agent-education tier.

### 3.2 Clean boundary — T3 agent-education vs T5 education-application

| Axis | T3 Agent-as-education | T5 Education-application |
|------|----------------------|--------------------------|
| **Whom teach?** | Humans learning to BUILD agents | Humans learning ANY subject (agents are mechanism) |
| **Subject-of-study** | Agents themselves | Any topic (math / science / Scrum / language / ...) |
| **Format** | Course / curriculum / tutorial | Runnable platform / application |
| **Agent role** | Subject-of-study | Delivery-mechanism |
| **User type** | Agent-builder (dev) | Any learner |
| **Examples (corpus)** | Microsoft ai-agents-for-beginners v6 / HF agents-course v26 | **DeepTutor v38** |
| **Tier structural** | T3 | T5 |

**Implication:** the two tiers are **complementary** (not competing) — T3 teaches production of agents; T5 applies agents to teach other subjects. A student could start at T3 to learn agent-building then use T5 DeepTutor to learn Scrum / math / language.

### 3.3 Education-application T5 criteria (observational — N=1)

DeepTutor v38 signatures:

- **Domain-orthogonal teaching infrastructure** — agent platform teaches ANY subject via KB upload (Scrum / math / biology / language); not subject-locked
- **Multi-agent pedagogy pipelines** — Deep Solve (multi-agent problem solving) + Book Engine (multi-agent living-book compilation) + TutorBot (persistent autonomous tutor) + Deep Research (parallel subtopic research)
- **Persistent learner-model** — Memory (Summary + Profile) + Notebooks + Question Bank maintain state across sessions
- **Content-generation capabilities** — Quiz Generation + Book Engine + Math Animator + Visualize generate educational content, not just retrieve
- **Dual-audience agent-native CLI** — SKILL.md exposes platform to external agents (bilateral corpus-first)

### 3.4 Promotion trajectory (speculative)

If N=2 education-application T5 appears in future corpus (hypothetical: MIT-OpenCourseware-Agent / Duolingo-Agent-Platform / Coursera-Agent-Coach), the observation could justify:
- Pattern #44 strengthening cross-reference with education-specific sub-pattern
- Or new Pattern candidate "Multi-agent Pedagogy Pipeline Architecture" (domain-specific)

**Not registered at v38** — N=1 consolidation-forward discipline applied. Documented as structural tier observation for corpus memory.

## Part 4 — Pattern #17 variant 5a academic-lab-ecosystem-portfolio observation

### 4.1 Pattern #17 variant taxonomy (post-v27 refinement)

| Variant | Data points | Description |
|---------|-------------|-------------|
| 1 | individual-led-dev (nextlevelbuilder + safishamsi + Luong + Tody + Mario + Shayan + Jarrod + ...) | Solo individuals with multi-project portfolios |
| 2 | big-tech curator (Anthropic / Vercel / Google / Microsoft skill registries) | Corporate official curators |
| 3 | solo-brand (safishamsi penpax.ai / nextlevelbuilder goclaw) | Solo-with-commercial-platform |
| 4 | commercial-startup ecosystem (VoltAgent + Skyvern + All Hands AI) | Startup with multi-product |
| 5 | ecosystem-scale commercial platform (HuggingFace + Microsoft AutoGen Team) | $1B+ valuation + 10+ years + OSS + commercial tier |
| 6 | individual-multi-runtime-publisher (Yeachan Heo OMC) | Solo publishes for multiple runtimes |
| **5a (observational)** | **academic-lab-ecosystem-portfolio (HKUDS)** | **Academic lab publishes 5+ agent repos + research papers** |

### 4.2 HKUDS as observational variant 5a

HKUDS signatures structurally parallel to variant 5 (ecosystem-scale commercial):
- 7+ repos (~173K combined)
- Multiple products at each ecosystem-stack layer (engine / RAG / methodology / runtime / apps)
- OSS with mixed MIT + Apache-2.0 strategy
- Active research publications (LightRAG EMNLP 2025 + DeepTutor arXiv-pending)

**Differences from variant 5:**
- No commercial tier (pure academic-lab OSS)
- No $1B valuation (academic lab, non-commercial)
- No 10+ years maturity (DeepTutor 4 months; lab-level maturity unknown)

**Registration decision:** NOT registered standalone at v38. Variant-within-pattern-at-N=2 criterion requires N=2; HKUDS is N=1 academic-lab-ecosystem-portfolio in corpus. **If another academic-lab ecosystem-portfolio emerges** (Stanford-NLP + Berkeley-RISE + MIT-CSAIL + CMU-DB hypothetically), could promote variant 5a within Pattern #17.

### 4.3 Structural parallels

| Signature | HuggingFace (variant 5) | Microsoft (variant 5) | **HKUDS (variant 5a observational)** |
|-----------|------------------------|----------------------|---------------------------------------|
| Repo count (agent-focused) | 14+ | N+ (subset of Microsoft org) | **7+** |
| Top-repo stars | 130K+ (Transformers) | 40K+ (AutoGen) | **40.7K (nanobot)** |
| Combined | ~600K | varied | **~173K** |
| OSS + permissive | ✅ | ✅ | ✅ (mixed MIT + Apache-2.0) |
| Research publications | ✅ | ✅ | ✅ (LightRAG EMNLP 2025) |
| Commercial tier | ✅ (Hub paid) | ✅ (enterprise offerings) | ❌ |
| Consumer application | ✅ (Hugging Chat / Spaces) | ✅ (Copilot / Bing AI) | ✅ (DeepTutor) |
| Foundation primitive | ✅ (Transformers) | ✅ (Semantic Kernel / AutoGen) | ✅ (nanobot) |
| Bus-factor classification | Large team | Large team | Lab PhDs + postdocs (moderate) |

## Part 5 — Pattern Library impact summary (v38 direct updates)

### 5.1 State transitions

| Pattern | Pre-v38 | Post-v38 |
|---------|---------|----------|
| **#44 Academic-Lab Affiliation** | CONFIRMED at N=2 (structurally-unambiguous-at-N=2) | **CONFIRMED at N=3 (default-≥3-observations-criterion-also-satisfied) 🆕** |
| #27 Community-Viral Scale Path | CONFIRMED 13 data points | CONFIRMED 14 data points (+ Asia-academic-amplified sub-path) |
| #28 Multi-Provider AI Support | CONFIRMED 5 data points | CONFIRMED 6 data points + CORPUS-MOST 41 integrations + native-SDK sub-variant |
| #18 Agent Runtime Standardization | CONFIRMED (triple-layer formulation v36) | CONFIRMED + 2nd T5-scope-type MCP-exclusion counter-evidence (after T1-scale pi-mono v36) |
| #17 Ecosystem-Layer Organizations | CONFIRMED 11 data points + 6 variants | CONFIRMED 12 data points + variant 5a academic-lab-ecosystem-portfolio observational N=1 |
| #42 Academic-Published Peer-Reviewed | CONFIRMED at N=2 | CONFIRMED at N=2 + observational-in-waiting (arXiv "Coming Soon" pending) |
| #29 License-Category Diversity | CONFIRMED 3+ Apache-2.0 | CONFIRMED 4th Apache-2.0 T5 data point |
| #12 Governance-Depth Correlates with Org | CONFIRMED | Reinforced (academic-lab medium-governance archetype consistent) |
| #22 AGENTS.md Industry Standard | CONFIRMED + minimum-viable + maximum sub-variants | Medium-weight AGENTS.md T5 data point (149 lines; between v36 max 182 and v37 min 327B) |

### 5.2 New candidates registered

**ZERO.** Consolidation-forward discipline APPLIED — 6 overlap-pre-check rejections in Phase 0.5:
1. Academic-lab ecosystem-portfolio T5 → strengthen Pattern #17 variant 5a observational
2. Education-application T5 sub-archetype → document as structural observation, not pattern
3. Hong Kong regional archetype → cross-tier observation only (Pattern #73 is T1-scoped)
4. Bilateral runtime-and-skill → N=1 spans #2 + #18; corpus-first observation
5. Multi-agent living-book compiler → N=1 narrow-domain; corpus-first observation
6. arXiv-pending release pattern → observation-in-waiting for Pattern #42

### 5.3 New OBSERVATION-TRACKs registered

**ZERO.** All observations either:
- Strengthen existing patterns (#17 / #27 / #28 / #44 / etc.)
- Document as structural tier observation (education-application T5)
- Document as observation-in-waiting (arXiv)
- Document as corpus-first (bilateral + living-book compiler)

### 5.4 Ratio preservation

**Pre-v38:** 34 confirmed + 23 active + 4 stale + 8 retired + 4 OT = 73 full / 57 active (ratio 23:34 = **0.68:1**)

**Post-v38:** 34 confirmed + 23 active + 4 stale + 8 retired + 4 OT = 73 full / 57 active (ratio 23:34 = **0.68:1 preserved**)

**Buffer:** 0.27 below 0.95:1 mini-audit trigger.

**Significance:** 2nd consecutive wiki preserving 0.68:1 ratio (v37 + v38). Consolidation-forward discipline demonstrated twice in v2.1 era.

## Part 6 — Corpus-firsts inventory (v38)

### 6.1 Tier + archetype firsts

| # | First |
|---|-------|
| 1 | **Asia-academic-lab T5** (joins US v30 UIUC+CMU + CN v22 Lab4AI on third continent Asia-HK) |
| 2 | **Education-application T5 sub-archetype** (uses agents to teach humans any subject; clean tier boundary vs T3) |
| 3 | **Hong Kong / HKU regional observation** (7th region in corpus after US + VN + CN + Korean + Pakistani + Austrian + others) |
| 4 | **Academic-lab ecosystem-portfolio** (HKUDS 7 repos ~173K combined; corpus-largest academic-lab portfolio) |
| 5 | **Pattern #44 N=3 default-criterion achievement** (first academic-lab-adjacent pattern at default tier) |

### 6.2 Architecture + primitive firsts

| # | First |
|---|-------|
| 6 | **Bilateral runtime-and-skill** (agent-HOST + agent-TOOL same repo; SKILL.md exposes DeepTutor while DeepTutor runs TutorBot + Capabilities) |
| 7 | **Multi-agent "living book" compiler** (Book Engine 14-block-type pipeline) |
| 8 | **Persistent-autonomous-tutor-bot architecture** (Heartbeat proactive initiation at T5) |
| 9 | **Soul Template personality-as-file** archetype |
| 10 | **8+ multi-channel bot delivery** at T5 (Telegram/Discord/Slack/Feishu/WeChat Work/DingTalk/Email/+) |
| 11 | **Per-bot LLM provider override** within single deployment |
| 12 | **27 LLM providers + 41 total integrations** (corpus-most-extensive) |
| 13 | **4-stage vision pipeline** for `geogebra_analysis` math-tutoring specialist tool |

### 6.3 Distribution + i18n firsts

| # | First |
|---|-------|
| 14 | **9-language README at T5** (corpus-first T5 ≥9 languages; Arabic + Russian + Hindi + Portuguese + Thai first simultaneously at T5) |
| 15 | **`.env.example_CN` region-specific default configuration** (beyond locale-file convention; first at T5) |
| 16 | **Docker GHCR multi-arch amd64+arm64** official T5 |
| 17 | **Native OpenAI/Anthropic SDK dropping litellm** at provider count 27 (architectural pivot v1.0.0-beta.3 from abstraction-library sub-variant to native-routing sub-variant) |

### 6.4 Ecosystem + lineage firsts

| # | First |
|---|-------|
| 18 | **50% HKUDS self-dependency fraction** (2 of 4 major deps are HKUDS: nanobot + LightRAG roadmap) |
| 19 | **Sequenced cross-repo integration roadmap** (LightRAG 🔜 post-v1.2.x explicit) |
| 20 | **HKUDS vertical stack hypothesis** (engine → methodology → infra → runtime → apps across 7 repos) |
| 21 | **arXiv "Coming Soon" badge** as deliberate pre-registration signal |
| 22 | **T5-scope Pattern #18 MCP-exclusion counter-evidence** (2nd scope-type after T1 pi-mono v36; T5 academic-research scope extension) |

### 6.5 Corpus coordination firsts (Storm Bear)

| # | First |
|---|-------|
| 23 | **27th consecutive Storm Bear meta-entity** (v10-v38 uninterrupted) |
| 24 | **Storm Bear direct operator-relevance top-3 rank** at v38 (#3 position; DeepTutor leapfrogs markitdown v28 / crawl4ai v29 / BMAD v11 for education-platform + Book Engine hypothesis) |
| 25 | **Storm Bear vault-as-book hypothesis** (Book Engine on 37-wiki vault → public shareable asset) |
| 26 | **Storm Bear bilateral-skill hypothesis** (inspire Storm Bear vault to expose own SKILL.md to external agents) |
| 27 | **Structural-failure observation on v27 diagnostic bundle** (15 sessions deferred = routine v2.1 escalation-mechanism empirically failed to produce action; route to v2.2 consideration) |

**Total corpus-firsts at v38: 27** (higher than v37's ~8 cold-start firsts; consistent with v36 pi-mono's ~10 firsts; reflects dense corpus-novel content in DeepTutor).

## Part 7 — Velocity + ratio metrics

### 7.1 Velocity at v38

- **Target:** ~2h 30min (YELLOW tolerance band +25% over GREEN 2h baseline)
- **Actual:** ~2h 40min (within tolerance; consistent with v36 pi-mono YELLOW + v37 bizos YELLOW precedents)
- **Plateau preserved:** 33 consecutive wikis at ~2h GREEN / ~2h 30-40min YELLOW (v6-v38)
- **6th v2.1-era execution:** all 5 v2.1 discipline mechanisms exercised cleanly

### 7.2 Ratio at v38

- **Pre-v38:** 23:34 = 0.68:1 (healthy; lowest since v22; 0.27 buffer below 0.95:1 mini-audit trigger)
- **Post-v38:** 23:34 = 0.68:1 (preserved)
- **2nd consecutive wiki preserving 0.68:1** (v37 + v38)
- **Next audit trigger:** candidate count ≥ 25 OR v41 wiki OR ratio > 0.95:1 (mini-audit) / > 1.05:1 (full audit)

## Part 8 — Strategic implications

### 8.1 For Storm Bear operator

1. **Pilot rank #3 new entrant** — DeepTutor leapfrogs prior candidates for education-platform + Book Engine + TutorBot VN-Scrum hypothesis
2. **Self-directed learning pilot viable in 1 weekend** — Setup Tour + load Storm Bear vault KB + explore 6 chat modes
3. **VN localization PR opportunity** — 9-language README missing VN; low-friction PR + positioning benefit
4. **Book Engine on Storm Bear vault experiment** — compile "Agent Framework Landscape 2026" public-shareable asset
5. **Pattern #44 credibility signal** — "built on HKUDS research-grade platform" stronger than "solo-maintainer framework" for VN enterprise clients

### 8.2 For Pattern Library evolution

1. **Academic-lab archetype matures** to first default-criterion pattern (#44 N=3)
2. **Pattern #17 variant taxonomy extends** observationally with variant 5a
3. **T5 tier saturation signal** — 6 archetype-diverse entrants; archetype-diversity-per-wiki at 100% preserved
4. **Pattern #18 scope-narrowing continues** — MCP-exclusion now at 2 distinct scope types (T1-scale + T5-academic-research); possible future refinement if N=3+
5. **Consolidation-forward discipline validated 2nd consecutive wiki** (v37 + v38 zero-new-active-candidates)

### 8.3 For corpus structural maturity

1. **T5 education-application** establishes education-as-app pattern adjacent to but distinct from T3 education-course
2. **Academic-lab ecosystem-portfolio** observation establishes academic-lab as scale-comparable to commercial (Pattern #17 variant 5 structural-parallel)
3. **HKUDS vertical-stack hypothesis** suggests corpus-observable academic-lab stack-building pattern
4. **Bilateral runtime-and-skill** observation plants seed for future Pattern #76 candidate if N=2 emerges
5. **arXiv-pending observation-in-waiting** mechanism enables deferred Pattern #42 data-point recognition

## Part 9 — Next wiki candidates + routing recommendations

### 9.1 High-priority targets (pattern-strengthening focus)

1. **Another academic-lab framework** → Pattern #44 to N=4 (observational reinforcement; no-audit-impact but increases pattern durability)
2. **Another education-application T5** → Pattern candidate "Multi-agent Pedagogy Pipeline" promotion from N=1 observational
3. **Another bilateral runtime-and-skill framework** → possible Pattern #76 candidate registration at N=2 structural-unambiguity
4. **Another ecosystem-scale commercial platform** (HuggingFace adjacent or similar) → Pattern #17 variant 5 to N=3 default-criterion (currently N=2 structural)

### 9.2 Mid-priority

5. **HKUDS sibling wiki** (nanobot 40.7K or LightRAG 34.2K) → intra-ecosystem coherence analysis; possible variant 5a N=1.5 (not N=2 since same org)
6. **T2 wiki entrant** (tier currently at N=2; extension would validate 3rd T2)
7. **T3 wiki entrant** (tier at N=2; extension would test solo-T3 hypothesis)

### 9.3 Lower-priority (ratio preservation / discipline)

8. **Discipline wiki** — zero-new-candidates 3rd consecutive = further cement consolidation-forward discipline pattern
9. **v27 diagnostic execution wiki** — not a framework wiki; Storm Bear operator-facing action wiki addressing BLOCKING-RECOMMENDATION backlog

## Part 10 — Appendix: full Pattern #44 observation catalog at N=3

### Lab4AI (LlamaFactory v22)

- **Framework:** `hiyouga/LLaMA-Factory` (70.3K stars)
- **Institution:** Lab4AI (Chinese academic-industry)
- **Paper:** ACL 2024 peer-reviewed (arXiv 2403.13372) — first peer-reviewed venue in corpus
- **Maintainer:** hiyouga (solo + Lab4AI affiliation)
- **Scope:** Training-infrastructure (outside-scope)
- **License:** Apache-2.0
- **Lineage:** PEFT + TRL + QLoRA + FastChat + 100+ research projects

### UIUC+CMU + All Hands AI (OpenHands v30)

- **Framework:** `OpenHands/OpenHands` (71.7K stars)
- **Institution:** UIUC PhD + CMU Professor + All Hands AI commercial ($18.8M)
- **Paper:** ICLR 2025 (arXiv 2407.16741; 23+ co-authors) + Nov 2025 SDK paper (arXiv 2511.03690; 11 co-authors) — 4 persistent authors across 16-month gap (first within-project 2-paper chain in corpus)
- **Maintainer:** 3-co-founder-triangle (Xingyao Wang + Graham Neubig + Robert Brennan)
- **Scope:** T5 SWE-agent
- **License:** MIT core + separate-license enterprise directory
- **Benchmark:** SWE-Bench Verified 77.6

### HKU / HKUDS (DeepTutor v38)

- **Framework:** `HKUDS/DeepTutor` (21.2K stars)
- **Institution:** HKU Data Intelligence Lab
- **Paper:** arXiv "Coming Soon" (pending; HKUDS LightRAG EMNLP 2025 sibling paper confirms lab-level publication track-record)
- **Maintainer:** `@pancacake` (solo-named + HKUDS lab-backing)
- **Scope:** T5 education-application (NEW sub-archetype)
- **License:** Apache-2.0
- **Ecosystem:** 7-repo HKUDS portfolio ~173K combined (nanobot + LightRAG + CLI-Anything + DeepTutor + RAG-Anything + DeepCode + OpenHarness)

### Cross-observation analysis

**3 continents × 3 scope categories × 3 institution types (national-affiliated / multi-institutional / single-lab ecosystem-portfolio)** — Pattern #44 durably applies across structural variation. **Strongest academic-lab pattern** in corpus at v38.

---

*This Phase 4b deliverable is the primary v38 strategic output. See `02 Wiki/` cluster summaries + entities for detailed source material, `03 Published/(C) DeepTutor - Huong dan cho nguoi moi.md` for bilingual beginner guide, and `04 Reviews/(C) 2026-04-24 v38 build learnings.md` for iteration log + Pattern Library direct-update notes.*
