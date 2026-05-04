# CLAUDE.md — dive-into-llms Beginner Analysis

> **Target:** `Lordog/dive-into-llms` — 《动手学大模型Dive into LLMs》系列编程实践教程 — Jupyter Notebook 100% + PDF slides + markdown, **NO LICENSE file** (default copyright; 2nd corpus after v37 bizos), by **SJTU BCMI Lab (Shanghai Jiao Tong University)** — lead Zhang Zuosheng (张倬胜) + maintainer Yuan Tongxin (Lordog).
> **Scale:** 34,000 stars / 4,200 forks / 220 watchers / 5 open issues / 73 commits / 15+ named contributors; 34K in ~12-18 months = ~60-90 stars/day sustained-community-viral.
> **Homepage:** https://github.com/Lordog/dive-into-llms (+ secondary curriculum at Huawei Ascend community https://www.hiascend.com/edu/growth/lm-development)
> **Routine:** `llm-wiki-routine-v2.1` (this is **v39** in Storm Bear corpus — 7th v2.1-era execution + 28th consecutive Storm Bear meta-entity)
> **Shipped:** 2026-04-24

---

## 12-axis classification (Phase 0 output)

| Axis | Value |
|------|-------|
| **Tier** | **T3 Agent-as-education — 3RD T3 ENTRANT (closes N=3 beyond inaugural-N=2 v26 5/5 milestone)** + NEW **T3 academic-consortium-multi-university-with-corporate-community-partnership sub-archetype** (distinct from Microsoft v6 big-tech-corporate + HF v26 commercial-ecosystem-platform) |
| **Archetype** | **Academic-consortium T3** — SJTU BCMI Lab (lead) + NUS (Fei Hao) + Huawei Ascend community — first multi-institutional-consortium T3 in corpus |
| **Scale tier** | Large (20-60K): 34K stars / ~12-18 months = ~60-90/day sustained-community-viral |
| **Primary lang** | **Jupyter Notebook 100%** (CORPUS-FIRST T3 Jupyter-primary; Microsoft v6 was markdown+notebook, HF v26 was MDX) |
| **Packaging** | **Clone + per-chapter Jupyter notebooks + per-chapter PDF slides + per-chapter README** (no pip/npm package; no hosted-platform; pure GitHub-materials distribution with PDF-slide primacy) |
| **Origin story** | **Academic-course-lecture-notes expansion** — originated as SJTU NIS8021 "Natural Language Processing Frontier Technology" + NIS3353 "AI Security Technology" course handouts by Zhang Zuosheng → expanded to open public tutorial |
| **Methodology** | **Hands-on-coding-practice + Chinese-academic-pedagogy + dual-track architecture** — original 11-chapter `《动手学大模型》` + secondary `《大模型开发全流程》` curriculum on Huawei Ascend; public-welfare (公益) framing |
| **Governance** | **LIGHT (2 files: README + .gitignore)** — **2ND ABSENT-LICENSE IN CORPUS after v37 bizos**; no CONTRIBUTING / SECURITY / CODE_OF_CONDUCT / AGENTS.md / CLAUDE.md |
| **Agent/skill count** | 11 chapters × (README + PDF + Jupyter notebook) = **~33 primary content primitives** + second curriculum on external platform; **coarse-grained curriculum primitives (GREEN baseline — not fine-grained component primitives like v36 pi-mono ~150 or v37 bizos ~150)** |
| **i18n** | **CN-primary** (Simplified Chinese — 1st CN-primary T3 in corpus); no EN translation; contrast Microsoft v6 EN-primary + HF v26 EN-primary |
| **Intellectual influence** | **Academic-course-lineage** (SJTU NIS8021 + NIS3353 course handouts) + **cross-corpus citation — LLaMa-Factory** (v22 corpus wiki explicitly cited in chapter 9 GUI Agent tutorial!) + Huawei Ascend partnership; **no Karpathy / John Lam / Boris Cherny / research-paper-chain-as-origin** — academic-course lineage is distinct archetype |
| **Agent platforms** | **Platform-agnostic code samples** — Transformers / vLLM / LLaMA-Factory / TRL / DeepSeek-R1 / Qwen2.5 / Qwen2-VL / PPO (standard HF ecosystem + CN-ecosystem DashScope Qwen + Zhipu GLM); target runtime = Jupyter + CUDA GPUs (A100/A800) |

