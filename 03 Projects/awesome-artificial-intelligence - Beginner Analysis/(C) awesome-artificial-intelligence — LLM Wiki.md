# (C) awesome-artificial-intelligence — LLM Wiki (v170)

> **Ship:** v170 · 2026-06-20 · branch `wiki/v170-awesome-ai` off `main` (based at `8def4ba` = v169, which is not yet merged — branching off `main`/`b55e0d4` would orphan the v168 + v169 cumulative state)
> **Verdict:** GOAL-ALIGNED INCLUDE 3/4 — (a) FAIL · (b) MODERATE · (c) MODERATE · (d) STRONG
> **Pattern outcome:** **Pattern #68 (Awesome-List-Genre Meta-Pattern) instance-strengthening** — v170 is the corpus's first **broad, opinionated AI-engineering practitioner field-map** instance (spanning learn + build + agents + models, vs the prior single-vertical lists). NO new top-level pattern (max stays **#85**). NO new Library-vocab. Counts UNCHANGED (**46 / 10**). Secondary observations only (NO mint): an opinionated-curation sub-flavor, a long-lived-curator-pivot #78 cross-reference, and a Claude-Code-first / Anthropic-guide-first ordering note.
> **Tier:** **OUTSIDE-SCOPE** (consistent with every prior awesome-list: build-your-own-x v8 / awesome-design-md v25 / awesome-mcp-servers v31 / awesome-claude-skills v50).
> ✅ **Continues the domain variation** — a **third** consecutive non-(operating-niche) ship after v168 ponytail (code-minimalism) and v169 SkillSpector (defensive-security). v170 is the corpus's **first awesome-list since v50** (~120 wikis) and the broadest-scope #68 instance to date.
>
> ⚠️ **(b) MODERATE is an operator-reviewable calibration.** A STRONG case exists (the list is an opinionated AI-*engineering* map with Claude Code + Anthropic's guide listed first, and it sits epistemically *upstream* of the vault's own subject selection). It is held at **MODERATE** for consistency: it is broader than the Claude/autonomous-agents core, it is a *reference/orientation* meta-resource (not a tool you operate or a substrate), and it is broader than awesome-claude-skills v50 (which was itself only MODERATE-to-STRONG). Either rating ships GOAL-ALIGNED (§31 keys the tier on (b) MODERATE+). See §5.

---

## 1. What it is

`owainlewis/awesome-artificial-intelligence` — GitHub description, verbatim:

> *"A curated list of Artificial Intelligence (AI) courses, books, video lectures and papers."*

That tagline is the **old** identity. The README itself has been **modernized into a tight, opinionated AI-engineering field-map**. Its preamble, verbatim:

> *"A curated collection of must-use, actively maintained resources for building and shipping AI systems."*

…with the stated focus on *"AI engineering (RAG, agents, evals, guardrails, deploy) plus the best books, guides, papers, and a carefully selected set of tools"* and an explicit anti-bloat note: *"you don't need tons of frameworks — start with simple LLM calls and work up."*

So it is **not** a sprawling, alphabetical, community-PR-intake "everything AI" list. It is a **curated, opinionated, actively-maintained-only** map for a practitioner who wants to learn AI engineering and ship agentic software — and its center of gravity is squarely on-goal: **Claude Code is the #1-listed coding agent** and **Anthropic's "Building Effective Agents" is the #1-listed guide.**

It is a **curated awesome-list** — a README of links, not software. The only code in the repo is a small Python tooling shell (`.python-version` + `pyproject.toml`, almost certainly a link-checker / CI). The product is the curation.

This is the corpus's **first awesome-list subject since v50** (awesome-claude-skills, ~120 wikis ago) and, structurally, the **broadest-scope** awesome-list it has analyzed — the prior four each cover a single vertical (tutorials / design-templates / MCP-servers / Claude-skills); this one spans the whole AI-engineering field.

## 2. What's in it (the curated contents)

Five top-level sections, each opinionated and short:

- **📚 Learn**
  - *Books (Modern & Practical):* Designing ML Systems · AI Engineering · Build an LLM from Scratch · Hands-On LLMs · LLM Engineer's Handbook · The 100-Page Language Models Book · Generative Deep Learning.
  - *Books (Foundational):* Artificial Intelligence: A Modern Approach · Deep Learning (Goodfellow) · Deep Learning: Foundations & Concepts (Bishop) · Understanding Deep Learning · Speech & Language Processing · Reinforcement Learning: An Introduction (Sutton & Barto).
  - *Courses:* Google GenAI path · Hugging Face LLM Course · fast.ai · Stanford CS324 · Full Stack Deep Learning · MIT 6.S191 · DeepLearning.AI shorts · DeepMind RL · **Karpathy — Neural Networks: Zero to Hero**.
  - *Landmark Papers:* Attention Is All You Need · Scaling Laws · GPT-3 (Few-Shot Learners) · **Constitutional AI**.
