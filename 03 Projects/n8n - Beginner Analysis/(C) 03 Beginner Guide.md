# Beginner Guide — n8n (bilingual VN+EN)

> ⚠️ **License caveat (must-read first):** n8n uses **Sustainable Use License (n8n SUL)** — source-available non-OSI. Commercial use is **conditional**: internal-business-use ALLOWED, hosting-as-service-to-third-parties RESTRICTED. **Storm Bear deployment OK for personal/internal automation; NOT OK for client-facing managed service without n8n.cloud subscription.**

> ⚠️ **Cảnh báo license:** n8n dùng SUL — không phải OSI license. Dùng nội bộ OK, không được host làm dịch vụ cho khách hàng nếu không subscribe n8n.cloud.

---

## Part 1 — What is n8n? / n8n là gì?

**EN:** n8n is a fair-code workflow automation platform. Think Zapier or Make/Integromat — but self-hostable, with native AI agent capabilities, 400+ integrations, and a visual canvas where you drag-and-drop nodes to build automations. It's TypeScript-based, runs on Node.js (or Bun), and scales from "single-user laptop Docker container" to "n8n.cloud managed multi-tenant SaaS".

**VN:** n8n là platform tự động hoá workflow theo mô hình "fair-code". Giống Zapier hay Make/Integromat — nhưng self-host được, có sẵn 6 loại AI agent + 16 LLM provider native, 400+ integration với services bên ngoài, dùng visual canvas kéo-thả để build automation. Code TypeScript, chạy trên Node.js (hoặc Bun), từ "Docker container trên laptop" đến "n8n.cloud managed SaaS multi-tenant" đều được.

## Part 2 — Who built it? / Ai làm?

**EN:** n8n GmbH (Berlin, Germany) — a German limited liability company founded around 2019 alongside the project itself. Solo-founder-CEO **Jan Oberhauser** (managing director per company imprint). 7-year operational history makes n8n one of the most mature commercial workflow-automation platforms in the AI-agent corpus.

**VN:** n8n GmbH (công ty TNHH Đức, trụ sở Berlin) — thành lập khoảng 2019 cùng project. Founder + CEO duy nhất là **Jan Oberhauser**. 7 năm hoạt động — đây là một trong những platform workflow-automation trưởng thành nhất trong corpus Storm Bear.

## Part 3 — Scope + applicability for Storm Bear

**Tier:** T2 Agent-as-service (workflow automation platform with persistent multi-tenant deployment + AI agent embedded). 4th T2 entrant in corpus (joins goclaw v4 + multica v15 + ruflo v42).

**Phase 0.9 STRICT criterion (b) PASS:** n8n IS an operational tool Storm Bear can deploy for Scrum-coach automation. See `02 Entities/(C) Storm Bear meta - operational tool for Scrum coaching (Phase 0.9 criterion b PASS).md` for 5 concrete use cases.

**VN gọn:** n8n hợp với Storm Bear ở mức HIGH-MEDIUM cho personal Scrum automation. Tự host được, license cho phép dùng nội bộ. KHÔNG dùng được cho dịch vụ thu phí khách hàng nếu không subscribe n8n.cloud.

## Part 4 — Install (3 paths)

### Path A: Quick Docker (recommended for first-time)

```bash
docker volume create n8n_data
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n
```

Visit `http://localhost:5678`. Sign up local-account (no telemetry phone-home for local Docker).

### Path B: npm CLI (for Node.js users)

```bash
npm install n8n -g
n8n start
```

Visit `http://localhost:5678`.

### Path C: n8n.cloud managed (commercial — Storm Bear deferred)

Sign up at https://n8n.io/cloud — free tier exists; Pro/Business tiers paid. **Storm Bear: only consider if needing client-facing managed service** (SUL restricts self-host hosting-as-service).

## Part 5 — 4-week roadmap for Storm Bear

| Week | Goal |
|---|---|
| **Week 1** | Install via Path A Docker; create first workflow (e.g., "fetch GitHub PR list daily, post to Slack") |
| **Week 2** | Wire AI Agent node with Anthropic provider; build "retro summarizer" workflow consuming Slack thread |
| **Week 3** | Connect Jira/Linear; build "sprint metrics digest" workflow |
| **Week 4** | Experiment with MCP Server Trigger node — expose 1 Storm Bear vault search workflow as MCP server consumable by Claude Code |

## Part 6 — 5 concrete Storm Bear use cases (summary)

