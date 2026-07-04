# (C) meetily — Pilot Methods Menu

*v196 · 2026-07-04 · "show me many methods to apply into my working flow" — 24 methods, laddered A→F by risk/lift*

> **The honest framing.** meetily's payoff for you splits two ways: **(1) the architecture** — its provider-agnostic LLM-client + templated map-reduce summarizer is a near-perfect blueprint for **hireui's first LLM feature**; and **(2) the app itself** — a genuinely private, local, no-cloud meeting notetaker for your **Scrum-coaching standups/retros** and **recruitment interview notes**. The architecture is the on-goal prize; the app is the personal-workflow win. Both are real.
>
> ⭐ **One-thing path: A1 → B5 → D16** — read the vendor-seam, borrow it, build hireui's first LLM feature on it. That is exactly "apply into my working flow."

---

## A — Read + learn (zero install, zero risk)

**A1 ⭐ — Read the provider-agnostic dispatcher.** `frontend/src-tauri/src/summary/llm_client.rs` (346 lines). See how ONE `generate_summary()` fans out to 7 providers: 6 share one OpenAI-chat path (URL + `Bearer` header differ), Claude gets its own `/v1/messages` + `x-api-key` + `anthropic-version` shape, and `BuiltInAI` bails early to a local sidecar. This is the "abstract the 90% shared, special-case the 10% that's truly different" discipline you want for hireui. ~20 min.

**A2 — Read the summarization engine.** `summary/processor.rs` (856 ln). Token-aware chunking (`threshold − 300` overhead, 100-token overlap), single-pass for cloud/short vs 3-pass map-reduce for local/long, English-summary cache-reuse for translations. This is how you summarize a transcript longer than the context window without losing the thread.

**A3 — Read the template system.** `summary/templates/*` + the JSON in `frontend/src-tauri/templates/{standard_meeting,daily_standup,retrospective,project_sync}.json`. A template = `{name, sections:[{title, instruction, format, item_format?}]}` rendered into a prompt. Note `standard_meeting.json`'s action-item table with **transcript-segment references + timestamps**. Adding a format = adding JSON, no code. Same idea as your `05 Skills/` templates.

**A4 — Read the two-path audio pipeline** (`docs/architecture.md` + `CLAUDE.md` audio section) as a pure systems-design case study: one raw stream → two consumers (RMS-ducked recording ‖ VAD-filtered transcription). You'll never touch audio, but "one source, two differently-processed consumers" is a broadly useful shape.

---

## B — Borrow patterns into hireui / the vault (zero-to-low install)

**B5 ⭐ — Steal the vendor-seam as hireui's first-LLM-feature template.** Your `mosh-ai-powered-apps` thread already spec'd "hireui FIRST LLM feature (A2 seam → A1 summarizer → A6 evals)." meetily's `generate_summary()` **is** that A2 seam, source-verified and battle-worn: one dispatcher, provider behind an interface, Claude one option, a cheap/local option for bulk. Copy the *shape*, write hireui's own. **Highest-ROI borrow.**

**B6 — Steal the map-reduce chunking + token budget** for any long-doc summarization in hireui (interview transcripts, candidate dossiers): the "single-pass cloud/short vs multi-level local/long" branch + reserve-overhead + overlap discipline. Don't reinvent it.

**B7 — Steal the template-as-JSON-sections → prompt pattern** for hireui report formats (interview notes, candidate one-pagers, offer summaries). Declarative + versionable; adding a format doesn't touch code. Composes with the ai-berkshire v187 domain-vertical-skill idea.

**B8 — Steal the English-cache-reuse-for-translation pattern** if hireui ever needs multi-language candidate reports: summarize once in English, translate on demand, never regenerate.

**B9 — Steal the content-fingerprint no-op guard** (FNV-1a over the transcript → skip re-summarizing unchanged input). Same pattern as **openwiki v195**'s content-snapshot SHA-256 guard — bank it as a general "don't recompute unchanged input" reflex for your loops.

**B10 — Adopt the provider-parity honesty.** meetily's `provider_name()` + per-provider request shaping is a clean example of *not* over-abstracting: 90% shared, Claude's real differences special-cased. When you build hireui's seam, resist the urge to force Claude into the OpenAI mold.

---

## C — Low-risk hands-on trial (install the app, scratch use)

**C11 ⭐ — Fully-local smoke test.** `install-snapshot` first → grab the **signed** macOS `.dmg` (or build from source, pin `0281737`) → run it with **Ollama + Whisper/Parakeet, NO cloud key** on a throwaway recording → watch the network to confirm nothing leaves the machine. Safest possible first trial; proves the local-first claim with your own eyes.

