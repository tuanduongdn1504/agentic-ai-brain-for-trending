# (C) Shannon — Hướng dẫn cho người mới bắt đầu (VN + EN)

> **Type:** Beginner bilingual published guide
> **Wiki:** shannon v45 (45th Storm Bear LLM Wiki)
> **Target:** [`KeygraphHQ/shannon`](https://github.com/KeygraphHQ/shannon) — "Shannon — AI Pentester by Keygraph"
> **⚠️ CRITICAL READ THIS FIRST:** Shannon là công cụ **tấn công thực sự** (not passive scanner). Đọc kỹ phần "2. Khung đạo đức + pháp lý" TRƯỚC KHI cài đặt.

---

## 1. Shannon là gì? / What is Shannon?

**VN:** Shannon là một **AI pentester tự động, white-box** cho web applications và APIs. Nó đọc mã nguồn (source code) của ứng dụng, xác định các điểm tấn công (attack vectors), rồi thực thi các exploit thật (SQLi, XSS, SSRF, bypass auth) để chứng minh lỗ hổng có thể khai thác **trước khi** chúng lên production. Nguyên tắc cốt lõi: *"POC or it didn't happen"* — chỉ vuln nào có exploit hoạt động mới được báo cáo.

**EN:** Shannon is an **autonomous, white-box AI pentester** for web applications and APIs. It reads your app's source code, identifies attack vectors, then executes real exploits (SQLi, XSS, SSRF, authentication bypass) to prove vulnerabilities are exploitable **before** they reach production. Core principle: *"POC or it didn't happen"* — only vulnerabilities with a working proof-of-concept exploit appear in the final report.

**Ra đời bởi:** Keygraph (commercial startup; [keygraph.io](https://keygraph.io/); SOC 2 Type I certified).

**Quy mô (2026-04-24):** 40.1K stars / 4.4K forks / 195 watchers / 17 open issues / AGPL-3.0 / TypeScript pnpm-workspaces monorepo / v1.1.0 (2026-04-21) / created ~16 months ago / Trendshift badge repository 15604.

---

## 2. ⚠️ KHUNG ĐẠO ĐỨC + PHÁP LÝ (bắt buộc đọc) / ETHICAL + LEGAL FRAMING (mandatory)

Shannon **KHÔNG PHẢI** một scanner passive. Nó **thực thi exploit thật sự** vào target — có thể tạo user, xóa data, phá session, inject payload. **Rủi ro pháp lý cao nếu dùng sai.**

### 2.1 Yêu cầu TUYỆT ĐỐI: Authorization (cấp phép)

**VN:** Bạn PHẢI có **sự cho phép rõ ràng, bằng văn bản** từ chủ sở hữu hệ thống target trước khi chạy Shannon.

- Quét và exploit hệ thống không thuộc sở hữu của bạn = **bất hợp pháp**
- Có thể bị truy tố theo luật như **Computer Fraud and Abuse Act (CFAA)** (Mỹ) hoặc các luật tương đương ở VN (Điều 288 BLHS về "đưa hoặc sử dụng trái phép thông tin mạng máy tính, mạng viễn thông")
- Keygraph **không chịu trách nhiệm** về việc sử dụng sai Shannon

**EN:** You **must have explicit, written authorization** from the target-system owner before running Shannon. Unauthorized scanning and exploitation = illegal under CFAA (US) or equivalent laws. Keygraph is not responsible for misuse.

### 2.2 KHÔNG chạy trên production

**VN:** README nói rõ: **"DO NOT run Shannon on production environments."**

- Shannon có thể: tạo user giả, sửa/xóa data, compromise test accounts, trigger side-effects từ injection
- Chỉ chạy trên: sandbox / staging / local dev (data không quan trọng)
- **Khuyến nghị:** chạy trong Virtual Machine (VM) để cô lập side-effects hoàn toàn

### 2.3 AGPL-3.0 derivative-disclosure

**VN:** Shannon Lite dùng license AGPL-3.0 — đây là license **copyleft nghiêm ngặt**.

- **Dùng nội bộ riêng tư:** OK, không cần share modifications
- **Cung cấp Shannon như SaaS / managed service cho khách hàng:** PHẢI open-source modifications

Nếu bạn build một SaaS bằng Shannon → phải public source code sửa đổi. Đọc kỹ [LICENSE file](https://github.com/KeygraphHQ/shannon/blob/main/LICENSE) (33.7 KB full AGPL-3.0 text).

### 2.4 Responsible disclosure (công bố trách nhiệm)

**VN:** Nếu Shannon phát hiện vuln ở ứng dụng của **bên thứ ba** (đã được ủy quyền test):

- **KHÔNG công bố public** ngay lập tức
- Báo vendor trước (coordinated disclosure)
- Cho vendor thời gian patch (thường 90 ngày)
- Chỉ công bố sau khi vendor release fix HOẶC sau timeline đã thông báo

### 2.5 Prompt injection risk

**VN:** Shannon đọc source code. Nếu bạn điểm nó vào **codebase độc hại** (untrusted/adversarial repo), kẻ xấu có thể inject prompt vào code comment / string → thao túng Shannon. **Chỉ chạy trên repo bạn sở hữu hoặc được ủy quyền.**

---

## 3. Tier trong Storm Bear corpus / Tier placement

**Shannon = T5 Agent-as-application — 9TH T5 ENTRANT với sub-archetype AI-pentester mới.**

- **T5 (Agent-as-application):** Framework là một autonomous agent standalone, user RUN như một complete application (không phải library, không phải education content).
- **9 T5 entrants (100% archetype-diversity):** deer-flow research / autoresearch ML / paperclip orchestration / Skyvern browser-automation / OpenHands SWE / DeepTutor education / browser-use browser-viral / rowboat personal-productivity / **shannon AI-pentester (NEW)**.

---

## 4. Shannon có 2 editions / Product Line

| Edition | License | Cho ai |
|---------|---------|--------|
| **Shannon Lite** (repo này) | AGPL-3.0 | Local testing của chính ứng dụng bạn |
| **Shannon Pro** | Commercial | Tổ chức cần AppSec platform toàn diện (SAST + SCA + secrets + business-logic + pentest correlated) |

**Hướng dẫn này tập trung vào Shannon Lite.** Shannon Pro cần inquire qua [Cal.com/team/keygraph/shannon-pro](https://cal.com/team/keygraph/shannon-pro).

---

## 5. Cài đặt / Installation (3 surfaces)

### 5.1 Prerequisites

- **Docker** (bắt buộc — worker image ~1 GB pull từ Docker Hub)
- **Node.js 18+** (cho npx)
- **pnpm** (nếu Clone+Build)
- **1 trong 5 AI provider:**
  - Anthropic API key (recommended) — [console.anthropic.com](https://console.anthropic.com)
  - Claude Code OAuth token
  - AWS Bedrock (bearer token)
  - Google Vertex AI (service account)
  - Custom Base URL (LiteLLM proxy — **"chỉ Claude models được support chính thức"**)

### 5.2 Surface 1: npx (khuyến nghị)

```bash
# Bước 1: Interactive wizard cấu hình credentials
npx @keygraph/shannon setup

# Hoặc export env var trực tiếp:
export ANTHROPIC_API_KEY=your-key

# Bước 2: Chạy pentest
npx @keygraph/shannon start -u https://your-app.com -r /path/to/your-repo
```

Shannon sẽ pull Docker image + start Temporal infra + launch ephemeral worker container.

### 5.3 Surface 2: Clone and Build (dev mode)

```bash
git clone https://github.com/KeygraphHQ/shannon.git
cd shannon

# Option A: tạo .env
cat > .env << 'EOF'
ANTHROPIC_API_KEY=your-api-key
CLAUDE_CODE_MAX_OUTPUT_TOKENS=64000
EOF

# Option B: export env vars
export ANTHROPIC_API_KEY="your-api-key"

pnpm install && pnpm build
./shannon start -u https://your-app.com -r /path/to/your-repo
```

### 5.4 Chạy local apps (localhost)

Docker containers không access được `localhost` trên host. Dùng `host.docker.internal`:

```bash
npx @keygraph/shannon start -u http://host.docker.internal:3000 -r /path/to/repo
```

### 5.5 Windows

**Chỉ support qua WSL2** — không support native Windows hoặc Git Bash.

```powershell
wsl --install
wsl --set-default-version 2
wsl --install Ubuntu-24.04
```

Enable Docker Desktop WSL2 backend → run Shannon inside WSL.

---

## 6. Cách hoạt động — 5-phase pipeline / How it works

```
Pre-Recon → Recon → [Vuln × 5 parallel] → [Exploit × 5 parallel] → Report
```

| Phase | Agents | Làm gì |
|-------|--------|--------|
| 1. Pre-Reconnaissance | 1 | Nmap + Subfinder + WhatWeb + source code analysis |
| 2. Reconnaissance | 1 | Attack surface map + browser exploration + code↔runtime correlation |
| 3. Vulnerability Analysis | 5 (parallel) | 5 agents (injection / xss / ssrf / auth / authz) hypothesize exploitable paths |
| 4. Exploitation | 5 (parallel) | Execute real PoCs; classify EXPLOITED / POTENTIAL / FALSE_POSITIVE |
| 5. Reporting | 1 | Consolidate validated findings; copy-paste PoCs |

**Pipelined-parallel:** vuln agent của 1 domain finish → exploit agent cùng domain start ngay (không đợi các vuln agent khác).

---

## 7. Workspaces + Resume

```bash
# Start với named workspace
npx @keygraph/shannon start -u <url> -r <repo> -w my-audit

# Resume (cùng command)
npx @keygraph/shannon start -u <url> -r <repo> -w my-audit

# List tất cả workspaces
npx @keygraph/shannon workspaces
```

Workspaces ở `./workspaces/` (local) hoặc `~/.shannon/workspaces/` (npx). Mỗi agent checkpoint via git commit → resume từ clean validated state.

**Monitor:**
- Temporal Web UI: `http://localhost:8233`
- `npx @keygraph/shannon logs <workspace>`
- `npx @keygraph/shannon status`

**Stop:**
- `npx @keygraph/shannon stop` (giữ workflow data)
- `npx @keygraph/shannon stop --clean` (full cleanup)

---

## 8. Configuration (optional YAML)

```yaml
# my-app-config.yaml
description: "Next.js e-commerce on PostgreSQL..."

authentication:
  login_type: form
  login_url: "https://your-app.com/login"
  credentials:
    username: "test@example.com"
    password: "yourpassword"
    totp_secret: "LB2E2RX7XFHSTGCK"  # 2FA auto-handled
  login_flow:
    - "Type $username into the email field"
    - "Type $password into the password field"
    - "Click the 'Sign In' button"
  success_condition:
    type: url_contains
    value: "/dashboard"

rules:
  avoid:
    - description: "AI should avoid testing logout"
      type: path
      url_path: "/logout"
  focus:
    - description: "AI should emphasize testing API endpoints"
      type: path
      url_path: "/api"

pipeline:
  retry_preset: subscription     # rate-limit safe
  max_concurrent_pipelines: 2    # 1-5, default 5
```

Chạy với `-c ./my-app-config.yaml`.

Support 4 login types: **form / SSO / API / basic**. TOTP auto qua `generate-totp` CLI.

---

## 9. Chi phí + thời gian / Cost & Performance

- **Thời gian:** 1-1.5 giờ / run (full pentest)
- **Chi phí API:** ~**$50 USD / run** (Claude Sonnet 4.5) — thay đổi theo model + app complexity
- **Docker resources:** worker image ~1 GB

**Tips tiết kiệm chi phí:**
- Dùng `--pipeline-testing` flag cho development testing (minimal prompts, 10s retries)
- Set `max_concurrent_pipelines: 2` trong config → giảm burst API usage
- `retry_preset: subscription` cho Anthropic subscription plans (6h backoff, 100 retries)

---

## 10. Shannon so sánh với T5 peers / vs other T5 frameworks

| Framework | Domain | License | Scale | Điểm khác biệt với Shannon |
|-----------|--------|---------|-------|---------------------------|
| [[Skyvern]] v24 | Browser automation | AGPL-3.0 | 21K | Workflow generalist; NOT security-focused |
| [[browser-use]] v41 | Browser-viral | MIT | 90K | Library-first; user writes automation code |
| [[OpenHands]] v30 | SWE coding | MIT | 72K | Writes code; Shannon attacks code (opposite) |
| [[DeepTutor]] v38 | Education | academic | YELLOW | Teaching not attacking |
| [[rowboat]] v43 | Personal productivity | — | — | Personal tasks not security |
| **shannon v45** | **AI-pentester** | **AGPL-3.0** | **40K** | **White-box + source-aware + POC-validated** |

**Shannon unique:** 5 attack domains × 2 phases = 10 parallel agents + code + runtime + "POC or didn't happen" discipline + OWASP WSTG alignment.

---

## 11. Storm Bear operator relevance (VN context)

**Direct pilot: LOW** (pilot ranking #12, lowest in corpus)

Storm Bear vault = markdown knowledge base, KHÔNG phải web app. Shannon không có target để test. **Hiện tại không áp dụng trực tiếp.**

**Observational value: MEDIUM-HIGH**

1. **Commercial playbook reference** — Keygraph's 2-tier open-core + Tower managed service = tham khảo nếu Storm Bear thương mại hóa Scrum Coach product trong tương lai
2. **Ethical product-positioning template** — 7-section disclaimer của Shannon = template cho commercial AI product positioning
3. **Architectural patterns** — Temporal.io + per-invocation task queue + git-checkpoint resume + Result<T,E> + prompt snapshots đáng quan sát
4. **"POC or it didn't happen" discipline** — mirror Pattern Library's N-observation promotion criteria
5. **XBOW benchmark rigor** — 96.15% hint-free result + full agent logs open = credibility signal

**Khi nào Shannon trở thành direct pilot:**
- Nếu Storm Bear phát triển web-app product (Scrum Coach SaaS, public wiki, client portal) → Shannon thành security-testing candidate
- 2-3 năm horizon, chưa immediate

---

## 12. Roadmap học Shannon trong 2-4 tuần (nếu muốn)

### Week 1: Setup + OWASP Juice Shop pilot

- Day 1-2: Read README + CLAUDE.md + SHANNON-PRO.md (overview)
- Day 3: Install Docker + Node.js + pnpm; setup Anthropic API key
- Day 4: `npx @keygraph/shannon setup`; dry-run với `--pipeline-testing`
- Day 5-7: Pull [OWASP Juice Shop](https://github.com/juice-shop/juice-shop) → run Shannon → compare với sample report (`sample-reports/shannon-report-juice-shop.md`)

### Week 2: Production-like target

- Day 8-10: Choose staging web app bạn sở hữu (hoặc [c{api}tal](https://github.com/Checkmarx/capital) / [crAPI](https://github.com/OWASP/crAPI))
- Day 11-12: Configure authentication.yaml với login flow
- Day 13-14: Full scan + review report

### Week 3-4 (advanced / optional)

- Day 15-17: Deep-dive `apps/worker/prompts/` — understand agent prompts
- Day 18-21: Experiment với custom rules (avoid/focus)
- Day 22-25: Study static-dynamic correlation concept (SHANNON-PRO.md) — whether Pro tier warranted
- Day 26-28: Contribute issue report nếu phát hiện limitation; join Discord community

**Total:** ~50 giờ practitioner time. **Chi phí API:** 4-6 runs × $50 = $200-300.

---

## 13. Giới hạn + Tradeoffs / Limitations

### Shannon Lite giới hạn

- **5 attack domains chỉ**: Injection / XSS / SSRF / Auth / Authz (không cover business-logic, vulnerable-deps, insecure-config)
- **LLM context windows**: phân tích có thể không exhaustive với large codebases
- **Chỉ Claude models officially supported** — alternative models may not reliably follow instructions
- **Không phải passive scanner** — mutative effects
- **Cần staging environment** — KHÔNG chạy production

### Cần Shannon Pro nếu muốn

- Full agentic SAST (data flow + point issues + business logic)
- SCA với reachability analysis
- Secrets detection với liveness validation
- Static-dynamic correlation pipeline
- CI/CD + GitHub PR scanning
- Self-hosted runner (customer data plane)
- Service boundary detection
- Compliance evidence (SOC 2 / HIPAA)

### Cần pentester người + DAST khác nếu

- Kiểm thử deep business-logic cụ thể domain
- Infrastructure-level pentest (network / cloud / physical)
- Red team exercises
- Social engineering / phishing tests

---

## 14. Resources + References

- **Repo:** [github.com/KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)
- **Company:** [keygraph.io](https://keygraph.io/)
- **Discord:** [discord.gg/9ZqQPuhJB7](https://discord.gg/9ZqQPuhJB7)
- **Twitter:** [@KeygraphHQ](https://twitter.com/KeygraphHQ)
- **Email:** [shannon@keygraph.io](mailto:shannon@keygraph.io)
- **Office Hours:** [Cal.com booking](https://cal.com/george-flores-keygraph/shannon-community-office-hours) (Thursdays, US/EU + Asia)
- **Shannon Pro Inquiry:** [Cal.com/team/keygraph/shannon-pro](https://cal.com/team/keygraph/shannon-pro)
- **XBOW benchmark:** [KeygraphHQ/xbow-validation-benchmarks](https://github.com/KeygraphHQ/xbow-validation-benchmarks)
- **Sample reports** (in repo): `sample-reports/shannon-report-juice-shop.md` / `shannon-report-capital-api.md` / `shannon-report-crapi.md`

---

## 15. Next action cho Storm Bear operator

**Với mức pilot relevance LOW:**

1. **KHÔNG cài Shannon ngay** (không có target web-app để test; cài đặt sẽ bị idle)
2. **Đọc README + SHANNON-PRO.md** như tham khảo commercial-playbook (30-45 phút)
3. **Ghi chú ethical-framing template** cho use case tương lai (15 phút)
4. **Re-evaluate** nếu Storm Bear phát triển web-app product trong tương lai

**Pilot ưu tiên cao hơn (xem [[Storm Bear 34th meta]]):**

1. claude-howto v32 (self-onboarding meta) — 13h weekend
2. spec-kit v17 (methodology) — 1 week
3. OMC v27 (multi-runtime orchestration) — 2-4h
4. claude-code-best-practice v34 (82 tips) — 6-8h
5. **v27 diagnostic HIGH bundle** (24 sessions deferred — BLOCKING-RECOMMENDATION) — next-highest-ROI operator work

---

**VN summary:** Shannon là T5 AI-pentester 9th entrant. KHÔNG phải pilot candidate cho Storm Bear (markdown vault, không có web-app target). Giá trị observational: commercial-playbook + ethical-framing template + architectural patterns. Đọc như reference; không cài đặt tại v45.

**EN summary:** Shannon is the 9th T5 entrant (AI-pentester sub-archetype). NOT a direct pilot for Storm Bear (markdown vault lacks web-app target). Observational value: commercial-playbook + ethical-framing template + architectural patterns. Read as reference; defer installation.
