# (C) MiroFish — Beginner Guide / Hướng dẫn người mới

**Project**: `666ghj/MiroFish` — *"A Simple and Universal Swarm Intelligence Engine, Predicting Anything"* / *简洁通用的群体智能引擎，预测万物*
**License**: AGPL-3.0
**Stars**: 57,307
**Status (snapshot)**: v0.1.2 (early-stage despite 57K stars)
**Storm Bear pilot relevance**: LOW direct / LOW-MEDIUM observational

---

## ⚠️ Read this first / Đọc cái này trước

Before evaluating MiroFish, understand 4 things:

**🇬🇧 EN**:
1. **AGPL-3.0 license** — if you deploy MiroFish as a network service (e.g., on `predict.mycompany.com`), you must make the **complete source code of any modifications publicly available** to your users. This is significantly more restrictive than MIT/Apache. Don't deploy MiroFish for paying clients without legal review.
2. **Commercial product, pre-monetization** — MiroFish has strategic backing from **Shanda Group** (a major Chinese internet conglomerate). The mirofish.ai homepage exists. The recruiting email is `mirofish@shanda.com`. There is NO Pro tier yet, but expect monetization to emerge later. Decisions you make today (data, integrations) may need re-evaluation when the commercial model is announced.
3. **High LLM API consumption** — README explicit warning: *"try simulations with fewer than 40 rounds first."* A 10-round simulation already involves dozens of agents × multiple actions × LLM calls. Default: Alibaba Qwen-plus via Bailian (CN cloud). Expect to spend money quickly. Set spending alerts before running.
4. **Domain mismatch for Scrum coaching** — MiroFish predicts financial / political / public-opinion / novel-ending outcomes. It is NOT designed for Scrum sprint outcome prediction or team retrospective simulation. Could you bend it that way? Theoretically yes; practically not falsifiable, not cost-effective. Treat MiroFish as **observational study**, not pilot.

**🇻🇳 VN**:
1. **License AGPL-3.0** — nếu bạn deploy MiroFish dưới dạng dịch vụ mạng (ví dụ trên `predict.mycompany.com`), bạn **phải công khai source code của mọi sửa đổi** cho người dùng. Hạn chế hơn nhiều so với MIT/Apache. Đừng deploy cho khách hàng trả phí mà chưa xem xét pháp lý.
2. **Sản phẩm thương mại, chưa kiếm tiền** — MiroFish có hậu thuẫn chiến lược từ **Shanda Group** (tập đoàn internet lớn của Trung Quốc). Có homepage mirofish.ai. Email tuyển dụng là `mirofish@shanda.com`. Chưa có Pro tier nhưng sớm muộn sẽ có. Quyết định hôm nay (data, tích hợp) có thể phải xem lại khi mô hình thương mại công bố.
3. **Tiêu LLM API rất tốn** — README cảnh báo rõ: *"thử simulation dưới 40 vòng trước."* 10 vòng đã có hàng chục agent × nhiều action × nhiều LLM call. Mặc định: Alibaba Qwen-plus qua Bailian (cloud TQ). Tiền bay rất nhanh. Bật cảnh báo chi tiêu trước khi chạy.
4. **Lệch domain với Scrum coaching** — MiroFish dự đoán tài chính / chính trị / dư luận / kết truyện. KHÔNG thiết kế để dự đoán kết quả sprint hay retrospective. Có thể uốn cong thành dùng cho Scrum không? Lý thuyết được; thực tế không kiểm chứng được, không tiết kiệm. Coi MiroFish như **case study quan sát**, không phải pilot.

---

## 1. What MiroFish is / MiroFish là gì

**🇬🇧 EN**:
MiroFish is a multi-agent prediction engine. You upload a "seed" — news, policy draft, financial signal, or a novel — and describe what you want to predict in natural language. MiroFish then:
1. Builds a knowledge graph from the seed
2. Generates "agents" with personalities, memory, and behavior derived from the seed entities
3. Runs a simulated social network (Twitter or Reddit) where these agents interact for N rounds
4. Generates a prediction report from the simulated outcomes
5. Lets you chat with any agent in the simulated world to dig deeper

The output is **a digital sandbox you can interrogate**, not just a forecast number.

**🇻🇳 VN**:
MiroFish là engine dự đoán đa-agent. Bạn upload "seed" — tin tức, dự thảo chính sách, tín hiệu tài chính, hay tiểu thuyết — rồi mô tả bằng ngôn ngữ tự nhiên muốn dự đoán cái gì. MiroFish sẽ:
1. Xây knowledge graph từ seed
2. Tạo "agent" có tính cách, ký ức, hành vi từ entity trong seed
3. Chạy mạng xã hội ảo (Twitter hoặc Reddit) với agent tương tác N vòng
4. Sinh báo cáo dự đoán từ kết quả mô phỏng
5. Cho bạn chat với bất kỳ agent nào trong thế giới ảo để đào sâu

