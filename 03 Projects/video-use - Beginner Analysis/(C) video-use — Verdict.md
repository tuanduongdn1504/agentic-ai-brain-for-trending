# (C) video-use — Verdict (LLM Wiki v198)

> Routine v2.6. Verdict produced **INLINE + hand-verified** per `feedback_wiki_verify_independently_check_collisions`: an 8-agent read-only research workflow (`wf_e7646fd9-850`, ~1.45M subagent-tokens, 109 tool-uses, **8/8 agents returned, 0 errors, 0 empty, all toolCalls>0**) did source-reading + upstream research ONLY. ALL corpus / collision / identity / mint claims verified BY HAND (see §7). Source-verified at commit `92c2b34`.

---

## Phase-0.9 STRICT — GOAL-ALIGNED INCLUDE 3/4

**(a) FAIL** — Browser Use, Inc. (Magnus Müller + Gregor Zunic, YC W25, $17M seed Felicis-led Mar-2025, SF, ~7 employees) is a funded startup, not Anthropic ((a)-7 is Anthropic-only). **RETURNING org** — `browser-use/browser-use` is corpus subject **v41** → a **#19 19a returning-institution** data-point, NOT corpus-first for this org. No (a)-rescue: Claude is a consumer/harness here, not the author. *(Note: a `claude` co-author appears on ~6 commits — the repo was built with Claude Code; a self-referential data-point, not Anthropic authorship, and not an (a)-rescue.)*

**(b) STRONG — keys the tier** (⚠️ MODERATE-on-the-video-domain recorded operator-reviewable, the OpenMontage v188 precedent). video-use is a **Claude-Code-first agent skill** = dead-center on the agent-skills substrate the vault studies + Goal #1, and it embodies three of the exact agent-engineering exemplars the vault tracks: (1) the **token-efficient perception layer** ("read the video, don't watch it" — transcript-as-DOM to dodge a 45M-token frame dump) lands directly on the **claude-api-cost-optimization** thread; (2) **parallel sub-agents, one animation each** lands on the **multi-agent-orchestration** thread; (3) the **self-eval/re-render loop** is a maker/checker discipline. Directly + safely pilotable — it's free, MIT, and runs in the vault's own Claude Code; the operator ships product/recruitment/Scrum content. **STRONG-not-STRONGEST** = third-party + Claude one of several harnesses (Codex/Hermes/OpenClaw) + a capability-augmentation skill (not the agent itself) + the domain is video, not software. §31 keys GOAL-ALIGNED on (b) MODERATE+.

**(c) STRONG** — production-grade code: `render.py` (659 LOC — per-segment extract→lossless concat→PTS-shifted overlays→subtitles-LAST, plus **undocumented** default loudnorm two-pass + HDR→SDR tonemapping + portrait auto-detect), `grade.py` (ASC-CDL auto-grade), `transcribe/pack/timeline_view`, a vendored 14-reference `manim-video/` sub-skill, MIT, actively maintained (community PRs through Jul 7). **Honest caveats:** ZERO tests + no CI; no releases/versioning (git-clone-only); filename-only transcript cache (stale-cache footgun); doc-vs-code gaps (README's `MarginV=35` vs code's `90`; "`--preview` 720p fast" vs actual 1080p `medium` — SKILL.md frames its numbers as "worked examples, not mandates," so the Hard Rules are the authority and they all hold); `scribe_v1` pinned though ElevenLabs' current product is Scribe v2; **ElevenLabs privacy** (audio uploaded → ~3-yr retention + training-by-default, future-only opt-out).

