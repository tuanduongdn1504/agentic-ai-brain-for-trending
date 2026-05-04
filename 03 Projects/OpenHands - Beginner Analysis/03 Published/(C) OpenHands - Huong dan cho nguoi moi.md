# (C) OpenHands — Hướng dẫn cho người mới / Beginner's Guide

> **Dự án:** [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)
> **Loại:** T5 Agent-as-application — autonomous SWE agent framework
> **Wiki version:** v30 (30th trong Storm Bear corpus)
> **Target reader:** developer + Storm Bear operator đang cân nhắc OpenHands cho Scrum coaching / engineering augmentation
> **Date:** 2026-04-22

---

## Phần 1. OpenHands là gì? / What is OpenHands?

**VN:** OpenHands (trước đây tên OpenDevin) là một **autonomous software engineering agent** — tức là một AI có thể viết code, chạy lệnh shell, browse web, dùng VS Code và IDE như một developer thật. Không giống như Claude Code hay Cursor (là **coding assistants** plugin trong IDE), OpenHands là một **standalone application** — bạn mô tả task, nó tự làm từ đầu đến cuối.

Công ty đứng sau là **All Hands AI** (startup huy động được $18.8M). Ba co-founder:
- **Xingyao Wang** — PhD candidate tại UIUC, đóng góp SWE-bench research
- **Graham Neubig** — Giáo sư tại CMU (Carnegie Mellon)
- **Robert Brennan** — software engineer

**EN:** OpenHands (formerly OpenDevin) is an **autonomous software engineering agent** — an AI that can write code, run shell commands, browse the web, use VS Code and IDEs like a human developer. Unlike Claude Code or Cursor (IDE-plugin coding assistants), OpenHands is a **standalone application** — you describe a task, it executes end-to-end.

The company behind it is **All Hands AI** ($18.8M funded). Three co-founders: Xingyao Wang (UIUC PhD candidate + SWE-bench contributor), Graham Neubig (CMU Professor), Robert Brennan (software engineer).

---

## Phần 2. Con số / The numbers

| Metric | Value |
|--------|-------|
| GitHub stars | **71,704** (top 5 trong Storm Bear corpus) |
| Forks | 9,030 |
| License | **MIT core** + separate-license enterprise directory |
| Tech stack | Python 71.4% + TypeScript 26.8% |
| Tuổi | ~25 tháng (created 2024-03-13) |
| Releases | **101 releases** — active velocity |
| Contributors | 188+ (theo ICLR 2025 paper) |
| SWE-Bench Verified | **77.6** (top OSS SWE agent) |
| Papers | ICLR 2025 + arXiv Nov 2025 SDK paper |

Là 1 trong những SWE-agent open-source được đầu tư và publish nghiêm túc nhất hiện nay.

---

## Phần 3. Quickstart — chạy thử / Quickstart

### 3.1 Docker (khuyên dùng nhất / most recommended)

**VN:**
```bash
# Pull và chạy Docker image
docker run -it --rm --pull=always \
    -e SANDBOX_RUNTIME_CONTAINER_IMAGE=docker.all-hands.dev/all-hands-ai/runtime:0.15-nikolaik \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v ~/.openhands-state:/.openhands-state \
    -p 3000:3000 \
    --add-host host.docker.internal:host-gateway \
    --name openhands-app \
    docker.all-hands.dev/all-hands-ai/openhands:0.15

# Truy cập GUI tại http://localhost:3000
```

Yêu cầu: Docker Desktop (Mac/Windows) hoặc Docker Engine (Linux) + LLM API key (Anthropic, OpenAI, Minimax, v.v.).

**Lưu ý:** versions thực tế có thể đã thay đổi. Check README mới nhất tại github.com/OpenHands/OpenHands để có command chính xác.

**EN:** Use Docker with LLM API key. Exact version tags change — always check the README for current `docker run` invocation.

### 3.2 CLI (cho developer quen terminal / terminal-native)

**VN:** CLI mode tương tự Claude Code — gõ lệnh vào terminal, agent trả lời + thực thi. Install qua package managers (pip / uv). Chi tiết trong docs.openhands.dev.

**EN:** CLI mode analogous to Claude Code. Install via pip/uv. See docs.openhands.dev for the canonical install command.

### 3.3 Cloud tier (miễn phí / free)

**VN:** Vào openhands.dev → đăng nhập GitHub hoặc GitLab → dùng free tier với Minimax LLM. Không cần cài Docker locally.

**EN:** Visit openhands.dev, log in via GitHub/GitLab, use free Cloud tier with Minimax-powered LLM. No local Docker required.

---

## Phần 4. Kiến trúc cốt lõi / Core architecture

### Action-Observation agent loop

```
User task (NL) → Perception (files/terminal/browser/IDE)
  → Action selection (LLM picks: shell / file edit / browser / IDE op)
  → Security analysis (pre-execution review)
  → Sandboxed execution (Docker container)
  → Observation (result → LLM context)
  → Loop or halt
```

