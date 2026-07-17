# Autopilot loop — 2026-07-17-13 (interactive)

- **Trigger:** operator-submitted anchor URL (interactive `/loop`-style burst; not the nightly queue — queue empty).
- **Topic:** NEW — `aws-email-at-scale-sqs-lambda-ses`
- **Source:** https://www.youtube.com/watch?v=HnQ0Wt6YyO0 — Tips Javascript (@anonystick), "Show dự án với cách mà các công ty lớn gửi hàng triệu email | AWS SQS, Lambda & SES" (2026-07-15, 16:13, ~1.3K views, VN, category People & Blogs).
- **Ingest path:** 5 (yt-dlp `vi-orig` Vietnamese auto-subs → `.venv/bin/python` `vtt-to-md.py` → 430 cue lines / 35 timestamped paragraphs → read in full in main loop; `notebook_id: none`).

## Pre-flight (Rule 1 — think before ingesting)

- **Theme call:** metadata pull → a Vietnamese backend/cloud-architecture tutorial on AWS message-queue email infrastructure. **On-corpus** (software engineering / cloud infra) — unlike the Pokémon case, **no confirmation gate needed**; proceeded directly. Framing set as the corpus' first cloud-infrastructure / transactional-email-at-scale topic + first Solution-Architect-framed subject, tied to hireui's transactional-email need.
- **Clean tree:** prior topic `pokesynergy-niche-business-tool` was already committed (`cc51330`); working tree clean before this ingest.

## What ran

1. `yt-dlp` metadata + `--list-subs` → `vi-orig` (Vietnamese original) track → `vtt-to-md.py` clean transcript (venv python; broken `python3` shim routed to `.venv`).
2. Full VN transcript read in main loop → architecture + claims understood (I read Vietnamese natively; skipped double-lossy auto-translation).
3. **Independent collision check** (grep `_master-index.md` + `_inventory.md`): no prior AWS/SQS/SES/SNS/Lambda/queue/email topic (matches were false positives — pokesynergy "Tool Solves", api-security/archon merely *reference* AWS docs). No "Tips Javascript" creator. → **corpus-first**. Verified myself, not via agent (wiki-verify discipline).
4. **Main-loop anchors (Opus, before the workflow):** 5 WebSearch checks — SES sandbox/quotas, SES throttling/`ThrottlingException`, SQS pricing, throttle-location semantics, bounce/complaint suspension thresholds. All corroborated + sharpened the claims.
5. **Verification + synthesis Workflow `wf_d65df574-01a`** — 11 agents (6 dives [SES/SQS/SNS+events/architecture/creator/landscape] + 3 refute-first verifiers over 14 claims + 2 synthesizers [corrected playbook + hireui translation & completeness critic]); ~702K tokens, 133 tool calls, **0 errors / 0 empty / 0 skipped**; dives Haiku 4.5, verify+synth Opus 4.8 high-effort. Duration ~5.2 min.
6. **Independent creator confirmation** (WebSearch): Tips Javascript = @anonystick (anonystick.com / github.com/anonystick / TRYBUY NestJS+AWS project). Identity held to the handle (no real name).
7. Main-loop synthesis of 11 wiki files + 1 pilot deliverable; folded in every correction; excluded 3 agent embellishments.

## Verification result

- **Scorecard (14 claims): 7 CONFIRMED · 4 CORRECT-BUT-INCOMPLETE · 2 MISLEADING · 1 OVERSIMPLIFIED · 0 FALSE · 0 FABRICATED** — technically honest talk; softness is over-claim/omission, not fabrication.
- **Both my main-loop anchors and the workflow verifiers independently flagged the same two MISLEADING items** (SQS-throttles-for-you; fixed quota tiers) — strong agreement.
- **Headline finding:** "SQS handles the 14/sec rate-limiting for you" is MISLEADING — SQS is a buffer with no downstream rate awareness; the **consumer** (Lambda concurrency + batch size + limiter) enforces the SES cap. The one place a junior following the video verbatim ships a bug.
- **Sharpened numbers** the video left vague: bounce **>5% = under review, >10% = sending paused**; complaint **>0.1%**; SQS **$0.40/M** Standard; SES sandbox **200/day @ 1/sec**.

## Rule-12 / wiki-verify (fail-loud)

- ⚠️ **Excluded a fabricated "self-correction":** an agent claimed the host said "nope, 86400 giây" on camera after the "60×60×60" misspeak. Transcript `[06:15]` shows no explicit self-correction — described accurately as a misspeak.
- ⚠️ **Discarded a strawman "correction":** the landscape agent invented a video claim ("inline send is fine because email is fast") to correct — the host said the **opposite**. Not incorporated.
- ⚠️ **Creator PII held to the handle:** the creator agent (correctly, refute-first) found only @anonystick and refused a real name; wiki asserts only the handle. Caption "Anistic"/"Tip" = garble of the handle.
- ⚠️ No `vNNN` version artifacts injected this ship (flagged as a recurring synthesis-agent artifact from prior ships; watched, none found).

## Metric Δ

- **Topics:** 63 → **64** (+1 NEW).
- **Scope this cycle:** 1/1 sources compiled = **100%**.
- **Files added:** 11 wiki files (`wiki/aws-email-at-scale-sqs-lambda-ses/`) + 1 raw transcript + 1 pilot deliverable (`output/`) + 1 inventory row + this loop-log.
- **Corpus firsts:** first AWS topic; first message-queue / cloud-infrastructure topic; first transactional-email-at-scale subject; first Solution-Architect-framed whiteboard-design talk; first @anonystick creator.

## Librarian bookkeeping

- ✅ `wiki/_master-index.md` — new entry added (newest-first, above pokesynergy).
- ✅ topic `_index.md` — created (11-file listing).
- ✅ `raw/_inventory.md` — row appended at top of data rows (Status: compiled). **NOTE:** inventory still lags `_master-index.md` — my row sits directly above the okf (2026-07-15) row because pokesynergy / data-structures / quanit / adaptive-engineering / okf-successors were never back-filled (pre-existing gap flagged in the pokesynergy loop log). My row is correct; the lag is unchanged and still needs a reconciliation pass.
- ✅ `[[wiki links]]` — cross-links throughout (fullstack-docker-cicd / api-security-7-techniques / hoidanit-fullstack-vibe-coding / mosh-ai-powered-apps).

## Flags

- **Coverage gap (pre-existing, NOT fixed):** `raw/_inventory.md` lags `wiki/_master-index.md` by ~11 topics (pokesynergy / data-structures / quanit / okf / adaptive-engineering / pocock-writing-great-skills / miai-iphone-ocr-server / codesistency / etc.). Out of scope this ship — flag for an inventory-reconciliation pass.
- **Filename staleness (pre-existing):** `_state/03a-projects-v48-v55.md` naming (Storm-Bear-root state, not this project) — unrelated, noted for the root refactor cycle.
- **No git commit made for this topic** — staged in the working tree on branch `autopilot-research`, left for operator review/commit per harness policy.

## Next action

- Operator: review the 11 files (start at `wiki/aws-email-at-scale-sqs-lambda-ses/_index.md` → `the-throttling-correction.md` [the headline] + `hireui-translation.md`), then commit (suggested: `autopilot-research: NEW topic aws-email-at-scale-sqs-lambda-ses`). Sharpest deployable takeaway = decide **build-vs-buy (managed ESP vs SES)** then ship **A1 "Email Outbox v1"** in the pilot-methods file. Optional: run the inventory-reconciliation pass to clear the ~11-topic lag.
