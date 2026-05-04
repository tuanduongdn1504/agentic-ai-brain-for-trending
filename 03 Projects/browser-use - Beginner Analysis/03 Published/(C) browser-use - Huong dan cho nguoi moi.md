# (C) browser-use — Hướng dẫn cho người mới / Beginner's Guide

> **Song ngữ VN + EN.** browser-use (89.9K sao) là open-source Python agent tự động hoá browser, do Magnus (Zurich) + Gregor (San Francisco) xây dựng với Browser-Use Cloud làm tier thương mại. Wiki v41, Storm Bear corpus.

---

## Phần 1 — It is what? / browser-use là gì?

**EN:** browser-use is an **async Python library** that turns natural-language instructions into autonomous browser automation. You write `Agent(task="Find top Hacker News post")`, and an LLM drives a real Chromium browser to complete that task step-by-step, clicking buttons and filling forms, using **hybrid DOM+vision** (element indices + screenshots).

**VN:** browser-use là **thư viện Python async** biến chỉ dẫn tiếng tự nhiên thành tự động hoá browser. Bạn viết `Agent(task="Tìm bài viết top Hacker News")`, và một LLM sẽ điều khiển Chromium thật để hoàn thành task đó từng bước — click nút, điền form — sử dụng **kiến trúc lai DOM+vision** (chỉ số element + ảnh chụp màn hình).

**Positioning verbatim:** *"🌐 Make websites accessible for AI agents. Automate tasks online with ease."* — *"Tell your computer what to do, and it gets it done."*

---

## Phần 2 — Corpus-first signals

**Tại sao wiki này quan trọng trong Storm Bear corpus (41 wiki):**

1. **7th T5 entrant + 2nd browser T5** — tạo **N=2 structural pair với Skyvern v24** (2 kiến trúc browser-automation đối lập trong cùng tier)
2. **Pattern #48 PROMOTES to CONFIRMED** — anti-bot/CAPTCHA/stealth bị gate sau Cloud commercial tier (giống Skyvern), structurally-unambiguous N=2
3. **Pattern #47 REFINED via counter-evidence** — hybrid DOM+vision là **điểm thứ 3** trên spectrum (vision-primary Skyvern / hybrid browser-use / DOM-only crawl4ai)
4. **Pattern #46 Duo-Founder UN-STALES** — Magnus+Gregor (Zurich/SF) nối tiếp Han brothers (Unsloth), N=2 structurally
5. **5 consecutive zero-new-active-candidate streak** (v37/v38/v39/v40/v41) — consolidation-forward discipline mạnh
6. **Corpus-first physical merchandise** (browsermerch.com) tại T5 open-core
7. **Corpus-first embedded CLOUD.md** 73.4KB ở repo root (chung với AGENTS.md 37.4KB = ~110KB LLM-context)
8. **Corpus-first `@sandbox` decorator** = zero-friction OSS→Cloud migration
9. **Corpus-first bidirectional MCP** (server + client) + DXT packaging
10. **Corpus-first dual-API v2+v3** active-maintenance + Python+TypeScript SDK song song
11. **Corpus-largest 15-native-LLM-providers + LiteLLM** = ~115 provider surface
12. **Corpus-first MIT + 89.9K scale** tại open-core T5 (license permissiveness cao nhất trên scale lớn nhất open-core)

---

## Phần 3 — Tier placement

**Tier 5 Agent-as-application** — browser-use là standalone autonomous agent hoàn thành task đầy đủ (không phải bridge, không phải education, không phải service-platform).

**Distinct from:**
- **Skyvern v24** (browser T5 N=1): cùng tier + cùng domain + commercial-entity archetype, nhưng **AGPL-3.0** + **vision-primary** architecture + 21.3K stars
- **deer-flow v9 / autoresearch v10 / paperclip v14 / OpenHands v30 / DeepTutor v38**: cùng tier, khác archetype + khác domain

