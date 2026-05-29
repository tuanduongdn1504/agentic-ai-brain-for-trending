# ai-engineering-from-scratch — Wiki (v113)

> `rohitg00/ai-engineering-from-scratch` · **"Learn it. Build it. Ship it for others."** · A hands-on AI engineering curriculum: 20 phases, 473 lessons (claimed), from raw-math foundations through agent engineering, multi-agent swarms, and production/ethics — every algorithm built from scratch before a framework is imported, every lesson emitting a reusable artifact (prompt / skill / agent / MCP server).

**(C) Claude-generated wiki page.** Fetched 2026-05-29 (GitHub API via `gh` + README / AGENTS.md / SKILL.md). Routine v2.3.1, wiki #113.

---

## Identity

| Field | Value |
|---|---|
| Repo | [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch) |
| What | Hands-on **AI engineering curriculum** (course + framework + skill-emitting workbook hybrid) |
| Tier / archetype | **T3 Education** / NEW sub-archetype *From-Scratch-then-Ship Curriculum with agentskills.io Artifact Emission* (PROVISIONAL N=1) |
| Stars / forks | **24,094★ / 3,904 forks** (fork_ratio **0.162**) |
| Watchers / open issues | 168 / 10 |
| Created / pushed | 2026-03-18 / 2026-05-27 (**~72 days** old at fetch) |
| Velocity | **~335 stars/day → Pattern #52 EXTREME-VIRAL pulse-class** (>300/d), 72-day window (<90d, so NOT Multi-Month-Sustained); **first T3 Education subject in the pulse band** |
| License | **MIT** (LICENSE file + GitHub API agree — clean) |
| Language | **Python** primary (~3.85 MB) + TypeScript / JavaScript / HTML / Julia / Rust / CSS / Shell / Dockerfile |
| Distribution | GitHub (clone) · web `aiengineeringfromscratch.com` (Vercel) · `python3 scripts/install_skills.py` for the 2 meta-skills |
| Default branch / homepage | `main` / aiengineeringfromscratch.com |
| Author | **Rohit Ghumare** (@rohitg00 / @ghumare64) — London UK; iii.dev; GDE @Google Cloud, CNCF Ambassador, Docker Captain, AWS CommunityBuilder; 7-yr account; 303 repos; 3,630 followers |

## What it is

An opinionated, build-everything-yourself path into AI engineering. The thesis from the README header: *"84% of students already use AI tools. Only 18% feel prepared to use them professionally. This curriculum closes that gap."* ~320 hours of material across **20 phases / 473 lessons** (per README), progressing math → ML → deep learning → CV → NLP → speech → transformers → generative → RL → LLMs-from-scratch → LLM-engineering → multimodal → tools/protocols (MCP) → **agent engineering (42 lessons)** → autonomous systems → **multi-agent & swarms** → infra/production → ethics/safety/alignment → capstones.

Each lesson follows a fixed spine:

1. **Motto** — the core idea in one line
2. **Problem** — a concrete challenge
3. **Concept** — intuition + diagrams
4. **Build It** — implement from raw math, no frameworks (Python / TS / Rust / Julia)
5. **Use It** — the same operation through a production library (PyTorch, etc.) so the framework stops being a black box
6. **Ship It** — emit a reusable artifact: an expert **prompt**, an **agentskills.io-format skill**, an **agent** loop, or an **MCP server**

The "Build It / Use It" split is, per AGENTS.md, "the spine."

## Repo layout (verified)

```
phases/                  20 phase dirs (00-setup-and-tooling … 19-capstone-projects)
.claude/skills/          find-your-level/  check-understanding/   ← 2 operational SKILL.md skills (agentskills.io format)
outputs/                 agents/  mcp-servers/  prompts/  skills/  index.json
                         ↑ scaffolded artifact dirs — skills/ holds only .gitkeep (student-generated, not in-repo)
scripts/                 install_skills.py · audit_lessons.py · build_catalog.py · lesson_run.py · scaffold-lesson.sh · …
AGENTS.md                operating manual for contributors AND AI agents touching the repo
LESSON_TEMPLATE.md · ROADMAP.md · SPONSORS.md · site/ · web/ · vercel.json · requirements.txt
```

