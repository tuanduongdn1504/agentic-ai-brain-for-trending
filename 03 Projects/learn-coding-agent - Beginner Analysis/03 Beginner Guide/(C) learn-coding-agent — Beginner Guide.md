# (C) learn-coding-agent — Beginner Guide / Hướng dẫn người mới

> **Subject:** `sanbuphy/learn-coding-agent` ("Claude Code Architecture Study")
> **Wiki #53 — outside-scope archive (single-tool-internals-deep-dive)**
> Bilingual VN + EN

---

## ⚠️ ĐỌC PHẦN NÀY TRƯỚC / READ THIS FIRST

### License caveat (critical)

**EN:** This repository has **no formal LICENSE file**. README §"Copyright & Disclaimer" declares: *"This repository is provided strictly for technical research and educational purposes. Commercial use is strictly prohibited."* This is informal research-only-non-commercial-restriction without a formal license name (NOT Apache/MIT/AGPL/SUL/PolyForm).

**Practical impact for you:**
- ✅ Personal study + learning + reference: PERMITTED
- ✅ Cite in your own research / blog post / academic context: PERMITTED (under fair-use)
- ❌ Re-package for client work / Scrum coaching deliverables: **PROHIBITED**
- ❌ Use in commercial training materials / pitch decks: **PROHIBITED**
- ❌ Republish or fork for commercial offering: **PROHIBITED**

The author also includes a DMCA-style takedown clause: *"If you are the copyright owner and believe this repository content infringes your rights, please contact the repository owner for immediate removal."* — meaning Anthropic (or any third party) can request takedown.

**VN:** Repo này **không có file LICENSE chính thức**. README chỉ ghi "research + educational purposes; Commercial use is strictly prohibited" (chỉ học tập / nghiên cứu; cấm dùng thương mại). Đây là tuyên bố không chính thức (informal) — không phải license tên cụ thể (Apache/MIT/AGPL/SUL/PolyForm).

**Tác động thực tế:**
- ✅ Đọc + học + tham khảo cá nhân: ĐƯỢC
- ✅ Trích dẫn trong nghiên cứu cá nhân / blog: ĐƯỢC (fair-use)
- ❌ Đóng gói lại cho công việc khách hàng / Scrum coaching: **CẤM**
- ❌ Sử dụng trong tài liệu training thương mại / pitch deck: **CẤM**
- ❌ Republish hoặc fork để bán: **CẤM**

### Verifiability caveat

**EN:** All claims about Claude Code internals are **per Sanbu's analysis based on publicly-available online references** — NOT Anthropic-confirmed; NOT decompiled-from-binary claim; NOT insider-leak. Sample-verify before relying on specifics for operational decisions.

**VN:** Mọi tuyên bố về Claude Code internals đều **dựa trên phân tích của Sanbu từ nguồn công khai online** — KHÔNG phải Anthropic xác nhận; KHÔNG phải decompile binary; KHÔNG phải insider-leak. Hãy sample-verify trước khi dựa vào những chi tiết cụ thể cho quyết định vận hành.

### Abandoned-status caveat

**EN:** Repo created 2026-03-31, last push 2026-04-01 → **abandoned 24+ days at probe time**. Studied version is Claude Code v2.1.88. Current Claude Code may have changed (codenames updated, feature flags renamed, file paths refactored). Do NOT assume specifics are current.

**VN:** Repo tạo 2026-03-31, lần push cuối 2026-04-01 → **bỏ rơi 24+ ngày tại thời điểm probe**. Phiên bản nghiên cứu là Claude Code v2.1.88. Claude Code hiện tại có thể đã khác (codename mới, feature flag đổi tên, file path refactor). KHÔNG mặc định mọi chi tiết còn đúng hôm nay.

---

## 1. Repo này là gì? / What is this repo?

**EN:** Solo Chinese researcher Sanbu (sanbuphy / 散步 / blog aispacewalk.cn) compiled a 4-language (EN+CN+JA+KO) research archive of Claude Code v2.1.88 internals from publicly-available online references. The archive has:
- 4 root READMEs (English / 中文 / 日本語 / 한국어; ~45 KB each)
- 20 deep-dive markdown reports (5 topics × 4 languages)
- ZERO code; ZERO governance files (no LICENSE / no CONTRIBUTING / no AGENTS.md / etc.)
- Repo abandoned 24+ days post-creation despite 11.7K stars + **CORPUS-RECORD 168.2% fork-to-star inversion** (19,741 forks > 11,735 stars)

