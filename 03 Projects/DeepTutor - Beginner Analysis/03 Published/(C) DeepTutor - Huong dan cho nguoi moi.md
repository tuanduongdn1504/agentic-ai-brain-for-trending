# DeepTutor — Hướng dẫn cho người mới / Beginner Guide

> **Repo:** `HKUDS/DeepTutor` (21.2K⭐, 2.9K forks, Apache-2.0, Python 3.11+ + Next.js 16)
> **Tagline:** *"DeepTutor: Agent-Native Personalized Tutoring"* (Trợ lý học tập cá nhân hóa, agent-native)
> **Author:** HKUDS = Data Intelligence Lab @ HKU (ĐH Hong Kong); maintainer: `@pancacake`
> **License:** Apache-2.0 (permissive — dùng thương mại OK, yêu cầu attribution)
> **Scope:** T5 Agent-as-application — **education-application T5 sub-archetype mới** (6th T5 entrant trong Storm Bear corpus)

---

## Part 1 — DeepTutor là gì? / What is it?

**VN:** DeepTutor là một **nền tảng học tập cá nhân hóa agent-native** — tức là agents (không phải chatbot tĩnh) chạy các pipeline nhiều bước để dạy bạn học. Bạn upload PDF / Markdown / TXT → xây Knowledge Base → chat qua 6 modes (Chat / Deep Solve / Quiz / Deep Research / Math Animator / Visualize) chia sẻ cùng context → hoặc biên soạn "living book" qua Book Engine (14 loại block) → hoặc viết tài liệu với AI Co-Writer → hoặc tạo **TutorBots** (tutor độc lập, mỗi bot có workspace + memory + personality riêng, kết nối Telegram/Discord/Slack/Feishu/WeChat/etc).

**EN:** DeepTutor is an **agent-native personalized learning platform** where agents (not static chatbots) run multi-step pipelines to teach you. Upload PDF/MD/TXT → Knowledge Base → chat across 6 modes sharing context → or Book Engine compiles interactive "living books" with 14 block types → or Co-Writer for multi-document AI-collaborative writing → or create **TutorBots** (autonomous tutors, each with own workspace + memory + personality + multi-channel connectors like Telegram/Discord/Slack/Feishu/WeChat).

**Khác biệt quan trọng:** DeepTutor **KHÔNG PHẢI chatbot**. TutorBot có **Heartbeat proactive** — chủ động nhắc lịch học / check-in / review — tutor tự nó "tìm đến bạn" thay vì chỉ đợi bạn hỏi.

## Part 2 — Corpus-first signals (v38)

DeepTutor là **thứ 6 trong Tier 5 "Agent-as-application"** của Storm Bear corpus (sau deer-flow / autoresearch / paperclip / Skyvern / OpenHands). Điểm đặc biệt tại v38:

