# (C) OpenMontage — Deep Dive (v188 LLM-Wiki ship)

> **Subject:** `calesthio/OpenMontage` — *"The first open-source, agentic video production system."*
> **Pinned & source-verified at commit** `1188e1b` (last commit 2026-06-30, `Merge PR #199 fix/video-compose-vertical-resolution`).
> **License** AGPL-3.0 · **Language** Python 63.3% / HTML 24.8% / TS 6.2% / JS 4.9% · **30.3k★ / 3.4k forks / 55 open issues** (page-stated §37.4 — NOT API-verified, so NOT a viral-velocity claim).
> **Author** `calesthio` ("Calesthio") — a **pseudonymous GitHub *user*** (not an org), bio *"Building open source AI Assisted and Agentic Tools. Creator of OpenMontage and Crucix"*, **Company: Microsoft**, **Location: Seattle WA**, X `@calesthioailabs`, YouTube `@OpenMontage`; a **serial agentic-tools builder** (OpenMontage 30.3k★ + Crucix 10.4k★ "personal intelligence agent" + 5 more repos).
> **Built 2026-07-01** at operator request ("build LLM wiki + double deep dive into the original resource for knowledge + show many methods to apply"). Verdict produced **inline + hand-verified** per `feedback_wiki_verify_independently_check_collisions`; a **14-agent read-only workflow** (`wf_326fd3eb-f01`, ~1.04M subagent-tokens) did source-reading + upstream research ONLY.

---

## 0. One-paragraph orientation

OpenMontage turns your **AI coding assistant** (Claude Code, Cursor, Copilot, Windsurf, Codex) into an end-to-end **video production studio**. You describe a video in plain language; the agent runs an 8-stage pipeline — **research → proposal → script → scene-plan → assets → edit → compose → publish** — selecting one of **12 production pipelines**, calling **~87–102 deterministic Python tools**, following **153 Markdown "stage-director" skills**, and rendering the final piece with **Remotion** (React), **HyperFrames** (HTML/CSS/GSAP), or **FFmpeg**. The single most important architectural fact: **there is no Python runtime orchestrator — the coding agent *is* the runtime.** All the intelligence lives in readable, version-controllable **YAML pipeline manifests + Markdown skills**; Python does only the deterministic work (tool execution, schema validation, checkpoint/state persistence, cost tracking). That instruction-driven, agent-first design — plus its budget-governance, quality-gate, and decision-audit machinery — is where the transferable value lies for a software team, quite apart from the video domain.

---

## 1. The four layers (with true counts, reconciled against the marketing)

OpenMontage is a **3-layer knowledge architecture** sitting on top of a tool substrate + a rendering substrate:

| Layer | What it is | Verified count | Marketing claim |
|---|---|---|---|
| **Tools** (`tools/`) | Python `BaseTool` subclasses — the deterministic execution layer | **~87–102** concrete tool implementations (agents counted 84 / 87 / 88 / 90 concrete subclasses; the registry reports ~102 entries; 121 `.py` files total incl. infra) | README says **"52 production tools"** |
| **Layer 2 skills** (`skills/`) | **OpenMontage-original** Markdown "stage-director" + meta skills | **153** `.md` (INDEX + ~6 core + ~33 creative + ~10 meta + ~103 pipeline stage-directors) | — |
| **Layer 3 skills** (`.agents/skills/`) | **Federated external-tech knowledge packs** (Remotion/FFmpeg/GSAP/Vercel/React docs, etc.) across ~78 namespaces | **561** `.md` (+ a **321**-file `.claude/skills/` mirror → **~1,035 total** skill files across all layers) | README says **"400+ agent skills"**; GitHub desc says **"500+"** |
| **Pipelines** (`pipeline_defs/`) | Declarative YAML orchestration specs | **12 production** + `framework-smoke` (CI) = **13 YAML** | README says **"12 pipelines"** ✓ |

**Honest reconciliation of the counts (a doc-vs-code note, faithfully flagged):**
- **Tools**: the README *understates* — it claims 52 but ~87–102 exist. The "52" is best read as a production-tier / older subset (ARCHITECTURE.md itself says "57+" in one place, "48" in the diagram — an *internal* inconsistency). This is under-claiming, not marketing inflation — mildly to the repo's credit.
- **Skills**: "500+" is roughly true only if you count all three layers (~1,035); the **original** OpenMontage skill count is **153** — the rest are federated external docs (Layer 3) + a `.claude` mirror. So "500+ skills" conflates original + vendored knowledge.
- **Pipelines**: "12 production pipelines" is **TRUE** (a 13th, `framework-smoke`, is a test harness).

