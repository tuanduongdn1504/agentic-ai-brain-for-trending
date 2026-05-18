# CloakBrowser — Hướng dẫn cho người mới (VN + EN)

> Bilingual beginner guide for v69 wiki subject · cấu trúc song ngữ tiếng Việt + English
>
> **IMPORTANT FRAMING NOTE:** CloakBrowser là một công cụ "stealth browser" (trình duyệt ẩn danh để vượt qua hệ thống phát hiện bot). Hướng dẫn này tập trung vào: (1) tool là gì, (2) cách thức hoạt động ở mức kiến trúc, (3) các use case hợp pháp. Hướng dẫn KHÔNG cung cấp kỹ thuật vượt qua hệ thống chống bot cụ thể của các dịch vụ web — đó là tài liệu thực hành thuộc trách nhiệm của người dùng đối với ToS và pháp luật.
>
> CloakBrowser is a stealth-browser tool (anti-detection automation). This guide focuses on: (1) what the tool is, (2) how it works architecturally, (3) legitimate use cases. The guide does NOT provide tactical evasion techniques against specific anti-bot services — that operational responsibility belongs to the user under their jurisdiction's ToS + applicable law.

---

## 1. CloakBrowser là gì? / What is CloakBrowser?

### VN

CloakBrowser là một phiên bản Chromium (trình duyệt mở nguồn nguồn) đã được **sửa đổi ở cấp source code C++** với 57 patch (vá) tích hợp vào binary. Mục đích của nó là cho phép automation (tự động hóa trình duyệt) bằng Playwright/Puppeteer mà KHÔNG bị các hệ thống chống bot phát hiện.

Nói cách khác:
- **Playwright bình thường** = trình duyệt automation bị nhận diện là bot
- **CloakBrowser** = trình duyệt automation TRỜI khó nhận diện là bot

### EN

CloakBrowser is a modified Chromium build (open-source browser) with **57 source-level C++ patches** baked into the compiled binary. Its purpose: enable Playwright/Puppeteer-based browser automation WITHOUT being detected by anti-bot systems.

In other words:
- **Standard Playwright** = browser automation identifiable as a bot
- **CloakBrowser** = browser automation hard to identify as a bot

---

## 2. Khi nào nên dùng CloakBrowser? / When should you use CloakBrowser?

### VN — Use case HỢP PHÁP

CloakBrowser phù hợp cho các tình huống:

✅ **Authorized red-team / pentest** — bạn được phép bởi chủ sở hữu hệ thống để kiểm tra phòng thủ chống bot
✅ **Nghiên cứu học thuật** — nghiên cứu về hệ thống nhận diện bot, fingerprinting
✅ **Accessibility testing** — kiểm tra trải nghiệm trình duyệt từ các profile khác nhau
✅ **Web archiving hợp pháp** — lưu trữ nội dung công khai cho mục đích bảo tồn (với tôn trọng robots.txt)
✅ **Privacy-preserving browsing** — duyệt web hạn chế bị fingerprinting
✅ **Scraping được phép** — scraping dữ liệu công khai khi ToS cho phép HOẶC được phép rõ ràng từ chủ sở hữu

### VN — Use case KHÔNG hợp pháp (theo BINARY-LICENSE)

Theo BINARY-LICENSE.md, các use case sau bị cấm rõ ràng:

❌ Truy cập trái phép vào hệ thống xác thực tài chính, ngân hàng, y tế, chính phủ
❌ Credential stuffing, brute-force login, tự động tạo tài khoản hàng loạt
❌ Vượt qua xác thực trên hệ thống bạn không sở hữu hoặc không được phép kiểm tra
❌ Gian lận, trộm danh tính, thu thập dữ liệu trái phép

### EN — Legitimate use cases

CloakBrowser is appropriate for:

✅ **Authorized red-team / pentest** — system owner has granted you permission to test anti-bot defenses
✅ **Academic research** — researching bot-detection systems, browser fingerprinting
✅ **Accessibility testing** — testing browser experience across diverse user profiles
✅ **Legitimate web archiving** — preserving publicly-available content for archival purposes (respecting robots.txt)
✅ **Privacy-preserving browsing** — reducing fingerprint exposure during ordinary web use
✅ **Authorized scraping** — scraping publicly-available data where ToS permits OR explicit owner permission

