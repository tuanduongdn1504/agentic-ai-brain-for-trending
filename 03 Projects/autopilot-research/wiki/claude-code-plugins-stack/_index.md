# Topic: claude-code-plugins-stack

> **Chase AI's "Use These 17 Claude Plugins, It Will Make You 10x Better."** + a double deep-dive into the original repo/source behind each of the 17. A *broad toolkit roundup* (design + productivity + data; skills + plugins + vendor CLIs), distinct from the *dev-skill stack* in [[claude-code-skills-stack/_index]] (Eric Tech, 8 skills) and the *meta-skills* in [[claude-skills/_index]] (Ben AI, 8 skills).
> **Compiled:** 2026-06-29 (path 5 yt-dlp full transcript read in full + direct primary-source `gh api`/WebFetch of all 17 originals + adversarial workflow verification `wf_81b898cf-93e` (35 agents = 17 research + 17 adversarial verify + 2 critics) + operator `gh api` ground-check).
> **Source video:** Chase AI — "Use These 17 Claude Plugins, It Will Make You 10x Better." ([V2RIVnGCy74](https://www.youtube.com/watch?v=V2RIVnGCy74), 2026-06-26, 17:30, 16.5K views). Creator already cited in [[10x-claude-code/_index]] + [[agent-dashboard-os/_index]]. Top-of-funnel for skool.com/chase-ai (paid "Claude Code Masterclass").

---

## The premise

Chase AI walks through 17 "plugins, skills, and CLIs" he actually uses, in three buckets — **Design** (Taste Skill, Impeccable, Awesome Design MD, Ponytail), **Productivity** (notebooklm-py, Playwright CLI, Codex Plugin, GWS, GitHub CLI, Skill Creator, Last 30 Days), **Data** (Firecrawl, autoresearch, Supabase CLI, Obsidian, LightRAG, Stripe CLI). For each: what it is, how it works, why you should care. See [[claude-code-plugins-stack/overview]].

**The headline for this operator is unusual: 9 of the 17 are already in your wiki — and two are this very project's own foundation.** `karpathy/autoresearch` is the ur-pattern your [[autopilot-research-routine|autopilot-research-routine]] is an explicit port of, and `teng-lin/notebooklm-py` is the engine your `yt-pipeline` skill runs on. So the value here is **a verified map + the 8 genuinely-new tools + the corrections**, not discovery. See [[claude-code-plugins-stack/originals-this-project-runs-on]].

## The 17 → their originals (all `gh api`-verified 2026-06-29)

| # | Bucket | Tool | Original | Verified | New here? |
|---|---|---|---|---|---|
| 1 | Design | Taste Skill | `leonxlnx/taste-skill` | 52.9K★ MIT, JS | covered ([[ai-web-design-workflow/_index]]) |
| 2 | Design | **Impeccable** | `pbakaus/impeccable` (Paul Bakaus) | 42.2K★ Apache-2.0, JS | **NEW** |
| 3 | Design | Awesome Design MD | `voltagent/awesome-design-md` | 94.2K★ MIT | covered ([[claude-code-skills-stack/_index]]) |
| 4 | Design | **Ponytail** | `DietrichGebert/ponytail` | 65.9K★ MIT, JS (17 days old) | **NEW** |
| 5 | Productivity | notebooklm-py | `teng-lin/notebooklm-py` | 17.0K★ MIT, Python | **you run it** |
| 6 | Productivity | Playwright CLI | `microsoft/playwright-cli` | 11.7K★ Apache-2.0 | covered ([[claude-code-skills-stack/_index]]) |
| 7 | Productivity | Codex Plugin | `openai/codex-plugin-cc` | 21.8K★ Apache-2.0 | covered ([[codex/_index]] + Storm Bear v62) |
| 8 | Productivity | **GWS** | `googleworkspace/cli` (Justin Poehnelt) | 29.1K★ Apache-2.0, Rust | **NEW** |
| 9 | Productivity | **GitHub CLI** | `cli/cli` | 45.0K★ MIT, Go | **NEW** |
| 10 | Productivity | Skill Creator | `anthropics/skills` | 156.5K★ first-party | covered ([[claude-code-skills-stack/_index]] + [[claude-skills/_index]]) |
| 11 | Data | **Last 30 Days** | `mvanhorn/last30days-skill` | 47.5K★ MIT, Python | **NEW** |
| 12 | Data | **Firecrawl** | `firecrawl/firecrawl` | 141.1K★ AGPL-3.0, TS | **NEW** |
| 13 | Data | autoresearch | `karpathy/autoresearch` | 89.1K★ MIT*, Python | **your routine's foundation** |
| 14 | Data | **Supabase CLI** | `supabase/cli` | 2.3K★ MIT, TS | **NEW** |
| 15 | Data | Obsidian | `kepano/obsidian-skills` (Steph Ango) | 38.8K★ MIT | covered ([[claude-code-skills-stack/_index]] + [[claude-code-memory-systems/_index]]) |
| 16 | Data | LightRAG | `HKUDS/LightRAG` | 37.1K★ MIT, Python | covered-mention ([[claude-code-memory-systems/_index]] L5) |
| 17 | Data | **Stripe CLI** | `stripe/stripe-cli` | 2.1K★ Apache-2.0, Go | **NEW** |

`*` autoresearch declares MIT in its README but has **no LICENSE file** (GitHub API reports `null`) — see [[claude-code-plugins-stack/source-provenance]].

## Articles

- [[claude-code-plugins-stack/overview]] — the premise, the 3 buckets, the "9-of-17 already yours" headline, the 7 cross-cutting themes, provenance summary
- [[claude-code-plugins-stack/the-17-plugins]] — full per-tool catalog (verified metadata + what it is + how it works + the video's claim + verdict)
- [[claude-code-plugins-stack/new-design-tools-impeccable]] — **NEW:** Impeccable deep-dive (44 deterministic rules + 23 commands + ALPHA live visual editor; the "GitHub made it native to Copilot" claim **REFUTED**)
- [[claude-code-plugins-stack/new-ponytail-code-minimalism]] — **NEW:** Ponytail deep-dive (7-rung "laziest senior dev" ladder; −54%/−22%/−20%/−27% Haiku benchmark verified; "Opus even more drastic" **UNVERIFIED**)
- [[claude-code-plugins-stack/new-research-tools-last30days-firecrawl]] — **NEW:** Last 30 Days (#1 GitHub Trending Mar 2026, confirmed) + Firecrawl (Fire-engine bot-evasion is **cloud-only**; "open-source = much of the same" **REFUTED**)
- [[claude-code-plugins-stack/new-infra-clis-supabase-stripe-github]] — **NEW:** the three dev-infra CLIs you shell out to — Supabase (the #1 hireui-Goal-#2 fit) + Stripe + GitHub CLI
- [[claude-code-plugins-stack/new-gws-google-workspace-firing]] — **NEW:** GWS — the Google Workspace CLI whose author *was actually fired* (confirmed), 103 agent skills, dynamic Discovery Service
- [[claude-code-plugins-stack/originals-this-project-runs-on]] — **autoresearch + notebooklm-py:** the two tools that ARE this vault's own foundation/toolchain (the routine's ur-pattern + the yt-pipeline engine), with corrections to Chase's framing
- [[claude-code-plugins-stack/already-deep-dived-crosswalk]] — the 7 covered originals (Taste Skill, Awesome Design, Playwright CLI, Codex, Skill Creator, Obsidian, LightRAG) → where they live + refreshed metadata + what this video adds
- [[claude-code-plugins-stack/video-to-original-crosswalk]] — every tool → source → what Chase adds → what the video gets wrong/omits
- [[claude-code-plugins-stack/source-provenance]] — verification ledger: confirmed / corrected / refuted / flagged (incl. the adversarial workflow + `gh api` ground-check)

## Pilot

Ranked methods to apply the toolkit to the operator's flows: `output/(C) 2026-06-29-claude-code-plugins-stack-pilot-methods.md` (methods across autopilot-vault / Storm-Bear-vault / hireui-Goal-#2 / Claude-Code-harness / Scrum-coaching, + skip list + critic's reframe). **Headline pilots:** Ponytail (cheapest NEW win — code-minimalism on agent output) + Supabase CLI (the hireui recruitment-SaaS data/auth layer) + a notebooklm-py v0.3.4→v0.7.2 upgrade audit (your own toolchain).

## Cross-links

- [[claude-code-skills-stack/_index]] — **sibling roundup** (Eric Tech, 8 dev skills); overlaps on Awesome Design MD, Playwright CLI, Obsidian, Skill Creator (same originals, different framing)
- [[claude-skills/_index]] — Ben AI's 8 *meta*-skills; Skill Creator appears in all three
- [[ai-web-design-workflow/_index]] — the **Taste Skill** deep-dive (the anti-slop design lever); Impeccable here is its closest rival (adds a live visual editor)
- [[codex/_index]] — Codex-as-adversarial-reviewer; the Codex Plugin is the install path (cross-ref Storm Bear curated v62 codex-plugin-cc)
- [[claude-code-memory-systems/_index]] — Obsidian (L1/L5 substrate) + LightRAG (L3/L5 semantic) both feature here
- [[claude-api-cost-optimization/_index]] — Ponytail (write-less-code) + Playwright-CLI-over-MCP are token-cost levers
- [[harness-engineering/_index]] — **autoresearch** is the autonomous-loop ur-pattern; Ponytail is an individual-scale discipline skill
- [[multi-agent-orchestration/_index]] — Codex adversarial review + a Firecrawl-fed candidate-screening agent
- [[graphify-codebase-graph/_index]] — Karpathy LLM-Wiki lineage; LightRAG graph-RAG vs Graphify code-graph
- [[self-hosted-devops-oss/_index]] — Firecrawl self-host + Supabase as own-your-infra
- [[prompt-evaluation/_index]] — Skill Creator's grader/comparator = LLM-as-judge
- [[10x-claude-code/_index]] — Chase AI is already a cited creator there

## Source provenance (headline)

Primary-source-grounded + adversarially verified (`wf_81b898cf-93e`, 35 agents) + **independently `gh api`-ground-checked** (every repo's stars/license/created-date confirmed against the live API 2026-06-29). All 17 originals are confirmed-real and link to exactly what Chase says. **Six load-bearing corrections** (Rule 12 fail-loud): (1) Impeccable did NOT "become native to GitHub Copilot" — *Impeccable* added a Copilot hook; users still install + enable. (2) Obsidian's kepano is **CEO**, not "founder." (3) autoresearch is **nanochat-pretraining-specific**, not "ML for any app"; its "83 experiments → 15 improvements" is **unverified**. (4) Firecrawl's open-source version **lacks** the bot-evasion (Fire-engine is cloud-only). (5) Stripe CLI has **zero** native Claude Code/LLM features. (6) GWS's firing is **real** (Justin Poehnelt) but the nuance is "fired ~2 days after Google announced its *own* CLI," not raw popularity. Full log: [[claude-code-plugins-stack/source-provenance]].
