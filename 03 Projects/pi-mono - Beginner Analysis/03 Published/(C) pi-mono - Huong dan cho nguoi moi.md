# pi-mono — Hướng dẫn cho người mới (bilingual VN+EN)

**Tác giả:** Claude (via Storm Bear vault, routine v2.1)
**Date:** 2026-04-23
**Chủ đề:** `badlogic/pi-mono` — AI agent toolkit của Mario Zechner (tác giả libGDX)
**Độ dài ước tính:** ~430 dòng / ~15 phút đọc

> **VN:** Đây là guide cho người mới bắt đầu với pi-mono — một bộ công cụ AI agent tự-chủ (stand-alone), có thể coi như "Claude Code phiên bản open-source đa-provider." Target reader: developer đã dùng qua Claude Code hoặc một coding agent tương tự, đang cân nhắc thử pi như một alternative.
>
> **EN:** Beginner's guide to pi-mono — an open-source AI agent toolkit structurally comparable to Claude Code but multi-provider (20+ LLM providers) and solo-maintained by Mario Zechner (libGDX creator). Target reader: developer familiar with Claude Code or similar coding agents, evaluating pi as an alternative.

---

## 1. pi-mono là gì? / What is pi-mono?

### VN

pi-mono là một **monorepo** (7 package TypeScript) do **Mario Zechner** (người Áo, tác giả framework game Java libGDX) publish từ tháng 8/2025. Flagship product là **pi-coding-agent** — một terminal coding agent CLI cạnh tranh trực tiếp với Claude Code, Cursor CLI, Codex CLI.

Cái tên "pi" không có ý nghĩa đặc biệt — Mario donated domain `pi.dev` từ người bạn tại `exe.dev`. "Monorepo" trong tên chỉ cấu trúc code: tất cả 7 package được publish cùng nhau, cùng version.

**Trạng thái (4/2026):** 38.950 stars / 4.542 forks / 200+ releases trong 8.5 tháng / MIT license / TypeScript 96.3%. **Đang được maintain rất tích cực** — commit gần nhất là hôm nay, release v0.69.0 được push 1 ngày trước wiki này.

### EN

pi-mono is a **monorepo** (7 TypeScript packages) published by **Mario Zechner** (Austrian; creator of the libGDX Java game framework) starting August 2025. The flagship is **pi-coding-agent** — a terminal coding agent CLI directly competing with Claude Code, Cursor CLI, and Codex CLI.

The name "pi" carries no special meaning — Mario was donated the `pi.dev` domain by friends at `exe.dev`. "Monorepo" in the name refers to code organization: all 7 packages ship together under lockstep versioning.

**Status (Apr 2026):** 38,950 stars / 4,542 forks / 200+ releases in 8.5 months / MIT license / TypeScript 96.3%. **Actively maintained** — latest commit today; v0.69.0 pushed one day before this wiki.

---

## 2. Mario Zechner là ai? / Who is Mario Zechner?

### VN

- **`@badlogic`** trên GitHub, **`@mariozechner`** trên npm, **`@badlogicgames`** trên Twitter/X
- **Người Áo** (không có thông tin city cụ thể từ public profile)
- **Creator của libGDX** — framework Java game-dev 25.000 stars, đã được maintain từ ~2009 (15+ năm)
- Hiện nay focus vào AI agent tooling thông qua pi-mono

pi-mono **không phải** project "solo đầu tay" — Mario đã có 15 năm kinh nghiệm maintain OSS framework ở scale tương tự. Điều này giải thích tại sao pi-mono có **governance rất chặt chẽ** ngay từ đầu (AGENTS.md 182 dòng, 3 GitHub Actions gate cho contribution, CHANGELOG discipline per-package).

**Strategic signal cho operator Storm Bear:** Mario mang theo 25K-star follower base từ libGDX sang agent-space, giúp pi-mono đạt 38.9K trong 8.5 tháng. Đây là ví dụ điển hình của **cross-domain founder-equity** (vốn-uy-tín chuyển miền) — Mario leverage reputation cũ để tăng tốc initial discovery cho project mới.

