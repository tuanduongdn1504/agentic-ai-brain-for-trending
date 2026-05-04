# (C) autoresearch — Hướng dẫn cho người mới

> Target audience: ML practitioners, Vietnamese ML researchers, agent enthusiasts curious về autonomous research automation
> Reading time: ~30 min
> Language: Bilingual (VN primary, EN technical terms)
> Source: `karpathy/autoresearch` (74K stars, Andrej Karpathy)

---

## Part 1 — autoresearch là gì?

### 1.1 Giới thiệu 1 phút

**autoresearch = Karpathy's autonomous ML research framework.** AI agents overnight optimize nanochat (GPT-style chatbot) training trên single GPU. **~100 experiments/night.** Minimal: 5 Python files + Markdown instructions. **74K stars** — Karpathy's star power amplifies reach.

**Workflow:**
1. Agent reads `program.md` (instructions Markdown)
2. Agent modifies `train.py` (experimental hypothesis)
3. Agent commits (git)
4. Agent runs 5-min training
5. Agent evaluates val_bpb (metric)
6. Agent keeps if better, reverts if worse
7. Agent logs to `results.tsv`
8. **Repeat indefinitely until human stops**

**Key concept:** **program.md = agent skill** — human-written instructions, iteratively refined based on agent performance.

### 1.2 Positioning trong Storm Bear corpus

**Tier 5 "Agent-as-application" — entrant #2** (second in tier after deer-flow v9).

| Tier | Frameworks (n=10) |
|------|-------------------|
| T1: Agent-as-assistant | ECC, Superpowers, gstack, GSD |
| T2: Agent-as-service | goclaw |
| T3: Agent-as-education | course |
| T4: Agent-as-bridge | notebooklm-py |
| **T5: Agent-as-application** | **deer-flow + autoresearch (MULTI-ENTRANT VALIDATED!)** |
| Outside scope | build-your-own-x |

→ **T5 tier validated** với 2 entrants. First multi-entrant validation after T1 (done in v5 GSD).

### 1.3 Ai nên quan tâm?

**Rất phù hợp:**
- ML researcher curious về research automation
- Computer science student learning autonomous AI
- Karpathy fans (74K stars = his audience)
- Agentic AI enthusiasts
- Anyone interested trong "AI does research overnight" concept

**Ít phù hợp:**
- Non-ML developers (framework very ML-specific)
- Researchers needing production-grade multi-GPU (autoresearch single-GPU only)
- People needing quantitative results (framework, not published findings)

**Mix phù hợp:**
- Scrum coach who wants understanding meta-pattern (agents iterating)
- Anyone building agent skills (program.md = reference pattern)

---

## Part 2 — Meta-relevance to Storm Bear vault

### 2.1 **Karpathy = author of LLM Wiki pattern Storm Bear is built on**

Storm Bear root CLAUDE.md:
> "building a persistent, compounding knowledge base following Karpathy's LLM Wiki pattern"

**autoresearch is Karpathy's OTHER meta-pattern:**
- **LLM Wiki pattern:** Agents maintain wikis iteratively
- **autoresearch:** Agents iterate research

**Same meta-structure, different domain.** Storm Bear inherits.

### 2.2 program.md ≈ Storm Bear routine

| Element | autoresearch | Storm Bear |
|---------|--------------|------------|
| Skill file | `program.md` (Markdown) | `llm-wiki-routine.md` (Markdown) |
| Orchestrates | Autonomous ML research loop | LLM Wiki 7-phase build |
| Human refines | Between runs (nightly) | Between wikis (action items) |
| Metric-driven | val_bpb keep/revert | 13-section format compliance |
| Artifact | Git commits + results.tsv | Obsidian wiki files |

**Direct lineage.** Storm Bear = Karpathy's pattern applied to knowledge work.

### 2.3 Why this matters emotionally/intellectually

Cvtot + Claude thinking about AI-agent-driven knowledge work = building on Karpathy's shoulders. autoresearch wiki = recognizing that explicitly.

**10-wiki corpus touches its own source.** Meta-cycle complete.

---

## Part 3 — 5 core concepts

### 3.1 program.md as agent skill

Markdown file containing agent instructions. Refined by human iteratively.