**VN:** Agent tự lập kế hoạch + thực thi trong Docker container cách ly. Nếu LLM generate một lệnh nguy hiểm (`rm -rf /`), security analysis review trước khi chạy.

**EN:** Agent plans + executes in isolated Docker container. Dangerous LLM-generated commands are security-reviewed pre-execution.

### 5 deployment surfaces / 5 interface
1. **SDK** (Python library — BYO agent)
2. **CLI** (terminal-native)
3. **Local GUI** (desktop app với REST API + React)
4. **Cloud** (openhands.dev hosted)
5. **Enterprise** (self-hosted Kubernetes + RBAC)

Chọn surface phù hợp:
- Solo developer thử: **CLI hoặc Local GUI**
- Team workflow: **Cloud free tier** hoặc **Enterprise**
- Build custom agent: **SDK**

---

## Phần 5. 4 pre-built workflows / 4 pre-built workflows

OpenHands cung cấp 4 workflow mặc định (trên openhands.dev):

1. **Fix Vulnerabilities** — quét repo, tìm CVE/pattern không an toàn, propose PR patches
2. **Review PRs** — phân tích diff, suggest improvements (security / performance / style)
3. **Migrate Code** — refactor lớn (framework migration, API version bump)
4. **Triage Incidents** — parse incident alerts, propose investigation + remediation

**VN — cho Storm Bear Scrum coach:**
- "Review PRs" → tự động review trong Scrum engineering team retro
- "Triage Incidents" → phân tích incident cho retrospective meeting
- "Fix Vulnerabilities" → security audit cho VN client
- "Migrate Code" → advisory cho client modernization project

**EN — for Storm Bear Scrum coach:**
- Review PRs → automated engineering-team code review
- Triage Incidents → post-incident retrospective input
- Fix Vulnerabilities → security audit for VN clients
- Migrate Code → modernization advisory

---

## Phần 6. LLM support / LLM providers

OpenHands là **model-agnostic** — hỗ trợ:
- **Claude** (Anthropic)
- **GPT** (OpenAI)
- **Minimax** (dùng trong free Cloud tier)
- **Other LLMs** qua SDK routing layer

**VN:** Bạn chọn provider và mô hình. Chi phí: theo token của provider. Claude Sonnet 4.x / GPT-5 / Minimax — đều chạy được.

**EN:** BYO LLM provider. Choose Claude / GPT / Minimax / etc. Cost = provider's per-token rate.

---

## Phần 7. SWE-Bench 77.6 — có ý nghĩa gì? / What does SWE-Bench 77.6 mean?

**VN:** SWE-Bench Verified là benchmark khó nhất hiện tại cho AI coding agents — đánh giá 2,294 GitHub issues thực tế từ 12 Python repos. Agent phải đọc codebase, hiểu vấn đề, fix bug, và pass unit tests thực. **77.6% resolution rate** là state-of-the-art cho OSS (đầu 2026). Con số này được track công khai qua Google Sheet mà ai cũng xem được.

**So sánh với Storm Bear corpus:**
- v17 spec-kit: 48× productivity claim (blog)
- v22 LlamaFactory: ACL 2024 peer-reviewed
- v24 Skyvern: WebBench 64.4% (browser-specific)
- **v30 OpenHands: SWE-Bench Verified 77.6 (SWE-specific top-tier)**

**EN:** SWE-Bench Verified = top-tier benchmark for AI coding agents (2,294 real GitHub issues, 12 Python repos). OpenHands' **77.6%** resolution rate is OSS state-of-the-art as of early 2026. Publicly tracked via live Google Sheet.

---

## Phần 8. Khi nào dùng / khi nào không / When to use / when not

### Dùng OpenHands khi / Use when:

- Bạn cần một AI agent tự làm end-to-end SWE task (không phải assistant trong IDE)
- Bạn đã có Docker + thoải mái với containerized tooling
- Bạn có LLM API key (Anthropic / OpenAI / etc.) và budget cho tokens
- Team muốn pre-built workflows (PR review / incident triage / code migration)
- Muốn build custom agent nhưng không muốn build từ scratch

### Không dùng OpenHands khi / Don't use when:

- Bạn chỉ cần autocomplete trong IDE (dùng Copilot / Cursor / Claude Code)
- Bạn không muốn / không thể chạy Docker
- Project là front-end small-scale không cần autonomous agent
- Cần Vietnamese localization native (OpenHands English-only ở docs)
- VN client có compliance requirements chặt về data sovereignty → enterprise self-hosted cần setup chu đáo

---

## Phần 9. Storm Bear operator context / Storm Bear bối cảnh

### Vị trí pilot ranking v30

1. spec-kit v17 (methodology)
2. OMC v27 (Scrum-ceremony alignment)
3. BMAD v11 (VN methodology)
4. markitdown v28 (doc ingestion utility)
5. crawl4ai v29 (web research utility)
6. **OpenHands v30 🆕 (SWE-agent platform)**
7. gws v13
8. codymaster v12

**VN:** OpenHands là #6 trong pilot ranking. Không cao hơn vì có learning curve đáng kể (Docker + SDK + LLM cost management). Nên deploy **sau khi** operator đã có methodology (spec-kit / BMAD / OMC) và ingestion flows (markitdown / crawl4ai) stable.

