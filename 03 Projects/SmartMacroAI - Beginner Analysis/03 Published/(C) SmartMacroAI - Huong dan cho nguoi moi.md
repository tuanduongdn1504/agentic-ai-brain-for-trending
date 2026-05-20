# (C) SmartMacroAI — Hướng dẫn cho người mới

> **Subject (URL)**: [tronieph.github.io/SmartMacroAI-Website/](https://tronieph.github.io/SmartMacroAI-Website/)
> **Substrate product**: [TroniePh/SmartMacroAI](https://github.com/TroniePh/SmartMacroAI)
> **Wiki version**: v80 (SIXTEENTH under routine v2.2)
> **Storm Bear strength**: **WEAK INCLUDE 1/4** (only (a) STRONG PASS via VN-LOCATED cultural-peer)
> **Bilingual**: VN primary, EN technical

## Phần 1 — Đây là gì? (What is it?)

**Tóm tắt 1 câu (VN)**: SmartMacroAI là phần mềm RPA (tự động hóa) cho Windows do Phạm Quốc Duy (lập trình viên Việt Nam) phát triển — kết hợp 4 chế độ nhập liệu (Stealth + Raw Input + Hardware + Driver Level Kernel) + computer vision + OCR + tích hợp OpenAI/Gemini làm OPTION TÙY CHỌN cho quyết định thông minh, miễn phí vĩnh viễn.

**One-line (EN)**: Windows-desktop RPA framework by VN-LOCATED solo developer Phạm Quốc Duy; 4-input-mode architecture + Computer Vision + OCR + Optional LLM-augmented decision-making (OpenAI + Gemini APIs) as one-of-many tool modes; perpetually free; .NET 8 + WPF.

**Phân biệt với corpus subjects khác** (Distinction from other corpus subjects):
- KHÔNG phải LLM-orchestration-brain framework (như v9 autoresearch / v79 autoresearch_folktales)
- KHÔNG phải Claude Code skill hay agent-framework (như v75 / v76 / v78)
- LÀ END-USER APPLICATION với LLM là 1 TOOL trong nhiều TOOLS
- **NEW T5 sub-archetype** "Hybrid-RPA-with-LLM-augmented-decision-making" PROVISIONAL N=1

## Phần 2 — Tín hiệu corpus-first / Corpus-first signals

**12 quan sát corpus-first**:

1. **CORPUS-FIRST Apple-Silicon-free Windows-only** end-user product với LLM integration trong v60+ window
2. **CORPUS-FIRST 4-input-mode automation architecture** (Stealth + Raw Input + Hardware + Driver Level Kernel)
3. **CORPUS-FIRST Driver-Level-Kernel-mode** for anti-cheat-bypass trong v60+ window (ethically-ambiguous; documented honestly)
4. **CORPUS-FIRST LLM-inversion-architecture** (LLM-as-callable-tool vs LLM-as-orchestration-brain)
5. **CORPUS-FIRST OpenAI + Gemini dual-AI-API integration** at solo developer scale
6. **CORPUS-FIRST CDP-Stealth (Chrome DevTools Protocol)** integration in v60+ window
7. **CORPUS-FIRST 830+ localization keys at solo developer scale** = depth-of-translation rather than breadth-of-locales
8. **CORPUS-FIRST dual-repo separation** (product + marketing site as distinct repos) at solo developer scale
9. **CORPUS-FIRST Facebook-share-distribution-channel evidence** in v60+ window (via fbclid in submitted URL)
10. **CORPUS-FIRST hybrid-donation-channel-localization** (MB Bank VN-domestic + PayPal international)
11. **CORPUS-FIRST unambiguous-absent-LICENSE-at-Apache-bundle-scale** (404-confirmed; bundles Apache 2.0 dependencies)
12. **CORPUS-FIRST Bézier-mouse-curves anti-detection discipline** in v60+ window

**Corpus-records (4)**:
1. **NEW CORPUS-RECORD-HIGH fork_ratio 0.765 = 76.5%** active-deployment-intent (3-wiki sustained ladder: v76 0.296 → v79 0.484 → v80 0.765)
2. **NEW CORPUS-RECORD Storm Bear streak 16** (extending v79's 15-record)
3. **NEW CORPUS-RECORD 9-consecutive-wiki active count UNCHANGED** post-v72-audit-relief (extending v79's 8-record)
4. **NEW CORPUS-RECORD INCLUDE rate 91.7%** (22/24 = 0.917 vs v79's 91.3%)

## Phần 3 — Tier placement & Archetype

**Tier**: T5 Application — **NEW sub-archetype "Hybrid-RPA-with-LLM-augmented-decision-making"** PROVISIONAL N=1

**Archetype**: solo-VN-LOCATED-developer-with-dual-repo-marketing-discipline (Pattern #19 NEW sub-mechanism 19k candidate)

**Scale**: small (<5K stars; 17 stars at 40 days)

**Verified GitHub metadata (2026-05-20)**:
- Product (`TroniePh/SmartMacroAI`): 17 stars / 13 forks / 0 subscribers / 0 issues / C# / NOASSERTION license / created 2026-04-10 / pushed 2026-05-13
- Marketing site (`TroniePh/SmartMacroAI-Website`): 0 stars / 0 forks / HTML / license None / created+pushed same dates

## Phần 4 — Cài đặt nhanh (Quick installation)

**Yêu cầu (Requirements)**:
- Windows 10 x64 (build 19041+) hoặc Windows 11
- .NET 8.0 runtime (đã bundle trong installer)
- 4 GB RAM tối thiểu
- 300 MB ổ cứng (core) / 600 MB (với Web Automation)
- Quyền Administrator (cho Driver Level mode)

**Cài đặt qua installer** (recommended for beginners):

```
1. Truy cập: https://github.com/TroniePh/SmartMacroAI/releases/latest
2. Tải SmartMacroAI-v1.6.0-Setup.exe
3. Chạy file installer, làm theo wizard
4. Mở SmartMacroAI từ Start Menu
```

**Hoặc cài đặt portable**:
```
1. Tải SmartMacroAI-v1.6.0-win-x64.exe HOẶC .zip
2. Nếu .zip: giải nén ra folder
3. Chạy SmartMacroAI.exe trực tiếp (không cần install)
```

**Build from source** (cho developers):
```bash
git clone https://github.com/TroniePh/SmartMacroAI.git
cd SmartMacroAI
dotnet restore
dotnet build
dotnet run
```

## Phần 5 — Cách sử dụng cốt lõi (Core usage pattern)

**3-step Getting Started** (từ website):
1. **Select Target** — chọn cửa sổ Windows hoặc tab browser muốn auto
2. **Build Script** — kéo-thả các action (click / type / image-recognition / OCR / if-else / loop)
3. **Run & Enjoy** — chạy macro

**4 chế độ Input (Input Modes)**:

| Mode | Cơ chế | Anti-detection | Use case |
|------|--------|-----------------|----------|
| **Stealth** | Win32 PostMessage gửi tới message queue cửa sổ | CAO (không chiếm chuột) | Auto chạy nền khi bạn vẫn làm việc |
| **Raw Input** | Win32 SendInput với hardware scan codes | TRUNG | Auto thông thường cần focus toàn hệ |
| **Hardware** | SetCursorPos + mouse_event | THẤP (chuột chạy nhìn thấy) | App khó tính từ chối SendInput |
| **Driver Level** | Kernel Interception driver (cần admin + cài driver) | CAO NHẤT (kernel-level) | Game có anti-cheat |

**Logic conditional**:
- Image recognition (multi-image search up to 20 per action; v1.6.0)
- Pixel color detection
- OCR text matching (Tesseract 5.2)
- If/Else branching
- Loop (count / infinite / break)
- CSV auto-fill
- **AI fallback (OpenAI / Gemini)** cho quyết định phức tạp (tùy chọn)

**Anti-Detection**:
- Bézier mouse curves (chuột đi theo đường cong tự nhiên thay vì thẳng)
- Randomized delays (delay ngẫu nhiên giữa các action)

## Phần 6 — Khái niệm + lựa chọn kiến trúc mới mẻ (Novel concepts / key architectural choices)

### LLM-Inversion-Architecture (CORPUS-FIRST)

Hầu hết corpus subjects (v9 / v66 / v75 / v78 / v79) đặt LLM ở vị trí orchestration-brain — LLM điều khiển vòng lặp và gọi tools. SmartMacroAI **đảo ngược**: rule-based engine làm orchestration; LLM chỉ là 1 trong nhiều tool-mode options (cùng với image-recognition / pixel-detection / OCR / template-matching).

**Implication**: với SmartMacroAI, bạn KHÔNG cần API key của OpenAI/Gemini cho hầu hết macros. Macros chạy bằng rule-based logic (image conditions + pixel conditions + OCR matching). LLM chỉ được gọi khi gặp tình huống "thông minh" như: "kiểm tra xem màn hình có đang show X không?" mà các rule cứng không match được.

### 4-input-mode choice-architecture

Đây là **CORPUS-FIRST** mô hình kiến trúc — đa số tool automation chỉ cung cấp 1-2 modes. SmartMacroAI cho 4 modes với trade-off rõ ràng giữa anti-detection vs reliability vs system-permission cost.

### Localization-Depth vs Locale-Breadth

So với v77 easy-vibe có 13 locales (BREADTH), v80 SmartMacroAI có 2 locales (EN + VN) NHƯNG 830+ keys mỗi locale = **DEPTH-of-translation** thay vì BREADTH. 2-locale × 830+ keys = 1,660+ translations. Approach hoàn toàn khác.

## Phần 7 — So sánh với corpus framework khác (vs other corpus frameworks)

| Axis | v9 autoresearch (Karpathy) | v44 browser-use | v79 autoresearch_folktales | **v80 SmartMacroAI** |
|------|-----------------------------|-----------------|----------------------------|----------------------|
| **Tier** | T5 | T2/T5 | T5 | **T5 NEW sub-archetype** |
| **LLM role** | Orchestration brain | Browser-control orchestration | Orchestration brain (inherits) | **Tool-mode option (NEW)** |
| **OS target** | Linux / GPU | Cross-platform | Apple Silicon only | **Windows only** |
| **Hardware target** | NVIDIA GPU | CPU | Apple Silicon MPS | **Windows x64** |
| **Distribution** | git clone + manual | pip install | uv-exclusive | **GitHub Releases binary (3 formats)** |
| **License** | (verify) | MIT | NOASSERTION (no LICENSE file) | **NOASSERTION (404-confirmed)** |
| **Author archetype** | Founder solo (Karpathy) | (verify) | Solo VN-diaspora YouTuber | **Solo VN-LOCATED indie** |
| **User type** | ML researcher | Web automation engineer | LLM experimenter | **RPA practitioner / gamer / power-user** |

## Phần 8 — Ethical framing / Khung đạo đức

**Anti-detection và anti-cheat considerations**:

SmartMacroAI **công khai mention "anti-cheat support"** trong README — kernel-level Driver Level mode được thiết kế để bypass game anti-cheat systems.

**Potential use cases (ethical spectrum)**:
- **LEGITIMATE**: Office automation / data entry / web scraping / testing / accessibility for disabled users
- **GREY**: Background gaming auto-clickers (some games allow; some prohibit)
- **HARMFUL**: Bot farming / cheat-tool for competitive games / mass-account creation / spam

**Decision burden on user**: SmartMacroAI is a TOOL; ethics are on USER. Like AutoHotkey or Pulover before it.

**Risks**:
- **Driver-level kernel mode** requires admin permission + custom-driver install → privileges-escalation surface
- **LLM API key handling**: README mentions OpenAI + Gemini integration but NO SECURITY.md / no key-rotation discussion → bring-your-own-key with no built-in safety net
- **No SBOM / no signed releases** → supply-chain trust requires manual verification

**Recommendation**:
- Verify download from official GitHub Releases (not third-party mirrors)
- Run in sandboxed Windows VM for sensitive scenarios
- Don't use for any competitive-game automation where ToS prohibits

## Phần 9 — Storm Bear relevance (VN operator + Scrum coach fit)

**Storm Bear strength**: **WEAK INCLUDE 1/4** (only (a) STRONG PASS)

| Criterion | Status | Tóm tắt |
|-----------|--------|---------|
| (a) Author-archetype peer | **STRONG PASS** | Phạm Quốc Duy = VN-LOCATED solo developer (MB Bank account + Vietnamese-first + "Made with ❤️ in Vietnam"); SECOND VN-LOCATED solo dev cluster N=2 sau v76 HoangNguyen0403 |
| (b) Vault-deployable for Scrum | **FAIL** | Windows-only desktop RPA; vault operator dùng macOS; domain mismatch with Scrum coaching |
| (c) Methodology-influence-node | **FAIL** | LLM-inversion + 4-input-mode + Bézier-curves là technical patterns, không phải methodology cho vault routine v2.2+ |
| (d) Corpus-citation | **FAIL** | Không cite corpus subject nào; chỉ cite AutoHotkey + Pulover (NOT in corpus) |

**Methodological takeaways (intellectual reference; không actionable)**:
- LLM-inversion-architecture có thể inspire vault routine design — vault routine v2.2 hiện đặt LLM (Claude) ở vị trí orchestration; v80 chứng minh inversion (LLM-as-callable-tool) có thể hoạt động
- Dual-repo-marketing-discipline ở solo dev scale là sister-pattern với vault Storm Bear's `00 Notes/` (raw) vs `03 Published/` (curated) separation

**Cultural-peer takeaways**:
- 2-wiki VN-LOCATED solo dev cluster (v76 + v80) trong v60+ window = VN dev community đang produce corpus-relevant artifacts
- 830+ localization keys depth = aspirational benchmark cho any VN-focused product

**Streak**: v80 extends Storm Bear streak từ 15 (v65-v79) → **16 consecutive PASS post-v64-RESET = NEW CORPUS-RECORD extension by 1 wiki**.

## Phần 10 — 4-week learning roadmap

**Tuần 1: Setup + first macro**
- [ ] Cài SmartMacroAI từ GitHub Releases
- [ ] Đọc README đầy đủ (bilingual)
- [ ] Thử Smart Recorder để record 1 macro click sequence
- [ ] Chạy macro trong Hardware mode + Stealth mode để hiểu khác biệt
- **Outcome**: workflow basics + chế độ input nào phù hợp

**Tuần 2: Image recognition + OCR**
- [ ] Tạo macro với image recognition (e.g., click khi thấy button X)
- [ ] Tạo macro với OCR text matching
- [ ] Combine image + OCR + pixel-color conditions
- [ ] Use ROI picker để optimize performance
- **Outcome**: hiểu computer vision pipeline

**Tuần 3: LLM-augmented decision**
- [ ] Setup OpenAI + Gemini API keys (paid; bring-your-own)
- [ ] Tạo macro có LLM-fallback decision (e.g., "if image not found, ask GPT-4 if screen state X")
- [ ] So sánh cost (LLM API calls) vs accuracy
- [ ] Hiểu trade-off rule-based vs LLM-augmented
- **Outcome**: hiểu khi nào nên + không nên dùng LLM

**Tuần 4: Architecture takeaways**
- [ ] Đọc code (.NET 8 + WPF + Win32 API + 4-input-modes)
- [ ] Reflect: LLM-inversion-architecture có thể apply ở vault routine nào?
- [ ] So sánh với corpus siblings (v9 autoresearch / v44 browser-use / v79 autoresearch_folktales)
- **Outcome**: methodology-level insights transferable beyond Windows RPA domain

## Phần 11 — Tradeoffs + limitations

**Trade-offs (intentional design)**:

| Trade-off | Reason | Cost |
|-----------|--------|------|
| Windows-only | Solo developer focus + .NET 8 + Win32 native | No macOS / Linux / mobile |
| 4-input-mode complexity | Coverage of anti-detection trade-offs | Cognitive load for new users |
| LLM-as-tool-mode (not orchestration) | LLM optional; rule-based default | Less "smart"-by-default |
| GitHub Releases binary (no app store) | Free distribution; no signing fees | No automatic update + no Microsoft Store discovery |
| No LICENSE file | (unclear intent) | License-compatibility uncertain for bundle |

**Limitations**:
- Windows-only (no cross-platform)
- No mobile / no web app version
- Requires admin permission for Driver Level mode
- Anti-cheat use case raises ethical considerations
- Solo developer = bus-factor risk
- No automated tests visible
- No SECURITY.md / no responsible-disclosure policy

## Phần 12 — Caveats + safety notes

**Supply-chain awareness**:
- NO LICENSE file in repo (404-verified) — license-enforceability uncertain
- Bundles Apache 2.0 + MS-PL + custom-licensed dependencies under no-license-of-its-own
- No SBOM / no signed releases / no signed commits
- Interception Driver requires kernel-level install — privilege-escalation surface

**AI API considerations**:
- User provides own OpenAI + Gemini keys
- No built-in cost tracking
- No rate-limiting discussion in README
- API keys + macro logic on same local system → keys exposure if macro logic shared

**Anti-cheat ethical framing**:
- README explicitly mentions kernel-level Driver Level mode for anti-cheat
- This is a USE CASE — agent doesn't endorse / encourage
- Verify game ToS before using; some prohibit kernel-input even for legitimate accessibility

**Vault operator-specific**:
- (b) FAIL means vault operator can't directly deploy
- Methodological-takeaways exist but require intellectual translation

## Phần 13 — Tài liệu tham khảo + Bước tiếp theo

**External references**:
1. [TroniePh/SmartMacroAI](https://github.com/TroniePh/SmartMacroAI) — product repo
2. [tronieph.github.io/SmartMacroAI-Website/](https://tronieph.github.io/SmartMacroAI-Website/) — marketing site (= submitted URL)
3. [GitHub Releases](https://github.com/TroniePh/SmartMacroAI/releases/latest) — binary downloads
4. [GitHub Issues](https://github.com/TroniePh/SmartMacroAI/issues) — bug reports

**Cross-wiki sibling references**:
- v76 [agent-skills-standard (Hanoi VN solo dev)](../agent-skills-standard%20-%20Beginner%20Analysis/) — VN-LOCATED structural-peer cluster
- v77 [easy-vibe (13-locale i18n)](../easy-vibe%20-%20Beginner%20Analysis/) — locale-breadth vs v80 depth
- v44 [browser-use](../browser-use%20-%20Beginner%20Analysis/) — Playwright sibling
- v79 [autoresearch_folktales](../autoresearch_folktales%20-%20Beginner%20Analysis/) — Storm Bear streak adjacency + fork_ratio CORPUS-RECORD ladder

**Next action suggestions (cho Storm Bear)**:
1. **Đọc `01 Analysis/(C) T5-NEW-sub-archetype-... .md`** cho formal Pattern Library proposal-document
2. **Note "LLM-inversion-architecture"** is a Library-vocabulary candidate worth tracking — could inform vault routine v2.2+ design considerations
3. **Decide v85 audit scope** — NEW T5 sub-archetype 80a stale-check + Library-vocabulary candidates filing decisions
4. **Reflect on 2-wiki VN-LOCATED cluster** — v76 + v80 = VN dev community signal
5. **Consider Facebook-share-distribution-channel as Phase 0 evidence axis** for future wiki builds

**Bước cụ thể nếu Storm Bear muốn thử SmartMacroAI**:
- Bạn có Windows machine không? → có thể chạy local
- Bạn có cụ thể automation need không? → identify before download
- Bạn muốn experiment LLM-as-tool-mode pattern? → cần OpenAI/Gemini API keys

→ **Recommendation**: **SKIP RUNNING**. Harvest methodological takeaways từ entity pages + Pattern Library implications. Subject domain mismatch.
