# (C) AI Agents for Beginners — Hướng dẫn cho người mới

> Target audience: Developers Việt muốn học AI Agents fundamentals trước khi adopt tool cụ thể
> Reading time: ~40 min
> Language: Bilingual (VN primary, EN technical terms preserved)
> Source: `cvtot/ai-agents-for-beginners` (fork of `microsoft/ai-agents-for-beginners`)

---

## Part 1 — Course là gì và ai nên học / What is this course

### 1.1 Giới thiệu 1 phút

**AI Agents for Beginners** là **khóa học (curriculum)** do Microsoft biên soạn, gồm:
- **10 bài học core** (lessons 01-10) — từ "AI Agent là gì" đến "deploy production"
- **4 bài continuing** (11-14) — Agentic Protocols, Context Engineering, Memory, Microsoft Agent Framework (MAF)
- **4 bài Coming Soon** — CUA, Scalable, Local, Securing

Tech stack: Azure AI Foundry, GitHub Models (free inference!), Semantic Kernel, AutoGen, Microsoft Agent Framework.

**Đặc điểm:** 50+ ngôn ngữ dịch (có tiếng Việt sẵn), Jupyter + .NET samples, MIT license, Microsoft Foundry Discord community.

### 1.2 Khác gì với các Storm Bear wiki khác?

5 wiki trước trong Storm Bear vault (ECC, Superpowers, gstack, GSD, goclaw) = **tool/framework để dùng**.
**Khóa học này = giáo trình để HIỂU.**

**Thứ tự khuyến nghị:**

```
Học khóa này (fundamentals) → Pick một Tier 1 tool → Deploy via Tier 2 (khi cần scale)
        ↓                             ↓                        ↓
   Know WHAT + WHY            Learn HOW (specific)      Ship PRODUCTION
```

### 1.3 Ai nên học?

**Rất phù hợp (strong fit):**
- Developer mới bước vào AI agents, chưa từng viết agent
- Team lead cần shared vocabulary cho team về agents
- Senior dev chuyển sang AI từ web/mobile/backend
- Bạn đã dùng ChatGPT/Claude chat nhưng chưa build agent system

**Ít phù hợp:**
- Đã build 3+ production agents với LangChain/CrewAI/AutoGen, cần deep reference
- Chỉ cần "dùng Claude Code nhanh" (→ học ECC thay)
- Chỉ cần deploy platform (→ học goclaw thay)

**Mix phù hợp:**
- Junior → Senior transition cần hệ thống hóa kiến thức

---

## Part 2 — Core concepts từ 10 lessons / Core concepts overview

### 2.1 Lesson 01 — AI Agent là gì?

**Định nghĩa:** "System enable LLMs perform actions by extending capabilities với tools + knowledge access."

**7 loại agent** (classic AI textbook taxonomy):

1. Simple Reflex (rule-based)
2. Model-Based Reflex (có world model)
3. Goal-Based (plan creation)
4. Utility-Based (preference weighting)
5. Learning (feedback-driven)
6. Hierarchical (tiered delegation)
7. Multi-Agent (cooperative)

**Insight:** Modern LLM agents thường là **hybrid** của types 3-7. Types 1-2 lỗi thời vì LLM inherently sophisticated hơn rule-based.

### 2.2 Lesson 02 — Frameworks landscape

**3 frameworks chính (Microsoft ecosystem):**

| Framework | Khi dùng |
|-----------|----------|
| **AutoGen** | Experimentation, prototyping, research |
| **Semantic Kernel** | Production enterprise apps |
| **Azure AI Agent Service** | Cloud deployment với Azure integration |

**Integration path:** "Build in SK → Deploy via Azure AI Agent Service" (Microsoft recommendation).

**Lưu ý:** Không cover LangChain/LangGraph/CrewAI (non-Microsoft). Nếu dùng Python non-Microsoft stack, cần thêm resources khác.

### 2.3 Lesson 03 — Design patterns (Space/Time/Core)

**3 design dimensions:**

- **Space** — agent kết nối người + hoạt động đa platform
- **Time** — quản lý past/present/future context
- **Core** — uncertainty + trust foundation

**3 implementation guidelines (non-negotiable):**

- **Transparency** — luôn disclose AI involvement
- **Control** — user agency, có thể override
- **Consistency** — multi-modal same persona

**Design decision matrix:** Với mỗi agent mới, answer questions per dimension + guideline → trước code.

### 2.4 Lessons 04-10 — Các pattern specific