### EN — Prohibited uses (per BINARY-LICENSE)

BINARY-LICENSE.md explicitly prohibits:

❌ Unauthorized access to financial, banking, healthcare, or government authentication systems
❌ Credential stuffing, brute-force login attempts, or automated account creation
❌ Circumventing authentication on systems you do not own or have authorization to test
❌ Fraud, identity theft, or unauthorized data collection

---

## 3. Kiến trúc 4 lớp / 4-layer architecture

### VN

CloakBrowser có kiến trúc 4 lớp xếp chồng:

```
Lớp 1: SDK Python/JavaScript (Playwright drop-in)
    ↓
Lớp 2: 18+ flag --fingerprint-* (configuration)
    ↓
Lớp 3: 57 C++ patches trong binary Chromium đã biên dịch
    ↓
Lớp 4: humanize=True (mô phỏng hành vi con người — optional)
```

Mỗi lớp đảm nhiệm một phần:
- **Lớp 1** = API tương thích Playwright (developer thấy code quen thuộc)
- **Lớp 2** = quyền cấu hình runtime (set GPU, timezone, locale, v.v.)
- **Lớp 3** = thực tế ẩn danh (canvas, WebGL, audio, TLS hand-shake)
- **Lớp 4** = thêm hành vi giống người (Bézier mouse curve, typing với typo)

### EN

CloakBrowser has 4 stacked architectural layers:

```
Layer 1: Python/JavaScript SDK (Playwright drop-in)
    ↓
Layer 2: 18+ --fingerprint-* flags (configuration)
    ↓
Layer 3: 57 C++ patches in compiled Chromium binary
    ↓
Layer 4: humanize=True (human behavior simulation — optional)
```

Each layer's responsibility:
- **Layer 1** = Playwright-compatible API (developer sees familiar code)
- **Layer 2** = runtime configuration (set GPU, timezone, locale, etc.)
- **Layer 3** = actual stealth machinery (canvas, WebGL, audio, TLS handshake)
- **Layer 4** = optional human-like behavior (Bézier mouse curves, typing with typos)

---

## 4. Cài đặt và "Hello World" / Installation and Hello World

### VN

**Python:**
```bash
pip install cloakbrowser
```

Lần đầu chạy, CloakBrowser sẽ tự động tải binary Chromium (~200MB, cached tại `~/.cloakbrowser/`).

**JavaScript:**
```bash
npm install cloakbrowser playwright-core
```

**Hello World (Python):**
```python
from cloakbrowser import launch

browser = launch()
page = browser.new_page()
page.goto("https://example.com")
print(page.title())
browser.close()
```

### EN

**Python:**
```bash
pip install cloakbrowser
```

On first run, CloakBrowser auto-downloads the Chromium binary (~200MB, cached to `~/.cloakbrowser/`).

**JavaScript:**
```bash
npm install cloakbrowser playwright-core
```

**Hello World (Python):**
```python
from cloakbrowser import launch

browser = launch()
page = browser.new_page()
page.goto("https://example.com")
print(page.title())
browser.close()
```

---

## 5. Phân biệt với Playwright thường / How it differs from standard Playwright

### VN

API gần như giống hệt — chỉ thay đổi `import` statement. Khác biệt nằm ở **binary** chạy bên dưới + tự động kích hoạt stealth-defaults.

| Tính năng | Playwright standard | CloakBrowser |
|---|---|---|
| `navigator.webdriver` | `true` (lộ là bot) | `false` (giống Chrome thật) |
| `navigator.plugins.length` | 0 | 5 (danh sách plugin thật) |
| `window.chrome` | `undefined` | object (có như Chrome thật) |
| UA string | `HeadlessChrome` | `Chrome/146.0.0.0` |
| TLS fingerprint | Mismatch | Giống hệt Chrome |
| reCAPTCHA v3 score | 0.1 (bot) | 0.9 (human-level) |

### EN

