# (C) Cluster — Microagents + LLM integrations + evaluation

> **Wiki:** v30 OpenHands
> **Cluster:** Agent ecosystem extensibility + LLM provider integration + SWE-Bench evaluation discipline
> **Source density:** Medium-High — README + SDK paper + openhands.dev workflows page + SWE-bench leaderboard
> **Status:** Cluster summary complete

---

## 1. Summary

OpenHands positions itself as **the open standard for autonomous software development** — a claim backed by three structural choices:

1. **Pre-built workflows** — Fix Vulnerabilities / Review PRs / Migrate Code / Triage Incidents (first-class product features, not community plugins)
2. **Model-agnostic LLM routing** — Claude + GPT + Minimax + OSS models via configurable routing layer
3. **SWE-Bench Verified 77.6** — top-tier measurable benchmark publicly tracked via Google Spreadsheet leaderboard

This cluster covers the agent ecosystem (what agents exist), LLM integrations (what models power them), and measurement discipline (how performance is validated publicly).

## 2. Sources in cluster

| Source | Type | Key content |
|--------|------|-------------|
| README.md — Product sections | Product docs | 5-surface taxonomy + workflow list + LLM support + trusted users |
| openhands.dev Product page | Company docs | Pre-built workflows + enterprise feature matrix |
| SDK paper arXiv 2511.03690 | Tech report | Multi-LLM routing + production agent features |
| SWE-Bench Verified leaderboard (Google Sheet) | Benchmark | 77.6 score + submission metadata |
| README.md — Trusted Users section | Adoption evidence | TikTok + Amazon + Netflix + Google + NVIDIA + Apple + VMware |

## 3. Pre-built workflows — first-class agent ecosystem

### 4 workflows highlighted on openhands.dev

| Workflow | Likely agent behavior |
|----------|----------------------|
| **Fix Vulnerabilities** | Scan repo for CVEs / insecure patterns + propose patch PRs |
| **Review PRs** | Analyze diff + suggest improvements + security/perf review (parallels Storm Bear [Skill tool: engineering:code-review]) |
| **Migrate Code** | Large refactor (framework migration / API version bump / codebase restructure) |
| **Triage Incidents** | Parse incident alerts + propose investigation + suggest remediation |

### Structural observation

These are **horizontal SWE workflows**, not vertical domain-specific (e.g., "migrate retail checkout system"). Cross-industry applicability.

**Corpus comparison:**
- [v18 agency-agents](../../../agency-agents%20-%20Beginner%20Analysis/): 144 agents across 14 divisions (vertical-specialized)
- [v27 oh-my-claudecode](../../../oh-my-claudecode%20-%20Beginner%20Analysis/): 19 specialized agents (horizontal)
- **OpenHands: 4 flagship workflows + SDK for arbitrary BYO**

OpenHands' intentional small count signals **curation over proliferation** — opposite positioning to agency-agents' 144-agent library.

### Workflow dependencies

All 4 workflows require:
- Repository read+write access (GitHub/GitLab OAuth in Cloud tier)
- LLM API access (Claude/GPT/Minimax/OSS)
- Docker runtime for sandboxed execution
- Optional: Slack/Jira/Linear integration (enterprise tier) for incident triage notifications

## 4. LLM integration architecture

### Multi-provider support (Pattern #28 6th data point)

README explicitly names supported LLMs:
- **Claude** (Anthropic)
- **GPT** (OpenAI)
- **Minimax** (used in Cloud free tier)
- **Other LLMs** (model-agnostic routing abstraction — SDK paper emphasizes this)

### Variant classification within Pattern #28

Storm Bear corpus now has 6 Pattern #28 data points with distinct implementation variants:

| Wiki | Variant | Mechanism |
|------|---------|-----------|
| v19 TrendRadar | **LiteLLM abstraction-library** | 100+ providers via `litellm` import |
| v15 multica | **Native + BYO 8 providers** | 8 explicit adapters |
| v20 fish-speech | **N/A** (not multi-LLM, TTS model) | — |
| v24 Skyvern | **Native 8+ providers** | Explicit per-provider adapters |
| v26 HF agents-course | **Multi-framework BYO curriculum** | smolagents + LangGraph + LlamaIndex |
| v27 oh-my-claudecode | **Multi-runtime orchestration** | 4 CLI runtimes (Claude + Codex + Gemini + Cursor) |
| v29 crawl4ai | **LLM-agnostic via unclecode-litellm fork** | LiteLLM-derivative after supply-chain incident |
| **v30 OpenHands** | **Native multi-LLM + SDK abstraction** | Built-in routing at SDK layer + BYO |

**v30 variant distinction:** OpenHands integrates multi-LLM routing at the **SDK-level abstraction** (not an imported library like LiteLLM; not a runtime-orchestration layer like OMC). Closer to Skyvern's native approach but with SDK-paper-documented formalization.

### Cloud tier LLM = Minimax

