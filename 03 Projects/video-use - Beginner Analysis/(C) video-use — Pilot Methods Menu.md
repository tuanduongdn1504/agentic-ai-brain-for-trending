# (C) video-use — Pilot Methods Menu (24 methods)

> **You asked: "pilot to apply knowledge into my working flow, show me many method for my apply."** Here are 24, laddered A→F. You're a software developer + Scrum coach building **hireui** (recruitment SaaS), you run the vault's own Claude Code, and you ship product/recruitment/team content. video-use is a **free MIT Claude-Code skill** → most of its value reaches you two ways: **(1) borrow the three patterns with zero install** (highest ROI, zero risk), and **(2) actually install it and edit real footage** (real payoff for demos/recruitment/Scrum content — behind one privacy fence).
>
> **⭐ One-thing path: B5 → C11 → D16** — steal the perception principle into `CLAUDE.md` (zero install) → install + edit one real screen-recording into a hireui product-demo (proves the loop) → make employer-branding / job-post recruitment videos (a real Goal-#2 content artifact). **The load-bearing fence is D's privacy rule: never send other people's footage (candidate interviews especially) to ElevenLabs.**

---

## The 3 patterns worth stealing (the "knowledge" you asked to apply)

1. **Structured-surface, not raw dump** — "read the video, don't watch it": give the agent a compact *transcript* (~12KB) + on-demand visual composites, never a 45M-token frame dump. This is the same idea as browser-use's DOM-not-screenshot, codebase-memory-mcp v172's code-graph-not-file-reads, fff v194's index-not-re-grep. It generalizes to **any heavy modality your agents touch.**
2. **Self-eval before you show it** — after producing output, the agent inspects its *own render* against a checklist and fixes+re-renders (max 3×) before presenting. A maker/checker loop baked into the skill.
3. **Hard-rules vs artistic-freedom skill structure** — a skill with a short "12 things you MUST do (correctness)" block and an explicit "everything else is a worked example, deviate freely" license. A clean template for authoring your own `05 Skills/`.

---

## Group A — Read & learn (0 cost, 0 risk)

- **A1. Read the perception idea.** README §"How it works" + `poster.html` (open in a browser). ~15 min. The single most transferable concept in the repo: the two-layer transcript+on-demand-visual surface.
- **A2. Read `SKILL.md`'s Hard-Rules-vs-artistic-freedom split.** Notice it separates 12 correctness invariants from ~everything-else-is-a-worked-example. This is the best skill-authoring structure in the corpus for your own `05 Skills/`.
- **A3. Read `render.py` (659 LOC) as an ffmpeg masterclass.** Per-segment-extract→lossless-concat→PTS-shifted-overlays→subtitles-LAST, plus the (undocumented) default loudnorm two-pass and HDR→SDR tonemap. Reusable ffmpeg knowledge independent of the skill.
- **A4. Read the vendored `manim-video/` references' three craft principles** — narration-first design gate, opacity-layering for cognitive load, first-render-excellence. Tool-agnostic; they apply to any explanatory content you make (Scrum training, product walkthroughs).

## Group B — Borrow the patterns into your work, zero install (highest ROI)

- **B5. ⭐ Put the "structured-surface-not-raw-dump" principle in your `CLAUDE.md`.** One line: *"When an agent must reason over a heavy artifact (long transcript, large file, big dataset, media), give it a compact structured surface + on-demand detail — never dump the raw bytes."* Composes with the fff v194 / codebase-memory-mcp v172 / Agent-Reach v174 token-economy threads. Zero install.
- **B6. Adopt the self-eval-before-showing loop** as a general vault discipline. It's the same shape as your `loop-verifier` skill + doubt-driven-development (v184): the maker inspects its own artifact against a checklist and rejects until it passes. Wire it into the loop-engineering v189 pilot you already run.
- **B7. Steal the Hard-Rules/artistic-freedom template** for your own skills — separate the ~5 correctness invariants (non-negotiable) from the "worked examples, deviate freely" body. Retrofit one existing `05 Skills/` file to this shape and see if it reads clearer.
- **B8. Steal the `project.md` session-memory pattern** — one appended section per session (Strategy / Decisions / Reasoning log / Outstanding), read on startup. It's a lightweight L-level memory file; it maps onto your CC-memory-systems thread and your existing STATE.md discipline.
- **B9. Steal the parallel-sub-agent-one-file-each brief** (SKILL.md's animation section, points 1–10). It's a clean, copy-pasteable spec for multi-agent fan-out where each agent writes a unique file (no overwrite races) — directly reusable in your multi-agent-orchestration pilots and your Workflow scripts.
- **B10. Steal the "12 hard rules" idea of encoding silent-failure traps as invariants.** For hireui, the analogue is "the N correctness invariants a coding agent must never violate" (e.g., agent-`*` branch only, GitNexus-first, no LLM spend without a spec) — write them as a hard-rules block in hireui's CONSTITUTION.

## Group C — Low-risk hands-on (install on a scratch machine)

- **C11. ⭐ Install it as a Claude-Code skill + edit one real screen-recording.** `git clone` → `uv sync` → `brew install ffmpeg` → symlink into `~/.claude/skills/video-use` → get an ElevenLabs key → record a 2–3 min screen-capture of a hireui feature → `claude` in that folder → *"edit this into a 60-second product demo."* Proves the whole loop end-to-end for ~$0.02 of Scribe. (`install-snapshot` first — see fence.)
- **C12. Pin the commit before installing.** No releases exist → `git checkout 92c2b34` after clone so a future `git pull` can't change behavior under you.
- **C13. Measure the token economy yourself.** After one edit, compare the ~12KB `takes_packed.md` the LLM actually read against a naive "describe every frame" baseline. Confirm (or refute) the 45M→12KB claim for your own footage; pair it with your ccusage/OTel cost-pilot.
- **C14. Test the self-eval loop honestly** — deliberately feed it a take with a hard mid-word cut and see whether the self-eval catches the audio pop / visual jump and re-renders. Tells you how much to trust the "you see it only after it passes" promise.
- **C15. Trial the vendored `manim-video/` sub-skill** on a scratch machine to produce one explainer animation (e.g., a hireui matching-flow diagram). Judge whether the progressive-disclosure reference system is worth adopting for your own skills.

## Group D — Goal-#2 (hireui + recruitment + Scrum) — the real payoff, behind the privacy fence

- **D16. ⭐ Employer-branding / job-post videos for hireui.** Record a hiring-manager or founder doing a 3-minute talking-head about a role/the company → video-use cuts filler, grades, burns 2-word captions → a polished recruitment clip. **Your own/consented footage only** → the privacy fence does not bite here. A genuine recruitment-product content artifact.
- **D17. hireui feature-launch / changelog videos.** Every shippable feature → a 30–60s screen-capture edited into a launch clip for the product's changelog / social. Repeatable, cheap, on-brand once you fix a grade + subtitle style.
- **D18. Sprint-review highlight reels (Scrum-coach leverage).** Record the demo portion of a sprint review → cut to a 2-minute highlight for stakeholders who missed it. The "preserve peaks, extend past punchlines" cut-craft maps directly onto "keep the moments that landed."
- **D19. Team retro / training recap clips.** Turn a recorded retro or a coaching session into a short recap with captions. The narration-first + opacity-layering craft (A4) makes these actually watchable.
- **D20. ⚠️ Candidate-interview processing — DO NOT, without the enterprise fence.** The tempting use ("auto-clip the best answers from a recorded interview") sends *another person's PII audio* to ElevenLabs, which retains it ~3 years and trains on it by default (future-only opt-out; Zero-Retention is enterprise-only). **This is a GDPR + consent problem.** If you ever pursue it: enterprise Zero-Retention Mode + explicit opt-out + written candidate consent + a data-residency review with hireui's counsel first. Default answer for now: **no.** (Recorded here so the idea is fenced, not forgotten.)
- **D21. Borrow the architecture for a hireui "media" feature spec** — if hireui ever needs to process uploaded video (candidate intros, job-post videos), the transcript-as-primary-surface + EDL + self-eval design is a source-verified template. Spec-only, on an `agent-*` branch, per hireui's CONSTITUTION (I-2 / I-8 / GitNexus-first); hireui has no LLM spend yet → design-it-right, don't retrofit.

## Group E — Off-goal / personal (optional)

- **E22. Personal content** — travel, family, hobby footage. Zero work relevance, but the fastest way to build intuition for what the skill does well vs badly before you trust it on work content.
- **E23. Podcast / talking-head cleanup** — if you record any long-form audio/video, the filler-removal + dead-space cutting is the one thing it's provably good at (Descript's original wedge).

## Group F — Vault-meta

- **F24. Write the "structured-surface-not-raw-dump" synthesis note.** video-use closes a five-subject arc: **browser-use v41** (DOM-not-screenshot) → **codebase-memory-mcp v172** §C#23 (code-graph-not-file-reads) → **Agent-Reach v174** (web-read-not-scrape-everything) → **fff v194** (resident-index-not-re-grep) → **video-use v198** (transcript-not-frames). One page in the Pattern Library on "the token-economy perception principle across modalities" is a genuine cross-wiki synthesis — and it's the deepest thing this ship teaches.

---

## Fence (mandatory before any install)

- **`install-snapshot`** the home dir before installing (unfamiliar package with system symlinks + brew).
- **`npm-security-check`** is N/A (pure Python), but do read `install.md` before letting an agent run it autonomously — it symlinks the repo into `~/.claude/skills/` and `brew install`s ffmpeg.
- **Pin `92c2b34`** (no releases exist; `git checkout` the commit so a `pull` can't shift behavior).
- **ElevenLabs key** → `.env` at the repo root (`chmod 600`, `.gitignore`'d — the install already does this); never commit it, never echo it.
- **PRIVACY (load-bearing):** every source file's audio goes to ElevenLabs, which **retains it ~3 years and trains on it by default** (future-only opt-out). **Own/consented footage only.** No candidate-interview or third-party-PII footage without enterprise Zero-Retention + consent + a data-residency review (D20).
- **Cost:** ~$0.11 per 30-min take of Scribe on a paid plan (Starter $6/mo); trivial, but it's real money on a metered API — not free like local Whisper.
- **hireui:** anything touching hireui stays on an `agent-*` branch, operator-installed skills only (I-8), GitNexus-first, per its CONSTITUTION. hireui has no LLM spend yet → build-it-right.
- **Stale-cache footgun:** re-shooting a take with the same filename reuses the old transcript (cache is keyed on filename, not content) — rename files or clear `edit/transcripts/` between shoots.
