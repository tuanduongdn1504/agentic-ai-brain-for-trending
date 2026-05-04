# Skyvern — Hướng dẫn cho người mới / Beginner Guide

> **Dành cho:** Developer / Scrum coach muốn automate browser workflows (Jira scraping, dashboard extraction, form filling) mà không viết brittle XPath selectors.
> **Scope note:** Skyvern là **T5 Agent-as-application** (autonomous browser agent). AGPL-3.0 + proprietary anti-bot creates licensing friction — đọc phần "Khi nào bạn cần" trước.

---

## 0. ⚠️ Đọc trước khi đi tiếp / Read this first

**VN:** Skyvern là tool hữu dụng cho specific usecase nhưng có 3 điểm cần biết:

1. **AGPL-3.0 license** — Nếu bạn deploy Skyvern như network service (SaaS hoặc internal team service), phải công bố source code. Cho personal/local use thì OK.
2. **Anti-bot measures chỉ có ở Skyvern Cloud** — OSS core không bypass Cloudflare/reCAPTCHA. Muốn tự động hóa commercial sites = phải trả tiền Skyvern Cloud ($).
3. **Chrome-only** — Firefox + Safari không support.

**Nếu bạn:**
- Chỉ cần scrape API-accessible data → dùng request/playwright trực tiếp (rẻ hơn)
- Cần automate internal company tools (no bot-detection) → **Skyvern OSS phù hợp**
- Cần automate commercial sites with bot-detection → **Skyvern Cloud required**
- Không OK với AGPL-3.0 → dùng Playwright + GPT-4V trực tiếp

**EN:** Skyvern is AGPL-3.0 + Chrome-only + anti-bot cloud-gated. Great for internal tools; friction for commercial client SaaS.

---

## 1. Skyvern là gì? / What is Skyvern?

**VN:** Skyvern là tool browser automation dùng **vision + LLM** thay vì DOM/XPath selectors. Extends Playwright.

Slogan: *"Automate Browser-based workflows using LLMs and Computer Vision."*

Cốt lõi:
- **Screenshot page → gửi LLM → LLM quyết định action** (thay vì `page.click('#login-btn')`)
- Resilient với UI changes (selector brittle ít phải sửa)
- 4 AI commands: **act / extract / validate / prompt**

**Benchmarks:**
- WebBench: 64.4% accuracy
- WebVoyager (Skyvern 2.0): 85.8%

**EN:** Skyvern uses vision + LLM for browser automation instead of XPath. Extends Playwright with 4 AI commands. WebBench 64.4% / WebVoyager 85.8%.

## 2. Khi nào bạn cần Skyvern / When you need it

### ✅ Dùng Skyvern khi:

- Scrape data từ tools không có API (legacy enterprise apps, old dashboards)
- Automate forms mà UI thay đổi liên tục (selector-based tool break liên tục)
- Cross-site automation (1 codebase cho nhiều sites)
- Natural-language task descriptions ("book a flight") = dễ handoff hơn low-level scripts

### ❌ KHÔNG dùng Skyvern khi:

- API có sẵn — dùng API rẻ + nhanh hơn
- High-frequency automation (latency LLM + cost)
- Real-time scraping (LLM too slow)
- Không OK với AGPL compliance
- Target site có anti-bot mà bạn không pay Cloud

### 🤔 MAYBE Skyvern khi:

- Scrum coach scraping Jira/Linear across teams → OSS OK (no anti-bot needed)
- Dashboard DORA metric collection → OSS OK
- Meeting notes extraction SaaS → phụ thuộc vào target site

## 3. 4 AI Page Commands — core abstraction

### `page.act(prompt)` — do something

```python
await page.act("Click the login button")
await page.act("Fill the email field with user@example.com")
```

### `page.extract(prompt, schema)` — scrape structured data

```python
data = await page.extract(
    "Extract all product names and prices",
    schema={"products": [{"name": "string", "price": "number"}]}
)
```

### `page.validate(prompt)` — check page state

```python
is_logged_in = await page.validate("Is the user logged in?")
```

### `page.prompt(prompt, schema)` — arbitrary LLM query

```python
analysis = await page.prompt(
    "What is this page about?",
    schema={"topic": "string", "sentiment": "string"}
)
```

### Higher-level methods

```python
await page.agent.run_task("Book a flight from SFO to NYC on March 15")
await page.agent.login(url="...", credentials={...})
await page.agent.download_files(...)
await page.agent.run_workflow("my_workflow_id")
```

## 4. Installation — 3 options

### Option 1 — pip (khuyến nghị)

```bash
pip install skyvern
skyvern quickstart
```

Requirements:
- Python 3.11.x (3.12 OK, 3.13 không support)
- Node.js + npm
- Windows: cần Rust + VS Code C++ dev tools

### Option 2 — Docker Compose

```bash
pip install skyvern && skyvern quickstart
# Select "Docker Compose" at prompt
# Open http://localhost:8080
```

### Option 3 — Skyvern Cloud (paid)

```
https://app.skyvern.com
```

Includes:
- Parallel execution
- **Anti-bot detection bypass** (Cloudflare, reCAPTCHA, DataDome)
- Proxy networks
- CAPTCHA solvers

## 5. Workflow Builder — 10+ block types

| Block | Purpose |
|-------|---------|
| Browser Task | High-level task |
| Action | Low-level click/type |
| Data Extraction | Scrape structured data |
| Validation | Check page state |
| For Loops | Iterate over lists |
| File Parsing | Parse PDF/CSV |
| Email Sending | SMTP/API email |
| HTTP Request | Call external APIs |
| Custom Code | Python/JS |
| File Upload | Block storage upload |
| Conditionals | (Coming soon) |

