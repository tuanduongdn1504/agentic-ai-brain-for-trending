# The anchor audit — and what it reveals about the scorecard itself

> **The prior ship's headline finding does not replicate.** [[../hermes-agent/_index]] concluded *"the operator's own anchor was the most accurate source in the bundle."* Here the anchor lands on **11.1%** hard error — *the same rate again* — but ranks **3rd of 6**. Because rank is a property of the companion set, not of the anchor. **And the deeper finding is that this corpus's own scorecard metric systematically penalises the sources that actually learn the most.**

## The ranking (160 graded claims, 6 sources)

| Source | Hard error | Claims | Views | Note |
|---|---|---|---|---|
| **HistoryAI** | **5.9%** (1/17) | 17 | 23,240 | ⚠️ **PAID SPONSORED** |
| How I AI | 10.0% (4/40) | 40 | **312,210** | highest reach |
| **Quân IT** | **11.1%** (4/36) | 36 | **237** | ⬅ **ANCHOR** |
| Nate B Jones | 13.6% (3/22) | 22 | 160,996 | |
| Eric Nowoslawski | 14.8% (4/27) | 27 | 29,067 | |
| Alex Carter | 16.7% (3/18) | 18 | 55,381 | crypto channel |

*Hard error = CORRECTED + FALSE + MISLEADING + CONTRADICTED-IN-BUNDLE.*

## Three findings, in increasing order of importance

### 1. The absolute rate travels; the rank does not

The anchor hit **11%** in the Hermes bundle and **11.1%** here — remarkably stable across two bundles, two topics, and a month. But in Hermes the highest-reach companion posted **50%**; here it posts **10.0%**. **The rank moved entirely because the company it keeps changed.**

So *"the operator picks reliable sources"* is **not** established by a rank, and never was. Only the absolute rate travels, and **one stable datapoint at ~11% across two bundles** is the finding worth keeping. A third bundle would make it a trend.

### 2. "Reach ≠ reliability" fails here — even at the extremes

Hermes found it held at the extremes only. **This bundle inverts it at the extremes**: the **312,210-view** source is *cleaner* than the **237-view** source on the mechanical count (10.0% vs 11.1%), and **the lowest error rate in the bundle belongs to a paid sponsored walkthrough.**

Neither reach nor independence nor absence of sponsorship predicts error here. The prior rule should be **narrowed to the Hermes bundle**, not carried forward as corpus doctrine.

### 3. ⭐⭐⭐ The metric rewards reciting and punishes doing

What *does* predict the grade profile is **proximity to published text.**

| | CONFIRMED | UNVERIFIED | What the source did |
|---|---|---|---|
| HistoryAI | **64.7%** | low | recites vendor-approved ground; **zero security reservations in 3,148 words** |
| Alex Carter | 38.9% | low | **no evidence he installed it**; reads vendor copy aloud — *and has the highest hard-error rate* |
| Quân IT | **19.4%** (last) | **44.4%** (highest) | **live zero-baseline first-run install and demo** |

The anchor's 16 UNVERIFIED claims are about a trial meter, a connector picker, two bots and a video clip **inside his own private account**. They are unverifiable **by construction** — not because he was careless, but because nobody else can see his screen.

**So the scorecard's most flattering profile belongs to the source that engaged least with the product, and its least flattering belongs to the only source that ran it from zero.** A metric built to catch confabulation ends up scoring *auditability*, and auditability is highest when a source stays closest to text a grader can fetch. Verifiability is **nearly orthogonal to how much a source actually learned.**

This is a limitation of the method, not of this bundle — and it argues for reporting the **error signature** rather than the rate.

## Error signature beats error rate

**The anchor's 36 claims contain zero fabrications** — 0 FALSE, 0 CONTRADICTED-IN-BUNDLE. Every claim traces to something on his screen. His entire error class is **one shape: the dropped qualifier** (8 CBI + 3 CORRECTED, every correction qualifier-shaped — per-bot vs per-account computer; *publish* vs *buy* in the marketplace; general xAI docs vs the Grok Bot doc tree). He also carries the bundle's **highest CBI rate (22.2%)**, so on hard+soft combined he is tied worst (33.3%, with Eric and Alex Carter). **He is the most cautious source about what exists and the least careful about qualifiers.**

Against that, three of five companions assert something their own artifact never showed them:

- **Nate** asserts a launch-time free tier that **did not exist** (FALSE), a 12-bot list that **never arrives** (CONTRADICTED), and a first-ever superlative (MISLEADING).
- **Alex Carter** asserts a **model picker no first-party surface exposes** (FALSE).
- **Eric** self-contradicts **twice on his own headline numbers**.

**Only the anchor and the paid walkthrough carry neither a FALSE nor a CONTRADICTED grade** — and the paid one earns it partly by saying less.

## ⚠️ The ranking is not robust to attribution — do not lean on it

Two adjustments scramble the order entirely:

- **Two of the anchor's four errors are the same defect** (claims 18 and 36, the per-bot computer), and the grading itself notes it *"is the vendor's headline, not his invention."* Count it once and attribute it upstream: the anchor falls to **~5.7%, best-equal.**
- **Two of Alex Carter's three errors are corrections aimed at this bundle's own grading**, not at the creator — one explicitly says *"I disprove my own bundle's finding."* Creator-attributable: **1/18 = 5.6%.**

Adjust both and **the ordering reverses.** A metric that flips under a reasonable attribution choice should not be quoted as a ranking — which is the strongest argument for the signature-over-rate rule above.

## Key Takeaways

- **~11% hard error for this operator's anchors, twice running.** The absolute rate is the durable finding; the rank is an artifact of the companion set.
- **"Reach ≠ reliability" does not generalise** — it inverted here, and a *paid sponsored* source posted the best mechanical score.
- ⭐⭐⭐ **The scorecard rewards proximity to fetchable text.** The source that installed the product from zero scores worst on CONFIRMED and highest on UNVERIFIED, by construction. **Report the error signature, not the rate.**
- **Fabrication and dropped-qualifier are different defects and should never share a number.** The anchor has the bundle's worst qualifier discipline and its cleanest invention record.
- **The ranking reverses under two defensible attribution calls** — one shared vendor error, one grader-directed correction. It is not a robust statistic.

## Sources

- Compile workflow `wf_c3cb4b9e-bbe` — 14 Opus agents, 0 errors / 0 empty, 1.35M tokens, 153 tool calls
- All six transcripts in `raw/2026-09-11-grok-bot-xai-persistent-agents/`
- [[../hermes-agent/_index]] — the prior anchor-audit result being tested

**Related:** [[_index]] · [[claims-scorecard]] · [[the-blockchain-misframing]] · [[one-computer-per-user-not-per-bot]] · [[caveats-and-corrections]]
