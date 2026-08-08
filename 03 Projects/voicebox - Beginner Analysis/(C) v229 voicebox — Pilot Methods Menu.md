# (C) v229 voicebox — Pilot Methods Menu

> **Honest framing:** voicebox's *domain* (voice cloning / TTS / dictation) is **off both goals**. The on-goal value is (1) the **product-first-MCP-retrofit architecture** as a hireui-agent-nativity template, and (2) a genuinely useful **personal** tool (local dictation for the operator + giving the vault's own Claude Code a voice). It is **NOT a hireui component** — a recruitment SaaS does not need voice cloning, and the "no consent lock" makes candidate/interviewer voice cloning a legal/deepfake minefield. This menu is mostly read / borrow / fence, not a padded 24.
>
> **⭐ One-thing path: A1 → B5 → (optional) C11.**

---

## A — Read & learn (zero install, zero risk)

- **A1 ⭐ — Read the MCP-retrofit design.** Read the v0.5.0 MCP section: FastMCP at `/mcp` (HTTP + stdio) + the `voicebox-mcp` stdio shim + the 4-tool surface (`voicebox.speak` / `voicebox.transcribe` / `voicebox.list_captures` / `voicebox.list_profiles`) + "optional personality rewriting via the local LLM." This is the **third** worked example of "a human product exposing itself TO a coding agent via its own first-party MCP server" (palmier-pro v192 `ToolExecutor` 51 tools / tabularis v212 read-only-gated 4 tools / voicebox 4 tools + a stdio shim).
- **A2 — Read the 7-engine + multi-backend orchestration** (MLX vs PyTorch routing; one shared local Qwen3 LLM for dictation-refine/personality/Compose) as a reference for how to abstract many upstream models behind one local runtime.
- **A3 — Read it as the local-first counter-example to the cloud speech tools** (ElevenLabs output / Wispr Flow input) — the "keep the data on-device" architecture that also anchors meetily v196 (on-device Whisper).

## B — Borrow patterns (zero install)

- **B5 ⭐ — Add voicebox as the 3rd data-point in hireui's agent-nativity / first-party-MCP spec.** When hireui eventually ships its own MCP server (the palmier-pro v192 template thread), voicebox's design reinforces: a **small, well-scoped tool surface** (4 verbs, not 51) + a **stdio shim** for stdio-only clients + **local-first so data never egresses**. Compose with palmier `ToolExecutor` + tabularis's **read-only mode + approval gates + pre-flight EXPLAIN** (the safer surface for a data-touching product).
- **B6 — Borrow the "one LLM, one model cache, one GPU footprint" discipline** for any hireui local-model path (dictation-refine style helpers) — a clean local-LLM-resource pattern.
- **B7 — File the corpus finding** (the v192 §C standalone N=2→3; the promotion-to-CONFIRMED now-eligible flag) for the next audit — a genuine corpus-structural payoff (F, below).

## C — Hands-on, personal (install-snapshot first; off-goal but real)

- **C11 ⭐ — Run it as your own local dictation tool + give the vault's own Claude Code a voice.** `install-snapshot` → install the DMG (macOS) or `just setup`/`just dev` from a pinned clone → enable the MCP server → register it in your own Claude Code so `voicebox.speak` reads results aloud in a preset voice. A genuinely fun, low-risk *personal* pilot (your machine, your data, local-only). Fence below.
- **C12 — Try the dictation hotkey** for drafting vault notes / journal entries (Whisper local, auto-paste) as a Wispr-Flow replacement.
- **C13 — Bench it against the corpus's other speech subjects** conceptually (meetily v196 on-device Whisper STT; fish-speech v20 TTS) to sharpen the "local speech stack" map.

## D — hireui / Goal-#2 (ARCHITECTURE ONLY — do NOT productize voice cloning)

- **D14 ⚠️ FENCE — hireui MUST NOT clone candidate or interviewer voices.** The "no consent lock" is a legal/consent/deepfake risk; recruitment is exactly the domain where synthetic-voice misuse is most dangerous. If a voice feature is *ever* built into hireui, use **preset voices + explicit, logged consent only**, behind the RATIFIED candidate-LLM-legibility ADR + a data-residency review.
- **D15 — Borrow the local-first / on-device-processing posture** (not the product) into hireui's data-residency ADR — the "redact/process local, reason cloud" thread (meetily v196 / local-AI-coding-agents), for any future candidate-audio handling.

## E — Off-goal / personal (optional)

- **E16 — Study Spacedrive-lineage engineering** (Jamie Pine's Rust/Tauri craft) as a general OSS-quality reference; off both goals.

## F — Vault-meta

- **F17 ⭐ — Flag the v192 §C promotion for the next audit.** Voicebox is the genuinely-independent non-port **N=3** of the palmier-pro v192 standalone → the v212-audit's promotion trigger is now SATISFIED → the next audit should **promote "Product-First Native Application Retrofitted with a First-Party MCP Server" to a CONFIRMED Library-vocab item (#12)** unless it finds a reason not to (counts 46/11 → 46/12 is the audit's act). Record the row N=2→3 now.
- **F18 — Record voicebox in the speech/voice-cluster synthesis** (fish-speech v20 TTS-model / meetily v196 on-device-STT / video-use v198 ASR-dependency / AIRI v210 agent-voice / **voicebox v229 all-in-one voice-cloning studio + agent-voice-via-MCP**) — the corpus's ~5th speech subject + FIRST voice-cloning studio.

---

## Fence (mandatory for any install/run)

- `install-snapshot` **before** installing; inspect `just setup` / the DMG-MSI installer (NOT source-cloned → treat as untrusted-until-inspected).
- It **downloads large third-party models** (Qwen3-TTS / Whisper / Kokoro / Chatterbox / HumeAI-TADA / Qwen3 LLM) — verify sources; expect multi-GB.
- **Local-first is a positive** — the user's own audio/models/captures stay on the machine. Keep it that way (no cloud egress).
- ⚠️ **NEVER clone a real person's voice without explicit consent** — the "no consent lock" is a legal/ethical fence, not a feature to exploit.
- **hireui:** architecture-borrow ONLY; never a hireui voice-cloning feature; per hireui's CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first).
- Pin **v0.5.0** (or the commit you install); the CHANGELOG may lag the repo.
