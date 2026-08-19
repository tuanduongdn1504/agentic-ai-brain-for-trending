# Statelessness and Context Cost

> **Source:** anchor [`yxQGugIwFaU`](https://www.youtube.com/watch?v=yxQGugIwFaU) [15:47]–[19:01]; reinforced across [`MshYeoy8g2o`](https://www.youtube.com/watch?v=MshYeoy8g2o).

## The claim, and why it is the right teaching anchor

> *"Bản thân thằng AI nó không nhớ được. Nó không nhớ."* — [15:47]

His mechanism ([16:15]): to answer your new message the model must be given **all previous content** plus the new message, together, as input. The whole prior conversation is re-tokenised and re-sent on **every** turn.

His consequence ([16:42]): if each turn is ~400 tokens of history and ~100 tokens of new message, then by turn 10 the input has ballooned — **more money and more processing time.** This is why a long chat feels slow and burns the monthly plan limit, which is the complaint he opens the video with.

**This is correct**, and framing it as a *design law* rather than a quirk is the pedagogically right move. It explains three symptoms at once — rising cost, rising latency, and the model "forgetting" once history is trimmed.

## The 2026 caveats his blanket framing omits

"It remembers nothing" is true of the raw model and was true of the API in general. In 2026 it is **incomplete**, and the omissions all point the same way — the problem is more tractable than he implies:

| Mechanism | What it changes |
|---|---|
| **Prompt caching** | The history is still *sent*, but unchanged prefixes bill at **~0.1× input** — a ~90% discount on the re-send. He teaches caching ([[prompt-caching-as-taught]]) but never states this number, which is the single biggest lever |
| **Compaction** | Server-side summarisation of earlier turns as the context limit approaches, instead of paying for raw history |
| **Context editing** | Clearing old tool results / thinking blocks before the model sees them |
| **Memory tools & stores** | Persistent cross-session state that lives *outside* the context window — see [[agent-memory-architecture/_index]] |

So the accurate statement is: **the model is stateless; the platform is not.** Statelessness is the default and the thing to design around, not an immovable ceiling.

## What is NOT wrong here (a verifier over-reach, corrected)

An automated verifier in this run flagged his cache-expiry passage as MISLEADING, claiming he quoted cache **write** prices where **read** prices apply. **That verdict is wrong and has been overridden.**

At [20:22] he says, verbatim, *"nó có phần cách này, **cách phần ghi này**"* — "it has this cache part, **this cache write part**" — and then reads $6.25 (5-minute) and $10 (1-hour) off that column. He **explicitly identified it as the write column** and his figures are exactly 1.25× and 2× the $5 base. He was right; the verifier was not. Full record in [[claims-scorecard]].

His cache-expiry framing — *when the cache expires you have to read everything again and it costs you* — is likewise **correct**, and if anything understates the case: a re-write costs 1.25×–2× base input, i.e. *more* than an uncached read, not less.

## Cross-links

- [[prompt-caching-as-taught]] — the mitigation he does teach, and the discount he omits
- [[vietnamese-token-inflation]] — the multiplier that compounds against this
- [[agent-forgetfulness-and-vendor-memory]] — video 3's treatment of the same weakness at agent scale
- [[claude-api-cost-optimization/prompt-caching]] — the Anthropic Platform-team version of the same lever
- [[mosh-ai-powered-apps/openai-to-claude-mapping]] — how to work with statelessness in code
- [[claims-scorecard]]
