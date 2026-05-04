# (C) CLAUDE.md Summary — gstack Development Conventions

> **Source:** `00 Sources/gstack/CLAUDE.md` (503 lines, ~20KB)
> **Ingested:** 2026-04-18
> **Coverage:** Full file
> **Routine context:** Source #2 of 3 cho gstack project (Phase 2)

---

## TL;DR

**VI:** CLAUDE.md của gstack dày 503 dòng — nhiều hơn ECC + Superpowers CLAUDE.md cộng lại. Đây là **development guide + dev culture + voice protection + code quality philosophy** in one file. Nội dung nổi bật: (1) **Slop-scan philosophy** — "AI code quality, not AI code hiding"; (2) **AI effort compression table** (3x-100x); (3) **Search before building** + Three Layers of Knowledge (Layer 3 = first-principles, prized highest); (4) **Voice protection** cho 3 hard-gates không contributor được đụng (ETHOS.md, promotional material, Garry's voice); (5) **E2E eval failure blame protocol** — cấm claim "pre-existing" without proof.

**EN:** gstack's CLAUDE.md is 503 lines (more than ECC+Superpowers combined). It's dev guide + culture + voice protection + code quality philosophy all-in-one.

---

## Build system overview

**Bun-based** (not Node.js). 20+ bun scripts cho testing, eval, building:

```bash
bun install              # deps
bun test                 # free tests <2s
bun run test:evals       # paid LLM-judge + E2E, diff-based, ~$4/run max
bun run test:e2e         # E2E only, ~$3.85/run max
bun run slop             # full slop-scan report
bun run slop:diff        # slop findings on changed files only
bun run build            # gen docs + compile binaries
bun run skill:check      # health dashboard
bun run dev:skill        # watch mode
bun run eval:select      # preview which E2E tests would run
```

**Key insight:** gstack has **paid test tiers** (~$4/run). Eval-driven like Superpowers nhưng explicit cost model.

### Two-tier E2E testing

- `gate` tier — CI default, blocks merge (safety guardrails, deterministic)
- `periodic` tier — weekly cron/manual (quality benchmarks, Opus model tests, Codex/Gemini integration)

→ **More rigorous than ECC** (free tests only). **Comparable to Superpowers** but with explicit cost discipline.

### Diff-based test selection

E2E tests auto-select based on `git diff` against base branch. Each test declares file dependencies trong `test/helpers/touchfiles.ts`. Changes to global touchfiles trigger all tests.

→ **Optimization:** giảm CI cost bằng selective testing. Pattern reusable cho Storm Bear nếu vault tests expensive.

---

## Slop-scan philosophy (DISTINCTIVE)

gstack uses [slop-scan](https://github.com/benvinegar/slop-scan) — tool catch patterns AI-generated code genuinely worse than human.

**Framing quote:**
> "We are NOT trying to pass as human code. We are AI-coded and proud of it. The goal is code quality."

→ **Anti-pattern embraced:** don't hide AI origin. Optimize code quality regardless of origin.

### What to fix (genuine quality)

- Empty catches around file ops → use `safeUnlink()` (ignores ENOENT, rethrows EPERM/EIO)
- Empty catches around process kills → use `safeKill()` (ignores ESRCH, rethrows EPERM)
- Redundant `return await` (remove when no try block)
- Typed exception catches vs bare `catch {}`

### What NOT to fix (linter gaming)

- String-matching error messages (brittle — Playwright/Chrome can change wording)
- Adding comments to trip slop-scan's exemption (noise, not documentation)
- Converting extension catch-and-log to selective rethrow (extensions crash entirely on uncaught)
- Tightening best-effort cleanup paths (shutdown should use `safeUnlinkQuiet` swallowing all)

### Utilities library

`browse/src/error-handling.ts` exports:
| Function | Use when | Behavior |
|----------|----------|----------|
| `safeUnlink(path)` | Normal deletion | Ignores ENOENT, rethrows others |
| `safeUnlinkQuiet(path)` | Shutdown/emergency | Swallows all errors |
| `safeKill(pid, signal)` | Sending signals | Ignores ESRCH, rethrows others |
| `isProcessAlive(pid)` | Boolean checks | Returns true/false, never throws |

**Score tracking:** Baseline 2026-04-09 = 100 findings / 432.8 score / 2.38 score/file. After cleanup: 90 / 358.1 / 1.96. **"Don't chase the number. Fix patterns that represent actual code quality problems."**

→ **Pattern generalizable:** Storm Bear có thể adopt slop-scan cho project mới nếu ship code. Principle = optimize quality, không hide AI origin.

---

## AI effort compression table (DISTINCTIVE — repeats ETHOS)

| Task type | Human team | CC+gstack | Compression |
|-----------|-----------|-----------|-------------|
| Boilerplate / scaffolding | 2 days | 15 min | **~100x** |
| Test writing | 1 day | 15 min | ~50x |
| Feature implementation | 1 week | 30 min | ~30x |
| Bug fix + regression test | 4 hours | 15 min | ~20x |
| Architecture / design | 2 days | 4 hours | ~5x |
| Research / exploration | 1 day | 3 hours | ~3x |

**Use:** "Always show both human-team and CC+gstack time when estimating."

> "Completeness is cheap. Don't recommend shortcuts when complete implementation is a 'lake' (achievable) not an 'ocean' (multi-quarter migration)."

→ **Mental model shift:** Traditional estimates assume human-time. gstack ask agent reframe theo AI-assisted time → different trade-off calculus.

---

## Search before building (ETHOS-linked)

> "Before designing any solution involving concurrency, unfamiliar patterns, infrastructure, or anything where the runtime/framework might have a built-in:
> 1. Search for '{runtime} {thing} built-in'
> 2. Search for '{thing} best practice {current year}'
> 3. Check official runtime/framework docs"

### Three Layers of Knowledge

- **Layer 1: Tried-and-true** — standard patterns. Risk: assume obvious answer is right.
- **Layer 2: New-and-popular** — current best practices. Risk: mania/crowd wrong.
- **Layer 3: First-principles** — original reasoning. **Prized above all.**

> "The best projects both avoid mistakes (Layer 1) while making brilliant observations that are out of distribution (Layer 3)."

→ **Match Karpathy's mentality.** Also match Storm Bear vault's "don't re-derive knowledge from scratch — search existing wiki first."

---

## Voice protection (3 HARD-GATES)

**Community PR guardrails — always AskUserQuestion before accepting PR that:**

1. **Touches ETHOS.md** — Garry's personal builder philosophy. No edits from external contributors or AI agents, period.
2. **Removes or softens promotional material** — YC references, founder perspective, product voice are intentional. PRs framing as "unnecessary" or "too promotional" → REJECT.
3. **Changes Garry's voice** — tone, humor, directness in skill templates, CHANGELOG, docs are not generic. PRs rewriting voice to be "neutral" or "professional" → REJECT.

> "Even if the agent strongly believes a change improves the project, these three categories require explicit user approval via AskUserQuestion. No exceptions. No auto-merging. No 'I'll just clean this up.'"

→ **Analogy:** Superpowers "carefully-tuned content" warning + "your human partner" terminology protection. Both frameworks protect voice from AI-agent-driven homogenization.

---

## Platform-agnostic design

> "Skills must NEVER hardcode framework-specific commands, file patterns, or directory structures. Instead:
> 1. Read CLAUDE.md for project-specific config
> 2. If missing, AskUserQuestion — let user tell you
> 3. Persist the answer to CLAUDE.md so we never have to ask again"

→ **Pattern:** Skills ask + persist config trong CLAUDE.md. Storm Bear vault đã làm tương tự (project CLAUDE.md chứa conventions).

---

## SKILL.md workflow (template-generated)

SKILL.md files are **generated** from `.tmpl` templates (not hand-written!):

1. Edit `.tmpl` file
2. Run `bun run gen:skill-docs` (or `bun run build`)
3. Commit both `.tmpl` + generated `.md`

**Token ceiling:** Generated SKILL.md must stay <100KB (~25K tokens). `gen-skill-docs` warns if exceeded.

**Merge conflicts:** NEVER resolve on generated SKILL.md directly — resolve on `.tmpl` + `scripts/gen-skill-docs.ts`, regenerate, stage regenerated files.

→ **Pattern:** Source-of-truth separation (template vs generated artifact). ECC + Superpowers don't have this — skills hand-authored.

---

## Writing SKILL templates (prompt-as-code)

> "SKILL.md.tmpl files are **prompt templates read by Claude**, not bash scripts. Each bash code block runs in a separate shell — variables do not persist between blocks."

**Rules:**
- Use natural language for logic and state (không shell variables)
- Don't hardcode branch names (detect main/master dynamically)
- Keep bash blocks self-contained
- Express conditionals as English ("1. If X, do Y. 2. Otherwise, Z.")

→ **Pattern name:** "Prompt-as-code architecture." Treat prompts as primary artifact, bash blocks as illustrations.

---

## E2E eval failure blame protocol (ANTI-SLOP PATTERN)

> "When an E2E eval fails during `/ship` or any other workflow, **never claim 'not related to our changes' without proving it.**"

**Required before attributing failure to "pre-existing":**
1. Run same eval on main/base branch, show it fails there
2. If passes on main but fails on branch → **IT IS YOUR CHANGE.** Trace the blame.
3. If can't run on main, say "unverified — may or may not be related" + flag as risk in PR body

> "'Pre-existing' without receipts is a lazy claim. Prove it or don't say it."

→ **Anti-pattern detection table** like Superpowers's 11 rationalizations. gstack instance: blame-pre-existing-without-proof.

---

## Long-running tasks discipline

> "When running evals, E2E tests, or any long-running background task, **poll until completion**. Use `sleep 180 && echo 'ready'` + `TaskOutput` in a loop every 3 minutes. **Never switch to blocking mode and give up when poll times out. Never say 'I'll be notified when it completes' and stop checking.**"

**Full E2E suite:** 30-45 minutes = 10-15 polling cycles. Do all of them.

→ **Match Superpowers autonomous-continuation discipline.** Both frameworks explicit about not-giving-up on long tasks.

---

## Commit style — "Always bisect commits"

> "Every commit should be a single logical change. When you've made multiple changes (e.g., rename + rewrite + new tests), split them into separate commits before pushing."

**Examples of good bisection:**
- Rename/move separate from behavior changes
- Test infrastructure separate from test implementations
- Template changes separate from generated file regeneration
- Mechanical refactors separate from new features

→ **Match git-worktree + single-task principle từ Superpowers.** Both frameworks enforce commit discipline.

---

## Compiled binaries warning

`browse/dist/` và `design/dist/` track binaries ~58MB mỗi cái, Mach-O arm64 only (don't work on Linux/Windows/Intel Mac). Tracked qua historical mistake.

> "**NEVER stage or commit these files.** When staging files, always use specific filenames (`git add file1 file2`) — never `git add .` or `git add -A`."

→ **Match ECC + Superpowers warning:** avoid `git add -A` / bulk staging (accidentally commits secrets/binaries).

---

## CHANGELOG style (user-facing)

> "CHANGELOG.md is **for users**, not contributors. Write it like product release notes:
> - Lead with what user can **do** that they couldn't before
> - Plain language: 'You can now...' not 'Refactored the...'
> - Never mention TODOS.md, internal tracking, eval infrastructure
> - Put contributor changes in separate 'For contributors' section at bottom
> - Every entry should make someone think 'oh nice, I want to try that.'"

→ **Distinctive discipline.** ECC + Superpowers don't have explicit CHANGELOG style. gstack treats it as marketing surface.

---

## Distinctive patterns (cho vault reference)

### Pattern 1: Prompt-as-code architecture

Skills = generated Markdown from `.tmpl` templates. Source of truth = template. Pattern reusable nếu Storm Bear build skill-generator tool.

### Pattern 2: Paid test tiers with cost discipline

`~$4/run max` explicit. Two-tier system (gate/periodic). Diff-based selection. Pattern if Storm Bear ever integrates paid LLM evals.

### Pattern 3: Slop-scan embracing AI origin

"AI-coded and proud of it." Don't hide, optimize quality. Anti-pattern vs trying to look human.

### Pattern 4: Voice protection hard-gates

3 categories (ETHOS, promotional, tone) always require AskUserQuestion. Match Superpowers's "your human partner" protection.

### Pattern 5: Blame-with-receipts

"Pre-existing without receipts is lazy." Claim = proof required. Anti-pattern framing.

---

## Open questions resolved

- ✅ Q9: License MIT contribution policy — strict voice + ETHOS protection, community PR triage built-in
- ✅ Q6: Slop scanner detect anti-patterns list — see "What to fix / What NOT to fix" above

## Open questions raised

- ⏸ Eval cost management — `$4/run max` on test:evals. Track actual spend qua time?
- ⏸ `gen-skill-docs.ts` implementation — reusable cho Storm Bear skill-from-template pattern?
- ⏸ OpenClaw integration depth — skills có thể publish via ClawHub, cross-ecosystem reach

---

## Cross-references

- [[(C) README summary]] — overview + 23 specialists
- [[(C) ETHOS + ARCHITECTURE summary]] — philosophy detail
- [[(C) index]]
- [[(C) log]]
- Cross-project: `../../Superpowers - Beginner Analysis/02 Wiki/(C) Philosophy and Contribution Culture summary.md` — voice protection analog

## Citations

- `00 Sources/gstack/CLAUDE.md` (full, 503 lines)
- Slop-scan section: lines ~320-380
- Voice protection: lines ~420-445
- AI effort compression: lines ~170-185 (also in ETHOS.md)