### EN

- `@badlogic` on GitHub, `@mariozechner` on npm, `@badlogicgames` on X/Twitter
- **Austrian** (no specific city in public profile)
- **Creator of libGDX** — Java game-dev framework, 25K stars, maintained since ~2009 (15+ years)
- Now focused on AI agent tooling via pi-mono

pi-mono is **not a first solo project** — Mario brings 15 years of similar-scale OSS-framework maintenance experience. This explains pi-mono's unusually tight governance from day one (182-line AGENTS.md, 3 GitHub Actions contribution-gate workflows, per-package CHANGELOG discipline).

**Strategic signal for Storm Bear operator:** Mario leveraged his 25K-star libGDX follower base to reach 38.9K in 8.5 months on pi-mono. This is a textbook **cross-domain founder-equity** transfer — using reputation-capital from domain A to accelerate project-launch in domain B.

---

## 3. 7 package monorepo tổng quan / 7-package monorepo overview

### VN

| Package | Vai trò |
|---------|---------|
| **pi-coding-agent** | Flagship: CLI terminal coding agent (thay thế Claude Code) |
| **pi-ai** | Foundation: Unified LLM API cho 20+ provider |
| **pi-agent-core** | Foundation: Agent runtime với tool calling + state management |
| **pi-tui** | Utility: Terminal UI framework với differential rendering |
| **pi-web-ui** | Utility: Web components cho AI chat interface |
| **pi-mom** | Spin-off: Slack bot được power bởi pi-coding-agent |
| **pi-pods** | Spin-off: CLI để deploy vLLM lên GPU pod |

**Lockstep versioning:** Tất cả 7 package luôn cùng version. Mỗi release bump cả 7.

**Hầu hết user chỉ cần dùng pi-coding-agent.** Nếu bạn muốn embed pi-ai hoặc pi-agent-core vào app của bạn → đó là advanced use-case.

### EN

| Package | Role |
|---------|------|
| **pi-coding-agent** | Flagship: terminal coding agent CLI (Claude Code alternative) |
| **pi-ai** | Foundation: unified LLM API across 20+ providers |
| **pi-agent-core** | Foundation: agent runtime with tool calling + state management |
| **pi-tui** | Utility: TUI framework with differential rendering |
| **pi-web-ui** | Utility: web components for AI chat interfaces |
| **pi-mom** | Spin-off: Slack bot powered by pi-coding-agent |
| **pi-pods** | Spin-off: CLI for deploying vLLM on GPU pods |

**Lockstep versioning:** All 7 packages always share the same version. Every release bumps all 7.

**Most users only need pi-coding-agent.** Embedding pi-ai or pi-agent-core in your own app is an advanced use case.

---

## 4. Install nhanh 5 phút / 5-minute install

### VN

```bash
# 1. Prereq: Node.js đã được cài (kiểm tra bằng node -v — cần v18+)
node -v

# 2. Install pi toàn hệ thống
npm install -g @mariozechner/pi-coding-agent

# 3. Set API key (Anthropic as default)
export ANTHROPIC_API_KEY="sk-ant-..."

# 4. Chạy
pi "Hello, what can you do?"
```

**Alternative auth:** chạy `pi` rồi dùng `/login` để OAuth với Claude Pro/Max, ChatGPT Plus/Pro, GitHub Copilot, Google Gemini CLI, hoặc Google Antigravity.

**Alternative provider:** thay `export ANTHROPIC_API_KEY=...` bằng `export OPENAI_API_KEY=...` hoặc `export GEMINI_API_KEY=...` hoặc 17+ provider khác.

**Local models:** `pi --provider ollama --model qwen2.5-coder` hoặc tương tự cho vLLM/LM Studio.

### EN

```bash
# 1. Prereq: Node.js installed (check node -v — need v18+)
node -v

# 2. Install pi globally
npm install -g @mariozechner/pi-coding-agent

# 3. Set API key (Anthropic as default)
export ANTHROPIC_API_KEY="sk-ant-..."

# 4. Run
pi "Hello, what can you do?"
```

