# Caveats & corrections (Rule 12 — fail loud)

## Source

Cross-checks against the video [`raw/2026-07-07-system-thinking-ai-coding.md`](../../raw/2026-07-07-system-thinking-ai-coding.md), the Naur deep-dive, and main-loop searches. See [[source-provenance]] for the full method.

## Attribution garbles (auto-caption, not the speaker's fault)

- **"Peter Law" → Peter Naur.** VN auto-caption of the Danish name. [[naur-programming-as-theory-building]].
- **"Programming Story Building" → "Programming as *Theory* Building."** "Theory" mis-transcribed as "Story."
- **"EBM" → IBM.** The tripling-entry-level-hiring firm is IBM (CHRO Nickle LaMoreaux).
- **"Generatives AI năm 2023"** — fine; refers to the post-ChatGPT GenAI wave.

## Naur fidelity — 2 paraphrases are looser than the source

- **"The whole program is completed in the brain *before* touching code" = PARTIAL/overstated.** Naur says the theory is *built through* solving the problem (iterative), not pre-composed waterfall-style.
- **The "conductor (nhạc trưởng)" metaphor = STRETCH.** Not in Naur; an interpretive gloss (resonant but not his language).
- The core "code is the shadow / program lives in the head" and "generate-without-theory = stop building theory" are **FAITHFUL.** Full table in [[naur-programming-as-theory-building]].

## Empirical claims — all CONFIRMED, but one required overriding our own verifier

- **Harvard, 62M records (junior hiring ↓ since 2023): CONFIRMED.** Hosseini Maasoum & Lichtinger, SSRN 5425555 (Aug 2025), 62M workers / 285K firms / 2015–2025; junior −7–12% at AI-adopters, seniors flat.
  - ⚠️ **VERIFIER MISFIRE (logged):** the empirical-verification subagent declared this a *misattribution* — insisting the real study was Stanford's *"Canaries in the Coal Mine"* (Brynjolfsson et al., ADP payroll ~3.5–5M/month, ages 22–25, −13–16%) and that "Harvard/62M" was wrong. A main-loop `WebSearch` **refuted the refutation**: the Harvard 62M study exists and matches the speaker exactly. The Stanford study is a real *sibling*, not the cited one. This is the classic corpus pattern — a lens/verifier substitutes a fact it "knows" for the one actually present, and confidently mis-corrects. Ground-checked before publication.
- **Jagged technological frontier: CONFIRMED.** Dell'Acqua et al. (HBS 2023 / Organization Science 2026), 758 BCG consultants.
- **IBM 3× entry-level hiring 2026: CONFIRMED.** Fortune/Axios/Bloomberg/Tom's Hardware, Feb 2026.

## Framing / bias caveats (do-not-oversell list)

- **Promotional close is real.** The last ~3 min pitch the **AI Software Builder Bootcamp** + CodeFarm (system thinking + self-hosting on VPS). The transferable method (3 questions + 4 steps) stands on its own; treat the "own your VPS / devs go to the chicken coop" framing as marketing, not analysis.
- **Small-channel, single-voice, no-code talk.** 1,920 subs, 2,925 views; opinion/thesis format ("No cut, no edit"), no repo, no demo, no citations on screen — the citations were reconstructed and verified by us, not shown by him.
- **"20–30% will survive the industry" / "only a few remain"** — rhetorical, uncited estimates. Motivational, not data.
- **"Prompting keeps getting easier / needs less context"** — a directional opinion; contested by the prompt-/context-engineering literature. Treat as a stance, not a finding. Cf. [[claude-md-12-rules]], [[harness-engineering]].
- **VPS self-hosting as the founder end-state** — reasonable for small products; it's also the bootcamp's upsell. Weigh against managed-vs-self-hosted trade-offs in [[fullstack-docker-cicd]] and [[self-hosted-devops-oss]].

## Key Takeaways

- **Content integrity is high**: every checkable claim is true; the only errors are auto-caption garbles and two loose Naur paraphrases.
- The one thing we had to fix was **our own verifier's mis-correction** of the Harvard-62M study — a reminder to ground-check "misattribution" verdicts, not just the original claims.
- Separate the **method (excellent, portable)** from the **pitch (marketing)** when applying this.