The API is nearly identical — only the `import` statement changes. The difference is in the **binary** running underneath + automatically activated stealth-defaults.

| Feature | Standard Playwright | CloakBrowser |
|---|---|---|
| `navigator.webdriver` | `true` (reveals bot) | `false` (matches real Chrome) |
| `navigator.plugins.length` | 0 | 5 (real plugin list) |
| `window.chrome` | `undefined` | object (present like real Chrome) |
| UA string | `HeadlessChrome` | `Chrome/146.0.0.0` |
| TLS fingerprint | Mismatch | Identical to Chrome |
| reCAPTCHA v3 score | 0.1 (bot) | 0.9 (human-level) |

---

## 6. License — đọc kỹ trước khi dùng / License — read carefully before use

### VN

CloakBrowser có **2 license riêng**, áp dụng cho 2 artifact khác nhau:

**LICENSE (MIT)** — áp dụng cho code Python/JS wrapper:
- Tự do sử dụng, sửa đổi, phân phối, bán
- Không đảm bảo gì

**BINARY-LICENSE.md (Proprietary + Acceptable Use)** — áp dụng cho binary Chromium đã biên dịch:
- Tự do dùng cho mục đích cá nhân hoặc thương mại
- **KHÔNG được phân phối lại binary** (redistribute)
- **KHÔNG được reverse engineer / decompile**
- **KHÔNG được dùng cho 4 use case bị cấm rõ ràng** (xem Section 2)
- Giới hạn trách nhiệm pháp lý của CloakHQ ở $100 max

**Sử dụng làm OEM/SaaS (bundling binary vào sản phẩm phân phối cho khách hàng thứ 3) cần license thương mại riêng.** Liên hệ cloakhq@pm.me.

### EN

CloakBrowser ships **2 separate licenses** for different artifacts:

**LICENSE (MIT)** — applies to Python/JS wrapper code:
- Free use, modify, distribute, sell
- No warranty

**BINARY-LICENSE.md (Proprietary + Acceptable Use)** — applies to compiled Chromium binary:
- Free for personal or commercial use
- **NO redistribution** of the binary
- **NO reverse engineering / decompilation**
- **NO use for 4 explicitly prohibited purposes** (see Section 2)
- CloakHQ's max aggregate liability capped at $100

**OEM/SaaS use (bundling the binary into a product distributed to third-party customers) requires a separate commercial license.** Contact cloakhq@pm.me.

---

## 7. Khi vẫn bị block — checklist debug / When you're still blocked — debug checklist

### VN

Theo README, hầu hết các tình huống bị block KHÔNG phải do fingerprint mà do:

1. **IP reputation kém** — datacenter IP thường bị flag. Dùng residential proxy.
2. **Timezone/locale không khớp với IP** — bật `geoip=True` để auto-detect từ proxy exit IP.
3. **Headless mode bị nhận diện** — dùng `headless=False` cho site khó.
4. **Hành vi quá nhanh** — bật `humanize=True` để mô phỏng người.

Recommended config cho site khó:
```python
browser = launch(
    proxy="http://residential-proxy:port",
    geoip=True,
    headless=False,
    humanize=True,
)
```

### EN

Per README, most blocks are NOT due to fingerprint issues but due to:

1. **Poor IP reputation** — datacenter IPs frequently flagged. Use residential proxies.
2. **Timezone/locale mismatch with IP** — enable `geoip=True` for auto-detection from proxy exit IP.
3. **Headless mode detected** — use `headless=False` for aggressive sites.
4. **Behavior too fast** — enable `humanize=True` for human simulation.

Recommended config for aggressive sites:
```python
browser = launch(
    proxy="http://residential-proxy:port",
    geoip=True,
    headless=False,
    humanize=True,
)
```

---

## 8. Cảnh báo pháp lý + đạo đức / Legal + ethical warnings

### VN

⚠️ **Đây là tool dual-use.** Tự bạn chịu trách nhiệm về cách sử dụng.

