# (C) Autopilot Loop — 2026-07-18-23

> **Trigger:** /loop (interactive; operator-submitted URL + operator-elected full bundle)
> **Topic:** hermes-agent (NEW — topic #69)
> **Started:** 2026-07-18T~22:15+0700
> **Ended:** 2026-07-18T23:15+0700
> **Duration:** ~60m (incl. ~4.6m verify workflow)

## Trigger detail
Operator pasted `https://www.youtube.com/watch?v=y96gIckJJ2Q` (after a first URL `m8VC2SV2igM` was caught as a **duplicate** of topic 67 vercel-eve — no build done on it). Anchor resolved to a VN no-code Hermes Agent tutorial. Collision check: net-new by URL and topic. Operator chose **full bundle + verify** (via AskUserQuestion).

## Per-cycle metrics
| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 8 (yt-search bundle) | 1 (topic itself) | 0 | ~1.0 |

Cold-start topic → 1 cycle created the full topic. `gaps_closed_ratio ≈ 1.0` (target 0.5 exceeded).

## Sources ingested
- `raw/2026-07-18-hermes-agent/` — `_sources.md` + t1–t8 transcripts (EN) + `t1-phan-dong-giang.vi.md` (VN original).
- 8 videos: t1 Phan Dong Giang (anchor) · t2 NetworkChuck (1.3M views) · t3 Tech With Tim · t4 Sean's AI Stories · t5 Tonbi masterclass · t6 Elestio · t7 Plastic Labs/Honcho · t8 AI LABS/Claude Code.
- Fetch: `yt-dlp --cookies-from-browser chrome` (no 429) → `bin/vtt-to-md.py` (venv python3). ~33.1K words EN + 10.5K VN. No NotebookLM.

## Verification
- Refute-first workflow **`wf_06a79485-687`** — 44 agents (8 gatherers → 22 merged claims → refute-first verifiers with 3-skeptic perspective panels on 6 hype claims → 2 completeness critics). 0 errors, ~1.83M tokens, 209 tool calls, ~4.6 min.
- Primary grounding (main loop): GitHub API ×2 endpoints, official README, site, docs.
- **Scorecard: 22 claims → 13 CONFIRMED / 4 MISLEADING / 4 FALSE / 1 UNVERIFIABLE / 0 fabricated.**
- Conflicts resolved (Rule 7 / Rule 12): H5 release-date panel split (Mar-12 vs May-7) → **direct releases-API check = v0.2.0 2026-03-12**; propagated critic-2 error corrected (216,731 > AutoGPT 184K → Hermes IS most-starred); skill-maturity contradiction (Sean: memory-learning not autonomous skill-improvement) surfaced, not averaged.

## Wiki articles created (11 — all NEW, topic #69)
- `wiki/hermes-agent/_index.md`
- `wiki/hermes-agent/overview.md`
- `wiki/hermes-agent/learning-loop-and-self-improving-skills.md`
- `wiki/hermes-agent/memory-system.md`
- `wiki/hermes-agent/channels-providers-deployment.md`
- `wiki/hermes-agent/hermes-vs-openclaw.md`
- `wiki/hermes-agent/claude-code-interop.md`
- `wiki/hermes-agent/pricing-license-and-skill-hub.md`
- `wiki/hermes-agent/claims-scorecard.md`
- `wiki/hermes-agent/caveats-and-corrections.md`
- `wiki/hermes-agent/source-provenance.md`
- `wiki/_master-index.md` (UPDATED — prepended hermes-agent; 68→69 topics)
- `raw/_inventory.md` (UPDATED — bullet raw→compiled)

## Final metric
- `gaps_closed_ratio` ≈ 1.0
- Stop reason: single-cycle cold-start topic complete; target_ratio (0.5) exceeded.

## Corpus-firsts
1. **Largest single repo by stars in the corpus — 216,731★** (verified 2× GitHub API), overtaking AutoGPT (184,043★).
2. **First dedicated *personal-agent-runtime* topic** (distinct from framework vercel-eve t67 / multiplexer herdr t68).

## Top unclosed gaps / follow-ups
1. **Data-residency + subagent-isolation threat-model** undocumented — the hard blocker for any candidate-facing hireui use (same as vercel-eve). Would need Nous docs or a self-host security review.
2. **Skill self-improvement maturity** — is there an eval/fitness loop, or memory-only? Re-check at a future Hermes release; Sean's AI Stories is the source to re-watch.
3. **Anthropic "June-15 subscription" pricing claim** (t8) — unverified; check Anthropic pricing docs (relevant to claude-api-cost-optimization).
4. **OpenClaw** has no dedicated corpus topic yet despite being referenced across vercel-eve/herdr/hermes-agent — candidate for a future NEW topic to anchor the comparison spine.

## Suggested next action
Two options: (A) **PILOT** Hermes operator-side as an always-on ops/automation agent (MIT, clean license; orthogonal to the v189 loop) and test the **Hermes-as-MCP-server-around-Claude-Code** pattern — the Goal-relevant angle; OR (B) ship a NEW **OpenClaw** topic to complete the agent-runtime comparison cluster (vercel-eve / herdr / hermes-agent all reference it). Branch `autopilot-research` is committed but **NOT merged** — operator merges when ready.
