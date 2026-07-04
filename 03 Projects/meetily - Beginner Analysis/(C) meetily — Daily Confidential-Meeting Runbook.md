# (C) meetily — Daily Confidential-Meeting Runbook

*v196 pilot · 2026-07-04 · the C11 → C13 → E21 path from the Pilot Methods Menu, made operational · Claude-authored (`(C)`); all facts source-verified at commit `0281737`*

> **Goal:** use your already-installed, fully-local meetily (Ollama, no cloud key) as a **daily private notetaker for confidential meetings** — coaching sessions, client 1:1s, sensitive standups. Nothing leaves your Mac. This runbook + the two templates in `pilot-templates/` are the "make the tool" part.
>
> ⚠️ **I can't drive your machine from here** — this vault session runs in a sandbox, not your laptop. Every step below is a *you-do-this-on-your-Mac* instruction. Where I state a path or behavior, it's read from meetily's source, not from your install.

---

## 0. One-time setup (≈10 min)

**a. Start Ollama + pull a summary model.** meetily's summary step calls Ollama at `http://localhost:11434` by default (verified: `summary/llm_client.rs:167`), so Ollama must be *running*:

```bash
ollama serve            # leave running (or it runs as a background service)
ollama pull qwen2.5:7b  # VN-friendly; OR llama3.1:8b for a general default
ollama list             # confirm the model is present
```

Pick a model that fits your RAM (7–8B needs ~6–8 GB free). `qwen2.5` handles Vietnamese noticeably better than Llama; use it if your meetings are VN or mixed VN-EN.

**b. Install the two confidential templates.** Copy the two files from this folder's `pilot-templates/` into meetily's **custom-template directory** — a *free Community-Edition* mechanism (verified: `summary/templates/loader.rs:25-30`, custom-first precedence):

```bash
mkdir -p ~/Library/Application\ Support/Meetily/templates
cp "/Users/Cvtot/KJ OS Template/03 Projects/meetily - Beginner Analysis/pilot-templates/"*.json \
   ~/Library/Application\ Support/Meetily/templates/
```

Restart meetily → they appear in the template picker as **"Confidential Session"** and **"Coaching 1:1"** (alongside the built-in Daily Standup / Standard Meeting).

> **Naming waiver (like the v189 loop-file waiver):** the template files keep clean machine-read names (`confidential_session.json`, `coaching_1on1.json`) — no `(C)` prefix — because the filename *is* the template ID meetily loads. They're Claude-authored; provenance is recorded here.

**c. Turn analytics OFF (confirm it's off).** It's opt-in default-OFF (verified: `AnalyticsProvider.tsx:41-57`), but check Settings → Analytics is disabled. For confidential work, leave it off.

**d. Turn on FileVault** (macOS disk encryption) if it isn't already — meetily stores recordings + transcripts + summaries as **plaintext in a local SQLite DB** under `~/Library/Application Support/Meetily/`. Local ≠ encrypted; FileVault closes that gap for a lost/stolen laptop.

---

## 1. Choose the transcription engine — the Vietnamese rule ⚠️

- **Vietnamese or mixed VN-EN meetings → use Whisper**, not Parakeet. Whisper is broadly multilingual (Vietnamese included). **NVIDIA Parakeet TDT 0.6b v3 is a ~25-*European*-language model — Vietnamese is not in that set.** Verify in meetily's model picker before a real VN session; if Parakeet gives garbage on Vietnamese, that's why — switch to Whisper.
- **English-only meetings → Parakeet is fine** (README claims ~4× faster than Whisper Large-V3; page-stated) and lighter.
- The summary language follows the transcript: meetily detects language via `whatlang` (Vietnamese supported) and can produce the summary in Vietnamese or translate it (it caches the English summary and translates on demand, so switching languages is cheap).

---

## 2. The Bluetooth gotcha — read before your first recording ⚠️

meetily ships a 235-line `BLUETOOTH_PLAYBACK_NOTICE.md` documenting a real macOS bug: it records at 48 kHz but Bluetooth devices negotiate lower rates, and macOS mis-resamples at the CoreAudio↔Bluetooth handoff. Symptom: playback sounds **1.5–3× too fast** on some BT headphones (Sony WH-1000XM4 named as bad; AirPods Pro usually OK).

**Safe rule for recording confidential meetings:** don't route audio through Bluetooth headphones while capturing — use the **built-in mic + built-in speakers**, or a **wired** headset. If you must use BT, do a 30-second test recording first and play it back to check the speed before you rely on it for a real session.

---

## 3. Record a real meeting (the C13 / E21 loop)

1. Open meetily → **New meeting** → pick a template (**Confidential Session** for a client/coaching call, **Coaching 1:1** for a 1:1, **Retrospective** / **Daily Standup** for ceremonies).
2. Select the **mic** (built-in / wired) and **system audio** device. meetily mixes both (mic + what your Mac plays) so it captures a video call's other side too — no bot joins the call.
3. Hit record. A live transcript appears; VAD sends only speech to the STT engine.
4. Stop → meetily runs the local summary (Ollama) into the template's sections. Review + edit the BlockNote rich-text notes.
5. The meeting, transcript, and summary are saved to the local SQLite DB. **Nothing was uploaded** (only local Ollama touched the transcript).

**First real run = your pilot's proof.** Do it on a low-stakes meeting first (a standup or an internal sync), not your most sensitive client call — confirm the loop end-to-end before you trust it with the confidential ones.

---

## 4. Daily habit + confidential-data hygiene

- **Daily:** one meeting → one template → one reviewed summary. Consistency is the pilot.
- **Retention:** decide a delete cadence for sensitive sessions (e.g. delete the raw recording after the summary is reviewed; keep only the summary). meetily stores everything locally, so *you* own retention — use it.
- **Redaction:** the Confidential Session template is written to *paraphrase* sensitive detail rather than quote it — but the raw **transcript** still holds verbatim speech. If you export or share a summary, share the summary, never the transcript.
- **Backups:** if Time Machine or a cloud backup covers `~/Library/Application Support/`, your confidential recordings are in that backup — check whether that's acceptable, or exclude the Meetily folder.

---

## 5. Graduation bar (L1 personal-trial → daily-driver)

Borrowing the loop-engineering L1→L2 discipline for a personal tool — don't declare it your daily notetaker until:

- [ ] **≥ 3 real meetings** recorded end-to-end, fully local, zero errors.
- [ ] Transcription accuracy is **usable** on *your* accent / VN-EN mix (Whisper for VN confirmed).
- [ ] The summary template output is **good enough to act on** without heavy rewriting.
- [ ] The Bluetooth speed issue is **ruled out** (test recording checked) or you've settled on built-in/wired.
- [ ] Retention + FileVault decided.

Track it in **`(C) meetily — Pilot Log.md`** (this folder). Promote to daily-driver only when all five are checked.

---

## Fence (carried from the wiki)

install-snapshot was done at install · run fully-local (Ollama, no cloud key — already your setup) · keep analytics opt-in-off · no published checksum for the .dmg → you trusted the Gatekeeper signature · the auto-updater points at the old `meeting-minutes` repo name (a staleness note — updates may lag) · meetily ships **no MCP server**, so it can't feed a Claude Code loop natively (that's fine for personal note-taking; if you ever want agent-queryable meeting history, the peer is Hyprnote/Anarlog). Pin your installed version; don't auto-accept a major update mid-pilot.
