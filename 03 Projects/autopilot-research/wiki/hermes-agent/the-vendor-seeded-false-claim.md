# The vendor-seeded false claim — why F4 keeps coming back

> **Added:** 2026-09-03 revisit (`raw/2026-09-03-hermes-agent-revisit/`). Companion to [[claims-scorecard]] (the 2026-07-18 snapshot) and [[revisit-2026-09-03]] (this drain's scorecard).
> **The finding is original to this ingest.** No source states it; it comes from putting one source's on-camera quote next to the vendor's own README, 47 days after the corpus graded the claim FALSE.

## What the revisit was designed to test

The 2026-07-18 build graded four claims **FALSE**, and the natural question was whether they belong to *one creator* or to *the whole genre of Hermes tutorials*. So the 2026-09-03 drain ran a **replication test**: six sources, each checked against the same four claims (see the matrix in [[revisit-2026-09-03]]).

The design assumed two possible answers — creator-specific, or genre-wide. **The evidence returned a third one the design did not anticipate: vendor-seeded.**

## The evidence

**H4 / F4** — *"the only agent with a built-in learning loop"* — was graded **FALSE** on 2026-07-18 ([[claims-scorecard]], H4), refuted by Hermes' own `hermes claw migrate`, which imports memories **and skills** from OpenClaw and therefore concedes OpenClaw has a learning loop too.

The 2026-08-26 anchor repeats it. Not paraphrased — read aloud off the screen, in both languages, at the same timestamp:

- **EN [00:55]** *(auto-translation)*: "This is the GitHub page for Hermes Agent. As you can see, it's described as an AI Agent that can learn by itself and continuously improve, built by Nous Research. **It's also the only Agent with a feature called the Learning Loop.**"
- **VN [00:55]** *(original)*: "…đây là cái trang kết hub của Hermish Agent. Thì như các bạn thấy thì **ở đây họ mô tả** là… Và nó là cái **agent duy nhất** mà có cái…"

The load-bearing words are the Vietnamese **"ở đây họ mô tả"** — *"here **they** describe."* The creator is not asserting this on his own authority. He is on the GitHub page, pointing at it, **quoting the project and attributing the quote to the project.**

And the project still says it. Read verbatim from the README on **2026-09-03**, first paragraph:

> "The self-improving AI agent built by Nous Research. **It's the only agent with a built-in learning loop** — it creates skills from experience, improves them during use, nudges itself to persist knowledge, searches its own past conversations, and builds a deepening model of who you are across sessions."

The grounder that retrieved it recorded the authorship explicitly: *"this claim is the README's own text, NOT attributed to video creators. This is project self-statement."*

## Why this matters more than "a creator got it wrong"

**The creator did nothing wrong.** He accurately relayed a false claim and correctly credited its source. His fidelity is exactly what produced the error — a careful creator reading first-party copy reproduces that copy's falsehoods *more* reliably than a careless one.

Which means the propagation path is **upstream of every creator in the genre**:

- The corpus can grade F4 FALSE as many times as it likes. That has no effect on the claim's supply.
- Any future Hermes tutorial that does the responsible thing — open the README, quote the project, attribute it — **will reproduce F4 again.**
- The 2026-07-18 build attributed H4 to "first-party" and was right to. This revisit shows the first-party claim is not a historical artifact: it survived 10 releases and 47 days, through v0.19.0, v0.20.x and v0.21.0, untouched.

**The corollary for this corpus:** a claim's verdict must carry its *origin*, because origin predicts recurrence. A creator-invented error dies with the creator. A **vendor-seeded** error recurs in every downstream source indefinitely, and the only thing that retires it is the vendor editing the sentence.

## The pattern beneath the other three

Once F4 is read as vendor-seeded, the rest of the matrix sorts cleanly by origin — and the two error classes behave completely differently:

| Claim | Origin | Behaviour across 6 independent sources |
|---|---|---|
| **F4** *only agent with a learning loop* | **Vendor README** (still live) | **1 REPEATS · 2 PARTIAL** — reproduced wherever a source quotes the README's framing |
| **F3** *runs under Claude Code* | Creator (AI LABS, v0.18 bundle) | **2 CONTRADICTS · 2 PARTIAL · 2 ABSENT** — **zero repeats.** Died with its creator |
| **F2** *launched February 2026* | Creator (single) | **1 REPEATS · 5 ABSENT** — appears exactly once, in `grep`-verified isolation |
| **F1** *~22K stars* | SEO blogs | **3 CONTRADICTS · 3 ABSENT** — **zero repeats**, and every video that gives a number gives a different one |

**The one claim the vendor owns is the one claim that replicated.** The three the vendor does not own were contradicted or absent in every source that touched them.

## The `claude-code` topic tag — how F3 probably got seeded

F3 (*"Hermes runs under Claude Code"*) is **not mentioned anywhere in the README** — the grounder checked and recorded "CLAUDE CODE MENTION: NOT MENTIONED — does not appear anywhere in the README."

But the repository's **GitHub topics** are:

> `ai`, `ai-agent`, `ai-agents`, **`anthropic`**, `chatgpt`, **`claude`**, **`claude-code`**, **`codex`**, `hermes`, `hermes-agent`, `llm`, `nous-research`, **`openai`**

The project SEO-tags itself with `claude-code`, `claude`, `codex`, `anthropic` and `openai` while never mentioning Claude Code in its own prose. That is a plausible seed for the exact confusion the corpus graded FALSE — and it is a **weaker** form of the same mechanism as F4: metadata the vendor controls, asserting a relationship the vendor's prose does not.

⚠️ **This is a hypothesis about causation, not a verified claim.** The topics are verified (GitHub API, 2026-09-03); that they *caused* the AI LABS framing is inference. Recorded here because it is testable — if a future source cites the topic list as evidence of Claude Code integration, it is confirmed.

## Key Takeaways

- **A false claim's origin predicts its recurrence.** Vendor-seeded claims recur through every faithful downstream source; creator-invented claims die with the creator. The 2026-09-03 matrix separates these two classes cleanly at N=6.
- **The only F4 fix is upstream.** Nothing this corpus writes retires it; Nous Research editing one sentence does.
- **Fidelity is not accuracy.** The most careful thing a creator can do — quote the vendor and attribute it — is precisely what propagated the corpus' most-refuted claim.
- **`hermes claw migrate` is still the refutation**, and it still ships (README, 2026-09-03, with `--dry-run`, `--preset user-data`, `--overwrite`). The vendor simultaneously publishes the exclusivity claim and the tool that refutes it.

## Cross-links
[[revisit-2026-09-03]] · [[claims-scorecard]] · [[caveats-and-corrections]] · [[hermes-vs-openclaw]] · [[claude-code-interop]] · [[learning-loop-and-self-improving-skills]] · [[source-provenance]]
