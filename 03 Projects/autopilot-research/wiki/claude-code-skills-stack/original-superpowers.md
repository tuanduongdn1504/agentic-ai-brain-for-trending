# Original Deep-Dive: Superpowers (obra/superpowers)

## Source

- Repo: [github.com/obra/superpowers](https://github.com/obra/superpowers) — author **Jesse Vincent** (GitHub `@obra`, Prime Radiant; also Request Tracker / Keyboardio / VaccinateCA).
- Verified (`gh api`, 2026-06-29): **240,869★**, 21,388 forks, **MIT**, primary language **Shell** (then JavaScript/TypeScript), created **2025-10-09**, actively pushed (2026-06-25), not archived.
- Plugin marketplace: `claude-plugins-official`.

## What it is

An agentic **skills framework + software-development methodology** for Claude Code (and 10+ other agents: Cursor, Codex, Gemini CLI, Copilot CLI, OpenCode, Kimi, etc.), distributed as a plugin. It packages composable skills and a meta-skill (`using-superpowers`) that detects intent and routes to the right sub-skill.

## How it actually works (7-stage pipeline — verified order)

1. **brainstorming** — activates *before* code; forces spec clarification with questions, explores alternatives, presents design sections for sign-off.
2. **using-git-worktrees** — isolates work on a branch with a clean test baseline.
3. **writing-plans** — decomposes the feature into bite-size (2–5 min) tasks with exact file paths, code stubs, and verification steps.
4. **subagent-driven-development** — dispatches a *fresh subagent per task* with two-stage review (spec-compliance, then code quality).
5. **test-driven-development** — classic red-green-refactor.
6. **requesting-code-review** — gates progress between tasks on critical issues.
7. **finishing-a-development-branch** — verifies all tests pass; offers merge or PR.

Also ships **`dispatching-parallel-agents`** (concurrent subagent workflows) — the "parallel agents" Eric demos.

## ⚠️ Corrections vs the video / draft

- **Pipeline order:** the video frames it as "brainstorm → plan → **write tests first** → execute". The repo's actual order runs **TDD *during* execution** (step 5), not before it; code review happens *between* tasks. The *philosophy* is "write tests first, always" — but mechanically tests are written inside the execution loop, per task. (Verdict: PARTIAL.)
- **"Markdown-based":** a draft claimed the core is Markdown. **REFUTED** — the codebase is **Shell 51.6% / JavaScript 41.3%** + TS; Markdown is documentation, not the implementation.
- **v6.0 (June 2026):** rewrote the review process for **~50% fewer tokens** + ~2× speed — CONFIRMED in release notes. (Eric's April-2026 video predates v6.0, so he likely demoed an earlier version.)

## Operator relevance

- **hireui Goal #2:** the strongest free TDD harness to bring to a real codebase — directly comparable to the **cc-sdd** pilot already ranked in the vault (architectural role-separation vs Superpowers' skill-routing).
- **Scrum coaching:** the 2–5-min task slicing + spec-first + definition-of-done gating are teachable Agile primitives, agent-enforced.
- **Storm Bear Pattern Library:** strong evidence for Pattern #21 (SDD Methodology Emergence) and Pattern #76 (Adversarial Subagent Review) — the two-stage per-task review is a textbook #76 instance.

## Install safety

Clean: MIT, no postinstall, installed via the official Claude plugin marketplace; reputable author. Token cost: a plugin loads only skill name+description until triggered (progressive disclosure), so baseline overhead is modest; v6.0 cut it further.

## Open questions

- Exact version Eric ran (pre-v6.0).
- Community `superpowers-marketplace` parity vs the official plugin.

## Key Takeaways

- Real, enormous (240.9K★), MIT, by a well-known engineer — the safest "foundation" pick in the stack.
- It's **Shell/JS**, and TDD runs *inside* execution — get the mechanism right when teaching/adopting it.
- Best read as the operator's reference SDD harness alongside cc-sdd and G-Stack.

## Related

[[claude-code-skills-stack/original-sdd-frameworks-gsd-gstack]] · [[claude-code-skills-stack/original-skill-creator]] · [[harness-engineering/_index]] · [[multi-agent-orchestration/_index]] · [[claude-api-cost-optimization/_index]]