| Lesson | Pattern | Use case |
|--------|---------|----------|
| 04 | Tool Use | Function calling, API invocation |
| 05 | Agentic RAG | Iterative retrieval loop (vs classic RAG) |
| 06 | Trustworthy | Safety, explainability |
| 07 | Planning | Task decomposition |
| 08 | Multi-Agent | Group Chat / Hand-off / Collaborative Filtering |
| 09 | Metacognition | Self-reflection, strategy adjustment |
| 10 | Production | Observability, guardrails, deployment |

**Đọc theo thứ tự** — mỗi lesson build on previous. Don't skip 04-05 (tool use + RAG = foundation cho 06-09).

### 2.5 Lessons 11-14 — Modern infrastructure

| Lesson | Topic | Why important |
|--------|-------|---------------|
| 11 | Agentic Protocols (MCP/A2A/NLWeb) | Agent ecosystem infrastructure |
| 12 | Context Engineering | 5 types + 4 failures |
| 13 | Agentic Memory | Short-term vs long-term |
| 14 | MAF | Microsoft's unified platform |

**Lesson 11 đặc biệt quan trọng** — MCP đã wide adoption (Claude Code native), A2A + NLWeb emerging.

---

## Part 3 — Các khái niệm then chốt / Key concepts

### 3.1 Agentic RAG (Lesson 05)

**Classic RAG:** retrieve → read → respond (linear)
**Agentic RAG:** plan → retrieve → assess → refine → repeat (loop)

**5-step iterative loop:**

1. Initial LLM call
2. Tool selection
3. Assessment
4. Refinement / repeat
5. Memory maintenance

**Khi dùng:** complex queries cần multi-step reasoning.
**Không dùng:** simple Q&A (classic RAG đủ rẻ hơn).

### 3.2 Multi-Agent Systems (Lesson 08)

**3 orchestration patterns:**

- **Group Chat** — agents exchange messages
- **Hand-off** — sequential delegation
- **Collaborative Filtering** — specialists contribute per dimension

**Refund process example:**
- Process-specific: customer, seller, payment, resolution, compliance (5 agents)
- General-purpose: shipping, notification, audit, security (4 agents cross-process)

→ Mixed specialists + utilities.

### 3.3 Context Engineering (Lesson 12)

**5 types context:**
1. Instructions (rules, prompts, tool descriptions)
2. Knowledge (facts, retrievals, memories)
3. Tools (APIs + feedback)
4. Conversation History (dialogue over time)
5. User Preferences (learned likes/dislikes)

**4 failure modes + fixes:**

| Failure | Issue | Fix |
|---------|-------|-----|
| Poisoning | Hallucinations cycle | Validate + quarantine |
| Distraction | History overwhelms | Summarize |
| Confusion | Too many tools | RAG for selective loading |
| Clash | Conflicting info | Prune + scratchpads |

### 3.4 Agentic Protocols (Lesson 11)

| Protocol | Connects | Status |
|----------|----------|--------|
| **MCP** | LLM ↔ tools | High adoption (Claude Code, many IDEs) |
| **A2A** | Agent ↔ agent | Emerging (Google) |
| **NLWeb** | Agent ↔ website | Newest (Microsoft) |

**Priority now:** Master MCP. Track A2A + NLWeb.

---

## Part 4 — Tech stack và setup / Tech stack

### 4.1 Required

- **Python 3.9+** hoặc **.NET 8+** (chọn 1)
- **GitHub account** — cho GitHub Models free tier
- **Azure account** (optional) — nếu muốn Azure AI Foundry examples

### 4.2 Free tier option

**GitHub Models:**
- Free inference endpoint cho OpenAI-compatible models
- Signup: github.com/marketplace/models
- Limits: rate-limited, good for learning không good cho production

### 4.3 Optional Azure setup

- **Azure AI Foundry** — full platform với Foundry Portal
- **Azure OpenAI Service** — dedicated endpoints
- **Azure AI Agent Service** — cho lesson 02 + 14

**Không bắt buộc cho learning** — GitHub Models đủ cho most lessons.

### 4.4 Repo setup

```bash
# Clone (lưu ý: large repo)
git clone https://github.com/cvtot/ai-agents-for-beginners.git
cd ai-agents-for-beginners

# Navigate to lesson
cd 01-intro-to-ai-agents

# Read README
# Open Jupyter notebook OR .NET markdown
```

**Nếu clone bị block (như build wiki này gặp phải):** dùng WebFetch raw.githubusercontent.com cho từng lesson individually.

---

## Part 5 — Unique features / Đặc trưng

### 5.1 Metacognition (Lesson 09)

**Unique concept** — rarely seen in Tier 1 siblings:

