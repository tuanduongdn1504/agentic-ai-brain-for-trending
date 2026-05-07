# Claude Code Hooks — Expert Disagreements

> **Topic:** [[_index|claude-code-hooks]]
> **Source:** `../../raw/2026-05-07-claude-code-hooks.md` § Outliers

The 5 sources don't agree on hooks. Three real conflicts surfaced.

---

## Conflict 1: Productivity boost vs latency drain

The single sharpest disagreement.

**The optimistic view:** Hooks "speed up your workflow massively" — set-and-forget automation that compounds over time [Source 5].

**The contrarian view (Joe Rhew, Source 3):** Hooks added so much latency to his CLI that he became "quite frustrated" and **removed most of his hooks** [Source 3]. The frustration centered on `pre-tool use` hooks firing on every interaction — even when the routing logic was correct, the cumulative wall-clock cost outweighed the benefit.

**Specifically guilty:** prompt hooks (AI-evaluated). Joe Rhew notes deterministic command hooks are fast, but any hook that requires Claude to "reason" adds significant token-processing time per fire [Source 3].

**Resolution heuristic:** start with notifications + post-tool-use formatters (cheap, infrequent). Add `pre-tool use` only with strict matchers. Never add prompt hooks without measuring latency first.

---

## Conflict 2: Minimalist vs essential

How important are hooks really?

**The minimalist view (Source 1, AI Terminal):** Despite the source title ("Hooks Deep Dive"), the speaker says: "I don't really do a whole lot of hooks myself and I don't really see a big need for a lot of them just personally" [Source 1].

**The essential view (Source 3 + Source 4):** Source 3 calls hooks "one of the most powerful features in Claude Code" [Source 3]. Source 4 (Matt Pocock) goes further — recommends **replacing `CLAUDE.md` entirely with hooks** to preserve the LLM's "instruction budget" [Source 4].

**Why this matters:** the 5 sources span three orders of magnitude in stated value (from "nice to have" to "primary instruction surface"). A new user reading any single source will get a wildly different sense of how much to invest. The bundle suggests starting small (notifications) and only escalating to `CLAUDE.md` replacement after measuring real friction.

---

## Conflict 3: AI-driven or AI-free?

A definitional fight that affects how you think about hooks.

**"Pure deterministic" camp (Source 5, Source 3):** Hooks are "non-AI deterministic token-free actions" or "pure automation where no LLM is involved" [Source 3, Source 5]. The whole point is avoiding the LLM in the inner loop.

**"Hooks include AI" camp (Source 2 + Source 3 again):** Both describe **prompt hooks** — hooks specifically evaluated by Claude to perform subjective reasoning, e.g. checking directory-structure overlap or applying security guardrails that need judgement [Source 2, Source 3].

**Why this matters:** the term "hook" has expanded to cover both pure shell scripts and AI-evaluated logic. This confuses newcomers who pick the wrong flavour. The bundle's recommendation: **default to deterministic command hooks; reach for prompt hooks only when the rule genuinely needs subjective judgement**, and accept the latency cost as a trade-off.

---

## Summary of conflicts

| Topic | Position A | Position B |
|---|---|---|
| **Workflow impact** | Speed up workflow, "set and forget" automation [Source 5] | Causes frustration, slows CLI to the point of being unusable [Source 3] |
| **`CLAUDE.md` vs hooks** | `CLAUDE.md` is the primary place for rules [Source 5] | Should "almost always" delete `CLAUDE.md` and use hooks for deterministic enforcement instead [Source 4] |
| **Ease of use** | Hooks are simple "event-driven shell commands" [Source 1] | Designing complex hooks requires intricate "filtering and routing" patterns [Source 2] |
| **AI involvement** | "Pure automation, no LLM" [Source 3, Source 5] | Prompt hooks are AI-evaluated [Source 2, Source 3] |

---

## Key Takeaways

- **Latency is the silent killer** — measure before/after when adding prompt hooks; remove if frustration sets in (Joe Rhew's lesson) [Source 3]
- **Don't take any single source's value claim at face value** — sources span "nice to have" to "primary instruction surface"; let your own friction calibrate
- **"Hook" is overloaded** — make sure you know which flavour (command vs prompt) you're picking before starting [Source 2, Source 3]
- **The Matt Pocock take is the most aggressive position** in the bundle — interesting if you want a strong opinion to test against, but verify with your own measurements before deleting `CLAUDE.md` [Source 4]
