# (C) meetily — Pilot Log

*v196 personal quick-win pilot (C11 → C13 → E21) · started 2026-07-04 · Claude-authored scaffold; you fill the run rows*

> **Pilot:** meetily as a daily private notetaker for confidential meetings, fully-local (Ollama, no cloud key). Setup + record + daily-use runbook: **`(C) meetily — Daily Confidential-Meeting Runbook.md`**. Templates: **`pilot-templates/`**. This log tracks the L1 personal-trial toward daily-driver (the graduation bar is in the runbook §5).

## Status

- **Phase:** L1 personal trial (not yet daily-driver).
- **Install:** ✅ done on the operator's Mac — fully-local, Ollama, no cloud key (operator-confirmed 2026-07-04).
- **Tooling shipped this session:** 2 validated custom templates (`confidential_session`, `coaching_1on1`) + the runbook.
- **⚠️ Environment note:** the vault session that built this cannot see/drive the operator's laptop (sandbox); all runs below are logged by the operator.

## Setup checklist (do once — from the runbook §0)

- [ ] `ollama serve` running + a model pulled (`qwen2.5:7b` for VN, or `llama3.1:8b`) + `ollama list` confirms it
- [ ] Both templates copied into `~/Library/Application Support/Meetily/templates/` and visible in the picker after restart
- [ ] Analytics confirmed OFF (Settings)
- [ ] FileVault ON (local SQLite holds plaintext transcripts)
- [ ] Bluetooth speed test done (or committed to built-in/wired mic)
- [ ] Vietnamese → Whisper selected (not Parakeet)

## Run log (fill one row per recorded meeting)

| # | Date | Meeting type | Template | STT engine | Lang | Summary model | Usable? (1–5) | Notes / edits needed |
|---|------|--------------|----------|-----------|------|---------------|---------------|----------------------|
| 1 | | (low-stakes first!) | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

## Graduation bar (from runbook §5 — check when true)

- [ ] ≥ 3 real meetings recorded end-to-end, fully local, zero errors
- [ ] Transcription usable on your accent / VN-EN mix
- [ ] Summary output good enough to act on without heavy rewriting
- [ ] Bluetooth speed issue ruled out (or built-in/wired settled)
- [ ] Retention + FileVault decided

**→ Promote to daily-driver only when all five are checked.** Record the promotion date here: __________

## Open questions to resolve during the trial

1. Does Whisper handle *your* Vietnamese + technical-English code-switching well enough for coaching notes?
2. Is the local model's summary quality (on `qwen2.5:7b` / `llama3.1:8b`) good enough, or do sensitive meetings warrant a bigger local model?
3. What's your retention rule for raw recordings vs summaries?
4. (Off this pilot, on-goal) — does reviewing meetily's `generate_summary()` vendor-seam change how you'll spec **hireui's first LLM feature**? (The B5→D16 path; separate from this personal trial.)
