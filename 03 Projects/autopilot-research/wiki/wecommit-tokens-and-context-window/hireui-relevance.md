# hireui Relevance

> **Why this topic matters to the product:** hireui is a Vietnamese-market recruitment SaaS with **no LLM integration yet** — which means these findings land as *design constraints for a feature not yet built*, not as a retrofit. That is the cheapest possible moment to absorb them.

## ⭐ The finding that is unique to this topic

Every other cost topic in the corpus is written for English. **This one tells you the tax you pay for operating in Vietnamese** — and it compounds in a way none of the four videos states:

> **Vietnamese token inflation multiplies against stateless history re-sending.**
> A Vietnamese conversation does not just cost ~3–7× more per turn. Because every turn re-sends the whole history ([[statelessness-and-context-cost]]), a Vietnamese session **reaches the context ceiling — and the slow, expensive regime — several times sooner** than an English one.

For a product whose core inputs are Vietnamese CVs and Vietnamese job descriptions, that is a first-order architectural fact, not a footnote.

## The pattern to adopt: cache in English, translate at the edge

The economically correct shape for hireui's first LLM feature (candidate↔job Match-Explain):

1. **Normalise to a stable, cacheable prefix.** Candidate profile and job description are fetched once and placed in a **frozen prefix** — no timestamps, no per-request ids, deterministic field order. Volatile content goes last, after the final cache breakpoint.
2. **Pay the write premium once** (1.25× for 5-minute TTL, 2× for 1-hour) and then **read at ~0.1×** across every subsequent matching call against that same candidate. Break-even is 2 requests on the 5-minute TTL.
3. **Reason in English, present in Vietnamese.** Do the matching over the English-normalised representation where tokens are cheapest, then translate only the **final** explanation into Vietnamese — as batch post-processing, outside the conversation loop.
4. **Never re-translate inside the loop.** Translating intermediate output back and forth inside the cached conversation destroys the cache prefix and forfeits the entire saving.

The target to hold yourself to: **a Vietnamese user should cost roughly 1.15× an English user, not 7×.** If your cost model shows 7×, the decomposition is wrong, not the language.

## The four rules, mapped onto hireui

From [[four-rules-for-token-discipline]]:

| Rule | hireui application |
|---|---|
| **1 — code, not prediction** | Never let the model compute a match score, rank candidates, count years of experience, or filter by salary/location. Those are **SQL and arithmetic**. The model's job is the *explanation*, not the *number*. This is the difference between a defensible feature and an unauditable one |
| **2 — terse output, cheap language** | Cap the explanation length explicitly; reason in English, render Vietnamese |
| **3 — schema before data** | Do not dump whole CV tables into context. Send the field structure, a sample, and the row count; drop columns that don't serve the decision. Cuts cost **and** improves output |
| **4 — partition by strength, and make it ask** | Semantic judgement → model; deterministic filtering → database. And require it to **list missing facts and ask** rather than infer a candidate attribute it does not have — inferring is precisely where a recruitment LLM becomes a liability |

## The governance convergence — this independently supports the ratified ADR

[[banking-principle-for-agent-correctness]] arrives, from 15 years of banking systems, at three rules that map one-to-one onto hireui's **RATIFIED candidate-LLM legibility ADR**:

| His rule | The ADR requirement |
|---|---|
| Quantifiable pass/fail criteria, never subjective words like "good" | **Fixed and legible** — a scoring instrument the model is graded *against*, never emergent scoring |
| Human review on every **irreversible** step | **Human-in-the-loop** — and it tells you *where* to put the human: at the steps you cannot undo |
| Generation and verification must not share a context; verify with tools the model doesn't control (SQL, `curl`) | **Audited + eval-gated** — the maker/checker split |

**Rule 1 is load-bearing for hireui specifically.** An irreversible step in recruitment is not "sending a quote email" — it is **rejecting a candidate**, or surfacing a ranking a recruiter acts on. Under the EU AI Act, employment screening is Annex III high-risk. His reversibility test gives you a *principled, non-arbitrary rule* for gate placement: **any step that changes a human's candidacy is irreversible and requires a human verdict.**

His closing observation is the strategic one for a small team: **criteria are a durable asset; prompts depreciate.** Models keep improving underneath you, but a well-specified acceptance criterion stays valid — and it is also the thing an auditor can read.

## Concrete next moves

1. **Before writing any LLM code**, write the acceptance criteria for Match-Explain as a numbered, quantifiable list (true/false or numeric only). That artifact *is* the eval harness and the audit record.
2. **Model the Vietnamese token cost explicitly** in the cost estimate — do not price the feature off English benchmarks.
3. **Design the cache prefix before the prompt.** Prefix stability is an architectural decision; retrofitting it means rewriting the request shape.
4. **Place the human gate by reversibility**, and write down which steps are irreversible.
5. **Fix the Sonnet 5 price in any spreadsheet** — $3/$15 from 2026-09-01, not $2/$10.

## Cross-links

- [[vietnamese-token-inflation]] — the tax, and the compounding effect
- [[prompt-caching-as-taught]] · [[claude-pricing-ladder]] — the levers and the real numbers
- [[four-rules-for-token-discipline]] · [[banking-principle-for-agent-correctness]] — the method and the governance
- [[miai-cv-matching-agent/_index]] — the corpus' domain-exact VN CV↔job source
- [[mosh-ai-powered-apps/_index]] — the vendor-seam pattern for hireui's first LLM feature
- [[claude-api-cost-optimization/_index]] — the first-party cost levers
- [[api-security-7-techniques/_index]] — the BOLA/authorization risk that sits underneath any candidate-data path
