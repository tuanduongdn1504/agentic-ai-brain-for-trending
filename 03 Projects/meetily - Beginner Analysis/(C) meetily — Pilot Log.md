# (C) meetily — Pilot Log

*v196 personal quick-win pilot (C11 → C13 → E21) · started 2026-07-04 · Claude-authored scaffold; you fill the run rows*

> **Pilot:** meetily as a daily private notetaker for confidential meetings, fully-local (Ollama, no cloud key). Setup + record + daily-use runbook: **`(C) meetily — Daily Confidential-Meeting Runbook.md`**. Templates: **`pilot-templates/`**. This log tracks the L1 personal-trial toward daily-driver (the graduation bar is in the runbook §5).

## Status

- **Phase:** L1 personal trial (not yet daily-driver).
- **Install:** ✅ done on the operator's Mac — fully-local, Ollama, no cloud key (operator-confirmed 2026-07-04).
- **Tooling shipped this session:** 2 validated custom templates (`confidential_session`, `coaching_1on1`) + the runbook.
- **⚠️ Environment note:** the vault session that built this cannot see/drive the operator's laptop (sandbox); all runs below are logged by the operator.

## Setup checklist (do once — from the runbook §0)

- [x] **Templates installed** — all 3 (`confidential_session`, `coaching_1on1`, `bien_ban_chi_bo`) copied into `~/Library/Application Support/Meetily/templates/` on 2026-07-04; jq-verified as valid JSON with correct display names. ⚠️ Verify they show in meetily's picker after a restart (the `.app` binary wasn't visible to the sandbox that installed them — the files are in the right home-dir path, but confirm the app reads them).
- [x] **`ollama serve` running + a VN-capable model present** — `qwen3.5:latest` (6.6 GB) confirmed pulled 2026-07-04 (a Qwen model; handles Vietnamese well). Good enough for the biên bản; no need to pull `qwen2.5`/`llama3.1` unless you want to compare.
- [ ] Analytics confirmed OFF (Settings)
- [ ] FileVault ON (local SQLite holds plaintext transcripts)
- [ ] Bluetooth speed test done (or committed to built-in/wired mic)
- [ ] Vietnamese → Whisper selected (not Parakeet) — **required for the chi bộ meeting**

## Dry-run validation — SYNTHETIC (2026-07-04, not a real meeting)

Before any real meeting, I ran a **fake sample chi bộ Đông Trà 1 transcript** (a full monthly-meeting script with attendance, 2 nội dung, 2 ý kiến, giải trình, biểu quyết 100%, closing time) through the `bien_ban_chi_bo` template's prompt on the installed **`qwen3.5:latest`** model, twice. This validates the summary quality *before* trusting it on a real Party meeting. **Findings — the template is good; the MODEL is the risk:**

- **Run A (qwen3.5, default):** ❌ FAILED — went into a degenerate reasoning loop ("Wait… Okay… Wait…" for 480+ lines), hallucinated facts mid-thought (said "6 thành viên", "Thư ký Trần Văn B" — both wrong), and **never emitted a final biên bản.**
- **Run B (qwen3.5, `/no_think` in prompt):** ⚠️ COMPLETED but qwen3.5 **ignored `/no_think`** (still emitted 250 lines of thinking) and, critically, **fabricated the two content sections:**
  - ✅ Structure, headers, Vietnamese — perfect.
  - ✅ Thông tin cuộc họp + Thành phần (15 ĐV / 13 có mặt / vắng-lý-do / Chủ trì Nguyễn Văn A / Thư ký Hoàng Thị E) + Kết thúc (20:45) — **all extracted correctly.**
  - ⚠️ Nội dung — right topics, but stripped of detail.
  - ❌ **Ý kiến đóng góp — fully hallucinated** (invented "phát triển đảng viên mới / thu hút đoàn viên thanh niên"; the transcript said *tuyên truyền phòng chống dịch* + *lấy ý kiến rộng rãi về báo cáo chính trị*).
  - ❌ **Giải trình của chủ trì — fully hallucinated** (invented Party boilerplate contradicting the transcript).

**Conclusion / model recommendation (BLUNT):** the `bien_ban_chi_bo` template works — factual fields extract cleanly — but **qwen3.5 is NOT trustworthy for the biên bản content sections; it drifts into generic Party-meeting boilerplate and fabricates ý kiến + giải trình.** For a Party-cell record where fidelity is procedurally critical, that is disqualifying **unless every summary is cross-checked against the transcript before use.** Before the real meeting: (1) try a **non-reasoning model** — `qwen2.5:7b` or larger (`qwen2.5:14b`/`32b` if RAM allows), or `llama3.1:8b` — which won't have the thinking-drift; (2) always keep + review the full transcript (meetily stores it); (3) a real, longer meeting *may* ground the model better than this terse synthetic script, but treat the ý kiến/giải trình sections as draft-to-verify, never final. Raw dry-run outputs: this session's scratchpad (`dryrun_output.md` = run A, `dryrun2_output.md` = run B); not committed (synthetic/throwaway).

## Gemini trial (Cách 1 — Custom OpenAI → Gemini direct) — started 2026-07-05

Operator elected to trial cloud Gemini for higher summary quality (vs the local qwen3.5 that fabricated). Setup path + verification:

- **Provider:** meetily → Settings → Custom (OpenAI-compatible).
  - **Base URL:** `https://generativelanguage.googleapis.com/v1beta/openai` (meetily auto-appends `/chat/completions` — verified in `llm_client.rs:177`; do NOT include the suffix).
  - **API key:** operator's Gemini key (from `aistudio.google.com/apikey`). **Enable billing (paid tier)** — free tier lets Google use the data.
  - **Model:** `gemini-2.5-pro` (quality) or `gemini-2.5-flash` (fast/cheap) — confirm current names.
