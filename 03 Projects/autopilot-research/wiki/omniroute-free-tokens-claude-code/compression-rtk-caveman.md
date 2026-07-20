# RTK + Caveman Compression

## Source
t2 [02:23], t3 [05:08], t5 [11:30]; OmniRoute `COMPRESSION_GUIDE.md`; Workflow verdict `compression-rtk-caveman` (CORRECT-BUT-INCOMPLETE, high).

## The claim
OmniRoute stacks two compression engines — **RTK** and **Caveman** — that "**save 15–95% of tokens**," averaging "**~89% on tool-heavy sessions.**" A repo example takes a 69-token explanation down to 19 tokens "with the same meaning."

## Verdict: CORRECT-BUT-INCOMPLETE (self-reported, not independently validated)
- The **range and mechanism are real and documented.** Modes span **Lite ≈15%** to **Stacked ≈78–95%**; the ~89% average comes from the project's own formula `1 − (1 − 0.80)×(1 − 0.46) = 89.2%` (RTK ≈80%, Caveman ≈46%).
- **But every figure is self-reported.** No third-party benchmark or peer-reviewed evaluation exists. The critic flagged this as arguably UNVERIFIABLE rather than "high confidence" — treat the 89% as a **vendor claim**, not a measured fact. OmniRoute does ship an offline eval harness (`npm run eval:compression`) you can run yourself.
- **Applies to prose/tool-chatter only.** The docs (and t3) are explicit and unusually careful: **code, URLs, and structured JSON pass through byte-for-byte identical**; only repetitive natural-language filler and tool payloads are squeezed. That preservation guarantee is the reassuring part.

## Why it matters here
- Coding agents emit huge, repetitive tool payloads every turn; on that traffic, heavy compression genuinely stretches a free tier further. t3's framing: "cutting 78–95% of the tokens means the same work that used to burn through a paid budget now barely dents a free one."
- **Trade-off to keep in mind:** compressing the *prose/instructions* portion of a prompt can subtly change model behaviour on nuance-sensitive tasks. The byte-perfect code/JSON guarantee limits the blast radius, but "same meaning" is the vendor's assertion, not a proven property — worth spot-checking on your own workload before relying on it.

## Key Takeaways
- **15–95% / ~89%** token savings is a **real, documented, self-reported** figure — not independently benchmarked. Run `npm run eval:compression` if it's load-bearing for you.
- **Code / URLs / JSON are preserved byte-for-byte**; only prose + tool chatter is compressed — a genuinely thoughtful safeguard.
- Compression is a legitimate reason the free-tier math works; just don't treat "89%" or "same meaning" as proven.
- Related: [[what-omniroute-is]] · [[claims-scorecard]] · [[caveats-and-corrections]]
