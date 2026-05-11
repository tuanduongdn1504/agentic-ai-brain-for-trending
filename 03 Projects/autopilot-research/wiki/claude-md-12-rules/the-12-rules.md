# The 12 rules — verbatim + author commentary

> Verbatim text from Mnilax's tweet thread (source: `raw/2026-05-11-claude-md-12-rules-mnilax.md`). Per `## Maintenance` in [[_index]], this article stays close to the original — extensions go to companion articles.

## Origin (3-author lineage)

| Step | Author | Date | Artifact | Stars/Reach |
|---|---|---|---|---|
| 1 | Andrej Karpathy | Jan 2026 | X.com thread complaining about Claude code-writing failure modes: silent wrong assumptions, over-complication, orthogonal damage | (thread) |
| 2 | Forrest Chang | Late Jan 2026 | Packaged complaints → 4 behavioral rules → CLAUDE.md → GitHub repo `forrestchang/andrej-karpathy-skills` | 5,828 stars day 1 / 60K bookmarks 2 weeks / 120K stars at time of Mnilax post |
| 3 | Mnilax | ~May 2026 | Tested Forrest's 4 rules on 30 codebases for 6 weeks → added 8 rules for May-2026-era failure modes (agent fights, hook cascades, skill loading, multi-step workflows) | (article) |

## Karpathy's 4 (the floor)

**Rule 1 — Think Before Coding.** No silent assumptions. State what you're assuming. Surface tradeoffs. Ask before guessing. Push back when a simpler approach exists.

**Rule 2 — Simplicity First.** Minimum code that solves the problem. No speculative features. No abstractions for single-use code. If a senior engineer would call it overcomplicated — simplify.

**Rule 3 — Surgical Changes.** Touch only what you must. Don't "improve" adjacent code, comments, or formatting. Don't refactor what isn't broken. Match existing style.

**Rule 4 — Goal-Driven Execution.** Define success criteria. Loop until verified. Don't tell Claude what steps to follow, tell it what success looks like and let it iterate.

Author's empirical claim: these 4 close **~40% of failure modes** in unsupervised Claude Code sessions.

## Mnilax's 8 additions (with the "moment" that justified each)

### Rule 5 — Use the model only for judgment calls

```text
Use Claude for: classification, drafting, summarization, extraction from unstructured text.
Do NOT use Claude for: routing, retries, status-code handling, deterministic transforms.
If a status code already answers the question, plain code answers the question.
```

**The moment:** Code that called Claude to "decide if we should retry on 503" worked beautifully for 2 weeks, then started flaking because the model started reading the request body as context for the decision. Retry policy became random because the prompt was random.

### Rule 6 — Token budgets are not advisory

```text
Per-task budget: 4,000 tokens.
Per-session budget: 30,000 tokens.
If a task is approaching budget, summarize and start fresh. Do not push through.
Surfacing the breach > silently overrunning.
```

**The moment:** A debugging session ran 90 minutes. Model iterated on the same 8KB error message, gradually losing track of which fixes it had tried. Suggested fixes that had been rejected 40 messages earlier. Token budget would have killed it at minute 12.

### Rule 7 — Surface conflicts, don't average them

```text
If two existing patterns in the codebase contradict, don't blend them.
Pick one (the more recent / more tested), explain why, and flag the other for cleanup.
"Average" code that satisfies both rules is the worst code.
```

**The moment:** Codebase had 2 error-handling patterns (async/await try/catch + global error boundary). Claude wrote new code that did BOTH. Errors were swallowed twice. 30 min to figure out why.

### Rule 8 — Read before you write

```text
Before adding code in a file, read the file's exports, the immediate caller, and any obvious shared utilities.
If you don't understand why existing code is structured the way it is, ask before adding to it.
"Looks orthogonal to me" is the most dangerous phrase in this codebase.
```

**The moment:** Claude added a function next to an existing identical function it hadn't read. New one took precedence via import order. Old one had been source of truth for 6 months.

### Rule 9 — Tests verify intent, not just behavior

```text
Every test must encode WHY the behavior matters, not just WHAT it does.
A test like `expect(getUserName()).toBe('John')` is worthless if the function takes a hardcoded ID.
If you can't write a test that would fail when business logic changes, the function is wrong.
```

**The moment:** Claude wrote 12 tests for an auth function. All passed. Auth was broken in production. Tests verified function returned something, not whether it returned the right thing.

### Rule 10 — Checkpoint after every significant step

```text
After completing each step in a multi-step task: summarize what was done, what's verified, what's left.
Don't continue from a state you can't describe back to me.
If you lose track, stop and restate.
```

**The moment:** 6-step refactor went wrong on step 4. Claude did steps 5 and 6 on top of the broken state. Untangling took longer than redoing whole thing.

### Rule 11 — Match the codebase's conventions, even if you disagree

