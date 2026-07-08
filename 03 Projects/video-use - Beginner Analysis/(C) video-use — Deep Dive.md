# (C) video-use — Deep Dive (LLM Wiki v198)

> Built 2026-07-08. Source: `github.com/browser-use/video-use`, shallow-cloned + **source-verified at commit `92c2b34`** (2026-07-01, a merge of community PR #91). MIT © Browser Use 2026. All code claims below are hand-read or workflow-verified against that clone; every fact-provenance follows routine v2.6 §37 (GitHub metrics are page-stated, NOT API-verified → never a Pattern #52 velocity claim).

---

## 0. One-sentence

**video-use is a free, MIT-licensed Claude-Code (Codex/Hermes/OpenClaw) *agent skill* that edits existing raw footage by conversation — the LLM never watches the video, it *reads* it, through a word-level ASR transcript (primary surface) plus on-demand visual composites — then cuts/grades/subtitles/animates it via ffmpeg and self-evaluates the render before showing you anything.** It is *"browser-use giving an LLM a structured DOM instead of a screenshot — but for video,"* built by the same company (Browser Use, YC W25).

Drop raw takes in a folder → `claude` in that folder → say *"edit these into a launch video"* → get `edit/final.mp4`.

---

## 1. What it is (and is not)

| | |
|---|---|
| **Repo** | `browser-use/video-use` — "Edit videos with coding agents" |
| **What ships** | A `SKILL.md` (the agent's brain) + 6 Python `helpers/` + a vendored `manim-video/` sub-skill + `install.md` + `poster.html` (a diagram of the perception idea) |
| **License** | MIT © Browser Use 2026 |
| **Language** | Python 76% / HTML 23% (poster + timeline SVG) / Shell 1% |
| **Maturity** | No releases, no versioning, git-clone-only; `pyproject` version `0.1.0`; **zero tests, no CI**; actively maintained (community PRs merged through Jul 7 2026) |
| **Stars** | ~15.9k page-stated §37.4 (NOT velocity-verified → not #52) |
| **Author** | Browser Use, Inc. (Magnus Müller + Gregor Zunic `@gregpr07`, YC W25, $17M seed Felicis-led Mar-2025, SF, ~7 employees). **NOT Anthropic.** Main committer `gregpr07` + a `claude` co-author on ~6 commits (built *with* Claude Code — a self-referential data-point, not Anthropic authorship). |

**It IS:** a conversational *editor* of footage you already shot.
**It is NOT:** a video *generator* (contrast OpenMontage v188, which produces a video from a text brief); not a GUI product (contrast Descript); not an MCP server (it's a skill, discovered via `~/.claude/skills/`); not the browser-use browser agent (it's a sibling repo in the same org).

---

## 2. The load-bearing idea — "read the video, don't watch it" (the perception layer)

This is the whole point of the project and its only genuinely novel contribution. The README frames the problem bluntly:

> Naive approach: 30,000 frames × 1,500 tokens = **45M tokens of noise.**
> Video Use: **12KB text + a handful of PNGs.**

Two layers give the LLM word-boundary precision from *text* (verified in `helpers/`):

- **Layer 1 — Audio transcript (always loaded).** One ElevenLabs **Scribe** call per source → word-level timestamps + speaker diarization + audio-event tags (`(laughter)`, `(applause)`). All takes pack into a single ~12KB `takes_packed.md` — the LLM's primary reading view. (`transcribe.py` uses model **`scribe_v1`**, `timestamps_granularity=word`, `diarize=true`, `tag_audio_events=true` — `transcribe.py:65-68`.)
- **Layer 2 — Visual composite (on demand).** `timeline_view.py` renders a filmstrip + waveform + word-labels PNG for a given time range, **called only at decision points** (ambiguous pauses, retake comparison, cut-point sanity) — not as a scan.

> This is exactly browser-use's own thesis (give the LLM a structured accessibility tree, not a screenshot) transplanted to a new modality. Same org, same idea — the corpus-recursive tie to **browser-use v41** is explicit in the README, not inferred.

---

## 3. The pipeline (verified end-to-end)

```
Transcribe ──> Pack ──> LLM Reasons ──> EDL ──> Render ──> Self-Eval
   (Scribe)   (~12KB)  (reads text,   (JSON  (ffmpeg)   (timeline_view on the
              takes_    drills into    cut               RENDERED output at every
              packed.md  timeline_view  list)            cut boundary; issue? fix +
                         at decisions)                    re-render, max 3 passes)
```

- **EDL** = an Edit Decision List (`edl.json`): `{sources, ranges:[{source,start,end,beat,quote,reason}], grade, overlays, subtitles}`. The LLM (or a dedicated editor sub-agent) writes it; `render.py` executes it deterministically.
- **Self-eval loop** (the second genuinely good idea): after rendering, the agent runs `timeline_view` on the *rendered output* at every cut boundary, checks for visual jumps / audio pops / hidden captions / misaligned overlays, and **fixes + re-renders up to 3× before showing you a preview.** A maker/checker discipline baked into a skill.

---

## 4. The render engine (`render.py`, 659 LOC — hand-read + workflow-verified)

Production-grade ffmpeg orchestration. The SKILL.md's "12 Hard Rules" are real code invariants, not aspirations. Verified against source:

| Hard rule | Verified at | Note |
|---|---|---|
| Per-segment extract → lossless `-c copy` concat (not single-pass filtergraph) | `render.py:214-283` | avoids double-encoding overlaid segments |
| 30ms audio fades at every cut (`afade`) | `render.py:188-189` | kills pops |
| Overlays `setpts=PTS-STARTPTS+T/TB` | `render.py:524` | frame-0-lands-at-window-start |
| **Subtitles applied LAST** in the filter chain | `render.py:538-543` | so overlays never hide captions |
| Master SRT = output-timeline offsets (`word.start − seg_start + seg_offset`) | `render.py:360-363` | captions stay aligned after concat |
| grade presets (`warm_cinematic`/`neutral_punch`/`none`) + `--filter` raw, applied per-segment | `grade.py:38-62`, `render.py:183` | ASC-CDL mental model |

**Undocumented behavior the code does but the README/SKILL.md omit** (a genuine "does more than it says" finding — good, not bad):
- **Loudness normalization ON BY DEFAULT** — two-pass `loudnorm` to social-standard −14 LUFS / −1 dBTP / LRA 11 (`render.py:387-490, 643-652`). Only in `--help`, not the docs.
- **HDR→SDR tone-mapping** — auto-detects PQ/HLG (iPhone default) and prepends a `zscale+tonemap` chain (`render.py:95-132`) so 8-bit output isn't blown-out on social re-encodes.
- **Portrait auto-detection** (`render.py:134-146`) — height-scaled output for vertical footage.

---

## 5. Doc-vs-code gaps (documented faithfully — none are bugs, most are the skill's own "worked-example" framing)

| README/SKILL.md says | Code actually does | Read |
|---|---|---|
| `--preview` = "720p fast" | `--preview` is **1080p, `medium`, CRF 22**; the 720p/`ultrafast`/CRF-28 mode is a *separate* `--draft` flag (`render.py:174-196`) | doc lag |
| Subtitle `MarginV=35` (the "bold-overlay" worked example) | code default is **`MarginV=90`** with a 9-line comment explaining it's a mobile-UI safe-zone rule, not taste (`render.py:42-56`) | code is the authority; SKILL.md explicitly says its numbers are "worked examples, not mandates" |
| "Cache transcripts per source … never re-transcribe unless the source changed" | cache is keyed on **filename stem only** — no content hash / mtime (`transcribe.py:104-109`). Re-shoot with the same filename → stale transcript silently reused. | real footgun; rename files or clear `transcripts/` |
| "1/10 the tokens of raw JSON" (~12KB) | `pack_transcripts.py` produces the packed md but **never measures** the ratio | plausible, unverified-in-code |

None of these change the verdict — the SKILL.md's core discipline is "the values are examples; the Hard Rules are law," and the Hard Rules all hold.

---

## 6. The vendored `manim-video/` sub-skill

A self-contained Manim (3Blue1Brown-style animation) skill bundled inside video-use: `SKILL.md` + **14 progressive-disclosure reference files** (`animations.md` 282 ln, `mobjects.md` 333 ln, `equations.md`, `updaters-and-trackers.md` 260 ln, `paper-explainer.md` 255 ln, …) routed by a 7-mode table. **No upstream attribution / no separate license** in the sub-dir (it inherits the repo's MIT; credits Manim Community + names the "3B1B palette" but not Grant Sanderson directly). `scripts/setup.sh` is a 15-line **read-only prerequisite checker** (checks `python3`/`manim`/`pdflatex`/`ffmpeg` via `command -v`; zero network, zero writes, zero risk).

The three durable, tool-agnostic pieces of craft in the references (worth reading even if you never touch Manim):
1. **"Narration first" as a design gate** — write what the narrator says *before* any code; it fixes order, duration, and what must be on screen when each sentence is heard.
2. **Opacity layering for cognitive load** — primary 1.0 / contextual 0.4 / structural (axes) 0.15.
3. **First-render excellence is non-negotiable** — broken kerning is a *failure*, not acceptable output (Manim's Pango renderer → monospace only).

The perception-layer skill (video-use itself) + this animation sub-skill are a clean example of an **agent-skill that vendors a second agent-skill** — the agent-skills-standard v76 / SkillOpt v178 / agent-skills v184 substrate the vault studies.

---

## 7. Cost, privacy, and the ElevenLabs dependency (the one real fence)

- **Transcription cost** — ElevenLabs Scribe v2 batch ≈ **$0.22/hr of audio** (post-June-2026 cut) → **~$0.11 per 30-minute take**; multi-speaker diarization is free. Roughly 5–20× a local Whisper run, but native diarization + word-level timestamps + audio-event tags remove the WhisperX+Pyannote toolchain. Free tier has **no commercial rights**; Scribe needs a paid plan (Starter $6/mo). *(The repo pins `scribe_v1`; ElevenLabs' current product is Scribe v2 — a version lag, but the v1 endpoint still works.)*
- **PRIVACY — the load-bearing fence.** Every source file's audio is uploaded to ElevenLabs. **ElevenLabs retains audio up to ~3 years and, by default, USES uploaded audio to train its models** (opt-out exists but is *future-only* — it doesn't cover already-sent audio; Zero-Retention is enterprise-only). Fine for your own launch/marketing footage. **A genuine problem for anything containing other people's PII — candidate interview recordings especially (GDPR + consent).** See the Pilot Menu's Group D fence.
- The repo itself is **clean of telemetry** — no PostHog/Sentry/analytics; the only tracking is a `utm_` marketing link to Browser Use Cloud in the README. Install is benign: no `curl|bash`, no `npx --yes` at install time (animation engines install lazily per-slot), API key written `chmod 600` to `.env` at the repo root and `.gitignore`'d, never echoed.

---

## 8. Landscape (where it sits — and what precedes it)

- **Descript (2017)** pioneered transcript-based editing ("edit video like a doc," filler removal) + its **Underlord** agent sidebar (Aug 2025). video-use is NOT the first transcript-editor — Descript is the "ripgrep/fzf precede fff as tools" analogue. Difference: Descript = GUI product + sidebar agent; video-use = a coding-agent skill, zero GUI, runs in your IDE/terminal.
- **OpenMontage v188** (corpus subject) = the closest cousin and the load-bearing contrast: it *produces* a video from a brief (research → script → **generate new assets** → render). video-use *edits existing raw footage* (footage → transcribe → pick cuts → render). Same generative-media composer substrate (Remotion / HyperFrames / Manim / FFmpeg), **opposite task: produce-from-nothing vs edit-what-you-shot.**
- Adobe Premiere text-based editing, CapCut, Opus Clip, Mosaic (Gemini-agent SaaS), HKUDS VideoAgent/ViMax (research) all occupy adjacent cells; none is "a token-efficient transcript-perception video *editor* delivered as a coding-agent skill."
- **The novelty is the conjunction, not any piece:** transcript-as-primary-surface + on-demand visual composites (to dodge the 45M-token frame dump) + coding-agent-skill delivery + a self-eval/re-render loop. Corpus-first *for that surface*; **NOT a world-first** (Descript, ffmpeg+Claude, agent skills all precede).

---

## 9. Why a browser-agent company shipped a video editor

No blog post states it, but the strategy is legible from the repo: video-use is **(a)** a showcase of the browser-use *perception thesis* generalized to a new modality (proof that "give the agent a structured surface, not the raw bytes" isn't browser-specific), and **(b)** a funnel — the README points users to Browser Use Cloud v4 and **Browser Use Box (bux)** (a 24/7 remote VM with Claude Code pre-installed, Telegram/SSH-driven, ~$1k/mo managed pilot) for "always-on editing." The editor is genuinely useful *and* a demand-gen artifact for the infra business.

---

## 10. Bottom line

A small, honest, production-grade agent skill whose value to a builder is **three transferable patterns** more than the pixels: (1) the *structured-surface-not-raw-dump* perception layer (the token-economy idea that unifies browser-use v41 / codebase-memory-mcp v172 / Agent-Reach v174 / fff v194 / this); (2) the *self-eval-before-you-show-it* render loop; (3) the *hard-rules-vs-artistic-freedom* skill-authoring structure. Directly pilotable — it's a free Claude-Code skill and you already run Claude Code. The one thing to fence hard is the ElevenLabs privacy exposure on any footage that isn't yours to send.

See **(C) video-use — Verdict.md** for the routine verdict + mint decision, and **(C) video-use — Pilot Methods Menu.md** for 24 ways to apply it.
