# Codex — Expert Disagreements

> **Topic:** [[_index|codex]]
> **Source:** `../../raw/2026-05-13-codex-long-running-agentic-harness-alternative-to.md` § Outliers

The 6 sources agree on the **shape** of the harness category but diverge sharply on which tool deserves the primary builder slot, whether multi-model is required, and what "real engineering" means in an agentic workflow. Five real conflicts surfaced.

---

## Conflict 1: Codex-as-primary vs Claude-as-primary

The sharpest disagreement in the bundle.

**Codex-first view (Riley Brown):** Calls Codex "**the NEW Best AI Coding Tool**" for 2026 [Source 3]. The full course is structured around Codex as the daily-driver — Claude appears only in passing.

**Claude-first view (Mosh Hamadani, Teacher's Tech):** Both describe Claude Code as **"the best option out there right now"** and build life-changing, "10x faster" workflows entirely on Claude Code [Source 4, Source 5]. Mosh in particular treats Codex as out-of-scope for his tutorial entirely.

**The "Forest Gump" contrarian view (Jack Roberts):** Claims Claude Code has **"gotten a little bit worse"** recently and suffered **"quality regression"** [Source 6]. Jokes that users expected "Albert Einstein" but "Forest Gump turned up" [Source 6]. Personally observed the model produce incorrect results on tasks it previously handled well.

**The hybrid resolution (Jack Roberts again):** Don't pick one — **use both**. Claude for building, Codex for adversarial review [Source 6].

**Why this matters:** A new user reading any single source comes away with a completely different "which tool to install first" answer. The bundle, taken as a whole, suggests installing both and treating the choice as **"which one is your default builder this month"** rather than a one-time decision.

---

## Conflict 2: Multi-model vs single-model

A directly related but distinct fight.

**The "Three Brain" advocate (Jack Roberts):** Relying on one model is a mistake because **every model has "blind spots"** [Source 6]. Operates a router that tags in Gemini for long-context video/PDF tasks, Codex for adversarial code reviews, Claude only for the primary build [Source 6]. Three models, each playing to its strength.

**The "Simplified Harness" counter (The AI Automators):** A divergence inside Anthropic's own research [Source 2]. The Automators initially used a complex multi-agent harness (planner + generator + evaluator). With **Opus 4.6 + 1M-token context**, they found they could **simplify the architecture** — remove sprints, remove context resets, **"one-shot" entire apps** because the model's context window had grown enough to eliminate the need for the orchestration layer [Source 2].

**The cynical undercurrent (The AI Automators):** Even as they describe simplification, they're **skeptical** of the 1M-token claim — note it's in Anthropic's "best interest to process tokens" for revenue, so claims that "context anxiety has been solved" should be read carefully [Source 2].

**Why this matters:** Multi-model isn't an obvious win — it adds latency, cost, and orchestration complexity. The bundle splits on whether that overhead pays for itself.

**Resolution heuristic:** if you're hitting Claude's failure modes regularly (especially self-evaluation), multi-model with Codex as judge is worth it. If you're not, the simpler single-Claude workflow may dominate.

---

## Conflict 3: Vibe coding vs real engineering

A philosophical divide that affects how you set up Codex/Claude Code, not just which one you pick.

**The engineering purist (Mosh):** Explicitly distances his approach from **"VIP coding experiments"** and **"product manager workflows where 50 AI agents build an app while you sleep"** [Source 5]. Insists that **software engineering is not going anywhere** and that developers must **review every line of code** and apply solid engineering practices [Source 5]. The carpenter mindset (analogized to a power saw) — the tool doesn't replace the craft [Source 5].

**The vibe coding multitasker (Riley Brown, Keith AI):** Lean into "vibe coding" — focus on **multitasking** and running 10+ tasks in parallel [Source 1, Source 3]. Riley Brown often uses **"full access" permissions** to let the agent "cook" while moving on to other tasks [Source 3]. The goal is to become an **"effective multitasker"** rather than a line-by-line reviewer [Source 3].

**Teacher's Tech sits in the middle:** Agrees with Mosh that fundamentals matter, but with a less-purist framing — "AI handles the mechanical parts" rather than "AI is a power saw" [Source 4].

**Why this matters:** The same Codex install can be operated in either mode. The mode is a **policy choice** (you and your team's), not a configuration choice. Mismatched expectations between collaborators on the same project will cause friction faster than any technical problem.

---

## Conflict 4: Self-evaluation — works or fundamentally broken?

A subset of Conflict 2 worth calling out separately.

**The "Claude is a poor QA agent" position (The AI Automators):** In testing, Claude often **identified legitimate bugs but then "talked itself into deciding they weren't a big deal"** and approved the work anyway [Source 2]. Self-evaluation is fundamentally broken; you **must** wire in a separate evaluator [Source 2].

**The implicit "good enough" position (Mosh, Teacher's Tech):** Neither source mounts a defense, but neither bothers wiring in a separate evaluator either. The implicit position: with careful prompting and human review, Claude's self-evaluation is acceptable [Source 4, Source 5].

**Why this matters:** This is the **technical foundation** of the Three Brain Auto-Router argument. If you accept "Claude is a poor QA agent" as a hard limit, you must run a multi-model setup. If you don't, single-Claude is fine.

The bundle does not resolve this. It's a question of how often you actually hit the failure mode, which depends on the kind of work you do (greenfield vs production maintenance, etc.).

---

## Conflict 5: Tool-choice risk and third-party wrappers

A short but pointed conflict on **vendor policy**.

**Keith AI's warning:** Using **Claude Code inside third-party wrappers like Open Code might carry a "risk of being banned" by Anthropic** [Source 1]. Recommends different tools depending on whether the user is a "Claude fan" or a "multi-model user" — implies the wrapper question matters for vendor relationship continuity, not just technical compatibility [Source 1].

**Nobody else in the bundle addresses this.** Mosh, Teacher's Tech, Riley Brown, Jack Roberts, and The AI Automators all use the vendors' native CLIs directly and don't mention wrapper risk.

**Why this matters:** If you're considering a wrapper layer (and there are many growing in the ecosystem), this is a one-source warning to take seriously and verify. Bans are catastrophic to a workflow built on a vendor relationship.

---

## Summary table

| Topic | Position A | Position B |
|---|---|---|
| **Primary tool** | Codex is "the NEW Best" [Source 3] | Claude Code is "10x faster, the best option" [Source 5] |
| **Quality trajectory** | Claude Code is "Forest Gump", regressing [Source 6] | Claude Code is life-changing, production-ready [Source 4, Source 5] |
| **Multi-model** | Three brains required — Claude/Codex/Gemini [Source 6] | Single Claude + 1M context is enough [Source 2] |
| **Engineering rigor** | "Vibe code", multitask, full access [Source 1, Source 3] | Review every line, carpenter mindset [Source 4, Source 5] |
| **Self-evaluation** | Claude is poor QA, must wire in separate evaluator [Source 2] | Implicit: self-eval is fine with human review [Source 4, Source 5] |
| **Wrapper risk** | Third-party wrappers risk Anthropic ban [Source 1] | Not addressed by any other source |
| **Context-window claims** | Skeptical — Anthropic has revenue incentive to push tokens [Source 2] | Accept Anthropic's claim, simplify harness around it [Source 2 also] |

---

## Key Takeaways

- **Codex-vs-Claude-primary is unresolved** — Riley Brown and Jack Roberts lean Codex/hybrid, Mosh and Teacher's Tech lean Claude [Source 3, Source 5, Source 6]
- **The contrarian Claude-regression take (Jack Roberts)** is the most striking single position in the bundle — verify before committing [Source 6]
- **Multi-model overhead is not an obvious win** — The AI Automators argue 1M-token Opus 4.6 obsoletes much of the orchestration layer [Source 2]
- **"Vibe coding" vs "real engineering" is a policy split, not a tool split** — the same Codex install runs either mode
- **Self-evaluation is the technical heart of the multi-model argument** — if Claude can't reliably review its own work, you need Codex (or another model) as judge [Source 2, Source 6]
- **Wrapper risk is a one-source warning** [Source 1] — take seriously, verify with vendor policy before betting a workflow on a third-party CLI
- **Context-window claims should be read with caution** — vendor incentives matter [Source 2]