**How the layers interlock** (verified example, `animated-explainer` @ `assets` stage): the pipeline YAML declares `required_tools: [image_selector, video_selector, tts_selector]` → the agent reads `skills/pipelines/explainer/asset-director.md` (Layer 2) → the skill says "call `image_selector`, which ranks providers across 7 dimensions" → if the agent doesn't know FLUX, the skill's `agent_skills: ['flux-best-practices']` points it to `.agents/skills/flux-best-practices/` (Layer 3) → the agent runs the tool, checkpoints the artifact as JSON, advances.

---

## 2. The end-to-end flow (8 stages, human-gated, cost-governed)

| # | Stage | Paid? | Director skill | Output artifact | Gate |
|---|---|---|---|---|---|
| 1 | **research** | free | `research-director.md` | `research_brief` (concepts, stats, refs) | optional |
| 2 | **proposal** | free | `proposal-director.md` | `proposal_packet` (cost estimate, 2–3 concepts, **locked render-runtime**, playbook) | **mandatory human approval** before any budget is reserved |
| 3 | **script** | free | `script-director.md` | `script` (narration + timecodes, 150–160 WPM) | optional |
| 4 | **scene_plan** | free | `scene-director.md` (or `video-reference-analyst.md` for "paste a reference video") | `scene_plan` (cuts, timing, visual brief) | optional |
| 5 | **assets** | **PAID begins** | `asset-director.md` | `asset_manifest` (files, metadata, `cost_log` entries) | mandatory (artifact + cost reconciliation); per-action approval at **$0.50** default |
| 6 | **edit** | free (decisions) | `edit-director.md` | `edit_decisions` (locked runtime, `templated` vs `atelier` mode, TTS, music, effects) | optional; **mandatory** if `atelier` |
| 7 | **compose** | **PAID (render)** | `compose-director.md` | `render_report` (MP4 H.264 + ffprobe) + **`final_review`** | mandatory 5-check `_run_final_review()` |
| 8 | **publish** | free | `publish-director.md` | `publish_log` (export metadata; **no auto-posting**) | human review |

Two "paste a video you already love" and "real video video" flows sit on top:
- **Reference-driven** (`video-reference-analyst.md`, an "AGENT_GUIDE Rule Zero" entry point): analyze the reference's transcript / pacing / scenes / keyframes → present 2–3 *grounded* concepts, not prompt-rewrites.
- **Real-footage documentary** (`documentary-montage`, BETA): `corpus_builder.py` fans out across **free/open sources** (Archive.org, NASA, Wikimedia Commons, Pexels, Pixabay, Unsplash + ~10 more), embeds clips with **CLIP**, then `clip_search.py` retrieves + ranks *actual motion footage* by thematic relevance and edits it into a timeline — "not the usual animate-a-few-stills trick."

---

## 3. Cost governance — the estimate → reserve → reconcile discipline

`tools/cost_tracker.py` implements a three-phase spend lifecycle that is one of the strongest transferable patterns here:

- **`estimate()`** — every tool declares `estimate_cost()` (USD) + `runtime_estimate()`; the proposal stage sums them into a preflight budget.
- **`reserve()`** — locks budget, checks the `single_action_approval_usd` threshold (**$0.50** default), raises `ApprovalRequiredError` / `BudgetExceededError`.
- **`reconcile()`** — records *actual* spend post-execution (entries tagged `ESTIMATED / RESERVED / COMPLETED / FAILED / REFUNDED`).
- **Budget modes**: `OBSERVE` (log only) · `WARN` (proceed + alert) · `CAP` (hard block). Default budget **$10** total, **10%** reserve holdback.
- **Free path = $0**: Piper TTS (offline) + free-stock/archival footage + Remotion + FFmpeg = a finished video with zero API spend.

