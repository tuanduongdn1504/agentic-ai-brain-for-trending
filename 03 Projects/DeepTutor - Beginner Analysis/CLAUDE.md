# CLAUDE.md — DeepTutor Beginner Analysis

> **Target:** `HKUDS/DeepTutor` — "Agent-Native Personalized Tutoring" — Python 3.11+ + Next.js 16, Apache-2.0, by HKUDS (Data Intelligence Lab, University of Hong Kong).
> **Scale:** 21,230 stars / 2,900 forks / 125 watchers / 20 open issues / 598 commits / 48 contributors; 20K in 111 days = ~190 stars/day community-viral.
> **Homepage:** https://github.com/HKUDS/DeepTutor (no separate homepage URL)
> **Routine:** `llm-wiki-routine-v2.1` (this is **v38** in Storm Bear corpus — 6th v2.1-era execution + 27th consecutive Storm Bear meta-entity)
> **Shipped:** 2026-04-24

---

## 12-axis classification (Phase 0 output)

| Axis | Value |
|------|-------|
| **Tier** | **T5 Agent-as-application — 6TH T5 ENTRANT** + NEW **education-application T5 sub-archetype** (teaches HUMANS via agents, distinct from T3 which teaches humans how to BUILD agents) |
| **Archetype** | **Academic-lab ecosystem-portfolio T5** — HKUDS publishes 7 major agent repos (nanobot 40.7K + LightRAG 34.2K + CLI-Anything 32.4K + DeepTutor 21.2K + RAG-Anything 18.3K + DeepCode 15.3K + OpenHarness 11.1K = ~173K combined) |
| **Scale tier** | Large (20-60K): 21.2K stars in ~4 months (111 days to 20K; ~190/day sustained-viral) |
| **Primary lang** | Python 74.7% + TypeScript 24.2% + JavaScript 0.4% |
| **Packaging** | pip editable (`pip install -e .`) + `[server]` / `[cli]` / `[all]` / `[math-animator]` extras + Docker Compose (GHCR multi-arch amd64+arm64) + 4 entry surfaces (Web UI / CLI Typer / WebSocket API / Python SDK) |
| **Origin story** | Academic-research (HKU Data Intelligence Lab) + agent-native-rewrite (v1.0.0 April 4 = ~200k-line rewrite) + research-paper-chain (arXiv "Coming Soon") |
| **Methodology** | **Agent-native personalized tutoring** — 2-layer plugin model (Tools / Capabilities) + TutorBot persistent-autonomous-agent + Book Engine "living book" multi-agent compiler + Co-Writer multi-document AI workspace |
| **Governance** | **Medium** — 5 files (README 759 lines + AGENTS.md 149 + SKILL.md 148 + CONTRIBUTING.md 220 + LICENSE 202 + Communication.md 233B for Feishu) + pre-commit hooks (Ruff / Prettier / detect-secrets / pip-audit / Bandit / MyPy / Interrogate) + `dev` / `multi-user` branching |
| **Agent/skill count** | **~60-70 user-facing primitives** — 7 tools + 4 built-in capabilities + 6 chat modes + 14 Book Engine block types + 15 CLI top-level command families + 12 REPL slash commands + 5 playground plugins + Soul Templates (TutorBot personas) + user-authored Skills (v1.2.2) + 8+ multi-channel connectors (Telegram / Discord / Slack / Feishu / WeChat Work / DingTalk / Email / …) |
| **i18n** | **9-language README** (EN + zh-CN + JA + ES + FR + AR + RU + HI + PT + TH) — ties HF agents-course v26 / oh-my-claudecode v27 / pi-mono v36 top-tier; **first Arabic + Russian + Hindi + Portuguese + Thai in a single T5 corpus entrant**; `.env.example_CN` for China-ecosystem providers |
| **Intellectual influence** | **HKUDS ecosystem-portfolio lineage** (nanobot powers TutorBot) + LlamaIndex (RAG backbone) + ManimCat (math animation) + arXiv-pending paper; **no Karpathy / John Lam / Boris Cherny citation** |
| **Agent platforms** | **Standalone** (NOT Claude Code plugin; NOT MCP-integrated) + **SKILL.md exposes DeepTutor CLI as an agent-skill for ANY tool-using agent** (nanobot / any LLM-with-tool-access); bilateral integration — DeepTutor IS a runtime AND publishes a skill that makes other agents drive it |

