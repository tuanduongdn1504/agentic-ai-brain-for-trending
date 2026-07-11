# Receipt Scanning with Claude Vision — Correct Implementation + Cost Arithmetic

> Main-loop takeover article (the workflow's vision dive died on context overflow); facts grounded in the claude-api skill (cached 2026-06-24) + Anthropic docs.

## What the video does
Photograph a receipt in the Expo app → Claude API parses vendor/total/tax/category → row lands in Supabase → dashboards update. The mechanism shown (it works on camera) but never architected: which model, what schema enforcement, where the key lives, what it costs.

## The correct implementation shape

1. **Image input**: `{"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": ...}}` content block ahead of the instruction text. (PDFs of receipts: `document` blocks.)
2. **Structured outputs, not prose-parsing**: use `client.messages.parse()` with a Pydantic/Zod schema, or `output_config: {format: {type: "json_schema", schema: ...}}` — guarantees valid JSON for `{vendor, date, total, tax, currency, category, line_items[]}`. Never regex Claude's prose. (Same lesson as the Mì AI pass, where the serving path bypassed its own validation layer — [[external|Storm Bear: miai-cv-matching-agent]].)
3. **Key stays server-side**: the Expo client posts the photo to a Next.js API route / Supabase Edge Function; only that server code holds `ANTHROPIC_API_KEY` → [[api-key-handling-in-mobile-apps]].
4. **Batch for backfills**: bulk-importing historical receipts belongs on the Batches API (50% price, ≤24h turnaround).

## Cost arithmetic (per receipt)

Assumptions: receipt photo downsampled to ≤1568px long edge ≈ ~1,600 image tokens (Opus 4.7+ accepts up to 2576px ≈ ~4,784 tokens — unnecessary fidelity for receipts; downsample client-side); ~150 tokens of instruction; ~300 output tokens of JSON.

| Model | Input $/MTok | Output $/MTok | ≈ cost/receipt | 1,000 receipts/mo |
|---|---|---|---|---|
| Haiku 4.5 | $1 | $5 | **~$0.003** | ~$3.30 |
| Sonnet 5 (intro $2/$10) | $2 | $10 | ~$0.007 | ~$6.60 |
| Sonnet 5 (list $3/$15) | $3 | $15 | ~$0.010 | ~$9.90 |
| Opus 4.8 | $5 | $25 | ~$0.016 | ~$16.30 |

- **Unit economics strongly favor the app**: at a typical $9.99/mo subscription, even Opus-tier scanning of 100 receipts/user/mo costs ~$1.60 — and Haiku-tier ~$0.33. Receipt extraction is a Haiku-class task (typed layout, bounded schema); reserve Sonnet/Opus for ambiguous/handwritten receipts via a confidence-based escalation ladder.
- Mirrors the corpus' recurring finding (Mì AI: ~$0.00134/CV): **document-extraction LLM cost is a rounding error**; the real costs are engineering and distribution.
- The video uses "some credits I have already" and never totals the build's API spend — for the record, a build session of this size plus a handful of scans is low-single-digit dollars of API credits (plus the Claude subscription for Code/Design).

## Accuracy discipline the video skips
- No eval set: collect N real receipts (crumpled, thermal-faded, non-English) + labeled ground truth; measure field-level extraction accuracy before/after prompt changes ([[external|Storm Bear: prompt-evaluation]], [[external|Storm Bear: ai-engineering]] Ch.3–4).
- Privacy: receipts are **financial documents** — data-retention posture, PII handling, and (for EU users) GDPR grounds needed before launch; nothing in the video addresses it.

## hireui mapping
Receipt→structured-row is the same pattern as **CV/resume→structured-profile**: image/PDF in, schema-validated JSON out, server-side key, Haiku-first with escalation, eval set before shipping. This article + [[external|Storm Bear: miai-cv-matching-agent]] jointly specify hireui's document-parsing seam.

## Key Takeaways
- Vision + structured outputs + server-side key is the entire correct architecture; everything else is plumbing.
- Haiku 4.5 is the right default for typed-document extraction; escalate on low confidence.
- Cost is negligible; evals and privacy are the actual work.
