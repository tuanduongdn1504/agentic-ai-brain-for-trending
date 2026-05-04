# (C) README summary — paperclip

> **Source:** `README.md` — WebFetch 2026-04-19
> **Status:** ✅ Phase 2 source summary
> **Parent index:** [[(C) index]]

---

## 1. Positioning + radical framing

**Tagline:** *"Open-source orchestration for zero-human companies"*

**Core metaphor (verbatim):** *"If OpenClaw is an employee, Paperclip is the company."*

**Signals:**
- **Autonomy-forward positioning** — "zero-human" is literal target, not hedged
- **Orchestration over execution** — Paperclip doesn't DO the work; it orchestrates agents that do
- **Company-scale abstraction** — not single-agent, not multi-agent, but "company" as primitive
- **AI alignment theory name** — "paperclip" = Nick Bostrom's paperclip maximizer thought experiment (1977 AI-safety illustration of unintended instrumental convergence)

**Philosophical polar-opposite to BMAD v11:**
- BMAD: "Human Amplification, Not Replacement"
- paperclip: "Zero-human companies"
- Corpus now has **explicit autonomy spectrum** with both poles named.

## 2. What paperclip actually does (capabilities)

From README Features section:

### 9 named features

1. 🔌 **Bring Your Own Agent (BYO Agent)** — works with OpenClaw, Claude Code, Codex, Cursor, Bash, HTTP endpoints
2. 🎯 **Goal Alignment** — tasks trace back to company mission
3. 💓 **Heartbeats** — scheduled/recurring execution (no manual kickoff)
4. 💰 **Cost Control** — per-agent budget enforcement with hard-stops
5. 🏢 **Multi-Company** — complete data isolation between orgs
6. 🎫 **Ticket System** — agent work intake queue
7. 🛡️ **Governance** — approval gates + manual agent override/termination
8. 📊 **Org Chart** — hierarchical teams with roles and reporting lines
9. 📱 **Mobile Ready** — mobile-accessible UI

### Core capabilities

- Task assignment + delegation across agent hierarchies
- Persistent agent sessions across reboots
- Scheduled execution ("Heartbeats")
- "Agents run autonomously 24/7 with human oversight"
- "Work on tasks until it's done"

### Use cases (from README)

- Autonomous note-taking apps
- Customer support
- Social media management
- Recurring business tasks

**Interpretation:** Paperclip is a **control plane for AI-agent companies.** The user defines: company mission, org structure, budgets, approval rules. Paperclip assigns tasks to agents, tracks cost, enforces governance, persists state.

## 3. Architecture overview

**Full-stack monorepo** (pnpm workspaces):

- **Node.js server** (Express API + Drizzle ORM)
  - Embedded PGlite for local development
  - External PostgreSQL for production
  - API server at `http://localhost:3100`
- **React UI** (dashboard + management interface)
- **CLI** (`paperclipai` command)
  - `npx paperclipai onboard --yes` for quick start
  - Manual: `git clone + pnpm install && pnpm dev` (Node 20+ / pnpm 9.15+)
