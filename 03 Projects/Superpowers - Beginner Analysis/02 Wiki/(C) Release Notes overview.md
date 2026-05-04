# (C) Release Notes Overview

> **Source:** `00 Sources/superpowers/RELEASE-NOTES.md` (58KB)
> **Ingested:** 2026-04-18
> **Coverage:** Headings full + read 5 latest versions (v5.0.0 → v5.0.7) detail
> **Strategy:** Skim-first per skill `llm-wiki-ingest` recommendation cho file >20KB

---

## TL;DR

**VI:** Superpowers active development — **27+ versions** từ launch (Oct 2025 per blog) đến hiện tại v5.0.7 (2026-03-31). Phát triển nhanh: 5 versions trong tháng 3/2026. Recent themes: **multi-harness expansion** (Copilot CLI, Cursor, Gemini, OpenCode, Codex App), **review loop optimization** (replaced subagent dispatch với inline self-review = save ~25 phút overhead), **zero-dependency push** (loại Express/Chokidar/WebSocket vendored deps).

**EN:** Superpowers under active development — **27+ versions** from launch (Oct 2025) to v5.0.7 (2026-03-31). Fast cadence: 5 versions in March 2026. Recent themes: multi-harness expansion, review loop optimization (replaced subagent dispatch with inline self-review = ~25 min overhead saved), zero-dependency push.

---

## Version timeline (skimmed headings)

**v5.x line — multi-harness expansion + review optimization**

| Version | Date | Theme |
|---------|------|-------|
| v5.0.7 | 2026-03-31 | GitHub Copilot CLI Support |
| v5.0.6 | 2026-03-24 | Inline Self-Review Replaces Subagent Review Loops |
| v5.0.5 | 2026-03-17 | Bug fixes (Brainstorm server, Windows) |
| v5.0.4 | 2026-03-16 | Review Loop Refinements (single whole-plan, raised bar) |
| v5.0.3 | 2026-03-15 | Cursor Support |
| v5.0.2 | 2026-03-11 | Zero-Dependency Brainstorm Server |
| v5.0.1 | 2026-03-10 | Agentskills Compliance, Gemini CLI Extension |
| **v5.0.0** | **2026-03-09** | **Breaking: subagent-driven mandatory, batching removed, slash commands deprecated** |
| v4.3.1 | 2026-02-21 | (skim) |
| v4.3.0 | 2026-02-12 | (skim) |
| v4.2.0 | 2026-02-05 | (skim) |
| v4.1.x | 2026-01-23 | (skim) |
| v4.0.x | 2025-12 | (skim) |
| v3.x | 2025-10 → 2025-12 | Initial public versions |

→ ~6 months tuổi, 27+ releases. **Active maintenance.**

---

## Major themes từ recent versions

### Theme 1: Multi-harness expansion

Mỗi version recent thêm support cho 1 harness mới:
- v5.0.7: GitHub Copilot CLI
- v5.0.5 + v5.0.4: OpenCode improvements
- v5.0.3: Cursor support (hooks-cursor.json)
- v5.0.1: Gemini CLI extension
- v5.0.6: Codex App compatibility design spec

→ **Strategy:** Cross-harness portability là priority. ECC mention 5 harnesses; Superpowers actively shipping support cho 7.

### Theme 2: Review loop optimization (significant insight)

**v5.0.6 lesson đáng học:**

> "The subagent review loop (dispatching a fresh agent to review plans/specs) doubled execution time (~25 min overhead) without measurably improving plan quality. Regression testing across 5 versions with 5 trials each showed identical quality scores regardless of whether the review loop ran."

**Action:** Replaced subagent review loops với **inline Self-Review checklists** (placeholder scan, internal consistency, scope check, ambiguity check). 

**Result:** "Self-review catches 3-5 real bugs per run in ~30s instead of ~25 min, with comparable defect rates."

→ **Lesson generalizable:** không phải mọi pattern phức tạp đều worth complexity. **Measure quality, không assume.**

### Theme 3: Zero-dependency push

**v5.0.2 milestone:**

> "Removed all vendored node_modules — server.js is now fully self-contained. Replaced Express/Chokidar/WebSocket dependencies với zero-dependency Node.js server using built-in `http`, `fs`, `crypto`."

→ Loại ~1,200 lines vendored deps. Custom WebSocket protocol implementation (RFC 6455).

**Match contributor culture từ CLAUDE.md:** "Superpowers is a zero-dependency plugin by design."

### Theme 4: Breaking change discipline (v5.0.0)

v5.0.0 (2026-03-09) là **major breaking release**:

