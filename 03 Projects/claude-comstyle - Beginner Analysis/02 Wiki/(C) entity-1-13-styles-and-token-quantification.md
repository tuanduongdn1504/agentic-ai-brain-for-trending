# (C) Entity 1 — 13 communication styles + Token-Economy-Quantification methodology + Compositional Mix & Match framework

**Type**: Core-product entity.
**Scope**: The 13 prompt-styles themselves + the design axes that organize them.

## What this entity is

The product surface of `claude-comstyle` is a **library of 13 named communication-style prompts** organized along three orthogonal design axes:

1. **Token-Economy Axis** (% output-token impact rating with 🟢🟡🔴 3-tier badge)
2. **Category Axis** (Productivity / Quirky-Fun / Mental-Model — 3-bucket taxonomy)
3. **Compositional Axis** (Mix & Match formal framework + `terminal CLI style` universal modifier)

Each of the 13 styles is documented via a **7-attribute schema** (title + tagline + token-rating + prompt + before/after example + CLI variant + pros/cons + best-for/not-suitable). The schema is consistently applied across all 13 entries.

## The Token-Economy Axis — PRIMARY observation

| Tier | Badge | Range | Styles |
|---|---|---|---|
| Heavy reducers | 🟢 | 50-75% fewer | Military, Caveman, Reality Check, git log, Socratic* |
| Light reducers | 🟡 | 20-35% fewer | BLUF |
| Neutral | 🔴 | ~0% | Yoda |
| Light expanders | 🔴 | +5-20% more | Pirate, 80s Hacker, Dad Joke, Rubber Duck |
| Heavy expanders | 🔴 | +20-40% more | Feynman, First Principles |

*Socratic asterisk = per-response saving but multi-turn cost can rise.

**Why this matters as an observation**:

- **Quantification IS the design axis** — token-impact isn't documented as an afterthought; it's the **primary discriminator** for choosing a style. Tables in the README sort styles by token-impact for at-a-glance selection.
- **3-tier badge taxonomy** (🟢🟡🔴) provides visual at-a-glance comparison distinct from raw % range. Categorical signaling complements ordinal signaling.
- **CORPUS-FIRST per-style quantification** — prior corpus subjects quantified aggregate token economy ("85% fewer tokens" v76; "540 tokens/skill avg" v76) at LDS or routing-architecture layer, not per-style. v87 quantifies at per-style granularity.
- **Trade-off transparency**: the README **explicitly names** styles that COST tokens (Feynman, First Principles, Pirate, 80s Hacker, Dad Joke, Rubber Duck) rather than hiding them. The token-economy axis cuts both ways — savings AND costs are quantified equally.

**Phase 4b PRIMARY**: this design axis is registered as **Library-vocab "Token-Economy-Quantification per Communication Style" PROVISIONAL N=1** at v87 audit-queue. v90 first-cycle stale-check.

## The Category Axis — 3-bucket taxonomy

| Category | Count | Styles | Common trait |
|---|---|---|---|
| Productivity | 5 | Military, Caveman, Reality Check, git log, BLUF | Reduce-tokens-and-fluff; optimize for fast cycles |
| Quirky / Fun | 4 | Yoda, Pirate, 80s Hacker, Dad Joke | Stylistic personality overlay; not for production work |
| Mental Model | 4 | Rubber Duck, Feynman, Socratic, First Principles | Pedagogy / thinking-tool framing; cost-tolerant for learning |

The 3-bucket taxonomy creates a use-case-based selection scaffold orthogonal to the token-economy axis. A user can:

- Start from **goal** ("I'm learning React" → Mental Model bucket) and then sort by token-economy
- Start from **token budget** ("I need 🟢 cheap" → Productivity or Socratic) and then sort by goal

The 2-axis selection grid is more intricate than the prior corpus design-skill clusters (v75/v81/v82/v83/v85) which organize primarily by aesthetic-style without cost-axis. v87 introduces **cost-as-first-class-axis** to prompt-style taxonomy.

## The Compositional Axis — Mix & Match formalized

The README dedicates a section to **explicit prompt composition**:

