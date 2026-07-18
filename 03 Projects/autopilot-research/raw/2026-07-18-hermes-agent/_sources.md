# Source manifest — hermes-agent bundle (2026-07-18)

> Ingested by `/loop autopilot research <url>` (operator-submitted anchor `y96gIckJJ2Q` + full yt-search bundle, operator-elected FULL bundle + verify).
> Fetch method: `yt-dlp 2026.xx --cookies-from-browser chrome --skip-download --write-subs --write-auto-subs --sub-langs "en-orig,en,en-US,vi,vi-orig" --sub-format vtt` → `bin/vtt-to-md.py`. Read in full. **No NotebookLM** (bundle ~33.1K words EN — within direct-read range, matching the herdr decision at ~23K).
> **Block note:** transcript fetch used `--cookies-from-browser chrome` from the start (per the herdr 429 lesson) — **no 429 this run**, all 8 fetched promptly. `python` in a fresh shell resolves to system Python 2 (env shim doesn't persist across Bash calls) → convert with the venv's `python3` explicitly.
> Verification: refute-first workflow `wf_06a79485-687` (8 gatherers → merged claim set → refute-first verifiers with 3-skeptic perspective-diverse panels on the 6 hype claims → 2 completeness critics), grounded on primary sources (GitHub API ×2 endpoints, official README, hermes-agent.nousresearch.com site + docs).

## YouTube sources (8 ingested)

| # | Slug | Channel | Views | Len | Uploaded | URL | Stance |
|---|------|---------|-------|-----|----------|-----|--------|
| 1 ⚓ | t1-phan-dong-giang | Phan Dong Giang - Learn AI (VN) | 4,022 | 39:29 | 2026-07-16 | https://www.youtube.com/watch?v=y96gIckJJ2Q | **Operator anchor** — VN no-code A-Z tutorial, "Dễ Hơn OpenClaw" (easier than OpenClaw) |
| 2 | t2-networkchuck | NetworkChuck | 1,321,276 | 32:39 | 2026-05-20 | https://www.youtube.com/watch?v=QQEgIo4Juxg | **⚠️ Mega-reach hype** ("you need to use Hermes RIGHT NOW!! goodbye OpenClaw!!") — hands-on install |
| 3 | t3-tech-with-tim | Tech With Tim | 19,739 | 18:28 | 2026-07-02 | https://www.youtube.com/watch?v=86Dfgazdu-0 | Credible dev — balanced OpenClaw-vs-Hermes 2026 comparison |
| 4 | t4-sean-ai-stories | Sean's AI Stories and AutoManus | 17,384 | 20:55 | 2026-07-05 | https://www.youtube.com/watch?v=LqG1q5NpOBE | **Recurring corpus creator** (anchored agent-memory-architecture) — harness/loop/self-improving lens |
| 5 | t5-tonbi-masterclass | Tonbi's AI Garage | 28,879 | 34:20 | 2026-05-18 | https://www.youtube.com/watch?v=ZKZLko9kLm4 | Deep technical masterclass ep.3 — Memory, Plugins, Honcho, Obsidian |
| 6 | t6-elestio | Elestio | 5,408 | 11:48 | 2026-05-08 | https://www.youtube.com/watch?v=jIP0q7HEC0g | Hosting-vendor framing — self-hosted, memory, multi-platform gateway |
| 7 | t7-plastic-labs-honcho | Plastic Labs | 5,258 | 1:50 | 2026-03-16 | https://www.youtube.com/watch?v=fiCNQyYwnRw | **First-party-adjacent** (Plastic Labs MAKES Honcho) — earliest source, dialectic-memory mechanism |
| 8 | t8-ai-labs-claude-code | AI LABS | 36,599 | 13:41 | 2026-06-06 | https://www.youtube.com/watch?v=Sb96po6S67k | "Hermes Agent under Claude Code Is Insane" — Claude Code integration angle |

Word counts (EN): t1 6,734 · t2 7,059 · t3 4,339 · t4 4,387 · t5 5,476 · t6 1,954 · t7 262 · t8 2,911 = **~33,122 words**. Plus `t1-phan-dong-giang.vi.md` (VN original, 10,480 words) kept for fidelity cross-check of the anchor.

⚠️ **Caption caveats:** (t1) is the EN **auto-translation** of a Vietnamese video — names/numbers treated as unverified per the discard-as-garble guard; the VN original is retained. (t7) is a 1:50 clip (~262 words) — authoritative-but-thin on the Honcho mechanism only.

## Primary sources (ground truth for fact-check — verified by main loop 2026-07-18)

- **GitHub API** — `api.github.com/repos/NousResearch/hermes-agent` (confirmed by TWO independent endpoints, incl. the search API): **216,731★ / 40,656 forks / 23,647 open issues**, created **2025-07-22**, language **Python**, license **MIT**, latest release **v0.18.2** (CalVer tag `v2026.7.7.2`, 2026-07-08), **27 tags**, ≥100 contributors, not archived, homepage `hermes-agent.nousresearch.com`. Release names are themed ("The Judgment Release" v0.18.0, "The Surface Release" v0.16.0).
- **GitHub org** — `Nous Research` (real Organization, created 2023-05-20, 88 public repos, blog nousresearch.com).
- **README** (`raw.githubusercontent.com/NousResearch/hermes-agent/main/README.md`) — tagline "The self-improving AI agent built by Nous Research… the only agent with a built-in learning loop"; MIT; Python 3.11 (+Node); channels; `hermes claw migrate` OpenClaw import; agentskills.io + MCP; install via `curl -fsSL …/install.sh | bash`.
- **Homepage** `hermes-agent.nousresearch.com` — headline "The Agent That Grows With You"; features (learning loop, multi-channel, cron, subagents, sandboxing, web/vision/TTS); freemium **Free/Plus/Super/Ultra** tiers ("300+ models").
- **Docs** `hermes-agent.nousresearch.com/docs/` — memory (FTS5 + LLM summarization + Honcho), skills (agentskills.io + `/learn`), gateway ("20+ platforms"), 60+ tools, cron, 6 backends (local/Docker/SSH/Daytona/Singularity/Modal), providers (Nous Portal/OpenRouter/OpenAI/any endpoint), MCP, `hermes setup --portal`.
- **Honcho** — by **Plastic Labs** (t7 source); dialectic user-modeling layer used for Hermes' cross-session user understanding.

## Selection note

~40 candidates surfaced across `yt-dlp ytsearch` on "Hermes Agent Nous Research", "Hermes Agent vs OpenClaw comparison", and "Hermes Agent persistent memory skills self-hosted". Scored for relevance/credibility/recency/**stance diversity**/corpus cross-links; selected 8 with the operator's anchor (`y96gIckJJ2Q`) force-included. Balance: 1 VN no-code anchor + 1 mega-reach (NetworkChuck 1.3M views) + 1 balanced-critical (Tech With Tim) + 1 recurring-corpus-creator memory lens (Sean) + 2 deep-technical (Tonbi masterclass, AI LABS/Claude Code) + 1 infra/hosting (Elestio) + 1 first-party-adjacent mechanism (Plastic Labs/Honcho). Dropped before fetch: pure-SEO micro-channels (Julian Goldie SEO, WorldofAI, Pro Guide), sub-2-min doorway clips, and duplicate OpenClaw-vs-Hermes reviews once stance coverage was satisfied.