**Alternative auth:** run `pi` then use `/login` for OAuth with Claude Pro/Max, ChatGPT Plus/Pro, GitHub Copilot, Google Gemini CLI, or Google Antigravity.

**Alternative provider:** replace `export ANTHROPIC_API_KEY=...` with `export OPENAI_API_KEY=...` or `export GEMINI_API_KEY=...` or 17+ others.

**Local models:** `pi --provider ollama --model qwen2.5-coder` or similar for vLLM/LM Studio.

---

## 5. So sánh với Claude Code / Comparison with Claude Code

### VN

| Dimension | pi-coding-agent | Claude Code |
|-----------|-----------------|-------------|
| **Provider** | 20+ (Anthropic / OpenAI / Google / Groq / local vLLM / ...) | Anthropic-only (Claude Pro/Max subscription) |
| **MCP support** | **KHÔNG** (cố ý loại; dùng CLI-tools + Skills thay) | Có (first-class) |
| **Agent Skills** | Có (via pi-skills sibling repo, compatible) | Có |
| **Session export** | HTML + GitHub gist + HF dataset | Text log |
| **Session fork/branch** | `/fork` + `/clone` + `/tree` | KHÔNG (linear) |
| **Extension API** | TypeScript modules, full system access | Claude Code plugin system |
| **Messaging queue** | Steering + follow-up queues | KHÔNG |
| **Session sharing philosophy** | First-class workflow (HF dataset upload) | KHÔNG |
| **Platform support** | Linux / macOS / Windows / Termux / tmux | Terminal-based |
| **License** | MIT | Proprietary (Anthropic) |
| **Maintainer** | Mario Zechner (solo, libGDX veteran) | Anthropic (corporate) |
| **Age** | 8.5 tháng | 1+ năm |
| **Star** | 38.9K | Closed product — no star metric |
| **Learning curve** | ~110 primitives | Comparable |

**Verdict tóm tắt:**
- **Nếu bạn cần multi-provider** → pi thắng rõ ràng
- **Nếu bạn cần MCP integration** → Claude Code thắng (pi cố ý không support)
- **Nếu bạn cần maturity + enterprise backing** → Claude Code thắng
- **Nếu bạn cần session export + sharing** → pi thắng

### EN

| Dimension | pi-coding-agent | Claude Code |
|-----------|-----------------|-------------|
| **Provider** | 20+ (Anthropic / OpenAI / Google / Groq / local vLLM / ...) | Anthropic-only (Claude Pro/Max subscription) |
| **MCP support** | **NO** (deliberately excluded; uses CLI-tools + Skills alternatives) | Yes (first-class) |
| **Agent Skills** | Yes (via pi-skills sibling repo, compatible) | Yes |
| **Session export** | HTML + GitHub gist + HF dataset | Text log |
| **Session fork/branch** | `/fork` + `/clone` + `/tree` | NO (linear) |
| **Extension API** | TypeScript modules, full system access | Claude Code plugin system |
| **Messaging queue** | Steering + follow-up queues | NO |
| **Session sharing philosophy** | First-class workflow (HF dataset upload) | NO |
| **Platform support** | Linux / macOS / Windows / Termux / tmux | Terminal-based |
| **License** | MIT | Proprietary (Anthropic) |
| **Maintainer** | Mario Zechner (solo, libGDX veteran) | Anthropic (corporate) |
| **Age** | 8.5 months | 1+ year |
| **Stars** | 38.9K | Closed product — no star metric |
| **Learning curve** | ~110 primitives | Comparable |

**Verdict summary:**
- **Need multi-provider** → pi wins
- **Need MCP integration** → Claude Code wins (pi deliberately opts out)
- **Need maturity + enterprise backing** → Claude Code wins
- **Need session export + sharing** → pi wins

---

## 6. Core commands / Các lệnh chính

### VN

**Slash commands (trong interactive mode):**

