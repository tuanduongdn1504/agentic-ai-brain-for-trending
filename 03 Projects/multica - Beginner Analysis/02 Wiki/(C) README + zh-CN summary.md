# (C) README + zh-CN summary — multica

> **Sources:** README.md (9KB) + README.zh-CN.md (8KB) — WebFetch 2026-04-19
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Positioning + tagline

**Description (GitHub):** *"The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, track progress, compound skills."*

**Tagline (README):** *"Your next 10 hires won't be human."*

**CN verbatim:** *"你的下一批员工，不是人类。"* (Literal: "Your next batch of employees won't be human")

### Framing analysis

**Autonomy-maximum positioning** — parallel to paperclip v14's "Open-source orchestration for zero-human companies":

| Framework | Tagline | Framing |
|-----------|---------|---------|
| paperclip v14 | "zero-human companies" | Autonomy = maximum |
| **multica v15** | **"next 10 hires won't be human"** | **Autonomy = maximum** |
| BMAD v11 | "Human Amplification, Not Replacement" | Human-centric |

**Pattern #13 (Autonomy-Framing Spectrum) reinforcement:** paperclip is no longer unique autonomy-maximum entrant. multica shares same pole. Pattern #13 strengthens — corpus has multiple explicitly autonomy-maximum projects now.

### "Managed agents platform"

"Managed" signals **T2 Agent-as-service** — SaaS + self-hosted option. User doesn't self-build agent infrastructure; multica manages runtime + orchestration.

Contrast:
- T1 (assistant): user installs framework, user drives
- T2 (service/platform): **user delegates operation to platform (multica or goclaw)**
- T5 (application): user runs standalone app (paperclip)

multica positions explicitly in T2 (service/platform) via "managed" keyword.

## 2. Core capabilities

### Task management (Linear-analog)

From CLAUDE.md: *"similar to Linear but with agents as first-class citizens"*

- **Issues-based workflow** — tasks as issues (Linear primitive)
- **Board view** — kanban-style visualization
- **Assignments** — tasks routed to agents (not humans)
- **Autonomous lifecycle:** `enqueue → claim → start → complete/fail`
- **Real-time progress** via WebSocket
- **Commenting + blocker reporting** — agents can signal human intervention needed

### Multi-workspace

- Per-workspace agents + issues + settings (isolation)
- Multiple workspaces per user
- More granular than paperclip's "Multi-Company" or goclaw's "Multi-Tenant"

### Compound skills

> *"Every solution becomes a reusable skill for the whole team."*

Skills compound team capabilities over time. Unclear architecture (no published library structure in README), but **skills-lock.json** implies external skill imports with integrity tracking.

## 3. Installation

| Method | Command |
|--------|---------|
| **Homebrew** (macOS/Linux) | `brew install multica-ai/tap/multica` (inferred format) |
| **Install script** (macOS/Linux fallback) | Shell one-liner |
| **PowerShell** (Windows) | PS installer |
| **Self-hosted** | `--with-server` flag + Docker |
| **Multica Cloud** | Cloud SaaS (hosted by multica-ai) |

**No native Docker container published** — self-hosting requires `docker-compose.selfhost.yml` separately.

## 4. Architecture overview

Per README + CLAUDE.md:

```
Next.js 16 web (apps/web)         Electron desktop (apps/desktop)
       ↓                                 ↓
       ↓     ←─── WebSocket ───→        ↓
       ↓                                 ↓
  Go backend (server/) — Chi + sqlc + gorilla/websocket
                              ↓
                         PostgreSQL 17
                         + pgvector (embeddings)
                              ↓
                         Agent Daemon (local machine)
```

### Key architectural signals

- **Next.js 16** — bleeding edge (released recently)
- **Electron desktop** — apps/desktop uses electron-vite (first desktop app in corpus)
- **Go 1.26.1** (bleeding edge Go release)
- **pgvector/pgvector:pg17** — PostgreSQL 17 with vector extension
- **sqlc** — Go SQL codegen (type-safe DB queries)
- **gorilla/websocket** — Go WebSocket library
- **Chi router** — lightweight Go HTTP router

### Local Agent Daemon

Agents run on LOCAL machine (not cloud). This matters because:
- **Privacy** — user's code stays local; not uploaded
- **Cost** — no cloud compute overhead per agent task
- **Agent choice** — local Claude Code/Codex/Cursor session
- **Multica Cloud coordinates** — but doesn't execute

Hybrid pattern: **local execution + cloud orchestration.**

## 5. Supported AI models — 8 broadcast

From README:
- **Claude Code** (Anthropic)
- **Codex** (OpenAI)
- **OpenClaw** (emerging standard; also in paperclip v14 + codymaster v12)
- **OpenCode**
- **Hermes** (also mentioned in paperclip adapter refactor)
- **Gemini** (Google)
- **Pi** (Inflection AI / Pi.ai)
- **Cursor Agent** (Cursor IDE)

**8 models = broadest BYO support in corpus** (paperclip 6, gws Claude-generic, BMAD Claude-primary).

**Model-agnostic architectural commitment** — multica doesn't privilege any provider.

## 6. Multica vs Paperclip (README has explicit section)