⚠️ **Trust model caveat**: `cost_log.json` is plaintext, local-only, unsigned. Budget can be bypassed by editing it; enforcement is not atomic at API-call time — **a runaway or prompt-injected agent could still rack up real cloud spend** on Veo/Kling despite `CAP` mode. This is the real pilot risk (see §7).

**Provider selection is a scored decision, not a hardcoded chain.** A 7-dimension selector ranks every viable provider: **task_fit 30% · output_quality 20% · control 15% · reliability 15% · cost_efficiency 10% · latency 5% · continuity 5%**, logging `options_considered` (with scores), `selected`, `reason`, `confidence` — no silent defaults.

---

## 4. The provider landscape it orchestrates

**~17 cloud (paid) providers** via a fal.ai gateway + direct APIs: **video** — Kling 2.5 (~$0.07/s), Veo 3 (~$0.40/s premium), MiniMax, Runway Gen-3/4, Grok Imagine, HeyGen avatars, Higgsfield (multi-model orchestrator, "Soul ID" consistency), Seedance; **image** — FLUX (Pro/Dev), Google Imagen, DALL·E 3, Recraft, Grok; **audio/TTS** — Google Chirp3-HD ($30/1M chars, 1M free/mo, emotional range), OpenAI TTS, ElevenLabs (voices + music + dubbing), Suno (full songs).

**~17 free/local providers**: **Piper TTS** (offline neural, ~30+ English voices), **Remotion** (MIT, React composer, CPU), **HyperFrames** (open-sourced by HeyGen, HTML/CSS/GSAP, Node ≥22), local diffusion video **WAN 2.1 / Hunyuan / CogVideo** (GPU-required), **ComfyUI**, and the CLIP-indexed **free-stock/archival corpus** (Archive.org / NASA / Wikimedia / Pexels / Pixabay / Unsplash / Coverr / MixKit / ESA / JAXA / NOAA / LOC / NARA / Freesound).

**Real cost-tracked demos (README, unverified vs current pricing):** "THE LAST BANANA" 60s animated short (6 Kling clips + Chirp3-HD + royalty-free music) = **$1.33**; "The Library at Alexandria" 70s atelier elegy = **$0.02**; "VOID Neural Interface" product ad (4 DALL·E-3 + OpenAI TTS + Remotion) = **$0.69**; two FLUX+Remotion shorts = **$0.15** each.

---

## 5. Quality discipline (this is the transferable gold for a software team)

OpenMontage enforces quality with a **dual-layer** model: **instruction-driven** governance (readable Markdown/YAML) + a thin **infrastructure** layer (Python for schema validation + state only).

