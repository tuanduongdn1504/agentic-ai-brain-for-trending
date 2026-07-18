# Theo (N=3) — claims scorecard & caveats

> The incremental scorecard for the Theo (t3.gg) pass, plus the fail-loud (Rule 12) log. Verified by an 9-agent refute-first workflow (`wf_0a283971-eb6`) + main-loop Opus anchors on every load-bearing number.

## Incremental scorecard — the signature of a credible independent source

Theo's ~34 checkable statements break down as **22 CONFIRMED · 3 CORRECT-BUT-INCOMPLETE · 8 OPINION · 1 UNVERIFIABLE — and, crucially, 0 FALSE / 0 FABRICATED.**

**That zero-FALSE line is the headline.** N=1 (TheAIGRID hype) carried **3 FALSE** framing claims; N=2 (BridgeMind vendor) carried **1 FALSE** sub-claim (the "5×" price error). The skeptical independent practitioner carries **none** — his errors are *incompleteness* (omitting the 51% rate) and *measurement context* (20 vs 62 TPS), not falsehoods.

### The claims that matter

| Theo claim | Verdict | Corpus relation |
|---|---|---|
| AA Intelligence Index = 57, "#3, behind Fable 5 & GPT-5.6 Sol, ~ Opus" | **CONFIRMED** | CORROBORATES #3/#10 |
| $3/$15/$0.30 = "roughly Sonnet-level priced"; ~2× verbosity cancels discount | **CONFIRMED** | CORROBORATES #2, #17 |
| Weights July 27; hosted-only at launch | **CONFIRMED** | CORROBORATES #1/#12 |
| #1 frontend / visual specialist | **CONFIRMED** (his own hands-on) | CORROBORATES #11 |
| Moonshot is a Chinese-parent company; don't send sensitive data | **CONFIRMED** (nuanced: Singapore-operated) | CORROBORATES residency |
| Subscriptions don't grant full 1M context | **CONFIRMED** | EXTENDS #1 |
| Not native in Claude Code/Codex; used OpenCode + CLI proxy | **CONFIRMED** | NEW mechanics |
| Omniscience: K3 "best open-weight at not hallucinating" | **CORRECT-BUT-INCOMPLETE** | CORROBORATES-with-caveat #4 (omits the 39%→51% rate) |
| No system/safety card at launch | **CORRECT-BUT-INCOMPLETE** | EXTENDS cyber |
| Inference "through Chinese servers" | **CORRECT-BUT-INCOMPLETE** | EXTENDS (Singapore-operated; trains on I/O) |
| ~20 TPS out | **UNVERIFIABLE / CONFLICTS** | reconciled: harness-measured vs AA's 62 raw-API |
| Deep SWE 73/70/67.5; GDPval 1668; SWE-marathon lead; Grok-below-K3 | **CONFIRMED** (as Theo's cited figures) | NEW granular / EXTENDS #3 |
| ping.gg 122-task port; Fish Slap 3D; sidebar "better than we had"; sub-agents check off parent to-dos; security audit | **OPINION** (lived evidence) | NEW texture |
| ~$63/day heavy use vs ~$1k OpenAI / ~$300–400 Fable | **OPINION** | NEW |

Full per-claim detail lives in the source raw file and the workflow journal; the four theme articles ([[theo-benchmarks-and-the-hallucination-reconciliation]], [[theo-independent-hands-on-evidence]], [[theo-cost-speed-and-how-to-use]], [[theo-security-safety-and-open-weight-risk]]) carry the reasoning.

## What Theo independently corroborates (the point of an N=3 source)

A skeptic who opened by saying he *hasn't been hyped about open weights* independently confirms **every one of the corpus's load-bearing corrections**: #3–4 not #1 · frontend specialist · Sonnet-tier pricing (not cheap) · 2× verbosity tax · weights-not-out-until-July-27 · Chinese-parent residency risk · the Omniscience-index improvement. Independent corroboration from a hostile-prior source is the strongest evidence class this topic has.

## Caveats & corrections (Rule 12 — fail loud)

1. **Sponsor excluded.** A **Depot** (CI/Docker) paid sponsor read runs **00:24–03:12** — excluded from all knowledge claims (verified no Depot claim leaked into the scorecard).
2. **Secondary-source enrichment stripped.** The workflow's Haiku agents attached precise sub-scores Theo **never states on-camera** ("Frontier SWE 86.6/81.2/71.3", "Terminal 88.3", "Program 77.8", "SWE-Marathon 42.0", "Browse Comp 91.2%", "Briefcase 1547", subscription tier *names* + "$19/$39/$99/$199", "Inkling 975B", "Grok 4.5 = 54"). Per wiki-verify discipline these were **not asserted** as Theo-claims or corpus-verified facts — the wiki keeps only Theo's on-camera figures (73/70/67.5, AA 57, GDPval 1668, DeepSeek V4 1.6T, 64×H100 = $2.6M, ~20 TPS, ~$63/day, $20–$200 tiers).
3. **Mandatory hallucination caveat applied.** Per the completeness critic, Theo's "best at not hallucinating" is shipped **only with** the 39%→51% raw-rate caveat. See [[theo-benchmarks-and-the-hallucination-reconciliation]].
4. **Speed conflict disclosed, not hidden.** Theo's ~20 TPS vs AA's ~62 TPS is marked UNVERIFIABLE-as-raw-speed and reconciled as harness-vs-API measurement context (consistent with the corpus's existing "26–28 launch / 62 official").
5. **Residency nuance corrected in K3's favor, verdict unchanged.** "Chinese servers" → international API is **MOONSHOT AI PTE. LTD. (Singapore)**; but the [privacy policy](https://platform.kimi.ai/docs/agreement/userprivacy) trains on inputs+outputs by default → **AVOID for candidate data still holds** ([[hireui-translation]]).
6. **ASR garble.** "Infropic" [25:43] = **Anthropic**; model name mangled as Kimmy/Gemini K3 throughout — normalized; no claim built on a garbled token without a clean-source check (discard-as-garble guard, both directions).
7. **Model-override limitation (disclosed, same as prior passes).** All **9** workflow agents ran **Haiku 4.5** despite per-agent effort overrides — so **every load-bearing number was independently re-verified in the main loop on Opus** against primary sources (Artificial Analysis, the-decoder, winbuzzer, officechai, Kimi privacy policy) before ship. The workflow supplied adversarial breadth, not sole authority.

## Key Takeaways

- **0 FALSE / 0 FABRICATED** — the defining contrast with N=1 (3 FALSE) and N=2 (1 FALSE). A skeptical independent source's errors are *incompleteness*, not *falsehood*.
- **Heavy CORROBORATES + OPINION split** is the healthy signature of a hands-on source: it confirms the facts and adds lived texture.
- **Three CBI nuances** (hallucination rate, safety-card, Singapore-not-China) each make the picture *more* precise and, for hireui, *more* cautious.
- **Discipline held:** sponsor excluded, Haiku enrichments stripped, garble normalized, overrides disclosed, load-bearing numbers Opus-verified.
