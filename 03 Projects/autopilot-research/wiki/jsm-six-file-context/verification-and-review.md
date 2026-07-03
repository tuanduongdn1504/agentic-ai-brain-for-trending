# Verification & review — CodeRabbit yes, tests no

> The methodology's weakest verified flank. Two adversarial verdicts anchor this page.

## VERIFIED: there is no test infrastructure

- `package.json` scripts: `dev`, `build`, `start`, `lint`, `postinstall` — **no test script**; no Jest/Vitest/Playwright/Cypress anywhere; zero test files in the tree (verifier: REFUTED the "verification discipline includes tests" reading).
- `code-standards.md` and `ai-workflow-rules.md` contain **no testing requirements** — the discipline is "verify end to end within defined scope," meaning *manually*.
- Contrast inside our corpus: Pocock's harness requires **tests + typecheck before every commit** ([[../pocock-real-feature-build/sandcastle-ralph-afk-loop]]); Anthropic's how-we-claude-code pillar is **agent-native verification** ([[../how-we-claude-code/_index]]). The six-file system has nothing equivalent — its gates are per-spec "Check When Done" bullets executed by a human.

## What verification actually looks like (on camera)

- `npm run build` per feature — TypeScript + ESLint as the only automated gate ("Build passes").
- Manual browser testing per feature: auth flows (sign-up, GitHub, redirects, sign-out), CRUD + slug generation, access control (incognito session → sign-in redirect; second account → access-denied page).
- Screenshot-driven design review: feed the agent a screenshot + markup ("make 50/50 left-right layout, fix fonts") — design feedback, not visual regression testing.
- The `current-issues.md` analyze-first pattern for stubborn bugs ([[feature-spec-workflow]]).

## CodeRabbit — two integration patterns (don't merge them into one "standard step")

Verifier verdict: the video demonstrates **two distinct review flows**, and `ai-workflow-rules.md` mandates **neither** (no CodeRabbit/PR/merge steps in the documented workflow):

1. **GitHub PR bot** (Feature 02): push to `development` → PR → *"CodeRabbit immediately hooked itself onto the PR"* → walkthrough summary + findings → fix → merge. Repo shows 8 PRs, merge-commit pattern.
2. **VS Code extension** (Features 04, 09, 17): review uncommitted changes inline in the editor, one-click apply fixes — no PR involved.

### What it caught (examples shown, consistent with CodeRabbit's documented capabilities — verified against docs)

- Accessibility: "Hide the off-screen sidebar from focus order and assistive tech when closed."
- Spec mismatch: sidebar prop present in implementation but missing from spec → spec refinement flagged.
- Validation edge case: name of only special characters passes truthy check → empty slug project.
- Type-only import used in value space; error handling where rename/delete close the dialog even when the API call failed ("a server error can look like a success").
- Review volume/specificity **increases** across the 28-feature arc (clipboard error handling → ref-mutation timing, double-commit on edge labels, Caps Lock handling for undo).

## Reading for our corpus

- CodeRabbit here is the **adversarial reviewer** role (Storm Bear Pattern #76 territory) implemented as SaaS: a third mechanism stratum next to cc-sdd's architectural role-separation and codex-plugin-cc's prompt-framing (both already in the Pattern Library).
- The review load-bearing insight: with agent-generated code, the review layer catches **spec gaps** as often as code bugs — reviews feed back into spec quality.

## Key Takeaways

- The six-file system ships **discipline without verification** — strong scoping rules, zero automated tests. Pair it with a test harness before trusting it for production work.
- "Check When Done" bullets are human-executed; they are a DoD checklist, not CI.
- CodeRabbit usage is real and effective in the video but **optional** in the documented methodology — a sponsor-shaped emphasis (CodeRabbit sponsors the video; see [[caveats-and-corrections]] #11 on sponsor gravity).
- For a pilot: adopt six files + specs AND keep your existing verify loop (typecheck+tests per commit) — the corpus's strongest combination, not either alone.