## Phase 0.5 Pattern pre-check

**Overlap pre-check outcomes (6 candidate attempts considered, 0 registered):**

1. **"Academic-lab ecosystem-portfolio T5"** — considered; strong overlap (>70%) with Pattern #17 Ecosystem-Layer Organizations (confirmed v15, refined v27 audit with 5 variants). HKUDS fits variant 5 (ecosystem-scale-research-lab platform) as a 6th archetype variant candidate. **Not registered standalone** — documented as observational variant for within-pattern N=2 future promotion if another academic-lab ecosystem-portfolio appears. Follow v33/v36 precedent.
2. **"Education-application T5 sub-archetype"** — considered; structural observation about T5 taxonomy, not a pattern (it's an archetype extension). **Documented in Phase 4b + entity pages; not registered.** Follow v30 OpenHands SWE-agent T5 sub-type precedent.
3. **"Hong Kong regional archetype"** — considered; Pattern #73 Regional-Archetype-Registry T1 is **T1-scoped** (73a Korean + 73b VN + 73c Pakistani). DeepTutor is T5. **Cross-tier observation only** — do NOT extend 73 to T5. Follow v37 VN cross-tier discipline.
4. **"Bilateral runtime-and-skill"** — SKILL.md exposes DeepTutor CLI for agent consumption WHILE DeepTutor itself runs agents (TutorBot + Capabilities). Novel dual-role. **Rejected standalone registration** — N=1, overlaps conceptually with Pattern #2 Distribution Evolution + Pattern #18 Agent Runtime Standardization. Document as observational corpus-first.
5. **"Multi-agent-living-book compiler"** — Book Engine 14-block-type multi-agent pipeline. Novel but N=1 and narrow-domain-specific. **Rejected; documented as corpus-first.**
6. **"arXiv-pending academic release"** — arXiv "Coming Soon" badge as deliberate pre-registration signal. Overlaps with Pattern #42 Academic-Published Peer-Reviewed Framework (confirmed v31 mini-audit at N=2 LlamaFactory + OpenHands). arXiv-pending does not yet qualify as Pattern #42 data point (not published). **Observational strengthening-in-waiting noted; not currently a #42 data point.**

**Un-stale check (all NEGATIVE):**
- #45 Dual-Licensing — NEGATIVE (Apache-2.0 single-license)
- #46 Duo-Founder + Team — NEGATIVE (HKUDS lab, not duo; `@pancacake` sole named maintainer)
- #52 Extreme-Viral-Velocity — NEGATIVE (~190/day is sustained-viral, not extreme; ~1K/day is threshold)
- Retired revivals (#14 / #16 / #23 / #25 / #49 / #55 / #60 / #70) — all NEGATIVE

**Counter-evidence observations (documented, not refining):**

- **Pattern #22 AGENTS.md industry standard** (confirmed) — DeepTutor AGENTS.md is 149-line rich architecture doc (mid-range between v36 pi-mono 182-line maximum and v37 bizos 327B minimum). Strengthens #22 adoption at T5 tier. No formulation change.
- **Pattern #18 Agent Runtime Standardization** (confirmed) — DeepTutor does NOT integrate OpenClaw/Hermes/MCP as primary; SKILL.md is own native agent-skill convention for nanobot (in-house runtime). **2nd T5-tier MCP-exclusion counter-evidence** after v36 pi-mono (T1-scale MCP-exclusion). Pattern #18 formulation post-v36 explicitly documents T1-scale deliberate-rejection; DeepTutor extends observation to T5 academic-research scope. **If N=2 emerges (another academic-lab T5 rejecting MCP), could justify refinement to "MCP-exclusion by scope type: T1-commercial + T5-academic-research."** Observational, not refining yet.
- **Pattern #28 Multi-Provider AI Support** (confirmed v25) — DeepTutor supports 27 LLM providers + 7 embedding providers + 7 search providers (35+ provider integrations total). **Corpus-most extensive provider coverage at T5.** Reinforces pattern; no formulation change.
- **Pattern #12 Governance-Depth correlates with organization** (confirmed v13 refined v28) — HKUDS academic-lab with 48 contributors + 1 named maintainer (`@pancacake`) + `dev`/`multi-user` branching + 7-tool pre-commit stack. **Medium governance at 21K-star academic-lab scale** — consistent with academic-lab archetype (lighter than corporate Microsoft / heavier than solo).

**Consolidation-forward discipline:** APPLIED. Zero new active candidates. 6 overlap-pre-check rejections; all observations routed to strengthening existing patterns or corpus-first notes.

**Pattern #44 Academic-Lab Affiliation strengthening to N=3:**
Currently confirmed at N=2 (Lab4AI LlamaFactory v22 + UIUC+CMU OpenHands v30 at v31 mini-audit promotion). HKUDS (HKU Data Intelligence Lab) is **3rd data point across a 3rd distinct institution** (Asia-academic-lab expanding the pattern from Chinese-academic-lab + US-academic-lab to Asia-HK-academic-lab). Pattern #44 strengthens to N=3. **Significance: moves from structurally-unambiguous-N=2 (criterion 2) to default-≥3-observations (criterion 1) — first academic-lab pattern to satisfy the default criterion.**

**Pattern #17 within-pattern variant observation:**
HKUDS publishes 7 major agent repos (~173K combined). Fits variant 5 "ecosystem-scale commercial platform" EXCEPT HKUDS is academic-lab not commercial. Proposes observational variant **5a academic-lab-ecosystem-portfolio** (vs current variant 5 commercial HuggingFace + Microsoft). N=1 observational; if another academic-lab ecosystem-portfolio emerges (e.g., Stanford-NLP or Berkeley-RISE with N≥3 agent repos at N≥20K each), could justify within-pattern variant-at-N=2 promotion. Documented; not registered.

## Phase 0.9 Primitive-count probe — YELLOW (3rd YELLOW in corpus)

**Primitive surface** (~120-150 distinct):

- **4 entry surfaces** (Web UI / CLI Typer / WebSocket API / Python SDK)
- **7 tools** (rag / web_search / code_execution / reason / brainstorm / paper_search / geogebra_analysis)
- **4 built-in capabilities** (chat / deep_solve / deep_question / deep_research)
- **6 Chat modes** (Chat / Deep Solve / Quiz Generation / Deep Research / Math Animator / Visualize)
- **5 playground plugins** (deep_research + plugins/ discovery loader)
- **14 Book Engine block types** (text / callout / quiz / flash cards / code / figure / deep dive / animation / interactive demo / timeline / concept graph / section / user note / placeholder)
- **15 CLI command families** (`run` / `chat` / `serve` / `bot` / `kb` / `memory` / `session` / `notebook` / `book` / `config` / `plugin` / `provider` + deeper subcommands)
- **12 REPL slash commands** (/quit / /session / /new / /tool / /cap / /kb / /history / /notebook / /refs / /config / /regenerate / /retry)
- **27 LLM provider bindings** (AiHubMix + Anthropic + Azure OpenAI + BytePlus + BytePlus Coding Plan + Custom + DashScope + DeepSeek + Gemini + GitHub Copilot + Groq + llama.cpp + LM Studio + MiniMax + Mistral + Moonshot + Ollama + OpenAI + OpenAI Codex + OpenRouter + OpenVINO + Qianfan + SiliconFlow + Step Fun + vLLM + VolcEngine + VolcEngine Coding Plan + Xiaomi MIMO + Zhipu)
- **7 embedding providers** (OpenAI / Azure OpenAI / Cohere / Jina / Ollama / vLLM-LM-Studio / custom)
- **7 search providers** (Brave / Tavily / Serper / Jina / SearXNG / DuckDuckGo / Perplexity)
- **8+ multi-channel bot connectors** (Telegram / Discord / Slack / Feishu / WeChat Work / DingTalk / Email / more)
- **4 knowledge objects** (Knowledge Base / Notebook / Question Bank / Skill)
- **2 memory dimensions** (Summary / Profile)
- **TutorBot objects** (Soul Template / Workspace / Heartbeat / Team/Sub-agents)
- **Co-Writer primitives** (multi-document Markdown + Rewrite/Expand/Shorten + save-to-notebook)
- **9 README languages**
- **4 installation options** (Setup Tour / Manual Local / Docker / CLI-only)
- **17 StreamEvent types implicit** (stage_start / stage_end / content / thinking / observation / tool_call / tool_result / progress / sources / result / error + more)

**Outcome: YELLOW** (2-3× GREEN baseline ~50-70 primitives; lower density than v36 pi-mono ~150-200 or v37 bizos ~150-180). **3rd YELLOW in corpus.**

**Scope-compression decisions (v2.1 informal discipline):**

- **4 entity allocation:**
  1. **DeepTutor core product** — 4 entry surfaces + 7 tools + 4 capabilities + 6 chat modes + Book Engine (14 blocks) + Co-Writer + Knowledge Hub + Memory (combined; cite upstream README for exhaustive per-mode detail)
  2. **TutorBot + CLI + nanobot ecosystem** — Persistent autonomous tutor + SKILL.md bilateral agent-skill + 12 REPL slash commands + 15 CLI command families + `.env`-configured 27+7+7 providers (combined)
  3. **HKUDS Data Intelligence Lab @ HKU + ecosystem-portfolio + academic-lab archetype + `@pancacake` maintainer** — 7-repo portfolio + Pattern #44 N=3 strengthening + cross-project HKUDS lineage (nanobot / LightRAG / RAG-Anything) + Asia-academic-lab archetype
  4. **27th consecutive Storm Bear meta-entity** — education-application T5 as operator-education-tool candidate + self-directed-learning workflow + VN-operator localization assessment + Scrum-coach training pilot + Pattern #44 academic-lab-as-credibility-signal

- **Lossy compression accepted:** per-provider setup details cite upstream README .env.example; per-block-type Book Engine implementation cites upstream source; per-CLI-flag enumeration abbreviated to category summaries.
- **Citation-not-replication:** full 759-line README + 148-line SKILL.md + 149-line AGENTS.md cited by path rather than replicated; full provider tables cite README anchor links; CLI command reference cites SKILL.md.
- **Velocity overhead expected:** ~2h 30min-2h 40min (vs ~2h GREEN baseline), consistent with v36 and v37 YELLOW precedents.

## Phase 4b routing mode

**Primary:** **T5 6-way comparison + Pattern #44 Academic-Lab Affiliation N=3 strengthening analysis + NEW education-application T5 sub-archetype formalization + Pattern #17 within-pattern academic-lab-ecosystem-portfolio variant 5a observation + 9-language i18n top-tier observation + arXiv-pending Pattern #42 observational note**

**Secondary:** Bilateral runtime-and-skill corpus-first (DeepTutor both runs agents AND exposes SKILL.md for external agents)

**Tertiary:** HKUDS ecosystem-portfolio as "academic Hugging Face" observation (6 sibling agent repos; cross-project lineage via nanobot + LightRAG)

**Novelty:** First Asia-academic-lab T5 + first education-application T5 sub-archetype + first 9-language top-tier T5 + first multi-agent-living-book-compiler (14 block types) + first persistent-autonomous-tutor-bot architecture in corpus + first bilateral runtime-and-skill T5 + first SEVENTH-repo-ecosystem-portfolio academic lab in corpus + first arXiv-pending observation-in-waiting + first ManimCat integration (math-animation specialist upstream) + first Unified Chat Workspace 6-mode single-thread UX + Pattern #44 reaches N=3 default criterion + Pattern #28 27-provider corpus-most coverage

## Storm Bear meta-entity warranted?

**YES (27th consecutive).** DeepTutor is **education-application T5** — the closest corpus peer to Storm Bear operator's "AI agents learning tool" mission. Scrum coach role involves teaching teams; DeepTutor's "personalized learning companion" is domain-adjacent. **Direct pilot viability HIGH for self-directed learning** (use DeepTutor to learn advanced AI/Scrum topics) + **MEDIUM for teaching workflow** (TutorBot could be VN-Scrum-coach persona). Apache-2.0 + no commercial gate + Python + multi-provider including DeepSeek/Qwen (cost-effective for VN) + Vietnamese-adjacent i18n via zh + Book Engine could compile Scrum body-of-knowledge from PDFs → interactive living book. Pattern #44 academic-lab-as-credibility-signal: HKU paper-forthcoming provides research credibility for VN-client pitches.

## Cross-references

**Sibling wikis cited by this wiki:**

- **v30 OpenHands** — closest structural peer (T5 academic-commercial SWE-agent + academic-lab UIUC+CMU + arXiv-published ICLR 2025); DeepTutor is T5 academic-research education-agent + academic-lab HKU + arXiv-pending → **Pattern #44 N=3 completion data point**
- **v22 LlamaFactory** — 2nd closest (Lab4AI academic-lab + ACL 2024 + outside-scope training-infra); DeepTutor is 3rd academic-lab pattern data point
- **v37 bizos** — primary reference (YELLOW precedent v37 + VN cross-tier observation precedent extended to HK cross-tier here)
- **v36 pi-mono** — YELLOW precedent v36 + MCP-exclusion T1-scale precedent (DeepTutor is MCP-exclusion T5-scale extension)
- **v34 claude-code-best-practice** — 82-tip aggregator comparison (DeepTutor is runtime not aggregator; opposite genre but both self-learning-tool candidates for Storm Bear)
- **v32 claude-howto** — VN-diaspora T1 interactive-self-assessment mechanism (#71 N=1) vs DeepTutor TutorBot persistent-autonomous-tutor (related-but-distinct learning-mechanism observations)
- **v29 crawl4ai** — multi-provider at 20+ count; DeepTutor exceeds at 27
- **v26 HF agents-course** — T3 agent-education multi-framework-BYO; DeepTutor is T5 application (teaches humans) vs T3 HF (teaches agent-builders) — clean tier boundary
- **v27 oh-my-claudecode** — 7-language README top-tier; DeepTutor 9-language extends

**Pattern Library state to update (Phase 5):**
- **Pattern #44 strengthens to N=3** (promotion-state-change from "CONFIRMED at N=2 structurally-unambiguous v31 mini-audit" to "CONFIRMED at N=3 default ≥3-observations-criterion-also-satisfied") — first academic-lab-adjacent pattern to achieve default criterion
- **Pattern #42 arXiv-pending observational** — not yet 3rd data point; tracked
- **Pattern #17 variant 5a academic-lab-ecosystem-portfolio observation** — N=1; not registered standalone; documented
- **Pattern #28 strengthens corpus-most provider count** (27 LLM + 7 embedding + 7 search = 41 integrations)
- **Pattern #18 MCP-exclusion T5-academic-research 2nd scope-type observation** (after T1-scale pi-mono v36)
- **Pattern #27 Community-Viral Scale Path** — 14th data point (~190 stars/day sustained-viral; 20K in 111 days; Asia-academic-amplified sub-path)
- **0 new active candidates; 0 new OBSERVATION-TRACKs**

**Ratio preservation target:** 34 confirmed + 23 active + 4 stale + 8 retired + 4 OT = **73 full / 57 active (ratio 23:34 = 0.68:1 unchanged).**

---

*This file is the project-level context for the v38 wiki build. See `02 Wiki/(C) index.md` for phase tracking and `04 Reviews/(C) 2026-04-24 v38 build learnings.md` for iteration log.*
