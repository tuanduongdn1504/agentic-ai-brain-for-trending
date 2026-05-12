# andrej-karpathy-skills — Hướng dẫn cho người mới / Beginner Guide

> **Subject:** [`forrestchang/andrej-karpathy-skills`](https://github.com/forrestchang/andrej-karpathy-skills) — *"A single CLAUDE.md file to improve Claude Code behavior, derived from Andrej Karpathy's observations on LLM coding pitfalls."*
> **Wiki version:** v63 / Build date: 2026-05-09

---

## 🇻🇳 Tiếng Việt

### Đây là gì?

Một plugin nhỏ — chỉ chứa **1 skill duy nhất** — cài vào Claude Code (hoặc Cursor) để thay đổi *cách AI hành xử* khi viết code. Không phải framework, không phải workflow, chỉ là **4 nguyên tắc hành vi** rút ra từ một bài tweet của Andrej Karpathy về những sai lầm phổ biến của LLM khi code.

**Tác giả:** forrestchang (cũng là founder dự án [Multica](https://github.com/multica-ai/multica)).
**Nguồn cảm hứng:** [Tweet của Andrej Karpathy](https://x.com/karpathy/status/2015883857489522876).

### 4 nguyên tắc

1. **Think Before Coding** (Suy nghĩ trước khi code) — Đừng giả định ngầm. Nếu không chắc, hỏi. Nếu có nhiều cách hiểu, trình bày tất cả. Nếu có cách đơn giản hơn, nói ra.
2. **Simplicity First** (Đơn giản trước) — Code tối thiểu giải quyết vấn đề. Không tính năng dự phòng, không abstraction cho code dùng 1 lần, không "linh hoạt" mà không ai yêu cầu. Hỏi: *"Một senior engineer có nói cái này phức tạp quá không?"*
3. **Surgical Changes** (Sửa chính xác) — Chỉ sửa những gì cần. Không "cải tiến" code lân cận, không refactor những gì không hỏng. Mỗi dòng thay đổi phải truy được về yêu cầu của user.
4. **Goal-Driven Execution** (Định hướng mục tiêu) — Biến yêu cầu thành tiêu chí thành công có thể kiểm chứng. Ví dụ: "Sửa bug X" → "Viết test tái hiện bug X, rồi làm test pass."

### Tại sao 121K sao trong 102 ngày?

- **Karpathy là tên tuổi lớn** — bất cứ chắt lọc tốt từ Karpathy đều thừa hưởng độ phủ
- **"Một file CLAUDE.md duy nhất" dễ bán** — cài đặt mất 2 phút, chỉ cần `curl` 1 file
- **Anti-overengineering chạm đúng nỗi bực** — nhiều người chán LLM viết code rườm rà
- **Hỗ trợ 3 nền tảng** (Claude Code plugin / per-project CLAUDE.md / Cursor rule) — tiếp cận đa số coder
- **Song ngữ EN+ZH** — mở thị trường developer Trung Quốc

### Cài đặt nhanh

**Cách A — Plugin marketplace (đề xuất):**
```
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

**Cách B — Per-project CLAUDE.md:**
```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
```

**Cách C — Cursor:**
Mở project trong Cursor, file `.cursor/rules/karpathy-guidelines.mdc` tự động áp dụng.

### Có nên dùng cho Storm Bear vault?

**Câu trả lời ngắn:** Có, nhưng theo cách *layered* — KHÔNG dùng làm methodology chính, mà dùng làm **lớp behavioral overlay** trên các pilot khác (cc-sdd / codex-plugin-cc / free-claude-code).

**Pilot priority:** **#3.5 / Tier-2** (sau cc-sdd v61 / codex-plugin-cc v62 / free-claude-code v60). Lý do: 4 nguyên tắc thay đổi *cách* AI hành xử, nhưng KHÔNG thêm workflow phase mới (như cc-sdd có spec → plan → tasks → impl).

**Khuyến nghị deployment:** sau khi pilot Tier-1 đã ổn định (Week 3+), cài thêm karpathy-skills theo per-project mode (KHÔNG per-vault, vì 4 nguyên tắc có thể xung đột với routine v2.1 wiki-build workflow).

### Tóm tắt: Khi nào dùng karpathy-skills?

✅ **Dùng khi:** đang viết code production trong real monorepo + muốn AI suy nghĩ trước khi code + ghét overengineered solutions.

❌ **Không dùng khi:** đang chạy wiki-build routine v2.1 (sẽ xung đột với Phase 0 probe) + đang prototype nhanh (4 nguyên tắc làm chậm).

### Trả lời câu hỏi "thay thế cc-sdd được không?"

**KHÔNG.** karpathy-skills + mattpocock-skills là **behavioral overlay + skills collection** — sửa CÁCH AI nghĩ và thêm narrow-task capabilities. cc-sdd là **methodology workflow harness** — thêm CÁC PHASE workflow mới (spec/plan/tasks/impl + adversarial review). Khác category. Combo có thể bổ sung cho cc-sdd như orthogonal layer, KHÔNG thay thế được.

---

## 🇬🇧 English

### What is this?

A tiny plugin — containing **just 1 skill** — that you install into Claude Code (or Cursor) to change *how the AI behaves* when writing code. Not a framework, not a workflow — just **4 behavioral principles** distilled from an Andrej Karpathy tweet on common LLM coding pitfalls.

**Author:** forrestchang (also founder of [Multica](https://github.com/multica-ai/multica)).
**Inspiration:** [Andrej Karpathy's tweet](https://x.com/karpathy/status/2015883857489522876).

### The 4 principles

1. **Think Before Coding** — Don't assume silently. If uncertain, ask. If multiple interpretations exist, present all. If there's a simpler approach, say so.
2. **Simplicity First** — Minimum code that solves the problem. No speculative features, no abstractions for single-use code, no "flexibility" that wasn't requested. Ask: *"Would a senior engineer say this is overcomplicated?"*
3. **Surgical Changes** — Touch only what you must. Don't "improve" adjacent code, don't refactor what isn't broken. Every changed line should trace to the user's request.
4. **Goal-Driven Execution** — Transform tasks into verifiable success criteria. Example: "Fix bug X" → "Write a test that reproduces bug X, then make it pass."

### Why 121K stars in 102 days?

- **Karpathy is a large-name source** — any good distillation inherits viral velocity
- **"Single CLAUDE.md file" sells** — 2-minute setup, just `curl` one file
- **Anti-overengineering taps real frustration** — many devs are tired of LLM bloat
- **3-platform distribution** (Claude Code plugin / per-project / Cursor rule) — covers most coders
- **Bilingual EN+ZH** — opens Chinese developer market

### Quick install

**Option A — Plugin marketplace (recommended):**
```
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

**Option B — Per-project CLAUDE.md:**
```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md
```

**Option C — Cursor:**
Open project in Cursor; `.cursor/rules/karpathy-guidelines.mdc` auto-applies.

### Should I use it for Storm Bear vault?

**Short answer:** Yes, but as a *layered* deployment — NOT as primary methodology, but as a **behavioral overlay** on top of other pilots (cc-sdd / codex-plugin-cc / free-claude-code).

**Pilot priority:** **#3.5 / Tier-2** (after cc-sdd v61 / codex-plugin-cc v62 / free-claude-code v60). Reason: the 4 principles change *how* the AI behaves but do NOT add new workflow phases (like cc-sdd's spec → plan → tasks → impl).

**Deployment recommendation:** after Tier-1 pilots stabilize (Week 3+), install karpathy-skills in per-project mode (NOT per-vault — the 4 principles could interfere with routine v2.1 wiki-build workflow).

### When to use karpathy-skills?

✅ **Use when:** writing production code in a real monorepo + want AI to think before coding + hate overengineered solutions.

❌ **Don't use when:** running wiki-build routine v2.1 (would conflict with Phase 0 probe determinism) + prototyping fast (the 4 principles slow you down).

### Answer to "can it replace cc-sdd?"

**NO.** karpathy-skills + mattpocock-skills is **behavioral overlay + skills collection** — modifies HOW the AI thinks and adds narrow-task capabilities. cc-sdd is a **methodology workflow harness** — adds NEW workflow phases (spec/plan/tasks/impl + adversarial review). Different categories. The combo can complement cc-sdd as orthogonal layer; it CANNOT substitute.

---

## Cross-references

- **Pattern #52 N=2-N=3 strengthening:** mattpocock-skills v57 + codex-plugin-cc v62 + andrej-karpathy-skills v63
- **Pattern #19 a4 derivative-distillation:** NEW sub-type at v63
- **Pattern #18 Layer 2 multi-platform-single-skill-manual-sync:** NEW sub-axis at v63
- **Pattern #57 57c corpus-foundation-individual inheritance:** strengthening at v63
- **Storm Bear pilot ranking:** #3.5 Tier-2 NEW (post-v63 update)
