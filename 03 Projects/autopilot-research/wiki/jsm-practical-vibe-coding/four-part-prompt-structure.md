# The Four-Part Prompt Structure

## Source

- Transcript 00:07:28–00:20:52 (the heart of the crash course).

## The four parts, in fixed order

1. **Point to AGENTS.md** — "Read the agents.md first and follow it strictly." Every prompt, no exceptions ("AI tools don't automatically remember what they read in previous sessions"; "strictly" signals rules aren't suggestions).
2. **One task** — one feature, one screen, one integration. Never "set up NativeWind and build onboarding and add auth" — "if something breaks across three tasks, you can't tell which one caused it."
3. **Constraints that protect what already works** — "the AI doesn't know to leave it alone unless you say so": *"Do not change the screen design." "Preserve the existing UI exactly." "Keep the existing Stream audio flow intact." "Don't expose any secrets in the mobile app."* — "your working code's institutional memory, written down so the AI treats it as something to work around, not to refactor."
4. **Design references** — attach the image for anything visual: "The AI reads layouts better than it reads descriptions of layouts. One image saves three prompts of explaining margins." (The repo ships these as `prompt_material/01…07-*.png` — numbered per-feature design PNGs.)

## Constraints are about BEHAVIOR, not code

- The most-failed part even after teaching the structure: devs "write a constraint that doesn't actually constrain anything" because they think in code, not behavior.
- Don't tell the AI how to write code — tell it **how the feature should behave**: what's already working that must stay, what may change, what's off-limits.
- Derived "the way a product engineer would": *what could go wrong from a user's perspective? what might the AI accidentally change that's working?*
- Includes ambiguity control: **"If anything is unclear, ask before implementing."** (Same contract as [[claude-md-12-rules]] Rule 1 and this vault's no-silent-assumptions rule.)

## Non-visual features: describe behavior + verification infrastructure

- No design to attach for state/auth/backend work — describe behavior instead: "Store the selected language using Zustand with AsyncStorage. If an authenticated user has no selected language, route them to language selection… Preserve the existing UI exactly."
- Then the underrated move: **"add a temporary button on the home screen to clear AsyncStorage so I can test the flow"** — *"prompt for the infrastructure that lets you verify the feature, not just the feature itself."* Dev-only affordances are part of the prompt, removed later.

## Fix prompts

- "The verification modal is appearing behind the keyboard on iOS. It should sit above the keyboard. Don't change any other modal behavior or layout." — problem + correct behavior + protective constraint. No feature re-explanations, no codebase pastes.

## Assessment

- Parts 1–2 are common practice; **part 3 (protective behavioral constraints) is the differentiator** — it encodes regression-prevention into every prompt in a repo with no tests ([[verification-and-review]]).
- Part 4 is validated by the repo: 7 numbered design PNGs committed as first-class prompt material — designs ARE context artifacts, cf. [[open-design/design-md-as-source-of-truth|DESIGN.md]] and the [[ai-web-design-workflow|design-workflow]] thread.
- The structure is a per-prompt restatement of scope: build-now / don't-touch / rules-from-file ([[practical-vibe-coding-workflow]]).

## Key Takeaways

- Fixed order: pointer → one task → behavioral constraints → design reference.
- Write constraints from user-visible behavior, not implementation.
- Ask-before-implementing belongs in the constraint block.
- Prompt for verification affordances (temp buttons, clear-state switches), not just features.
- One problem, one fix, one verification for repairs.