Agent tự hỏi:
- "Tôi có phải right specialist không?"
- "Approach hiện tại đang work không?"
- "Nên escalate không?"

→ **Metacognition = orchestration intelligence layer**. Advanced concept, quan trọng cho large MAS.

### 5.2 Protocol-aware (Lesson 11)

Đây là course duy nhất (trong Storm Bear corpus 6 wikis) dạy MCP/A2A/NLWeb explicitly at concept level. Tier 1 siblings USE MCP, không TEACH MCP.

### 5.3 Microsoft ecosystem integration

- Semantic Kernel
- AutoGen
- MAF (merger path)
- Azure AI Agent Service
- Azure AI Foundry

→ **Nếu bạn là team Microsoft** — course này + Azure docs = complete learning path.
→ **Nếu non-Microsoft stack** — course concepts vẫn 90% transferable, samples cần adapt.

### 5.4 Vietnamese translation

**Điểm mạnh:** Course có bản dịch tiếng Việt sẵn (trong 50+ languages folder).

**So sánh với 5 siblings:**
- ECC: không có VN
- Superpowers: không có VN
- gstack: không có VN
- GSD: không có VN (4 langs: pt-BR, zh-CN, ja-JP, ko-KR)
- goclaw: có `README.vi.md` + Zalo community
- **ai-agents-for-beginners: có VN translation** ✅

→ Course + goclaw = 2/6 projects có VN native. **Storm Bear wiki layer adds accessibility cho VN developer community.**

---

## Part 6 — So sánh với 5 siblings / Compare with 5 siblings

### 6.1 Positioning matrix

| Project | Tier | Purpose | Khi pick |
|---------|------|---------|----------|
| **ai-agents-for-beginners** | **Tier 3 (NEW)** | **Học concepts** | **Bạn mới, chưa biết agent** |
| ECC | Tier 1 | Dev tool (Claude Code) | Muốn dùng Claude Code pro |
| Superpowers | Tier 1 | Methodology + TDD | Muốn 7-stage workflow |
| gstack | Tier 1 | Specialist roles | Muốn sprint pipeline với roles |
| GSD | Tier 1 | Context rot + 14 harnesses | Muốn context management + multi-harness |
| goclaw | Tier 2 | Multi-tenant platform | Muốn deploy agent-as-service |

### 6.2 Learning path recommendations

**Path A — Developer mới 100%:**
1. AI Agents for Beginners (lessons 01-10) → 2-3 tuần
2. Pick Tier 1 tool (start ECC hoặc Superpowers) → 1-2 tuần
3. Build first project với tool → 2-4 tuần

**Path B — Senior dev cần AI fluency:**
1. AI Agents for Beginners (lessons 01-03 + 08 + 12) → 3-5 ngày
2. Pick Tier 1 tool based on workflow fit → 1 tuần
3. Advanced lessons (09 metacognition + 10 production) → as needed

**Path C — Team lead cần train team:**
1. Team reads lessons 01-05 together → 1 tuần
2. Standardize on 1 Tier 1 tool cho team → decide
3. Lead handles lesson 10 (production) separately

### 6.3 Không dùng path song song

**Tránh:** học ECC + Superpowers + gstack + GSD cùng lúc. Mỗi Tier 1 = 1-2 tuần deep focus. Pick one, master, rồi evaluate others.

---

## Part 7 — Lộ trình 4 tuần / 4-week roadmap

### Week 1 — Foundation

- Day 1-2: Lesson 01 (Intro + 7 types) + Lesson 02 (Frameworks)
- Day 3-4: Lesson 03 (Design Patterns Space/Time/Core)
- Day 5-7: Lesson 04 (Tool Use) + run Jupyter sample

**Deliverable:** Hiểu "AI Agent là gì", có thể explain 7 types + 3 design dimensions.

### Week 2 — Patterns

- Day 8-10: Lesson 05 (Agentic RAG)
- Day 11-12: Lesson 06 (Trustworthy) + Lesson 07 (Planning)
- Day 13-14: Lesson 08 (Multi-Agent)

**Deliverable:** Can design multi-agent system với orchestration pattern choice + RAG strategy.

### Week 3 — Advanced + Infrastructure

- Day 15-16: Lesson 09 (Metacognition)
- Day 17-18: Lesson 10 (Production)
- Day 19-21: Lesson 11 (Protocols MCP/A2A/NLWeb) + Lesson 12 (Context Engineering)

**Deliverable:** Hiểu protocols landscape + context engineering discipline.

### Week 4 — Synthesis + Tool Adoption

- Day 22-24: Lesson 13 (Memory) + Lesson 14 (MAF) — optional, depth
- Day 25-28: Pick Tier 1 tool (ECC/Superpowers/gstack/GSD), setup, build first project