| Command | Tác dụng |
|---------|----------|
| `/login` `/logout` | OAuth subscription login |
| `/model` | Switch model |
| `/scoped-models` | Config danh sách model cho Ctrl+P cycling |
| `/settings` | Mở settings panel |
| `/resume` | Browse past sessions |
| `/new` | Start new session |
| `/name <name>` | Đặt tên session |
| `/fork` | Tạo session mới từ một previous message |
| `/clone` | Duplicate current session |
| `/tree` | Navigate session branches |
| `/compact [prompt]` | Manual context compact |
| `/export [file]` | Export session sang HTML |
| `/share` | Upload session lên GitHub gist |
| `/copy` | Copy last assistant message |
| `/reload` | Reload extensions/skills/prompts |
| `/hotkeys` | Show all keybindings |
| `/changelog` | Show version history |
| `/quit` | Exit pi |

**Keybindings phổ biến:**

| Key | Action |
|-----|--------|
| `Ctrl+C` | Clear editor (2 lần để thoát) |
| `Esc` | Cancel (2 lần để mở `/tree`) |
| `Ctrl+L` | Mở model selector |
| `Ctrl+P` | Cycle model forward |
| `Shift+Tab` | Cycle thinking level (off/minimal/low/medium/high/xhigh) |
| `Shift+Enter` | Multi-line input |
| `Tab` | Path autocomplete |
| `Ctrl+V` | Paste image |
| `@` | Fuzzy file reference (type @ rồi autocomplete filename) |
| `!command` | Run bash + send output to LLM |
| `!!command` | Run bash nhưng KHÔNG send output |

### EN (same content, translated above)

---

## 7. Storm Bear operator use-cases / Use cases cho operator

### VN

Nếu bạn là **Scrum coach / software developer dùng Claude Code hàng ngày** (như profile của Storm Bear operator), pi có thể là:

**Use case 1: Backup runtime khi Anthropic gặp sự cố**
- Cài sẵn pi; set `OPENAI_API_KEY` hoặc `GEMINI_API_KEY` làm backup
- Khi Claude Code xuống → chạy `pi --provider openai --model gpt-4o` để tiếp tục

**Use case 2: So sánh output chất lượng giữa các provider**
- Mid-session switch provider bằng `/model` → thấy ngay Claude vs GPT-5 khác nhau thế nào với cùng task
- Dùng được cho research / due-diligence trước khi commit vào provider cụ thể

**Use case 3: Local model experimentation**
- Cài Ollama hoặc LM Studio → chạy `pi --provider ollama --model qwen2.5-coder`
- Test xem local model có đủ chất cho tác vụ nào không (ví dụ: documentation rewriting vs complex reasoning)

**Use case 4: Publish session data công khai**
- Sau khi hoàn thành một wiki Scrum / tutorial session, export HTML + push lên HF dataset
- Học hỏi từ community (xem sessions của người khác)
- Build public portfolio signal

**Use case KHÔNG nên dùng pi:**
- Nếu bạn dựa nặng vào MCP server (pi không support MCP out-of-box)
- Nếu bạn muốn integration sâu với Claude Code ecosystem (pi standalone, không plugin-compatible)

### EN

If you're a **Scrum coach / software developer using Claude Code daily** (Storm Bear operator profile), pi can be:

**Use case 1: Backup runtime during Anthropic outages**
- Pre-install pi; set `OPENAI_API_KEY` or `GEMINI_API_KEY` as backup
- When Claude Code goes down → run `pi --provider openai --model gpt-4o` to continue

**Use case 2: Cross-provider output quality comparison**
- Mid-session `/model` switch → see Claude vs GPT-5 delta on same task immediately
- Useful for research / due-diligence before committing to a specific provider

**Use case 3: Local model experimentation**
- Install Ollama or LM Studio → run `pi --provider ollama --model qwen2.5-coder`
- Test whether local models are sufficient for specific tasks (e.g. doc rewriting vs complex reasoning)

