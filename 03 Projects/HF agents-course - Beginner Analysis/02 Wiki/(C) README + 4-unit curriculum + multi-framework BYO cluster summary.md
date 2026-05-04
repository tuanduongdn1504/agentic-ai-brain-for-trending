# (C) README + 4-Unit Curriculum + Multi-Framework BYO Cluster Summary

> **Cluster:** Course structure + multi-framework teaching + HF Learn platform
> **Parent:** [[(C) index]]
> **Sources:** README + hf.co/learn/agents-course
> **Status:** ✅ Phase 2 cluster summary

---

## 1. Cluster scope

3 related signals:
1. **4-unit + bonus curriculum** structure
2. **3-framework BYO teaching** (smolagents + LangGraph + LlamaIndex)
3. **HF Learn platform** hosting (first in corpus)

## 2. Course structure

### 4 primary units + bonus

| Unit | Focus (inferred from topics + framework list) |
|------|-----------------------------------------------|
| Unit 1 | Agent fundamentals + concepts |
| Unit 2 | smolagents framework (+ Bonus: observability + evaluation) |
| Unit 3 | LangGraph / LlamaIndex / multi-framework |
| Unit 4 | Automated evaluation + leaderboard + student projects |

### Prerequisites

- Basic Python
- Basic LLMs

**Low barrier to entry** — accessible to developers without deep ML background.

### Certification model

**No formal credential.** Instead:
- Unit 4 features automated evaluation of student agents
- Leaderboard with peer comparison
- Completion tracking via HF Learn platform

**Informal-but-gamified** completion model.

## 3. Multi-framework BYO teaching

### 3 frameworks covered

| Framework | Origin | Role |
|-----------|--------|------|
| **smolagents** | HuggingFace (owned) | "Lightweight framework for creating capable AI agents" |
| **LangGraph** | LangChain | Graph-based agent workflows |
| **LlamaIndex** | LlamaIndex org | RAG + data connectors |

### BYO curriculum philosophy

**HF course teaches its own framework (smolagents) alongside competitors** (LangGraph + LlamaIndex). This is:
- **Ecosystem-thinking** — acknowledge ecosystem diversity
- **Competitive-confidence** — teach competitors, trust own merits
- **Learner-service** — give students tool choice

### Contrast with Microsoft v6

v6 Microsoft ai-agents-for-beginners taught:
- Microsoft Agent Framework (primary)
- Azure ecosystem integration
- Semantic Kernel
- **Single-platform-focused curriculum** (Microsoft-owned tools)

**HF v26 = multi-framework BYO; Microsoft v6 = single-platform.** Distinct pedagogical approaches.

## 4. Pattern #53 candidate — Multi-Framework BYO Curriculum

### Registration

> **Pattern #53 Multi-Framework BYO Curriculum (CANDIDATE N=1):** T3 Agent-as-education frameworks take divergent curriculum philosophies — single-platform focused (teaches one framework's tools) vs multi-framework BYO (teaches ecosystem diversity including competitors). Philosophical choice between "teach the one true way" and "empower ecosystem navigation." Observed at T3 N=2 (Microsoft v6 single-platform; HuggingFace v26 multi-framework).

### Evidence

- **Microsoft v6:** single-platform (Microsoft Agent Framework + Azure)
- **HuggingFace v26:** multi-framework BYO (smolagents + LangGraph + LlamaIndex)

### Validation path

Watch T3 at N=3+ — does 3rd course go single-platform or multi-framework? Pattern may generalize beyond T3 (Pattern #28 Multi-Provider AI Support confirmed v25 audit is framework-level analog).

### Relation to Pattern #28

Pattern #28 Multi-Provider AI Support (confirmed v25 audit) observes framework-level multi-provider patterns (LiteLLM abstraction + multica/Skyvern native BYO). Pattern #53 observes curriculum-level analog.

**Possible generalization at higher N:** "Multi-vendor coverage" as corpus-wide phenomenon spanning frameworks + curricula.

## 5. HF Learn platform hosting

### hf.co/learn/agents-course

First corpus wiki with **hosted learning platform** (not GitHub-only).

### Platform features (inferred)

- Registration at bit.ly/hf-learn-agents
- Progress tracking
- Automated evaluation
- Leaderboard
- Linked to HF Hub (model uploads, Spaces demos)

### GitHub role

GitHub repo (`huggingface/agents-course`) hosts:
- Course materials (MDX — markdown with JSX)
- Contribution pipeline
- Issue tracking
- Reference code

**GitHub = source; HF Learn = delivery.**

### Contrast with v6 Microsoft

v6 Microsoft ai-agents-for-beginners = **GitHub-only** (lessons in repo, no separate learning platform).

**HF v26 introduces hosted-platform variant to T3 taxonomy.**

## 6. Platform comparison with corpus wikis

| Framework | Platform type | Corpus wiki |
|-----------|---------------|-------------|
| Microsoft ai-agents-for-beginners | GitHub-only | v6 |
| **HF agents-course** | **HF Learn + GitHub** | **v26** |
| Skyvern | pip/Docker/Skyvern Cloud | v24 |
| awesome-design-md | GitHub + getdesign.md | v25 |
| Most T1/T4/T5 | GitHub + installer | various |

**HF Learn platform = distinct T3 delivery model.** Analog: Coursera / Udemy / edX (but HF's is free).

## 7. Topics + scope coverage

### GitHub topics

`agentic-ai / agents / course / huggingface / langchain / llamaindex / smolagents`

### Implied scope

- Agent fundamentals
- Multi-framework hands-on
- Evaluation + observability
- Production considerations (Unit 2 Bonus)
- Leaderboard competition (Unit 4)

### Not explicitly covered (inferred gaps)

- Deep reinforcement learning for agents (different HF course)
- Specific vertical applications (medical / legal / financial)
- Formal correctness / safety engineering

## 8. Key observations

### Cluster-level

- **4-unit + bonus** = compact curriculum (vs v6 Microsoft 10+4+4 expansive)
- **3-framework BYO** = ecosystem-thinking teaching philosophy
- **HF Learn hosted platform** = first hosted delivery in corpus
- **smolagents integration** = HF promotes own framework while teaching competitors

### Cross-corpus

- **T3 closure at N=2** — 5/5 tier validation milestone
- **Pattern #53 candidate** (Multi-Framework BYO Curriculum) — new registration
- **Pattern #28 Multi-Provider AI Support confirmed** — analog at curriculum level
- **First hosted-platform T3** — delivery model diversifies

## 9. References

- Parent: [[(C) index]]
- Source: README + hf.co/learn/agents-course (platform hosted)
- Sibling clusters: [[(C) HuggingFace ecosystem + commercial-platform org cluster summary]] + [[(C) Named-instructors + leaderboard + Discord community cluster summary]]
- T3 peer: ai-agents-for-beginners v6
- Pattern #28 Multi-Provider AI Support confirmed v25 audit — framework-level analog

---

**Cluster summary: 4-unit + bonus curriculum teaching 3 frameworks BYO (smolagents + LangGraph + LlamaIndex) with low barrier (Basic Python + Basic LLMs). HF Learn platform hosting (first hosted-platform in corpus) + GitHub materials. Leaderboard certification model (Unit 4 automated evaluation). Pattern #53 candidate (Multi-Framework BYO Curriculum) registered; analog to confirmed Pattern #28 at framework level.**