1. **Subagent-driven development MANDATORY** trên capable harnesses (Claude Code, Codex). Removed user choice.
2. **Executing-plans no longer batches** — removed "execute 3 tasks then stop" pattern. Continuous execution, stop only on blockers.
3. **Slash commands deprecated** (`/brainstorm`, `/write-plan`, `/execute-plan`) — point to skills.
4. **Specs/plans directory restructured** — `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`

→ Willing to break backward compat cho cleaner architecture. ECC has similar pattern (commands→skills migration).

### Theme 5: Architecture guidance integrated across skills

v5.0.0 added:

> "Design-for-isolation và file-size-awareness guidance added to brainstorming, writing-plans, và subagent-driven-development:
> - Brainstorming: 'Design for isolation and clarity' + 'Working in existing codebases'
> - Writing-plans: 'File Structure' + 'Scope Check' backstop
> - SDD implementer: 'Code Organization' + 'When You're in Over Your Head'"

→ Architecture concerns không siloed in 1 skill — woven through skill pipeline.

---

## Distinctive patterns observed across versions

### Pattern 1: Subagent context isolation principle

v5.0.2 introduced cross-skill: "All delegation skills (brainstorming, dispatching-parallel-agents, requesting-code-review, subagent-driven-development, writing-plans) now include context isolation principle. Subagents receive only the context they need, preventing context window pollution."

→ Match ECC's "Iterative Retrieval Pattern" (sub-agent context problem). **Convergent solution.**

### Pattern 2: Implementer status protocol

v5.0.0 SDD added: "Subagents now report DONE, DONE_WITH_CONCERNS, BLOCKED, or NEEDS_CONTEXT. Controller handles each status appropriately: re-dispatching with more context, upgrading model capability, breaking tasks apart, or escalating to human."

→ Structured status codes hơn ECC's free-form summary. Worth adopting.

### Pattern 3: Instruction priority hierarchy explicit

v5.0.0:

> 1. User's explicit instructions (CLAUDE.md, AGENTS.md, direct requests) — highest
> 2. Superpowers skills — override default system behavior
> 3. Default system prompt — lowest

→ Match ECC's "system prompt > user > tool result" claim từ longform guide. **Different hierarchy levels, both explicit.**

### Pattern 4: Eval-driven changes

Multiple versions reference "regression testing across 5 versions với 5 trials each" — **eval evidence required cho behavior changes.**

→ Match contributor culture: "Skills are not prose — they are code that shapes agent behavior."

### Pattern 5: Active community contributions

v5.0.x credits: @karuturi, @mvanhorn, @daniel-graham, @arittr, @sarbojitrana, @lucasyhzlu-debug, @culinablaz, @吉田仁 — active community.

→ Despite 94% PR rejection rate, real contributors getting merged.

---

## Connection to ECC patterns (cross-project insights)

| Pattern | Superpowers | ECC | Convergence/Divergence |
|---------|-------------|-----|------------------------|
| Subagent context isolation | Cross-skill principle (v5.0.2) | "Iterative Retrieval Pattern" (longform) | **Convergent** — same problem, similar solution |
| Status protocol cho subagents | Structured (DONE/BLOCKED/etc.) | Free-form summaries | Superpowers more rigorous |
| Commands→Skills migration | v5.0.0 deprecation explicit | "Skills > Commands" (shortform) | **Convergent** |
| Cross-harness support | 7 harnesses explicit | 5+ harnesses | Both prioritize portability |
| Eval-driven skill changes | "5 versions × 5 trials" | "Verification loop" skill | **Convergent** but Superpowers more strict |
| Zero-dependency philosophy | Public stated | NOT enforced (ECC has separate paid products) | **Divergent** — different commercial model |

---

## Open questions từ ingest này

1. ⏸ **v3.x → v4.x → v5.x semver meanings** — what's a major version bump in Superpowers? Backward-compat policy explicit?
2. ⏸ **Eval methodology cụ thể** — "5 versions × 5 trials" mention. Full methodology documented? **→ đọc skill `writing-skills`.**
3. ⏸ **`docs/superpowers/specs/` + `docs/superpowers/plans/` populated chưa?** — có example designs/plans để reference không? **→ check folder.**
4. ⏸ **Brainstorm server architecture** — WebSocket-based visual companion. Cần thiết hay nice-to-have? Worth deeper dive nếu visual-heavy use case.
5. ⏸ **Performance metrics** — claim "~25 min overhead saved" trong v5.0.6. Repository có benchmark suite public?

---

## Cross-references

- [[(C) README summary]] — overview
- [[(C) Philosophy and Contribution Culture summary]] — eval discipline context
- [[(C) index]]
- [[(C) log]]

## Citations

- `RELEASE-NOTES.md`, lines 1–300 (read full v5.0.0 → v5.0.7)
- Lines 300+ skimmed via grep headings (45 versions total in file)
- v3.0 launch context: blog.fsck.com/2025/10/09/superpowers/ (referenced in README)