**Use case 4: Public session data publication**
- After finishing a wiki / Scrum tutorial session, export HTML + push to HF dataset
- Learn from community (read others' sessions)
- Build public portfolio signal

**Do NOT use pi if:**
- You rely heavily on MCP servers (pi doesn't support MCP natively)
- You want deep Claude Code ecosystem integration (pi is standalone, not plugin-compatible)

---

## 8. Pilot roadmap cho Storm Bear / 2-4 hour pilot plan

### VN

**Week 1 (2 giờ): Install + baseline test**
- [ ] Install pi-coding-agent (10 phút)
- [ ] Cấu hình API keys cho 2 provider (Anthropic + 1 backup) (5 phút)
- [ ] Chạy 1 wiki-generation session với Claude → export HTML (30 phút)
- [ ] Chạy lại session với GPT-5 → export HTML (30 phút)
- [ ] So sánh 2 HTML output side-by-side (20 phút)
- [ ] Note 3 sự khác biệt quan trọng vào `04 Reviews/pi-mono-pilot-notes.md` (25 phút)

**Week 2 (optional, +2 giờ): Advanced features**
- [ ] Install pi-skills từ `npm:@mariozechner/pi-skills` (10 phút)
- [ ] Test 1 skill cross-runtime (pi + Claude Code invocation với same skill) (45 phút)
- [ ] Explore session fork + clone (`/fork` + `/clone`) (30 phút)
- [ ] Test `/share` upload session lên GitHub gist (10 phút)
- [ ] Write 1-page "pi vs Claude Code cho Storm Bear workflow" decision-doc (25 phút)

**Outcome expected:**
- Biết chính xác khi nào dùng pi thay Claude Code (nếu có)
- Có backup runtime ready cho Anthropic-outage scenario
- Understand cross-provider handoff workflow

### EN

**Week 1 (2 hours): Install + baseline test**
- [ ] Install pi-coding-agent (10 min)
- [ ] Configure API keys for 2 providers (Anthropic + 1 backup) (5 min)
- [ ] Run 1 wiki-generation session with Claude → export HTML (30 min)
- [ ] Re-run session with GPT-5 → export HTML (30 min)
- [ ] Compare both HTMLs side-by-side (20 min)
- [ ] Log 3 key differences to `04 Reviews/pi-mono-pilot-notes.md` (25 min)

**Week 2 (optional, +2 hours): Advanced features**
- [ ] Install pi-skills via `npm:@mariozechner/pi-skills` (10 min)
- [ ] Test 1 cross-runtime skill (invoke same skill via pi + Claude Code) (45 min)
- [ ] Explore session fork + clone (`/fork` + `/clone`) (30 min)
- [ ] Test `/share` upload to GitHub gist (10 min)
- [ ] Write 1-page "pi vs Claude Code for Storm Bear workflow" decision-doc (25 min)

**Expected outcome:**
- Know precisely when (if ever) to use pi over Claude Code
- Backup runtime ready for Anthropic-outage scenarios
- Understand cross-provider handoff workflow

---

## 9. Ethical / quality caveats / Lưu ý về ethical + chất lượng

### VN

**Không có red flags đáng lo ngại:**
- License: MIT (clean; không commercial-gate)
- Author: Mario Zechner (real name + public identity + long OSS track record)
- Monetization: không có crypto / không có paid tier / không có data-harvesting (HF session upload là opt-in)
- Governance: `lgtm`/`lgtmi` gate chặt nhưng transparent — rules trong CONTRIBUTING.md rõ ràng

**Quality caveats minor:**
- Solo maintainer → bus factor = 1 (Mario là toàn bộ project)
- 8.5 tháng tuổi → ít production-track-record hơn Claude Code
- Contribution gate cao → khó contribute back (cần `lgtm` approval trước)
- EN-only docs → không có VN cho VN-client demos

**Không phải cho:**
- Production-critical Scrum coaching workflows mà không thể afford downtime (Claude Code enterprise backing ăn đứt)
- Beginners hoàn toàn mới với coding agents (learning curve ~110 primitives)

### EN

**No red flags:**
- License: MIT (clean; no commercial gating)
- Author: Mario Zechner (real name + public identity + long OSS track record)
- Monetization: no crypto / no paid tier / no data-harvesting (HF session upload is opt-in)
- Governance: `lgtm`/`lgtmi` gate is strict but transparent — rules clear in CONTRIBUTING.md

**Minor quality caveats:**
- Solo maintainer → bus factor = 1 (Mario is the whole project)
- 8.5 months old → less production track record than Claude Code
- High contribution gate → contributing back requires upfront `lgtm` approval
- EN-only docs → no VN for Vietnamese-client demos

**Not for:**
- Production-critical Scrum coaching workflows that can't afford downtime (Claude Code enterprise backing wins)
- Complete beginners to coding agents (~110 primitive learning curve)

---

## 10. Additional resources / Tài nguyên thêm

### VN

- **Repo:** https://github.com/badlogic/pi-mono
- **Homepage:** https://pi.dev
- **Discord:** discord.gg/3cU7Bz4UPx
- **Mario's Twitter:** @badlogicgames
- **Mario's website:** mariozechner.at
- **pi-skills:** https://github.com/badlogic/pi-skills (Claude Code + Codex CLI compatible skills)
- **pi-share-hf:** https://github.com/badlogic/pi-share-hf (HF dataset uploader cho sessions)
- **Mario's HF dataset:** huggingface.co/datasets/badlogicgames/pi-mono (sessions của Mario)
- **AGENTS.md:** https://github.com/badlogic/pi-mono/blob/main/AGENTS.md (development rules)
- **CONTRIBUTING.md:** https://github.com/badlogic/pi-mono/blob/main/CONTRIBUTING.md

### EN (same resources)

---

## 11. Storm Bear relevance summary / Tóm tắt relevance cho Storm Bear

### VN

**Pilot priority: MEDIUM (NEW #3 trong framework-pilot-ranking post-v36)**

- **Pros:** Multi-provider escape-hatch, session export/share workflow, Mario's libGDX credibility signal, MIT + active maintenance, 1-command install
- **Cons:** Solo bus factor, no MCP, EN-only, higher learning curve than Claude Code, high contribution-gate friction

**Action at v36:**
1. Cài pi-coding-agent như backup runtime (2 giờ pilot) — nếu Claude Code gặp outage
2. Note Pattern observations vào Pattern Library (đã làm trong Phase 4b deliverable)
3. KHÔNG switch primary runtime từ Claude Code sang pi ngay — chưa đủ production-track-record để justify chi phí chuyển đổi

**Strategic reminder:**
Mario's cross-domain founder-equity transition (libGDX → pi-mono) là pattern đáng nhớ cho Storm Bear future — nếu 1 ngày Storm Bear publish public AI-Scrum-tool, reputation-capital từ Scrum-coach brand là lever thực sự.

### EN

**Pilot priority: MEDIUM (NEW #3 in framework-pilot-ranking post-v36)**

- **Pros:** Multi-provider escape-hatch, session export/share workflow, Mario's libGDX credibility signal, MIT + active maintenance, 1-command install
- **Cons:** Solo bus factor, no MCP, EN-only, higher learning curve than Claude Code, high contribution-gate friction

**Action at v36:**
1. Install pi-coding-agent as backup runtime (2-hour pilot) — for Anthropic outage scenarios
2. Record Pattern observations in Pattern Library (done in Phase 4b deliverable)
3. Do NOT switch primary runtime from Claude Code to pi — insufficient production track record to justify switching cost

**Strategic reminder:**
Mario's cross-domain founder-equity transition (libGDX → pi-mono) is a pattern worth remembering for Storm Bear's future — if Storm Bear ever publishes a public AI-Scrum-tool, reputation-capital from the Scrum-coach brand is a real lever.

---

*(C) Claude-generated 2026-04-23 per routine v2.1. Bilingual VN/EN guide for pi-mono v0.69.0 wiki v1.*