- **Tôn trọng robots.txt** — nếu site cấm scraping, đừng scrape (kể cả nếu bạn có thể bypass)
- **Tôn trọng rate limit** — đừng làm gián đoạn dịch vụ
- **Tôn trọng ToS** — đọc Terms of Service trước khi automation
- **Có sự đồng ý khi test** — chỉ kiểm tra hệ thống bạn có quyền
- **Tuân thủ pháp luật bản địa** — luật có thể khác giữa các quốc gia (vd: CFAA tại Mỹ, GDPR tại EU)
- **Indemnification** — BINARY-LICENSE yêu cầu bạn bồi thường cho CloakHQ nếu họ bị kiện vì hành động của bạn

Khi nghi ngờ: **hỏi luật sư**, không hỏi AI.

### EN

⚠️ **This is a dual-use tool.** You bear responsibility for its use.

- **Respect robots.txt** — if a site disallows scraping, don't scrape (even if you can bypass)
- **Respect rate limits** — don't disrupt services
- **Respect ToS** — read Terms of Service before automating
- **Get consent before testing** — only test systems you have authorization for
- **Comply with local law** — laws vary by jurisdiction (e.g., CFAA in US, GDPR in EU)
- **Indemnification** — BINARY-LICENSE requires you to indemnify CloakHQ for legal exposure arising from your actions

When in doubt: **consult a lawyer**, not an AI.

---

## 9. So sánh với các tool stealth khác / Comparison with other stealth tools

### VN

Theo README, CloakBrowser định vị là vượt trội về kỹ thuật:

| Tính năng | playwright-stealth | undetected-chromedriver | Camoufox | CloakBrowser |
|---|---|---|---|---|
| Cấp độ patch | JS injection | Config patches | C++ (Firefox) | **C++ (Chromium)** |
| reCAPTCHA v3 score | 0.3-0.5 | 0.3-0.7 | 0.7-0.9 | **0.9** |
| Cloudflare Turnstile | Đôi khi | Đôi khi | Pass | **Pass** |
| Survives Chrome updates | Hay vỡ | Hay vỡ | Yes | **Yes** |
| Maintenance | Stale | Stale | Unstable | **Active** |
| Playwright API | Native | Native | Không | **Native** |

**Honest disclosure:** CloakBrowser công khai thừa nhận Camoufox đạt 0.7-0.9 reCAPTCHA — gần CloakBrowser. Không tự xưng là vượt trội tuyệt đối.

### EN

Per README, CloakBrowser positions itself as technically superior:

| Feature | playwright-stealth | undetected-chromedriver | Camoufox | CloakBrowser |
|---|---|---|---|---|
| Patch level | JS injection | Config patches | C++ (Firefox) | **C++ (Chromium)** |
| reCAPTCHA v3 score | 0.3-0.5 | 0.3-0.7 | 0.7-0.9 | **0.9** |
| Cloudflare Turnstile | Sometimes | Sometimes | Pass | **Pass** |
| Survives Chrome updates | Breaks often | Breaks often | Yes | **Yes** |
| Maintenance | Stale | Stale | Unstable | **Active** |
| Playwright API | Native | Native | No | **Native** |

**Honest disclosure:** CloakBrowser openly acknowledges Camoufox scores 0.7-0.9 reCAPTCHA — close to CloakBrowser. Doesn't claim absolute superiority.

---

## 10. Tích hợp với framework / Framework integrations

### VN

CloakBrowser tương thích với các framework automation:

| Framework | Mô tả | Status |
|-----------|------|--------|
| browser-use | Python agent browser framework (70K stars) | Documented |
| Crawl4AI | LLM-friendly scraper (58K stars) | Documented + CloakHQ FORK exists |
| Crawlee | Apify Python scraper (8.6K stars) | Documented + CloakHQ FORK exists |
| Scrapling | Python scraper (21K stars) | Documented |
| Stagehand | TypeScript agent browser (BrowserBase, 21K stars) | Documented |
| LangChain | LLM framework (100K+ stars) | Documented |
| Selenium | Browser automation classic | Documented |

Có 2 mode tích hợp:
- **Mode 1:** Framework launch binary của CloakBrowser
- **Mode 2:** CloakBrowser launch trước, framework connect qua CDP

### EN

