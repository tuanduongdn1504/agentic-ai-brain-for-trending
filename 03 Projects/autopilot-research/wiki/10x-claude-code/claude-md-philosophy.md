# `claude.md` Philosophy — minimalism vs documentary

The `claude.md` (or `agents.md`) file is supposed to be the project's "brain" — persistent context the agent loads on every session. The 6 creators in this corpus split sharply on how that brain should be structured.

## Three schools of thought

### 1. Minimalist — Boris Cherny
- **Reported state:** his personal `claude.md` is **two lines**.
- **Content:** PR automation rules, nothing else.
- **Rationale:** the model already knows how to write code. The `claude.md` is for things-that-are-non-default. Two lines covers the non-default in his workflow.
- **Trade-off:** works because Boris knows his stack and tools intimately. A new developer with the same 2-line `claude.md` would get inconsistent results.

### 2. Nuke-and-restart — Sean Kochel
- **Practice:** when the file starts causing "noise" or the model goes off-track, delete and start fresh.
- **Rationale:** over-engineering `claude.md` is a treadmill — every fix adds a line, every line adds friction, eventually the file fights the model.
- **Trade-off:** loses accumulated lessons. Some teams write a "noted regressions" section that survives nukes.

### 3. Documentary — AI LABS
- **Reported state:** `claude.md` is a hub pointing to a multi-file system:
  - **PRD** — what we're building, why
  - **`architecture.md`** — system design, key decisions
  - **`decision.md`** — log of why-we-chose-X-over-Y
  - **`feature.json`** — token-efficient feature checklist
- **Rationale:** a single agent session shouldn't need to re-derive the project's intent. Persistent docs are cheaper than re-explaining each session.
- **Trade-off:** maintenance burden. If docs drift from reality, agent acts on stale information — which is worse than no docs.

### 4. Skill-decomposed — Eric Tech (middle path)
- **Practice:** break knowledge into discrete skill files (`/skills/stripe-checkout.md`, `/skills/code-review.md`).
- **Rationale:** `claude.md` stays small because skill-specific SOPs live in their own files, loaded only when needed.
- **Trade-off:** requires upfront skill-design work, but compounds well as the library grows.

## What predicts the "right" choice for you?

Three variables matter:

| Variable | Skews toward minimalist | Skews toward documentary |
|---|---|---|
| Codebase familiarity | High (you wrote it) | Low (legacy / inherited) |
| Team size | Solo | Team (≥3 devs) |
| Failure cost | Low (personal projects) | High (production) |
| Codebase age | <6 months | >2 years |
| Onboarding frequency | Rare | Frequent |

A solo dev maintaining their own 2-year-old codebase can run with 2 lines. A 5-person team onboarding a new hire onto a 10-year-old codebase needs the full PRD + architecture + decision-log.

## Common failure modes

- **The "kitchen sink"** — every lesson learned gets a new bullet point. After 6 months, the `claude.md` is 800 lines and nothing it says actually steers the agent because the relevant rules are buried.
- **The "stale doc"** — `architecture.md` describes a system that's been refactored 3 times since. Agent acts on stale info; humans don't notice because the doc was "trusted".
- **The "circular reference"** — `claude.md` says "see `architecture.md`"; `architecture.md` says "see `decisions.md`"; `decisions.md` says "see `claude.md`". Agent burns context fetching files that point at each other.

## Operational rules of thumb (synthesized across creators)

1. **Cap `claude.md` at ~50 lines for solo work, ~150 lines for teams.** Beyond that, decompose to skills (Eric Tech pattern) or split into multiple files (AI LABS pattern).
2. **When the model goes off-track, ask: did the file fight me?** If yes, nuke (Kochel) or trim that section. If no, the issue is elsewhere (context overflow, prompt ambiguity).
3. **Date-stamp every section.** Sections older than 6 months should be reviewed for staleness during quarterly cleanups.
4. **Don't document what the model already knows.** "Use TypeScript" is wasted bytes. "Use TypeScript with `strict: true` AND no `any` ever — see decision-log entry 47" is useful.
5. **Skills > rules where possible.** "When integrating Stripe, follow this 12-step SOP" should live in `/skills/stripe.md`, not `claude.md`.

## Cross-references

- See [[creator-disagreements]] § 3 for the original disagreement quotes.
- See [[../workflow-ai-coding/core-patterns|workflow-ai-coding § Persistent Memory]] for the cross-corpus consensus.
- See [[tactical-tricks]] § 2 for how to write your first skill file (the lightweight on-ramp to the documentary school).