- **🛠 Build**
  - *Guides & Playbooks:* **Anthropic — Building Effective Agents (listed first)** · OpenAI Agents Guide · Google AI Agents paper · Google Agents Companion · OpenAI Cookbook · LLM Engineer Handbook.
  - *Frameworks:* PocketFlow · Google ADK · Pydantic-AI · LangGraph · CrewAI · AutoGen · LlamaIndex · Haystack · Docling.
  - *Evals:* OpenAI Evals. *IDEs:* Cursor · GitHub Copilot.
- **🤖 Agents → Coding (17 tools):** **Claude Code (listed first)** · Codex CLI · Gemini CLI · Cursor CLI · Aider · OpenCode · OpenHands · Cline · Continue · Goose · Factory Droid · Amp · Mistral Vibe · Qwen Code · Pi · Nanocoder · Kilo CLI.
- **🧠 Models:** *Language* — ChatGPT · **Claude** · Gemini · Grok · Llama · Mistral · DeepSeek · Qwen · Kimi · GLM · Cohere. *Image / Video / Audio* sets. *Compare* — OpenRouter · LMArena · Artificial Analysis.
- **📡 Follow → Newsletters:** The Rundown AI · AlphaSignal · Superhuman AI · AI Engineer.

**Style:** curated and *opinionated* (not alphabetical), restricted to "must-use, actively maintained" entries. No contribution guidelines, no badges. The selection itself — and its ordering — is the editorial signal.

## 3. The curation philosophy (what distinguishes it from the other awesome-lists)

The other corpus awesome-lists (v8 build-your-own-x, v25 awesome-design-md, v31 awesome-mcp-servers, v50 awesome-claude-skills) are **single-vertical, community-PR-intake, broadly-inclusive** directories. This one is different on two axes:

1. **Opinionated, exclusionary curation.** "Must-use, actively maintained" + "you don't need tons of frameworks" is an *editorial point of view*, not an inclusive catalog. It is closer to a senior engineer's recommended reading/tooling shortlist than to a comprehensive index.
2. **Cross-domain field-map breadth.** It deliberately spans the *whole pipeline* of becoming an AI-engineering practitioner — theory (foundational books) → modern practice (engineering books, courses, papers) → build tooling (frameworks/evals/IDEs/guides) → the agent layer (17 coding agents) → the model layer (multi-vendor) → staying-current (newsletters). The others each cover one slice.

These are **within-pattern refinements** of Pattern #68 (see §6), not a new pattern — but they are what makes v170 the most goal-adjacent awesome-list in the corpus.

## 4. How it works (architecture, such as it is)

There is essentially no runtime architecture — it is a curated `README.md`. The repo carries a thin Python tooling layer (`.python-version`, `pyproject.toml`) that is almost certainly a **link-checker / freshness CI** (consistent with the "actively maintained" claim — dead links would undercut the editorial promise). MIT-licensed. Distribution = read the README on GitHub (or fork it). There is no install, no agent integration, no API. The "engineering" is curation discipline + link hygiene, which is exactly why criterion (c) lands at MODERATE (§5).

## 5. Phase 0.9 verdict — GOAL-ALIGNED INCLUDE 3/4