**Archetype: Commercial-startup + open-core + MIT + 2-founder team (Zurich + SF)** — khác với corporate (ByteDance v9), solo (Karpathy v10), community-platform (paperclip v14), academic-commercial-fusion (OpenHands v30), academic-lab (DeepTutor v38).

---

## Phần 4 — Installation / Cài đặt

### Local OSS install (free, BYO LLM API key)

```bash
# EN: Install uv (modern Python packaging)
# VN: Cài uv (công cụ packaging Python hiện đại)
pip install uv
uv venv --python 3.12
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# EN: Install browser-use + Chromium
# VN: Cài browser-use + Chromium
uv pip install browser-use
uvx browser-use install

# EN: Configure LLM API key (choose one)
# VN: Cấu hình API key LLM (chọn 1)
cat > .env <<EOF
# Option A: Browser Use Cloud (5 free tasks + best accuracy)
BROWSER_USE_API_KEY=your-key

# Option B: Anthropic Claude
# ANTHROPIC_API_KEY=your-key

# Option C: OpenAI
# OPENAI_API_KEY=your-key

# Option D: Google Gemini (free tier)
# GOOGLE_API_KEY=your-key
EOF
```

### Get Browser-Use Cloud API key

Visit `https://cloud.browser-use.com/new-api-key` → create account → get 5 free tasks + API key.

**VN:** Vào `https://cloud.browser-use.com/new-api-key` → tạo tài khoản → nhận 5 task miễn phí + API key.

### Docker install (alternative)

```bash
# EN: If you prefer Docker
# VN: Nếu thích Docker
docker pull browser-use/browser-use:latest
docker run --rm -e BROWSER_USE_API_KEY=... browser-use/browser-use:latest "your-task-here"
```

### Template quickstart (CLI-generated starter)

```bash
uvx browser-use init --template default   # Minimal starter
uvx browser-use init --template advanced  # All config options commented
uvx browser-use init --template tools     # Custom tools examples
```

---

## Phần 5 — Core usage pattern / Pattern sử dụng cơ bản

### The minimal example (5 lines)

```python
from browser_use import Agent, ChatBrowserUse
import asyncio

async def main():
    agent = Agent(task="Find the top Hacker News post", llm=ChatBrowserUse())
    await agent.run()

asyncio.run(main())
```

**Breakdown:**
- **Task** = plain English (or VN — LLM hiểu cả)
- **LLM** = provider adapter (ChatBrowserUse recommended — fastest + cheapest + most accurate)
- **agent.run()** = runs step-by-step; each step: read page → decide action → execute → verify

### With Browser configuration

```python
from browser_use import Agent, Browser, ChatBrowserUse

browser = Browser(
    headless=False,           # Hiển thị cửa sổ (debug)
    window_size={'width': 1200, 'height': 800},
    # use_cloud=True,         # Dùng Cloud browser (stealth + anti-bot)
    # allowed_domains=['jira.mycompany.com'],  # Giới hạn domain (security)
)

agent = Agent(
    task="Log into Jira and extract sprint-42 velocity",
    browser=browser,
    llm=ChatBrowserUse(),
)
```

### Custom tools (extend agent capabilities)

```python
from browser_use import Agent, Tools

tools = Tools()

@tools.action(description='Fetch 2FA code from authenticator app')
async def get_2fa_code():
    # Call your password manager / authenticator
    return "123456"

agent = Agent(
    task="Login to Jira with 2FA using get_2fa_code action",
    tools=tools,
    llm=ChatBrowserUse(),
)
```

### Structured output (Pydantic schema)

```python
from pydantic import BaseModel

class SprintReport(BaseModel):
    sprint_id: str
    completed_points: int
    planned_points: int
    story_count: int

agent = Agent(
    task="Extract Sprint-42 report from Jira",
    output_model_schema=SprintReport,
    llm=ChatBrowserUse(),
)

history = await agent.run()
report: SprintReport = history.structured_output  # Type-safe!
```

