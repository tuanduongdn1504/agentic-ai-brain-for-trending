# (C) Open Questions — Superpowers Wiki

> Tracking questions raised during ingest. Resolve qua các source ingest sau, hoặc carry over thành TODO.
> Format: ⏸ open / 🟡 partial / ✅ resolved / ❌ rejected

---

## Câu hỏi hiện tại / Current open questions

### Pre-ingest (từ initial survey only — chưa đọc README)

1. ⏸ **GitHub stars count** — chưa verify (peek webfetch ghi "available via Claude's official plugin marketplace" nhưng không có số stars). **→ verify khi ingest README + check via API.**
2. ⏸ **Distribution model so với ECC** — Superpowers có `.claude-plugin/`, `.codex/`, `.cursor-plugin/`, `.opencode/`, `.gemini/` per-folder. ECC dùng plugin centralized. Khác biệt fundamental? **→ ingest README + plugin manifests.**
3. ⏸ **7-stage workflow exact stages** — webfetch ghi "brainstorming through branch completion" nhưng không liệt kê 7 stages cụ thể. **→ ingest README + docs/.**
4. ⏸ **Skills count + categorization** — folder `skills/` có 16 entries (ls -la trên). ECC có 185. Quality vs quantity philosophy? **→ enumerate Phase 3.**
5. ⏸ **TDD enforcement implementation** — built-in vs ECC's skill-based approach. Cơ chế cụ thể là gì? **→ đọc TDD-related files.**
6. ⏸ **Subagent count** — folder `agents/` có 3 entries (ls trên). ECC có 48. Different design philosophy? **→ verify Phase 3.**
7. ⏸ **Claude marketplace listing** — webfetch ghi "available via Claude's official plugin marketplace". URL? Listing identifier? **→ check `.claude-plugin/`.**
8. ⏸ **Author Jesse Vincent (obra) background** — context giúp đánh giá design decisions. **→ google + ingest README intro.**
9. ⏸ **RELEASE-NOTES.md 58KB** — large file, có thể chứa changelog đầy đủ. Strategy: skim headings, focused read latest 2-3 versions. **→ Phase 2.**
10. ⏸ **Comparison axis với ECC** — 11 axis identified trong CLAUDE.md table. Mỗi axis cần data thật để fill. **→ track suốt Phase 2-3.**

---

## Câu hỏi đã giải / Resolved

_Chưa có. Ingest đầu tiên sẽ resolve một số._

---

## Câu hỏi tự nhiên / Self-resolved (insights phát hiện không cần ask)

_Chưa có._

---

## Notes về comparison philosophy

> Đây là project KHÔNG chỉ analyze Superpowers, mà cũng phải compare với ECC. Lưu ý:

- **Tránh bias** — đừng treat ECC như benchmark "đúng". Mỗi tool có philosophy riêng.
- **Track design decisions** — khi tools khác nhau ở 1 axis, hỏi "vì sao?" thay vì "cái nào tốt hơn?"
- **Use case-based comparison** — kết quả comparison guide nên là "When to choose X vs Y" thay vì "X is better"
- **Honest about gaps** — nếu chỉ ingest 1/2 sources và compare, mark explicit "based on partial knowledge"

---

## Cross-references

- [[../02 Wiki/(C) index]]
- [[../02 Wiki/(C) log]]
- ECC sister project open questions: `03 Projects/Everything Claude Code - Beginner Analysis/01 Analysis/(C) README - open questions.md`