## 6. Multi-LLM support

Skyvern supports 10+ LLM providers:

| Provider | Models |
|----------|--------|
| OpenAI | GPT-5, GPT-4.1, o3, o4-mini |
| Anthropic | Claude 4, Claude 4.5 |
| Azure OpenAI | Same as OpenAI |
| AWS Bedrock | Multiple |
| Google Gemini | Gemini models |
| Ollama | Local (privacy-first) |
| OpenRouter | Aggregated |
| OpenAI-compatible endpoints | Any (fallback) |

## 7. Authentication + integrations

### Password managers

- ✅ Bitwarden
- ✅ Custom HTTP credential service
- ❌ 1Password (unsupported)
- ❌ LastPass (unsupported)

### 2FA

- QR-based (Google Authenticator, Authy)
- Email-based
- SMS-based

### Workflow platforms

- Zapier
- Make.com
- N8N

## 8. Pricing & licensing

### OSS (self-hosted)

- Free
- AGPL-3.0 — source disclosure required nếu deploy SaaS

### Skyvern Cloud

- Paid (check app.skyvern.com for current pricing)
- Includes anti-bot + proxy + CAPTCHA
- Pricing varies by usage

## 9. Ecosystem context

### Comparison với other browser agents

| Framework | License | Approach |
|-----------|---------|----------|
| Playwright / Puppeteer / Selenium | Apache / BSD | DOM-based |
| Skyvern | AGPL-3.0 | Vision + LLM |
| browser-use (external) | MIT | Vision + LLM |
| Agent-E / LaVague | MIT | Vision + LLM variants |
| UiPath / Power Automate | Proprietary | Record-replay |

Skyvern's AGPL choice distinguishes from MIT peers.

### Intellectual lineage

> *"Skyvern was inspired by the Task-Driven autonomous agent design popularized by BabyAGI and AutoGPT"*

## 10. Lộ trình 4 tuần / 4-week roadmap

### Tuần 1 — Orient + install

- [ ] Đọc README + cluster summaries
- [ ] Install `pip install skyvern` + `skyvern quickstart`
- [ ] Chạy ví dụ workflow đơn giản (1 form fill)
- [ ] Quyết định: OSS self-host vs Cloud trial

### Tuần 2 — First automation

- [ ] Chọn use case nhỏ (VD: scrape 1 Jira board status)
- [ ] Viết `page.extract(...)` với schema định nghĩa rõ
- [ ] Test manually 3-5 lần để observe LLM behavior
- [ ] Log costs + latency (benchmark tự làm)

### Tuần 3 — Workflow builder

- [ ] Thử workflow builder: loops + extraction + validation
- [ ] Integrate với Zapier/N8N nếu phù hợp
- [ ] Setup 2FA + password manager nếu cần auth
- [ ] Document workflow template reusable

### Tuần 4 — Evaluate + decide

- [ ] So sánh cost/time vs manual/API
- [ ] Nếu cần anti-bot: thử Cloud trial
- [ ] AGPL compliance review nếu deploy team-wide
- [ ] Decide: continue / abandon / consolidate với existing tools

## 11. Storm Bear operator relevance / Mức độ phù hợp

**VN:** Storm Bear operator (Scrum coach + developer):

**Potential use cases:**
1. Jira/Linear scraping across teams
2. DORA metric dashboard extraction
3. Retrospective data aggregation
4. Enterprise SaaS without API scraping

**Trở ngại:**
- AGPL-3.0 complexity cho team-wide deployment
- Anti-bot gated to Cloud (paid)
- Chrome-only

**Verdict: MEDIUM relevance.**
- ✅ Tool legitimate, actively maintained
- ✅ Direct utility cho metric collection
- ⚠️ Licensing friction cho client-facing
- ⚠️ Cost consideration nếu target sites có anti-bot

**Action:** Potential pilot cho internal use; avoid client-facing deployment without AGPL audit.

**EN:** Medium relevance for Storm Bear. Utility for Scrum metric collection; AGPL + anti-bot friction for commercial client work.

## 12. Next actions

**Nếu bạn là developer muốn try:**
1. `pip install skyvern && skyvern quickstart` — 15 phút có demo working
2. Pick 1 use case cụ thể + write workflow

**Nếu bạn là Storm Bear operator:**
1. Decide: OSS internal use vs avoid entirely
2. If OSS: pilot 1 metric-collection workflow
3. AGPL review trước khi deploy team-wide

**Nếu bạn compare với alternatives:**
1. Check browser-use (MIT) — licensing-friendlier alternative
2. Check if Playwright + raw GPT-4V đủ cho use case

## 13. References

- Skyvern GitHub: github.com/Skyvern-AI/skyvern
- Homepage: skyvern.com
- Cloud: app.skyvern.com
- Discord: discord.gg/fG2XXEuQX3
- Twitter: @skyvernai
- Technical report: skyvern.com/blog (Skyvern 2.0)

---

**Skyvern = vision + LLM browser automation (4 AI commands: act/extract/validate/prompt). WebBench 64.4% / WebVoyager 85.8%. AGPL-3.0 OSS + Skyvern Cloud proprietary anti-bot moat. T5 browser-automation specialty — first domain-specific T5 in corpus. Storm Bear: MEDIUM relevance (utility for Scrum metrics, AGPL friction).**