**Deliverable:** One shipped agent project using chosen Tier 1 tool.

---

## Part 8 — Tiếp theo nên làm gì / Next steps

### 8.1 Sau 4-week roadmap

**Option 1 — Deep dive 1 Tier 1 tool:**
Pick tool fit nhất với workflow, master trong 4-6 tuần.

**Option 2 — Contribute back to course:**
- VN translation improvements (course đã có VN, cần QA)
- PR lesson code samples
- Discord community participation

**Option 3 — Advance to Tier 2 platform:**
Khi cần deploy multi-user agent service → study goclaw (Storm Bear vault đã có wiki).

**Option 4 — Compare frameworks outside Microsoft:**
- LangChain / LangGraph
- CrewAI
- OpenAI Agents SDK
- Anthropic Claude SDK

### 8.2 Red flags khi học

- **Skipping lessons 01-03** — foundation. Skip = confusion later.
- **Coding before reading** — Jupyter notebooks make sense chỉ khi đọc README trước
- **Solo learning without discussion** — Discord + Storm Bear team = learning multiplier
- **Jumping to MAF (L14) first** — enterprise-specific, cần foundation trước

### 8.3 Storm Bear vault usage

**Vault's role for this course:**
- Wiki này = curated summary cho quick lookup
- `02 Wiki/(C) *.md` entity pages = reference trong lúc học
- Cross-references đến Tier 1/2 siblings = thấy **concept → implementation** mapping

**Recommended flow:**
1. Đọc lesson trên upstream repo (Jupyter/README)
2. Cross-reference với vault entity page ([[(C) Agent Design Patterns]], etc.)
3. Check sibling implementation trong ECC/Superpowers/gstack/GSD/goclaw wikis
4. Apply concept trong chosen Tier 1 tool

---

## Part 9 — Contribution opportunities

### 9.1 VN market

Course đã có VN translation. Contribution paths:

- **QA + improve existing VN translations** — likely machine-translated, human review valuable
- **Add VN-specific context** — Vietnamese dev community examples, Zalo integration samples (learned từ goclaw)
- **Vietnamese-specific lesson annotations** — e.g., Azure pricing trong VN context, latency từ Singapore/Jakarta regions

### 9.2 Non-VN

- **Additional lessons** — e.g., "AI Agents with Open Source Stack" (LangChain-centric, since course is Azure-centric)
- **Non-Microsoft framework examples** — Ollama + local models, CrewAI, LangGraph
- **Integration tests** — lesson code against live APIs với automated test

### 9.3 Storm Bear cross-ref

Bản wiki này (6th in Storm Bear vault) = unique positioning:

- **First Tier 3 entrant** — education tier addition to v4 taxonomy
- **First different-domain wiki** — testing routine generalization beyond agent-framework tools
- **VN-accessible full course summary** — quick-lookup reference trong VN cho busy devs

---

## Tóm tắt / Summary

**AI Agents for Beginners = Microsoft curriculum, 10 + 4 + 4 lessons, 50+ languages (VN có), free với GitHub Models.**

**Không phải tool. Là giáo trình.** Học trước khi adopt Tier 1 tool.

**4-week roadmap** → pick Tier 1 tool → ship real project.

**Unique value trong Storm Bear corpus:** Tier 3 slot. Teaches what Tier 1/2 siblings implement. Foundation layer.

---

## Cross-references

- Main vault: `../../../CLAUDE.md`
- Goals: `../../../GOALS.md`
- Routine: `../../../05 Skills/llm-wiki-routine.md`
- Wiki entities:
  - [[../02 Wiki/(C) Agent Design Patterns]]
  - [[../02 Wiki/(C) Agentic RAG]]
  - [[../02 Wiki/(C) Multi-Agent Systems]]
  - [[../02 Wiki/(C) Agentic Protocols (MCP + A2A + NLWeb)]]
- Siblings (Tier 1):
  - `../../Everything Claude Code - Beginner Analysis/03 Published/*`
  - `../../Superpowers - Beginner Analysis/03 Published/*`
  - `../../gstack - Beginner Analysis/03 Published/*`
  - `../../get-shit-done - Beginner Analysis/03 Published/*`
- Siblings (Tier 2):
  - `../../goclaw - Beginner Analysis/03 Published/*`
- Taxonomy (prior v4): `../../goclaw - Beginner Analysis/03 Published/(C) Agent framework taxonomy.md`
- Taxonomy v2 (3-tier, này session): [[(C) Agent framework taxonomy v2 - 3 tier]]
