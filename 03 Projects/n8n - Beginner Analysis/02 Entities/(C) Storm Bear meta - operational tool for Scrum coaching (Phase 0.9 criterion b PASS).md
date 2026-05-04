# (C) Storm Bear Meta — Operational Tool for Scrum Coaching

> **Phase 0.9 STRICT 4-criteria gate decision:** Criterion (b) PASS — n8n is a genuinely operational tool that Storm Bear can deploy for internal Scrum-coaching workflow automation under SUL internal-business-use clause.

> **First Storm Bear meta-entity under STRICT amendment session 66.** 39th consecutive Storm Bear meta-entity (38th GRANDFATHERED v55 + 39th first-strict v56). Streak preserved with legitimate criterion-pass evidence, NOT cautionary-contrast lightweight-INCLUDE.

---

## Phase 0.9 STRICT criteria scorecard

| Criterion | Verdict | Evidence | Notes |
|---|---|---|---|
| (a) Author archetype peer | ❌ FAIL | Jan Oberhauser = German solo-CEO of mature GmbH commercial entity (~7 years, 185K stars, ~?-employee company) | NOT structural peer to solo-VN Scrum coach + developer in early-fluency phase. German commercial maturity vs VN solo emerging-operator divergence is too wide. |
| (b) Operational tool for Scrum-coaching workflows | ✅ **PASS** | 400+ integrations including Jira/Linear/Slack/GitHub/Anthropic/OpenAI + 6 AI agent types + self-host with SUL internal-business-use permitted + Docker-simple-deploy + bidirectional MCP | Verified via docs.n8n.io/advanced-ai integration list + SUL internal-use clause |
| (c) Methodology-influence-node | ❌ FAIL | n8n is workflow-automation lineage (Zapier 2011 → Make/Integromat → n8n 2019); NOT in vault's methodology lineage (Karpathy LLM Wiki / John Lam / Lance Martin / Boris Cherny / SDD / TDD / agentic-engineering) | Workflow-automation pre-dates LLM era; n8n added AI overlay 2023+; no Karpathy-lineage influence |
| (d) In-corpus reference | ⚠️ TENTATIVE | TrendRadar v19 may mention n8n as multi-channel push target — needs corpus grep for "n8n" string in v19 entry; NOT verified at v56 ship | Q1 in OPEN-QUESTIONS — if PASSES, criterion (d) double-PASS strengthens evidence and Pattern #57 sub-variant 57c forward-citation extends to N=3 |

**Decision:** Criterion (b) STRONGLY PASSES → INCLUDE Storm Bear meta-entity legitimately under session-66 STRICT amendment.

**Distinct from v55 cautionary-contrast lightweight-INCLUDE:** v55 automate-faceless-content was 4/4 criteria FAIL but agent chose lightweight-INCLUDE via cautionary-contrast framing — this triggered session-66 amendment. v56 n8n is a CLEAN single-criterion-PASS legitimate INCLUDE — first under tightened criteria.

---

## Concrete Storm Bear operational use cases (criterion b evidence)

### Use case 1: Sprint metrics aggregation pipeline

**Goal:** Automatically aggregate sprint metrics from Jira/Linear into a daily dashboard delivered to Slack.

**n8n workflow:**
1. **Schedule trigger** — daily 06:00 ICT
2. **Jira node** — query active sprints + extract velocity / WIP / burndown
3. **Linear node** — query active cycles + extract issue states + cycle progress
4. **Code node (TypeScript)** — compute DORA metrics + sprint-velocity trend
5. **Slack node** — post markdown digest to #scrum-team channel