## Phase 0.5 Pattern pre-check

**Overlap pre-check outcomes (5 candidate attempts considered, 0 registered):**

1. **"Academic-consortium-multi-institutional T3 sub-archetype"** — considered; **strong overlap with Pattern #44 Academic-Lab Affiliation (CONFIRMED N=3 at v38)**. SJTU BCMI Lab + NUS + Huawei is **multi-institutional variant** of academic-lab archetype. **Not registered standalone** — documented as Pattern #44 N=4 strengthening with observational sub-variant note "multi-institutional-consortium" (vs single-institution Lab4AI + UIUC+CMU + HKU). If another multi-institutional-consortium appears at N=2, could formalize as within-pattern variant. Follow v38 DeepTutor variant-5a observational precedent.
2. **"CN-regional T3 archetype"** — considered; **Pattern #73 Regional-Archetype-Registry is T1-scoped** (73a Korean + 73b VN + 73c Pakistani + 73d Austrian at v36 observational). dive-into-llms is T3. **Cross-tier observation only — do NOT extend 73 to T3**. Follow v37 bizos + v38 DeepTutor cross-tier discipline. Documented as observational.
3. **"PDF-primary T3 distribution"** — considered; per-chapter PDF slides (2-11 MB each) alongside README + Jupyter. Novel at T3 (Microsoft v6 = README-primary, HF v26 = MDX-primary). **N=1; rejected standalone**; documented as T3-sub-archetype observation in Phase 4b. Follow v38 bilateral-runtime-and-skill precedent (corpus-first note without registration).
4. **"Corporate-community partnership in academic-consortium"** — Huawei Ascend community as curriculum co-developer (secondary 《大模型开发全流程》). Novel corpus observation. **Overlaps with Pattern #17 Ecosystem-Layer Organizations + Pattern #31 Open-Core**. Not a clean fit for either — Huawei is neither ecosystem-layer-publisher nor open-core-commercial-entity. **N=1 rejected standalone**; documented as corpus-first observation. If N=2 emerges (e.g., another academic-consortium with corporate-hardware-community partnership), consider registration.
5. **"Absent-LICENSE sub-category N=2"** — Pattern #29 License-Category Diversity (CONFIRMED v21) currently covers OSS + non-OSI + custom-research licenses. Absent-LICENSE introduced v37 bizos observationally. **dive-into-llms is N=2 absent-LICENSE** (bizos + dive-into-llms). **Not a new candidate — strengthens #29 within-pattern sub-category**. Could formalize at next audit as #29 refinement (4th sub-category: absent-LICENSE = implicit-default-copyright). Documented as strengthening.