- **URL verified reachable** 2026-07-05 (POST → HTTP 400 not 404 = valid endpoint; a Test-connection failure ⇒ key/model/billing, not URL).
- **Standalone pre-test** (run in Terminal with your key before touching meetily):

  ```bash
  curl https://generativelanguage.googleapis.com/v1beta/openai/chat/completions \
    -H "Authorization: Bearer YOUR_GEMINI_KEY" -H "Content-Type: application/json" \
    -d '{"model":"gemini-2.5-pro","messages":[{"role":"user","content":"Trả lời một câu tiếng Việt."}]}'
  ```

  JSON reply ⇒ key+model+URL all good (meetily will work with the same values). 401/403 ⇒ key/billing. 400 "model not found" ⇒ wrong model name → list models: `curl "https://generativelanguage.googleapis.com/v1beta/models?key=YOUR_KEY"`.
- **Ready-to-run harness** (does the connectivity test + auto-diagnoses HTTP codes + runs the synthetic-transcript fidelity comparison in one command; key via env var, never stored): `~/Documents/test-gemini-meetily.sh` (vault copy in `pilot-templates/`). Run: `GEMINI_KEY=your_key bash ~/Documents/test-gemini-meetily.sh`. Verified working against a bogus key (extracts Google's real error message + points to the cause).

**⚠️ Trial scope fence (non-negotiable):** Gemini = cloud → transcript leaves the machine to Google.
- **NON-sensitive meetings ONLY** (personal, internal coaching). **NEVER chi bộ / mật content** — those stay 100% local (gemma2:27b / qwen2.5-instruct + verify).
- Paid tier (no-training) even for non-sensitive.

**What to measure each trial meeting** (decide keep/drop after ~3–5):

| # | Date | Meeting (non-sensitive) | Model | Fidelity: ý kiến/giải trình invented? | Names/numbers correct? | Edit effort (1=none…5=heavy) | Cost/summary | Keep? |
|---|------|------------------------|-------|----------------------------------------|------------------------|------------------------------|-------------|-------|
| G1 | | | gemini-2.5-pro | | | | | |
| G2 | | | | | | | | |
| G3 | | | | | | | | |

**Decision gate:** keep Gemini if — no fabrication in ý kiến/giải trình across ≥3 meetings AND edit effort ≤2 AND cost acceptable. Otherwise revert to local model + controlled-prompt drafting. **Apples-to-apples anchor:** run the same synthetic chi bộ transcript (the qwen3.5 dry-run one) through Gemini once — if it does NOT fabricate the ý kiến/giải trình sections that qwen3.5 invented, that's the clearest quality signal.

**✅ Synthetic anchor result — 2026-07-05 (`gemini-2.5-flash`, free tier):** PASSED cleanly, verified by hand-reading the full output (`~/Documents/gemini-bienban-test-output.md`), not just the grep. **Zero fabrication** where qwen3.5 fabricated: ý kiến correctly attributed (Trần Văn B → tuyên truyền phòng chống dịch; Vũ Thị F → lấy ý kiến rộng rãi về báo cáo chính trị), giải trình faithful, biểu quyết 100%. All facts correct: 19:30 5/7, nhà đ/c Trần Văn B, 15 ĐV (14 chính thức + 1 dự bị), 13 có mặt / 2 vắng + lý do, Chủ trì Nguyễn Văn A, Thư ký Hoàng Thị E, kết thúc 20:45. It even **preserved the tháng-6 detail qwen3.5 stripped** AND the 14/1 breakdown my own hand-draft dropped. Decisive win over qwen3.5. ⚠️ Caveats: (1) one SYNTHETIC short test — real 2-hour meetings may compress more (flash is small); the ≥3-real-meeting gate still stands. (2) `flash` free-tier ⇒ Google may use the data → only for non-sensitive; for the no-training guarantee (and `2.5-pro` quality on long meetings) enable billing. Net: Gemini is trustworthy enough to proceed to meetily config for non-sensitive meetings; still verify formal records.

## Run log (fill one row per recorded meeting)

| # | Date | Meeting type | Template | STT engine | Lang | Summary model | Usable? (1–5) | Notes / edits needed |
|---|------|--------------|----------|-----------|------|---------------|---------------|----------------------|
| 1 | | (low-stakes first!) | | Whisper | vi | (NOT qwen3.5 — see dry-run) | | verify ý kiến + giải trình against transcript |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

## Graduation bar (from runbook §5 — check when true)

- [ ] ≥ 3 real meetings recorded end-to-end, fully local, zero errors
- [ ] Transcription usable on your accent / VN-EN mix
- [ ] Summary output good enough to act on without heavy rewriting — **⚠️ dry-run flag: qwen3.5 fabricated ý kiến + giải trình; switch to a non-reasoning model + always verify content sections against the transcript**
- [ ] Bluetooth speed issue ruled out (or built-in/wired settled)
- [ ] Retention + FileVault decided

**→ Promote to daily-driver only when all five are checked.** Record the promotion date here: __________

## Open questions to resolve during the trial

1. Does Whisper handle *your* Vietnamese + technical-English code-switching well enough for coaching notes?
2. Is the local model's summary quality (on `qwen2.5:7b` / `llama3.1:8b`) good enough, or do sensitive meetings warrant a bigger local model?
3. What's your retention rule for raw recordings vs summaries?
4. (Off this pilot, on-goal) — does reviewing meetily's `generate_summary()` vendor-seam change how you'll spec **hireui's first LLM feature**? (The B5→D16 path; separate from this personal trial.)