CloakBrowser is compatible with automation frameworks:

| Framework | Description | Status |
|-----------|-------------|--------|
| browser-use | Python agent browser framework (70K stars) | Documented |
| Crawl4AI | LLM-friendly scraper (58K stars) | Documented + CloakHQ FORK exists |
| Crawlee | Apify Python scraper (8.6K stars) | Documented + CloakHQ FORK exists |
| Scrapling | Python scraper (21K stars) | Documented |
| Stagehand | TypeScript agent browser (BrowserBase, 21K stars) | Documented |
| LangChain | LLM framework (100K+ stars) | Documented |
| Selenium | Browser automation classic | Documented |

Two integration modes:
- **Mode 1:** Framework launches CloakBrowser's binary
- **Mode 2:** CloakBrowser launches first; framework connects via CDP

---

## 11. Lộ trình thử nghiệm an toàn (4 tuần) / Safe experimentation roadmap (4 weeks)

### VN

**Tuần 1 — Hiểu công cụ**
- Cài đặt + chạy `cloaktest` (test script tích hợp)
- Đọc README đầy đủ, đặc biệt là Section "Test Results" + "Comparison Table"
- Đọc BINARY-LICENSE.md đầy đủ, chú ý Section "Acceptable Use"
- Thử Hello World trên `https://example.com`

**Tuần 2 — Site testing hợp pháp**
- Chạy `examples/fingerprint_scan_test.py` để hiểu fingerprint
- Chạy `examples/recaptcha_score.py` (trên demo site, KHÔNG trên site thật chưa được cho phép)
- So sánh kết quả với standard Playwright

**Tuần 3 — Persistent profile + proxy**
- Setup persistent profile với `launch_persistent_context()`
- (Nếu cần) thêm residential proxy hợp pháp + `geoip=True`
- Hiểu cách `humanize=True` thay đổi behavior

**Tuần 4 — Đánh giá use case**
- Đánh giá xem use case của bạn có nằm trong Acceptable Use không
- Đọc ToS của site target
- (Nếu doubt) hỏi luật sư hoặc compliance team
- Quyết định: tiến tới production hay dừng lại

⚠️ **Trong cả 4 tuần:** chỉ test trên các site bạn có quyền hoặc demo site công khai.

### EN

**Week 1 — Understanding the tool**
- Install + run `cloaktest` (built-in test script)
- Read full README, especially "Test Results" + "Comparison Table" sections
- Read full BINARY-LICENSE.md, pay attention to "Acceptable Use" section
- Try Hello World on `https://example.com`

**Week 2 — Legitimate site testing**
- Run `examples/fingerprint_scan_test.py` to understand fingerprinting
- Run `examples/recaptcha_score.py` (on demo sites, NOT on production sites without authorization)
- Compare results with standard Playwright

**Week 3 — Persistent profile + proxy**
- Set up persistent profile with `launch_persistent_context()`
- (If needed) add legitimate residential proxy + `geoip=True`
- Understand how `humanize=True` changes behavior

**Week 4 — Use case evaluation**
- Evaluate whether your use case falls within Acceptable Use
- Read ToS of target site
- (If in doubt) consult legal counsel or compliance team
- Decide: proceed to production or stop

⚠️ **Throughout all 4 weeks:** only test against sites you have authorization for or public demo sites.

---

## 12. Tại sao CloakBrowser quan trọng / Why CloakBrowser matters

### VN

CloakBrowser là **chủ thể đầu tiên trong 68-wiki corpus được xây dựng chuyên cho stealth/anti-detection**. Các chủ thể trước có stealth như là một feature trong một product lớn hơn (browser-use, crawl4ai, Skyvern). CloakBrowser đảo ngược tỉ lệ: stealth LÀ product, mọi thứ khác là support.

Đây là quyết định kiến trúc cấp **purpose-built-for-stealth** vs **stealth-as-feature** — quan trọng vì:
1. Đầu tư patch sâu hơn (57 C++ patches vs runtime JS injection)
2. Bảo trì tập trung hơn (1 release/3 ngày sustained)
3. Áp dụng nguyên tắc "single-axis differentiation that's deeply technical"
4. License-axis cũng được tối ưu hóa cho dual-use risk-mitigation

