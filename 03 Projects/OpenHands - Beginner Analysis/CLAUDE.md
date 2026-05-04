# OpenHands - Beginner Analysis

Đọc, phân tích, và viết wiki song ngữ về [`OpenHands/OpenHands`](https://github.com/OpenHands/OpenHands) — **"🙌 OpenHands: AI-Driven Development"** (f.k.a. OpenDevin).

**71,704 stars (#5 in corpus — between LlamaFactory v22 70.3K and Unsloth v23 62.2K; ABOVE crawl4ai v29 64K), 9,030 forks (12.6%), MIT core (enterprise dir separate license → license field `NOASSERTION`), Python 71.4% + TypeScript 26.8%, main-branch, created 2024-03-13 (~25 months old), pushed 2026-04-22 (today), 315 MB (largest T5 in corpus by 2×+), 410 open issues, 433 watchers, homepage openhands.dev**. Organization: **All Hands AI** (commercial-entity). **3 named founders:** Xingyao Wang (UIUC PhD candidate + SWE-bench contributor) + Graham Neubig (CMU Professor) + Robert Brennan (software engineer). **Funding:** $18.8M disclosed on openhands.dev. **Research lineage:** ICLR 2025 (arXiv 2407.16741 OpenHands/OpenDevin paper, 23+ authors across multiple institutions) + November 2025 SDK paper (arXiv 2511.03690).

**Scope status: T5 Agent-as-application — 5TH T5 entrant.** T5 extends from N=4 to N=5.

**Tagline (README verbatim):** *"OpenHands: AI-Driven Development"* + mission *"the open standard for autonomous software development"* + *"secure, transparent, model-agnostic coding agents."*

**Origin:** Published June 2024 as OpenDevin ("an open platform for AI software developers as generalist agents"), direct open-source response to Cognition Labs' Devin demo. Rebranded to OpenHands. Accepted ICLR 2025 with 23-author paper spanning UIUC + CMU + Carnegie Mellon + multiple institutions. Follow-up SDK paper (Nov 2025) formalizes the production SDK with additional authors.

**Core product — composable AI software engineering agent stack:**

| Component | Purpose |
|-----------|---------|
| **Software Agent SDK** | Composable Python library — define agents locally, deploy to cloud (first-class product per Nov 2025 paper) |
| **CLI** | Terminal interface compatible with Claude, GPT, Minimax + other LLMs (Claude Code-like) |
| **Local GUI** | Desktop app — REST API + React frontend (Devin-like / Jules-like local experience) |
| **Cloud Platform** | Hosted at openhands.dev — free tier via GitHub/GitLab login + Minimax; enterprise tier with Slack/Jira/Linear integration, multi-user |
| **Enterprise Edition** | Self-hosted Kubernetes + RBAC + collaboration (separate license — not MIT) |
| **Pre-built workflows** | Fix Vulnerabilities / Review PRs / Migrate Code / Triage Incidents |

**Key architecture signals (from SDK paper arXiv 2511.03690):**
- **Native sandboxed execution** — Docker-based runtime
- **Lifecycle control** — pause, resume, observe agent state
- **Model-agnostic multi-LLM routing** — Claude, GPT, Minimax, open models
- **Built-in security analysis** — agent actions reviewable pre-execution
- **Local-to-remote execution portability** — same agent runs locally or in cloud
- **Integrated REST/WebSocket services** — first-class API surface
- **VS Code + VNC browser + CLI** — multi-interface environments

**SWE-Bench Verified: 77.6** (prominent README badge, link to live spreadsheet). **State-of-the-art OSS SWE agent as of 2026-04**. First corpus wiki with SWE-Bench Verified as headline metric.

**Adoption signals (README):** TikTok, VMware, Amazon, Netflix, Google, NVIDIA, Apple listed as "Trusted Users."

**8 README translations** (de / es / fr / ja / ko / pt / ru / zh via readme-i18n.com). Ties fish-speech v20 + oh-my-claudecode v27 for top i18n breadth.

**Governance & community:**
- **COMMUNITY.md:** "benevolent dictator model" — "engineers, academics, and enthusiasts reimagining software development for an AI-powered world"
- **Core values:** High Openness + High Agency
- **Slack:** dub.sh/openhands (primary community channel)
- **Roadmap:** public ("plans, work, successes, failures all public record")
- **101+ releases** (latest 1.6.0 March 2026)

**Commercial path:** **Confirmed open-core commercial entity.**
- **MIT core:** openhands, agent-server Docker images
- **Separate licensing:** enterprise directory
- **Cloud:** free tier + paid enterprise tier
- **Funding:** $18.8M raised

**v2 Routine 12-axis classification:**

| Axis | Value |
|------|-------|
| **Tier** | **T5 Agent-as-application (5TH entrant)** |
| **Archetype** | **Academic-commercial-fusion-open-core-commercial-entity** (NEW T5 variant — merges research-paper-chain + open-core commercial + named academic-lab affiliation) |
| **Scale tier** | **71.7K stars** (#5 corpus; largest T5 entry by 15%+ over autoresearch 74K note: autoresearch is Karpathy solo-known; OpenHands = commercial-backed at similar scale) |
| **Primary lang** | Python 71.4% + TypeScript 26.8% |
| **Packaging** | Docker (primary) + pip SDK + CLI + Cloud hosted + Kubernetes (enterprise) |
| **Origin story** | Founded 2024-03 as open-source response to Devin demo; academic-commercial fusion (UIUC + CMU + All Hands AI company) |
| **Methodology** | Action-Observation agent loop + sandboxed runtime + multi-LLM + BYO agent architecture via SDK |
| **Governance files** | README + COMMUNITY.md + LICENSE (MIT + separate enterprise) + CONTRIBUTING (implied) + public roadmap + Slack + 101 releases |
| **Agent/skill count** | SDK primitives + pre-built workflows (Fix Vulns / Review PRs / Migrate Code / Triage Incidents) + BYO agents |
| **i18n** | **8 languages** (de/es/fr/ja/ko/pt/ru/zh) — tied top 3 in corpus |
| **Intellectual influence** | **Explicit OpenDevin research paper lineage (ICLR 2025, 23+ authors)** + SDK paper (arXiv 2511.03690 Nov 2025) + SWE-bench research integration (Xingyao Wang contributor) + Devin-response (open-source counterpart positioning) |
| **Agent platforms** | CLI + Local GUI + Cloud + Enterprise Kubernetes + SDK (most deployment surfaces in corpus for T5; 5 surfaces matches crawl4ai v29's 3 but broader T5-specific) |

**Tier placement rationale:** T5 Agent-as-application — OpenHands is an autonomous software-engineering agent application (not a framework for building agents: T1; not a training utility: outside-scope; not a content-bridge: T4; not a platform-for-agents: T2). Equivalent T5 peers: deer-flow v9 (research-agent application) / autoresearch v10 (ML-research application) / paperclip v14 (orchestration application) / Skyvern v24 (browser-automation application). OpenHands is **SWE-agent application** — a novel T5 sub-domain.

**T5 extends to N=5** (from N=4 post-v24). 5 distinct organizational archetypes now:
- **T5-corporate:** deer-flow (ByteDance)
- **T5-solo-known-figure:** autoresearch (Karpathy)
- **T5-community-platform:** paperclip
- **T5-commercial-entity-pure:** Skyvern
- **T5-academic-commercial-fusion:** OpenHands (NEW v30)

**v30 pattern implications preview:**

- **Pattern #9 Multi-Axial Tier Bifurcation (confirmed, Resolution D at 65% leading model at v19)** — T5 now 5 archetypes at N=5, more archetype-diverse than T4 N=6 (which had 6 archetype variants). T5 maintains 100% diversity-per-wiki.
- **Pattern #17 Ecosystem-Layer Organizations (confirmed, 7+ data points)** — All Hands AI is commercial-startup-ecosystem with academic co-founder anchor (CMU Neubig). 4th archetype variant data point at minimum (or fusion of variants 2+3).
- **Pattern #19 Intellectual Lineage Archetypes (confirmed v20, 4 archetypes at N≥2)** — OpenHands is **research-paper-chain archetype** (4th archetype, ICLR 2025 paper with 23+ authors + SDK paper). **6th data point of Pattern #19 research-paper-chain archetype** (joins fish-speech v20 TTS chain + LlamaFactory v22 PEFT/QLoRA chain + Unsloth v23 optimizer chain).
- **Pattern #27 Community-Viral Scale Path (confirmed v21, 7 data points at v29)** — 71.7K in 25 months = ~2,900 stars/month organic. Corporate-academic-amplified sub-path distinct from pure-solo-organic (crawl4ai) or pure-community-viral (paperclip). 8th data point.
- **Pattern #28 Multi-Provider AI Support (confirmed v25, 5 data points at v29)** — Claude + GPT + Minimax + model-agnostic-routing = 6th data point. Native multi-provider (BYO) variant.
- **Pattern #29 License-Category Diversity (confirmed v21)** — MIT core + separate enterprise license = split-licensing-via-directory (distinct from #45 Dual-Licensing Strategy which is dual-OSS). Potentially strengthens #31 Open-Core rather than #45.
- **Pattern #31 Open-Core Commercial Entity (confirmed v24 at N=2)** — **3rd data point CONFIRMED** at v30 (not just pending as for crawl4ai). OpenHands satisfies all 4 criteria: commercial entity founded around product, OSS core, proprietary enterprise tier, commercial tier differentiator (Kubernetes self-hosted + RBAC). **Pattern #31 strengthens from N=2 to N=3.**
- **Pattern #32 Research-Paper-Chain Lineage (confirmed v22 at N=2)** — OpenHands ICLR 2025 paper (23 authors) + SDK paper (Nov 2025 11 authors) = 2nd data point for fully-academic-peer-reviewed + multi-paper chain. **Pattern #32 strengthens from N=2 to N=3.**
- **Pattern #42 Academic-Published Peer-Reviewed Framework (STALE-CANDIDATE flagged v27, N=1 at LlamaFactory v22)** — OpenHands ICLR 2025 acceptance = **N=2 VALIDATION** (peer-reviewed at top ML venue). **Pattern #42 UN-STALE + potentially PROMOTE to CONFIRMED at v30 under structurally-unambiguous-at-N=2 criterion.**
- **Pattern #44 Academic-Lab Affiliation Archetype (STALE-CANDIDATE flagged v27, N=1 at LlamaFactory v22)** — Graham Neubig CMU + Xingyao Wang UIUC = **N=2 data point with multi-institutional academic affiliations.** **Pattern #44 UN-STALE + potentially PROMOTE to CONFIRMED at v30 under N=2 multi-institutional criterion.**

**NEW candidates at v30 (targeting 2-3 to stay near 1:1 ratio — pre-check against overlap per v29 Phase 5 action item #3):**

- **#67 Academic-Commercial Fusion Archetype** — founders span academic institution + commercial company simultaneously (not sequential-to-commercial transition); corpus data points = OpenHands (UIUC PhD + CMU faculty + LLC) + potentially LlamaFactory v22 if Lab4AI has commercial wrapper (TO VERIFY). Distinct from #17 ecosystem-layer (which is commercial-only) and #31 open-core (which doesn't require academic co-founder). **N=1 at v30, observation-track if overlap with #31 too high.**
- **#68 SWE-Agent Domain-Specific T5 Sub-Type** — T5-Application with SWE-specific focus (vs research-agent deer-flow / ML-research autoresearch / orchestration paperclip / browser Skyvern). First SWE-focused T5 in corpus; observational-only until N=2 emerges.
- **#69 Open-Source-Devin-Response Archetype** — positioning as OSS counterpart to proprietary closed-source agent (Devin → OpenHands). Observational. May relate to Pattern #13 Autonomy-Framing Spectrum (framing by opposition).

**⚠️ Candidate-registration discipline:** v29 Phase 5 action item #3 requires pre-check overlap. #67 overlaps Pattern #31 + #42 + #44 significantly — **recommend REGISTER as observation-track or defer pending audit.** #68 is speculative sub-type — **defer.** #69 overlaps Pattern #13 — **defer or observation-track.** Final plan: **register 1-2 candidates maximum; prefer promoting existing candidates (#42 + #44) over new registration.**

**Revised plan for Phase 5 pattern updates:**
1. **Pattern #31 strengthen to N=3** (data-point add, no status change)
2. **Pattern #32 strengthen to N=3** (data-point add, no status change)
3. **Pattern #42 PROMOTE candidate N=1→N=2 (un-stale)** — propose promotion at next audit
4. **Pattern #44 PROMOTE candidate N=1→N=2 (un-stale)** — propose promotion at next audit
5. **Pattern #17 Ecosystem-Layer** — 8th data point (commercial-startup academic-fusion variant)
6. **Pattern #27 Community-Viral** — 8th data point (corporate-academic-amplified sub-path)
7. **Pattern #28 Multi-Provider** — 6th data point
8. **Pattern #9** — T5 N=5 = more archetype-diverse than T4 N=6 per-wiki — Resolution D holds
9. **Pattern #19** — 6th research-paper-chain archetype data point
10. **NEW candidate: #67 Academic-Commercial Fusion Archetype** — register if audit post-v30 keeps ratio healthy

**Post-v30 ratio projection:** 28 confirmed + 28 active + 1 new (if #67 registered) = 29 active candidates. Ratio 28:29 = **0.97:1** (below 1.00 trigger). ✅ Safe.

## Claude's Role

Claude là wiki maintainer, chạy bằng routine `llm-wiki-routine-v2.md` (**30th auto-execution, 12th v2 routine execution**):

- **Ingest sources via WebFetch + API probe** — GitHub API + README + arXiv 2511.03690 + arXiv 2407.16741 + openhands.dev + COMMUNITY.md
- **Cross-reference với 29 sibling wikis** — primarily T5 peers (deer-flow v9 / autoresearch v10 / paperclip v14 / Skyvern v24) + research-paper-chain peers (fish-speech v20 / LlamaFactory v22 / Unsloth v23) + academic-lab peer (LlamaFactory v22)
- **Phase 4b = T5 5-way comparison + Pattern #31 + #32 + #42 + #44 strengthening + possible candidate #67**
- **Beginner angle** — VN/EN developer + Storm Bear Scrum coach use cases (PR review / retro automation / code migration workflows)

**Prime directive:** Outcome = wiki + T5 extends to N=5 + Pattern #31 strengthens to N=3 + Pattern #32 strengthens to N=3 + Pattern #42 + #44 un-stale via N=2 validation.

## Process — routine `llm-wiki-routine-v2.md`

7 phases. 12th v2 routine execution. Phase 4b = T5 5-way + pattern strengthening + minimal new candidate registration (discipline from v29 action item #3).

## Key People

- **Xingyao Wang** — UIUC PhD candidate + SWE-bench contributor + All Hands AI co-founder; 1st author on both ICLR 2025 + SDK Nov 2025 papers
- **Graham Neubig** — CMU Professor + All Hands AI co-founder; senior author ICLR 2025 paper
- **Robert Brennan** — software engineer + All Hands AI co-founder
- **ICLR 2025 paper co-authors (23+):** Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li, Jaskirat Singh, Hoang H. Tran, Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian, Yanjun Shao, Niklas Muennighoff, Yizhe Zhang, Binyuan Hui, Junyang Lin, Hao Peng, Heng Ji (multi-institutional academic collaboration)
- **SDK paper co-authors:** Simon Rosenberg, Juan Michelini, Calvin Smith, Hoang Tran, Engel Nyst, Rohit Malhotra, Xuhui Zhou, Valerie Chen + 3 shared with ICLR paper
- **Cross-project:** 29 sibling wikis. This is 30th = T5 N=5 + research-paper-chain 3rd validation + 21st consecutive Storm Bear meta-entity.

## Folder Structure

```
OpenHands - Beginner Analysis/
├── CLAUDE.md
├── 00 Sources/
├── 01 Analysis/
├── 02 Wiki/
├── 03 Published/
├── 04 Reviews/
```

## Rules & Conventions

- **`(C)` prefix** + song ngữ VN + 13-section format
- **Cross-reference 29 siblings MANDATORY** — especially T5 peers + research-paper-chain peers + academic-affiliation peer
- **Pattern Library direct update** — strengthen #31, #32, #42, #44; +1 new candidate maximum (#67 if discipline allows)
- **Discipline: register fewer candidates** (v29 action item #3) — prioritize strengthening existing over new registrations

## Current Status

> **Last updated:** 2026-04-22
> **Status:** 🟡 Routine v2 auto-execute IN PROGRESS — 30th LLM Wiki, 12th v2 execution, T5 N=5 extension, research-paper-chain 3rd data point, Pattern #31 + #32 strengthen to N=3

### Expected milestones

- [x] Phase 0 Pre-flight (probe + guard; ratio 1.00:1 cleared by v29 audit; v30 cleared to build)
- [x] Phase 1 Scaffold
- [ ] Phase 2 Source ingestion (3 clusters)
- [ ] Phase 3 Entity pages (4)
- [ ] Phase 4a Beginner guide
- [ ] Phase 4b T5 5-way + Pattern #31/#32/#42/#44 strengthening + ≤1 new candidate
- [ ] Phase 5 Iteration log v30
- [ ] Phase 6 Vault updates
