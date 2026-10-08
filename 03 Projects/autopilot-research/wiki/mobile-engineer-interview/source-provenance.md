# Source & provenance

## Sources

Five **private** YouTube videos on the operator's own channel **Tuấn Dương** (the interviewer). Operator-submitted URLs. All Vietnamese-language with embedded English technical terms.

| # | ID | Title (candidate) | Stack | Length | Recorded |
|---|---|---|---|---|---|
| 1 | `OVN_9-15sy0` | Vũ Thành Long (FL) | Flutter | 51:47 | 2025-05-27 |
| 2 | `aKMVTOvgjsI` | Do Minh Thanh (FL) | Flutter | 1:04:17 | 2026-06-15 |
| 3 | `0n8oaue3-y4` | Trương Nhất (FE) | React / JS | 33:08 | 2026-06-15 |
| 4 | `PVO5AX4YAgQ` | Đỗ Thanh Tuấn (MO) | React Native + Android | 35:08 | 2026-06-17 |
| 5 | `DztoZaxz79Y` | Huỳnh Đinh Hoàng Viên (FE) | React | 55:29 | 2026-08-05 |

~3h55m total. Hiring company referenced as "Innovo" (ASR-garbled "Eno"/"Enovo" — not asserted with certainty).

## Ingestion (Path 5 — yt-dlp only)

1. **Access:** all five are **Private** videos — yt-dlp failed with "Private video. Sign in…" on anonymous access. Resolved via `--cookies-from-browser chrome` (the operator's logged-in YouTube session can view them; read-only, local). Safari/Brave/Firefox/Edge had no usable cookie store; **Chrome** worked.
2. **Captions:** `--write-auto-subs --sub-langs vi-orig,en --skip-download --sub-format vtt` — pulled BOTH the Vietnamese-original ASR and YouTube's auto-translated English, per video.
3. **Cleaning:** `awk` cleaner kept only tagged continuation lines (`<c>`), stripped inline tags, stamped a timestamp at each minute boundary → ~34K words en + ~34K words vi across the 5. (Python is SIGKILLed in this environment; all text transforms via awk/sed/jq.)
4. **NO NotebookLM, NO yt-search.**

## Why both languages

The English auto-translation is readable for *meaning* but **mangles every technical term** (`Flashbox`, `Isaac`, `TD tag`, `.abb`). The Vietnamese-original preserves English tech words as spoken (React speakers say "useEffect", "component", "Promise" in English inside Vietnamese sentences). Faithful extraction required cross-referencing **both** + domain knowledge to reconstruct each term. Garble→term map: [[caveats-and-corrections]].

## Verification trail

- **Extraction (maker):** one agent per video read both transcripts and produced a structured Q&A record, reconstructing garbled terms with a verified garble key.
- **Failure + recovery:** the first Workflow (`wf_89de7c46-db7`) extracted 3/5; videos 2 (aKMV, the 64-min one) and 3 (0n8o) hit the StructuredOutput retry cap — likely too-long output truncating the JSON against a strict schema. A second Workflow (`wf_2408264b-657`) recovered both with a **looser schema + a ~30-item cap + compact-output instruction**. Recorded loudly in [[caveats-and-corrections]] (Rule 12: fail loud).
- **Verification (checker):** one refute-first verifier per video re-read both transcripts to catch hallucinated questions, dubious reconstructions, speaker-swaps, and technically-wrong model answers. Findings folded into [[claims-scorecard]] and [[caveats-and-corrections]].
- **Authorship:** Opus main-loop synthesised the wiki from the verified extractions, applying the verifier corrections (maker/checker split).

**Totals:** 5 videos · 170 Q&A items · ~166 verified-OK · 13 agents across 2 Workflows.

## Scope & privacy

These are the operator's own private hiring recordings of named candidates. The wiki + raw stay in the private autopilot-research vault (scope-clamped; nothing published externally). Candidate names are kept here and in [[overview]] as the operator's own record; the **portable cheatsheet** (`output/`) is anonymised + question-centric (personal data minimised in any artifact that leaves the vault).

## Key Takeaways

- Private videos ⇒ authenticated fetch via the operator's own Chrome session (read-only).
- Doubly-garbled ASR ⇒ every term is a reconstruction; **trust the wiki's verified answers, not the captions**.
- One extraction pass failed on 2/5 and was recovered with a looser schema — surfaced, not hidden.

**Raw:** `raw/2026-08-06-mobile-engineer-interview.md`. Back to [[_index]].
