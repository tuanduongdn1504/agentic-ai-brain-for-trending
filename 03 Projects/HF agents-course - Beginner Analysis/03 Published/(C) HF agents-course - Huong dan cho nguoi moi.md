# HF agents-course — Hướng dẫn cho người mới / Beginner Guide

> **Dành cho:** Developer muốn học xây dựng AI agents qua course free, có structure + hands-on + community. Course chính thức của HuggingFace.
> **Scope note:** T3 Agent-as-education — khóa học, không phải framework. Drop-in learning, không code library.

---

## 0. Đọc trước khi đi tiếp / Read this first

**VN:** HF agents-course là khóa học **free** của Hugging Face dạy build AI agents. Cần biết:

- **Prerequisites:** Basic Python + Basic LLMs (hiểu LLMs là gì, API call qua OpenAI/Anthropic)
- **Time:** ~15-25 giờ (4 units + bonus)
- **Hosted:** hf.co/learn/agents-course
- **Certification:** Leaderboard (không phải certificate chính thức)
- **Teaches 3 frameworks:** smolagents (HF) + LangGraph + LlamaIndex

**Bạn nên enroll khi:**
- Muốn học agents từ đầu có structure
- Thích hands-on learning (code-heavy)
- Muốn thử nhiều frameworks (không tied to 1 platform)
- Free budget (không chi tiền cho Coursera/Udemy)

**KHÔNG cần enroll khi:**
- Đã expert ở agents
- Chỉ muốn dùng 1 specific framework (tự read docs nhanh hơn)
- Không thích leaderboard / competition

**EN:** Free HuggingFace AI agents course. 4 units + bonus. Teaches smolagents + LangGraph + LlamaIndex BYO. Prerequisites: Python + LLMs basics. ~15-25h. Leaderboard-based completion (no formal cert).

## 1. HF agents-course là gì? / What is it?

**VN:** Khóa học chính thức của **Hugging Face** (công ty AI/ML lớn, chủ sở hữu Hub với 1M+ models OSS) dạy build AI agents.

**Format:**
- 4 units + bonus
- Hosted tại hf.co/learn/agents-course
- GitHub repo (huggingface/agents-course) chứa materials
- Discord community

**4 instructors có tên:**
- Ben Burtenshaw
- Joffrey Thomas
- Thomas Simonini (nổi tiếng — làm HF Deep RL Course trước đó)
- Sergio Paniego

**EN:** Official Hugging Face course teaching AI agents. 4 units + bonus, free, hosted at hf.co/learn. 4 named instructors. Teaches 3 frameworks.

## 2. Cấu trúc khóa học / Course structure

### 4 units

| Unit | Focus |
|------|-------|
| **Unit 1** | Agent fundamentals + concepts |
| **Unit 2** | smolagents framework (+ Bonus: observability + evaluation) |
| **Unit 3** | LangGraph / LlamaIndex / multi-framework |
| **Unit 4** | Automated evaluation + leaderboard + student projects |

### Prerequisites

- **Basic Python** — functions, classes, async basics
- **Basic LLMs** — what LLMs are, how APIs work

**Low barrier intentional** — accessible to developers without deep ML background.

### Thời gian / Time

Không explicit, nhưng tương tự HF courses khác (Deep RL, NLP): ~15-25 hours.

## 3. 3 frameworks dạy / 3 frameworks taught

### smolagents (Unit 2)

**Owner:** HuggingFace
**Position:** "Lightweight framework for creating capable AI agents"
**Why HF promotes it:** HF's answer to LangChain. Minimal overhead, native HF Hub integration.

### LangGraph (Unit 3)

**Owner:** LangChain
**Position:** Graph-based stateful agent workflows
**Why taught:** Industry-leading agent framework

### LlamaIndex (Unit 3)

**Owner:** LlamaIndex org
**Position:** RAG + data connectors
**Why taught:** Data-heavy agent context management

**HF teaches own framework alongside competitors = ecosystem-thinking curriculum.**

## 4. So sánh với Microsoft ai-agents-for-beginners / Compare with v6 peer

| Dimension | Microsoft v6 | HuggingFace v26 |
|-----------|--------------|------------------|
| **Structure** | 10 + 4 + 4 Coming Soon | 4 units + bonus |
| **Frameworks** | Microsoft Agent Framework + Azure (single-platform) | smolagents + LangGraph + LlamaIndex (multi-framework BYO) |
| **Platform** | GitHub only | HF Learn + GitHub |
| **Certification** | None | Leaderboard Unit 4 |
| **Authors** | Anonymous team | 4 named instructors |
| **Scale** | ~10K stars (older) | 28K stars |
| **License** | MIT | Apache-2.0 |

**Pick based on:**
- **Want single-platform (Microsoft ecosystem):** v6 Microsoft
- **Want multi-framework exposure:** v26 HuggingFace
- **Want named instructors + leaderboard:** v26 HuggingFace
- **Want broader coverage (18 lessons):** v6 Microsoft
- **Want HF Hub / Spaces integration:** v26 HuggingFace

## 5. Enrollment / Đăng ký

### Bước 1 — Register

Go to **hf.co/learn/agents-course** → register (free, need HF account)

### Bước 2 — Join Discord

discord.gg/UrrTSsSyjb → primary support channel

### Bước 3 — Start Unit 1

Read course materials + run code examples

### Bước 4 — Progress through units

- Unit 2: deep dive smolagents
- Unit 3: LangGraph + LlamaIndex
- Unit 4: build capstone project + submit to leaderboard