1. **Education-application T5 sub-archetype MỚI** — dùng agents để dạy humans bất kỳ môn học nào (khác với T3 education-course dạy HOW-to-build-agents)
2. **Asia-academic-lab T5** — HKUDS là lab nghiên cứu ở ĐH Hong Kong (trước có US v30 UIUC+CMU + CN v22 Lab4AI; giờ thêm HK)
3. **Pattern #44 Academic-Lab Affiliation N=3** — DeepTutor là data point thứ 3, đưa pattern lên tier default-criterion đầu tiên cho pattern liên quan đến academic-lab
4. **9-language README** (EN + zh-CN + JA + ES + FR + AR + RU + HI + PT + TH) — Arabic + Russian + Hindi + Portuguese + Thai lần đầu xuất hiện cùng lúc ở T5
5. **27 LLM providers** (lớn nhất trong corpus Storm Bear) + 7 embedding + 7 search = **41 integrations**; `.env.example_CN` pre-configured cho Trung Quốc
6. **14-block-type multi-agent "living book" compiler** (corpus-first)
7. **Bilateral runtime-and-skill** — DeepTutor vừa RUN agents (TutorBot + Capabilities) vừa EXPOSE SKILL.md cho external agents vận hành (2-way; corpus-first)
8. **HKUDS 7-repo academic ecosystem-portfolio** (nanobot 40.7K + LightRAG 34.2K + CLI-Anything 32.4K + DeepTutor 21.2K + RAG-Anything 18.3K + DeepCode 15.3K + OpenHarness 11.1K = ~173K combined) — largest academic-lab ecosystem trong corpus
9. **Persistent autonomous TutorBot architecture** với Soul Templates (personality-as-file) + 8+ multi-channel connectors
10. **arXiv "Coming Soon" badge** — Pattern #42 observational-in-waiting (chưa publish, không tính data point)
11. **20K stars trong 111 ngày = ~190 stars/ngày sustained-viral** (Pattern #27 14th data point)
12. **Không tích hợp MCP** — T5-academic-research 2nd counter-evidence cho Pattern #18 (sau v36 pi-mono T1-scale)

## Part 3 — Tier placement + vị trí

**Tier:** **T5 Agent-as-application** — DeepTutor là standalone runnable application (không phải framework để dev tự build, không phải plugin Claude Code).

**Archetype:** Academic-lab ecosystem-portfolio + education-application — **kết hợp hai đặc trưng lần đầu cùng xuất hiện trong corpus**.

**So sánh T3 vs T5 ở v38:**

| Axis | T3 (v6 Microsoft / v26 HF agents-course) | T5 (DeepTutor v38) |
|------|----------------------------|---------------------|
| **Teach what?** | Cách build agent | Bất kỳ môn học gì (dùng agent làm phương tiện) |
| **Audience** | Dev học agent-skills | Học sinh / sinh viên / self-learner |
| **Format** | Course curriculum | Runnable platform |
| **Agent role** | Subject-of-study | Delivery-mechanism |

## Part 4 — Cài đặt / Installation

### 4.1 Option A — Setup Tour (khuyến nghị)

```bash
git clone https://github.com/HKUDS/DeepTutor.git
cd DeepTutor

# Tạo Python virtual environment (chọn 1)
conda create -n deeptutor python=3.11 && conda activate deeptutor
# Hoặc:
python -m venv .venv && source .venv/bin/activate

# Chạy guided tour
python scripts/start_tour.py
```

Tour sẽ hỏi Web mode (khuyến nghị) hay CLI mode, cài deps, config LLM + embedding + search providers, test connection, auto-launch. Mặc định mở `http://localhost:3782`.

### 4.2 Option B — Manual

```bash
pip install -e ".[server]"
cd web && npm install && cd ..
cp .env.example .env
# Sửa .env (tối thiểu cần: LLM_BINDING, LLM_MODEL, LLM_API_KEY, LLM_HOST +
# EMBEDDING_BINDING, EMBEDDING_MODEL, EMBEDDING_API_KEY, EMBEDDING_HOST, EMBEDDING_DIMENSION)
python scripts/start_web.py
```

**Lưu ý VN:** `cp .env.example_CN .env` có sẵn config CN providers (DeepSeek + DashScope + Zhipu + Moonshot + Brave search) — tiết kiệm 50-80% chi phí so với OpenAI, phù hợp budget Việt Nam.

### 4.3 Option C — Docker (nhanh nhất cho production)

```bash
git clone https://github.com/HKUDS/DeepTutor.git && cd DeepTutor
cp .env.example .env   # (hoặc .env.example_CN)
# Pull ảnh đã build sẵn (linux/amd64 + linux/arm64 đều có)
docker compose -f docker-compose.ghcr.yml up -d
```

Official image: `ghcr.io/hkuds/deeptutor:latest` hoặc pin version `:1.0.0`. Mở `http://localhost:3782`.

### 4.4 Option D — CLI only (không cần web)

```bash
pip install -e ".[cli]"
cp .env.example .env
deeptutor chat
```

**Daily launch** sau setup lần đầu: `python scripts/start_web.py` — tự động bật backend + frontend + mở browser.

## Part 5 — Core usage pattern

### 5.1 Workflow cơ bản

1. **Upload documents** → tạo Knowledge Base
   ```bash
   deeptutor kb create scrum-bok --doc ScrumGuide2020.pdf
   deeptutor kb add scrum-bok --doc EssentialScrum.pdf
   deeptutor kb set-default scrum-bok
   ```

2. **Chat với RAG** (hoặc trên web UI):
   ```bash
   deeptutor chat --tool rag --tool web_search --kb scrum-bok
   ```
   Inside REPL:
   - `/cap deep_solve` → switch sang multi-agent problem-solving
   - `/cap deep_research` → decompose + parallel research
   - `/tool on code_execution` → bật Python sandbox

3. **Compile "living book"** từ KB (Web UI → Book menu; hoặc API)
4. **Tạo TutorBot** VN Scrum Master:
   ```bash
   deeptutor bot create vn-scrum-coach \
     --persona "Socratic VN Scrum Master who asks probing questions in Vietnamese about sprint mechanics"
   ```

### 5.2 6 Chat modes

| Mode | Khi nào dùng |
|------|--------------|
| Chat | Hỏi đáp thông thường + tools (RAG + web + code + reason + brainstorm + paper) |
| Deep Solve | Giải bài toán / vấn đề phức tạp: plan → investigate → solve → verify + citations |
| Quiz Generation | Tạo câu hỏi đánh giá từ KB (có validation) |
| Deep Research | Phân tích topic: decompose → parallel subtopic agents → cited report |
| Math Animator | Tạo animation Manim từ concept toán |
| Visualize | Tạo diagram SVG / Chart.js / Mermaid / HTML từ natural language |

## Part 6 — Novel concepts

### 6.1 2-layer plugin model

- **Level 1 — Tools** (7 built-in: rag / web_search / code_execution / reason / brainstorm / paper_search / geogebra_analysis). Đơn chức năng; LLM gọi theo nhu cầu.
- **Level 2 — Capabilities** (4+ built-in: chat / deep_solve / deep_question / deep_research + extended: math_animator / visualize). Multi-step; "take over the conversation"; stream events.

### 6.2 TutorBot = persistent autonomous agents

Không phải chatbot. Mỗi bot có:
- **Soul Template** (personality-as-file: Socratic / encouraging / rigorous / custom)
- **Workspace độc lập** (memory + session + skills tách biệt)
- **Heartbeat proactive** — tự initiate nhắc nhở / review / check-in
- **Multi-channel** (Telegram + Discord + Slack + Feishu + WeChat Work + DingTalk + Email)
- **Per-bot LLM provider** — bot này dùng Claude, bot kia dùng DeepSeek
- **Skill Learning** — add file SKILL.md vào workspace → bot có thêm ability

### 6.3 Book Engine = multi-agent living-book compiler

Input: topic + KB. Output: interactive book 14 block types. Multi-agent pipeline: outline → retrieve sources → chapter tree → page plan → compile blocks. Real-time progress timeline.

**14 blocks:** text / callout / quiz / flash cards / code / figure / deep dive / animation / interactive demo / timeline / concept graph / section / user note / placeholder.

### 6.4 Bilateral SKILL.md (corpus-first)

DeepTutor đồng thời:
- Chạy agents bên trong (TutorBot + Capabilities) — agent-HOST
- Public SKILL.md cho external agents điều khiển DeepTutor qua CLI — agent-TOOL

Đưa file `SKILL.md` cho nanobot / Claude-with-tool-use / Codex → LLM đó tự vận hành DeepTutor (setup providers + tạo KB + chạy capability + đọc NDJSON events). **Corpus-first 2-way.**

## Part 7 — So sánh DeepTutor với các khung khác trong Storm Bear corpus

| Dimension | DeepTutor v38 | OpenHands v30 | deer-flow v9 | paperclip v14 | Skyvern v24 | autoresearch v10 |
|-----------|---------------|---------------|---------------|---------------|-------------|------------------|
| Tier | T5 | T5 | T5 | T5 | T5 | T5 |
| Scope | Education | SWE | Research | Orchestration | Browser | ML research |
| Org archetype | Academic-lab (HKU) | Academic-commercial (UIUC+CMU + All Hands AI) | Corporate (ByteDance) | Community-platform | Commercial (Skyvern-AI) | Solo-known (Karpathy) |
| License | Apache-2.0 | MIT + enterprise-dir | MIT | MIT | AGPL-3.0 + Cloud | MIT |
| arXiv | "Coming Soon" | ICLR 2025 + Nov 2025 SDK | No paper | No paper | No paper | Blog-post-only |
| LLM providers | **27 (corpus-most)** | Multi | Multi via LangGraph | Multi | 8+ | — |
| Deployment | Docker GHCR + local + CLI | Docker + SDK + Cloud | Python + Next.js | Monorepo | Docker + Cloud | Single-dir Python |
| Multi-channel bot | 8+ | — | — | — | — | — |
| Book compiler 14 blocks | ✅ unique | — | — | — | — | — |
| TutorBot persistent autonomous | ✅ unique | Partial (agent loop) | — | Partial (orchestration) | — | Cron-scheduled single agent |

**Đặc trưng DeepTutor:** education-purpose + ecosystem-portfolio (7 repos HKUDS) + bilateral SKILL.md + largest provider coverage.

## Part 8 — Ethical + supply-chain framing

**Rủi ro thấp** cho Storm Bear operator:

| Rủi ro | Đánh giá | Mitigation |
|--------|----------|------------|
| License commercial-gate | ❌ None (Apache-2.0) | Attribution requirement (standard) |
| Maintainer bus-factor | Medium (`@pancacake` solo name-face, lab backing) | Fork + monitor |
| arXiv unpublished | Low-medium credibility for client pitches | Cite HKUDS lab + LightRAG EMNLP 2025 track record |
| Supply-chain (no SECURITY.md) | Medium | Run `pip-audit` locally; monitor HKUDS issues |
| Data privacy (KB) | Low nếu self-host Docker | Không upload KB cloud provider; tất cả local |
| Client-content copyright | Medium | Per-document licensing (book copyright tách biệt) |
| Dependency CN-ecosystem | Low | `.env.example_CN` optional; có thể dùng US-only stack |

**So sánh với các corpus framework ⚠️ higher-risk:**
- ❌ fish-speech v20 (non-OSI commercial-funnel license) — DeepTutor Apache-2.0 sạch hơn
- ❌ system-prompts-leaks v21 (ethical gray zones) — DeepTutor không có
- ❌ Skyvern v24 (AGPL-3.0 commercial-moat + anti-bot gated) — DeepTutor không có gate

**Kết luận:** DeepTutor có **rủi ro thấp nhất cho VN-solo-operator adoption** trong số 6 T5 entrants.

## Part 9 — Storm Bear relevance (VN operator + Scrum Coach)

### 9.1 Use case trực tiếp

**Self-directed learning:**
- Upload Storm Bear wiki corpus (37 wikis) → tạo KB "Agent-Framework Corpus"
- Deep Research + Chat with RAG để xem-và-hiểu-nhanh từng framework
- Meta-ROI: accelerate vault knowledge compounding

**Scrum teaching:**
- Upload Scrum BoK (Scrum Guide / Agile Estimating / Succeeding with Agile) → KB "Scrum BoK"
- Book Engine compile "Scrum Living Book" VN (nếu i18n VN UI có) với 14 block types
- TutorBot VN Scrum Master — Soul Template + Vietnamese persona

**Client research:**
- Deep Research topic "VN Scrum adoption 2026" → cited report từ RAG + web + arXiv
- Co-Writer tạo client proposals / pitch decks multi-document

### 9.2 Effort ước tính

- **Week 1** (1 weekend): Setup Tour install + load 2 KBs (Storm Bear vault + Scrum BoK) + thử 6 chat modes
- **Week 2-3** (1-2 weekends): Compile Book Engine trên Scrum BoK + tạo TutorBot "VN Scrum Master"
- **Week 4+** (ongoing): Tích hợp vào workflow weekly (use DeepTutor thay cho lookup / research)
- **Month 2+** (nếu VN client pilot): PR VN README + `language: "vi"` UI support (~1-2 weekends)

### 9.3 Pilot ranking updated at v38

**Top 5 Storm Bear pilots (revised):**
1. claude-hud v35 (5-min install + immediate ROI)
2. spec-kit v17 (SDD methodology)
3. **🆕 DeepTutor v38 (education platform + Book Engine + TutorBot VN-Scrum potential)**
4. OMC v27 (Scrum-ceremony pipeline)
5. claude-code-best-practice v34 (82-tip aggregation)

**Tại sao DeepTutor vào top 3:** sự kết hợp unique giữa self-learning platform + teaching platform + VN viability + academic credibility (HKUDS lab) + cost-effective multi-provider setup. No other T5 entrant offers this combination.

## Part 10 — 4-week learning roadmap

### Week 1 — Self-directed learning

- Install (Setup Tour option A)
- Load 2 KBs: Storm Bear vault + personal learning materials
- Explore 6 chat modes (Chat / Deep Solve / Quiz / Deep Research / Math Animator / Visualize)
- Toggle tools `/tool on rag` `/tool on web_search` `/tool on reason`

**Success criteria:** Cảm thấy tự tin dùng DeepTutor thay cho ChatGPT + Claude web cho daily learning.

### Week 2 — Book Engine experiment

- Compile "Storm Bear Agent-Framework Landscape 2026" living book từ 37 wikis KB
- Review outline → reorder chapters → watch 14-block-type compilation
- Export + present self-review (concept graph / timeline / flash cards)

**Success criteria:** Book compilation xong; đánh giá output quality so với tự viết từ đầu.

### Week 3 — TutorBot VN Scrum Master

- Create TutorBot `vn-scrum-coach` với Socratic persona VN-Scrum-Master
- Add skills: `scrum-ceremony-skill.md` + `agile-estimation-skill.md` (operator-authored)
- Connect Telegram channel (test self-driven check-in)

**Success criteria:** TutorBot hoạt động, có proactive Heartbeat nhắc lịch, trả lời được 10-15 câu hỏi Scrum cơ bản.

### Week 4 — Deep Research + client synthesis

- Run Deep Research "VN Scrum adoption 2026 landscape" với KB + web + arXiv
- Co-Writer multi-document pitch deck cho client hypothetical
- Evaluate end-to-end: research → writing → notebook save workflow

**Success criteria:** Có thể pitch VN client với DeepTutor-generated research report; DeepTutor đã integrate vào weekly Storm Bear workflow.

## Part 11 — Tradeoffs + limitations

### Pros

- Apache-2.0 + 27 LLM providers (highest corpus) + Docker multi-arch
- Bilateral SKILL.md = agent-native on both sides
- Book Engine + TutorBot + Deep Research = education-platform-grade features
- HKUDS academic-lab credibility (+ LightRAG EMNLP 2025 sibling paper)
- Active development (~9 releases/month post-v1.0)
- CN-ecosystem-friendly (`.env.example_CN` + 11 CN LLM bindings) = VN budget-friendly

### Cons

- `@pancacake` sole named maintainer bus-factor (offset by HKUDS lab)
- No Vietnamese UI i18n (PR opportunity)
- No MCP integration (doesn't plug vào Claude Code workflow; standalone only)
- Python 3.11+ required; Manim optional (heavy if math-animator dùng)
- arXiv paper pending (< ICLR 2025 OpenHands credibility for now)
- 27 providers = choice-paralysis; cần opinionated defaults

### Competitive positioning

- **vs Anthropic Claude Projects:** DeepTutor = self-host + Apache-2.0 + multi-provider + Book Engine + TutorBot multi-channel; Claude Projects = cloud-only + Anthropic-only
- **vs Notion AI / Obsidian AI plugins:** DeepTutor = agent-native + multi-mode + compilation; Notion/Obsidian = note-centric + LLM-augmented
- **vs OpenWebUI + self-host LLM:** DeepTutor = education-focused + TutorBot autonomous; OpenWebUI = generic chat-UI + multi-user

## Part 12 — Caveats + safety notes

- ⚠️ **KB documents copyright** — bạn tải sách Scrum lên KB là trách nhiệm cá nhân; không redistribute KB
- ⚠️ **API costs** — Deep Research runs parallel agents → chi phí tăng; monitor usage theo tuần
- ⚠️ **Client data privacy** — self-host Docker; KB lưu tại `./data/knowledge_bases` local, không upload cloud provider
- ⚠️ **Code execution tool** — sandboxed Python nhưng vẫn có risk; dùng cho trusted content thôi
- ⚠️ **arXiv "Coming Soon"** — chưa trích dẫn được paper; present là "HKUDS research-backed" + cite LightRAG EMNLP 2025 sibling paper thay thế cho đến khi DeepTutor paper publish
- ⚠️ **TutorBot multi-channel** — Telegram/Discord/Slack/Feishu/WeChat bot tokens cần secure storage; không commit `.env` lên public repo

## Part 13 — References + next action

**Repo:** https://github.com/HKUDS/DeepTutor
**License:** Apache-2.0
**HKUDS org:** https://github.com/HKUDS (7-repo academic ecosystem-portfolio)
**Cluster siblings:** nanobot 40.7K + LightRAG 34.2K (EMNLP 2025) + CLI-Anything 32.4K + RAG-Anything 18.3K + DeepCode 15.3K + OpenHarness 11.1K

**Storm Bear cross-refs:**
- `/Users/Cvtot/KJ OS Template/03 Projects/OpenHands - Beginner Analysis/` — closest T5 peer (academic-commercial)
- `/Users/Cvtot/KJ OS Template/03 Projects/LlamaFactory - Beginner Analysis/` — outside-scope academic-lab precedent
- `/Users/Cvtot/KJ OS Template/03 Projects/bizos-company-os - Beginner Analysis/` — v37 YELLOW precedent
- `/Users/Cvtot/KJ OS Template/PATTERN_LIBRARY.md` — Pattern #44 now N=3 default-criterion

**Recommended next action (operator):**

**Option 1 (self-directed; 1 weekend):** Cài Setup Tour + load Storm Bear vault KB → explore Deep Research trên corpus của chính mình → đánh giá xem DeepTutor có replace workflow ChatGPT/Claude hiện tại không.

**Option 2 (VN client pilot; 2-3 weekends):** Fork DeepTutor + PR VN README + start `language: "vi"` UnifiedContext + first VN client demo hypothetically — earn "first VN contributor on HKUDS/DeepTutor" positioning.

**Option 3 (Book Engine on vault; 1-2 weekends):** Upload Storm Bear vault → compile "Agent Framework Landscape 2026" living book → vault becomes shareable public-HTML asset.

**Status:** DeepTutor ranks #3 Storm Bear pilot at v38. Strongly recommended: Option 1 before end of 2026-Q2 (1 weekend investment; unlock education-platform workflow).

---

*Hướng dẫn này hoàn thành v38 Storm Bear corpus wiki cho HKUDS/DeepTutor. Xem wiki pages trong `02 Wiki/` để tra cứu architecture / org / Storm Bear strategic synthesis chi tiết, và `04 Reviews/(C) 2026-04-24 v38 build learnings.md` cho iteration log đầy đủ.*