**The 5 topics:**
1. **Telemetry & Privacy** — what's collected, why direct API users can't UI-opt-out
2. **Hidden Features & Codenames** — Capybara/Tengu/Fennec/Numbat animal codenames + obscured feature flag naming + internal vs external user dual-tier prompts + hidden commands
3. **Undercover Mode** — Anthropic-employee mode that hides AI authorship in OSS commits
4. **Remote Control & Killswitches** — hourly polling + accept-or-die dialog + 6+ killswitches + GrowthBook flag-without-consent
5. **Future Roadmap** — Numbat (next model) + KAIROS (autonomous mode) + voice + 17 unreleased tools

**VN:** Tác giả Trung Quốc Sanbu (sanbuphy / 散步 / blog aispacewalk.cn) tổng hợp archive 4 ngôn ngữ (EN+CN+JA+KO) về internals của Claude Code v2.1.88 từ nguồn công khai online. Archive gồm:
- 4 README gốc (~45 KB mỗi)
- 20 báo cáo deep-dive markdown (5 chủ đề × 4 ngôn ngữ)
- KHÔNG code; KHÔNG file governance
- Repo bỏ rơi 24+ ngày sau khi tạo, dù có 11.7K stars + **KỶ LỤC CORPUS 168.2% fork-to-star** (19,741 forks > 11,735 stars)

---

## 2. Quick navigation: 5-report tour / Tham quan nhanh 5 báo cáo

**EN/VN combined:**

| # | EN file | Topic / Chủ đề | What you learn / Bạn học được |
|---|---------|----------------|-------------------------------|
| 01 | `docs/en/01-telemetry-and-privacy.md` | Telemetry pipeline / Đường ống telemetry | Two-tier (Anthropic 1P + Datadog), no UI-opt-out for direct API users / 2 tầng, không opt-out qua UI cho direct API |
| 02 | `docs/en/02-hidden-features-and-codenames.md` | Codenames + feature flags + ant vs external | Animal codenames (Capybara/Tengu/Numbat), obscured flag naming, internal employees get materially better prompts / Codename động vật, flag tên ngẫu nhiên, nhân viên Anthropic được prompt tốt hơn |
| 03 | `docs/en/03-undercover-mode.md` | Undercover mode / Chế độ ẩn danh | Anthropic employees auto-strip AI attribution in OSS commits; "Do not blow your cover" / Nhân viên Anthropic tự động ẩn AI attribution khi commit OSS |
| 04 | `docs/en/04-remote-control-and-killswitches.md` | Remote control / Điều khiển từ xa | Hourly polling, accept-or-die dialog, 6+ killswitches, GrowthBook A/B without consent / Polling 1 giờ/lần, dialog "đồng ý hoặc app exit", 6+ killswitch |
| 05 | `docs/en/05-future-roadmap.md` | Roadmap signals / Tín hiệu lộ trình | Numbat (next model), KAIROS (autonomous mode with `<tick>` heartbeats), voice mode, 17 unreleased tools / Numbat (model tiếp theo), KAIROS (chế độ tự chủ), voice, 17 tool chưa ra |

VN reader: docs/zh/ for Simplified Chinese; docs/ja/ for Japanese; docs/ko/ for Korean. **No VN translation exists.** If you want VN translation, you'd machine-translate from EN or CN (low effort; ~24 KB total).

---

## 3. 1-week reading roadmap / Lộ trình đọc 1 tuần

**Day 1 / Ngày 1 (~30 min):** Read README.md fully. Understand the architecture overview, ASCII diagrams, 12 progressive harness mechanisms, key design patterns. / Đọc README.md đầy đủ. Hiểu kiến trúc tổng quan, ASCII diagrams, 12 cơ chế harness, design patterns chính.

**Day 2 (~20 min):** Read `01-telemetry-and-privacy.md`. Understand what Claude Code collects on every event. Action: run `ls ~/.claude/telemetry/` to see your local telemetry-disk-state. / Đọc `01-...`. Hiểu Claude Code thu thập gì mỗi event. Hành động: chạy `ls ~/.claude/telemetry/` để thấy state telemetry trên máy bạn.

**Day 3 (~25 min):** Read `02-hidden-features-and-codenames.md`. Understand codename system + obscured flag naming + ant-vs-external prompt asymmetry. Note: as external user, you get a strictly-inferior product per Sanbu's claim. / Đọc `02-...`. Hiểu codename + flag naming + asymmetry ant-vs-external. Lưu ý: là external user, bạn nhận sản phẩm tệ hơn (theo phân tích Sanbu).