**C12 — Verify the privacy posture.** On first launch, confirm analytics is **opt-in default-OFF** (it is — gated at `AnalyticsProvider.tsx`, defaults false). Read `PRIVACY_POLICY.md` against what you observe. Leave it off.

**C13 ⭐ — Record a real standup/retro** with the shipped `daily_standup.json` / `retrospective.json` template → judge summary quality on local Ollama vs Claude (BYO-key). This is a **direct Scrum-coaching pilot** — a private, local notetaker for your own ceremonies.

**C14 — Measure token/cost per summary** by pointing the summary step at your Claude key on ONE meeting. Pairs with your `claude-code-observability` (ccusage/OTel) thread. Decide local-vs-Claude for your standups on real numbers.

**C15 — Import an existing interview recording** ("Import & Enhance" beta) → re-transcribe Parakeet vs Whisper → judge accuracy/speed for recruitment interview notes.

---

## D — hireui / Goal-#2 (the recruitment-SaaS payoff)

**D16 ⭐ — Build hireui's first LLM feature on meetily's blueprint.** A candidate-interview-notes summarizer, on an `agent-*` branch (hireui CONSTITUTION I-2), operator-installed (I-8), GitNexus-first. The design = meetily's vendor-seam (B5) + templated summarizer (B6/B7); the code = hireui's own. This is the single completed Goal-#2 artifact this whole thread has been building toward.

**D17 — Prototype a hireui interview-summary template** (JSON sections: Candidate Summary / Strengths / Concerns / Fit Score / Follow-ups + a transcript-reference table), modeled on `standard_meeting.json`'s action-item-with-references section.

**D18 — Compose with the ai-berkshire v187 "AI Hiring Committee."** 4-persona candidate eval → feeds a meetily-style templated summary. Two corpus threads compose into one real hireui feature.

**D19 — Study the data-sovereignty model for hireui's privacy story.** If hireui ever records interviews (candidate PII), meetily's **local-first, no-cloud, no-bot** posture is the GDPR/consent-friendly reference — a compliance blueprint, not code.

**D20 — Wire an eval gate on the summarizer** (the mosh-ai A6-evals + TimesFM v193 backtest-gate thread): a golden set of interview transcripts + expected summary points, gate on quality before shipping. Verify-before-trust.

---

## E — Off-goal personal use (you're also a person)

**E21 — Use it as your actual daily notetaker** for client Scrum-coaching sessions. Local transcription = client-confidential-safe; nothing leaves your Mac. This is the lowest-friction real win.

**E22 — Author your own coaching templates** (retro variants, 1:1 notes, sprint-review) as JSON — the format is trivial and yours forever.

---

## F — Vault-meta / synthesis

**F23 — Write the "provider-agnostic LLM-client patterns across the corpus" note.** meetily `generate_summary()` (dispatcher) + freellmapi v112 (live proxy) + cc-switch v73 (config-switcher) + OpenHuman v118 (routing) + the mosh-ai vendor-seam → one synthesis on how to abstract multi-provider LLM access. Directly feeds hireui's design (D16).

**F24 — Log the watch axis for the overdue ~v192 audit:** meetily = the corpus's FIRST meeting-assistant + 2nd speech-domain subject (after fish-speech v20 TTS); note the emerging **"consumer-app-whose-LLM-architecture-is-the-goal-relevant-part"** tier (GLM-5 v176 / DeepSpec v186 / TimesFM v193 / meetily v196 — off-domain-goal-adjacent).

---

## Fence (mandatory before any install)

- `install-snapshot` first · prefer the **signed** `.dmg` or build-from-source (pin commit `0281737`) · **no published checksum** → verify via Gatekeeper signature.
- **Run fully-local first** (Ollama, no cloud key); only add a BYO cloud key once you trust it.
- Verify analytics stays **opt-in-off**; the PostHog write-key is public (low-risk) but real.
- Treat the auto-updater's `meeting-minutes` endpoint as a **staleness note** (old repo name).
- hireui borrows are **DESIGN-only** per its CONSTITUTION — build hireui's own seam, don't bolt meetily in; `agent-*` branch (I-2), operator-installs (I-8), GitNexus-first; hireui has no LLM spend yet → build-it-right.
- ⚠️ It ships **no MCP server** — you can't wire meetily itself into a Claude Code loop natively (the MCP-exposing peer is **Hyprnote/Anarlog**, if that's ever the requirement).

## Rank

**⭐ Start: A1 → B5 → D16** (the on-goal arc: read → borrow → build hireui's first LLM feature). **Personal quick-win: C11 → C13 → E21** (install local → record a retro → use it daily). Everything else is optional depth.