## 6. HuggingFace ecosystem (miễn phí / free) you can use

Khi học course, bạn có access free:
- **HF Hub** — 1M+ models (Llama, Mistral, Qwen, smolagents demos, etc.)
- **Spaces** — host demo apps free
- **Inference API** — free tier for experiments
- **Datasets** — 200K+ datasets
- **Tokenizers + Transformers** — full OSS libraries

**Free + integrated ecosystem** = significant learning advantage.

## 7. Community

### Discord
- Primary support
- 4 instructors participate
- Cross-course integration (shared with HF Deep RL Course, NLP Course, etc.)
- Peer learning

### Other channels
- GitHub issues (for material bugs / contributions)
- HF Forum
- Twitter (follow HF + instructors)

## 8. Leaderboard certification

### How it works

- Unit 4: build agent for benchmark tasks
- Automated evaluation runs agents
- Leaderboard displays rankings
- Public → portfolio evidence

### No formal certificate

Không phải **formal credential** cho CV/resume. Nhưng:
- Leaderboard placement = public proof of skill
- Top ranks = community recognition
- Portfolio link = job application value

**Hybrid informal-gamified model.**

## 9. Lộ trình 4 tuần / 4-week roadmap

### Tuần 1 — Unit 1 + orient

- [ ] Register tại hf.co/learn/agents-course
- [ ] Join Discord (discord.gg/UrrTSsSyjb)
- [ ] Complete Unit 1 (agent fundamentals)
- [ ] Set up HF account + Hub access

### Tuần 2 — Unit 2 smolagents

- [ ] Complete Unit 2 main content
- [ ] Build first smolagents example
- [ ] Unit 2 Bonus: observability + evaluation

### Tuần 3 — Unit 3 multi-framework

- [ ] Complete LangGraph section
- [ ] Complete LlamaIndex section
- [ ] Compare 3 frameworks — pick favorite for Unit 4

### Tuần 4 — Unit 4 capstone + leaderboard

- [ ] Build capstone project (choose framework)
- [ ] Submit to automated evaluation
- [ ] Check leaderboard placement
- [ ] Deploy to HF Spaces as portfolio

## 10. Storm Bear operator relevance / Mức độ phù hợp

**VN:** Storm Bear operator (Scrum coach + developer):

**Medium relevance:**
- ✅ Build AI agent skill = long-term investment
- ✅ smolagents framework có thể useful cho Scrum-coaching agent prototype
- ✅ HF Hub + Spaces = free infrastructure cho experiment
- ✅ Free + structured = low-cost skill development

**Timing considerations:**
- Storm Bear = primary Scrum coaching role
- AI agent fluency = secondary skill
- ~15-25h commitment = feasible week-by-week

**Potential Storm Bear application:**
- Complete course → build Scrum-coaching agent as Unit 4 project
- Use smolagents + HF Hub for deployment
- Capture learnings → feed Storm Bear vault patterns
- Share demo via HF Spaces as team tool

**EN:** Medium relevance. Build AI agent fluency + prototype Scrum-coaching agent. Free + structured. ~15-25h commitment.

## 11. Critique / Nhận xét

### Strengths

- ✅ Free + accessible
- ✅ Multi-framework BYO = ecosystem literacy
- ✅ Named instructors = quality + accountability
- ✅ Integrated HF ecosystem = free tooling
- ✅ Leaderboard gamification = engagement
- ✅ Active Discord community

### Limitations

- ⚠️ **English only** — no i18n (same gap as Microsoft v6)
- ⚠️ **Fast-moving field** — agent frameworks evolve; content may age
- ⚠️ **3 frameworks = cognitive load** — students may master none deeply
- ⚠️ **No formal credential** — leaderboard not transferable to CV
- ⚠️ **Prerequisites** — not absolute-beginner friendly (assumes Python + LLMs)

## 12. Next actions

**Nếu bạn muốn enroll:**
1. Go to hf.co/learn/agents-course now (free registration)
2. Join Discord for peer learning
3. Commit to 4-week schedule (~4h/week)

**Nếu bạn đang decide between v6 Microsoft + v26 HF:**
- Single-platform preference + broader coverage → Microsoft v6
- Multi-framework exposure + HF ecosystem → HuggingFace v26
- Can do both sequentially (Microsoft first for breadth, HF second for depth)

**Nếu bạn là Storm Bear operator:**
1. Evaluate: primary Scrum role vs secondary AI agent skill
2. If enrolling: use Scrum-coaching agent as Unit 4 project
3. Deploy demo to HF Spaces for team

## 13. References

- Course platform: hf.co/learn/agents-course
- GitHub: github.com/huggingface/agents-course
- Discord: discord.gg/UrrTSsSyjb
- Parent org: huggingface.co
- smolagents: github.com/huggingface/smolagents
- LangGraph: langchain-ai/langgraph
- LlamaIndex: llamaindex.ai
- T3 peer: Microsoft ai-agents-for-beginners (alternative course)

---

**HuggingFace agents-course = free 4-unit course teaching 3 frameworks BYO (smolagents + LangGraph + LlamaIndex). 4 named instructors, Discord community, leaderboard certification. Prerequisites: Python + LLMs basics. ~15-25h. T3 tier (Agent-as-education) — closes 5/5 tier validation milestone in Storm Bear corpus. Storm Bear: MEDIUM relevance (AI agent skill-building; Scrum-coaching agent prototype possibility).**
