# Sources — agent containment & the monitoring-vs-execution budget

> **Drained:** 2026-09-13 by `/loop`. **RE-ANCHORED topic** (Option C). The operator's submitted video was
> `VeizK1M7V7E` "Sam Altman on Astra, AGI, and the future of OpenAI". A pre-flight found that anchoring on it
> would produce a scorecard of OpenAI grading OpenAI, so the anchor was moved to the incident's evidentiary
> spine and the interview demoted to one source with a declared interest.

## Evidentiary spine — all three fetched and HTTP-verified by the main loop, not by an agent

| # | Source | Published | Org | Independent of OpenAI? | Artifact |
|---|---|---|---|---|---|
| a1 | [Security incident disclosure — July 2026](https://huggingface.co/blog/security-incident-july-2026) | **2026-07-16** | Hugging Face | **YES — fully** | Victim disclosure |
| a2 | [Anatomy of a Frontier Lab Agent Intrusion: A Technical Timeline](https://huggingface.co/blog/agent-intrusion-technical-timeline) | **2026-07-27** | Hugging Face | **YES — fully** | Forensic timeline |
| a3 | [Brief independent investigation of agents' behavior…](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) | **2026-08-26** | METR | **Organizationally yes; evidentially NO** | On-prem log review |

**Decomposition — do not read this as three witnesses.**
3 artifacts → **2 organizations** → **1 fully decorrelated witness**.
METR's data was *supplied by* OpenAI, its review window *capped by* OpenAI (Jun 26–Jul 13, with virtually all
reviewed data from Jul 7 onward), investigators could not query the model or touch OpenAI infrastructure, and
OpenAI retained redaction rights. **Every METR-derived figure must be tagged OpenAI-scoped.**
Hugging Face is the only witness that owes OpenAI nothing — and **a1 was published on 2026-07-16 before HF knew
who had attacked them**, which makes it structurally incapable of reciting OpenAI's account. That is the
strongest anti-recitation control available to this corpus to date.

## Demoted source — interested party, graded as such

| # | Source | Published | Interest |
|---|---|---|---|
| s4 | "Sam Altman on Astra, AGI, and the future of OpenAI" — Sources Podcast, `VeizK1M7V7E` | **2026-09-01** | **OpenAI CEO describing OpenAI's own containment response, two days before his company's next launch.** Sponsor-read segments present. Not a witness. |

Load-bearing quote, [07:30]–[07:58], verbatim from the auto-captions:
> "after the hu[gg]ing face incident we put a lot more controls in place uh in terms of how we monitor our
> agents … while they're working the way we sandbox things the way th[at] … the slowdown and reallocation of
> resources after hugging face I think is what you'd expect"

## Excluded, and why

- **GPT-6 / Astra — EXCLUDED ENTIRELY.** Launched 2026-09-03; it cannot in principle satisfy a
  pre-2026-09-03 decorrelation prong, and nothing about it was verified first-hand.
- **All five sources named by the pre-flight's re-anchor probe — DROPPED.** 0 of 5 cleared the gate.
  One (*"Resilient Cyber, ~2026-09-04"*) **does not exist**: the publication's RSS `pubDate`s run
  Sep 1, 2, 3, 6, 10, 11 — verified by the main loop. One (Redwood) was **misdescribed** (its corrections are
  an inline block, not a separate errata post; the "containment" wording matches a different post). The other
  three (Big Technology w/ Stamos, AI Explained, 80,000 Hours) are real but are **commentary carrying no
  artifact of their own**; the 80,000 Hours episode is post-cutoff and sources its spine to OpenAI's report.

## Fetch guard

| File | Words | Status |
|---|---|---|
| a1 | 880 | PASS — **after 1 recovery** |
| a2 | 5,616 | PASS — **after 1 recovery** |
| a3 | 31,763 | PASS |
| s4 | 14,709 | PASS (0 recoveries) |

🔴 **Recovery detail — new silent-failure instance.** `bin/html-to-clean-md.py` returned rc=0 and printed
`wrote …` for a1 and a2 while emitting **57 and 98 words**: readability-lxml selected huggingface.co's
**sidebar model cards** (GLM-5.2, NVFP4) instead of the article body, and stamped the correct article title on
top of them. A file with a right-looking header and no content is the most dangerous shape of failure this
corpus tracks. **Fix used: `https://raw.githubusercontent.com/huggingface/blog/main/<slug>.md`.**
