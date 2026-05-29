# hello-agents — Wiki (v111)

> *"📚 《从零开始构建智能体》—— 从零开始的智能体原理与实践教程"* — "Building Intelligent Agents from Scratch: a principles-and-practice tutorial that takes you from LLM *user* to agent-system *builder*."

## 1. Identity & metadata

| Field | Value |
|---|---|
| Repo | `datawhalechina/hello-agents` |
| What it is | Free, open-source **technical book + hands-on tutorial** teaching how to build LLM agents from scratch — 16 chapters / 5 parts + a self-developed companion framework (**HelloAgents**) |
| Org | **Datawhalechina** — Chinese AI/ML open-source education community (**SECOND datawhale subject in corpus** after [[v77 easy-vibe]]) |
| Project lead | **Chen Sizhou / 陈思州 (Sizhou Chen, @jjyaoao)** — location "China", Datawhale member, bio "interested in LLM Agent / Audio / Speech", 297 followers, GitHub since 2021; **also author of the companion framework `jjyaoao/HelloAgents`** |
| Co-sponsors | **Sun Tao (@fengju0213, CAMEL-AI)** + **Jiang Shufan (@Tsumugii24)** |
| Advisory expert | **Zhu Xinzhong** — Chief Scientist, Datawhale; **Zhejiang Normal University** (the academic anchor; cf. v77's Fang Ke / Tsinghua) |
| Contributor affiliations | Zhejiang University · Nanjing University · Beijing Univ. of Posts & Telecommunications · Imperial College London (+ others) |
| Tier / archetype | **T3 Education** / community-org-published integrated open-source book + companion framework (cf. v74 commercial book-companion · v77 web vibe-course) |
| License | **CC BY-NC-SA 4.0** (LICENSE.txt confirmed: "Attribution-NonCommercial-ShareAlike 4.0 International") — GitHub API reports `NOASSERTION` = **Pattern #83 83f.3** mismatch (same as v77) |
| Primary language | **Python 72.5%** + Jupyter 11.2% + Vue 8.4% + HTML 2.9% + JS 2.5% + CSS 1.1% |
| Stars / forks / subs | **54,441 ★ / 6,655 forks / 172 subscribers** · ~65 open issues (Issues tab; API `open_issues_count` 126 incl. PRs) |
| Created / pushed | **2025-09-07** / 2026-05-26 (~264 days) |
| Velocity | **~206 stars/day → Pattern #52 HIGH-NOT-EXTREME (150–300/d)**, sustained 264 days (2nd-longest HIGH-NOT-EXTREME sustenance after cc-switch's 289d) |
| fork_ratio | 0.122 — strong active-deployment signal (higher than v77's 0.095; below the 0.15 high-bar) |
| Releases / commits | 2 releases (latest **V1.0.2**, 2026-02-10) / 795 commits · default branch `main` · Discussions ENABLED |
| Topics | `agent` · `llm` · `rag` · `tutorial` |
| Size | ~218 MB (asset/notebook-heavy) |
| Homepage | https://hello-agents.datawhale.cc · https://datawhalechina.github.io/hello-agents/ · PDF via Datawhale |

## 2. What it is

A **from-scratch, systems-level curriculum** that walks a Python-capable developer from "I call an LLM API" to "I build, train, and evaluate agent systems." It is published by Datawhale as a free open-source book (the repo *is* the book — Chinese-primary prose + English README + runnable code + notebooks), not a code-companion to a separately-sold book. Target audience: AI developers, software engineers, and students with basic Python + LLM-API familiarity (no algorithm/training background required).

**16 chapters across 5 parts:**

- **Part 1 — Agent & LLM fundamentals:** (1) Intro to Agents · (2) History of Agents · (3) LLM Fundamentals (Transformer)
- **Part 2 — Building your LLM agent:** (4) Classic paradigms — **ReAct / Plan-and-Solve / Reflection** · (5) Low-code platforms — **Coze / Dify / n8n** · (6) Framework practice — **AutoGen / AgentScope / LangGraph** · (7) **Build your own agent framework** (→ the HelloAgents framework)
- **Part 3 — Advanced extension:** (8) Memory & Retrieval · (9) **Context Engineering** · (10) Communication protocols — **MCP / A2A / ANP** · (11) **Agentic-RL** (SFT → GRPO) · (12) Performance evaluation & benchmarking
- **Part 4 — Comprehensive case studies:** (13) Intelligent Travel Assistant · (14) Automated Deep-Research Agent · (15) Building a Cyber Town (multi-agent simulation)
- **Part 5 — Capstone:** (16) Capstone project

Plus **`Extra-Chapter/`** (12 community contributions — interview questions, context-engineering, Dify tutorials, …), **`Additional-Chapter/`**, and **`Co-creation-projects/`** community co-authored work.

**Companion framework — `jjyaoao/HelloAgents`** (1,813 ★, Python, created 2025-09-11, 4 days after the tutorial): a self-developed agent framework "based on the OpenAI-native API" that Chapter 7 teaches you to build toward and that students then reuse. The book *teaches you to build the very framework it ships* — a tight tutorial↔framework loop by the same lead author.

## 3. Repository layout

```
hello-agents/
├── docs/                  ← the book chapters (VitePress site; Vue 8.4% + HTML/CSS) → hello-agents.datawhale.cc
├── code/                  ← runnable chapter code (Python primary)
├── Extra-Chapter/         ← 12 community-contributed extra chapters
├── Additional-Chapter/    ← additional material
├── Co-creation-projects/  ← community co-authored agent projects
├── README.md · README_EN.md
├── LICENSE.txt            ← CC BY-NC-SA 4.0 (full text present; API still NOASSERTION → 83f.3)
└── fix_bold_format.py · 读者反馈问卷.png · 读者群二维码.png (reader-feedback + community-group QR)
```

## 4. Corpus position (cross-references)

- **Pattern #19 sub-mechanism 19h "Chinese-Educational-Community-Organization-with-University-Anchor" N=2 STRENGTHENING (PRIMARY)** — v77 easy-vibe (Datawhale + **Tsinghua**, lead Sanbu, mentor Fang Ke) registered 19h PROVISIONAL N=1; v111 hello-agents (Datawhale + **Zhejiang Normal University**, lead Chen Sizhou, advisor Zhu Xinzhong) = **N=2**. Same org-archetype, **different sub-team + different university anchor + different academic mentor** = genuine cross-instance spread within the sub-mechanism, relieving the Pattern #19 graveyard by moving a N=1 candidate → N=2. See `01 Analysis/(C) Pattern-19-19h-...N2-strengthening.md`. **Honest caveat:** both instances are the *same parent org* (Datawhale) → validated within Datawhale, not yet cross-org.
- **datawhale = 2nd same-org 2-wiki cluster in v60+ window** — after [[v83 open-design]] + [[v91 html-anything]] (nexu-io). But a **structurally different variant**: nexu-io = *indie-org product-portfolio* (one small team, 5 products in 90 days); datawhale = *large-community-org multi-independent-project* (different sub-teams, different academic anchors). Corpus-novel same-org-cluster *kind*.
- **Pattern #52 HIGH-NOT-EXTREME N+1 (post-CONFIRMED strengthening)** — ~206/d × 264d. NOT a promotion (sub-class CONFIRMED at v73); notable as the **2nd-longest HIGH-NOT-EXTREME sustenance window** after cc-switch (289d).
- **Pattern #83 83f.3 license-declaration-vs-API mismatch N+1** — CC BY-NC-SA 4.0 in LICENSE.txt + README, but API `NOASSERTION` (GitHub's detector won't classify a CC content-license as a code license). **Exact same observation as v77** = same-org repeat.
- **Pattern #45 CC-NC license-family** — v77 (CC BY-NC-SA 4.0) + [[v90 academic-research-skills]] (CC-BY-NC 4.0) + v111 (CC BY-NC-SA 4.0) = N=3 by-instance, but only **2 distinct authors** (Datawhale ×2 + Edward Wu) → cross-author spread is weak; SECONDARY/OC only.
- **Pattern #57 57c-product framework-citation density (taught-tools)** — AutoGen ([[v89 VibeCodingTracker]] pinned microsoft/autogen) + Dify ([[v77 easy-vibe]] covered) + n8n (corpus subject) + MCP ([[v66 agentmemory]] / [[v70 codegraph]] / [[v76 agent-skills-standard]]) + Coze + LangGraph + AgentScope. These are *tools taught*, not the subject's substrate — citation density is high but at the curriculum layer.
- **CAMEL-AI cross-link** — co-sponsor Sun Tao (@fengju0213) is from CAMEL-AI (camel-ai/camel, a multi-agent framework), tying the subject into the broader agent-framework ecosystem.
- **China-Mainland sub-cluster + Asian-LOCATED cluster extension** — joins v82 / v83 / v91 / v94 / v100 / v105 (China-Mainland) + the broader Asian-LOCATED cluster.
- **T3 Education tier** — distinct from [[v74 LLMs-from-scratch]] (commercial book-companion code), [[v77 easy-vibe]] (web vibe-course, JS-primary, no framework), and [[v79 autoresearch_folktales]] (research-framework derivative). hello-agents = *integrated open-source technical book + self-developed companion framework* → OC-layer T3 sub-archetype candidate (held at OC, not promoted, per cascade-discipline).

## 5. Functional fit / pilot relevance

**HIGH — Tier-1 relevance to Storm Bear's #1 stated goal.** The vault's CLAUDE.md main goal is verbatim *"Master Claude and autonomous agents for software development."* hello-agents is the single **most goal-aligned subject in the recent corpus** for that goal: a free, comprehensive, from-scratch curriculum on exactly the agent paradigms, frameworks, memory/retrieval, context-engineering, protocols, RL, and evaluation the operator wants to master.

Three chapters map **directly onto the vault's own machinery**:
- **Ch 8 Memory & Retrieval** ↔ the claude-mem v103 pilot + the vault's documented context-thrashing problem.
- **Ch 9 Context Engineering** ↔ the LLM Wiki Routine's own context-budget discipline (chapter-file sizing, surgical extracts).
- **Ch 12 Performance Evaluation** ↔ the Pattern Library audit/eval cadence.

**Pilot type = READ, not install.** Cost-of-trial MODERATE (it's a 16-chapter book — a reading commitment, not a 5-minute tool trial), but zero-risk and reversible (it's free reading; CC-BY-NC is fine for personal vault learning). Recommended fenced trial: read Part 3 (Ch 8–9–12) first — the chapters most directly applicable to improving the vault's own routine — then sample Ch 4 (classic paradigms) for the conceptual base. Complements the install-pilot stack (claude-mem / harness / humanizer / cclog-cli) as the *learning/methodology* leg.

## 6. Honest caveats / non-claims

- **NOT a Pattern #52 promotion** — HIGH-NOT-EXTREME is CONFIRMED (N=3 at v73); this is post-CONFIRMED N+1 strengthening only.
- **NOT a Claude Code skill / NOT in the agentskills.io (57k) chain** — it's a tutorial that *teaches building agents*; no SKILL.md / AGENTS.md / plugin manifest.
- **NO new top-level Pattern** — the PRIMARY is a sub-mechanism (19h) N=2 strengthening, not a structural first.
- **19h same-org caveat** — both 19h instances are Datawhale; the sub-mechanism is validated *within* Datawhale, not yet across multiple Chinese-edu community-orgs (cross-org N=2 still owed).
- **Different team from v77** — this is NOT the same people as easy-vibe (Chen Sizhou + Zhejiang Normal, not Sanbu + Tsinghua). The shared element is the *org* and the *org-archetype*, not the contributors.
- **Chinese-primary content** — README_EN exists, but the chapter depth is Chinese; non-Chinese readers face a partial language barrier (mitigated by code being language-neutral).
- **CC-NC = non-commercial** — fine for the operator's personal learning use; would matter if vault content ever republished commercially.

## 7. Storm Bear verdict (Phase 0.9 STRICT)

**STRONG INCLUDE 4/4** (4× STRONG, balanced — cf. v89): (a) STRONG via (a)-4 community-org cultural-peer PROBABLE-PASS (Datawhale + university-anchor, same call as v77) + China-Mainland/Asian cluster extension · (b) STRONG — most goal-aligned subject in recent corpus for the #1 "master agents" goal; MODERATE-cost read, DIRECT applicability · (c) STRONG — rich agent-building methodology, Ch 8/9/12 directly inform the vault's own routine · (d) STRONG — same-org as v77 + many taught-tools are corpus subjects. Streak → **"41+1*"** (22nd consecutive clean PASS post-v84 OVERRIDE). Full reasoning: `01 Analysis/(C) Phase-0-and-0.9-INCLUDE-verdict.md`.

## Sources
- [datawhalechina/hello-agents · GitHub](https://github.com/datawhalechina/hello-agents) (metadata + README_EN verified via GitHub API 2026-05-29)
- [Sizhou Chen / 陈思州 (@jjyaoao) · GitHub profile](https://github.com/jjyaoao)
- [jjyaoao/HelloAgents — companion framework](https://github.com/jjyaoao/HelloAgents)
- [Online book — hello-agents.datawhale.cc](https://hello-agents.datawhale.cc) · [datawhalechina.github.io/hello-agents](https://datawhalechina.github.io/hello-agents/)
