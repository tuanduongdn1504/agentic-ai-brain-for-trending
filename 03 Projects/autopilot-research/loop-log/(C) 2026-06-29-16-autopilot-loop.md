# (C) Autopilot Loop — 2026-06-29-16

> **Trigger:** manual (interactive session — operator submitted a YouTube URL with "build knowledge + double deep-dive into the originals + show me many pilot methods")
> **Topic:** claude-code-plugins-stack (Chase AI — "Use These 17 Claude Plugins, It Will Make You 10x Better.")
> **Started:** 2026-06-29 (session)
> **Ended:** 2026-06-29 (session)
> **Mode:** path 5 yt-dlp full transcript + direct primary-source `gh api`/WebFetch of all 17 originals + adversarial Workflow verification + `gh api` ground-check

## Per-cycle metrics

| Cycle | Sources added | Gaps before | Gaps after | Ratio |
|-------|---------------|-------------|------------|-------|
| 1 | 1 video + 17 originals | 1 (cold topic) | 0 (12-file topic compiled, indexed, cross-linked) | ~1.0 |

## Sources ingested

- `raw/2026-06-29-claude-code-plugins-17-chase-ai.md` — Chase AI video V2RIVnGCy74 transcript (yt-dlp `en` auto-subs, deduped ~3,840 words, read in full) + the 17-originals map.
- 17 originals fetched directly (`gh api` + WebFetch): leonxlnx/taste-skill, pbakaus/impeccable, voltagent/awesome-design-md, DietrichGebert/ponytail, teng-lin/notebooklm-py, microsoft/playwright-cli, openai/codex-plugin-cc, googleworkspace/cli, cli/cli, anthropics/skills, mvanhorn/last30days-skill, firecrawl/firecrawl, karpathy/autoresearch, supabase/cli, kepano/obsidian-skills, HKUDS/LightRAG, stripe/stripe-cli.

## Verification

- **Workflow `wf_81b898cf-93e`** — 35 agents: 17 research (one per original) → 17 independent adversarial skeptics (re-verify load-bearing claims with fresh WebSearch + `gh api`, default-to-UNVERIFIED) → 2 critics (completeness + operator-fit). ~1.6M tokens, 776 tool calls.
- **1 agent failure:** `research:github-cli` ("prompt too long") → GitHub CLL researched directly by operator via `gh api repos/cli/cli`.
- **Self-caught script bug:** the first launch was stopped within seconds — the `pipeline()` return-chaining would have discarded the rich stage-1 research and returned only verdicts. Patched stage 2 to merge `{...research, verification}`, resumed from cache via `resumeFromRunId` (completed agents cached, only new shape re-ran).
- **`gh api` ground-check** of all 17 repos' stars/license/created-date, 2026-06-29.

## Wiki articles created/updated

- `wiki/claude-code-plugins-stack/_index.md` (NEW)
- `wiki/claude-code-plugins-stack/overview.md` (NEW)
- `wiki/claude-code-plugins-stack/the-17-plugins.md` (NEW — full catalog)
- `wiki/claude-code-plugins-stack/new-design-tools-impeccable.md` (NEW)
- `wiki/claude-code-plugins-stack/new-ponytail-code-minimalism.md` (NEW)
- `wiki/claude-code-plugins-stack/new-research-tools-last30days-firecrawl.md` (NEW)
- `wiki/claude-code-plugins-stack/new-infra-clis-supabase-stripe-github.md` (NEW)
- `wiki/claude-code-plugins-stack/new-gws-google-workspace-firing.md` (NEW)
- `wiki/claude-code-plugins-stack/originals-this-project-runs-on.md` (NEW — autoresearch + notebooklm-py)
- `wiki/claude-code-plugins-stack/already-deep-dived-crosswalk.md` (NEW — the 7 covered originals)
- `wiki/claude-code-plugins-stack/video-to-original-crosswalk.md` (NEW)
- `wiki/claude-code-plugins-stack/source-provenance.md` (NEW)
- `wiki/_master-index.md` (UPDATED — added claude-code-plugins-stack topic)
- `raw/_inventory.md` (UPDATED — new row, top of table)
- `output/(C) 2026-06-29-claude-code-plugins-stack-pilot-methods.md` (NEW — 20 ranked pilot methods)

## Final metric

- `gaps_closed_ratio` ≈ 1.0 (cold-start topic: 12-file wiki + pilot menu + index + inventory all compiled in one cycle)
- Stop reason: deliverable complete (wiki + double-deep-dive + pilot menu all produced); single-cycle interactive run.

## Headline findings

- **Most-overlapping ingest to date:** 9 of 17 originals already in the wiki; **2 are this project's own foundation** (karpathy/autoresearch = the routine's ur-pattern; teng-lin/notebooklm-py = the yt-pipeline engine).
- **8 genuinely new:** Impeccable, Ponytail, GWS, GitHub CLI, Last 30 Days, Firecrawl, Supabase CLI, Stripe CLI.
- **6 load-bearing corrections** (see source-provenance): Impeccable→Copilot REFUTED, Obsidian "founder"→CEO, autoresearch "any app"/"83 exp" overstated/unverified, Firecrawl OSS lacks Fire-engine, Stripe CLI no native LLM, GWS firing real-but-nuanced.
- **Top pilots:** Ponytail (cheapest NEW win, measured cost discipline), Supabase CLI (#1 hireui Goal-#2 fit; schema→TS-types fixes Candidate-Detail token-drift), notebooklm-py upgrade audit (own toolchain v0.3.4→v0.7.2).

## Top-3 unclosed gaps / follow-ups

1. **notebooklm-py upgrade not yet tested** — v0.3.4→v0.7.2 audit is a recommended pilot, not done (would touch the yt-pipeline; needs a branch test).
2. **`notebooklm.md` "bus factor = 1" is now stale** — verified 27 contributors; the skill's caveat should be amended (out-of-scope edit to skills/, deferred to operator).
3. **No pilot deployed yet** — this ingest produces a 20-method menu; the Goal-#2 needle only moves on actual deployment (Ponytail + Supabase recommended first).

## Suggested next action

Commit this topic on a branch `wiki/v-claude-code-plugins-stack` (per the operator's branch-don't-merge-to-main convention), report the branch, and let the operator merge. Then this week: pilot **Ponytail** on a sandbox (1h) + branch-audit **notebooklm-py v0.7.2** against the yt-pipeline smoke test.