Output là **sandbox số bạn có thể tra hỏi**, không chỉ là con số dự báo.

---

## 2. Use cases (per README)

- ✅ **Public Opinion Simulation** (live demo: Wuhan University event)
- ✅ **Novel Ending Simulation** (Bilibili demo: Dream of the Red Chamber)
- 🟡 **Financial Prediction** (listed "coming soon")
- 🟡 **Political News Prediction** (listed "coming soon")

**For Scrum coaching role**: none of these fit directly. Don't try to retrofit "predict sprint outcome" — the simulation infrastructure is built for **public-opinion-style** dynamics (posts, likes, retweets, comments), not engineering team behavior.

---

## 3. System requirements / Yêu cầu hệ thống

| Tool | Version | Note |
|------|---------|------|
| Node.js | 18+ | for frontend |
| Python | 3.11 - 3.12 | not 3.13+ |
| uv | latest | Python package manager from Astral |
| Docker | optional | alternative to source install |
| LLM API key | required | Qwen via Bailian recommended; OpenAI/Claude/etc. work |
| Zep Cloud account | required | https://app.getzep.com (free tier sufficient for testing) |
| ~4-8 GB RAM | recommended | for backend + frontend dev servers + simulation subprocesses |

**Cost estimate for a 10-round simulation** (rough; verify yourself before scaling):
- ~50-200 agents × 10 rounds × ~3-5 LLM calls per agent per round = ~1500-10000 LLM calls
- Qwen-plus typical cost: ~$0.50-3 per 1M tokens; one call ~500-2000 tokens
- → **single simulation: $1-15 USD ballpark** depending on agent count + token sizes
- 40-round simulation: **$5-60 USD ballpark**

⚠️ Always check current pricing on your provider before running.

---

## 4. Install — Source clone (recommended for evaluation)

```bash
# Clone
git clone https://github.com/666ghj/MiroFish.git
cd MiroFish

# Configure
cp .env.example .env
# Edit .env, fill in:
#   LLM_API_KEY=your_qwen_or_openai_key
#   LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
#   LLM_MODEL_NAME=qwen-plus
#   ZEP_API_KEY=your_zep_key

# One-click install everything
npm run setup:all

# Start backend + frontend together
npm run dev
```

Frontend at `http://localhost:3000`, backend at `http://localhost:5001/health`.

## 4 (alt). Install — Docker

```bash
git clone https://github.com/666ghj/MiroFish.git
cd MiroFish
cp .env.example .env
# (edit .env same as above)

docker compose up -d
```

If pull is slow from your region, swap to the CN mirror in `docker-compose.yml`: `ghcr.nju.edu.cn/666ghj/mirofish:latest`.

⚠️ The Dockerfile runs `npm run dev` — meaning Docker deployment uses **dev-mode servers** (Flask debug + Vite dev). Not production-hardened. Fine for evaluation; do NOT expose to public internet without putting nginx + SSL in front and switching to production builds.

---

## 5. First simulation walkthrough

1. Open `http://localhost:3000` in browser
2. Create a project (likely a "+" button on dashboard)
3. Upload seed material — start with a small text file (e.g., a 1-page summary of an event)
4. Describe what you want to predict (e.g., "How will public opinion react to this policy in 7 days?")
5. **Set rounds to ≤10 for the first run** (per README warning)
6. Wait for graph building → environment setup → simulation → report generation
7. Read the report
8. Click on an agent in the simulated world → chat with them to understand their reasoning

**First run will likely cost $1-5 USD in LLM tokens. Monitor your API dashboard.**

---

## 6. Storm Bear use cases — honest assessment

### 6a. Direct utility: NONE

There is no direct vault-applicable use case for Scrum coaching. MiroFish is not built for:
- Sprint outcome prediction
- Team retrospective simulation
- Stakeholder behavior modeling at company scale
- Backlog prioritization
- Anything Scrum-Master-flavored

Don't try to make it fit.

### 6b. Speculative use cases (don't pilot, don't recommend to clients)

If you really wanted to try (cost: $5-30 USD per attempt; falsifiability: low):
- Upload a sprint retrospective document; describe "predict team's behavior next sprint"
- Upload a stakeholder kickoff meeting transcript; describe "predict stakeholder concerns at sprint review"
- Upload a backlog; describe "predict which stories will slip"

**Why this is not recommended**:
- The OASIS multi-agent simulation models **public-opinion-style** dynamics (posts/likes/retweets), not engineering team standups
- "Personality + memory + behavior" injected from a 10-page retrospective is **semantically thin** — won't capture team dynamics nuance
- No way to validate whether the prediction was right (you'd have to wait a sprint, then realize the cost wasn't worth it)
- Storm Bear's value to clients is **structured human reflection**, not algorithmic forecasting

