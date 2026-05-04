# (C) 4-Unit Curriculum + Multi-Framework BYO Teaching

> **Type:** Entity — core curriculum methodology
> **Parent:** [[(C) index]]
> **Sources:** README + HF Learn platform
> **Status:** ✅ Phase 3 entity page

---

## 1. Summary

HF agents-course = **4 units + bonus** teaching **3 frameworks BYO** (smolagents + LangGraph + LlamaIndex). Low barrier (Basic Python + LLMs). Hosted at HF Learn platform + GitHub materials. Leaderboard certification (Unit 4 automated evaluation). **Multi-framework BYO curriculum philosophy** distinct from v6 Microsoft single-platform approach — registers Pattern #53 candidate.

## 2. Curriculum structure

### 4 units + bonus

| Unit | Focus |
|------|-------|
| Unit 1 | Agent fundamentals + concepts |
| Unit 2 | smolagents framework (+ Bonus: observability + evaluation) |
| Unit 3 | LangGraph / LlamaIndex / multi-framework |
| Unit 4 | Automated evaluation + leaderboard + student projects |

### Prerequisites

- **Basic Python** — functions, classes, async basics
- **Basic LLMs** — what LLMs are, API usage

**Low barrier intentional.** Accessible to developers without ML background.

### Time commitment

Not explicitly stated. Comparable HF courses (Deep RL, NLP) typically 20-40 hours. Inferred ~15-25 hours for agents-course (4 units).

## 3. Multi-framework BYO teaching

### 3 frameworks

| Framework | Owner | Focus | Positioning |
|-----------|-------|-------|-------------|
| **smolagents** | HuggingFace | "Lightweight framework for creating capable AI agents" | HF's answer to LangChain/LlamaIndex |
| **LangGraph** | LangChain | Graph-based agent workflows | LangChain's stateful agents |
| **LlamaIndex** | LlamaIndex org | RAG + data connectors | Data-heavy agent context |

### BYO curriculum philosophy