### CLI persistent-browser workflow

```bash
# EN: Browser stays open between commands (~50ms latency)
# VN: Browser giữ nguyên giữa các lệnh (~50ms latency)
browser-use open https://news.ycombinator.com
browser-use state                       # Xem các element clickable + index
browser-use click 5                      # Click vào element index 5
browser-use get text 10                  # Lấy text của element 10
browser-use screenshot page.png          # Chụp màn hình
browser-use close                        # Đóng browser
```

---

## Phần 6 — Novel concepts / Khái niệm đặc trưng

### 1. Hybrid DOM+Vision architecture

**EN:** Agent sees **both** DOM tree (element indices) **and** screenshots (visual layout). DOM gives stable element IDs; screenshot gives disambiguation for visually-similar elements.

**VN:** Agent nhìn thấy **cả** DOM tree (chỉ số element) **và** screenshot (layout). DOM cung cấp ID ổn định; screenshot giúp phân biệt các element trông giống nhau.

**Toggle:**
```python
Agent(use_vision=True)      # Always screenshots
Agent(use_vision='auto')    # Screenshots only when agent requests (default)
Agent(use_vision=False)     # DOM-only (fastest, cheapest)
```

### 2. `@sandbox` decorator — OSS→Cloud 1-line migration

```python
from browser_use import Browser, sandbox, ChatBrowserUse

@sandbox(cloud_profile_id='jira-auth-profile')  # Runs on Cloud
async def sprint_report(browser: Browser):
    agent = Agent(task="Extract Sprint-42 report", browser=browser, llm=ChatBrowserUse())
    await agent.run()

asyncio.run(sprint_report())
```

Cùng 1 function chạy local (không decorator) hay production Cloud (có decorator). **Corpus-first T5.**

### 3. Profile Sync (Chrome cookies → Cloud)

```bash
# EN: Upload local Chrome profile to Cloud (preserves login/cookies)
# VN: Upload profile Chrome cục bộ lên Cloud (giữ đăng nhập/cookies)
export BROWSER_USE_API_KEY=your-key
curl -fsSL https://browser-use.com/profile.sh | sh
# -> Interactive: log into services you need → you get profile_id
```

Sau đó dùng trong `@sandbox(cloud_profile_id='your-profile-id')`.

### 4. 15 LLM providers + LiteLLM (115 total)

```python
from browser_use import Agent, ChatBrowserUse, ChatAnthropic, ChatOpenAI, ChatGoogle
# + ChatOllama, ChatGroq, ChatCerebras, ChatDeepSeek, ChatMistral, 
# + ChatOpenRouter, ChatVercel, ChatAzureOpenAI, ChatBedrock, ChatOCI

agent = Agent(
    task="...",
    llm=ChatAnthropic(model='claude-sonnet-4-6'),
    # llm=ChatGoogle(model='gemini-3-flash-preview'),
    # llm=ChatOpenAI(model='gpt-4.1-mini'),
    # llm=ChatOllama(model='llama3.2'),  # Local OSS
)
```

### 5. MCP bidirectional

**Server mode** (browser-use tools as MCP for Claude Desktop):
```bash
uvx browser-use[cli] --mcp
```

**Client mode** (Agent connects to external MCP servers):
Python API connects to filesystem/GitHub/etc. MCP servers — extends capabilities.

### 6. Claude Code Skill integration

```bash
mkdir -p ~/.claude/skills/browser-use
curl -o ~/.claude/skills/browser-use/SKILL.md \
  https://raw.githubusercontent.com/browser-use/browser-use/main/skills/browser-use/SKILL.md
```

Skill hoạt động trong Claude Code (direct-install, không dùng plugin marketplace).

---

## Phần 7 — vs other corpus frameworks

### vs Skyvern v24 (direct browser T5 peer)

