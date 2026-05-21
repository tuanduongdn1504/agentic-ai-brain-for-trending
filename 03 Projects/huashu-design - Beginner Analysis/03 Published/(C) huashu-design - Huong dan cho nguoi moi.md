# huashu-design — Hướng dẫn cho người mới (Trilingual EN/VN/zh-reference)

> Wiki v82 — 花叔 / Huasheng (Hua Shu) / China · MIT (relicensed 2026-05-14) · `huasheng.ai` + `bookai.top` · 14,478 stars / 1,965 forks / 32 days at fetch
> [GitHub repo](https://github.com/alchaincyf/huashu-design)

---

## What is huashu-design? / huashu-design là gì? / huashu-design 是什么?

**EN**: huashu-design is a **monolithic Claude Code skill** that turns terminal-agent typing into finished designs. Tagline: *"Type. Hit enter. A finished design lands in your lap."* It outputs HTML, MP4, GIF, editable PPTX, PDF, and 60fps animations — so it's not just design rules but an actual multimedia-output toolchain.

**VN**: huashu-design là một **Claude Code skill monolithic** (đơn-skill, không bundle nhiều skill như v81 taste-skill) — biến việc gõ trong terminal agent thành thiết kế hoàn chỉnh. Slogan: *"Gõ. Bấm enter. Một thiết kế giao được tới tay bạn."* Output gồm HTML, MP4, GIF, PPTX có thể chỉnh sửa, PDF, và animation 60fps — tức là không chỉ luật thiết kế mà còn cả toolchain multimedia.

**zh**: huashu-design 是一个**单体 Claude Code 设计 skill**(不像 v81 taste-skill 那样拆成 12 个 skill bundle)。标语:"打字。回车。一份能交付的设计。" 输出包括 HTML、MP4、GIF、可编辑 PPTX、PDF、以及 60fps 动画 — 不只是设计规则,而是真正的多媒体输出 toolchain。

---

## Why does it exist? / Vì sao nó ra đời?

**EN**: The author 花叔 (Hua Shu) played with Anthropic's Claude Design product until 4 a.m. on its launch day, then never opened it again — not because it was bad ("the most polished product in the category") but because they preferred an agent working in the terminal over any graphical UI. So they **reverse-engineered Claude Design's system prompts and brand asset protocols** and reimplemented them as a Claude Code skill — with explicit Anti-Slop additions.

**VN**: Tác giả 花叔 chơi với sản phẩm Claude Design của Anthropic đến 4 giờ sáng ngày ra mắt, sau đó không mở lại nữa — không phải vì nó tệ ("sản phẩm chỉn chu nhất trong category") mà vì tác giả thích agent làm việc trong terminal hơn là GUI đồ họa. Vậy nên tác giả **reverse-engineer system prompts + brand asset protocols của Claude Design** rồi tái triển khai dưới dạng Claude Code skill — kèm thêm phần Anti-Slop.

---

## How to install / Cài đặt thế nào

**EN**: One command via Claude Code's standard skill install (shorthand owner/repo form):

**VN**: Một lệnh qua câu lệnh cài skill chuẩn của Claude Code (dạng shorthand owner/repo):

```bash
npx skills add alchaincyf/huashu-design
```

**EN**: Unlike v81 taste-skill (which needs `--skill` flag for per-skill choice), v82 is monolithic so no flag is needed.

**VN**: Khác với v81 taste-skill (cần flag `--skill` để chọn từng skill), v82 là monolithic nên không cần flag.

---

## The 5-mechanic methodology / 5 cơ chế phương pháp luận

### 1. Core Asset Protocol — Mandatory for brand work / Bắt buộc khi làm brand

**EN**: 5-step process: Ask → Search → Download → Verify → Freeze to spec. Philosophy: *"great hi-fi design doesn't start from a blank page, it grows from existing design context."*

**VN**: Quy trình 5 bước: Hỏi → Tìm → Tải → Xác minh → Đóng băng vào spec. Triết lý: "Thiết kế hi-fi tốt không bắt đầu từ trang trắng — nó nảy nở từ ngữ cảnh thiết kế có sẵn."

### 2. Design Direction Advisor / Cố vấn hướng thiết kế

**EN**: Recommends 3 differentiated directions from a "5 schools × 20 philosophies" = 100-philosophy taxonomy when briefs are vague.

**VN**: Đề xuất 3 hướng khác biệt từ taxonomy "5 trường phái × 20 triết lý" = 100 triết lý khi brief mơ hồ.

### 3. Junior Designer Workflow / Quy trình designer junior

**EN**: Show work early with assumptions + placeholders, then iterate.

**VN**: Show sớm bản nháp với giả định + placeholder, rồi lặp đi lặp lại.

### 4. Fact Verification First / Xác minh sự thật trước

**EN**: Uses WebSearch to confirm products/technologies mentioned in tasks rather than relying on training-data alone.

**VN**: Dùng WebSearch để xác minh sản phẩm/công nghệ trong task thay vì chỉ dựa vào training data.

### 5. Anti AI-slop Rules / Luật chống AI-slop

**EN**: Avoids common AI visual tropes using `text-wrap: pretty` + CSS Grid + carefully chosen serif display faces + `oklch` colors. Avoids purple gradients, emoji icons, rounded corners with left borders, SVG silhouettes.

**VN**: Tránh các sáo mòn AI thường gặp bằng `text-wrap: pretty` + CSS Grid + serif display fonts chọn kỹ + màu `oklch`. Tránh gradient tím, emoji icons, bo tròn với left border, SVG silhouettes.

---

## Who is 花叔 (Hua Shu / Huasheng)? / 花叔 là ai? / 花叔是谁?

**EN**: 花叔 (Chinese for "Uncle Hua", Latinized "Huasheng" or "Huashu") is a **China-Mainland-located solo developer** who self-identifies as *"AI Native Coder. Ship products without writing code."* Track record:
- **Cat Fill Light** (iOS App Store Top 1 in Paid category)
- ***A Book on DeepSeek*** (book authorship)
- **Nüwa.skill** (separate GitHub Claude Code skill with 12k+ stars)
- **300k+ followers across platforms**
- Domains: `huasheng.ai` (brand) + `bookai.top` (developer hub)
- Twitter: @AlchainHust (handle suggests possible HUST = Huazhong University of Science and Technology alumni)

**VN**: 花叔 (tiếng Trung nghĩa "Bác Hoa", Latin "Huasheng" hoặc "Huashu") là **solo developer ở Trung Quốc Đại Lục**, tự nhận là *"AI Native Coder. Ship sản phẩm không cần viết code."* Thành tích:
- **Cat Fill Light** (Top 1 paid app iOS App Store)
- ***Sách về DeepSeek*** (tác giả sách)
- **Nüwa.skill** (Claude Code skill khác trên GitHub, 12k+ sao)
- **300k+ followers trên các nền tảng**
- Domains: `huasheng.ai` (brand) + `bookai.top` (developer hub)
- Twitter: @AlchainHust (handle gợi ý cựu sinh viên HUST = Đại học Khoa học và Công nghệ Hoa Trung)

---

## Comparison with v75 impeccable + v81 taste-skill / So sánh với v75 + v81

**EN**: v82 is the **3rd design-skill in T1 cluster** within a 7-wiki window (v75 → v81 → v82). It's structurally similar to v75 (single-skill multi-target) and distinct from v81 (12-skill bundle).

**VN**: v82 là **design-skill thứ 3 trong cluster T1** trong cửa sổ 7-wiki (v75 → v81 → v82). Cấu trúc tương tự v75 (single-skill multi-target), khác với v81 (12-skill bundle).

| Axis | v75 impeccable | v81 taste-skill | v82 huashu-design |
|---|---|---|---|
| **Skills** | 1 monolithic | 12 sub-variants | 1 monolithic |
| **Harnesses** | 14 | ~4 | 6 (incl. Hermes from v78 corpus-recursive) |
| **Output** | Prompts only | Prompts only | **Prompts + actual file-output pipelines** (HTML+MP4+GIF+PPTX+PDF+60fps animation) |
| **Author** | Paul Bakaus (Google) | Leon Lin (Munich) | 花叔 (China) |
| **i18n** | EN-only | EN-only | **EN + zh bilingual** |
| **Anti-slop framing** | NO | YES (PRIMARY) | YES (named "Anti AI-slop Rules" section + CSS-technique enumeration) |
| **Lineage** | Anthropic frontend-design + ehmo typecraft (NOTICE.md 2-source) | Self-originated | **Anthropic Claude Design reverse-engineering with explicit attribution** |
| **Velocity** | 155.8/d HIGH-NOT-EXTREME | 202.9/d HIGH-NOT-EXTREME | **452.4/d EXTREME-VIRAL pulse** |

---

## Is it safe to install? / Cài có an toàn không?

**EN**: **Mostly yes, with caveats** — broader supply-chain surface than v75/v81:
- ✅ Text-only SKILL.md + references/
- ✅ Local-first install
- ⚠️ **`scripts/` folder contains shell + Node.js + Python scripts** that execute on user machine (audio mixing + PPTX/PDF export + TTS) — broader execution surface than prompts-only v75/v81
- ⚠️ `.env.example` indicates external-service integration (likely TTS API)
- ⚠️ No `SECURITY.md` observed
- ⚠️ No `CODEOWNERS` observed
- ⚠️ Solo-maintainer trust model (花叔 sole maintainer)
- ⚠️ LICENSE relicensed 2026-05-14 mid-life-cycle (current MIT; prior license state unknown)

**VN**: **Phần lớn an toàn, nhưng có lưu ý** — surface supply-chain rộng hơn v75/v81:
- ✅ SKILL.md + references/ chỉ là text
- ✅ Cài local
- ⚠️ **Folder `scripts/` có shell + Node.js + Python scripts** chạy trên máy user (audio mixing + PPTX/PDF export + TTS) — bề mặt thực thi rộng hơn v75/v81 prompts-only
- ⚠️ `.env.example` cho thấy tích hợp service ngoài (có thể là TTS API)
- ⚠️ Không thấy `SECURITY.md`
- ⚠️ Không thấy `CODEOWNERS`
- ⚠️ Mô hình tin tưởng solo-maintainer (花叔 duy nhất)
- ⚠️ LICENSE relicensed 2026-05-14 giữa vòng đời (hiện MIT; trước đó không rõ)

---

## Should I (Storm Bear / vault user) install it? / Có nên cài (Storm Bear / vault user) không?

**EN**: **Yes, IF you have UI / presentation / Scrum-board / sprint-report work planned**. Stronger pilot case than v75 + v81 because:
- Multimedia output covers Scrum-presentation use cases (PPTX + PDF)
- 60fps animation export for dashboards or journal visualizations
- TTS integration for retrospective video presentations
- One-command shorthand install via `npx skills add alchaincyf/huashu-design`
- Reversible via uninstall

**Pilot ranking**: cc-switch #1 / agent-skills-standard #2 / ECC fenced-scope #3 / taste-skill #4 / **huashu-design #5 NEW v82** / codegraph #6 / agents-best-practices #7 / agentmemory #8

**EN**: **If no UI / presentation work planned**: skip for now. Joins corpus-knowledge-only tier (v63 Karpathy + v74 Raschka + v75 impeccable + v77 easy-vibe + v79 + v80 + v81 + v82).

**VN**: **Có, NẾU bạn có việc UI / thuyết trình / Scrum-board / sprint-report**. Lý do mạnh hơn v75 + v81:
- Output multimedia phù hợp use case Scrum-presentation (PPTX + PDF)
- Animation 60fps cho dashboard hoặc journal visualization
- TTS cho video retrospective
- Cài một lệnh shorthand `npx skills add alchaincyf/huashu-design`
- Có thể uninstall

**Pilot ranking**: cc-switch #1 / agent-skills-standard #2 / ECC fenced-scope #3 / taste-skill #4 / **huashu-design #5 v82 MỚI** / codegraph #6 / agents-best-practices #7 / agentmemory #8

**VN**: **Nếu không có việc UI / thuyết trình**: bỏ qua tạm thời. Vào tier corpus-knowledge-only (v63 Karpathy + v74 Raschka + v75 + v77 + v79 + v80 + v81 + v82).

---

## What this wiki contributes to the Pattern Library / Wiki này đóng góp gì cho Pattern Library

**EN**:
- **Anti-Slop-Design-Curation observation track N=2 STRENGTHENING** — v81 + v82 = PROMOTION-ELIGIBLE at v85 audit (MEDIUM-HIGH confidence)
- **CORPUS-FIRST PRO-VIBE + Anti-Slop CO-EXISTENT framing within same subject** = orthogonality-validation evidence for v81 framing-revision
- **Pattern #57 NEW sub-variant 57h candidate** "Reverse-Engineering-of-Anchor-Corpus-Foundation-Product with explicit attribution" PROVISIONAL N=1
- **Pattern #19 NEW sub-mechanism 19m candidate** "Chinese-AI-Native-Coder-Influencer-with-Multi-Product-Portfolio" PROVISIONAL N=1
- **Pattern #84 84c.1 N+1 strengthening** = 9-consecutive-wiki Pattern #84 84c arc v71→v82 = NEW CORPUS-RECORD
- **Pattern #52 EXTREME-VIRAL pulse N+1 strengthening** = 4th evidence point (300-500/d sub-band)
- **Pattern #45 within-pattern + License-relicensing-event-tracking sub-mechanism candidate** PROVISIONAL N=1
- **Pattern #51 PRO-VIBE-explicit sub-pole N=2 STRENGTHENING at solo-influencer sub-scope** (v77 community-org + v82 solo-influencer)
- **Storm Bear STRONGEST 4/4 (all-STRONG)** = 6th STRONGEST in v65-v82 window + 18-streak NEW CORPUS-RECORD + 92.0% → 92.3% INCLUDE rate

**VN**:
- **Anti-Slop-Design-Curation observation track N=2 STRENGTHENING** — v81 + v82 = ĐỦ ĐIỀU KIỆN PROMOTE tại audit v85 (MEDIUM-HIGH confidence)
- **CORPUS-FIRST PRO-VIBE + Anti-Slop ĐỒNG TỒN TẠI cùng subject** = bằng chứng orthogonality-validation cho việc revise framing tại v81
- **Pattern #57 sub-variant MỚI 57h candidate** "Reverse-Engineering-of-Anchor-Corpus-Foundation-Product with explicit attribution" PROVISIONAL N=1
- **Pattern #19 sub-mechanism MỚI 19m candidate** "Chinese-AI-Native-Coder-Influencer-with-Multi-Product-Portfolio" PROVISIONAL N=1
- **Pattern #84 84c.1 N+1 strengthening** = chuỗi 9 wiki liên tiếp Pattern #84 84c v71→v82 = KỶ LỤC CORPUS MỚI
- **Pattern #52 EXTREME-VIRAL pulse N+1 strengthening** = bằng chứng thứ 4 (sub-band 300-500/d)
- **Pattern #45 within-pattern + License-relicensing-event-tracking sub-mechanism candidate** PROVISIONAL N=1
- **Pattern #51 PRO-VIBE-explicit sub-pole N=2 STRENGTHENING tại sub-scope solo-influencer** (v77 community-org + v82 solo-influencer)
- **Storm Bear STRONGEST 4/4 (all-STRONG)** = lần STRONGEST thứ 6 trong cửa sổ v65-v82 + chuỗi 18 KỶ LỤC CORPUS MỚI + INCLUDE rate 92.0% → 92.3%

---

## Sources & cross-wiki links / Nguồn & liên kết wiki khác

- v75 impeccable (T1 design-skill anchor) — `impeccable - Beginner Analysis/`
- v81 taste-skill (Anti-Slop framing N=1 → N=2 with v82) — `taste-skill - Beginner Analysis/`
- v77 easy-vibe (PRO-VIBE-explicit anchor) — `easy-vibe - Beginner Analysis/`
- v78 ECC (Hermes harness corpus-recursive citation source) — `ECC-v78-recursive-revisit - Beginner Analysis/`
- v76 agent-skills-standard + v80 SmartMacroAI (Asian-LOCATED cluster partial) — `agent-skills-standard - Beginner Analysis/` + `SmartMacroAI - Beginner Analysis/`

> **Wiki status**: Built under routine v2.2 (eighteenth execution). Phase 4b PRIMARY proposal-document at `01 Analysis/(C) Anti-Slop-Design-Curation-N2-strengthening-with-PRO-VIBE-coexistent-framing.md`.