**HF teaches its own framework (smolagents) alongside competitors.** Philosophical statement:
- Ecosystem-thinking (don't dominate; enable)
- Competitive confidence (trust smolagents on merits)
- Learner-service (give students tool choice)

### smolagents deep-dive at Unit 2

Unit 2 focuses on smolagents with observability + evaluation bonus. Central curriculum unit features HF's owned framework.

**Strategy:** teach smolagents thoroughly, then show competitors in Unit 3 for ecosystem literacy.

## 4. Pattern #53 candidate — Multi-Framework BYO Curriculum

### Registration

> **Pattern #53 Multi-Framework BYO Curriculum (CANDIDATE N=1 within T3):** T3 Agent-as-education frameworks take divergent curriculum philosophies — single-platform focused (teaches one framework's tools) vs multi-framework BYO (teaches ecosystem diversity including competitors). Philosophical choice between "teach the one true way" and "empower ecosystem navigation."

### Evidence (T3 N=2)

- **Microsoft v6 ai-agents-for-beginners:** single-platform (Microsoft Agent Framework + Azure; Semantic Kernel secondary)
- **HuggingFace v26 agents-course:** multi-framework BYO (smolagents + LangGraph + LlamaIndex)

### Pattern implications

- **Organizational correlation:** Microsoft as platform-owner teaches own platform; HF as ecosystem-platform teaches ecosystem diversity
- **Competitive confidence correlation:** larger platform (HF Hub dominant) teaches competitors; smaller platform (Microsoft Agent Framework) focuses own

### Related to Pattern #28 Multi-Provider AI Support (confirmed v25 audit)

Pattern #28 observes **framework-level** multi-provider support. Pattern #53 observes **curriculum-level** multi-framework teaching.

**Possible generalization:** "Multi-vendor coverage" as corpus-wide phenomenon spanning frameworks + curricula + tooling.

## 5. Comparison with Microsoft v6 curriculum

### Structure differences

| Dimension | Microsoft v6 | HuggingFace v26 |
|-----------|--------------|------------------|
| **Lesson count** | 10 + 4 + 4 Coming Soon (18 total planned) | 4 units + bonus |
| **Frameworks** | Microsoft Agent Framework + Azure + Semantic Kernel | smolagents + LangGraph + LlamaIndex |
| **Philosophy** | Single-platform teaching | Multi-framework BYO |
| **Prerequisites** | Python + LLMs basics | Python + LLMs basics (same) |
| **Hosting** | GitHub-only | HF Learn + GitHub |
| **Structure depth** | Broader (18 lessons) | Deeper per-unit (4 units) |

### Philosophical distinction

- **Microsoft v6:** "Learn agents via Microsoft platform" — platform-owned path
- **HuggingFace v26:** "Learn agents via 3 major frameworks" — ecosystem path

Both valid pedagogically. Different org incentives.

## 6. smolagents positioning within course

### What smolagents is

HuggingFace's own agents framework, positioned as:
- **Lightweight** — minimal overhead vs LangChain/LlamaIndex
- **Capable** — production-ready
- **Integrated with HF Hub** — native model access

### Why HF teaches it prominently

- **Self-interested:** drives smolagents adoption
- **Ecosystem-thinking:** HF Hub + smolagents = native HF stack
- **Simplicity:** good entry point for students (lighter than LangChain)

### Competitive positioning

Teaching LangGraph + LlamaIndex alongside smolagents signals:
- **Honesty:** acknowledges competitors are strong
- **Confidence:** smolagents can stand on merits
- **Breadth:** students graduate with ecosystem literacy

## 7. Observability + evaluation (Unit 2 Bonus)

### Content

Unit 2 Bonus covers:
- Observability practices (tracing, logging agent steps)
- Evaluation methods (measuring agent performance)

### Significance

**Production-oriented.** Not just "build agents" but "measure + monitor agents." Reflects industry maturity — agents moving from demo to production.

### Tools likely covered

Common observability tools:
- **LangSmith** (LangChain's)
- **Weights & Biases**
- **Langfuse**
- **Arize Phoenix**

(Specifics not confirmed from README-level analysis.)

## 8. Leaderboard evaluation (Unit 4)

### How it works

- Students build agents for Unit 4 projects
- Automated evaluation runs against benchmark tasks
- Leaderboard displays rankings
- Peer comparison drives engagement

### Pattern #8 data point

Leaderboard = form of research-benchmark integration (Pattern #8, 8 data points post-v26).

### Gamification effect

Ranking-based motivation:
- Higher engagement than completion certificates
- Public portfolio evidence
- Cross-student collaboration (top ranks become community helpers)

## 9. Pedagogical approach inferred

### Teaching style (from HF courses tradition)

HF courses (Deep RL, NLP, agents) historically:
- **Hands-on code-heavy** — Jupyter notebooks / code examples primary
- **Minimal lecture** — compared to theory-heavy academic courses
- **Project-driven** — build real things, not just read
- **Community-integrated** — Discord + Hub + Spaces for learner interaction

### Likely agents-course pedagogy

- Code examples for each framework
- Hands-on agent builds per unit
- Integration with HF Hub (upload models, run Spaces)
- Discord for Q&A
- Leaderboard for capstone

## 10. Edges + limitations

### Course limitations

- **English-only** — no i18n (same gap as v6 Microsoft)
- **Fast-moving field** — agent frameworks evolve; course content may age
- **Prerequisites assumed** — basic Python + LLMs not absolute-beginner
- **No formal certification** — leaderboard not transferable credential

### Multi-framework BYO challenges

- **Cognitive load** — learning 3 frameworks = more complex than 1
- **Fragmentation** — students may master none deeply
- **Framework drift** — LangGraph/LlamaIndex may change; HF needs to keep content fresh

## 11. Related concepts

- [[(C) HuggingFace Commercial-Ecosystem + Pattern 17 Strengthening]]
- [[(C) Named-Instructor Team + Leaderboard Certification]]
- [[(C) T3 Closure at N=2 + 5-of-5 Tier Validation Milestone + Storm Bear]]
- T3 peer: ai-agents-for-beginners v6 (single-platform curriculum contrast)
- Pattern #28 Multi-Provider AI Support (confirmed v25 audit) — framework-level analog
- Pattern #53 candidate (new at v26)
- Parent: [[(C) index]]

## References

- README + hf.co/learn/agents-course
- smolagents documentation
- LangGraph documentation
- LlamaIndex documentation

---

**4 units + bonus curriculum teaching 3 frameworks BYO (smolagents + LangGraph + LlamaIndex). HF teaches own framework prominently (Unit 2) alongside competitors (Unit 3). Multi-framework BYO pedagogy distinct from v6 Microsoft single-platform approach. Pattern #53 candidate (Multi-Framework BYO Curriculum) registered at N=1 within T3 N=2. Prerequisites: Basic Python + LLMs. Leaderboard certification (Unit 4 automated eval).**