**Day 4 (~20 min):** Read `03-undercover-mode.md`. This is information-only for non-Anthropic users. Implication: when you see surprisingly-human commits in Anthropic-adjacent OSS repos, undercover-mode is one possibility. / Đọc `03-...`. Chỉ để biết với non-Anthropic users. Hệ quả: khi thấy commit "người-viết" trong repo OSS gần Anthropic, undercover-mode là một khả năng.

**Day 5 (~30 min):** Read `04-remote-control-and-killswitches.md`. Critical operational caveat: Claude Code may exit mid-session if you reject remote-settings-dangerous-changes dialog. **Save vault state frequently; commit mid-task.** / Đọc `04-...`. Cảnh báo vận hành quan trọng: Claude Code có thể exit giữa session nếu bạn từ chối dialog. **Lưu vault thường xuyên; commit giữa task.**

**Day 6 (~30 min):** Read `05-future-roadmap.md`. Understand Numbat next-model + KAIROS autonomous mode + voice mode + 17 unreleased tools. Plan vault Pattern #18 evolution. / Đọc `05-...`. Hiểu Numbat + KAIROS + voice + 17 tool. Lên kế hoạch tiến hóa Pattern #18 cho vault.

**Day 7 (~45 min):** Re-read all 5 reports. Cross-reference with your own Claude Code daily use. Sample-verify: pick 2-3 specific claims (file paths, env var names, killswitch flag names) and check against current Claude Code behavior. / Đọc lại 5 báo cáo. Cross-reference với daily Claude Code use của bạn. Sample-verify: chọn 2-3 tuyên bố cụ thể (file path, env var, killswitch flag) và kiểm tra thực tế.

**Total: ~3.5 hours over 1 week. / Tổng: ~3.5 giờ trong 1 tuần.**

---

## 4. Top 6 operational takeaways for Storm Bear / 6 takeaway vận hành cho Storm Bear

(See E4 entity page for full detail. Summary here.)

1. **Telemetry has no UI-opt-out for direct API users.** Anthropic + Datadog get env fingerprint, repo-URL hash, tool inputs (truncated), file extensions on every event. / Telemetry không opt-out qua UI cho direct API user.
2. **Remote killswitches can disable features mid-session.** Hourly polling; accept-or-die dialog; reject = app exits. Save vault state frequently. / Killswitch từ xa có thể disable feature giữa session. Lưu state thường xuyên.
3. **GrowthBook A/B assignment without consent.** Storm Bear sessions may behave differently across days based on opaque experiment groups. / Phân nhóm A/B không cần consent. Hành vi có thể khác giữa các ngày.
4. **External users get inferior prompts vs Anthropic-internal.** "Be extra concise" external vs "Err on side of more explanation" internal; ~29-30% Capybara v8 false-claims rate for external. **Verify-before-act for important decisions.** / External user nhận prompt tệ hơn ant-internal. Verify trước khi act với quyết định quan trọng.
5. **Numbat / KAIROS / voice / 17 unreleased tools coming.** Plan vault Pattern #18 infrastructure for upcoming model migration + autonomous-mode. / Numbat / KAIROS / voice / 17 tool sắp ra. Lên kế hoạch Pattern #18.
6. **Repo URL is fingerprinted (SHA256 first-16-char) and sent to Anthropic.** Server-side correlation across users/sessions/devices possible. Storm Bear vault git remote is fingerprinted; this is unavoidable for direct API. / URL repo bị fingerprint (SHA256 16 ký tự đầu) gửi Anthropic. Vault git remote bị fingerprint không tránh được.

---

## 5. What this archive is NOT / Đây KHÔNG phải

**EN:**
- ❌ NOT an Anthropic-confirmed source
- ❌ NOT a decompiled-from-binary leak
- ❌ NOT an insider source from an Anthropic employee
- ❌ NOT a maintained / updated reference (abandoned day-2)
- ❌ NOT a tool / framework / library you install
- ❌ NOT licensed for commercial re-use

**EN — what it IS:**
- ✅ A solo CN researcher's compilation from publicly-available online references and discussions
- ✅ A single-tool-internals-deep-dive sister-archive to system-prompts-leaks v21 multi-tool-prompt-collection
- ✅ A static point-in-time snapshot of Claude Code v2.1.88 (now possibly stale)
- ✅ Useful for personal Claude Code operational awareness
- ✅ Educational reference for understanding production agent harness architecture

