# Privacy & data-residency — the real killer app (the hireui angle)

> This is the article the video *doesn't* write but is the most important one for a regulated product team. Grounded in the [[source-provenance|economics-privacy dive]] + the operator's standing compliance thread.

## The core insight

Beto frames local inference as **cost** and **offline convenience**. For a product handling **personal data**, the bigger prize is **data-residency**: **when the model runs on your machine, the data never leaves it.**

For **hireui** — a multi-tenant recruitment SaaS processing candidate **CVs and PII** — that is the strongest possible compliance posture.

## Why local inference is a superior compliance posture

| Property | Cloud LLM API | **Local inference** |
|---|---|---|
| Data egress | Candidate PII sent to a 3rd party | **None — stays on the box** |
| Sub-processor | Adds a processor to your GDPR/PDPL records | **No new sub-processor** |
| Cross-border transfer | Possible (US servers ← EU/VN data) | **None** |
| Vendor training-on-data risk | Must trust the vendor's ZDR/retention terms | **N/A — no vendor sees it** |
| Offline / air-gapped | Impossible | **Works fully offline** |
| Audit trail | Split across your logs + vendor's | **Entirely internal** |

**Regulatory context (why this is load-bearing for hireui):**
- **EU AI Act** classifies recruitment/employment screening as **high-risk** (Annex III). Compliance obligations (data governance, human-in-the-loop, transparency) apply regardless of where the model runs — but local inference **satisfies the data-governance leg directly** (no third-party processor, no transfer, internal audit trail). Deadline nominally **2026-08-02**, possibly extended to **2027-12-02** via the pending Digital Omnibus — a moving target ([[../miai-cv-matching-agent/_index|miai-cv-matching-agent]] tracks this).
- **Vietnam PDPL** (Law 91/2025, in force 2026-01-01): consent-per-purpose, no data trading, penalties for cross-border-transfer violations. Local inference sidesteps the cross-border-transfer question entirely.
- **GDPR**: local = fewer processors, no international transfer mechanism needed for the inference step.

## What local does NOT solve (be honest)

- **You now own the box's security.** "No third party" also means "no third-party security team." Patch, isolate, access-control it yourself.
- **Data governance still applies.** High-risk-AI obligations (bias testing, human-in-the-loop, documentation) don't disappear because the model is local — they get *easier to evidence*, not waived.
- **Quality gap is real.** A local 4-bit 27B is below a cloud frontier model. For nuanced final decisions you may still want the cloud model — which reintroduces the transfer question for *that* step.

## The right architecture for hireui: hybrid, tiered by sensitivity

The seam that makes this practical is hireui's planned **Match-Explain vendor abstraction** ([[../mosh-ai-powered-apps/_index|Mosh A2 seam]]): the provider is swappable, so route by **data-sensitivity × task-difficulty**:

| hireui task | Data | Route | Why |
|---|---|---|---|
| Bulk **CV parsing / field extraction** | Raw PII | **Local** | High volume, cheap, and PII never egresses |
| **PII detection / redaction** before any cloud call | Raw PII | **Local** | Redact locally, *then* the cloud model sees only sanitized text |
| **Resume image parsing** (logos, signatures, format anomalies) | PII images | **Local (Qwen3.6 vision)** | Local multimodal works ([[qwen3.6-27b]] C10); zero image egress |
| **Match-Explain** (nuanced candidate↔job reasoning) | Redacted/derived | **Cloud frontier** | Quality matters most; feed it redacted inputs |

**Pattern: "redact local, reason cloud."** Local model strips/derives from raw PII; only sanitized, minimized data ever reaches a cloud model. Best of both — strongest residency on the raw data, best quality on the hard reasoning.

## Takeaways
- The video's real gift to hireui is **not** cost — it's **data-residency**: local inference = candidate PII never leaves the machine.
- For high-risk-employment AI, that turns a compliance *liability* (third-party processing of PII) into an internal, auditable control.
- Design **hybrid, tiered by sensitivity** behind the Match-Explain seam: **redact local, reason cloud**.
- This is the strongest reason for the operator to pilot the stack — see pilot methods **A3** and **B1/B2** in the [../../output/(C) 2026-07-11-local-ai-coding-pilot-menu.md](../../output/(C)%202026-07-11-local-ai-coding-pilot-menu.md).

## See also
[[qwen3.6-27b]] · [[hardware-economics-and-tco]] · [[../miai-cv-matching-agent/_index|miai-cv-matching-agent]] · [[../agent-memory-architecture/_index|agent-memory-architecture (data-residency ADR)]] · [[../cowork-third-party-inference/_index|cowork-third-party-inference (local+private)]]