**Deployment:** Self-host n8n on personal VPS or local Docker; SUL internal-business-use permitted (this is Storm Bear's own internal automation, not client-facing service).

**Why valuable:** Replaces manual sprint-metrics-export + Excel-aggregation cycle. Compounds with ECC v1 wiki Storm Bear pilot #1 (Claude Code + ECC profile install).

### Use case 2: Retro Q&A automation

**Goal:** After each retrospective, auto-summarize the Slack discussion thread into a structured retro doc.

**n8n workflow:**
1. **Slack trigger** — message in #retro-team channel with `/retro-end` slash-command
2. **Slack node** — fetch thread messages from preceding 60 min
3. **AI Agent node (Conversational)** — Anthropic provider; prompt = "Summarize this retro into Liked / Learned / Lacked / Longed-For / Action-Items"
4. **Notion node** — create new page in Retros database
5. **Slack node** — reply with link to created Notion doc

**Deployment:** Self-host with Anthropic API key (operator-owned); SUL allows.

**Why valuable:** Removes scribe burden during retro; AI captures action items objectively; structured output flows to Notion knowledge base.

### Use case 3: Standup digest

**Goal:** Daily team standup summary across Slack/Discord/email channels.

**n8n workflow:**
1. **Schedule trigger** — daily 08:30 ICT
2. **Slack node** — fetch standup messages from #standup channel since yesterday 08:30
3. **AI Agent node (Tools Agent)** — Anthropic provider; tools = SlackUserLookup + JiraIssueDetail
4. **Code node** — format markdown with linked Jira/Linear references
5. **Email node + Slack DM node** — distribute to scrum master + product owner

**Deployment:** Self-host. SUL allows internal-business-use.

### Use case 4: GitHub PR triage with AI

**Goal:** When a PR opens, run AI triage and post structured review checklist.

**n8n workflow:**
1. **GitHub Webhook trigger** — `pull_request.opened`
2. **GitHub node** — fetch PR diff + linked issue
3. **AI Agent node (ReAct)** — Anthropic provider; prompt = "Review for: missing tests / breaking changes / security risks / linked issue alignment"
4. **GitHub node** — post review comment with structured checklist
5. **Linear node** — update linked issue status

**Deployment:** Self-host. SUL allows internal-business-use.

### Use case 5: Storm Bear-as-MCP-server experimentation

**Goal:** Expose Storm Bear vault knowledge as MCP server consumable by Claude Code or other MCP-aware agents.

**n8n workflow:**
1. **MCP Server Trigger** — listen on local port for MCP requests
2. **HTTP node** — search Storm Bear vault via grep/awk (or future Storm Bear API)
3. **AI Agent node** — synthesize answer with citations
4. **Return MCP response** — structured tool-use response

**Deployment:** Self-host. SUL allows internal-business-use.

**Why this is corpus-first interesting:** n8n's MCP Server Trigger node enables Storm Bear to be a CONSUMER of n8n workflows AND a PROVIDER (via the same n8n instance acting as MCP server). This bidirectional capability is unique at T2 and unlocks experimentation Storm Bear couldn't do with non-MCP-bidirectional workflow tools.

---

## Storm Bear pilot rank estimate

**MEDIUM-HIGH operational** — ranks #3-5 in Storm Bear pilot ladder (post-v54 pilot top-7 unchanged at v55; v56 inserts n8n as new entrant).

**Rationale for #3-5 rank:**
- Bidirectional MCP unlocks Storm Bear-as-MCP-server experimentation (HIGH novelty for vault)
- 5 concrete operational Scrum-coach use cases articulated (HIGHER specificity than most pilot candidates)
- 7-year-mature commercial GmbH = stable platform (LOWER risk than emerging-startup pilots)
- BUT SUL hosting-as-service restriction = cannot productize for client-facing managed service (DEPRESSES rank vs unrestricted-license alternatives)
- Self-host complexity = ~1-day setup vs claude-hud / claude-howto quick-wins (DEPRESSES rank)

**Likely placement:** Between claude-howto self-onboarding (#2 pilot) and claude-context (#5 pilot) — call it **rank #3 or #4** pending operator validation.

## Caveats for Storm Bear deployment

1. **SUL non-OSI status** — Storm Bear must NOT extract n8n components and embed in Storm Bear-published-skills (publishing under any OSI license would violate SUL implicit terms; verify with operator-counsel if planning public-release derivative work)
2. **Hosting-as-service restriction** — Storm Bear must NOT offer n8n-managed-service to coaching clients without n8n.cloud commercial subscription
3. **Bun runtime ecosystem signal** — n8n claims Bun-compatibility but verify before committing tooling decision
4. **Default branch `master`** — Storm Bear's GitHub workflows may need `master` adaptation if mirroring n8n
5. **Active fork community** — 30.8% fork ratio suggests many self-hosted variants; quality of community-maintained-forks is operator-due-diligence task

## Compounds + connections to existing Storm Bear vault

- **Pattern #18 bidirectional MCP** strengthens Storm Bear-as-MCP-server design exploration (cross-references claude-howto v23 + ollama v46 MCP integrations)
- **Pattern #28 16 native LLM providers** strengthens multi-runtime escape-hatch story (cross-references oh-my-openagent v52 multi-runtime + browser-use v41 LiteLLM)
- **Pattern #29 SUL N=3 sub-context** strengthens vault license-decision research (v27 HIGH bundle item #5 — cross-references omo v52 + GitNexus v33 license analysis)
- **400+ integrations breadth** is a reference benchmark for any future Storm Bear "skill" / "integration" library (cross-references awesome-claude-skills v50 864-skill catalog)

---

## Output assessment

This Storm Bear meta-entity is **NOT cautionary-contrast** (which would be: "n8n is what NOT to do — too restrictive, too commercial, too enterprise"). It IS legitimate criterion-(b)-PASS operational-tool-deployment evaluation with 5 concrete use cases + 4 deployment caveats + pilot-rank estimate.

This validates session-66 STRICT amendment: when criterion (b) genuinely passes, INCLUDE adds operator-actionable value. When 0/4 PASS (as v55 was), INCLUDE via cautionary-contrast becomes Goodhart's-law streak-preservation.

**v56 = first legitimately-strict-criteria-passed Storm Bear meta-entity. Streak metric meaningful again.**
