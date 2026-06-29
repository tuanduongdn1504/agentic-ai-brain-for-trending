# Source Provenance & Verification Log

*Transparency audit of sources, claims flagged, and methodological limits for the `ai-web-design-workflow` topic.*

## Method

- **Primary source:** YouTube video PFO01z7Qe38 (Lukas Margerie), transcript via `yt-dlp` auto-subs → `bin/vtt-to-md.py` (216 cue lines), **read in full**.
- **Double deep-dive:** the four originals fetched directly (GitHub API + raw.githubusercontent.com for the Taste Skill; WebFetch + WebSearch for the products).
- **Adversarial verification:** Workflow `wf_8b23bf2d-231` — 14 agents (6 research incl. Taste Skill ×2 independent angles → 6 skeptic verifiers → synthesis brief → completeness critic). The Taste Skill was researched twice independently to maximize verbatim-rubric fidelity.
- **No fabrication:** every product capability and rubric rule below traces to a fetched source; claims that could not be confirmed are flagged, not asserted.

## Originals verified

| Original | Status | Evidence |
|---|---|---|
| **Taste Skill** (leonxlnx/taste-skill) exists, MIT, ~47.2K★ | ✅ T1 | GitHub API metadata; `stargazers_count` confirmed by two agents |
| Install `npx skills add https://github.com/leonxlnx/taste-skill` | ✅ T1 | README verbatim |
| 13 skill variants (taste-skill, gpt-tasteskill, redesign-skill, …) | ✅ T1 | `/skills` contents API listing |
| 3 dials (DESIGN_VARIANCE/MOTION_INTENSITY/VISUAL_DENSITY, baseline 8/6/4) | ✅ T1 | SKILL.md Section 1, both agents |
| Em-dash binary ban (Section 9.G) | ✅ T1 | Verbatim quote extracted by both agents |
| Hero ≤2 lines / ≤20 words / pt-24; Bento zero-empty-cells; no 3-equal-cards; WCAG AA 4.5:1; motion isolation; window-scroll ban; reduced-motion >3; real-images-required; one-icon-family | ✅ T1 | SKILL.md sections 4–9, verbatim |
| **62-point pre-flight gate, all-or-nothing** | ✅ T1 (CORRECTED) | Verified **62**, not the "73+" an early draft claimed |
| **14 official design systems** | ✅ T1 (CORRECTED) | Verified **14**, not "15+" |
| Format = Anthropic SKILL.md (no YAML); `.claude-plugin/plugin.json` → **runs in Claude Code**; portable to Cursor/ChatGPT/Cline | ✅ T1 | Repo structure + README |
| File sizes: core 87KB / redesign 15KB / gpt-taste 8KB | ✅ T1 | Byte counts confirmed |
| **GPT-5.5** real, released 2026-04-23 (ChatGPT) / 04-24 (API); powers Codex | ✅ T1/T2 | OpenAI API docs + WebSearch (announcement page 403'd) |
| GPT-5.5 modes `low/medium/high/xhigh/none`; 400K context | ✅ T1 | API docs (research had omitted `none`) |
| GPT-5.5 pricing ~$5/$30 per 1M (Pro $30/$180) | ✅ T2 | WebSearch |
| **ChatGPT Images 2.0** real, ~2026-04-21; in Codex; ~95–99% text; ~$32/1M output | ✅ T2 | MacRumors/TechCrunch/BuildFastWithAI (medium confidence) |
| **Seedance 2.0** real — ByteDance, 2026-02-12; on Higgsfield/fal.ai/WaveSpeed; DiT+RayFlow; native audio; 4–15s | ✅ T1 | Higgsfield page + fal.ai + WaveSpeed + multi-source |
| **Pietro Schirano** (CEO Magic Path, ex-Anthropic) | ✅ T1 | LinkedIn / X / podcast |
| **Jake Soft Servo** robot-arm-in-Codex post | ✅ T2 | X @soft_servo 2026-04-23 verbatim |
| **Lukas Margerie** (Framer; Builderz Gym) | ✅ T2 | site/X/skool |
| **Claude Design** (Anthropic) launched 2026-04-17 | ✅ T1 | anthropic.com/news + TechCrunch |
| "Vibe-designing" recognized 2026 movement | ✅ T2 | Adobe Creative Trends, NxCode, Muzli, Fast Company |

## Claims corrected

- **Pre-flight count: 62, not 73+** (early draft over-counted).
- **Design systems: 14, not 15+.**
- **GPT-5.5 "extra high intelligence" mode → does not exist.** Real top tier is `xhigh`.
- **GPT-5.5 context 400K verified; "1M" unverified** — do not cite 1M.
- **"40% fewer tokens vs GPT-5.4"** = OpenAI self-report, no published scaffold — directional only.
- **"Codex beats Claude at front-end" (video opinion) → reversed by evidence:** multi-prompt UI test (blog.kilo.ai) favors Opus 4.7; Altman acknowledged GPT-5.5 trailed on front-end at launch; no design benchmark exists.
- **Images 2.0 "4K upscaling" → unconfirmed** (2K experimental is the verified ceiling); **"$30/M" → $32/M**.
- **Seedance Elo 1,351 → ~1,195** (1,351 was a March-2026 figure).
- **redesign-skill "Greenfield/Preserve/Overhaul" named modes + "11.A-F" numbering → not present;** the file uses "How This Works" / "Design Audit" / 7-step Fix Priority.
- **"C dance" → "Seedance"** (phonetic mishearing).

## Claims flagged ⚠️

- **🔴 Meta-correction — Seedance "fabricated/skip" was itself wrong.** The verification workflow's *synthesis brief* concluded Seedance 2.0 "is not a real product — skip it." Its own high-confidence `seedance-2.0` research agent **refuted** that (T1, multi-host). Per Rule 7 + Rule 4 the wiki records **Seedance as real** and treats the brief's verdict as the error. (A reminder that synthesis layers can over-correct; always check the underlying agent.)
- **🟡 Images 2.0 QR-code generation — likely fabricated, dropped.** A draft asserted it with citations; the cited sources contain no such claim. Removed from the wiki.
- **🟡 "Anton Guilds"** (author of the landing-page prompt) — **unverifiable**; no such person found; likely conflation (Anton Sten / Anton Repponen) or pseudonym; prompt not public.
- **🟡 Magic Path "time machine" demo** — Schirano + Magic Path real; the specific demo not located (plausible, unconfirmed).
- **🟡 Higgsfield consumer pricing tiers** (Starter/Plus/Ultra) + explicit aspect-ratio support — appear in aggregators, **not** on the official Higgsfield page (Business $49/seat confirmed).
- **🟡 Images 2.0 per-tier ChatGPT prices** ($20/$200) and **$5/M text input** — not confirmed in fetched sources.
- **🟡 Taste Skill license scope for derivative prompt-framing** inside a proprietary product — MIT covers redistribution; treat prompt edits as permissive but don't resell the skill itself.
- **🟡 GPT-5.5 announcement page** — 403'd; first-party numbers via API docs/aggregation.

## Not attempted / out of scope

- Reproducing the video's exact comparison (prompt + settings not published).
- Spot-checking all 13 Taste Skill variants' SKILL.md (3 core variants read in full; others confirmed by directory listing + README).
- Independent benchmarking of Images-2.0 text accuracy / GPT-5.5 token efficiency on a real workload (recommended as a pilot, not done here).
- The programmatic API model id for Images 2.0.

## Key takeaways

- **Strongest evidence = the Taste Skill** (fully T1, two independent reads). The product claims are weaker (T2 / single-source) and move fast — treat numbers as snapshots.
- The verify pass earned its keep: caught **62-vs-73**, **14-vs-15**, a **fabricated QR capability**, a **reversed Claude-vs-Codex** claim, and — most importantly — **a synthesis layer wrongly declaring a real product fake** (Seedance).
- For the operator: the **durable, adoptable** asset is the **Taste Skill on Claude Code**; everything OpenAI-specific is a swappable, faster-decaying detail.

## Related

[[ai-web-design-workflow/_index]] · [[ai-web-design-workflow/taste-skill-deep-dive]] · [[ai-web-design-workflow/video-to-original-crosswalk]] · [[ai-web-design-workflow/overview]]