| Axis | Multica | Paperclip |
|------|---------|-----------|
| Focus | Team collaboration | Zero-human companies |
| Governance | Lightweight | Heavy (4 primitives + 5 invariants) |
| User model | Multi-user roles | Solo operator (multi-user roadmap) |
| Deployment | Cloud-first + self-hosted | Self-hosted primary |
| Autonomy framing | "Next 10 hires won't be human" | "Zero-human companies" |
| Stack | TS + Go + Electron | TS monorepo |
| Target | Teams with agents as teammates | Fully-autonomous company |

**multica differentiates on:**
1. **Multi-user team focus** (vs paperclip's solo operator current state)
2. **Cloud-first** (vs paperclip self-hosted-primary)
3. **Lightweight governance** (vs paperclip's constitutional 5 invariants)
4. **Linear-analog UX** (vs paperclip's company-chart)

Both are autonomy-maximum philosophically; differ on collaboration + deployment + governance weight.

## 7. Chinese README (README.zh-CN.md) — honest assessment

### Quality verdict: Machine-translated (consistent with BMAD VN, codymaster VN patterns)

**Evidence:**
- Reads naturally but post-translation-localization patterns
- All AI models listed are international (Claude/Codex/Gemini/etc) — **no Chinese models** (Zhipu/Qwen/DeepSeek) which would be expected if CN-authored
- Community channels international only (GitHub/X) — no WeChat/QQ/Zhihu
- **No CN-specific content** — same examples as EN

**Verbatim tagline CN:** *"你的下一批员工，不是人类。"*

### Depth

Same sections as EN. Full content parity. Not abbreviated.

### CN audience interpretation

- Translation suggests CJK market outreach
- No CN model integration = generic global positioning in CN language
- Compare: deer-flow v9 (ByteDance) has Chinese-primary docs + native community; multica has translation-only

### Corpus CN pattern

| Project | CN support | Origin |
|---------|-----------|--------|
| deer-flow v9 | ZH-primary docs | Native (ByteDance) |
| **multica v15** | **README.zh-CN translated** | **Machine** |

2 CN-adjacent projects in 15 wikis. Neither serves specifically VN operator (Storm Bear).

## 8. Community + positioning signals

### Community

- **X (Twitter):** @MulticaAI
- **GitHub:** multica-ai/multica + docs + issues
- **No Discord/Slack mentioned in README** (contrast paperclip's active Discord)
- **CN translation but no CN-native community**

### Company structure (vague)

- "multica-ai" org
- "Multica Cloud" offering implies commercial entity
- **No LLC/VC disclosed** (parallel to paperclip v14)
- **No individuals named**

**Community-platform archetype hypothesis fit:** ✅ likely (similar to paperclip + goclaw patterns).

## 9. Version + release

- **Current:** v0.2.6 (pre-1.0)
- **43 releases** over 2,473 commits — mature cadence (~weekly)
- **goreleaser** for Go binary distribution — professional
- **Homebrew tap** — polished distribution

## 10. Exact section headers (from README TOC)

- What is Multica?
- Features
- Quick Install
- Getting Started
- Multica vs Paperclip
- CLI
- Architecture
- Development
- Star History

**10-section structure** — cleaner than paperclip's 15+ sections.

## 11. Cross-references to T2 peer (goclaw v4)

| Axis | goclaw (v4) | multica (v15) |
|------|-------------|---------------|
| Stars | 8K | 16.2K (2× larger) |
| Tagline | "Multi-Tenant AI Agent Platform in Go" | "Your next 10 hires won't be human" |
| Primary language | Go 100% | TS 53% + Go 43% |
| Apps | CLI + web | CLI + web + **Electron desktop** |
| Agent models | Claude + Gemini | **8 models** |
| Multi-tenancy | Multi-Tenant | Multi-workspace |
| VN signals | README.vi.md + Zalo x2 | — (CN instead) |
| Author org | nextlevelbuilder | multica-ai (different) |
| License | CC BY-NC 4.0 | Likely MIT (in LICENSE file) |
| Cloud offering | Community | **Multica Cloud SaaS + self-hosted** |
| Archetype | Community-platform | Community-platform (hypothesis) |

→ Both T2 entrants align on community-platform archetype if hypothesis valid. **Pattern #9 platform-tier homogeneity evidence.**

## 12. Ecosystem cross-pollination (skills-lock.json)

multica imports 4 external skills:

| Skill | Source org | Significance |
|-------|-----------|--------------|
| frontend-design | **anthropics/skills** | **Anthropic official** skill registry |
| shadcn | shadcn/ui | Standard UI lib |
| ui-ux-pro-max | **nextlevelbuilder** | **Same org as goclaw v4!** |
| web-design-guidelines | vercel-labs/agent-skills | Vercel official |

**Major corpus-level signal:**
- **nextlevelbuilder contributes to multica** — goclaw's org shares ecosystem
- Anthropic + Vercel as reference contributors
- **skills-lock.json is first dependency-locked skill manifest in corpus** — SHA-256 integrity

## Open questions surfaced

- Funding source Q1
- nextlevelbuilder ecosystem connection Q3
- Multica Cloud pricing Q4
- 8 agent models maintenance Q7
- OpenClaw + Hermes ecosystem ownership Q8
- Chinese market strategy (why CN no VN) Q17