**VN:** KHÔNG phải nguồn được Anthropic xác nhận; KHÔNG decompile binary; KHÔNG insider Anthropic; KHÔNG được maintain (bỏ rơi day-2); KHÔNG phải tool / framework cài đặt; KHÔNG license thương mại. **LÀ:** archive solo của tác giả CN từ nguồn công khai; sister-archive của system-prompts-leaks v21; snapshot tĩnh Claude Code v2.1.88 (có thể đã cũ); hữu ích cho operational awareness; giáo dục về kiến trúc agent harness.

---

## 6. Comparison with sister-archive system-prompts-leaks v21 / So sánh với archive anh-em v21

| Dimension | system-prompts-leaks v21 | learn-coding-agent v53 |
|-----------|---------------------------|------------------------|
| Subject scope | 31 AI tools (broad multi-tool) | 1 AI tool (Claude Code; single-tool deep-dive) |
| Content type | System prompts (extracted) | Architecture + telemetry + codenames + killswitches + roadmap |
| Stars | 135.5K | 11.7K |
| Forks | 34K | 19.7K (CORPUS-RECORD 168.2% inversion) |
| Author | x1xhlol (pseudonymous, multi-handle) | Sanbu (named GitHub, but low-identity) |
| Author region | Unknown | China (CN-blog active) |
| Maintenance | Active | Abandoned day-2 |
| License | GPL-3.0 (controversial application) | None formal; "Commercial use prohibited" only |
| Monetization | 6-channel (Patreon + Ko-fi + crypto + ZeroLeaks commercial) | Zero monetization signals |
| i18n | EN-only | Quadrilingual EN+CN+JA+KO |
| Pattern #38 fit | 38a multi-tool-prompt-archive | 38b single-tool-internals-deep-dive |

**Both are sister-archives in Pattern #38 prompt-leak-archive genre family.** v53 is the second N=2 data point that may promote #38 to CONFIRMED at next mini-audit.

---

## 7. Storm Bear pilot relevance / Mức độ phù hợp pilot Storm Bear