**Workflow matching:**
- Scrum engineering team PR reviews → Review PRs workflow
- Retrospective incident analysis → Triage Incidents workflow
- VN client security audit → Fix Vulnerabilities workflow
- Modernization advisory → Migrate Code workflow

### Caveats cho VN operator

- Docs English-only; cần tự viết VN system prompt cho Scrum context
- Docker + 315 MB repo — laptop thấp specs có thể chậm
- LLM API cost accumulates — quản lý budget kỹ
- Academic-commercial fusion entity — stability trung bình (3 co-founder + $18.8M funding)
- Commercial-tier boundaries không rõ từ docs hiện tại → cần dig trước khi recommend cho VN client

---

## Phần 10. Roadmap 4-tuần / 4-week roadmap

### Tuần 1: Install + baseline
- Cài Docker + pull OpenHands image
- Chạy "Hello World" agent — ask it to modify a simple Python script
- Set up LLM API key (Anthropic recommended for quality/latency)
- Đọc arXiv 2407.16741 (ICLR 2025 paper) — architecture understanding

### Tuần 2: Pre-built workflows
- Thử Review PRs workflow trên 1 Storm Bear vault PR
- Thử Triage Incidents workflow với 1 past incident doc
- Document learnings — what worked / what didn't / token cost

### Tuần 3: Custom Scrum-coach agent
- Sử dụng SDK để build minimal VN-Scrum-coach agent
- System prompt: Scrum ceremony context + VN cultural context
- Task: analyze team retro notes → identify themes → propose action items

### Tuần 4: Client pilot assessment
- Decide: move to Cloud tier? Stay OSS self-hosted? Build custom on SDK?
- If VN client interested → enterprise tier evaluation + compliance check
- Document total 4-week learnings for Storm Bear vault

---

## Phần 11. Cross-references trong Storm Bear corpus

### T5 peers (autonomous agent applications)
- [v9 deer-flow](../../deer-flow%20-%20Beginner%20Analysis/) — research agent (ByteDance)
- [v10 autoresearch](../../autoresearch%20-%20Beginner%20Analysis/) — ML research (Karpathy solo)
- [v14 paperclip](../../paperclip%20-%20Beginner%20Analysis/) — orchestration (community)
- [v24 Skyvern](../../Skyvern%20-%20Beginner%20Analysis/) — browser automation (commercial)

### Research-paper-chain peers (Pattern #32)
- [v20 fish-speech](../../fish-speech%20-%20Beginner%20Analysis/) — TTS 2-paper chain
- [v22 LlamaFactory](../../LlamaFactory%20-%20Beginner%20Analysis/) — ACL 2024 + ecosystem chain
- [v23 Unsloth](../../Unsloth%20-%20Beginner%20Analysis/) — narrower chain

### Open-core commercial peers (Pattern #31)
- v20 fish-speech (foundation-model)
- v24 Skyvern (browser)
- **v30 OpenHands (SWE-agent) ✅ N=3**

---

## Phần 12. Đánh giá honest / Honest assessment

**Pros:**
- Academic credibility (ICLR 2025 + CMU faculty co-founder + UIUC PhD + multi-institutional paper)
- Commercial stability ($18.8M funding + 3 co-founders + 101 releases + 188+ contributors)
- MIT core license (permissive, allows commercial derivative)
- State-of-the-art SWE-Bench Verified 77.6
- Named enterprise adoption (TikTok / Amazon / Netflix / Google / NVIDIA / Apple)
- Production-grade SDK formalized in Nov 2025 paper

**Cons:**
- Docker dependency (315 MB)
- Benevolent-dictator governance — continuity depends on 3-person core
- No native Vietnamese docs
- Enterprise-tier commercial boundaries unclear from public docs
- LLM API cost accumulates with heavy use
- Newer T5 sub-type (SWE-agent) = less corpus evidence for long-term stability

**Verdict (VN operator):** Good long-term platform bet, Medium-priority pilot at v30 (#6). Deploy after methodology + ingestion utilities are stable. Production-ready, not experimental.

---

## Phần 13. Tài nguyên / Resources

- **GitHub:** github.com/OpenHands/OpenHands
- **Docs:** docs.openhands.dev
- **Company:** openhands.dev
- **Community Slack:** dub.sh/openhands
- **ICLR 2025 paper:** arXiv 2407.16741
- **SDK paper:** arXiv 2511.03690
- **SWE-Bench live leaderboard:** link from README badge

**Storm Bear internal:**
- [Project CLAUDE.md](../CLAUDE.md)
- [Wiki index](../02%20Wiki/(C)%20index.md)
- [T5 5-way comparison Phase 4b](./(C)%20T5%205-way%20comparison%20+%20Pattern%20implications%20+%20candidates.md)

---

**Shipped 2026-04-22 as v30 Storm Bear corpus entry. 12th v2 routine execution. Post-audit-clean first wiki. T5 extends to N=5.**