**Key sections:**
- Objective (what to optimize)
- Capabilities (what agent can do)
- Workflow (how to iterate)
- Constraints (what's off-limits)

### 3.2 5-minute experiment loop

Fixed wall-clock budget. ~100 experiments/night. Enables:
- Fairness (same budget)
- Comparability (same metric)
- Velocity (100x human)

### 3.3 val_bpb metric

Validation bits-per-byte. Vocabulary-size-independent. Information-theoretic. Lower = better.

Solves: fair comparison across architectural variations với different vocab sizes.

### 3.4 Git-based experiment tracking

- Each hypothesis = commit
- Each failure = revert
- Each campaign = branch (e.g., `autoresearch/mar5`)
- History = lineage of thinking

### 3.5 prepare.py / train.py / analysis.ipynb separation

| File | Role | Agent access |
|------|------|--------------|
| prepare.py | Data + tokenizer | Read-only |
| train.py | Experimental surface | **Full modify** |
| analysis.ipynb | Human tool | Read-only |

**Clear trust boundary.**

---

## Part 4 — Cài đặt và thử

### 4.1 Prerequisites

- **Single NVIDIA GPU** (H100 tested; smaller GPUs require config changes)
- **Python 3.10+**
- **uv package manager** (Karpathy's preferred)
- **CUDA toolkit**
- Moderate ML knowledge

### 4.2 Install

```bash
git clone https://github.com/karpathy/autoresearch.git
cd autoresearch

uv sync          # install deps
uv run prepare.py  # one-time data + tokenizer prep
```

### 4.3 First experiment (human-driven, not agent)

```bash
uv run train.py  # runs with default config
# Outputs val_bpb metric; baseline = starting point
```

### 4.4 Agent-driven (simulation)

autoresearch expects agent like Claude Code or Codex integration:
- Claude Code reads program.md
- Claude Code modifies train.py
- Human triggers experiment runs
- Claude Code logs results
- Loop iterates

**In practice:** Install Claude Code, open autoresearch repo, tell Claude Code: "follow program.md to optimize val_bpb."

### 4.5 Smaller GPU adaptation

README provides guidance:
- Reduce depth: 8 → 4 layers
- Use TinyStories dataset (smaller)
- Decrease sequence length: 1024 → 256
- Lower batch: 2^14 tokens

---

## Part 5 — So sánh với deer-flow (T5 peer)

Direct comparison — both T5 "Agent-as-application" tier.

### 5.1 2-way comparison matrix

| Axis | deer-flow | autoresearch |
|------|-----------|--------------|
| **Purpose** | General autonomous harness | ML research specialist |
| **Domain** | Any task | ML model optimization |
| **Task duration** | Minutes-hours | Overnight continuous |
| **Form factor** | Full-stack app | Python scripts + Jupyter |
| **Lines of code** | Thousands | ~50 KB total |
| **Services** | 4 (Nginx + Frontend + Gateway + LangGraph) | 1 (Python process + GPU) |
| **User interaction** | Web UI + IM + API | CLI + Jupyter |
| **Author** | ByteDance (corporate) | Karpathy (solo research) |
| **Stars** | 62K | 74K |
| **Complexity** | High | Low |
| **Deployment** | Docker + Nginx + Node | Single `uv run` |
| **Agent library** | Public + custom progressive | Single program.md |
| **Metric** | Task completion (subjective) | val_bpb (objective) |
| **Iteration count** | 1 task = 1 run | 100+ experiments/campaign |
| **Target audience** | Team / Production | ML researcher / learner |

### 5.2 Complementary, not competitive

- **deer-flow:** better for diverse long-horizon tasks
- **autoresearch:** better for structured iteration in narrow domain

**Together:** different tools for different needs within T5 tier.

### 5.3 T5 subcategorization hypothesis

N=2 validated T5 multi-entrant. Observable diversity suggests future subcategories:
- **T5a: General harness** (deer-flow, OpenHands, AutoGPT)
- **T5b: Specialized iteration** (autoresearch, domain-specific research tools)

At N=3+ should formalize.

---

## Part 6 — Storm Bear vault synergy

### 6.1 Routine v2 lessons from autoresearch

**Directly portable:**

1. **Git-branch-per-campaign** — `autoresearch/mar5` convention. Storm Bear could do `wiki/v10-autoresearch-build`.

2. **Results.tsv** — structured metric log. Storm Bear iteration logs could add structured metrics section.

3. **Keep/revert discipline** — if routine v2 change lowers quality, revert. Requires Storm Bear quality metric (v11 work?).

4. **Fixed budget enforcement** — ~2h per wiki becomes hard budget, not soft guideline.

### 6.2 Conceptually inspiring

**autoresearch = Karpathy demonstrating what's possible** when agent + skill + metric + budget align.

Storm Bear could aspire to similar discipline:
- Agent (Claude) maintains vault
- Skill (routine v2) orchestrates phases
- Metric (quality score) guides keep/revert
- Budget (2h per wiki) enforces fairness

**Future Storm Bear v2.0** could adopt this pattern fully.

### 6.3 Cvtot's Scrum coaching meta-application

Imagine: Scrum coach automation via autoresearch-style pattern:
- **Agent:** Claude Code
- **Skill:** `scrum-coach-skill.md` (retro synthesis, team health, action item extraction)
- **Workflow:** Weekly auto-run on team metrics
- **Metric:** Team health score over time
- **Iteration:** Adjust skill based on delivery outcomes

**Not in autoresearch directly, but the pattern is reusable.**

---

## Part 7 — Lộ trình 1-tuần (exploration)

Minimal exploration, not production deployment.

### Day 1-2: Understanding
- Clone autoresearch, read README + program.md verbatim
- Understand 5 files' roles
- Run prepare.py + 1 baseline train.py

### Day 3-4: Setup agent
- Open autoresearch in Claude Code
- Ask Claude Code to "follow program.md and optimize val_bpb"
- Observe 3-5 experiments
- Read commit history + results.tsv

### Day 5-6: Iteration
- Review agent's choices
- Edit program.md với new directive (e.g., "try different attention patterns")
- Observe 3-5 more experiments
- Compare metric improvement

### Day 7: Synthesis
- Write personal iteration log
- Map findings to Storm Bear routine v2 ideas
- Decide: deeper investment OR revert to Storm Bear main work?

---

## Part 8 — Rủi ro + Watchouts

### 8.1 Cost

- GPU time: H100 ~$2-5/hour cloud, 12 hours/night = $24-60/night
- LLM agent calls: Claude Code subscription or per-call pricing
- **Budget $100-200 for 1 week exploration realistic**

### 8.2 Safety

Agent modifies Python code + executes. Risks:
- Infinite loop crashes
- OOM crashes
- Network calls (agent shouldn't need internet)
- Filesystem writes outside sandbox

**Mitigation:** Run in isolated environment (Docker or VM).

### 8.3 Reproducibility

Training non-deterministic. 2 runs same config → different val_bpb. Noise interpretation challenge.

### 8.4 Karpathy's future

Experimental repo. Karpathy may pivot or deprecate. Don't build production pipeline on this.

### 8.5 Metric gaming risk

Agent learns to game val_bpb without real improvement. Monitor for suspicious patterns (e.g., val set leak).

---

## Part 9 — Tiếp theo / Next steps

### 9.1 For ML researcher

- Install + run 1-week exploration (above roadmap)
- Compare to your own manual research velocity
- Decide: adopt pattern for your research?

### 9.2 For Storm Bear vault operator (Cvtot)

- Reflect on Karpathy lineage (root CLAUDE.md already credits)
- Consider routine v2 adopting autoresearch patterns:
  - Fixed budget enforcement
  - Keep/revert với quality metric (requires defining metric first)
  - Structured results.tsv per wiki
  - Branch-per-campaign workflow

### 9.3 For agentic AI enthusiast

- Study program.md as skill-file reference
- Compare với deer-flow skills library
- Design your own autonomous agent application

### 9.4 Contribution opportunities

- VN translation of README (PR to upstream)
- Adaptation guide cho consumer GPUs (4090, etc.)
- Benchmark different agents (Claude vs Codex vs others)
- Document discovered architectural insights (findings collection)

---

## Tóm tắt / Summary

**autoresearch = Karpathy's autonomous ML research framework.** AI agents overnight iterate train.py to minimize val_bpb. **5-min budget per experiment, ~100/night.** 5-file minimal codebase.

**Tier 5 entrant #2 — validates "Agent-as-application" tier.**

**PEAK meta-relevance cho Storm Bear vault** — Karpathy authored the LLM Wiki pattern Storm Bear is built on. This wiki = recognition of intellectual lineage.

**Pattern lessons:**
- Markdown agent skills (program.md)
- Keep/revert với metric
- Fixed budget enforcement
- Git-based iteration tracking

**Complementary với deer-flow (T5 peer):**
- deer-flow = general autonomous harness
- autoresearch = specialized research iteration

**Storm Bear future:** Routine v2 could adopt autoresearch patterns. Honor the lineage.

---

## Cross-references

- Main vault: `../../../CLAUDE.md`
- Goals: `../../../GOALS.md`
- Routine: `../../../05 Skills/llm-wiki-routine.md`
- Wiki entities this project:
  - [[../02 Wiki/(C) Program.md as Agent Skill]]
  - [[../02 Wiki/(C) 5-Minute Experiment Loop]]
  - [[../02 Wiki/(C) val_bpb Metric + Evaluation Fairness]]
  - [[../02 Wiki/(C) Karpathy's Meta-contribution to Storm Bear]]
- T5 peer: `../../deer-flow - Beginner Analysis/`
- Taxonomy v4 (5-tier): `../../deer-flow - Beginner Analysis/03 Published/(C) Agent framework taxonomy v4 - 5 tier with application.md`
- Phase 4b (this wiki): [[(C) T5 2-way comparison + Karpathy meta-reflection]]