- **packages/** — monorepo shared code (types, schemas, utilities)
- **Modular plugin system** for extensibility

### Tech stack inferred from package.json

- TypeScript 97.4%
- Node 20+
- pnpm 9.15+
- Vitest (unit tests)
- Playwright (E2E + multiuser-authenticated)
- Drizzle ORM (schema management)
- Embedded PGlite / external Postgres
- promptfoo (LLM eval framework — first in corpus)
- Tailscale (tailnet bind mode)

## 4. BYO Agent — multi-model adapter system

paperclip is explicitly **multi-model agnostic**:

**Supported agents/providers:**
- **OpenClaw** — Paperclip's apparent companion agent standard (3 runtime modes: join / docker-ui / sse-standalone)
- **Claude Code** (Anthropic)
- **Codex** (OpenAI)
- **Cursor**
- **Bash** (shell scripts as agents)
- **HTTP endpoints** (arbitrary services as agents)

**Implementation:** adapter-plugin.md describes refactor toward runtime-registered adapters (vs hardcoded). Server becomes "source of truth for is this adapter actually registered."

**Interpretation:** paperclip is deliberately model-agnostic infrastructure. Strategic non-lock-in. Contrasts with BMAD (Claude Code primary) or gws (Gemini first-class, Claude via generic skill).

## 5. Governance layer (critical to positioning)

Despite "zero-human" tagline, paperclip emphasizes human oversight via 4 governance primitives:

| Primitive | Behavior |
|-----------|----------|
| **Approval gates** | Agents must request approval at defined checkpoints |
| **Manual override** | Human can "pause or terminate any agent — at any time" |
| **Budget hard-stops** | "When they hit the limit, they stop" — cost enforcement |
| **Audit log** | "Immutable audit log" of all agent actions |

**Reconciling "zero-human companies" + governance:** paperclip's thesis is that humans can supervise at policy level (set mission, budgets, approval rules) while operations run autonomously. "Zero-human" = zero-human-in-operational-loop, not zero-human-in-governance.

**Nick Bostrom reference reframed:** paperclip-maximizer illustrates what happens WITHOUT governance. paperclip-the-product argues governance layer prevents maximizer failure mode.

## 6. 3 bind modes (deployment flexibility)

From README onboarding:

| Mode | Flag | Use case |
|------|------|----------|
| **Local loopback** | default | Single-user on single machine |
| **LAN** | `--bind lan` | Multi-device within local network |
| **Tailnet** | `--bind tailnet` | Remote access via Tailscale VPN |

**Implication:** paperclip supports hobbyist (loopback) through team (LAN) through distributed remote (tailnet) without requiring public-internet deployment. Security-conscious design.

## 7. Community + ecosystem

- **Discord:** discord.gg/m4HZY7xNG3
- **GitHub Discussions** — ideas + RFC
- **Plugin Registry:** awesome-paperclip repository (community plugins)
- **No Zalo / VN channel** — global community only

**No individual maintainers named** — attribution to "paperclipai" org and "Paperclip" copyright. Anonymity strategic or under-documented.

## 8. What paperclip is NOT (explicit disclaimers)

From README "What Paperclip is not":

- **Not a single-agent tool** — designed for coordinated teams
- **Not a chatbot** — orchestration infrastructure, not user-facing conversation
- **Not a replacement for humans in governance** — despite tagline, governance layer requires human policy setup

This explicit framing mitigates paperclip-maximizer concern: even the product positioning acknowledges the design requires human governance framework.

## 9. Alignment-theory framing — unique in corpus

**Name origin:** Nick Bostrom's 2003 paperclip maximizer thought experiment — an AI tasked with "maximize paperclip production" that converts all matter into paperclips because it wasn't given values beyond the literal goal. Illustrates **instrumental convergence** and **misaligned optimization** risks.

**paperclipai's use of the reference:**
- **Name** = the project — visible signal
- **ROADMAP "MAXIMIZER MODE"** = upcoming higher-autonomy feature — explicit double-down
- **Governance layer** = implicit response (the alignment-theory solution: control layer around maximizer)

**Two possible interpretations:**

1. **Ironic/self-aware** — team deliberately names the thing they're building, embracing alignment-theory awareness as brand
2. **Naive** — team uses clever name without engaging safety implications

README + ROADMAP content + 4 governance primitives suggest interpretation #1 (self-aware). But **no SAFETY.md with explicit alignment framework** is a gap.

**Corpus first:** no prior 13 wikis had explicit AI-safety-theory naming or MAXIMIZER MODE trajectory.

## 10. Version + timeline

- **6 releases** (low count for 2,264 commits = rolling-main model)
- **No version number in README** (README suggests pre-1.0)
- **Copyright 2026 Paperclip** — matches vault's 2026-04-19 date
- **"Paperclip is still moving quickly"** per ROADMAP — no locked timelines

Contrast with BMAD v11 (v6.3.0 versioned) + gws v13 (v0.22.5 pre-1.0 with 44 releases). paperclip skips formal version number — "released when ready" model.

## 11. Cross-references to T5 peers

| Axis | deer-flow (v9) | autoresearch (v10) | paperclip (v14) |
|------|----------------|---------------------|------------------|
| Stars | 62K | 74K | **55.9K** |
| Backing | ByteDance corporate | Karpathy solo | **Unclear ("paperclipai" org)** |
| Specialization | SuperAgent harness | ML research | **Agent orchestration "company-scale"** |
| Language | Python + Next.js | Python | **TypeScript** |
| Framing | Long-horizon tasks | ML experiments | **"Zero-human companies"** |
| Alignment framing | Implicit | Implicit | **Explicit (Bostrom reference)** |
| Feature breadth | Moderate | Narrow | **Highest in T5 (9 named features)** |
| Governance focus | Implicit | Implicit | **Explicit 4-primitive governance** |
| Multi-tenancy | No | No | **Yes (Multi-Company)** |
| LLM evals | — | val_bpb metric | **promptfoo framework** |

→ paperclip adds **third archetype** to T5: community-platform-generalist-with-governance. Distinct from deer-flow's autonomous-harness and autoresearch's specialist-loop.

## 12. Exact section headers

What is Paperclip? / Paperclip is right for you if / Features / Problems Paperclip solves / Why Paperclip is special / What Paperclip is not / Quickstart / FAQ / Development / Roadmap / Community & Plugins / Telemetry / Contributing / Community (repeated) / License / Star History

**Most elaborate README structure in T5** — enterprise-product-style information architecture.

## Open questions surfaced

- Funding source (Q1)
- Team size / anonymity (Q2)
- OpenClaw companion nature (Q4)
- Alignment-theory stance (Q6)
- "Zero-human" literal vs aspirational (Q7)
- MAXIMIZER MODE semantics (Q5)
- Multi-tenant isolation depth (Q13)