**Un-stale check (all NEGATIVE):**
- #45 Dual-Licensing — NEGATIVE (no license)
- #46 Duo-Founder + Team — NEGATIVE (academic-lab multi-institutional team ≠ duo-founder)
- #52 Extreme-Viral-Velocity — NEGATIVE (~60-90/day sustained, not extreme; ~1K/day threshold)
- Retired revivals (#14 / #16 / #23 / #25 / #49 / #55 / #60 / #70) — all NEGATIVE

**Counter-evidence observations (documented, not refining):**

- **Pattern #22 AGENTS.md industry standard** (confirmed) — dive-into-llms has **NO AGENTS.md** (also no CLAUDE.md). T3 tier AGENTS.md-abstention is now observational N=3 (Microsoft v6 absent + HF v26 absent + dive-into-llms v39 absent). **T3 ≠ codebase tier** — AGENTS.md is for agent-driven codebases; educational curricula systematically abstain. **Could formalize as Pattern #22 narrow-scope-exclusion observation**: "AGENTS.md adoption is codebase-tier-specific; T3 education curricula systematically abstain." No action yet; continued observation.
- **Pattern #18 Agent Runtime Standardization** (confirmed) — dive-into-llms teaches model-level primitives (Transformers / LLaMA-Factory / TRL / PPO / SFT), NOT agent-runtime-level (no OpenClaw / Hermes / MCP). T3 tier is pedagogically upstream of agent-runtime concerns. **Strengthens tier-scope narrowing — T3 focuses on ML/DL primitives, not agent-runtime integration**. No refinement; documented.
- **Pattern #28 Multi-Provider AI Support** (confirmed) — Chapter 2 prompting tutorial demonstrates 4+ CN providers (Qwen DashScope + Zhipu AI + Baidu Wenxin + Baichuan) + OpenAI. **Pedagogical multi-provider-awareness** is observational — distinct from library-level (markitdown `llm_client` DI) and framework-level (TrendRadar LiteLLM). **T3 pedagogy-level multi-provider** is 7th data point type. Documented.
- **Pattern #12 Governance-Depth** (confirmed) — dive-into-llms academic-multi-institutional-consortium with 2-file governance (README + .gitignore only). **Lightest governance at this scale in corpus** (34K stars with 0 governance files beyond README). **Counter-evidence to Pattern #12 organization-correlation**: academic-lab affiliation here produces LESS governance depth than solo-maintainer (e.g., claude-hud v35 3mo solo-with-7-governance-files). **Academic-consortium governance is orthogonal to corporate-solo-LLC axis** — observational finding. Could refine #12 at next audit to include "academic-consortium = light-governance despite institutional backing."

**Consolidation-forward discipline:** APPLIED. **Zero new active candidates. Zero new OBSERVATION-TRACKs.** 5 overlap-pre-check rejections; all observations routed to strengthening existing patterns or corpus-first notes.

**Pattern #44 Academic-Lab Affiliation strengthening to N=4 multi-institutional-consortium sub-variant:**

Currently confirmed at N=3 default-criterion at v38 (Lab4AI + UIUC+CMU + HKU = 3 single-institution-lab data points). SJTU BCMI Lab is **4th institution** but introduces **new sub-variant**: multi-institutional-consortium (SJTU + NUS + Huawei) vs single-institution-lab (prior 3). **Pattern #44 strengthens to N=4 with sub-variant observation**. If another multi-institutional-consortium appears at N=2 in Asia-academic tier, could formalize as within-pattern variant 44a-single-institution vs 44b-multi-institutional-consortium. Documented as within-pattern sub-variant observation.

## Phase 0.9 Primitive-count probe — GREEN

**Primitive surface** (~30-40 distinct):

- **11 chapters** (chapter1-chapter11) — primary content blocks
- **11 per-chapter READMEs** (1-16 KB each)
- **11 per-chapter PDF slides** (2-11 MB each)
- **11 per-chapter Jupyter notebooks** (8-74 KB each; executable code)
- **Per-chapter assets** (screenshots, diagrams, figures)
- **1 requirements.txt** (chapter 11 RLHF only)
- **2 curricula** (primary 11-chapter + secondary Huawei Ascend)
- **4 topic clusters** (Foundations: ch1-2 / Security-alignment: ch3-6, ch10-11 / Advanced-architectures: ch7-8 / Agents: ch9-10)
- **~15+ contributor profiles** across 2 teams

**Outcome: GREEN** (curriculum primitives are coarser-grained than component primitives; 33 content units × 3 deliverables each = ~33 primary primitives cleanly fit 4-entity format). Distinct from v36 pi-mono + v38 DeepTutor YELLOW (fine-grained component primitives).

**Velocity target:** ~2h standard GREEN baseline. No scope-compression pressure.

**4 entity allocation:**
1. **Core product** — 《动手学大模型》 11-chapter original curriculum + PDF/README/Jupyter tripartite per-chapter structure + 4 topic clusters + SJTU NIS8021+NIS3353 academic-course origin
2. **Secondary curriculum + Huawei Ascend partnership** — 《大模型开发全流程》 on Huawei Ascend community + national-hardware-ecosystem positioning + 2025/06 expansion (math reasoning / GUI Agent / alignment / steganography)
3. **SJTU BCMI Lab + Zhang Zuosheng + multi-institutional-consortium + academic-lab Pattern #44 N=4 strengthening** — SJTU lead + NUS (Fei Hao) + Huawei Ascend (ZOMI) + 10+ SJTU faculty-student contributors + CN-academic-community positioning
4. **28th consecutive Storm Bear meta-entity** — T3 tier-completion-beyond-inaugural-N=2 milestone + CN-primary T3 for VN-operator bilingual adjacency (CN pedagogical material accessible to VN readers) + self-directed-ML-learning pilot + no-license implications for Storm Bear

## Phase 4b routing mode

**Primary:** **T3 3-way comparison (Microsoft v6 + HF v26 + SJTU v39) + tier-completion-beyond-inaugural-N=2 milestone + Pattern #44 N=4 multi-institutional-consortium sub-variant strengthening + academic-course-lineage T3 sub-archetype formalization**

**Secondary:** CN-primary T3 + Absent-LICENSE Pattern #29 within-pattern sub-category N=2 (bizos + dive-into-llms)

**Tertiary:** Cross-corpus citation — chapter 9 GUI Agent tutorial explicitly references LLaMa-Factory (v22 Storm Bear corpus wiki); **2nd cross-corpus reference in corpus** after v27 oh-my-claudecode citing v1 ECC + v2 Superpowers (SJTU citing v22 = first externally-occurring cross-corpus reference — not via corpus self-citation but via independent third party)

**Novelty:** First CN-primary T3 + first academic-course-lineage T3 sub-archetype + first multi-institutional-consortium T3 + first PDF-slides-per-chapter T3 + first absent-LICENSE T3 + first Huawei Ascend corporate-community partnership in corpus + first dual-curriculum T3 (public GitHub + external platform) + 2nd absent-LICENSE wiki overall (bizos v37) + first SJTU institution in corpus + first NUS institution in corpus + Pattern #44 N=4 with multi-institutional-consortium sub-variant + first externally-originated cross-corpus citation (ch9 GUI Agent → LLaMa-Factory v22)

## Storm Bear meta-entity warranted?

**YES (28th consecutive).** dive-into-llms is **T3 agent-education (teaches humans how to BUILD + UNDERSTAND LLMs)** — adjacent to HF agents-course v26 (teaches how to build agents) and Microsoft v6 (teaches fundamentals). For Storm Bear operator (VN Scrum coach + software developer learning Claude/autonomous-agents):

**MEDIUM-LOW direct adoption:**
- CN-primary may challenge Storm Bear's VN default; however CN ≈ zh shares 80%+ readability with VN technical vocabulary; SJTU academic rigor is world-class
- **11 chapters cover foundational ML/DL → advanced alignment → agent-scope GUI/safety** — broader spectrum than HF v26 (agent-focused) + Microsoft v6 (agent-focused)
- Jupyter-primary format requires GPU infrastructure (A100/A800 40-80GB) for chapters 1/4/9/11 — friction for operator-only self-study without cloud credits
- **No-license introduces legal ambiguity** — materials can be read/learned-from but CANNOT be legally forked / redistributed / adapted without author permission (default copyright applies); ⚠️ must be noted in beginner guide

**MEDIUM-HIGH observational value:**
- **Pattern #44 academic-lab-as-credibility-signal** — SJTU BCMI + NUS backing demonstrates "academic-consortium tutorial" as legitimate framework archetype for future Storm Bear-backed content
- **Dual-curriculum pattern** (GitHub public + external-platform partnered) = potential future Storm Bear distribution model (vault + Medium / Substack + VN educational platform)
- **Huawei Ascend partnership** = example of hardware-vendor-community corporate partnership for educational credibility
- **Chinese-academic-pedagogy** pedagogical register could influence Storm Bear's VN-pedagogy (both operate in cultural-non-English-native academic-rigor context)
- **Cross-corpus citation** (ch9 citing LLaMa-Factory v22) = external validation of Storm Bear wiki subjects; increments vault credibility

**Pilot ranking at v39:** N/A for framework pilots (T3 is education tier, not framework tier). For self-learning ranking: **#2 after claude-howto v32** (claude-howto = VN-diaspora self-onboarding, self-pacing; dive-into-llms = CN-academic-rigor, deep-technical-foundations). Complementary paths. Recommended for operator seeking foundational LLM pedagogy beyond Claude Code / agent orchestration tooling.

## Cross-references

**Sibling wikis cited by this wiki:**

- **v6 Microsoft ai-agents-for-beginners** — primary T3 reference (inaugural T3 entrant; 10-lesson structure; big-tech corporate archetype). SJTU v39 = 3rd T3 entrant; distinct archetype (academic-consortium vs big-tech-corporate).
- **v26 HF agents-course** — secondary T3 reference (4-unit + multi-framework BYO; commercial-ecosystem-platform archetype); SJTU v39 extends T3 beyond N=2 inaugural.
- **v22 LlamaFactory** — **CROSS-CORPUS CITATION**: chapter 9 GUI Agent tutorial explicitly uses LLaMa-Factory for fine-tuning Qwen2-VL-7B on OS-Kairos dataset. **First externally-originated cross-corpus reference** (LLaMa-Factory as upstream dependency) vs v27 OMC (internal self-citation of v1 + v2).
- **v38 DeepTutor** — primary Pattern #44 reference (N=3 → N=4 strengthening at v39; academic-lab variant sub-type observation); DeepTutor = T5 education-APPLICATION (teaches humans via agents), SJTU = T3 education-CURRICULUM (teaches humans with Jupyter+PDF). Clean tier boundary.
- **v37 bizos** — absent-LICENSE precedent (bizos = 1st absent-LICENSE, dive-into-llms = 2nd); Pattern #29 sub-category strengthening N=2.
- **v31 awesome-mcp-servers** — Anglo-awesome-list (Frank Fiegel) vs SJTU academic-course-aggregator (different archetype at similar function — curating resources); Pattern #68 Awesome-List-Genre would need meta-reclassification for academic-curriculum (not registered).
- **v32 claude-howto** — VN-diaspora self-onboarding T1 vs SJTU CN-academic curriculum T3; complementary learning-tool candidates for Storm Bear operator; both non-Anglo-authored tutorials at scale.
- **v24 Skyvern** — cross-reference via chapter 6 Jailbreak + chapter 10 Agent Safety tutorials (both address agent-space security topics; SJTU covers academically, Skyvern covers operationally).

**Pattern Library state to update (Phase 5):**
- **Pattern #44 strengthens to N=4** with multi-institutional-consortium sub-variant observation (4th institution; first multi-institutional-consortium; 3 continents extended to 4 if counting NUS Singapore)
- **Pattern #29 License-Category Diversity** — absent-LICENSE sub-category strengthens to N=2 (bizos v37 + dive-into-llms v39)
- **Pattern #27 Community-Viral Scale Path** — 15th data point (CN-academic-amplified sub-path ~60-90 stars/day sustained)
- **Pattern #28 Multi-Provider AI Support** — 7th observational data point (T3 pedagogy-level multi-provider awareness sub-variant: Qwen + Zhipu + Baidu + Baichuan + OpenAI)
- **Pattern #22 AGENTS.md** — 3rd T3-abstention observation (v6 + v26 + v39); could formalize tier-scope narrowing at audit
- **Pattern #12 Governance-Depth** — counter-evidence N=1 "academic-consortium light-governance despite institutional backing"
- **Pattern #17 Ecosystem-Layer** — 12th data point (Huawei Ascend corporate-community-as-educational-partner observational variant; not registered)
- **0 new active candidates; 0 new OBSERVATION-TRACKs**

**Ratio preservation target:** 34 confirmed + 23 active + 4 stale + 8 retired + 4 OT = **73 full / 57 active (ratio 23:34 = 0.68:1 preserved 3rd consecutive wiki v37 + v38 + v39).**

---

*This file is the project-level context for the v39 wiki build. See `02 Wiki/(C) index.md` for phase tracking and `04 Reviews/(C) 2026-04-24 v39 build learnings.md` for iteration log.*