### 6c. Observational value: MEDIUM

Things to learn from MiroFish even without piloting:
- **AGPL-3.0 commercial-product pattern** — useful if Storm Bear ever commercializes
- **Multi-agent simulation methodology** — interesting research direction; CAMEL-AI / OASIS lineage is worth following
- **Pattern #12 v42 refined formulation** corroboration — vault governance philosophy reference
- **i18n architecture** — registered-vs-translated-vs-documented 3-tier mismatch is a corpus-observable lesson for vault publishing strategy
- **Bilingual EN+ZH README at 57K** — minimum-viable documentation localization at high-scale; useful template

---

## 7. 4-week evaluation roadmap (if you decide to invest time despite domain mismatch)

⚠️ Storm Bear operator: this is for **observational case study only**, not pilot. Total time: ~6-10 hours.

### Week 1 — Setup + first run (2 hours)

- Get Qwen API key via Bailian (or OpenAI key as fallback)
- Get Zep Cloud key (free tier)
- Clone + `npm run setup:all` + `npm run dev`
- Run live demo at https://666ghj.github.io/mirofish-demo/ (browser-only; no install)
- Run one local 10-round simulation with a public-opinion seed (cost: ~$1-5 USD)
- Goal: experience the 5-stage workflow end-to-end

### Week 2 — Architecture deep-dive (3 hours)

- Read `services/report_agent.py` (99 KB) — understand toolset structure
- Read `services/zep_tools.py` (66 KB) — understand memory-graph tool patterns
- Read `services/simulation_runner.py` (69 KB) — understand subprocess IPC
- Goal: extract architectural patterns (reflection-loop, tool-call structure, memory-graph integration) — these MAY be vault-applicable to skills/automation, but not directly

### Week 3 — Pattern Library reflection (2 hours)

- Compare MiroFish governance to vault governance — confirm Pattern #12 v42 refined fits
- Compare MiroFish license choice to vault license decision space — document outcome
- Compare MiroFish i18n strategy to vault i18n ambition (currently EN+VN bilingual)
- Goal: produce 1-2 page memo on "what MiroFish teaches Storm Bear about commercial-product positioning, even though we don't pilot it"

### Week 4 — Decision (1 hour)

- Decision: continue tracking MiroFish in corpus reference set OR drop
- If continue: monitor for v0.2 / v1.0 / Pro tier launch
- If drop: archive observation; deprioritize
- Goal: explicit decision recorded in `OPEN-QUESTIONS.md`

---

## 8. Ethical considerations / Cân nhắc đạo đức

**🇬🇧 EN**:
1. **Public opinion prediction** is a sensitive use case. Tools that simulate public opinion can be repurposed for influence campaigns. Don't use MiroFish to **plan** propaganda campaigns; only to **understand** likely public response to public information (policy drafts, news, etc.). The boundary matters.
2. **Personality + memory injection** for simulated agents based on real-world entity extraction creates digital effigies of real people. Be careful about whose data goes in. Public figures + public events = OK. Private individuals + private data = NOT OK without explicit consent.
3. **Financial prediction** is regulated in many jurisdictions. Outputs are NOT investment advice. Don't sell MiroFish predictions to retail traders. Don't trust them yourself.
4. **Novel ending simulation** (Dream of the Red Chamber demo) is creative-sandbox-OK. No ethical issues.

**🇻🇳 VN**:
1. **Dự đoán dư luận công chúng** là use case nhạy cảm. Công cụ mô phỏng dư luận có thể bị tận dụng cho chiến dịch ảnh hưởng. Đừng dùng MiroFish để **lập kế hoạch** chiến dịch tuyên truyền; chỉ để **hiểu** phản ứng dư luận với thông tin công khai (dự thảo chính sách, tin tức, v.v.). Ranh giới quan trọng.
2. **Inject tính cách + ký ức** cho agent ảo dựa trên trích xuất entity thực tế tạo ra hình nộm số của người thật. Cẩn thận với data đầu vào. Người công khai + sự kiện công khai = OK. Cá nhân riêng tư + data riêng tư = KHÔNG OK trừ khi có đồng ý rõ ràng.
3. **Dự đoán tài chính** bị quản lý ở nhiều nước. Output KHÔNG phải lời khuyên đầu tư. Đừng bán dự đoán MiroFish cho nhà đầu tư cá nhân. Đừng tự tin vào nó.
4. **Mô phỏng kết truyện tiểu thuyết** (demo Hồng Lâu Mộng) là creative-sandbox-OK. Không vấn đề đạo đức.

