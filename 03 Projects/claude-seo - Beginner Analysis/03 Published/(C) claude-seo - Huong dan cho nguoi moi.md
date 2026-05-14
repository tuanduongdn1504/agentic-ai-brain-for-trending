# claude-seo — Hướng dẫn cho người mới / Beginner's Guide

> **Subject:** [`AgriciDaniel/claude-seo`](https://github.com/AgriciDaniel/claude-seo)
> **Built by:** [Agrici Daniel](https://agricidaniel.com/about) — AI Workflow Architect
> **Wiki version:** v64 — 2026-05-13 (Storm Bear vault, llm-wiki-routine-v2.1)
> **License:** MIT (+ CC BY 4.0 for FLOW 41 prompts bundled)
> **Stars / forks:** 6,494 / 993 — ~95 ngày tuổi tại thời điểm phân tích
> **Bài viết bằng tiếng Việt và tiếng Anh / Bilingual: Vietnamese & English**

---

## 1. claude-seo là gì? / What is claude-seo?

### 🇻🇳 Tiếng Việt

`claude-seo` là một **plugin SEO toàn diện cho Claude Code** — bạn cài đặt một lần, sau đó có 26 lệnh slash (`/seo audit`, `/seo page`, `/seo schema`, ...) sẵn sàng phân tích website của bạn ngay trong terminal.

Không như những công cụ SEO truyền thống (Ahrefs, Semrush, Screaming Frog) yêu cầu trả phí hàng tháng và phải mở giao diện web/desktop riêng, `claude-seo` chạy **ngay trong môi trường code của bạn**, kết quả trả về dạng văn bản tự nhiên (đôi khi kèm báo cáo PDF), và sử dụng AI để hiểu ngữ cảnh thay vì chỉ rà checklist.

**43 nguyên thuỷ** (25 sub-skills + 18 sub-agents) bao quát:
- SEO kỹ thuật (technical SEO) — 9 hạng mục
- Chất lượng nội dung (E-E-A-T theo chuẩn Google Quality Rater 9/2025)
- Schema.org markup (có cảnh báo schema bị deprecated)
- Sitemap XML
- Tối ưu ảnh + ảnh trên SERP
- Tối ưu cho AI Search (Google AI Overviews, ChatGPT, Perplexity) — gọi là **GEO**
- Local SEO + Google Business Profile + bản đồ
- Hreflang + 4 hồ sơ văn hoá (DACH, Pháp ngữ, Tây Ban Nha, Nhật)
- Tích hợp Google APIs (GSC, PageSpeed, CrUX, GA4)
- Phân tích backlink (Moz, Bing, Common Crawl miễn phí)
- Phân cụm chủ đề (semantic clustering)
- Theo dõi drift SEO (so sánh thay đổi qua thời gian, lưu SQLite)
- E-commerce SEO + dữ liệu marketplace

### 🇬🇧 English

`claude-seo` is a **comprehensive SEO plugin for Claude Code** — you install it once, then have 26 slash commands (`/seo audit`, `/seo page`, `/seo schema`, ...) ready to analyze your website right from the terminal.

Unlike traditional SEO tools (Ahrefs, Semrush, Screaming Frog) that require monthly fees and a separate web/desktop UI, `claude-seo` runs **inside your coding environment**, returns results as natural language (sometimes with PDF reports), and uses AI to understand context instead of just running checklists.

**43 primitives** (25 sub-skills + 18 sub-agents) covering:
- Technical SEO — 9 categories
- Content quality (E-E-A-T per Sept 2025 Quality Rater Guidelines)
- Schema.org markup (with deprecation alerts)
- XML sitemaps
- Image optimization + image SERP
- AI search optimization (Google AI Overviews / ChatGPT / Perplexity) — called **GEO**
- Local SEO + Google Business Profile + maps
- Hreflang + 4 cultural profiles (DACH / Francophone / Hispanic / Japanese)
- Google APIs integration (GSC / PageSpeed / CrUX / GA4)
- Backlink analysis (free: Moz / Bing / Common Crawl)
- Semantic topic clustering
- SEO drift monitoring (track changes over time, SQLite-persisted)
- E-commerce SEO + marketplace data

---

## 2. Ai là tác giả? Tại sao nên quan tâm? / Who's the author? Why care?

### 🇻🇳 Tiếng Việt

Tác giả là **Agrici Daniel** (agricidaniel.com), tự gọi mình là "AI Workflow Architect". Anh không chỉ xây một plugin SEO — anh xây cả một **hệ sinh thái 5 sản phẩm** dưới cùng tên thương hiệu:

1. **claude-seo** (sản phẩm này) — phân tích SEO
2. **claude-blog** — viết bài blog tối ưu SEO
3. **claude-banana** — sinh ảnh SEO bằng AI (qua Gemini)
4. **codex-seo** — bản port sang Codex CLI (cho người dùng OpenAI Codex)
5. **FLOW** — bộ 41 prompt framework đánh giá SEO (CC BY 4.0, là kiến thức nền cho `seo-flow` skill)

Cộng thêm 1 sản phẩm cộng đồng (AI Marketing Claude) được liên kết chính thức trong README.

**Tại sao đây là điểm thú vị:** đây là một **cá nhân solo** xây 5 sản phẩm có ghép nối chức năng, có cross-product workflow chính thức trong README:
```
1. /seo audit example.com           → tìm gaps
2. /seo backlinks example.com       → phân tích backlink
3. /blog write "keyword"            → viết bài (sản phẩm khác)
4. /seo image-gen hero "topic"      → sinh ảnh hero (extension)
5. /seo geo example.com/post        → tối ưu cho AI Search
```

**Quan trọng:** trong corpus 63 wiki của Storm Bear vault, đây là **lần thứ 3 quan sát "ecosystem-portfolio-builder"** (sau v61 cc-sdd của gotalab Nhật và v63 karpathy-skills của forrestchang). 3 hồ sơ khác nhau = bằng chứng đủ để PROMOTE mẫu này thành sub-type chính thức tại đợt audit v66.

### 🇬🇧 English

The author is **Agrici Daniel** (agricidaniel.com), self-styled "AI Workflow Architect". He didn't just build an SEO plugin — he built an **ecosystem of 5 products** under one brand:

1. **claude-seo** (this product) — SEO analysis
2. **claude-blog** — SEO-optimized blog writing
3. **claude-banana** — AI image generation (via Gemini)
4. **codex-seo** — Codex CLI port (for OpenAI Codex users)
5. **FLOW** — 41-prompt SEO framework (CC BY 4.0, knowledge base for the `seo-flow` skill)

Plus 1 community product (AI Marketing Claude) officially cross-linked from the README.

**Why this matters:** this is a **solo individual** building 5 functionally-coupled products with an explicit cross-product workflow in the README:
```
1. /seo audit example.com           → find gaps
2. /seo backlinks example.com       → analyze backlinks
3. /blog write "keyword"            → write the post (different product)
4. /seo image-gen hero "topic"      → generate hero image (extension)
5. /seo geo example.com/post        → optimize for AI Search
```

**Important:** in Storm Bear vault's 63-wiki corpus, this is the **3rd observation of "ecosystem-portfolio-builder"** (after v61 cc-sdd by Japanese gotalab and v63 karpathy-skills by forrestchang). 3 distinct shapes = enough evidence to PROMOTE this pattern to a confirmed sub-type at the v66 audit.

---

## 3. Cài đặt như thế nào? / How to install?

### 🇻🇳 Tiếng Việt

**Cách 1 (khuyên dùng nếu bạn dùng Claude Code 1.0.33+):**
```bash
# Trong Claude Code:
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-seo
```

**Cách 2 (Unix / macOS / Linux):**
```bash
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/install.sh
```

**Cách 3 (Windows PowerShell):**
```powershell
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
powershell -ExecutionPolicy Bypass -File claude-seo\install.ps1
```

**Lưu ý quan trọng về bảo mật:** Tác giả **không khuyến khích** dùng PowerShell one-liner `irm | iex` (kiểu `irm url | iex`) vì:
> *"Claude Code's own security guardrails flag `irm ... | iex` as a supply chain risk"*

Tức là chính Claude Code đã đánh dấu kiểu cài này là rủi ro chuỗi cung ứng. Tác giả bắt buộc bạn `git clone` trước (để có thể đọc `install.ps1` rồi mới chạy).

**Yêu cầu hệ thống:** Python 3.10+ / Claude Code CLI / Tuỳ chọn: Playwright cho screenshot / Tuỳ chọn: Google API credentials.

### 🇬🇧 English

**Method 1 (recommended for Claude Code 1.0.33+):**
```bash
# In Claude Code:
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-seo
```

**Method 2 (Unix / macOS / Linux):**
```bash
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/install.sh
```

**Method 3 (Windows PowerShell):**
```powershell
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
powershell -ExecutionPolicy Bypass -File claude-seo\install.ps1
```

**Important security note:** The author **does not endorse** the PowerShell one-liner `irm | iex` pattern because:
> *"Claude Code's own security guardrails flag `irm ... | iex` as a supply chain risk"*

Claude Code itself flags this install pattern as supply-chain risk. The author requires you `git clone` first (so you can read `install.ps1` before running it).

**System requirements:** Python 3.10+ / Claude Code CLI / Optional: Playwright for screenshots / Optional: Google API credentials.

---

## 4. Thử nó ngay trong 5 phút / Try it in 5 minutes

### 🇻🇳 Tiếng Việt

Sau khi cài, mở Claude Code và thử lần lượt:

```
/seo audit https://example.com
```
→ Quét toàn bộ website. Spawn lên tới **15 sub-agent chạy song song** (technical / content / schema / sitemap / performance / visual / geo / local / maps / google / backlinks / cluster / sxo / drift / ecommerce). Trả về danh sách findings có ưu tiên.

```
/seo page https://example.com/about
```
→ Phân tích sâu 1 trang (title / meta / heading / nội dung / schema / nội ảnh / liên kết).

```
/seo schema https://example.com
```
→ Detect schema hiện có, validate, cảnh báo nếu có HowTo (deprecated 9/2023) hoặc FAQ (restricted 8/2023) hoặc SpecialAnnouncement (deprecated 7/2025).

```
/seo geo https://example.com
```
→ Đánh giá tối ưu cho AI Search (Google AI Overviews, ChatGPT, Perplexity). Tính passage-level citability (134-167 từ tối ưu).

```
/seo sitemap generate
```
→ Sinh sitemap mới với template theo ngành (SaaS / local / ecommerce / publisher / agency).

**Bonus:** sau bất kỳ lệnh phân tích nào, plugin sẽ tự gợi ý:
> *"Generate a PDF report? Use `/seo google report`"*

PDF được tạo bằng `scripts/google_report.py` (WeasyPrint + matplotlib) — báo cáo A4 chuyên nghiệp, có Title page, TOC, biểu đồ 200 DPI, palette màu navy/forest-green/amber/red.

### 🇬🇧 English

After install, open Claude Code and try in order:

```
/seo audit https://example.com
```
→ Scans the whole site. Spawns up to **15 parallel sub-agents** (technical / content / schema / sitemap / performance / visual / geo / local / maps / google / backlinks / cluster / sxo / drift / ecommerce). Returns prioritized findings.

```
/seo page https://example.com/about
```
→ Deep single-page analysis (title / meta / headings / content / schema / images / links).

```
/seo schema https://example.com
```
→ Detects existing schema, validates, warns if HowTo (deprecated Sept 2023) or FAQ (restricted Aug 2023) or SpecialAnnouncement (deprecated July 2025) present.

```
/seo geo https://example.com
```
→ Scores AI Search optimization (Google AI Overviews / ChatGPT / Perplexity). Computes passage-level citability (134-167 words optimum).

```
/seo sitemap generate
```
→ Generates new sitemap with industry template (SaaS / local / ecommerce / publisher / agency).

**Bonus:** after any analysis command, the plugin proactively offers:
> *"Generate a PDF report? Use `/seo google report`"*

The PDF is generated via `scripts/google_report.py` (WeasyPrint + matplotlib) — professional A4 report with title page, TOC, 200 DPI charts, navy/forest-green/amber/red color palette.

---

## 5. Điểm nổi bật / Strengths

### 🇻🇳 Tiếng Việt

**(a) Lớn nhất trong corpus T1**
- 43 nguyên thuỷ (25 sub-skills + 18 sub-agents) — **bộ T1 lớn nhất quan sát được trong 63 wiki của vault**
- Đặc biệt: 26 lệnh slash bao quát ngành SEO toàn vẹn

**(b) Phát hành đa nền tảng (5 + 1)**
- Claude Code (chính)
- Cursor
- Cursor Cloud Agents
- Google Antigravity
- Gemini CLI
- + 1 bản port chị em: **codex-seo** cho Codex CLI (TOML agents, deterministic runners)
- → **6-platform-reach — kỷ lục corpus T1**

**(c) Theo dõi standards "sống" (Living-Domain-Standards)**
- 8 sự kiện deprecation được track với ngày cụ thể (HowTo 9/2023, FAQ 8/2023, SpecialAnnouncement 7/2025, FID→INP 12/3/2024...)
- Quality Rater Guidelines version 9/2025
- E-E-A-T mở rộng theo Google December 2025 core update
- **Bộ tracker external-authority mạnh nhất quan sát trong corpus**

**(d) Bảo mật ở mức "production-grade"**
- v1.9.6 vá **10 lỗ hổng có tên** (VULN-A01 đến VULN-A10) trong 1 release
- SSRF protection trong tất cả script gọi user URL
- Atomic file writes / Path-traversal block / URL allowlist / 5 MB caps
- CI guard 13 assertions ở v1.9.9 đảm bảo manifest consistency

**(e) Quality gates chống Goodhart**
- Programmatic SEO: WARNING tại 100+ trang, **HARD STOP tại 500+** không qua audit
- Local SEO: WARNING tại 30+ trang location, HARD STOP tại 50+
- Plugin **từ chối mass-generate** ngay cả khi có thể — anti-Goodhart-law discipline

**(f) Cộng đồng tích cực**
- v1.9.0 ship 5 contributions từ Pro Hub Challenge (Lutfiya Miller / Florian Schmitz / Dan Colta / Chris Muller / Matej Marjanovic)
- 5/6 submissions được chấm "Proficient or above"

**(g) Tuỳ chọn extension mềm dẻo**
- DataForSEO (commercial, 22 lệnh, 9 API modules)
- Banana (sinh ảnh AI, có thể tái dùng standalone install)
- Firecrawl (crawl full-site với JS rendering — mitigate SPA limitation)
- 4-tier Google credential: Tier 0 (API key) → Tier 1 (+OAuth) → Tier 2 (+GA4) → Tier 3 (+Ads). Giá trị ngay từ Tier 0.

### 🇬🇧 English

**(a) Largest in T1 corpus**
- 43 primitives (25 sub-skills + 18 sub-agents) — **largest T1 collection observed in the vault's 63-wiki corpus**
- Notable: 26 slash commands span the entire SEO domain comprehensively

**(b) Multi-platform deployment (5 + 1)**
- Claude Code (primary)
- Cursor
- Cursor Cloud Agents
- Google Antigravity
- Gemini CLI
- + 1 sister-port: **codex-seo** for Codex CLI (TOML agents, deterministic runners)
- → **6-platform reach — corpus T1 record**

**(c) Living-Domain-Standards tracking**
- 8 deprecation events tracked with specific dates (HowTo Sept 2023, FAQ Aug 2023, SpecialAnnouncement July 2025, FID→INP March 12 2024...)
- Quality Rater Guidelines version September 2025
- E-E-A-T expanded per Google December 2025 core update
- **Strongest external-authority tracker observed in corpus**

**(d) Production-grade security**
- v1.9.6 patched **10 named vulnerabilities** (VULN-A01 through VULN-A10) in one release
- SSRF protection in all scripts accepting user URLs
- Atomic file writes / Path-traversal block / URL allowlist / 5 MB caps
- CI guard with 13 assertions at v1.9.9 ensuring manifest consistency

**(e) Anti-Goodhart quality gates**
- Programmatic SEO: WARNING at 100+ pages, **HARD STOP at 500+** without audit
- Local SEO: WARNING at 30+ location pages, HARD STOP at 50+
- Plugin **refuses to mass-generate** even when mechanically capable — anti-Goodhart-law discipline

**(f) Active community**
- v1.9.0 shipped 5 contributions from Pro Hub Challenge (Lutfiya Miller / Florian Schmitz / Dan Colta / Chris Muller / Matej Marjanovic)
- 5/6 submissions scored "Proficient or above"

**(g) Flexible extension model**
- DataForSEO (commercial, 22 commands, 9 API modules)
- Banana (AI image gen, can reuse standalone install)
- Firecrawl (full-site crawl with JS rendering — mitigates SPA limitation)
- 4-tier Google credential: Tier 0 (API key) → Tier 1 (+OAuth) → Tier 2 (+GA4) → Tier 3 (+Ads). Value starts at Tier 0.

---

## 6. Điểm cần lưu ý / Caveats

### 🇻🇳 Tiếng Việt

**(a) SPA/CSR sites trả về false-negative**

README ghi rõ:
> *"Sites that render content client-side without server-side rendering will produce false-negative findings on content, schema, headings, and meta in most subagents."*

Nếu site của bạn là **Single Page Application không có SSR** (Vite/CRA React thuần, Vue/Angular client-only), orchestrator sẽ thấy HTML rỗng. **Workaround:** dùng Firecrawl extension để có JS rendering, hoặc bật `seo-visual` agent (dùng Playwright).

Đây là vấn đề được track ở GitHub issue #11 cho v2.0 epic.

**(b) Bản 1.x là final patch (1.9.9)**

v1.9.9 (11/5/2026) là **bản patch 1.x cuối cùng**. v2 đang trong giai đoạn thiết kế. Nếu bạn cần các tính năng deferred:
- #11 SPA/CSR audit (full)
- #51 Subagent research persistence
- #61 google_report `--type full` audit-schema
- #89 uv adoption
- #53 seo-notebooklm
- #46 macOS SSL với pip-system-certs

→ tất cả đợi v2.

**(c) Một số API yêu cầu tài khoản trả phí**

- DataForSEO extension: cần tài khoản DataForSEO (commercial)
- Google APIs: Tier 0 (API key) miễn phí; Tier 1+ cần OAuth/SA setup (vẫn miễn phí cho most use case nhưng có quota)
- Banana extension: nanobanana-mcp setup riêng

Plugin **không gate** core functionality sau extensions — bạn có thể dùng `/seo audit` mà không cài bất kỳ extension nào.

**(d) Không persist subagent findings giữa các lần chạy (intentional v1.x contract)**

Nếu bạn chạy `/seo audit` rồi muốn agent khác đọc lại findings, bạn phải copy/paste hoặc lưu thủ công. v2 sẽ revisit theo issue #51.

**(e) Drift incidents lịch sử (đã fix)**

Lịch sử CHANGELOG cho thấy **3 lần version-source-drift** (v1.8.1, v1.9.7, v1.9.8) trước khi tác giả thiết lập CI manifest-guard. Đây không phải vấn đề hiện tại (v1.9.9 đã có 13 assertions), nhưng cho thấy quá trình learning. Tin tốt: tác giả đã hệ thống hoá thành CI gate, sẽ không lặp lại.

### 🇬🇧 English

**(a) SPA/CSR sites produce false-negatives**

README clearly states:
> *"Sites that render content client-side without server-side rendering will produce false-negative findings on content, schema, headings, and meta in most subagents."*

If your site is a **client-side rendered SPA without SSR** (vanilla Vite/CRA React, client-only Vue/Angular), the orchestrator sees empty HTML. **Workaround:** use the Firecrawl extension for JS rendering, or enable the `seo-visual` agent (uses Playwright).

Tracked at GitHub issue #11 for the v2.0 epic.

**(b) 1.x is now final patch (1.9.9)**

v1.9.9 (May 11, 2026) is the **final 1.x patch**. v2 is in design. If you need deferred features:
- #11 SPA/CSR audit (full)
- #51 Subagent research persistence
- #61 google_report `--type full` audit-schema
- #89 uv adoption
- #53 seo-notebooklm
- #46 macOS SSL via pip-system-certs

→ all wait for v2.

**(c) Some APIs require paid accounts**

- DataForSEO extension: requires DataForSEO account (commercial)
- Google APIs: Tier 0 (API key) free; Tier 1+ requires OAuth/SA setup (still free for most use cases but with quotas)
- Banana extension: separate nanobanana-mcp setup

Plugin **does NOT gate** core functionality behind extensions — you can use `/seo audit` without any extension installed.

**(d) Subagent findings NOT persisted across runs (intentional v1.x contract)**

If you run `/seo audit` then want another agent to re-read findings, you must copy/paste or save manually. v2 will revisit per issue #51.

**(e) Historical drift incidents (now fixed)**

CHANGELOG history shows **3 version-source-drift incidents** (v1.8.1, v1.9.7, v1.9.8) before the author established the CI manifest-guard. This is not a current problem (v1.9.9 has 13 assertions), but shows the learning process. Good news: the author systematized it into a CI gate, won't recur.

---

## 7. Khi nào nên dùng? / When to use?

### 🇻🇳 Tiếng Việt

**Phù hợp với:**
- Solo dev / agency / SaaS team đã dùng Claude Code và cần phân tích SEO định kỳ
- Người làm content / blog cần loop chặt giữa audit → write → publish
- Local business cần GBP + maps intelligence không muốn trả phí Yext/Birdeye
- E-commerce cần product schema + marketplace intelligence
- Site đa ngôn ngữ cần hreflang + cultural profile
- Bất kỳ ai cần báo cáo PDF chuyên nghiệp cho stakeholder
- Người dùng OpenAI Codex (qua codex-seo sister-port)

**Không phù hợp với:**
- Pure SPA không có SSR (đợi v2)
- Site yêu cầu Ahrefs/Semrush deep-link data làm primary (claude-seo có Moz/Bing/Common Crawl miễn phí làm baseline; bạn cần DataForSEO extension cho premium data)
- Team không dùng Claude Code/Cursor/Antigravity/Gemini CLI (chưa hỗ trợ platform khác)
- Người không quen với CLI / terminal workflow

### 🇬🇧 English

**Good fit for:**
- Solo dev / agency / SaaS team already using Claude Code and needing regular SEO analysis
- Content/blog teams needing tight audit → write → publish loops
- Local businesses needing GBP + maps intelligence without paying for Yext/Birdeye
- E-commerce needing product schema + marketplace intelligence
- Multi-language sites needing hreflang + cultural profiles
- Anyone needing professional PDF reports for stakeholders
- OpenAI Codex users (via codex-seo sister-port)

**Not a fit for:**
- Pure SPA without SSR (wait for v2)
- Sites requiring Ahrefs/Semrush deep-link data as primary (claude-seo provides Moz/Bing/Common Crawl free baseline; need DataForSEO extension for premium data)
- Teams not using Claude Code / Cursor / Antigravity / Gemini CLI (other platforms not yet supported)
- Users uncomfortable with CLI / terminal workflow

---

## 8. Học gì từ Storm Bear vault wiki? / What does the Storm Bear vault wiki contribute?

### 🇻🇳 Tiếng Việt

Bài wiki v64 này không chỉ giới thiệu `claude-seo` — nó còn đăng ký các **ngụ ý Pattern Library** vào kho tri thức của vault:

1. **Pattern #19 ecosystem-portfolio-builder N=3 promotion-eligible** — claude-seo là bằng chứng N=3 (sau gotalab v61 và forrestchang v63). Đợt audit v66 sẽ deliberate việc promote sub-type này lên trạng thái CONFIRMED.
2. **Pattern #18 Layer 1 cross-IDE-coexistence tại quy mô 5-platform** — split CLAUDE.md vs AGENTS.md là cơ chế phát hiện
3. **Pattern #18 Layer 2 NEW sub-archetype candidate** — codex-seo sister-port là bằng chứng N=1 cho "solo-author cross-vendor parallel-port"
4. **NEW T1 sub-archetype: domain-vertical-skill-collection** — claude-seo là N=1 đầu tiên (vertical SEO 100%); chờ N=2 sang lĩnh vực khác (legal/medical/finance)
5. **NEW Pattern: Living-Domain-Standards Tracking** — bộ tracker external-authority với deprecation dates là N=1 đầu tiên
6. **Pattern #28 Progressive Disclosure** strengthening qua 4 chiều (metadata / credentials / extensions / runtime)
7. **Pattern #59 Claude Code Plugin Marketplace** tại quy mô solo-individual high-engagement (6.5K sao + 15.3% fork ratio)
8. **Pattern #52 EXTREME-VIRAL counter-evidence** — claude-seo NOT extreme-viral (~68 stars/day below 300/day threshold), tăng cường specificity của Pattern #52

Wiki ship này có **1 promotion-eligible + 6 strengthenings + 2 NEW candidates + 4 observational candidates** — chuẩn bị đầy đủ cho audit v66.

**Storm Bear meta-entity SKIPPED tại v64** theo Phase 0.9 STRICT (0/4 strong PASS) — vì SEO domain không trực tiếp phục vụ vault Goal #2 ("build software with these tools"). Streak Storm Bear meta-entity reset 4 → 0 sau v64 SKIP. Tỷ lệ INCLUDE qua 9 wiki post-amendment: 77.8% (7 PASS / 2 SKIP) — calibration lành mạnh.

### 🇬🇧 English

This v64 wiki doesn't just describe `claude-seo` — it registers **Pattern Library implications** into the vault's knowledge base:

1. **Pattern #19 ecosystem-portfolio-builder N=3 promotion-eligible** — claude-seo is N=3 evidence (after gotalab v61 and forrestchang v63). The v66 audit will deliberate promoting this sub-type to CONFIRMED status.
2. **Pattern #18 Layer 1 cross-IDE-coexistence at 5-platform scale** — the CLAUDE.md vs AGENTS.md split is the discovered mechanism
3. **Pattern #18 Layer 2 NEW sub-archetype candidate** — codex-seo sister-port is N=1 evidence for "solo-author cross-vendor parallel-port"
4. **NEW T1 sub-archetype: domain-vertical-skill-collection** — claude-seo is the first N=1 (100% SEO vertical); waiting for N=2 in another vertical (legal/medical/finance)
5. **NEW Pattern: Living-Domain-Standards Tracking** — external-authority tracker with deprecation dates is the first N=1
6. **Pattern #28 Progressive Disclosure** strengthening across 4 dimensions (metadata / credentials / extensions / runtime)
7. **Pattern #59 Claude Code Plugin Marketplace** at solo-individual high-engagement scale (6.5K stars + 15.3% fork ratio)
8. **Pattern #52 EXTREME-VIRAL counter-evidence** — claude-seo is NOT extreme-viral (~68 stars/day below 300/day threshold), strengthening Pattern #52's specificity

This wiki ship has **1 promotion-eligible + 6 strengthenings + 2 NEW candidates + 4 observational candidates** — fully prepared for the v66 audit.

**Storm Bear meta-entity SKIPPED at v64** per Phase 0.9 STRICT (0/4 strong PASS) — SEO domain doesn't directly serve vault Goal #2 ("build software with these tools"). Storm Bear meta-entity streak resets 4 → 0 after v64 SKIP. INCLUDE rate across 9 post-amendment wikis: 77.8% (7 PASS / 2 SKIP) — healthy calibration.

---

## 9. Tài liệu tham khảo / Further reading

- **Project CLAUDE.md:** [../CLAUDE.md](../CLAUDE.md) — phân loại 12-axis + Pattern Library implications preview
- **Wiki index:** [../02 Wiki/index.md](../02%20Wiki/index.md)
- **Cluster 1 — README + 26 commands:** [../02 Wiki/cluster-1-readme-and-commands.md](../02%20Wiki/cluster-1-readme-and-commands.md)
- **Cluster 2 — Architecture + skill system:** [../02 Wiki/cluster-2-architecture-and-skill-system.md](../02%20Wiki/cluster-2-architecture-and-skill-system.md)
- **Cluster 3 — Ecosystem + CHANGELOG:** [../02 Wiki/cluster-3-ecosystem-and-changelog.md](../02%20Wiki/cluster-3-ecosystem-and-changelog.md)
- **Entity 1 — claude-seo core:** [../02 Wiki/entity-1-claude-seo-core.md](../02%20Wiki/entity-1-claude-seo-core.md)
- **Entity 2 — ecosystem-portfolio N=3:** [../02 Wiki/entity-2-ecosystem-portfolio-n3.md](../02%20Wiki/entity-2-ecosystem-portfolio-n3.md)
- **Entity 3 — T1 domain-vertical + Living-Domain-Standards:** [../02 Wiki/entity-3-domain-vertical-and-living-standards.md](../02%20Wiki/entity-3-domain-vertical-and-living-standards.md)
- **Entity 4 — multi-platform + Pattern Library implications:** [../02 Wiki/entity-4-multi-platform-and-patterns.md](../02%20Wiki/entity-4-multi-platform-and-patterns.md)

**External:**
- Repo gốc: https://github.com/AgriciDaniel/claude-seo
- Tác giả: https://agricidaniel.com/about
- Marketing site: https://claude-seo.md/
- YouTube demo: https://www.youtube.com/watch?v=COMnNlUakQk
- Codex sister-port: https://github.com/AgriciDaniel/codex-seo
- FLOW framework: https://github.com/AgriciDaniel/flow

---

> *Generated by Claude (Storm Bear vault, llm-wiki-routine-v2.1) on 2026-05-13. Bilingual VN+EN.*