- **`skills/meta/reviewer.md`** (344 lines) — a **CHAI**-criteria finding system (**A**ccurate = cite the exact artifact field/frame · **C**omplete = pattern-scan the whole class · Constructive = propose a concrete fix or downgrade to "investigation"). *(CHAI is repo-attributed to a "CMU/Harvard study, arXiv 2604.21718v2" — recorded as **repo-cited, not independently verified**.)* Runs at every checkpoint. Domain checks include **slideshow-risk scoring** (6 dims — repetition / decorative_visuals / weak_motion / weak_shot_intent / typography_overreliance / unsupported_cinematic_claims; **fail ≥ 4.0, revise ≥ 3.0**), decision-log auditing, reference-alignment, and delivery-promise preservation.
- **`skills/meta/checkpoint-protocol.md`** (344 lines) — JSON state persistence + **resume-from-failure** (`in_progress` + `partial_progress`, e.g. `completed_scene_ids: [1,2,3]`) + per-stage human-approval gates (policies `guided` / `manual_all` / `auto_noncreative`).
- **`schemas/artifacts/final_review.schema.json`** — a mandatory **5-check** post-render gate: `technical_probe` (ffprobe) · `visual_spotcheck` (4+ frames flagged for black/broken overlays/missing assets/unreadable text) · `audio_spotcheck` (narration/music presence, clipping) · `promise_preservation` (`delivery_promise_honored`, `render_runtime_used` matches the locked value, `silent_downgrade_detected`) · `subtitle_check` (word-level sync ±100ms).
- **`schemas/artifacts/decision_log.schema.json`** — a **16-category** decision audit trail; each entry requires `options_considered` (≥1 alternative, each with score/reason/`rejected_because`), `selected`, `reason`, `confidence (0–1)`.
- **`docs/PR_REVIEW_GUIDE.md`** (529 lines) — **scenario-based** review (8 scenario prompts: New Provider / Selector / GPU Runtime / Render Runtime / Pipeline / Schema / Dependency / Docs), 14 review areas, 5 severity levels, an 8-point merge-readiness rubric.
- **`AGENT_GUIDE.md`** (688 lines) — **Rule Zero** (all video requests go through pipelines, never ad-hoc API calls), the **Decision Communication Contract** (announce-before-execution for any paid/consequential call), the **"Present Both Composition Runtimes" HARD RULE** (Remotion + HyperFrames both shown before locking, no silent choice), a **no-silent-downgrade** rule (motion-required deliverables can't be quietly swapped to stills/FFmpeg), and a mandatory **`templated` vs `atelier`** authoring-mode decision.
- **CI** — `.github/workflows/ci.yml` runs `make install-dev` + `make lint` (py_compile on 4 core files — syntax only) + `make test` (pytest, phase-organized). **`framework-smoke.yaml`** is a 2-stage, *no-tool-execution* pipeline used to validate manifest/checkpoint/schema contracts cheaply — a beautifully lightweight CI harness for a YAML-driven system.

---

## 6. The durable domain knowledge (the "knowledge to learn from the resource")

The skills encode real, tool-independent **video craft**. This is the knowledge worth extracting regardless of whether you ever run the tool:

**Narrative & learning science**
- **Misconception-first structure** (Derek Muller's Veritasium PhD, Sydney 2008): state the common wrong belief → show why it's wrong → reveal the correct concept. Higher retention than explanation-first.
- **Mayer's Multimedia Learning** (Cambridge 2001/2020): *segmenting* (≤1 concept per 30–45s), *coherence* (cut decorative visuals), *modality* (don't make the viewer read the same text they're hearing).
- **Kurzgesagt / 3Blue1Brown**: vivid visual metaphors, 2–3s shot rhythm, big-picture framing; **1–3s of deliberate silence** after a key insight.

**Pacing** — 150–160 WPM narration · a new visual every 3–5s · a pattern-interrupt every 45–90s (retention).

**Color & accessibility** — 6 grading profiles (cinematic_warm/cool, moody_dark, bright_clean, vintage_film, high_contrast); skin-tone protection via the vectorscope **123° line**; **Wong 2011** colorblind-safe palette; WCAG 4.5:1 text / 3:1 graphics; never color-only (pair with pattern/label).

**Subtitles** — 3–4 words/cue vertical (TikTok/Reels), 6–8 horizontal (YouTube); ≤20 chars/line on mobile; word-level timing from **WhisperX** (±50ms); ASS `.ass` format with full 8-char hex (`&H00FFFFFF`).

**Audio mixing** — ducking hierarchy relative to narration at −12dB: music −24..−18dB, ambient −30..−24dB, Foley/SFX −18..−12dB; 500–1000ms crossfades; normalize to **−14 LUFS** (YouTube), −1dB peak headroom.

**Editing (Walter Murch's "Rule of Six" hierarchy)** — **emotion > story > rhythm > eye-trace > 2D screen grammar > 3D/technical**. Aspect ratios 2.39:1 / 1.85:1 / 16:9 / 9:16; 24fps ("film") vs 30fps ("video") vs 60fps ("hyperreal"); 4–8s average shot.

**Screen recording** (directly useful for **hireui product demos**) — capture 4K, deliver 1080p (zoom headroom); 60fps for UI/scrolling, 30fps for static code; cursor enlarged 1.5–2× with a highlight ring; 1.5–2× code zoom with 0.8s eases; speed-ramp navigation, key moments at 1.0×; silence-removal via `ffmpeg silencedetect`.

**Data-viz** — bar ≤5–7, pie 3–5, line 5–12 points; build 2–4s / hold 3–5s; 32px title / 24px min value labels @1080p.

**Lip-sync/voice** — `lip_sync` (post-production audio replacement) vs `talking_head` (photo→avatar, HeyGen); `wav2lip` (draft) → `wav2lip_gan` (final); a `voice-performance-director` skill directs pacing/emphasis/emotion.

---

## 7. Security, license & install posture

**Benign install & runtime** (source-verified): `make setup` = `pip install` + `npm install` (remotion-composer) + optional `piper-tts` + `npx --yes hyperframes` cache-warm + `.env` copy. **No `curl|bash`, no postinstall scripts, no sudo.** **No telemetry / phone-home** (grep-clean). **No auto social-posting** — `tools/publishers/` is empty (`__init__.py` only); `publish_log` defines a schema but ships no posting tool (the "auto-post" fear is disproven). Subprocess-safe (`subprocess.run` without `shell=True`; `os.system` appears only in educational `manimgl` skill *templates*). API keys stay local in `.env`, never logged/transmitted; cost tracking is local JSON.

**Two real risks:**
1. **AGPL-3.0 network copyleft** — anyone who offers OpenMontage (modified or not) as a *network service* must disclose source to users, and derivatives must be AGPL. A **commercial / hireui-productization flag**, not a security bug (same class as PilotDeck v175's AGPL and cortex-hub v181's PolyForm license wrinkles). For *internal / personal* use it's a non-issue.
2. **Cloud-API cost runaway** — budget enforcement is local + non-atomic; a runaway/prompt-injected agent could spend real money on paid video providers despite `CAP` mode.

**Concrete pilot fence:** run on a **scratch machine** in **`CAP` budget mode** with a **low cap** + provider keys that have their **own spend limits** (or start on the **$0 free/local path** — Piper + stock + Remotion + FFmpeg) · inspect `Makefile` + `.env.example` before `make setup` · never point it at accounts with real money without provider-side caps · pin commit `1188e1b` · treat AGPL as a **blocker for any hireui *productization*** (fine for internal demo/marketing videos or pattern-stealing).

---

## 8. "World's first?" + the honest boundary

The self-claim is *"the first open-source, agentic video production system."* Assessment: **defensible under an explicit definition** (agent-orchestrated multi-stage pipeline + scored provider selection + decision audit + human checkpoints + end-to-end research→render). The **closest peer**, HeyGen's **HyperFrames** (open-sourced ~May 2026), is a **composition primitive**, not an end-to-end system — and OpenMontage actually *uses* it as one of its render runtimes. The big commercial players (Synthesia, Runway, Kling, Pika) are closed SaaS with no agent orchestration. **NOT a world-first at AI video generation broadly** (that space is huge) — the claim is scoped to the *open-source, agent-orchestrated, end-to-end* framing.

**Top honest caveats** (carry these into any use):
- The *hard* generative work is **upstream** (Veo/Kling/fal.ai/Suno models) and the *hard* composition is **upstream too** (Remotion + HeyGen's HyperFrames); OpenMontage is the **orchestration + governance + craft-knowledge** layer.
- The 561 Layer-3 skills are **vendored external docs**, not original; only ~153 skills are OpenMontage-authored.
- Doc-vs-code count nuances (tools under-claimed, skills conflated across layers) — §1.
- Cost figures are anecdotal and pricing-sensitive; the "agentic" is **architecture, not autonomy** (it needs an agent host and gates on human approval).
- `diagram.png` is an empty placeholder; HyperFrames lacks caption/avatar parity with Remotion (Wave-1); no lockfiles/SBOM; harness-file "drift check" is only a substring test.

---

## 9. What to take away

Two distinct payoffs, and for a software developer they're very unequal:

1. **The agent-engineering architecture is the real prize** (dead-on your Goal #1). OpenMontage is a working, 30.3k★ demonstration of: *put the intelligence in Markdown skills + YAML pipeline manifests, keep code to deterministic offload + schema validation + state; gate every stage on a checkpoint; log every decision with its alternatives; govern spend with estimate→reserve→reconcile; review with a scored, criteria-based meta-skill; validate contracts with a cheap no-execution CI harness; distribute across harnesses with thin pointers to one shared guide.* Every one of those transfers to a software team's Claude Code workflow (and to this vault + hireui) — see the Pilot Methods Menu.
2. **The video capability is genuinely usable** but off your software goal — best as internal **hireui demo/marketing videos** or an explainer of your own LLM-Wiki method, on the **$0 free/local path**.

*See `(C) OpenMontage — Verdict.md` for the routine-v2.6 classification and `(C) OpenMontage — Pilot Methods Menu.md` for 24 concrete ways to apply this.*