1. **Sprint metrics aggregation** — Jira/Linear → DORA dashboard daily Slack digest
2. **Retro Q&A automation** — Slack thread → AI summary → Notion retro doc
3. **Standup digest** — multi-channel standup messages → AI summary → email + Slack DM
4. **GitHub PR triage with AI** — PR webhook → AI-driven review checklist → Linear update
5. **Storm Bear-as-MCP-server experimentation** — n8n MCP Server Trigger exposes vault search to Claude Code

Full details in `02 Entities/(C) Storm Bear meta...md`.

## Part 7 — License caveats (re-emphasis)

**SUL allows:**
- Self-host for internal/personal use
- Process internal team data
- Build custom integrations for own use
- Modify source for own use

**SUL restricts:**
- Hosting n8n as a managed service for third-party clients (without n8n.cloud commercial subscription)
- Reselling n8n functionality
- Embedding n8n as backend for client-facing SaaS without commercial license

**Pattern Library context:** n8n SUL joins **omo v52 SUL-1.0** + **GitNexus v33 PolyForm-Noncommercial** = corpus N=3 in custom-non-OSI-commercial-restriction sub-context. This is a coherent license-family Storm Bear should understand before public-release decision (v27 HIGH bundle item #5).

## Part 8 — Common pitfalls

1. **Don't deploy n8n as client-facing managed service without commercial license** — SUL violation
2. **Default branch is `master` (not `main`)** — adapt CI/CD scripts accordingly
3. **High open-issues count (1,580)** — large mature project, expect community-contribution churn; pin specific version in production
4. **400+ integrations sounds great but quality varies** — community-contributed nodes may have lower polish than core nodes
5. **AI agent nodes evolve fast** — 6 agent types now; expect changes; pin AI workflow versions
6. **Bun runtime claim is ecosystem signal** — verify before committing tooling decision

## Part 9 — Community + resources

- **GitHub:** https://github.com/n8n-io/n8n (185K stars, active)
- **Docs:** https://docs.n8n.io
- **Community forum:** https://community.n8n.io
- **n8n.cloud commercial:** https://n8n.io/cloud
- **License:** https://docs.n8n.io/sustainable-use-license/
- **Imprint:** https://n8n.io/imprint/

## Part 10 — Storm Bear corpus connections

- **Pattern #18 bidirectional MCP** — n8n is corpus-first explicit MCP-Server-Trigger node naming + strongest T2 evidence
- **Pattern #29 license sub-context N=3** — n8n SUL joins omo v52 + GitNexus v33
- **Pattern #50 commercial-funnel** — n8n.cloud companion platform 50a Standard
- **Pattern #28 multi-provider** — 16 native LLM providers (no LiteLLM)
- **Pattern #2 distribution evolution** — 5+ surfaces (npm + Docker + cloud + self-host + Docker Desktop)
- **T2 N=4 extension** — joins goclaw v4 + multica v15 + ruflo v42

## Part 11 — When NOT to use n8n

- If you need OSI-compliant license for downstream re-licensing → use Apache/MIT alternatives
- If client-facing-managed-service is the goal → either subscribe n8n.cloud OR pick OSI alternative
- If sub-100ms latency required → workflow-orchestration overhead may be too slow
- If you need a code-first workflow tool (vs visual canvas) → consider Temporal, Airflow, Prefect

## Part 12 — Next steps for new Storm Bear users

1. Install via Path A Docker (`docker run`)
2. Build first workflow following 4-week roadmap Week 1
3. Read `02 Entities/(C) Storm Bear meta...md` for 5 use cases
4. Read `04 Phase 4b T2 4-way comparison.md` for n8n-vs-other-T2 corpus context
5. If considering public-release derivative: re-read SUL fully + consult operator-counsel

## Part 13 — Quick reference (cheat sheet)

| Q | A |
|---|---|
| What tier? | T2 Agent-as-service (4th T2 entrant) |
| Stars? | 185,728 (3rd-largest in corpus) |
| Age? | 7 years (2nd-oldest in corpus) |
| License? | n8n SUL (source-available, non-OSI, internal-OK, hosting-restricted) |
| Primary lang? | TypeScript |
| AI agents? | 6 types (Conversational / OpenAI Functions / Plan-and-Execute / ReAct / SQL / Tools) |
| LLM providers? | 16 native (no LiteLLM) |
| Vector stores? | 11 (corpus-broadest) |
| MCP support? | **Bidirectional** (Client + Server Trigger nodes — corpus-first at T2) |
| Storm Bear pilot rank? | #3-4 estimate (operator validation pending) |
| Phase 0.9 STRICT? | Criterion (b) PASS → INCLUDE legitimately |