---

## 9. Comparison to corpus T5 peers

| T5 wiki | Domain | Storm Bear pilot |
|---------|--------|---|
| deer-flow v9 | research | observational |
| autoresearch v10 | ML training | observational |
| paperclip v14 | orchestration | observational |
| Skyvern v24 | browser automation | observational |
| OpenHands v30 | SWE | medium-high (#6) |
| DeepTutor v38 | education | high (#3 at v38) |
| browser-use v41 | browser automation hybrid | medium-high (#4 at v41) |
| rowboat v43 | personal productivity | high (#1 at v43) |
| shannon v45 | AI pentesting | low |
| **MiroFish v49** | **prediction-simulation** | **low (this guide)** |

MiroFish is the **9th-or-10th-priority T5 wiki** for Storm Bear pilot consideration. Most T5 wikis have higher direct utility for Scrum coaching role.

---

## 10. Architecture cheat sheet

```
User browser (Vue 3 SPA, port 3000)
    │ HTTP/axios
Flask backend (port 5001)
    ├── /api/graph        Stage 1: Knowledge graph from seed
    ├── /api/simulation   Stages 2-3-5: OASIS multi-agent sim lifecycle
    └── /api/report       Stages 4-5: ReportAgent + chat with agents

External services:
    ├── Zep Cloud         Memory graph (paid SaaS; pinned 3.13.0)
    ├── LLM (Qwen/etc.)   Vendor-agnostic via OpenAI SDK format
    └── OASIS subprocess  camel-oasis 0.2.5 + camel-ai 0.2.78 (multi-agent runtime)

Simulation platforms (hard-coded):
    ├── Twitter           6 actions
    └── Reddit            13 actions
```

---

## 11. Common pitfalls / Sai lầm thường gặp

1. **Running 40+ rounds on first try** — read README warning; start with 10
2. **Forgetting `ZEP_API_KEY`** — backend will silently fail at simulation stage; check `Config.validate()`
3. **Setting `LLM_BASE_URL` wrong** — Qwen via Bailian uses `https://dashscope.aliyuncs.com/compatible-mode/v1`; OpenAI direct uses `https://api.openai.com/v1`; check provider docs
4. **Deploying Docker container to public internet** — dev-mode runtime, not production-hardened; expose only behind nginx + auth
5. **Treating MiroFish as Scrum tool** — domain mismatch; you'll waste evaluation time
6. **Forking and modifying without considering AGPL-3.0** — derivative works distributed (incl. as network service) require source disclosure
7. **Using MiroFish predictions as decision input without statistical validation** — output is a sandbox interrogation tool, not validated forecast

---

## 12. References

- README EN: `00 Source/MiroFish/README.md`
- README ZH: `00 Source/MiroFish/README-ZH.md`
- LICENSE (AGPL-3.0): `00 Source/MiroFish/LICENSE`
- Backend deps: `00 Source/MiroFish/backend/pyproject.toml`
- Live demo: https://666ghj.github.io/mirofish-demo/
- CAMEL-AI / OASIS upstream: https://github.com/camel-ai/oasis
- Zep Cloud: https://app.getzep.com/
- Alibaba Bailian (Qwen): https://bailian.console.aliyun.com/
- Wiki entity pages: `02 Entity Pages/`
- Phase 4b deliverable (T5 10-way + Pattern strengthening): `04 Phase 4b Deliverable/`

---

## 13. Bottom line / Tóm lại

**🇬🇧 EN**: MiroFish is a serious, well-engineered multi-agent prediction-simulation app with credible commercial backing (Shanda Group), credible methodology lineage (CAMEL-AI / OASIS), and impressive viral traction (57K stars in 5 months). For Storm Bear's Scrum coaching role, it is **NOT a pilot candidate** — domain mismatch is fundamental. Treat it as a **valuable observational case study** for AGPL-3.0 commercial-product positioning, multi-agent simulation methodology, and i18n architecture lessons. Do NOT spend more than 6-10 hours evaluating it for vault use cases.

**🇻🇳 VN**: MiroFish là app dự đoán-mô phỏng đa-agent nghiêm túc, kỹ thuật tốt, có hậu thuẫn thương mại đáng tin (Shanda Group), lineage phương pháp đáng tin (CAMEL-AI / OASIS), và độ lan tỏa ấn tượng (57K sao trong 5 tháng). Với vai trò Scrum coach của Storm Bear, **KHÔNG phải candidate pilot** — domain lệch hoàn toàn. Coi như **case study quan sát có giá trị** về positioning sản phẩm thương mại AGPL-3.0, phương pháp mô phỏng đa-agent, và bài học kiến trúc i18n. ĐỪNG dành quá 6-10 giờ đánh giá nó cho use case của vault.
