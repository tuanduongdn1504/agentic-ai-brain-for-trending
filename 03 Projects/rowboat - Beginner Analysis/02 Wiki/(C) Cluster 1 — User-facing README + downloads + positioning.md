# (C) Cluster 1 — User-facing README + downloads + positioning

**Sources:** README.md (156 lines, 6.4KB) + google-setup.md (156 lines, 3.9KB) + GitHub repo metadata + rowboatlabs.com landing page + downloads page

## 1. Verbatim positioning

- **One-liner (header):** *"Open-source AI coworker that turns work into a knowledge graph and acts on it"*
- **Description:** *"Rowboat connects to your email and meeting notes, builds a long-lived knowledge graph, and uses that context to help you get work done - privately, on your machine."*
- **Landing page tagline (rowboatlabs.com):** *"Your AI coworker, with memory"*
- **Local-first claim:** *"Rowboat is a local-first AI coworker"*
- **Vault claim:** *"Under the hood, Rowboat maintains an Obsidian-compatible vault of plain Markdown notes with backlinks — a transparent 'working memory' you can inspect and edit."*
- **Differentiator (verbatim):** *"Most AI tools reconstruct context on demand by searching transcripts or documents. Rowboat maintains long-lived knowledge instead: context accumulates over time, relationships are explicit and inspectable, notes are editable by you, not hidden inside a model, everything lives on your machine as plain Markdown. The result is memory that compounds, rather than retrieval that starts cold every time."*

## 2. Repo metadata (GitHub API as of 2026-04-24)

| Field | Value |
|---|---|
| Stars | 13,056 |
| Forks | 1,266 (9.7% fork ratio) |
| Subscribers | 72 |
| Watchers (legacy GitHub field) | 13,056 |
| Open issues | 98 |
| Size | 79.5 MB |
| Created | 2025-01-13 (~15.5 months) |
| Last push | 2026-04-24 (today) |
| Default branch | main |
| Language | TypeScript 96.7% |
| License | Apache-2.0 |
| Homepage | https://www.rowboatlabs.com |
| Topics | productivity, open-source, ai, orchestration, multiagent, agents, ai-agents, llm, generative-ai, chatgpt, openai, ai-agents-automation, **claude-code**, agents-sdk, **claude-cowork** |

**Velocity:** ~840 stars/month sustained-organic over 15.5 months. **YC S24-amplified-community sub-path** of Pattern #27.

**Topic signals:** explicit `claude-code` + `claude-cowork` + `agents-sdk` topics — Anthropic-runtime-aligned positioning at T5. First T5 in corpus to claim `claude-cowork` topic as identity signal.

## 3. README structure (9 top-level sections)

1. Demo (YouTube embed + Trendshift badge + Discord + Twitter + **YC S24 badge** corpus-first project-level YC-batch acknowledgment)
2. Installation (Mac/Windows/Linux desktop binaries + GitHub releases + Google setup)
3. What it does (3-claim: Remember / Understand / Help you act + Obsidian-compatible vault claim)
4. Integrations (Gmail + Google Calendar + Rowboat-meeting-notes OR Fireflies + Composio.dev product library)
5. How it's different (long-lived-knowledge vs retrieval-cold-start framing)
6. What you can do with it (Meeting prep / Email drafting / Docs & decks / Follow-ups / On-your-machine help)
7. Live notes (`@rowboat` mention triggers live-updating note; tracks competitor/market topics across X/Reddit/news)
8. Bring your own model (Local Ollama/LM Studio + Hosted with BYO-API-key; data stays in local Markdown vault)
9. Extend with MCP + Local-first by design (footer)

## 4. Distribution surfaces (4-surface CORPUS-FIRST T5)

| Surface | Mechanism | Target audience | Status |
|---|---|---|---|
| **Mac/Windows/Linux desktop binaries** | rowboatlabs.com/downloads + GitHub releases | End users (personal-productivity audience) | Primary distribution since pivot |
| **Docker compose** | docker-compose.yml in repo root (legacy SaaS deployment) | Self-hosters (legacy multi-agent SaaS audience) | Maintained-but-secondary |
| **npm `@rowboatlabs/rowboatx` v0.16.0** | Hono server + ink CLI; `rowboatx` bin | Developers integrating CLI server | Active (v0.16.0 = 16 minor releases) |
| **PyPI `rowboat` v5.0.1** | `pip install rowboat`; Python SDK by Ramnique Singh | Developers integrating with API | Active (v5.x mature) |

