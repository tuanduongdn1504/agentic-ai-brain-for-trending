# Benchmarks — fact vs hype

The video spends ~[00:28]–[10:10] on benchmarks and frames them as "unbelievable … clearly beating the frontier." Here is what each leaderboard actually says.

## The headline: it's a specialist, not "the most powerful"

| Board | K3 result | Reality |
|---|---|---|
| **arena.ai Frontend Code Arena** | **#1**, 1,679 Elo, 76% win rate | TRUE — but a **narrow** board (frontend/visual coding). #1 in 6 of 7 domains; #2 in Gaming behind Fable 5. A **17-place jump** from K2.6's #18. |
| **Artificial Analysis Intelligence Index** | **#3–4**, score **57.1** | Behind **Fable 5 (59.9)** and **GPT-5.6 Sol (58.9)**; ~tied **Opus 4.8 (~56)**. NOT "beating the frontier." |
| **General text arena** | **#9**, ~1,486 Elo | **Mid-pack.** The ~193-point gap vs its own frontend score is the whole story: K3 is domain-narrow. |
| **GDPval (AA v2)** | ~1,687 Elo, **#3** | Above Opus 4.8, **below** GPT-5.6 Sol Max (1,748) and Fable 5. |
| **Vals Index** | 74.7%, **#2 of 38** | Real, publicly available. (The video's "Vowels Index" appears to be a mis-hearing of "Vals Index.") |

## The win-rate numbers were wrong (COR7, UPHELD)

- Video said: "Claude Fable 5 and GPT-5.6 were **58% and 50%**."
- Actual arena.ai data: **Fable 5 = 63%**, **GPT-5.6 Sol = 58%**, K3 = 76% (K3's own number is correct).

## The reliability regression the video omitted (COR5, UPHELD)

- K3's **hallucination rate ROSE from 39% → 51%** gen-over-gen, while accuracy rose 33% → 46% (AA Omniscience Index). **It fabricates more even as it answers more correctly.** The video never mentions this — and for a recruitment product it's the single most important number (see [[hireui-translation]]).

## The fabricated "2,840 Elo writing #1" claim (UNVERIFIABLE → treat as false)

- At ~[06:30] the video cites a tweet ("Louis … our internal writing benchmark … editorial voice at 2,840 Elo … surpassing Claude Fable 5").
- **No public benchmark records this.** K3's actual public text/writing Elo is ~1,486; the top public writing Elo is ~1,508 (Fable 5). A "2,840 Elo" score is nearly 2× any frontier model on any standard scale. This is either a **private, non-standard-scale internal metric** or garbled. **Do not quote it as fact.**

## Benchmark-saturation caveat (the skeptics' point)

- The Frontend Arena #1 may partly reflect **optimization *for* that benchmark** — models trained on the visual-coding tasks people repeat online. ProgramBench author Ofir Press noted K3 reported a **non-recommended metric** (averaging implementation-% rather than counting fully-working programs), which can overstate results.
- Simon Willison's framing (see [[reception-and-skeptics]]): benchmark-to-quality correlation "has been mostly severed"; the thing that matters — **agentic tool-calling over long conversations** — is exactly what the frontend board does *not* test.

## Key Takeaways

- **#1 on frontend, #3–4 overall, #9 on text.** "World's most powerful AI" is marketing; "strong frontend specialist, near-frontier generalist" is the truth.
- The video got the model's own numbers roughly right but **inverted the competitors'** win-rates and **hid the hallucination regression**.
- The "2,840 Elo writing" claim is **unverifiable and implausible** — a good example of a hype-video number to never repeat.
