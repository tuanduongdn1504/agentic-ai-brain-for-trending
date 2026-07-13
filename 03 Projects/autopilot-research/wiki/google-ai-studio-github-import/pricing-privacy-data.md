# Pricing, privacy & data residency — the decisive hireui section

> The video never mentions any of this. For a recruitment SaaS handling candidate PII, **this page is the whole ballgame.** Verify against Google's own [Terms](https://ai.google.dev/terms) and [pricing](https://ai.google.dev/pricing) before touching AI Studio with anything real.

## 1. The genuinely-free (unpaid) tier TRAINS on your inputs

Google's Gemini API / AI Studio terms for the **Unpaid Services**:
- *"Google uses the content you submit to the Services and any generated responses to provide, improve, and develop Google products and services and machine learning technologies."*
- *"Human reviewers may read, annotate, and process your API input and output."*
- Explicit warning (buried in the ToS): **"Do not submit sensitive, confidential, or personal information to the Unpaid Services."**

⇒ Anything you put through the free tier — a repo, a CV, a prompt — **may train Google's models and be read by a human.**

## 2. The nuance the verification pass surfaced: "billing-attached = paid classification"

AI Studio accessed through a **Cloud Project with an active billing account** is classified as a **Paid Service**, and Google **does NOT** use paid prompts/responses "to improve our products" — **even if your usage stays within free quotas.** The training-by-default policy applies to the *genuinely unpaid* service (no billing account).

- **Regional carve-out:** for **EEA / Switzerland / UK** users, paid-service data protections apply to **all** tiers, including free.
- **Precise operator rule:** *"free tier"* in the video means the **no-billing** path → trains on you. **Attach a billing account** to get the no-training paid classification. When in doubt, assume training and keep PII out.

## 3. Paid ≠ data residency (the part most people miss)

The paid tier stops **training**, but it does **not** guarantee **where your data lives**:
- Gemini API docs: *"Prompts might be processed at any Google Cloud data center."*
- Binding **data-residency / ZDR-equivalent** terms exist only via **Vertex AI enterprise** with a negotiated **Data Processing Addendum** (contact Google Cloud sales). The standard paid Gemini API does **not** offer configurable regional residency.
- Paid data is still logged briefly for safety/abuse/legal (not training).

## 4. The three-tier map for candidate PII

| Path | Trains on you? | Residency guarantee? | OK for candidate PII? |
|---|---|---|---|
| AI Studio / Gemini **free** (no billing) | **Yes** + human review | No | **❌ Never** (ToS-forbidden) |
| Gemini API **paid** (billing attached) | No | **No** (any GCP DC) | ⚠️ Only if residency isn't required |
| **Vertex AI** enterprise + DPA/ZDR | No | **Yes** (negotiated) | ✅ With signed DPA |
| **Managed Agents** (preview) | n/a | No (preview) | **❌ Pre-GA forbids PII** ([[managed-agents]]) |

## 5. The safe boundary for hireui (the rule to write down)

- **Prototyping / design / code exploration** → OK on a **billing-attached** account with **synthetic data only** (no real candidate PII, no secrets, ideally not the proprietary production repo).
- **Any candidate PII in production** → **only** Vertex AI enterprise with a signed DPA + residency, *or* keep it off Google entirely and use the hybrid **"redact local, reason cloud"** pattern from [[../local-ai-coding-agents/privacy-data-residency|local-ai]] behind the [[../mosh-ai-powered-apps/_index|Mosh A2 seam]].
- **Code-enforce it:** the free tier is one careless prompt away from egressing a candidate's data into Google's training set. Put this in the CONSTITUTION (pilot **D1/D2**) so a junior following the video literally can't do it.

## The residency spectrum (corpus lens)

This topic sits at the **weakest** end of a spectrum the corpus has now mapped end-to-end:

`local inference (strongest — nothing egresses)` → `Vertex AI + DPA` → `paid Gemini API (no residency)` → **`AI Studio free tier (trains + human-review — weakest)`**

Same lens as [[../local-ai-coding-agents/privacy-data-residency|local-ai-coding-agents]], opposite pole.

## See also
[[_index]] · [[managed-agents]] · [[cloud-run-deploy]] · [[../local-ai-coding-agents/privacy-data-residency|local-ai: data residency]]
