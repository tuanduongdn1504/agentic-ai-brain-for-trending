# Docs-first, AI-second — the headline discipline

> The label "docs-first-AI-second" is ours; the position is Eric's, stated on camera (video #4, 13:06–13:34 + 22:14–22:46 + 44:30–52:25; video #3 restates it with a third reason).

## Source
- Video #4 tD0Uve-0Ltk, chapters "Lý do chọn Nestjs" (13:43), "Tài liệu Nestjs" (16:05), "Fix lỗi typescript" (43:00) — raw: `raw/2026-07-04-hoidanit-fullstack-vibe-coding.md`
- Video #3 osISSsyTJJ8 [00:33:04–00:35:15 + 01:02:41] — the series' most complete statement of the rule, now fully transcribed: `raw/2026-07-04-hoidanit-ep3-mvp-frontend.md`
- Verbatim anchor [00:13:06]: *"Bởi vì không phải cái gì AI nó cũng biết. AI thì nó phụ thuộc vào data, nó training."* — "AI doesn't know everything. AI depends on its data, its training."

## The rule as taught
- **Project initialization / setup / upgrades → official documentation, never AI.** Three stated reasons across eps 3–4:
  1. **Staleness:** AI output is bounded by training data; docs track the current release.
  2. **Cross-platform testing:** official install paths are tested on Windows/Mac/Linux; an AI-generated scaffold carries no such guarantee.
  3. **Token/cost efficiency** (ep 3): AI-driven init generates many files → high token cost for zero judgment value — scaffolding is a solved, deterministic task.
- **Error fixing → AI is welcome**, with discipline: paste the exact error, apply one suggestion, re-run, repeat. On camera the TypeScript failure took *multiple* AI iterations with partial/wrong fixes (baseUrl/dist detours) before the version-pin resolution — the instructor narrates this as normal: **"AI is helper, not oracle"; every suggestion is verified empirically by re-running.**
- **Upgrades → docs Migration section** (e.g., NestJS 11's Express-5 change), not AI summaries.
- Complement: **read docs at your project's version** (version dropdown), because real jobs maintain old versions — see [[version-pinning-discipline]].
- **Ep-3 nuance (full transcript):** docs-first is the *learning* rule; for the *cohort*, students download his frozen scaffold instead of re-running create-vite ("Download dự án init FE tại đây — KHÔNG tự coding phần này") — the demo teaches the thinking, the frozen artifact carries the course. See [[vite-react-init-workflow]].
- Scope boundary from ep 1: the human also owns **what to build** — "bây giờ các bạn muốn xây sản phẩm gì?"; product scope is never delegated to AI ([[beginner-pedagogy-model]]).

## Why this matters beyond beginners
- It's a clean, teachable **division of labor between docs and models**: deterministic, vendor-tested procedures (init/install/migrate) stay with docs; diagnostic judgment (error triage, fix candidates) goes to the model. Same altitude as Mnilax Rule 5 ("if code can answer, code answers") — here: *if docs can answer, docs answer*; cf. [[claude-md-12-rules/_index]].
- The token-cost reason independently rediscovers the cost-discipline lever documented in [[claude-api-cost-optimization/_index]] — from a beginner educator, arguing *don't spend model tokens on deterministic work*.
- The on-screen failure loop (AI partial fixes → re-run → next error) is a beginner-scale version of the verification discipline in [[how-we-claude-code/_index]]-style agent-native verify and [[jsm-practical-vibe-coding/_index]]'s "one problem, one fix, one verification".
- Inversion of most vibe-coding content: the demo where the AI *fails* repeatedly is kept in, as the lesson.

## Key Takeaways
- Rule: **scaffold from docs, debug with AI, verify every AI suggestion by running it.**
- Three stated rationales: docs are better-*tested*, fresher, and cheaper (tokens) for deterministic work — an argument from test coverage + cost, not AI skepticism.
- Kept-in failure footage is the pedagogy: beginners watch AI be partially wrong and see the recovery procedure.
- Transferable as a one-line harness constraint for agent work: "initialization and dependency changes follow official docs; cite the doc page in the diff."