**Corpus-first signal:** No prior T5 wiki has 4-surface distribution. DeepTutor v38 had 1 surface (Streamlit web). browser-use v41 had 2 (pip + Browser-Use Cloud). OpenHands v30 had 5 surfaces (SDK + CLI + GUI + Cloud + Enterprise) — comparable but commercial-tier-heavy. Rowboat's 4-surface is OSS-only (Apache-2.0).

## 5. Integration ecosystem (6 user-configurable + framework abstractions)

| Integration | Config file | Type | Notes |
|---|---|---|---|
| **Google (Gmail/Calendar/Drive)** | OAuth credentials via google-setup.md guided flow | Native | 156-line setup guide; OAuth Web App type; localhost:8080 callback |
| **Deepgram** (voice STT) | `~/.rowboat/config/deepgram.json` | Optional | Voice input + voice notes |
| **ElevenLabs** (voice TTS) | `~/.rowboat/config/elevenlabs.json` | Optional | Voice output |
| **Exa** (research search) | `~/.rowboat/config/exa-search.json` | Optional | Web research |
| **Composio** (external tool marketplace) | `~/.rowboat/config/composio.json` | Optional | Generic external tool bridge |
| **MCP servers** | Generic Model Context Protocol | Optional | Any MCP-compatible server |
| **Fireflies** (alternative meeting notes) | (mentioned but not detailed) | Optional alternative | Alternative to Rowboat-built-in meeting notes |
| **Klavis** (cloud agent infra) | Env var KLAVIS_API_KEY (in start.sh) | Optional | Klavis = third-party MCP cloud platform |

**6 explicit user-configurable integrations + 2 mentioned-but-not-detailed (Fireflies + Klavis) = 8 total integration touchpoints.**

**Standardized config format** — every API key file uses `{ "apiKey": "<key>" }`. Discoverable + deterministic. Corpus-first standardized config-file-format-discipline at T5.

## 6. Google setup workflow (156 lines, 7-step)

1. Open Google Cloud Console
2. Create new project (e.g. "Rowboat Integration")
3. Enable Gmail + Calendar + Drive APIs (3 services)
4. Configure OAuth consent screen (External audience, Testing mode acceptable)
5. Add test users (manual addition required in Testing mode)
6. Create OAuth Client ID (Web application type, redirect URI `http://localhost:8080/oauth/callback`)
7. Copy Client ID + Secret into Rowboat

**Embedded screenshots:** 5 image links to apps/docs/docs/img/google-setup/ (proper docs-site asset pipeline).

**Troubleshooting section:** 1 common-error walkthrough (Authorization Successful but app shows error) with 3 diagnostic steps.

**Observation:** 156-line dedicated setup doc for a single integration is corpus-most-elaborate Google-Workspace-integration-setup at T5. gws v13 (T4 Google Workspace CLI) had its own setup but as part of broader documentation. Rowboat's setup-doc-as-standalone reflects YC-startup attention to onboarding friction reduction.

## 7. Live notes feature (`@rowboat` mention)

- Type `@rowboat` on a note → live note created
- Use cases: track competitor / market topic across X+Reddit+news; monitor person/project/deal across web+communications; running summary of any subject
- Everything written back to local Markdown vault
- "You control what runs and when" (user-controlled scheduling)

This is the **Track Blocks** primitive surfaced as user-facing feature. See Cluster 2 + Entity 1 for technical depth.

## 8. Bring-your-own-model claim

- **Local models:** Ollama + LM Studio (corpus-first explicit LM Studio mention)
- **Hosted models:** BYO API key/provider
- **Swap-anytime claim** — your data stays in local Markdown vault (independence from model choice)

This is **Pattern #28 Multi-Provider AI Support** strengthening at T5 with local+hosted hybrid. From package.json (Cluster 2) we'll see Vercel AI SDK + 5+ explicit provider packages.

## 9. Local-first design claims (3 explicit guarantees)

1. All data stored locally as plain Markdown
2. No proprietary formats or hosted lock-in
3. You can inspect/edit/back up/delete everything any time

**Corpus context:** Local-first framing strongest in corpus at T5. crawl4ai v29 was tool-local but data-flow ambiguous. Rowboat's local-first-by-design discipline = corpus-first explicit local-first-personal-productivity at T5.

**Caveat (not stated in README):** When using hosted LLMs (OpenAI / Anthropic / etc.), prompts + context get sent to provider. Local-first applies to data-at-rest, not data-in-flight. Local Ollama/LM Studio mitigates this fully.

## 10. Demo + community surfaces

- **YouTube demo:** youtube.com/watch?v=7xTpciZCfpw (linked from README hero)
- **Discord:** discord.gg/wajrgmJQ6b (named server)
- **Twitter:** @rowboatlabshq (org account)
- **Trendshift badge:** repository 13609 (signals viral discovery via Trendshift platform)
- **YC S24 badge:** Y Combinator badge in header (project-level, not just commercial-page)