**EN: NOT A PILOT CANDIDATE.** Reasoning:
- Research-only license blocks commercial Scrum coaching content re-use
- Static abandoned archive (no update path)
- Subject IS Claude Code (Storm Bear's existing tool, not migration target)
- No installable surface

**Storm Bear pilot ranking unaffected at v53.** Top-11 unchanged from post-v52:
1. claude-hud v35
2. spec-kit v17
3. claude-howto v32
4. claude-code-best-practice v34
5. ruflo v42 (only if team scales)
6. OMC v27 / claude-howto self-onboarding
7. pi-mono v36
8. vercel-labs/agent-skills v51 (SKILL.md format reference)
9. markitdown v28 (doc ingestion)
10. crawl4ai v29 (web research)
11. graphify v16 (vault knowledge graph)

**v53 is REFERENCE-ONLY.** Use as Claude Code operational caveats reference; do not pilot.

**VN: KHÔNG phải pilot candidate.** License research-only chặn re-use thương mại; archive tĩnh đã bỏ rơi; subject IS Claude Code (đã đang dùng); không có surface cài đặt. Pilot ranking không đổi sau v53.

---

## 8. What to do after reading / Sau khi đọc, làm gì?

**EN:**
1. **Operational hygiene check** — verify your local `~/.claude/telemetry/` directory state; understand what's pending
2. **Save habit** — commit vault state more frequently (Claude Code may exit mid-session per Caveat 2)
3. **Verify-before-act** — for important Storm Bear decisions, sample-verify Claude Code outputs (Capybara v8 false-claims rate ~29-30% for external users)
4. **Plan Pattern #18 evolution** — Numbat + KAIROS + voice coming; vault may need infrastructure changes
5. **Cross-reference** — read v21 system-prompts-leaks wiki for sister-archive context
6. **Do NOT republish** — research-only license blocks commercial re-use

**VN:** Kiểm tra `~/.claude/telemetry/` state local; commit vault thường xuyên hơn (Caveat 2); verify trước khi act với quyết định quan trọng; lên kế hoạch Pattern #18 cho Numbat/KAIROS/voice; đọc v21 wiki cho context anh-em; KHÔNG republish.

---

## 9. Cross-references / Tham chiếu

- **E1** — Core archive (5-doc + roadmap signals)
- **E2** — Pattern implications (#38 38b N=2 / #29 29-absent-4 / #75 N=2)
- **E3** — Sanbu / sanbuphy.cn ecosystem + abandoned-day-2 mystery
- **E4** — 42nd Storm Bear meta-entity (Claude Code operational caveats)
- **C1, C2, C3** — Cluster summaries
- **04 Phase 4b Deliverable** — Pattern + sister-archive comparison
- **system-prompts-leaks v21** — Sister-archive (Pattern #38 38a parent)

---

## 10. Honest verdict / Đánh giá thật

**EN:** learn-coding-agent v53 is a **medium-value reference** for Storm Bear operator. Top 6 operational caveats are genuinely actionable for daily Claude Code use. Architecture documentation is useful Claude Code internals reference. Pattern Library payoff (#38 38b N=2 + #29 29-absent-4 + #75 N=2) is significant. **BUT**: claims need sample-verification (Sanbu's analysis, not Anthropic-confirmed); license blocks commercial re-use; archive is abandoned and may already be partially stale.

**Recommended commitment**: **3.5h reading over 1 week** + ongoing operational-awareness application. Do NOT plan deep dependency.

**VN:** v53 là **reference giá trị trung bình** cho Storm Bear operator. 6 cảnh báo vận hành thực sự actionable cho daily Claude Code use. Tài liệu kiến trúc là reference internals tốt. Lợi ích Pattern Library lớn. **NHƯNG**: tuyên bố cần sample-verify; license cấm re-use thương mại; archive đã bỏ rơi và có thể đã cũ một phần.

**Cam kết đề xuất**: **3.5 giờ đọc trong 1 tuần** + ứng dụng operational-awareness lâu dài. KHÔNG nên dependency sâu.

---

## 11. Key claims that need verification / Tuyên bố cần verify

For Storm Bear operator who wants to sample-verify Sanbu's claims:

1. **`OTEL_LOG_TOOL_DETAILS=1` env enables full tool input capture** → set this env var, run a query with sensitive-content tool input, check `~/.claude/telemetry/` for full vs truncated logging
2. **`~/.claude/projects/<hash>/sessions/<id>.jsonl` session persistence format** → check existing sessions on your machine; verify JSONL format + structure
3. **40+ built-in tools** → run `/help` or check Claude Code's tool list against Sanbu's inventory (FILE OPS / SEARCH / EXECUTION / WEB / AGENT / MCP / SKILLS / INTERACTION / PLANNING / SYSTEM)
4. **80+ slash commands** → run `/` in Claude Code; count
5. **Hidden commands `/btw`, `/stickers`, `/thinkback`, `/effort`** → try in Claude Code; verify behavior
6. **5 MCP transports (stdio / sse / http / ws / sdk)** → check Claude Code MCP configuration docs

If 4+ of 6 above verify correctly, Sanbu's analysis has reasonable accuracy. If <2 verify, treat archive as suspect.

---

## 12. Final framing / Lời cuối

**EN:** This archive exists because Anthropic's Claude Code product is closed-source but widely-used; users want to understand internals; legal-licensed reverse-engineering archives fill that gap. v53 learn-coding-agent is one such archive (sister to v21 system-prompts-leaks). Use respectfully: read for personal understanding, do not republish, verify claims, treat as point-in-time snapshot.

**VN:** Archive này tồn tại vì sản phẩm Claude Code của Anthropic đóng-source nhưng được dùng rộng; users muốn hiểu internals; archive reverse-engineering hợp pháp lấp khoảng trống đó. v53 là một trong số đó (anh-em v21). Dùng có trách nhiệm: đọc để hiểu cá nhân, không republish, verify claims, coi như snapshot tĩnh.

---

## 13. Quick reference card / Thẻ tham chiếu nhanh

```
Repo:        sanbuphy/learn-coding-agent
URL:         https://github.com/sanbuphy/learn-coding-agent
Stars:       11,735      Forks: 19,741 (168.2% inversion CORPUS RECORD)
License:     None formal (research-only via README only)
Status:      ABANDONED 2026-04-01 (24+ days stale)
Languages:   EN + CN + JA + KO (quadrilingual)
Studies:     Claude Code v2.1.88 internals
Reports:     5 deep-dives (telemetry / hidden / undercover / remote / roadmap)
Author:      Sanbu (sanbuphy / 散步) — CN; blog aispacewalk.cn; 279 repos
Pilot rank:  REFERENCE-ONLY (not in top-11)
Read time:   ~3.5h over 1 week
Wiki #53:    Outside-scope archive (Pattern #38 38b sub-variant N=2)
```