> Styles can be combined:
> ```
> Military brevity + BLUF format. Direct. No filler.
> Lead with one-sentence answer. Details only if needed.
> ```
> ```
> Feynman explanation style + git log action items at the end.
> ```
> ```
> Reality Check + Military. Honest verdict, no words wasted.
> ```

Plus the **`terminal CLI style` universal modifier** appendable to any base style:

> *Want even fewer tokens? Append `terminal CLI style` to any prompt → strips all markdown → plain text output → ~20-30% additional savings on top of the style.*

**Composition modes** observable in the README:

| Mode | Example | Result |
|---|---|---|
| Within-category mix | Military + BLUF (both Productivity) | Both token-reducers stack |
| Cross-category mix | Feynman + git log (Mental + Productivity) | Pedagogy + action-items hybrid |
| Universal modifier overlay | Any style + `terminal CLI style` | +20-30% additional savings |
| 3-way composition | Reality Check + Military + git log | Honest verdict + no filler + bullet action items |

**CORPUS-FIRST formal Compositional Prompt Style Mixing framework** in v60+ window. Prior corpus prompt-related subjects (v71 agents-best-practices + v77 easy-vibe curriculum) did not frame style/prompt composition as a first-class product feature. Library-vocab candidate "Compositional Prompt Style Mixing" registered at OC layer pending v90 framing decision.

## The 7-attribute-per-style schema

Each entry in the README follows:

1. **Heading**: emoji + style name
2. **Tagline**: 1-line flavor description
3. **Token savings rating**: 🟢🟡🔴 badge + % range + reasoning if asterisk
4. **Prompt block**: verbatim, ready to copy
5. **Before/After table**: default Claude column vs styled column; same input question
6. **`+ terminal CLI style` variant**: shows further-compressed plain-text output
7. **Pros / Cons + Best-for / Not-suitable-for**

13 styles × 7 attributes ≈ **91 attribute-instances** at consistent schema. This is **MICRO-LDS density** (vs v85 669+ codified elements). But the **schema consistency** at this scale is itself a candidate observation: Library-vocab "Multi-Attribute Style Schema" PROVISIONAL N=1 (sister to Token-Economy-Quantification PRIMARY).

## Storm Bear direct-applicability subset

Out of the 13 styles, **4 map directly to Storm Bear's CLAUDE.md communication rules**:

| Storm Bear rule | claude-comstyle match | Mechanism |
|---|---|---|
| "Blunt and direct — challenge me" | **Reality Check** | `[what works] → [real risk] → [verdict: ship / rethink / scrap]` format forces real evaluation; "Not here to criticize. Here to give the honest take nobody else will say." |
| "Always end with suggested next action" | **git log** | Imperative-verb bullets; every bullet is an action item; max 72 chars |
| (general concision) | **Military** | `[problem] → [cause] → [fix]` — fix is implicit next-action |
| (lede priority) | **BLUF** | One-sentence conclusion first, details after; matches Storm Bear's "no narration" preference |

**Composition candidate for vault sessions**:

```
Reality Check + Military + git log action items.
Honest verdict, no filler, bullet next-actions.
```

This composition maps to **both** Storm Bear CLAUDE.md communication rules at once. Pilot Tier-1 actionable candidate at **lowest-cost-of-trial in corpus** (1-min single-file copy install + reversible-via-delete + zero-dependency + zero-API-key).

## What this entity does NOT include

- **No source for % token-impact claims** — they are stated as "tested on Claude" but methodology is not published
- **No formal evaluation protocol** — there's no script you can run to verify Military gives 65-75% fewer tokens for your use case
- **No A/B testing harness** — claims are author-asserted
- **No localization of prompts themselves** — the prompts are English; only the example tables include VN
- **No formal namespace / collision avoidance** — `/style` command could collide with other skills; no announced policy

These gaps are documented honestly per-style via Pros/Cons (Pattern #83 within-pattern), but project-level honest-disclosure of measurement-methodology gap is absent. Recommendation if Storm Bear pilots: run own A/B on 2-3 representative vault tasks to verify the claimed % range holds for vault use cases.