**Corpus-first Pattern #50 evidence:** rowboatlabs.com (commercial) + downloads page + Discord + YouTube + Twitter + Trendshift + YC = **7-surface commercial-funnel companion-platform** = strongest funnel signal in corpus tied with ruflo v42 for #50 reinforcement.

## 11. Star-the-repo CTA

*"⭐ If you find Rowboat useful, please star the repo. It helps more people find it."*

In-README explicit star-CTA is conventional. Distinguishes from claude-hud v35 (consent-gated LLM-ask-for-star = corpus-first within-product star solicitation).

## 12. License + ethical framing

**License:** Apache-2.0 standard (LICENSE file 11.1KB / 201 lines = unmodified Apache-2.0).

**No ethical framing required** in beginner guide. Standard Apache-2.0 + clear OSS commercial entity (YC-backed) + no perverse incentive observed + no autonomy-max framing + no data-leak risk surface beyond standard LLM-API disclosure.

**Privacy framing:** "privately, on your machine" + "everything lives on your machine as plain Markdown" + "data stays in your local Markdown vault" — privacy-first language used 4+ times in README. Counter-balances LLM-API-data-flow caveat naturally.

## 13. Cluster 1 corpus-firsts (target tally)

| # | Observation | Confidence |
|---|---|---|
| 1 | YC S24 batch as project-level README badge (not just commercial-page) | HIGH (first explicit YC-batch in repo header in 43 wikis) |
| 2 | `claude-cowork` repo topic as identity signal | HIGH (first in corpus) |
| 3 | 4-surface distribution at T5 (desktop + Docker + npm + PyPI all OSS) | HIGH (no prior T5 has 4 OSS-only surfaces) |
| 4 | Standardized `{ "apiKey": "<key>" }` config-file-format-discipline | HIGH (first explicit cross-integration standardization in corpus) |
| 5 | Local-first-personal-productivity explicit positioning at T5 | HIGH |
| 6 | Knowledge-graph-as-Markdown explicitly Obsidian-compatible at T5 | HIGH (Storm Bear vault peer-category) |
| 7 | "Memory compounds vs retrieval cold-start" framing at T5 | MEDIUM (similar framing exists in Mem0/Letta but not in Storm Bear corpus prior) |
| 8 | 7-surface commercial-funnel (rowboatlabs.com + downloads + Discord + YouTube + Twitter + Trendshift + YC) | HIGH (ties ruflo v42; distinct funnel-component composition) |
| 9 | 156-line dedicated single-integration setup doc (Google) | HIGH (most elaborate integration onboarding in corpus) |
| 10 | "AI coworker" framing as primary noun at T5 | MEDIUM (distinct from "AI assistant" / "AI agent" common framing) |

## 14. Cross-pattern observations

- **Pattern #17 variant 3 commercial-startup** — Rowboat Labs YC-S24 = 14th data point strengthening (within-pattern; do NOT register YC-S24 as sub-variant standalone)
- **Pattern #19 archetype 1 (Karpathy)** — implicit structural parallel via Obsidian-vault-as-knowledge-graph framing; NOT explicitly cited; **observational corpus-first implicit-not-explicit Karpathy structural parallel**
- **Pattern #27 Community-Viral** — 19th observation; YC-S24-amplified-community sub-path
- **Pattern #28 Multi-Provider** — strengthening; local Ollama + LM Studio + hosted BYO
- **Pattern #50 Commercial-Funnel** — 6th data point strengthening; 7-surface funnel
- **Pattern #2 Distribution Evolution** — 4-surface at T5 corpus-first observational data point
- **Pattern #22 AGENTS.md** — counter-evidence (CLAUDE.md present 5.4KB, AGENTS.md absent); T5 YC-startup-stage Anthropic-runtime-aligned

## 15. Cluster 1 absences (informative)

- No CONTRIBUTING.md mentioned in README (verified absent in repo)
- No SECURITY.md
- No CODE_OF_CONDUCT.md
- No AGENTS.md (CLAUDE.md present instead — Anthropic-runtime alignment)
- No i18n (no VN/CN/JA/KO/Ukrainian etc. — EN-only at 13K T5)
- No formal SECURITY policy mentioned despite handling Gmail OAuth credentials + LLM API keys
- No mention of PostgreSQL/MongoDB-as-knowledge-store-alternative (Markdown is THE only store; principled choice)
- No mention of MOBILE/iOS/Android (desktop-only intentional at v1)
- No mention of TEAM/multi-user (personal-coworker positioning intentional; legacy `apps/rowboat` had multi-user via Auth0)