- **(a) FAIL.** The author is **`owainlewis` (Owain Lewis), an individual developer** — not Anthropic, not an org, and not any of the vault's six cultural-peer (a)-axes (VN/Asian solo-dev, Tiếng Việt, vi-VN i18n, VN/Asian community-org, VN/Asian founder-anchor, recognized-cultural-cluster). The only major-vendor (a) carve-out, **(a)-7 "Foundational-Vendor-Direct-Source," is Anthropic-only.** The name "Owain" (Welsh) is a *heritage inference*, and per the v151 / v160→v169 discipline a name/heritage inference is **NOT** an (a)-rescue. **(a) FAILs cleanly; no rescue, no axis minted** — consistent with v168 ponytail (bare-handle FAIL) and v169 SkillSpector (corporate-not-Anthropic FAIL). It doesn't need a rescue — it is goal-aligned through (b).
- **(b) MODERATE.** Goal #1 = *"master Claude and autonomous agents for software development."* This is a curated **AI-engineering field-map** with an unmistakable on-goal spine: Claude Code is the first coding agent listed, Anthropic's "Building Effective Agents" the first guide, Constitutional AI a listed paper, the Build → Frameworks/Evals/IDEs section is exactly the goal-domain toolchain. A practitioner pursuing goal #1 would find it immediately useful. Held at **MODERATE (not STRONG)** because (i) its breadth ranges well beyond the Claude/autonomous-agents core (11 language models, image/video/audio sets, foundational deep-learning + RL theory), (ii) it is a *reference/orientation meta-resource*, not a tool you operate or the substrate itself, and (iii) it is broader than awesome-claude-skills v50, which was only MODERATE-to-STRONG → this should sit at or below that. **⚠️ Operator-reviewable:** a STRONG call is defensible if the list is weighted as a *foundational upstream reference* (it is arguably where the wild patterns the vault reports on first surface). Either way → GOAL-ALIGNED (§31 keys on (b) MODERATE+).
- **(c) MODERATE.** Strong **curation** maturity — opinionated editorial discipline, "actively maintained" hygiene (link-checker tooling), large + durable readership (page-stated ≈14.6k★ / ≈2.3k forks, §7), one of the longer-lived awesome-AI lists. But the *engineered surface is minimal* — it is curated links + a link-checker, with no novel aggregation mechanism, semantic analysis, or decision-support tooling. STRONG-for-the-genre, MODERATE against an engineering-rigor bar; recorded as **MODERATE**.
- **(d) STRONG.** A **clean instance of the CONFIRMED Pattern #68** (Awesome-List-Genre Meta-Pattern) — the established home — plus several scoped secondary observations (§6). No forcing required; the pattern connection is unambiguous.

**Tier (2-tier INCLUDE, routine v2.5 §31):** (b) is **MODERATE** (MODERATE+) → **GOAL-ALIGNED INCLUDE**, full stop. (a)'s FAIL does **not** affect the tier — off-goal capture is defined by `(b) FAIL`, which does not apply here. *(This is the v169 cascade error guarded against explicitly: the build workflow's critic confirmed (b), not (a), keys the tier.)*

## 6. Pattern Library outcome — Pattern #68 instance-strengthening (NO mint)

**PRIMARY — Pattern #68 "Awesome-List-Genre Meta-Pattern" (CONFIRMED, promoted at the v31 mini-audit). v170 is a clean new instance.**

- Pattern #68 was promoted **N=3** at v31 across three OUTSIDE-SCOPE *audience* sub-types: **(a)** human-directed learning = build-your-own-x v8 · **(b)** AI-content-input = awesome-design-md v25 · **(c)** AI-runtime-infrastructure directory = awesome-mcp-servers v31. awesome-claude-skills **v50** was a subsequent instance (sub-type c, hybrid). **v170 is the next catalogued instance** (v8 / v25 / v31 / v50 / **v170**); the exact running N is audit-maintained.
- **What v170 adds (the distinguishing observation):** it is the corpus's first **broad, opinionated AI-engineering practitioner field-map** — spanning learn + build + agents + models rather than a single vertical. This is best read as a **hybrid of audience sub-type (a) human-directed-learning + (c) tooling-directory**, at field-map breadth. A new audience sub-type label *"(d) general-AI-engineering-field-map"* was proposed during the build; per §28 anti-inflation it is **recorded as an observation and deferred to the next audit**, NOT confidently minted (whether a new sub-type increments #68's N or is organizational-only is exactly the kind of counting question an audit settles — not a ship-time mint).

**SECONDARY observations (NOT minted):**

- **Opinionated / exclusionary curation philosophy** ("must-use, actively maintained" + anti-bloat) — a within-pattern refinement of curation-intensity, distinct from the inclusive community-PR-intake of v8/v25/v31. Observation, not a new pattern (curation-intensity has never been escalated to top-level).
- **Pattern #78 (Living-Domain-Standards Tracking) — CROSS-REFERENCE, NOT an instance.** The list has *pivoted over its lifetime* from classical-AI-education to AI-engineering/agents — but that is the **curator's selection-criteria evolution**, not the list documenting a versioned/deprecation-aware standard. #78 requires the subject to *track a living standard with discipline*; an awesome-list that drifts with the field does not qualify. Recorded as a cross-reference only.
- **Claude-Code-first / Anthropic-guide-first ordering** — a curation bias that places the on-goal center of gravity at the top. Reinforces (b); not a structural pattern.
- **Pattern #22 (AGENTS.md-absence across the awesome-list genre)** — consistent: a curated README has no AGENTS.md. Already within #22's scope; noted, not re-minted.

**Explicit NON-claims:**

