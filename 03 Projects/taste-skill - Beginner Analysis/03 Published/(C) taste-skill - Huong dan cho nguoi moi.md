# taste-skill — Hướng dẫn cho người mới (Bilingual EN/VN)

> Wiki v81 — Leon Lin (Leonxlnx) / Munich · MIT · `tasteskill.dev` · 18,264 stars / 1,560 forks / 90 days at fetch
> [GitHub repo](https://github.com/Leonxlnx/taste-skill)

---

## What is taste-skill? / taste-skill là gì?

**EN**: taste-skill is a **bundle of 12 portable Agent Skills** for Claude Code, Codex, Cursor, and ChatGPT Images. It positions itself as *"The Anti-Slop Frontend Framework for AI Agents"* — meaning it upgrades AI-built interfaces with stronger layout, typography, motion, and spacing **instead of the boilerplate "looks AI-generated" output** that default LLMs produce.

**VN**: taste-skill là một **bộ 12 Agent Skill di động** dành cho Claude Code, Codex, Cursor, và ChatGPT Images. Nó tự định vị là *"Khung Frontend Chống-Slop dành cho AI Agent"* — nghĩa là nó nâng cấp các UI do AI tạo ra với layout, typography (kiểu chữ), chuyển động, và spacing (khoảng cách) tốt hơn, **thay vì kiểu UI "trông như AI làm" mặc định** mà các LLM thường tạo ra.

---

## Why does it exist? / Vì sao nó ra đời?

**EN**: When you ask Claude / Cursor / Codex to build a frontend, the default output tends to look generic and boilerplate. Leon Lin calls this *"slop"*. taste-skill is a curation overlay — it injects design discipline into the agent's context so the agent produces UIs that look like they were built by someone who cares about taste.

**VN**: Khi bạn yêu cầu Claude / Cursor / Codex xây frontend, kết quả mặc định thường trông chung chung và như khuôn mẫu. Leon Lin gọi đó là *"slop"* (rác). taste-skill là một lớp curate (chọn lọc chất lượng) — nó tiêm kỷ luật thiết kế vào ngữ cảnh của agent, để agent tạo ra UI trông giống như được xây bởi người có "gu" (taste).

---

## How to install / Cài đặt thế nào

**EN**: One command per skill via Claude Code's standard skill install:

**VN**: Một lệnh cho mỗi skill, qua câu lệnh cài skill chuẩn của Claude Code:

```bash
npx skills add https://github.com/Leonxlnx/taste-skill --skill "<skill-name>"
```

**EN**: Choose from the 12 skill names below based on what aesthetic or workflow you want.

**VN**: Chọn từ 12 tên skill bên dưới tuỳ thuộc vào phong cách hoặc luồng làm việc bạn muốn.

---

## The 12 skills (3-axis decomposition) / 12 skills (chia theo 3 trục)

### Axis A — Aesthetic / Phong cách thẩm mỹ (4 skills)

| Skill | EN | VN |
|---|---|---|
| `taste-skill` | Base brand-skill; default taste rules | Skill nền + bộ luật taste mặc định |
| `minimalist-skill` | Clean/centered layout pole | Layout sạch / căn giữa |
| `brutalist-skill` | Asymmetric/modern layout pole | Layout bất đối xứng / hiện đại |
| `soft-skill` | Soft design pole | Phong cách thiết kế mềm mại |

### Axis B — Workflow / Luồng làm việc (4 skills)

| Skill | EN | VN |
|---|---|---|
| `redesign-skill` | Improve existing UI | Cải tiến UI có sẵn |
| `image-to-code-skill` | Convert image reference → frontend code | Chuyển hình tham khảo → code frontend |
| `output-skill` | Enforce output format / quality gate | Áp luật định dạng output / cổng chất lượng |
| `stitch-skill` | Compose layouts from parts | Ghép layout từ các thành phần |

### Axis C — Platform / Extension (4 skills)

| Skill | EN | VN |
|---|---|---|
| `gpt-tasteskill` | Variant for GPT/Codex harness | Phiên bản cho GPT/Codex |
| `imagegen-frontend-web` | Image-gen reference for web | Tham khảo image-gen cho web |
| `imagegen-frontend-mobile` | Image-gen reference for mobile | Tham khảo image-gen cho mobile |
| `brandkit` | Branding + identity layer | Lớp thương hiệu + nhận diện |

**EN**: The 12 = 4 + 4 + 4 clean partitioning is what makes this a "Multi-Skill Brand Portfolio with Sub-Variant Taxonomy" — a new T1 sub-archetype this wiki proposes.

**VN**: Cách phân chia 12 = 4 + 4 + 4 sạch là điều khiến nó trở thành một "Multi-Skill Brand Portfolio with Sub-Variant Taxonomy" — một sub-archetype T1 mới mà wiki này đề xuất.

---

## How it works (the setting-spectrum) / Cơ chế hoạt động (setting-spectrum)

**EN**: Each skill carries dimensional settings — for example:
- **Layout dimension**: lower = centered/clean; higher = asymmetric/modern.
- **Motion dimension**: ranges from `hover` to `scroll` to `magnetic`.

The agent reads these settings + design-discipline rules from the skill file, then produces frontend code (React / Vue / Svelte are all supported because output is **design-intent rules**, not framework-locked code).

**VN**: Mỗi skill mang theo cài đặt theo chiều — ví dụ:
- **Chiều layout**: thấp = căn giữa/sạch; cao = bất đối xứng/hiện đại.
- **Chiều chuyển động**: trải từ `hover` đến `scroll` đến `magnetic` (nam châm).

Agent đọc các cài đặt này + luật kỷ luật thiết kế từ file skill, rồi tạo ra code frontend (React / Vue / Svelte đều được hỗ trợ vì output là **luật ý-định-thiết-kế**, không phải code khoá vào framework).

---

## Who is Leon Lin? / Leon Lin là ai?

**EN**: Leon Lin (`@Leonxlnx` GitHub / `@lexnlin` Twitter) is a Munich-based solo developer with **104 public repos** and **819 followers**. Bio: *"i like to build stuff"*. He runs the project as a solo founder with GitHub Sponsors (8 named sponsors at time of writing) and the `tasteskill.dev` custom domain. **No paid tier or SaaS observed** — pure OSS + donations.

**VN**: Leon Lin (`@Leonxlnx` trên GitHub / `@lexnlin` trên Twitter) là một solo dev sống ở Munich, có **104 repo public** và **819 followers**. Tiểu sử: *"i like to build stuff"* ("tôi thích build đồ"). Anh điều hành dự án như một solo founder với GitHub Sponsors (8 nhà tài trợ có tên tại thời điểm viết) và custom domain `tasteskill.dev`. **Không thấy gói trả phí hay SaaS** — thuần OSS + donate.

---

## Comparison with v75 impeccable / So sánh với v75 impeccable

**EN**: Both are T1 Assistant Skill / design-language tier. But they're architecturally inverted:

**VN**: Cả hai đều thuộc tier T1 Assistant Skill / design-language. Nhưng kiến trúc thì ngược nhau:

| | v75 impeccable | v81 taste-skill |
|---|---|---|
| Skills | **1 canonical skill** / **1 skill chuẩn** | **12 distinct skills** / **12 skill khác nhau** |
| Harnesses | **14 harness directories** / **14 thư mục harness** | **~4 harness ecosystem** / **~4 hệ sinh thái harness** |
| Multiplicity layer / Tầng đa-bội | Distribution layer / Tầng phân phối | Content layer / Tầng nội dung |
| Author / Tác giả | Paul Bakaus (Google Creative Technologist) | Leon Lin (Munich solo founder) |
| License | Apache 2.0 + NOTICE.md | MIT |

---

## Is it safe to install? / Cài có an toàn không?

**EN**: **Mostly yes, with caveats**:
- ✅ Text-only content (no executable code; skill is design-rules + prompts).
- ✅ Zero-API-key (no telemetry observed).
- ✅ Local-first (skill installs into your local Claude Code skill folder).
- ⚠️ No `SECURITY.md` observed.
- ⚠️ No injection-scanning / no Zod schema validation / no per-skill `evals.json` (unlike v76 agent-skills-standard's 6-axis discipline).
- ⚠️ Solo-maintainer trust model — single point of failure/compromise.

**VN**: **Phần lớn là an toàn, nhưng có lưu ý**:
- ✅ Nội dung chỉ là text (không có code chạy được; skill là luật thiết kế + prompts).
- ✅ Không cần API key (không thấy telemetry).
- ✅ Local-first (skill cài vào thư mục skill cục bộ của Claude Code).
- ⚠️ Không thấy file `SECURITY.md`.
- ⚠️ Không thấy injection-scanning / Zod schema validation / `evals.json` mỗi skill (khác với kỷ luật 6-trục của v76 agent-skills-standard).
- ⚠️ Mô hình tin tưởng solo-maintainer — single point of failure/compromise.

---

## Should I (Storm Bear / vault user) install it? / Có nên cài (Storm Bear / vault user) không?

**EN**: **Yes, IF you have UI work planned in the next 30 days**. Per-skill granularity lets you trial with just `taste-skill` base + 1 aesthetic variant (e.g., `minimalist-skill`). Reversible via uninstall. Adds taste-layer to any UI work in vault tooling (dashboards / Scrum-board overlays / journal exports).

**EN**: **If no UI work planned**: skip for now. Becomes corpus-knowledge-only subject (similar to v75 impeccable + v63 Karpathy + v74 Raschka). Revisit when UI work appears.

**VN**: **Có, NẾU bạn có việc về UI trong 30 ngày tới**. Vì cài theo từng skill nên có thể thử với `taste-skill` base + 1 variant thẩm mỹ (ví dụ `minimalist-skill`). Có thể uninstall lại được. Thêm lớp "taste" vào bất kỳ công việc UI nào trong vault tooling (dashboards / Scrum-board overlays / xuất journal).

**VN**: **Nếu không có việc về UI**: bỏ qua tạm thời. Trở thành đối tượng kiến-thức-corpus-only (giống v75 impeccable + v63 Karpathy + v74 Raschka). Quay lại khi có việc về UI.

---

## What this wiki contributes to the Pattern Library / Wiki này đóng góp gì cho Pattern Library

**EN**:
- **NEW T1 sub-archetype** "Multi-Skill Brand Portfolio with Sub-Variant Taxonomy" PROVISIONAL N=1 at **MEDIUM confidence** (revised post-self-review).
- **Pattern #19 NEW sub-mechanism 19l** "Munich-Solo-Founder-with-Multi-Skill-Design-Brand-Portfolio" PROVISIONAL N=1.
- **Anti-Slop-Design-Curation observation track candidate at OC layer** PROVISIONAL N=1 (NOT Pattern #51 sub-pole — orthogonal axis to vibe-coding-spectrum).
- **Library-vocabulary item #12 `llms.txt`** N=1 → N=2 PROMOTION-ELIGIBLE.
- **Pattern #84 84c.1 N+1 strengthening at repo-stored layer** = 8-consecutive-wiki Pattern #84 84c arc v71→v81 (NEW CORPUS-RECORD).
- **Pattern #52 N=4 HIGH-NOT-EXTREME** age-distribution-coverage strengthening (202.93 stars/day × 90 days mid-life-cycle).
- **Storm Bear STRONGEST 4/4** = 5th STRONGEST in v65-v81 window.

**VN**:
- **T1 sub-archetype MỚI** "Multi-Skill Brand Portfolio with Sub-Variant Taxonomy" PROVISIONAL N=1 ở **MEDIUM confidence** (đã chỉnh sau self-review).
- **Pattern #19 sub-mechanism MỚI 19l** "Munich-Solo-Founder-with-Multi-Skill-Design-Brand-Portfolio" PROVISIONAL N=1.
- **Anti-Slop-Design-Curation observation track candidate ở OC layer** PROVISIONAL N=1 (KHÔNG phải Pattern #51 sub-pole — trục trực giao với vibe-coding-spectrum).
- **Library-vocabulary item #12 `llms.txt`** N=1 → N=2 ĐỦ ĐIỀU KIỆN PROMOTE.
- **Pattern #84 84c.1 N+1 strengthening tầng repo-stored** = chuỗi 8 wiki liên tiếp Pattern #84 84c v71→v81 (KỶ LỤC CORPUS MỚI).
- **Pattern #52 N=4 HIGH-NOT-EXTREME** strengthening phủ khoảng tuổi (202.93 sao/ngày × 90 ngày mid-life-cycle).
- **Storm Bear STRONGEST 4/4** = lần STRONGEST thứ 5 trong cửa sổ v65-v81.

---

## Sources & cross-wiki links / Nguồn & liên kết wiki khác

- v75 impeccable (DIRECT SISTER) — `impeccable - Beginner Analysis/`
- v77 easy-vibe (`llms.txt` sibling) — `easy-vibe - Beginner Analysis/`
- v76 agent-skills-standard (supply-chain discipline contrast) — `agent-skills-standard - Beginner Analysis/`
- v78 ECC (multi-skill scope analog + Pro-SaaS contrast) — `ECC-v78-recursive-revisit - Beginner Analysis/`

> **Wiki status**: Built under routine v2.2 (seventeenth execution). Phase 4b PRIMARY proposal-document at `01 Analysis/(C) T1-NEW-sub-archetype-Multi-Skill-Brand-Portfolio-with-Sub-Variant-Taxonomy-N1-registration.md`.
