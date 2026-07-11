# Source provenance & verification method

## How this topic was sourced

- **Path 5 (yt-dlp only, operator-submitted single video).** No NotebookLM.
- **Ingest:** `yt-dlp --dump-json` for metadata; `yt-dlp --write-auto-subs --sub-langs "vi.*,vi,en.*" --sub-format vtt` for captions. VN auto-subs (`sub.vi.vtt`, 475KB) downloaded; **English track hit HTTP 429** (not needed). ffmpeg absent (subtitle-only, irrelevant).
- **Clean:** custom `clean.py` — stripped VTT tags/timestamps, deduped YouTube's rolling-caption repetition → **1,100-line / ~57.4K-char timestamped transcript**, **read in full in the main loop**. (Note: the machine's `python3` shim is broken — used `/usr/local/opt/python@3.12/bin/python3.12`.)
- **Raw artifact:** [`raw/2026-07-07-system-thinking-ai-coding.md`](../../raw/2026-07-07-system-thinking-ai-coding.md) — metadata + description links + chapter map + extracted claims + full transcript.

## The "double deep dive" into the original resource

Because this is a **conceptual talk with one primary intellectual source (an essay) + three empirical citations** — not a code repo — the dive was scoped to two focused subagents plus main-loop ground-checks, rather than a large repo-file fan-out:

- **Agent A — primary-source deep dive on Naur 1985.** Fetched the essay's body text + canonical quotes from multiple mirrors (essay itself is offline/journal-bound): riverandsoftware.com, catenary.wordpress.com, embeddedartistry.com, inventwithpython.com; author facts from Wikipedia + amturing.acm.org. Produced the Ryle-theory definition, the three-capabilities list, the program-death/revival quotes, and a fidelity table. → [[naur-programming-as-theory-building]].
- **Agent B — adversarial verification** of the four checkable claims (name/title, jagged frontier, Harvard-62M hiring study, IBM 3×). Refute-first.
- **Main-loop ground-checks (2 WebSearches)** on the two highest-risk items (the "Harvard/62M" study and the IBM claim) — which **overturned Agent B's mis-correction** of the Harvard study.

## Verification ledger

| Claim | Verdict | Source |
|---|---|---|
| Author = **Peter Naur**, *"Programming as Theory Building"* (1985); Turing 2005; BNF; ALGOL 60 | **CONFIRMED** | amturing.acm.org; en.wikipedia.org/wiki/Peter_Naur |
| Naur thesis (theory-in-head, code-as-shadow, program death/revival) | **CONFIRMED (faithful in spirit)** | essay mirrors above |
| "Jagged technological frontier" (Harvard/BCG) | **CONFIRMED** | Dell'Acqua et al., SSRN 4573321; *Organization Science* 2026 |
| Harvard, **62M records**, GenAI cut junior hiring since 2023 | **CONFIRMED** (verifier misfire overridden) | Hosseini Maasoum & Lichtinger, SSRN 5425555 (Aug 2025) |
| **IBM 3×** entry-level hiring 2026 (Nickle LaMoreaux) | **CONFIRMED** | Fortune 2026-02-13; Axios; Bloomberg; Tom's Hardware; ibm.com/think |

## Misfire log (Rule 12)

- **Agent B (empirical verifier) mis-corrected the Harvard-62M claim** as a "misattribution to Stanford's *Canaries in the Coal Mine*." OVERRIDDEN by main-loop `WebSearch` confirming the Harvard 62M study (Hosseini & Lichtinger) exists and matches. This is the recurring **verifier-confabulation / substitute-a-known-fact** pattern flagged in the vault's wiki-verify discipline; caught pre-publication. Detailed in [[caveats-and-corrections]].
- No other misfires; no discard-as-garble overturns (all four claims ground-truthed on first main-loop check).

## Reception (not verified beyond view counts)

- 2,925 views / 227 likes / 1,920 subs at capture (2026-07-07). Small VN channel; no independent commentary located. Treat popularity claims as marketing.

## Key Takeaways

- **Sourcing is transparent and reproducible**: one first-party VN video → one essay + three citations, all verified.
- The dive was **right-sized to a conceptual source** (2 agents + main-loop checks) rather than the repo-scale workflows used for code subjects elsewhere in the corpus.
- The single most important discipline event was **overriding our own verifier** — logged loudly per Rule 12 and the vault's wiki-verify rule.