- **NOT a new top-level pattern.** Max confirmed stays **#85**; the curated-list shape is fully captured by the CONFIRMED Pattern #68. (Same anti-inflation discipline that rejected the over-reaching #86/#88 proposals at v168.)
- **NOT Pattern #52 (viral velocity).** Page-stated ≈14.6k★ / ≈2.3k forks / **0 releases** are NOT API-verified (§37.4) and **no creation date is shown** on the rendered page → velocity is unestablishable → not a #52 claim. (The ~2015 origin is corpus-lore inference, not page-verified.)
- **NOT Pattern #57 (corpus-recursion).** The list *mentions* Claude Code as one of 17 coding agents, but it does not cite, recurse, or use the Storm Bear vault corpus as source material. Mentions ≠ recursion. (And it lacks the high-density aggregator-mediated multi-citation structure that v50 awesome-claude-skills had.)
- **NOT a new Library-vocab item.** Awesome-lists are a confirmed Pattern #68 archetype; this is instance-strengthening, not a new semantic dimension.

**Counts UNCHANGED: 46 confirmed top-level patterns / 10 CONFIRMED Library-vocab.** Tracked PROVISIONAL surface unchanged (no new §C standalone — this files into #68).

## 7. §37 provenance

- **Page-stated, NOT API-verified (§37.4):** ≈**14.6k★ / ≈2.3k forks / 668 watchers / 0 published releases** *(as of 2026-06-20 page render, github.com/owainlewis/awesome-artificial-intelligence — confidence: stated, NOT API-verified)*. MIT license. Primary-language tag: Python (the link-checker tooling; the content is Markdown). Owner = individual `owainlewis`.
- **No creation date shown** on the rendered repo → age & velocity **unestablishable** → **explicitly NOT a Pattern #52 claim.** The frequently-cited ~2015 origin is *corpus-lore / inference* — confidence: speculation, NOT page-verified.
- **Author identity:** "Owain Lewis" is inferred from the GitHub username — confidence: stated-at-GitHub, NOT independently verified. The (a) FAIL does not depend on the exact identity (an individual non-Anthropic author FAILs (a) regardless).
- **README contents** (§2) are page-verified from the rendered README at ship time; the curated *targets* (Claude Code, LangGraph, etc.) are link references, not claims about those projects.

## 8. Streak / state

- **Streak:** `GA:31 · OG:11 [7 ov]` → **`GA:32 · OG:11 [7 ov]`** (32nd GOAL-ALIGNED PASS; NOT an override; historical "49+3\*" frozen @v125).
- **§35 ceiling:** rolling-3-ship window {v168 GA, v169 GA, **v170 GA**} = **0 OG → STAYS CLEAR.** No ceiling-override needed or taken.
- **17 consecutive goal-aligned ships v153→v170.** v168 (code-minimalism) + v169 (defensive-security) + v170 (AI-engineering field-map) are three consecutive ships that broaden the corpus *off* the v153→v166 operating/monitoring niche.
- **Counts:** 46 confirmed patterns / 10 CONFIRMED Library-vocab **UNCHANGED.** Max pattern #85.
- **Override-frequency triggers (2-in-20 / 3-in-30):** v153→v170 = **zero** operator overrides (clean).

## 9. Pilot note

This subject is **not "pilotable" in the tooling sense** — it is a curated reading/tooling list, not software you install and run (unlike v168 ponytail or v169 SkillSpector). Its direct value to goal #1 is as a **vetted reading/orientation map**: the Build → Guides (Anthropic's "Building Effective Agents"), the Frameworks shortlist (LangGraph/Pydantic-AI/CrewAI/AutoGen), the Evals pointer (OpenAI Evals), and the Landmark Papers (incl. Constitutional AI) are a sensible study path for the vault's goal.

- **The PILOT lever still stands** (zero of the catalogued operating-niche subjects piloted; v170 does not discharge it because it is a reference, not a tool). The strongest *pilotable* on-goal candidates remain **v169 SkillSpector** (read-only `--no-llm` scan of the vault's own `05 Skills/` — lowest risk) and **v168 ponytail** (cuts the vault's own token spend; installs hooks → `install-snapshot` first).
- **The "vary the domain" lever is now triply discharged** (v168 / v169 / v170 are three distinct non-niche domains).

## Suggested next action

Commit the v170 ship on `wiki/v170-awesome-ai` (don't merge — operator reviews + merges; note the branch is based on v169/`8def4ba`, which is itself unmerged). Then, the highest-value open move is still the **standing PILOT lever**: run **SkillSpector `--no-llm` over the vault's own `05 Skills/`** (read-only, free, on-goal, lowest-risk). Optionally, mine this list directly for goal #1 by reading the **Build → Guides** entries (Anthropic "Building Effective Agents" first) as a study path.