The 2 shipped skills are **meta-skills about the curriculum itself**: `find-your-level` (an interactive placement quiz that maps your knowledge to a starting phase) and `check-understanding` (per-phase quizzes). They use real agentskills.io YAML frontmatter (`name` / `version` / `description` with trigger phrases / `tags`).

## Tech taught (vendor-neutral)

PyTorch · JAX · Transformers / Hugging Face · vLLM · TensorRT-LLM · LangGraph · CrewAI · AutoGen · **Model Context Protocol (MCP)** · **Anthropic Claude Agent SDK** · OpenAI APIs · Kubernetes / Docker · FSDP / DeepSpeed · Langfuse · OpenTelemetry. Latest content references DeepSeek-V3, Jamba, speculative decoding, computer-use agents.

## Corpus position

**PRIMARY — NEW T3 Education sub-archetype "From-Scratch-then-Ship Curriculum with agentskills.io Artifact Emission" PROVISIONAL N=1.** The three prior T3 Education subjects are structurally different: **[[v74 LLMs-from-scratch]]** is a *book-companion code repo* (passive reference accompanying Manning's book), **[[v77 easy-vibe]]** is a *vibe-coding course* (VitePress site, conceptual), **[[v111 hello-agents]]** is an *agent-building book + companion framework* (HelloAgents). This subject's distinguishing structural property is that its pedagogical **output unit is a deployable agent-artifact**: the Build→Use→**Ship** loop is designed so each lesson emits a prompt / SKILL.md / agent / MCP server, the repo ships 2 operational agentskills.io meta-skills + `install_skills.py`, and scaffolds `outputs/{agents,mcp-servers,prompts,skills}/` for the artifacts. **Honest caveat (load-bearing):** the output dirs are empty `.gitkeep` placeholders — the "473 artifacts" are *student-generated by design*, not shipped in-repo; only the 2 meta-skills are realized. The sub-archetype is registered on the *pedagogical-structure* distinction (artifact-emitting "Ship It" spine), not on a claim of 473 in-repo artifacts. Full proposal: `01 Analysis/(C) T3-NEW-sub-archetype-From-Scratch-then-Ship-Curriculum-with-skill-emission-N1.md`.

**Secondary (OC layer):**
- **Pattern #81 sub-observation "names-the-drift-and-drifts-anyway" N=2** (anchor agentmemory v66; v113 = N=2). **Directly verifiable manifest drift across three files:** README **473 lessons / 473 artifacts**, AGENTS.md **435 lessons** (verbatim: *"Every rule below keeps 435 lessons coherent over time"*), `find-your-level/SKILL.md` **"260-lesson" / "260+ lessons"**. The repo explicitly invokes coherence-as-discipline while its own headline count has drifted across three surfaces, with no CI guard. This is the **inverse pole** of Pattern #81 proper (Manifest-Drift-*as-First-Class-CI-Concern*, anchored v64 claude-seo's 5-version atomic-bump CI with 13 assertions) — so it strengthens the agentmemory sub-observation, **not** clean #81.
- **Pattern #57 57k Standards-Conformance-Layer chain** — agentskills.io implementer at education-curriculum scale (joins v76 → v93 → v98 → v99 → v100). First *education* implementer in the chain; honest: modest realization (2 meta-skills + AGENTS.md, not a large library).
- **Pattern #52 EXTREME-VIRAL pulse N+1** (anchors v63 Karpathy + v68 zero) — and the **first T3 Education subject** to reach the pulse band (prior education subjects: v74 ~92/d, v77 ~92/d, v111 ~206/d).
- **Pattern #84 Cross-Vendor Ecosystem-Tolerance** — teaches PyTorch/JAX + Claude SDK + OpenAI + LangGraph/CrewAI/AutoGen + MCP vendor-neutrally (curriculum-as-vendor-neutral-tour).
- **Pattern #82 quantitative-marketing** ("84% use AI / 18% prepared", "473 lessons", "~320 hours", "473 artifacts you authored"); **Pattern #19** Indian-diaspora-London-DevRel profile (NOT a new (a) sub-axis per the v98 precedent); **Library-vocab #12** LLM-routing artifacts (AGENTS.md + `.claude/skills/`).

## Functional fit (Storm Bear)

**Verdict: STRONG INCLUDE 3/4** — (a) **FAIL** / (b) STRONG / (c) STRONG / (d) STRONG. NOT STRONGEST (no STRONGEST criterion). Full reasoning: `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md`.

- **(a) FAIL** — Rohit Ghumare is a **London, UK** engineer + established global DevRel (Google Cloud GDE, CNCF Ambassador, Docker Captain), Indian-heritage. None of the 7 (a) sub-axes PASS: not VN/Asian-located-peer, no Tiếng Việt or VN-locale inclusion (English-only), not a community-org cultural-peer, and **not (a)-7** (personal repo `rohitg00/*`, not a foundational-vendor org). Per §25 + the v98 (Indian-diaspora-Berlin) and v112 (Pakistani-Dublin) precedents, no new (a) sub-axis is coined for a single South-Asian-diaspora-London instance. Honest FAIL.
- **(b) STRONG** — this is, alongside [[v111 hello-agents]], the **single most goal-aligned learning resource** in the recent corpus for Storm Bear's #1 goal ("Master Claude and autonomous agents for software development"): Phase 13 *Tools & Protocols* (MCP, 23 lessons) + Phase 14 *Agent Engineering* (42 lessons) + Phase 16 *Multi-Agent & Swarms* (25 lessons) + Claude Agent SDK throughout. **Cost-to-try: LOW** (clone + read) to **MINIMUM** (install 2 skills via `install_skills.py`, reversible by delete). It is a **READ/learning pilot, not an operational vault tool** — so STRONG, not STRONGEST.
- **(c) STRONG** — highly instructive: from-scratch-before-framework pedagogy, fixed Build/Use/Ship lesson spine, 20-phase progression, ethics/safety as required not optional. A reference for *how to structure* a curriculum (relevant to Storm Bear's own routine-pedagogy work).
- **(d) STRONG** — high corpus connectivity: T3 Education sibling to v74 + v77 + v111; agentskills.io 57k implementer; Pattern #81 sub-observation N=2 with v66; teaches/cites v72's DeepSeek + LangGraph/CrewAI/AutoGen + MCP; Patterns #52/#57/#82/#84.

**Pilot:** **HIGH-RELEVANCE READ-pilot** for the #1 goal — but a *reading/learning* commitment, not a vault install. Recommended fenced trial: read Phase 13 (MCP) + the first ~10 lessons of Phase 14 (Agent Engineering), and optionally install `find-your-level` to placement-test. It complements [[v111 hello-agents]] (read-pilot, agent fundamentals) — hello-agents is the gentler book-led path; this is the broader build-everything path. Does **not** join the operational Claude-Code-adjacent install stack (claude-mem / harness / humanizer / cclog-cli).

## Honest non-claims

- **Not a clean Pattern #81 strengthening** — Pattern #81 proper is manifest-drift-*as-CI-concern* (a discipline that prevents drift). This repo exhibits the inverse (drift without CI), so it's a **sub-observation N=2**, not top-level #81.
- **Not a Pattern #52 promotion** — pulse N+1 in a 72-day (<90d) window; could mature toward Multi-Month-Sustained if velocity holds to ~v118+.
- **agentskills.io 57k chain extension is modest** — 2 operational meta-skills + AGENTS.md; `outputs/skills/` is empty `.gitkeep`. The "473 artifacts" are student-generated aspirational, not in-repo.
- **Not (a)-7** — personal repo, not a foundational-vendor org; author is Google Cloud DevRel, not Anthropic/OpenAI/Google org-direct.
- **NEW sub-archetype is N=1 PROVISIONAL** — registered on pedagogical-structure distinction; promotion-eligible toward N=2 only if a second "Ship-It-emits-deployable-artifacts" curriculum appears.
- CORPUS-FIRST claims (first T3-education pulse-EXTREME-VIRAL; first artifact-emitting curriculum) are scoped + pressure-test-ready, held as cautious notes.

## Sources

- Repo + GitHub API metadata (`gh`) + README + AGENTS.md + `.claude/skills/find-your-level/SKILL.md` + repo tree (fetched 2026-05-29).
- Corpus cross-refs: [[v111 hello-agents]] · [[v77 easy-vibe]] · [[v74 LLMs-from-scratch]] · [[v72 DeepSeek-TUI]] · agentmemory v66 (Pattern #81 sub-observation anchor) · Pattern #52 / #57 / #81 / #82 / #84 / #19 (`PATTERN_LIBRARY.md` + `_patterns/`).
- Routine: `05 Skills/llm-wiki-routine-v2.3.md` (v2.3.1).