**(d) STRONG** — dense cross-refs: **browser-use v41** (SAME ORG + the explicit, README-stated design inspiration — "browser-use for video"); **OpenMontage v188 §C** (the closest cousin — same generative-media composer substrate, opposite task: *produce-from-brief* vs *edit-existing-footage*); **fish-speech v20** + **meetily v196** (the corpus's speech-domain cluster — TTS / on-device STT; ElevenLabs Scribe = hosted ASR, a third data-point); agent-skills substrate (agent-skills-standard v76 / SkillOpt v178 / agent-skills v184 + the vendored manim sub-skill = progressive disclosure); the **token-efficient-perception** thread (codebase-memory-mcp v172 §C#23 "99.2% token reduction" / Agent-Reach v174 / fff v194 — all "give the agent a compact structured surface, not the raw thing").

**Verdict: GOAL-ALIGNED INCLUDE 3/4 [(a) FAIL · (b) STRONG · (c) STRONG · (d) STRONG].**

---

## Pattern outcome — 1 NEW §C standalone at N=1 (CORPUS-FIRST for the surface, NOT world-first)

**"Agent-First Transcript-Driven Video-EDITING Layer for Coding Agents"** — a coding-agent skill that edits *existing raw footage* by treating a **word-level ASR transcript as the primary reasoning surface** (with on-demand visual composites at decision points, deliberately avoiding a full-frame token dump), emits a deterministic Edit Decision List rendered via ffmpeg, and **self-evaluates the rendered output before presenting it** (fix + re-render loop).

**Why a mint (the defining conjunction):** (transcript-as-primary-surface perception, to dodge the ~45M-token frame explosion) × (EDIT existing footage — not generate) × (coding-agent-skill delivery) × (self-eval/re-render maker-checker loop). The perception layer is the genuinely novel, load-bearing mechanism — the browser-use "structured DOM instead of a screenshot" idea transplanted to video, by the org that built browser-use.

**Scope honestly bounded — CORPUS-FIRST for the surface, NOT a world-first.** Descript (2017) pioneered transcript-based editing; ffmpeg+Claude integrations exist; agent skills exist. The novelty is the *conjunction + the token-efficient perception layer + skill delivery*, exactly the fff v194 framing (fzf/ripgrep precede as tools).

**DISTINCT from OpenMontage v188 §C** ("Agent-First End-to-End Generative-Media (Video) PRODUCTION System") — the load-bearing boundary: v188 *produces* a video from a text brief (research→script→**generate new assets**→render, "the agent as production DIRECTOR"); video-use *edits* footage you already shot (footage→transcribe→pick cuts→render). Different input (brief vs raw takes), different task (produce-from-nothing vs edit-existing), different core mechanism (asset-generation pipeline vs transcript-perception). Calling this N=2-of-v188 would conflate produce and edit — a real error, so it is NOT filed as N=2-of-v188.

**⚠️ NO-MINT alternative recorded operator/audit-reviewable** (the ai-berkshire v187 / camofox v179 discipline): *"video-use is simply the video-EDITING vertical of the OpenMontage v188 generative-media family; domain-crossing within a represented family doesn't warrant a new standalone."* I lean MINT (edit-vs-produce is a real task boundary; the transcript-as-DOM perception layer is a distinct, corpus-first mechanism; v188's own §C row scopes itself to PRODUCTION). Either way **counts UNCHANGED 46/11.** §28 ≤2-new-standalones cap honored (1 mint).

**⚠️ Audit flag (~v192, overdue):** the video-adjacent §C cluster is now **three** rows — v188 (produce) / v192 palmier-pro (product-first-app-retrofitted-with-MCP; the mint is about the MCP-retrofit *relationship*, NOT video) / v198 (edit). Confirm at audit whether v188+v198 should stay separate or merge into an "agent-first video" meta-standalone. My read: keep separate (produce vs edit is a real boundary), but flag it.

---

## SECONDARY (NOT minted)

- **#19 19a returning-institution** — first `browser-use/video-use` repo, but Browser Use is a returning org (v41). NOT corpus-first browser-use.
- **browser-use v41 corpus-recursive cross-ref** — the README's own "structured DOM, but for video" thesis makes v41 the explicit design lineage. ⚠️ **NOT #57** (recursion = a corpus subject citing *another* corpus subject as influence; this is the *same org's own prior product* — a self-reference / author-lineage, worth recording, not a #57 promotion).
- **fish-speech v20 / meetily v196 speech-domain cross-ref** — ElevenLabs Scribe = hosted ASR; the corpus now holds TTS (fish-speech v20) + on-device STT (meetily v196) + hosted ASR-as-a-dependency (video-use). NO N-bump (a dependency, not a speech-model subject).
- **agent-skills substrate** — a skill that vendors a second skill (`manim-video/`); progressive disclosure; agent-skills-standard v76 / SkillOpt v178 / agent-skills v184 family. NO N-bump.
- **LV #20 Token-Economy-Quantification QUALIFIED-ADJACENT** — the "45M tokens → 12KB" claim is the token-economy idea, but it's a page-stated/README illustration (not a measured benchmark) → N stays 4, bump deferred (the v168/v172/v194 precedent).
- **#84 84c** — multi-harness (Claude Code / Codex / Hermes / OpenClaw via a symlinked SKILL.md). NOT the ponytail v168 14-platform generator mechanism → NO N-bump.
- **#66 supply-chain — BENIGN install / MODERATE data-privacy.** Install clean (MIT, no `curl|bash`, no postinstall, no `npx --yes` at install time, `.env` `chmod 600` + `.gitignore`'d, zero telemetry in the repo). The real risk is **data egress to ElevenLabs** (audio retained ~3 yr + trained-on by default) — a MODERATE fence for any non-owned footage (candidate interviews especially → GDPR).

**NON-claims:** NOT #52 (~15.9k★ page-stated §37.4, no releases → velocity unestablishable) · NOT world-first (Descript precedes transcript-editing) · NOT #18 B1-MCP (a skill, not an MCP server) · NOT a new top-level pattern (max #85) · NOT corpus-first for AI video generally (OpenMontage v188 precedes) · NOT the first speech/media subject (fish-speech v20).

---

## Tier + counts

- **Tier T1 Skill/Methodology Collection** (Transcript-Driven Video-Editing Skill flavor; the OpenMontage v188 / karpathy v63 / agent-skills v184 family).
- Counts UNCHANGED **46 / 11**. §C live standalones **37 → 38** (+1, N=1). Tracked PROVISIONAL surface **≈44 → ≈45** (7 clusters + 38 live standalones).
- Streak → **GA:59** *(v198 is cleanly goal-aligned — (b) STRONG, no OFF-GOAL question, unlike v196/v197's per-operator MODERATE)*; ⚠️ OFF-GOAL alt reading (v176/v186/v191/v193/v196/v197 as OG) → GA:53·OG:17.
- **§35 CLEAR** — window {v196, v197, **v198**}: under the GA reading 0 OG → clear; and even under the strict reading where v196+v197 are OG, **v198 being cleanly GOAL-ALIGNED is exactly what §35 requires** after a potential breach ("the next ship MUST be GOAL-ALIGNED") → resolved.
- **45 consecutive goal-aligned ships v153→v198** (GA reading).

---

## §7 — Hand-verification log (per `feedback_wiki_verify_independently_check_collisions`)

- **Collision grep** across `_state/` + `_patterns/` + `03 Projects/` for `video-use` / `video use` / ElevenLabs / Descript / HyperFrames — **CLEAN**: no prior video-editing subject; the "video-use" hits are all inside OpenMontage v188's vendored source tree + node_modules + a MoneyPrinterTurbo phrase, none a subject. ElevenLabs appears only as a mention in unrelated wikis; Descript only ever as a landscape reference, never a subject.
- **browser-use = v41** confirmed by reading `_state/03b` (the v41 entry — same org, Magnus + Gregor Zunic, MIT, 89.9k★-at-v41) → this is a RETURNING org, #19 19a, not corpus-first.
- **OpenMontage v188 §C row** read directly from `_patterns/06:90` — its standalone is explicitly scoped to PRODUCTION ("the agent becomes a production DIRECTOR whose deliverable is a rendered file") → confirms video-use (edit) is DISTINCT, not N=2-of-v188.
- **Source hand-read (me, not just the workflow):** README, SKILL.md, install.md, pyproject.toml, .env.example, and the full 659-LOC `render.py`. The render-agent's claims (per-segment concat, 30ms fades, PTS-shift, subtitles-last, output-offset SRT, MarginV=90, loudnorm-default) matched my own line-by-line read exactly (correct line numbers → real reads, no confabulation). Workflow agents A2/A3/A4/A5/A6/A7/A8 covered transcribe/install/manim/identity/landscape/Scribe/history.
- **Confabulation check:** the identity agent flagged its own inaccurate search premises (no "Miloslav" founder; Felicis not Khosla led the seed) and corrected them — used the corrected facts. Star counts disagreed across agents (15.9k / conflicting browser-use-core figures) → no #52 claim. `inflation_check` = discipline HELD (1 mint ≤2 cap; N=1 scoped-not-world-first; NO-MINT alt recorded; DISTINCT-from-v188 established by hand; counts 46/11 unchanged; no N-bumps; no double-count).