### EN

CloakBrowser is **the corpus-first dedicated-stealth subject across 68 wikis**. Prior subjects had stealth as one feature in a larger product (browser-use, crawl4ai, Skyvern). CloakBrowser inverts the proportion: stealth IS the product; everything else is support.

This is a **purpose-built-for-stealth** vs **stealth-as-feature** architectural decision — important because:
1. Deeper patch investment (57 C++ patches vs runtime JS injection)
2. More focused maintenance (sustained 1 release every 3 days)
3. Applies "single-axis differentiation that's deeply technical" principle
4. License-axis also optimized for dual-use risk-mitigation

---

## 13. Đọc thêm / Further reading

### VN

- **README**: [github.com/CloakHQ/CloakBrowser#readme](https://github.com/CloakHQ/CloakBrowser#readme) — đầy đủ API + comparison + troubleshooting
- **BINARY-LICENSE**: [github.com/CloakHQ/CloakBrowser/blob/main/BINARY-LICENSE.md](https://github.com/CloakHQ/CloakBrowser/blob/main/BINARY-LICENSE.md) — quan trọng nếu dùng commercial
- **CHANGELOG**: [github.com/CloakHQ/CloakBrowser/blob/main/CHANGELOG.md](https://github.com/CloakHQ/CloakBrowser/blob/main/CHANGELOG.md) — patch progression theo thời gian
- **Issues**: [github.com/CloakHQ/CloakBrowser/issues](https://github.com/CloakHQ/CloakBrowser/issues)
- **Homepage**: [cloakbrowser.dev](https://cloakbrowser.dev)
- **Pattern Library Pattern #45**: trong vault này, để hiểu license-axis context

**Corpus siblings** (cũng trong vault này):
- v29 crawl4ai — LLM-friendly scraper
- v34 browser-use — Agent browser framework
- v24 Skyvern — Auth-aware automation
- v23 Unsloth — Pattern #45 sub-variant 45a sibling
- v59 AutoGPT — Pattern #45 sub-variant 45b sibling

### EN

- **README**: [github.com/CloakHQ/CloakBrowser#readme](https://github.com/CloakHQ/CloakBrowser#readme) — full API + comparison + troubleshooting
- **BINARY-LICENSE**: [github.com/CloakHQ/CloakBrowser/blob/main/BINARY-LICENSE.md](https://github.com/CloakHQ/CloakBrowser/blob/main/BINARY-LICENSE.md) — critical for commercial use
- **CHANGELOG**: [github.com/CloakHQ/CloakBrowser/blob/main/CHANGELOG.md](https://github.com/CloakHQ/CloakBrowser/blob/main/CHANGELOG.md) — patch progression over time
- **Issues**: [github.com/CloakHQ/CloakBrowser/issues](https://github.com/CloakHQ/CloakBrowser/issues)
- **Homepage**: [cloakbrowser.dev](https://cloakbrowser.dev)
- **Pattern Library Pattern #45**: in this vault, for license-axis context

**Corpus siblings** (also in this vault):
- v29 crawl4ai — LLM-friendly scraper
- v34 browser-use — Agent browser framework
- v24 Skyvern — Auth-aware automation
- v23 Unsloth — Pattern #45 sub-variant 45a sibling
- v59 AutoGPT — Pattern #45 sub-variant 45b sibling

---

**Closing note / Lời kết:**

VN: Đây là **knowledge-base documentation**, không phải tutorial vận hành chống bot. Nếu bạn cần làm bypass cụ thể, hãy: (a) đảm bảo bạn có quyền pháp lý, (b) đọc ToS site target, (c) hỏi luật sư khi có doubt, (d) dùng tool có trách nhiệm.

EN: This is **knowledge-base documentation**, not an operational anti-bot tutorial. If you need to perform specific bypass work: (a) ensure you have legal authorization, (b) read target site ToS, (c) consult a lawyer when in doubt, (d) use the tool responsibly.

— v69 wiki · 2026-05-18 · CloakHQ/CloakBrowser
