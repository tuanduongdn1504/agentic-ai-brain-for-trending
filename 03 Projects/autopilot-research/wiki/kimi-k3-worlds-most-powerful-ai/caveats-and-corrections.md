# Caveats & corrections

## Corrections to the video (verified, UPHELD high)

1. **"Open source — download the weights, do whatever"** → FALSE at video time. Hosted-API-only; weights promised July 27 (Modified MIT). [[open-weights-reality]]
2. **"Cost-effective / won't break the bank"** → MISLEADING. A ~3.2–3.8× price *increase* over K2.6 ($0.95/$4 → 3.16×/3.75×); frontier-tier pricing. *(corrected 2026-07-17 from "~5–6×")* [[pricing-and-the-end-of-cheap-chinese-ai]]
3. **"Beats the frontier; Fable 5 = 58%, GPT-5.6 = 50%"** → FALSE. Actual arena.ai win-rates Fable 5 **63%** / GPT-5.6 Sol **58%**; AA Index rank **#3–4**. [[benchmarks-fact-vs-hype]]
4. **Silent on reliability** → hallucination rate **rose 39%→51%**. [[benchmarks-fact-vs-hype]]
5. **"The US restricted K3 for hacking"** → FALSE. Controls were on Anthropic's Fable 5 / Mythos 5. [[cyber-and-export-control]]
6. **"#1 across the arenas"** → MISLEADING. #1 frontend, **#9 general text**.
7. **"Self-host it"** → FALSE in practice. 650GB–1.7TB memory; months of tooling lag.
8. **Win-rate + Elon + demos framing** → various CBI/misattribution (see [[claims-scorecard]]).

## Unverifiable claims (flagged, not asserted)

- **"#1 writing at 2,840 Elo" (Louis / editorial-voice):** no public record; implausible scale. **Do not quote.** Presented in-wiki only as "an unverifiable cited figure."
- **GDPval "near human / beats GPT-5.6":** partially wrong (K3 is *above* the human baseline; *below* GPT-5.6 Sol Max). Presented with the correct numbers.
- **Anthropic↔Moonshot distillation (~3.4M queries, Feb 2026):** a real *accusation*, **unproven** for K3. Presented as an open question, never as fact.

## Excluded per wiki-verify discipline (Rule 12 fail-loud)

- **"K3 covers 13 languages"** — a synthesis-agent claim that is actually the **cc-sdd 13-platform/language figure bleeding from vault CLAUDE.md context**. Not a verified K3 fact → **excluded**. [[hireui-translation]]
- **Creator real-name PII** — a dive surfaced a first name from the channel's public About page (low-confidence). Per librarian PII discipline (cf. the @anonystick handle-only + pokesynergy PII handling), the wiki holds identity to the **@TheAiGrid** handle + public channel facts and does **not** assert a personal name. [[source-and-creator]]
- **Model-override note (not an error, a limitation):** the verification workflow's per-agent `opus`/`sonnet` overrides were **silently ignored by the runtime** — all 11 agents ran **Haiku 4.5** (same behavior noted on the OKF ship). Mitigation: every load-bearing correction was **independently re-verified in the main loop on Opus** with primary sources before ship. [[source-and-creator]]

## Transcript garble (ASR)

The model name is mangled throughout the auto-captions as **Kimiko 3 / Qwen 1.5 3 / Gemini K3 / Kimi Kate 3 / Kimmy K3 / Kimik AI 3 / K say** — all normalized to **Kimi K3**. "Kimi Work" appears as "co-work / Kimi Work"; "Vals Index" as "Vowels Index." No claim was built on a garbled token without a clean-source check (discard-as-garble guard, both directions).

## Source-discrepancy notes

- **Export-control lift date:** sources give **June 30** vs **July 1, 2026** — a 1-day discrepancy; wiki says "late June / July 1."
- **KDA decode speedup:** cited as **6×** or **6.3×** depending on throughput-vs-TPOT measure; wiki uses 6.3× with the qualifier.

## N=3 reconciliations (Theo pass — see [[theo-claims-scorecard-and-caveats]])

- **Hallucination (refines correction #4):** the corpus's "39%→51%" is the raw *rate* (worse); Theo cites the composite AA-Omniscience *Index* (+6→+18, better via more refusals + accuracy 33%→46%). Both true, different metrics. [[theo-benchmarks-and-the-hallucination-reconciliation]]
- **Speed:** Theo's ~20 TPS vs AA's ~62 TPS = harness-measured vs raw-API — consistent with the corpus's existing "26–28 launch / 62 official." Marked UNVERIFIABLE-as-raw-speed.
- **Residency (refines the "Chinese-hosted" framing):** the international API is **MOONSHOT AI PTE. LTD. (Singapore)**, not literally Chinese servers — but it **trains on inputs+outputs by default**, so the hireui AVOID *strengthens*. [[theo-cost-speed-and-how-to-use]]
- **ASR:** "Infropic" = Anthropic (add to the garble list above).

## Key Takeaways

- **3 FALSE, 3 MISLEADING** framing claims sit on top of a **real, well-specced model** — the corrections are about *availability, ranking, pricing-context, and geopolitics*, not the tech.
- Two confabulations were caught and excluded (the "13 languages" context-bleed; creator PII), and the workflow model-override limitation is disclosed — nothing swept under the rug.
- **N=3 (Theo) corroborated all corrections at 0 FALSE**, and its one apparent conflict refined (not overturned) correction #4.
