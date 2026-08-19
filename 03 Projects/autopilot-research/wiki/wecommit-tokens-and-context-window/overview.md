# Overview

## What this bundle is

Four videos by one Vietnamese practitioner — **Trần Quốc Huy** ([@tranquochuywecommit](https://www.youtube.com/@tranquochuywecommit), 189K subscribers) — that build a single argument from the bottom up:

> **Understand the smallest unit the model operates on (the token), and the right way to work with AI follows as a consequence.**

His stated method comes from ~15 years optimising database systems for banks, securities firms, hospitals and telecoms: *to optimise any system, first understand its smallest unit of operation.* Applied to LLMs, that unit is the token — and it determines cost, latency, and answer quality at once.

## The chain of reasoning

```
tokens are the unit          → tokenization-mechanics
  ↓ vocabulary is mostly English
Vietnamese fragments more    → vietnamese-token-inflation      ⭐ corpus-first
  ↓ the model has no memory
history is re-sent each turn → statelessness-and-context-cost
  ↓ so re-sending must get cheaper
caching, and its real prices → prompt-caching-as-taught · claude-pricing-ladder
  ↓ so: what do you actually do?
four rules for discipline    → four-rules-for-token-discipline
  ↓ at scale, that becomes
an org chart of agents       → agent-org-chart-architecture · dont-swap-models
  ↓ and to make it correct
criteria + reversible gates  → banking-principle-for-agent-correctness  ⭐
```

## What is genuinely new to this corpus

1. **Vietnamese-vs-English token inflation.** Grep-verified corpus-first: no existing topic across 77 covers it. Every other cost source in the vault is written for English.
2. **The reversibility rule for gate placement.** Not "review everything" or "review nothing", but *review exactly the steps you cannot undo.* The underlying principle is textbook (transaction atomicity); using it to decide **where the human sits in an agent pipeline** is not.
3. **"Change two variables, not vendors."** A direct counter-position to the corpus' cheaper-upstream-routing band — optimise workload and call count, not price per token.
4. **A production agent org chart** — CEO agent → departments → specialists, routed by semantics rather than rules — described from an operator who runs his own business on it.
5. **A 189K-subscriber Vietnamese source** — ~2.5× the previous largest VN channel in the corpus, filling the VN-practitioner vertical on token economics.

## Integrity profile

**43 source claims adjudicated: 25 CONFIRMED · 13 incomplete/imprecise · 2 stale-since-publication · 2 unverified · 1 FALSE · 0 FABRICATED.**

A technically-sound practitioner explainer. The parts a reader would act on — pricing, cache arithmetic, tokenization mechanics, the four rules — hold up; his pricing table is **exact** on every tier. The failure mode is *imprecision and omission*: he under-sells caching by never quoting the ~90% read discount, and phrases the Vietnamese cost difference in a way that invites the wrong inference.

> ⭐ **The only fabrication in this entire compilation came from our own extraction pipeline**, which "corrected" the correct model names (Fable 5, Opus 5, Sonnet 5) into legacy models that do not exist. Caught by an independent verifier, then settled by grep. Full record in [[caveats-and-corrections]] — it is the most transferable methodological lesson in this topic.

## Two convergences worth noting

The bundle independently re-derives two things this vault already holds, from a completely different starting point (Vietnamese data engineering rather than English harness engineering):

- **CLAUDE.md Rule 5** — *"If code can answer, code answers."* His rule 1 is the same rule, reasoned from the fact that the model manipulates token ids and therefore cannot be trusted with arithmetic.
- **The maker/checker split.** His "never let AI verify its own output; verify with tools it doesn't control" is the doctrine behind this project's `loop-verifier` agent — and this compilation's own fabrication-and-catch is empirical support for it.

Independent derivation from an unrelated lineage is the strongest kind of evidence a knowledge base can get for a rule it already follows.

## Reading order

**If you have five minutes:** [[four-rules-for-token-discipline]], then [[banking-principle-for-agent-correctness]].

**If you are building something:** [[hireui-relevance]] → [[vietnamese-token-inflation]] → [[prompt-caching-as-taught]].

**If you want to know what to distrust:** [[caveats-and-corrections]] → [[claims-scorecard]].

## All articles

| Article | What it covers |
|---|---|
| [[tokenization-mechanics]] | Tokens, the BPE vocabulary he describes but never names, the on-screen quirks, strawberry |
| [[vietnamese-token-inflation]] | ⭐ Corpus-first: why VN costs more, the volume-not-rate fix, the compounding effect |
| [[statelessness-and-context-cost]] | No memory, full-history re-send, and the 2026 caveats he omits |
| [[prompt-caching-as-taught]] | His cache teaching verified exact — and the ~90% discount he leaves out |
| [[claude-pricing-ladder]] | The PhD/master's/undergrad/high-school ladder, verified, plus the Sonnet 5 expiry |
| [[four-rules-for-token-discipline]] | The actionable payload |
| [[agent-org-chart-architecture]] | CEO → departments → specialists; semantic routing; the dashboard |
| [[dont-swap-models]] | "Change two variables, not vendors" — and the corpus counter-pole |
| [[agent-forgetfulness-and-vendor-memory]] | The memory canon (CoALA, Generative Agents, MemGPT) + vendor survey |
| [[banking-principle-for-agent-correctness]] | ⭐ Criteria, reversibility, and independent verification |
| [[claims-scorecard]] | All 43 verdicts + the 6 main-loop overrides |
| [[caveats-and-corrections]] | ⭐ The extraction fabrication, the ASR garble map, what to un-learn |
| [[source-provenance]] | The four videos, the channel, and what could not be established |
| [[hireui-relevance]] | Cache-in-English, translate-at-the-edge, and the ADR convergence |