| Axis | browser-use v41 | Skyvern v24 | Winner for Scrum-coach |
|------|------------------|-------------|------------------------|
| License | MIT | AGPL-3.0 | **browser-use** (cleaner commercial use) |
| Architecture | Hybrid DOM+vision | Vision-primary | **browser-use** (more debuggable) |
| LLM providers | 15+ (115 via LiteLLM) | ~10 | **browser-use** |
| Cloud migration | `@sandbox` decorator | Separate API | **browser-use** |
| MCP integration | Bidirectional + DXT | None documented | **browser-use** |
| Benchmark | BU Bench V1 (100 tasks, open-source) | WebBench 64.4% + WebVoyager 85.8% | **Skyvern** (more rigorous public benchmarks) |
| Anti-bot | Cloud-only (like Skyvern) | Cloud-only | Tie (both #48) |
| Scale | 89.9K | 21.3K | **browser-use** (4.2× larger adoption) |

**Decision tree:**
- **Want MIT for client SaaS?** → browser-use
- **Want AGPL-3.0 for OSS-enforcement?** → Skyvern
- **Want vision-primary debugging (trace screenshots)?** → Skyvern
- **Want DOM-stable element selectors + vision augmentation?** → browser-use
- **Want Claude Code / MCP integration today?** → browser-use
- **Want peer-reviewed-adjacent benchmarks?** → Skyvern

### vs other T5 entrants

- **OpenHands v30** — SWE-agent (code), not browser; complementary for dev workflows
- **deer-flow v9** — research-agent (long-horizon report), not browser; ByteDance corporate
- **autoresearch v10** — ML-experiment autonomous; Karpathy's own framework
- **paperclip v14** — orchestration-agent (zero-human-company); philosophically opposite from Scrum-coach positioning
- **DeepTutor v38** — education-agent; different domain

### vs T4 bridge tools (complementary, not competitive)

- **markitdown v28** — static file → Markdown (PDF/DOCX/PPT)
- **crawl4ai v29** — web scraping without LLM in loop
- **claude-context v40** — semantic search over codebase/docs
- **graphify v16** — folder → knowledge graph

browser-use adds **authenticated SaaS extraction** to this stack — the piece the T4 tools can't do alone.

---

## Phần 8 — Ethical framing / Khung đạo đức

⚠️ **browser-use automation interacts with websites in ways that may touch ToS grey areas. Consider carefully.**

### Low-risk use cases ✅

1. **Your own accounts** (Jira/Linear/Notion with your credentials + your workspace)
2. **Public data scraping** (respect robots.txt + rate limits)
3. **Testing** (your own dev/staging environments)
4. **Client workspaces with explicit written authorization** (Scrum-coach scenario — always get email approval before automating)
5. **Browser profile sync for your own auth** (cookies.txt equivalent; personal-auth not shared)

### Higher-risk use cases ⚠️

1. **CAPTCHA bypass** — requires Cloud tier (Pattern #48); bypassing CAPTCHAs may violate site ToS + anti-automation laws in some jurisdictions
2. **Residential proxies for scale** — some jurisdictions regulate residential-proxy use
3. **Authenticated session automation without account-owner consent** — potentially illegal (CFAA in US, similar laws elsewhere)
4. **Aggressive scraping causing service degradation** — potentially liable for damages

### Storm Bear Scrum-coach discipline

- **Always get explicit written client authorization** before automating their SaaS tools
- **Never automate credentials not yours or not explicitly-shared by client**
- **Use `sensitive_data` parameter** to keep credentials out of LLM prompts
- **Use `allowed_domains` Browser parameter** to prevent agent from navigating outside authorized scope
- **Log all agent actions** for audit trail (save_conversation_path)
- **Respect rate limits** (`wait_between_actions=1.0` for slow-sensitive sites)

---

## Phần 9 — Storm Bear operator relevance

**Pilot ranking: #4 in corpus** (after claude-hud / spec-kit / claude-howto).

**Primary use cases for Scrum-coach:**

1. **Jira sprint-report extraction** (weekly, per client) → CSV/markdown for stakeholder comms
2. **Linear cycle-time analysis** (per sprint, per team) → retrospective data
3. **DORA metrics collection** (deployment frequency, lead time, MTTR, change failure rate) across GitHub + Jira + monitoring dashboards
4. **Scrum consultancy competitive scan** (pricing pages + team-size + methodology-stack)
5. **Storm Bear vault source extension** — extend ingestion to authenticated SaaS + JavaScript-heavy SPAs

**Complementary stack:**
- markitdown (static files) + crawl4ai (public web + no-auth) + **browser-use (authenticated + interactive)** + claude-context (semantic search)

**Cost estimate (at Storm Bear scale):**
- 10 clients × 2 ceremonies/week × 4 weeks = 80 tasks/month
- At ~$0.05-0.20/task (ChatBrowserUse + short Cloud sessions) = **$4-16/month**
- Profitable even at 1 client × $50/month coaching retainer

**Caveats:**
- Anti-bot Cloud-gated → production use needs paid tier
- 15-min session cap → chunk long workflows
- MIT library + Cloud ToS (separate) — read both before commercial deployment

---

## Phần 10 — 1-week evaluation roadmap

### Day 1 — Setup + first task (30min)

```bash
# Install
pip install uv && uv venv --python 3.12 && source .venv/bin/activate
uv pip install browser-use && uvx browser-use install

# Get API key from cloud.browser-use.com/new-api-key
echo "BROWSER_USE_API_KEY=your-key" > .env

# First task
cat > first.py <<'EOF'
from browser_use import Agent, ChatBrowserUse
import asyncio
from dotenv import load_dotenv
load_dotenv()

async def main():
    agent = Agent(task="Find the top Hacker News post title and URL", llm=ChatBrowserUse())
    await agent.run()

asyncio.run(main())
EOF

uv run first.py
```

### Day 2 — Profile sync + authenticated task (1h)

```bash
export BROWSER_USE_API_KEY=your-key
curl -fsSL https://browser-use.com/profile.sh | sh
# Interactive: log into Jira/Linear/Notion → get profile_id
```

Write `day2.py` using authenticated task (read Jira sprint board).

### Day 3 — `@sandbox` production deployment (1h)

Wrap Day 2 task in `@sandbox(cloud_profile_id='...')`. Run 3× to verify idempotency + measure cost.

### Day 4 — Custom tools + output schema (1h)

Define Pydantic `SprintReport` schema. Add `@tools.action` for 2FA code fetch. Re-run end-to-end.

### Day 5 — Real client pilot (2h)

Pick 1 client workflow. Run weekly-sprint-report extraction end-to-end. Measure:
- Total cost (tokens + Cloud minutes)
- Success rate (3-5 runs)
- Manual-time saved vs automated-cost

### Day 6-7 — Decision (2h)

Evaluate pilot outcome:
- **Proceed to production** if: ≥80% success + cost < $5/report + manual-time saved ≥30min
- **Iterate** if: success < 80% but failures are fixable (prompt refinement + better output schema)
- **Defer** if: blocked by ToS concerns or success < 50%

**Total pilot cost:** ~$0-10 (5 free tasks + modest pay-as-you-go top-up)

---

## Phần 11 — Tradeoffs + limitations

### Technical

- **Chromium-only** (CDP is Chromium-family)
- **Async Python only** (no sync API)
- **Python 3.11+** required
- **Pre-1.0 (v0.12.6 at 89.9K)** — breaking changes possible; pin version
- **Monolithic service files** (7 files >40KB) — contributor onboarding has learning curve
- **Tabs-not-spaces** Python indentation (non-PEP8)
- **No Firefox/WebKit/Safari** support

### Commercial

- **Anti-bot bypass Cloud-gated** (Pattern #48)
- **ChatBrowserUse default = paid** beyond 5 free tasks
- **Cloud session 15-min cap** for long workflows
- **Cloud pricing** not transparent in README (credits-based; check cloud.browser-use.com)

### Operational

- **Hybrid DOM+vision** slower per step than DOM-only (LLM vision inference latency)
- **Cost per action** adds up for high-volume or long-horizon tasks
- **LLM hallucination** — action reasoning can fail (mitigated by `max_failures=3` retry + `final_response_after_failure=True`)

---

## Phần 12 — Caveats + safety notes

### Credential hygiene

```python
# ❌ WRONG — credentials in prompt
Agent(task="Login as user=admin password=secret123", ...)

# ✅ RIGHT — sensitive_data parameter
Agent(
    task="Login using <admin-creds>",
    sensitive_data={'<admin-creds>': f"user={os.environ['USER']} pass={os.environ['PASS']}"},
)
```

### Domain restrictions

```python
# ✅ Explicit allowlist prevents agent from navigating outside authorized scope
Browser(allowed_domains=['*.atlassian.net', 'jira.mycompany.com'])
```

### Rate limiting

```python
Browser(wait_between_actions=1.0)  # 1-second pause between actions
Agent(max_actions_per_step=1)       # 1 action at a time (vs 3 default)
```

### Profile isolation

Use **separate `cloud_profile_id` per client** to prevent cross-client authentication leakage:
```python
@sandbox(cloud_profile_id=f'client-{client_id}-jira')
```

### Logging + audit trail

```python
Agent(save_conversation_path='./audit-logs/client-X-sprint-42.jsonl')
```

All LLM prompts + browser actions saved for client-audit review.

---

## Phần 13 — References + next action

### Official documentation
- **Repo:** https://github.com/browser-use/browser-use (MIT)
- **Docs:** https://docs.browser-use.com
- **Cloud:** https://cloud.browser-use.com
- **Blog:** https://browser-use.com/posts
- **Discord:** https://link.browser-use.com/discord
- **Twitter:** @browser_use + @mamagnus00 + @gregpr07
- **Merch:** https://browsermerch.com

### Wiki cross-references
- [[(C) index]] — browser-use wiki index
- Skyvern v24 — prior browser T5 + Pattern #47 + #48 founder
- crawl4ai v29 — Pattern #47 refinement (3-point spectrum)
- Unsloth v23 — Pattern #46 un-stale partner
- markitdown v28 — complementary document-ingestion bridge
- claude-context v40 — complementary semantic search

### Next action for Storm Bear operator

**Choose ONE:**

**Option A — Execute 1-week browser-use pilot** (address 30:0 observational-to-pilot gap)
- Day 1-7 protocol (Phần 10)
- Output: pilot-outcome report + go/no-go for production
- Cost: $0-10 + 8 hours operator time

**Option B — Execute v27 diagnostic HIGH bundle** (address 18-session BLOCKING-RECOMMENDATION)
- vault CLAUDE.md refactor (using v34 + v41 AGENTS.md-versioning + claude-hud v35 templates)
- Pattern Library audit + v2.2 routine refactor
- Cost: 1-2 days operator time

**Option C — Continue to v42 wiki** (accept ongoing observational-phase)
- Routine auto-execute next corpus candidate
- Cost: ~2-3h per wiki; no pilot execution

**Recommendation:** Option A (browser-use pilot) offers **highest learning-per-hour** — tests whether wiki insights translate to operational value. Option B preserves vault integrity. Option C is path-of-least-resistance.

---

**browser-use = T5 browser-automation agent (MIT + 89.9K stars + hybrid DOM+vision + 15 LLM providers + `@sandbox` decorator + Browser-Use Cloud commercial tier). Pilot ranking #4 for Storm Bear Scrum-coach. Jira/Linear/DORA-metric extraction is primary use case. 1-week evaluation cost $0-10. Complements markitdown/crawl4ai/claude-context stack. Anti-bot Cloud-gated (Pattern #48 promoted N=2). Ethical discipline required for client workspaces. Corpus-first 30th consecutive Storm Bear meta-entity marks vault-applicability reflection streak.**
