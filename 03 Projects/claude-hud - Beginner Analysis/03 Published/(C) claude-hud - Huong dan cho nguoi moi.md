# claude-hud — Hướng dẫn cho người mới / Beginner's guide

> **Bilingual VN/EN.** Câu trả lời ngắn gọn cho người Scrum coach / dev muốn hiểu và thử claude-hud trong ~5 phút.
> **Short answer for the Scrum coach / dev who wants to understand and try claude-hud in ~5 minutes.**

**Subject:** `jarrodwatts/claude-hud` — *"A Claude Code plugin that shows what's happening — context usage, active tools, running agents, and todo progress. Always visible below your input."*
**Version analyzed:** v0.0.12 released (CHANGELOG) / v0.1.0 Unreleased (package.json) at 2026-04-23
**Wiki version:** v1 (Storm Bear corpus #35)

---

## Part 1 — Đó là cái gì? / What is this?

**VN:** claude-hud là một Claude Code plugin hiển thị **thanh trạng thái (statusline)** ngay dưới ô nhập liệu của bạn. Nó cho biết: model hiện tại đang dùng, context window còn bao nhiêu phần trăm, công cụ nào đang chạy, subagent nào đang làm việc, và todo list đã hoàn thành bao nhiêu. Tất cả diễn ra real-time (~300ms cập nhật).

**EN:** claude-hud is a Claude Code plugin that displays a **statusline** right below your input box. It shows: which model is currently in use, how much context window is left, what tools are running, what subagents are working, and how much of your todo list is complete. All real-time (~300ms refresh).

**Hình ảnh 2-dòng mặc định / Default 2-line view:**
```
[Opus] │ my-project git:(main*)
Context █████░░░░░ 45% │ Usage ██░░░░░░░░ 25% (1h 30m / 5h)
```

---

## Part 2 — Tại sao nên quan tâm? / Why should you care?

**VN:** Nếu bạn dùng Claude Code cho công việc thật (viết code, quản lý repo, huấn luyện team), bạn sẽ gặp 3 vấn đề lặp lại:

1. **Context window hết bất ngờ** → Claude Code tự động `/compact`, bạn mất context của cuộc đối thoại
2. **Rate limit hết bất ngờ** → Bạn phải chờ 5 giờ hoặc 7 ngày để reset
3. **Subagent / tool chạy ngầm không biết** → Khi gọi Task tool, bạn không biết nó đang làm gì cho đến khi kết thúc

claude-hud giải quyết cả 3 bằng cách **hiện tình trạng real-time** lên statusline. Không cần gõ `/context` hay `/status`.

**EN:** If you use Claude Code for real work (writing code, managing repos, training teams), you'll hit 3 recurring problems:

1. **Context window runs out unexpectedly** → Claude Code auto-`/compact`s, you lose conversation context
2. **Rate limits hit unexpectedly** → You wait 5 hours or 7 days for reset
3. **Subagents / tools run invisibly** → When you invoke Task tool, you don't know what it's doing until it finishes

claude-hud solves all 3 by **showing status real-time** on the statusline. No need to type `/context` or `/status`.

---

## Part 3 — Cài đặt 5 phút / 5-minute install

**VN:** Trong Claude Code session, chạy 3 lệnh này:

**EN:** Inside a Claude Code session, run these 3 commands:

```
Step 1: /plugin marketplace add jarrodwatts/claude-hud
Step 2: /plugin install claude-hud
Step 3: /claude-hud:setup
```

Sau đó **restart Claude Code** (`exit` và `claude` lại). Statusline sẽ xuất hiện.

After that, **restart Claude Code** (`exit` and `claude` again). The statusline will appear.

**Linux cảnh báo / Linux caveat:** Nếu gặp lỗi `EXDEV: cross-device link not permitted`:
```bash
mkdir -p ~/.cache/tmp && TMPDIR=~/.cache/tmp claude
```
Rồi chạy lại `/plugin install claude-hud` trong session mới. / Then re-run `/plugin install claude-hud` in the new session.

**Windows cảnh báo / Windows caveat:** Nếu `/claude-hud:setup` báo "no JavaScript runtime found":
```powershell
winget install OpenJS.NodeJS.LTS
```
Rồi restart shell và chạy lại setup. / Then restart shell and re-run setup.

---

## Part 4 — Nó hiển thị cái gì? / What does it show?

### Mặc định 2 dòng / Default 2 lines

**VN:**
- **Dòng 1:** Model `[Opus]` + tên project + branch git + dirty indicator `*` nếu có file thay đổi chưa commit
- **Dòng 2:** Context bar (xanh→vàng→đỏ theo %) + usage bar (5-hour rate limit) + đếm ngược reset

**EN:**
- **Line 1:** Model `[Opus]` + project name + git branch + dirty indicator `*` if uncommitted changes
- **Line 2:** Context bar (green→yellow→red by %) + usage bar (5-hour rate limit) + reset countdown

### Dòng tùy chọn / Optional lines (bật qua `/claude-hud:configure`)

```
◐ Edit: auth.ts | ✓ Read ×3 | ✓ Grep ×2       ← Tools activity
◐ explore [haiku]: Finding auth code (2m 15s)   ← Agent status
▸ Fix authentication bug (2/5)                  ← Todo progress
```

- **Tools line:** Hiện công cụ đang chạy + tổng công cụ đã hoàn thành / Shows running tools + aggregated completed
- **Agents line:** Hiện subagent (Task tool) + model + mô tả + thời gian / Shows subagent + model + description + elapsed time
- **Todos line:** Hiện todo hiện tại + tiến độ / Shows current todo + progress

---

## Part 5 — 3 preset chọn nhanh / 3 quick-start presets

**VN:** Khi chạy `/claude-hud:setup`, bạn sẽ được chọn preset:

**EN:** When you run `/claude-hud:setup`, you'll pick a preset:

| Preset | Gì được bật / What's enabled | Khi nào dùng / When to use |
|--------|------------------------------|---------------------------|
| **Full** | Tất cả: tools + agents + todos + git + usage + duration | Khi bạn muốn biết hết / When you want everything visible |
| **Essential** | Tools/agents/todos lines + git status, ít thông tin phụ | Cân bằng giữa visibility và noise / Balance between visibility and noise |
| **Minimal** | Chỉ model + context bar (2 dòng) | Muốn tối giản, chỉ cần biết context health / Want minimal, just need context health |

**Recommend cho Scrum coach / Recommend for Scrum coach:** Bắt đầu với **Essential** — cân bằng tốt. Sau đó bật/tắt từng element sau 1 tuần.

**Recommend for Scrum coach:** Start with **Essential** — good balance. Then toggle individual elements after 1 week of observation.

---

## Part 6 — Context threshold và màu sắc / Context threshold and colors

**VN:** Context bar có 3 ngưỡng màu:

**EN:** Context bar has 3 threshold colors:

| Ngưỡng / Threshold | Màu / Color | Ý nghĩa / Meaning |
|-----|------|-------|
| < 70% | 🟢 Xanh / Green | Bình thường, làm việc thoải mái / Normal, work freely |
| 70-85% | 🟡 Vàng / Yellow | Cảnh báo, chuẩn bị dọn dẹp / Warning, prepare to consolidate |
| > 85% | 🔴 Đỏ / Red | Nguy hiểm, sắp `/compact` / Critical, `/compact` imminent |

**Tip cho Storm Bear operator / Tip for Storm Bear operator:** Khi thấy vàng mid-phase (đang giữa chừng wiki build), **dừng tay, viết file trung gian ra**, rồi tiếp tục. Tránh bị `/compact` ép phải làm lại.

**Tip for Storm Bear operator:** When you see yellow mid-phase (middle of a wiki build), **pause, write an interim file out**, then continue. Avoid being forced by `/compact` to redo work.

---

## Part 7 — Usage rate limit / Usage rate limit

**VN:** Dòng 2 phần "Usage" hiển thị rate limit của subscriber plan:
- `Usage ██░░░░░░░░ 25% (1h 30m / 5h)` — đã dùng 25% quota 5-tiếng, còn 1h30m đến reset
- Nếu 7-day usage >= 80% (default), hiện thêm: `| ██████████ 85% (2d / 7d)`

**EN:** Line 2 "Usage" section shows subscriber rate limit:
- `Usage ██░░░░░░░░ 25% (1h 30m / 5h)` — used 25% of 5-hour quota, 1h30m until reset
- If 7-day usage >= 80% (default threshold), also shows: `| ██████████ 85% (2d / 7d)`

**Caveat quan trọng / Important caveat:**
- **API-key-only users** (không subscriber) sẽ không thấy usage line / API-key-only users (not subscriber) won't see usage line
- **AWS Bedrock** models hiện `Bedrock` và ẩn usage (billing ở AWS) / AWS Bedrock hides usage (billing at AWS)
- **Google Vertex** models hiện `Vertex` và ẩn cost estimate / Google Vertex hides cost estimate

---

## Part 8 — Customize sâu / Deep customization

**VN:** Sau khi setup, có 2 cách customize:

**EN:** After setup, 2 ways to customize:

### Cách 1 — Guided (khuyến nghị cho người mới) / Way 1 — Guided (recommended for beginners)

```
/claude-hud:configure
```

Flow có hướng dẫn: chọn preset → chọn ngôn ngữ (en / zh) → toggle từng element → preview → save.

Guided flow: pick preset → pick language (en / zh) → toggle each element → preview → save.

### Cách 2 — Manual (khi cần advanced) / Way 2 — Manual (when you need advanced)

Edit file:
```
~/.claude/plugins/claude-hud/config.json
```

Có ~49 config keys covering: layout / git / display toggles / colors / thresholds. Đọc README section "Options" cho bảng đầy đủ.

~49 config keys covering: layout / git / display toggles / colors / thresholds. Read README "Options" section for full table.

**Ví dụ config.json / Example config.json:**

```json
{
  "language": "en",
  "lineLayout": "expanded",
  "pathLevels": 2,
  "gitStatus": {
    "enabled": true,
    "showDirty": true,
    "showAheadBehind": true,
    "showFileStats": true
  },
  "display": {
    "showTools": true,
    "showAgents": true,
    "showTodos": true,
    "showDuration": true
  },
  "colors": {
    "context": "cyan",
    "warning": "yellow",
    "critical": "red"
  }
}
```

---

## Part 9 — Use case cụ thể cho Storm Bear operator / Concrete use cases for Storm Bear operator

**VN:**

**Use case 1 — Wiki build dài 2 tiếng:**
- Preset: Essential
- Bật: `showDuration: true` (track 2h plateau)
- Kết quả: Thấy context bar progress xanh→vàng→đỏ để biết khi nào phải save state

**Use case 2 — Debug subagent không phản hồi:**
- Bật: `showAgents: true`
- Kết quả: Thấy `◐ agent-name [model]: description (2m 15s)` — biết subagent đang làm gì, bao lâu rồi

**Use case 3 — Track tool pattern khi phân tích Phase 2 efficiency:**
- Bật: `showTools: true`
- Kết quả: Thấy real-time Read/Edit/Grep counts — biết phase nào nặng Read, phase nào nặng Edit

**Use case 4 — Tránh bị /compact bất ngờ giữa Phase 4b:**
- Theo dõi context bar liên tục
- Khi chuyển sang yellow (70%), dừng và write interim output

**EN:**

**Use case 1 — Long 2-hour wiki build:**
- Preset: Essential
- Enable: `showDuration: true` (track 2h plateau)
- Result: See context bar progress green→yellow→red to know when to save state

**Use case 2 — Debug unresponsive subagent:**
- Enable: `showAgents: true`
- Result: See `◐ agent-name [model]: description (2m 15s)` — know what subagent is doing, for how long

**Use case 3 — Track tool pattern when analyzing Phase 2 efficiency:**
- Enable: `showTools: true`
- Result: See real-time Read/Edit/Grep counts — know which phase is Read-heavy, which is Edit-heavy

**Use case 4 — Avoid unexpected /compact mid-Phase-4b:**
- Watch context bar continuously
- When it turns yellow (70%), pause and write interim output

---

## Part 10 — 1-week evaluation protocol / 1-week evaluation protocol

**VN:**

| Ngày / Day | Hành động / Action | Quan sát / Observe |
|-----|-------|---------|
| 0 | Cài đặt + setup (5 phút) | Statusline xuất hiện chưa? |
| 1-3 | Default 2-line HUD | Context bar đổi màu có đúng lúc không? Có phân tâm không? |
| 4 | Bật `showTools: true` | Tools line có hữu ích hay noise? |
| 5 | Bật `showAgents: true` | Agents line có hữu ích hay noise? |
| 6 | Bật `showTodos: true` + `showDuration: true` | Todos + duration có cần thiết? |
| 7 | Quyết định / Decision | Giữ (configure preset cuối) / Gỡ (`/plugin uninstall claude-hud`) |

**EN:** Same protocol in English. If net-positive signal-to-noise after 7 days, keep. Else uninstall — zero sunk cost, clean removal.

---

## Part 11 — Khi nào KHÔNG nên dùng / When NOT to use

**VN:**
- Nếu bạn chỉ thỉnh thoảng dùng Claude Code (< 5 session/tuần) — overhead > value
- Nếu terminal bạn quá hẹp (< 80 cols) — statusline có thể wrap không đẹp (có `branchOverflow: "wrap"` config nhưng vẫn chiếm 3-4 dòng)
- Nếu bạn làm việc trên Claude API (không qua Claude Code) — plugin chỉ chạy trong Claude Code
- Nếu bạn tu-tu dùng custom statusline khác — phải chọn 1 trong 2

**EN:**
- If you use Claude Code only occasionally (< 5 sessions/week) — overhead > value
- If your terminal is too narrow (< 80 cols) — statusline may wrap awkwardly (there's `branchOverflow: "wrap"` config but still takes 3-4 lines)
- If you work with Claude API (not Claude Code) — plugin only runs in Claude Code
- If you already have a custom statusline — must choose one or the other

---

## Part 12 — Cần biết thêm / Things to know

### License / Legal

- **MIT** — free to use, modify, distribute, even commercially
- Author: Jarrod Watts, Sydney Australia (jarrodwatts.com)

### Security posture

- Author states explicitly: *"ClaudeHUD never falls back to credential scraping or undocumented API calls"*
- PR → CI → dist workflow (preventive supply-chain hardening) — compiled output never shipped in PRs
- Report vulnerabilities via GitHub private advisory

### Update mechanism

- **Automatic** via Claude Code `/plugin` UI
- Author bumps version in plugin.json → you see update prompt
- No need to re-run `/claude-hud:setup` after update

### Bus factor

- **1 maintainer** (Jarrod Watts). MIT + small scope = forkable if he goes dark.
- Active community contributors (5+ credited in CHANGELOG)
- Project is 3 months old; stability track record still forming

---

## Part 13 — Tóm lại / TL;DR

**VN:** claude-hud = plugin cho Claude Code hiển thị context / tools / agents / todos real-time. Cài đặt 5 phút, đánh giá 1 tuần, uninstall nếu không hợp. Phù hợp cao với Storm Bear operator (VN Scrum coach dùng Claude Code cho wiki build + team work).

**Verdict cho Storm Bear operator:** **HIGH priority pilot — cài đặt ngay.** Zero friction, immediate ROI nếu giải quyết context-budget blindness.

**EN:** claude-hud = Claude Code plugin that shows context / tools / agents / todos real-time. 5-minute install, 1-week evaluation, uninstall if not a fit. Strong fit for Storm Bear operator (VN Scrum coach using Claude Code for wiki builds + team work).

**Verdict for Storm Bear operator:** **HIGH priority pilot — install immediately.** Zero friction, immediate ROI if it solves your context-budget blindness.

---

## Links

- Repo: https://github.com/jarrodwatts/claude-hud
- Author: https://github.com/jarrodwatts
- Blog: https://jarrodwatts.com
- Preview image in README shows actual statusline rendering

## Storm Bear corpus cross-references

- `../claude-code-best-practice - Beginner Analysis/` (v34, 82 Claude Code tips)
- `../claude-howto - Beginner Analysis/` (v32, tutorial approach)
- `../oh-my-claudecode - Beginner Analysis/` (v27, 1st plugin-marketplace-native T1)

---

*(C) Claude-generated 2026-04-23 per LLM Wiki routine v2.1. Bilingual VN/EN for Storm Bear operator + anyone else curious about claude-hud.*
