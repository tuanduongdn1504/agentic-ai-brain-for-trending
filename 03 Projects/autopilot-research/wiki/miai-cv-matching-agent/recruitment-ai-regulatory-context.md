# Recruitment-AI Regulatory Context (what the demo never mentions)

## Source

Dive `regulatory-corpus` + refute-first verify (wf_dd724957-cac), searches run 2026-07-05. Date-sensitive — re-verify before relying on deadlines.

## Why this article exists

The demo matches candidates to jobs with an AI score — in production that is an **Automated Employment Decision Tool**, one of the most regulated AI categories anywhere. The video (reasonably, as a lab) says nothing about this. Anyone piloting the pattern in a real recruitment product (hireui) must know this table.

## Verified landscape (as of 2026-07-05)

- **NYC Local Law 144** (CONFIRMED): in force since 2023-01-01 (enforcement 2023-07-05). AEDTs used for NYC hiring/promotion need an **independent bias audit within 12 months of use**, publicly posted results, and candidate notice. Penalties $500–$1,500 **per day per violation**.
- **EU AI Act** (CONFIRMED, date-sensitive): employment/worker-management AI is **high-risk (Annex III)**. The original 2026-08-02 compliance date for high-risk obligations was **pushed to 2027-12-02 by the Digital Omnibus** (Parliament 2026-06-16, Council 2026-06-29). Obligations when they land: risk management, bias testing, human oversight, technical documentation, monitoring.
- **Illinois HB 3773** (CONFIRMED): in force **2026-01-01** — prohibits AI with discriminatory effect in employment decisions (even unintentional), mandatory notice when AI is used in hiring/promotion/discipline; IDHR enforcement + civil suits.
- **Colorado** (PARTIAL — corrected): SB 24-205 (due 2026-06-30) was **replaced before taking effect** by **SB 26-189** (signed 2026-05-14, effective **2027-01-01**) — a narrower disclosure/transparency framework around "automated decision-making technology".
- **Vietnam PDPL** (PARTIAL): Law 91/2025/QH15 effective **2026-01-01** + Decree 356/2025 — **explicit, verifiable prior consent** required for recruitment-data processing (no implied consent). Claims about mandatory DPAs with AI vendors and delete-if-not-hired specifics could **not be independently verified** — treat as open questions for counsel.
- **PII flow**: the demo posts full CV PDFs to a third-party API with no consent flow, no redaction, no size/MIME limits ([[code-audit]]) — fine for a fictional Claude-written CV, a GDPR/PDPL incident with real ones.

## Design consequences for a real product

- Prefer **assistive over decisional** framing: retrieval rank + explanation for a human recruiter (lower regulatory class) instead of an auto-score that filters candidates (AEDT).
- If scores exist, they need calibration + bias testing + audit trails ([[matching-quality-vs-production]]) — uncalibrated LLM scores are indefensible in an audit.
- Log the agent's inputs/outputs (the demo logs nothing) — audit-ability is a legal requirement, not observability nice-to-have.
- Consent + DPA before any CV leaves your infrastructure; minimize/redact where possible.

## Key Takeaways

- Recruitment matching is a **regulated AI category** in NYC (now), Illinois (now), EU (2027-12), Colorado (2027-01) — ship the compliance surface with the feature, not after.
- The EU extension (Aug 2026 → Dec 2027) is recent, material news — verified against multiple law-firm sources; re-check before quoting.
- Human-in-the-loop + explanation-first design is both the better product and the lighter regulatory posture.
- First regulatory-landscape article in this wiki's recruitment/agent thread; [[external|Storm Bear: multi-agent-orchestration]]'s job-screener has zero compliance coverage (verified) — this fills that gap.
