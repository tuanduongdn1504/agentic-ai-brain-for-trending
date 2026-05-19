# impeccable — Hướng dẫn cho người mới (VN + EN)

> **Subject:** [pbakaus/impeccable](https://github.com/pbakaus/impeccable) — "The design language that makes your AI harness better at design"
> **Tác giả / Author:** Paul Bakaus (Creative Technologist at Google; người tạo jQuery UI)
> **License:** Apache 2.0
> **Wiki version:** v75

---

## 🇻🇳 Tiếng Việt

### impeccable là gì?

**impeccable** là một "design skill" (kỹ năng thiết kế) cài được vào các công cụ AI như Claude Code, Cursor, Gemini CLI, OpenCode, Codex CLI, GitHub Copilot, và 8 công cụ khác — tổng cộng **14 công cụ AI**.

Khi cài vào, AI của bạn sẽ học được:
- **Bộ từ vựng thiết kế** (design vocabulary) — gọi đúng tên các yếu tố UI thay vì mô tả mơ hồ
- **23 lệnh chuyên biệt** — `/impeccable critique` để review thiết kế, `/impeccable audit` để kiểm tra accessibility, `/impeccable polish` để hoàn thiện trước khi ship
- **27 quy tắc "đừng làm"** (anti-patterns) — chặn AI tạo ra UI nhìn là biết "AI làm" (dark mode mặc định, gradient tím-xanh, glassmorphism, card-trong-card)

### Tại sao dùng impeccable?

Vấn đề: AI tạo UI thường trông giống nhau và "nhìn là biết AI làm." Bạn không có cách nói rõ ràng để hướng dẫn AI tạo thiết kế đẹp hơn.

Giải pháp: impeccable cung cấp **ngôn ngữ chung** để bạn và AI nói cùng một thứ tiếng về thiết kế.

### Cài đặt nhanh (Claude Code)

```bash
# Copy thư mục skill vào project của bạn
cp -r .claude/skills/impeccable /path/to/your/project/.claude/skills/

# Hoặc tải bundle từ https://impeccable.style
```

### Dùng CLI không cần API key

```bash
# Quét HTML/folder/URL để tìm anti-patterns
npx impeccable detect ./dist/index.html
npx impeccable detect https://your-site.com
```

CLI sẽ báo cáo vi phạm theo 27 quy tắc thiết kế. Không cần API key, không tốn token.

### Sử dụng cơ bản

Khi đã cài skill, gõ trong Claude Code:

```
/impeccable shape new-feature
```

→ Claude sẽ giúp bạn lên kế hoạch UX/UI **trước khi viết code**.

```
/impeccable critique /dashboard
```

→ Claude review UX của trang dashboard với hệ thống chấm điểm.

```
/impeccable audit
```

→ Claude kiểm tra accessibility (WCAG 2.1 AA), performance, responsiveness.

```
/impeccable polish
```

→ Claude hoàn thiện chi tiết trước khi ship.

### Triết lý thiết kế

impeccable theo nguyên tắc **"restraint in service of craft"** (kiềm chế phục vụ thủ công):

- **Màu sắc**: chỉ dùng OKLCH, KHÔNG đen/trắng tinh khiết — màu kem ấm + một màu nhấn magenta duy nhất (≤10% màn hình)
- **Typography**: Cormorant Garamond italic cho display + Instrument Sans cho body; dòng dài 65-75 ký tự
- **Spacing**: hệ 8/16/24/32/48/80/120px (cố ý bỏ 4px)
- **Motion**: ease-out exponential `cubic-bezier(0.16, 1, 0.3, 1)`, 150-1200ms
- **Shadow**: phẳng mặc định; shadow chỉ xuất hiện khi hover

### 5 "Đừng làm" tuyệt đối

1. KHÔNG viền màu bên trái (side-stripe borders)
2. KHÔNG gradient cho chữ (gradient text)
3. KHÔNG glassmorphism mặc định
4. KHÔNG dùng template "hero + số liệu lớn"
5. KHÔNG nhảy ngay vào modal làm giải pháp đầu tiên

### "AI slop test"

Bài kiểm tra cuối cùng: nếu output **rõ ràng nhìn là AI tạo**, skill đã thất bại. impeccable cố gắng đẩy output đến mức **không phân biệt được với designer chuyên nghiệp**.

### Khi nào KHÔNG nên dùng impeccable?

- Project có brand requirement nằm ngoài thẩm mỹ của Bakaus (SaaS landing page nhiều trang trí, UI game, e-commerce bán lẻ)
- Bạn cần học design fundamentals — impeccable giả định bạn đã hiểu vấn đề
- Bạn muốn thẩm mỹ "AI-marketing" (dark + gradient + glow) — impeccable cố ý chặn các pattern này

### Thông tin nhanh

- 🌟 **28,816 stars** (rất viral, 155.8 stars/ngày trong 185 ngày)
- 🍴 **1,559 forks**
- 📦 **14 công cụ AI** được hỗ trợ (kỷ lục corpus)
- 📜 **Apache 2.0** + NOTICE.md trích dẫn 2 nguồn (Anthropic frontend-design skill + ehmo typecraft-guide-skill)
- 🏗️ Tác giả **Paul Bakaus** — Creative Technologist tại Google, người tạo jQuery UI

---

## 🇬🇧 English

### What is impeccable?

**impeccable** is a design skill installable into 14 AI coding tools — Claude Code, Cursor, Gemini CLI, OpenCode, Codex CLI, GitHub Copilot, and 8 others.

Once installed, your AI gains:
- **A shared design vocabulary** — name UI elements precisely instead of describing them vaguely
- **23 specialized commands** — `/impeccable critique` for design review, `/impeccable audit` for accessibility checks, `/impeccable polish` for shipping readiness
- **27 deterministic anti-pattern rules** — block AI output that obviously reads as "AI-generated" (dark mode defaults, purple-to-blue gradients, glassmorphism, cards-in-cards)

### Why use impeccable?

Problem: AI-generated UIs tend to look the same — distinctively "AI-made." You lack a clear way to direct AI toward better design.

Solution: impeccable provides the **shared language** so you and the AI speak the same dialect about design.

### Quick install (Claude Code)

```bash
# Copy skill directory into your project
cp -r .claude/skills/impeccable /path/to/your/project/.claude/skills/

# Or download a bundle from https://impeccable.style
```

### CLI without API key

```bash
# Scan HTML / directory / URL for anti-pattern violations
npx impeccable detect ./dist/index.html
npx impeccable detect https://your-site.com
```

The CLI reports violations against the 27 rules. No API key. No token cost.

### Basic usage

With the skill installed, in Claude Code:

```
/impeccable shape new-feature
```

→ Claude helps you plan UX/UI **before writing code**.

```
/impeccable critique /dashboard
```

→ Claude reviews dashboard UX with scored evaluation.

```
/impeccable audit
```

→ Claude checks accessibility (WCAG 2.1 AA), performance, responsiveness.

```
/impeccable polish
```

→ Claude refines final details before shipping.

### Design philosophy

impeccable follows **restraint in service of craft**:

- **Color**: OKLCH-only, NO pure black/white — warm paper neutrals + one decisive magenta accent (≤10% screen coverage)
- **Typography**: Cormorant Garamond italic (display) + Instrument Sans (body); 65-75 character line length
- **Spacing**: 8/16/24/32/48/80/120px scale (4px deliberately omitted)
- **Motion**: expo-out easing `cubic-bezier(0.16, 1, 0.3, 1)`, 150-1200ms
- **Shadow**: flat by default; shadows respond only to hover/state-change

### 5 absolute bans

1. NO side-stripe borders
2. NO gradient text
3. NO default glassmorphism
4. NO hero-metric templates
5. NO modals as the first-thought solution

### "AI slop test"

The final test: if output **obviously reads as AI-generated**, the skill failed. impeccable pushes output toward being **indistinguishable from a professional designer's work**.

### When NOT to use impeccable

- Projects with brand requirements outside Bakaus's aesthetic (heavily-decorated SaaS landings, game UIs, retail e-commerce)
- You need design fundamentals — impeccable assumes you already understand the problem
- You want "AI marketing" aesthetic (dark + gradient + glow) — impeccable deliberately blocks these patterns

### Fast facts

- 🌟 **28,816 stars** (highly viral, 155.8 stars/day over 185 days)
- 🍴 **1,559 forks**
- 📦 **14 AI tools** supported (corpus record)
- 📜 **Apache 2.0** + NOTICE.md crediting 2 sources (Anthropic frontend-design skill + ehmo typecraft-guide-skill)
- 🏗️ Author **Paul Bakaus** — Creative Technologist at Google, jQuery UI creator

---

## Thông tin nguồn / Sources

- Repository: https://github.com/pbakaus/impeccable
- Homepage: https://impeccable.style
- Parent skill: https://github.com/anthropics/skills/tree/main/skills/frontend-design
- Tactical additions: https://github.com/ehmo/typecraft-guide-skill
- Author profile: https://github.com/pbakaus