```text
If the codebase uses snake_case and you'd prefer camelCase: snake_case.
If the codebase uses class-based components and you'd prefer hooks: class-based.
Disagreement is a separate conversation. Inside the codebase, conformance > taste.
If you genuinely think the convention is harmful, surface it. Don't fork it silently.
```

**The moment:** Claude introduced React hooks into a class-component codebase. They worked. They also broke the codebase's testing patterns that assumed `componentDidMount`. Half a day to remove and rewrite.

### Rule 12 — Fail loud

```text
If you can't be sure something worked, say so explicitly.
"Migration completed" is wrong if 30 records were skipped silently.
"Tests pass" is wrong if you skipped any.
"Feature works" is wrong if you didn't verify the edge case I asked about.
Default to surfacing uncertainty, not hiding it.
```

**The moment:** Claude said a database migration "completed successfully." It had silently skipped 14% of records that hit constraint violations. Skip was logged but not surfaced. Problem discovered 11 days later.

## The numbers (author's empirical claim)

50 tasks × 30 codebases × 6 weeks across 3 configurations:

| Config | Mistake rate | Compliance |
|---|---|---|
| No CLAUDE.md | **41%** | n/a |
| Karpathy's 4 rules | ~10-11% (implied) | **78%** |
| Mnilax 12 rules | **3%** | **76%** |

Key insight per Mnilax: "going from 4 rules to 12 added almost no compliance overhead (78% → 76%) but cut the mistake rate by another 8 points. The new rules cover failure modes the original 4 didn't address — they don't compete for the same attention budget."

### Falsifier check

The 41% → 3% claim is single-author, self-tested. Independent verification belongs here when it emerges. Marker: ⚠️ **NOT INDEPENDENTLY CORROBORATED** as of 2026-05-11.

When future ingests touch this claim:
1. Independent benchmark replicating the methodology → append `### Replication YYYY-MM-DD` to this section
2. Counter-evidence (rules tested, smaller-than-claimed effect) → append `### Counter-evidence YYYY-MM-DD`
3. Methodology critiques (50 tasks not representative, etc.) → flag in `## Limitations`

## Where Karpathy's 4 silently break (Mnilax's diagnosis)

1. **Long-running agent tasks** — Karpathy's 4 target the moment of code-writing. Silent on multi-step pipelines. No budget rule (→ Rule 6), no checkpoint rule (→ Rule 10), no fail-loud rule (→ Rule 12). Pipelines drift.
2. **Multi-codebase consistency** — "Match existing style" assumes one style. Monorepos with 12 services force Claude to pick. Originals don't say how. Picks randomly or averages. (→ Rule 11)
3. **Test quality** — Goal-Driven Execution treats "tests pass" as success. Doesn't say tests must be meaningful. Result: tests that test nothing useful but make Claude confident. (→ Rule 9)
4. **Production vs prototype** — The same 4 rules that protect production code from over-engineering slow down prototypes that legitimately need 100 lines of speculative scaffolding. Karpathy's Simplicity First overfires on early-stage code.

## What Mnilax tried but rejected

- Adding Reddit/X rules — most were restatements of Karpathy's 4 in different words, or domain-specific ("always use Tailwind") that don't generalize
- More than 12 rules — tested up to 18. Compliance dropped 76% → 52% past 14 rules. The 200-line CLAUDE.md ceiling is real
- Tooling-dependent rules — "Always use eslint" breaks when eslint isn't installed; fails silently. Replaced with capability-agnostic phrasings
- Examples instead of rules — 3 examples cost ~10 rules of context; Claude over-fits. Rules abstract, examples specific → use rules
- "Be careful" / "think hard" / "really focus" — pure noise, ~30% compliance because not testable. Replaced with concrete imperatives
- "Be senior" identity prompts — don't work. Claude already thinks it's senior. Compliance gap is thinking vs doing; imperatives close gap, identity prompts don't

## The mental model (author's framing)

> "CLAUDE.md is not a wishlist. It's a behavioral contract that closes specific failure modes you've observed. Every rule should answer: what mistake does this prevent?"

> "Your mileage will vary. If you don't run multi-step pipelines, Rule 10 doesn't matter. If your codebase has one consistent style enforced by linting, Rule 11 is redundant. Read the 12, keep the ones that map to mistakes you've actually made, drop the rest. A 6-rule CLAUDE.md tuned to your real failure modes beats a 12-rule one with 6 rules you'll never need."

## Key Takeaways

- **Behavioral contract, not wishlist** — every rule must prevent a specific observed mistake
- **200-line compliance ceiling** is real and measured — past it, Claude pattern-matches without reading
- **Conditional adoption** — drop rules that don't match your real failure modes; 6 well-fit beats 12 generic
- **Concrete imperatives > identity prompts** — "state assumptions explicitly" beats "be careful"
- **Rules ≠ examples** — examples cost more context and cause over-fitting
- **Compliance does NOT degrade linearly with rule count up to ~12-14** — adding orthogonal rules is nearly free if each addresses a distinct failure mode
- **Self-reported empirical numbers** (41% → 3%) need independent verification — flagged for falsifier check