Interesting commercial-tier choice — Minimax (Chinese LLM) powers the free Cloud tier. Corpus-first Minimax reference. Distinct from fish-speech v20 + TrendRadar v19 CN-ecosystem references because here Minimax is **used by a US-incorporated company** for cost-efficient Cloud tier.

## 5. Evaluation discipline — SWE-Bench Verified 77.6

### Why this matters structurally

SWE-Bench Verified is the **top-tier open benchmark** for LLM-driven software engineering (2,294 real-world GitHub issues from 12 Python repos with verified acceptance tests). 77.6% resolution rate as of README publish is state-of-the-art for open-source agents.

### Pattern #8 Research-Benchmark Emergence — data point inventory

| # | Wiki | Benchmark | Venue rigor |
|---|------|-----------|-------------|
| 1 | v6 AI-Agents course | Implicit evaluation | Documentation-embedded |
| 2 | v10 autoresearch | val_bpb metric | Karpathy blog-embedded |
| 3 | v12 codymaster | SkillsBench +18.6pp | Self-declared |
| 4 | v16 graphify | 71.5× token reduction | Self-declared |
| 5 | v17 spec-kit | 48× productivity claim | Blog post |
| 6 | v20 fish-speech | Seed-TTS Eval 0.54% WER + EmergentTTS 81.88% | arXiv preprint |
| 7 | v22 LlamaFactory | ACL 2024 peer-reviewed | Top-tier ML conference |
| 8 | v24 Skyvern | WebBench 64.4% + WebVoyager 85.8% | Benchmark-specific |
| 9 | v26 HF agents-course | Unit 4 leaderboard | Course-level |
| **10** | **v30 OpenHands** | **SWE-Bench Verified 77.6** | **Top-tier SWE benchmark + ICLR-paper-validated** |

**Pattern #8 10th data point at v30.** First corpus wiki with SWE-Bench Verified specifically (distinct from training-infra, TTS, course, or browser benchmarks — SWE-agent-specific).

### Measurement discipline features

- **Public live spreadsheet** — link in README badge points to editable Google Sheet (radical transparency unusual for commercial entity)
- **Verified variant** — uses rigorous SWE-Bench Verified subset, not full SWE-Bench (handles annotation noise problem)
- **Continuous tracking** — implicit (live sheet) rather than static paper-embedded number

**Corpus-first: live-updated public benchmark spreadsheet.** Exceeds v22 LlamaFactory ACL 2024 (paper-embedded; static) in update frequency, exceeds v17 spec-kit (blog claim) in verifiability.

## 6. Adoption evidence — "Trusted Users"

### Named users in README

TikTok, VMware, Amazon, Netflix, Google, NVIDIA, Apple (+ implicit others per "trusted users" framing)

### Interpretation discipline

**What this evidence does establish:**
- OpenHands is used SOMEHOW at these organizations (some form of deployment)
- The company is comfortable listing these names (marketing claim, likely with permission)

**What this evidence does NOT establish:**
- Scale of usage at any specific org
- Whether usage is team-level pilot or org-wide standard
- Commercial spend (enterprise tier revenue)

**Corpus comparison:** First T5 wiki with named enterprise adoption. v22 LlamaFactory had HuggingFace + ModelScope + Modelers hubs (infra adoption). Others didn't list enterprise users.

## 7. Cluster synthesis

### The three-legged stool

OpenHands' claim to be the "open standard" rests on:

1. **Ecosystem** (pre-built workflows + BYO SDK + 188+ contributors) — community leverage
2. **Flexibility** (multi-LLM routing + Docker-native runtime + 5 deployment surfaces) — technical optionality
3. **Measurement** (SWE-Bench 77.6 + live leaderboard + 2 peer-reviewed papers) — credibility

All three legs are structurally **open** (MIT + public papers + public leaderboard), which makes the "open standard" positioning defensible.

### Storm Bear relevance

For the Storm Bear operator:
- **Review PRs workflow** → candidate for internal Scrum team code-review automation
- **Triage Incidents workflow** → candidate for customer-facing incident triage pipeline
- **Fix Vulnerabilities workflow** → CVE-scan + PR automation for VN client engagements
- **SDK composability** → could build a Scrum-coaching-agent on OpenHands runtime (vs stdlib Python)

### Cross-wiki signals

- **Pattern #19 community-viral lineage**: OpenDevin→OpenHands rebrand parallels fish-speech "origin story" + BabyAGI/AutoGPT-cited-by-Skyvern. Community-viral narrative with academic paper anchor is the fusion.
- **Pattern #27 Community-Viral Scale Path**: 71.7K / 25 months = ~2,900 stars/month sustained. 8th data point. Neither pure-solo (crawl4ai) nor pure-community (paperclip) — **corporate-academic-amplified** sub-path.
- **Pattern #9 Multi-Axial Tier Bifurcation**: T5 N=5 with 5 distinct archetypes = 100% diversity-per-wiki maintained. Resolution D stays leading model.

**Next cluster:** All Hands AI company + research paper lineage + community governance → deeper into organizational archetype + Pattern #17 + #19 + #31 + #32 + #42 + #44 data points.
