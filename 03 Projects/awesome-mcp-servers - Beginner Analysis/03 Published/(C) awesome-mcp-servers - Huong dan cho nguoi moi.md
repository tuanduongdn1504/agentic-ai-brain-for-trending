# (C) awesome-mcp-servers — Hướng dẫn cho người mới / Beginner Guide

> **Repo:** [`punkpeye/awesome-mcp-servers`](https://github.com/punkpeye/awesome-mcp-servers) · **85,323 stars · MIT · created 2024-11-30 · maintained by Frank Fiegel (Glama founder)**
> **Bilingual VN/EN.** Part of Storm Bear LLM Wiki v31. Written by Claude (C). 2026-04-22.
> **Scope frame:** OUTSIDE-SCOPE — MCP-server-aggregator sub-type. Sử dụng như **discovery directory**, không phải evaluation gate.

---

## 1. `awesome-mcp-servers` là gì? / What is this?

**VN:** `awesome-mcp-servers` là một danh mục cộng đồng được curate kỹ (**~1,200 MCP servers** trải rộng **50+ categories**) cho Model Context Protocol — protocol do Anthropic công bố tháng 11/2024, định nghĩa cách AI agent kết nối với resources (database, API, file system, web service, v.v.).

Repo ra đời **đúng ngày 30/11/2024** (đồng thời với MCP spec launch), tác giả Frank Fiegel (punkpeye, Miami FL) — người đồng sáng lập công ty Glama (glama.ai). Mô hình kinh doanh: OSS aggregator ở phía trên, commercial platform Glama Chat + glama.ai/mcp/servers ở phía dưới (Pattern #50 Commercial-Funnel Companion — reaches N=2 ở v31 cùng với VoltAgent + getdesign.md v25).

**EN:** `awesome-mcp-servers` is a community-curated directory of **~1,200 MCP servers** across **50+ categories** for the Model Context Protocol (Anthropic-published Nov 2024). The repo launched the same day as the MCP spec and is maintained by Frank Fiegel (Glama founder, Miami FL). Business model: OSS aggregator as top-of-funnel, Glama commercial stack downstream. This is **the de facto discovery directory** for the MCP ecosystem.

### Vì sao bạn nên quan tâm / Why it matters

- **MCP đã trở thành de facto standard** — Storm Bear corpus có ≥6 wikis consuming MCP (goclaw v4 / multica v15 / graphify v16 / spec-kit v17 / TrendRadar v19 / OpenHands v30). awesome-mcp-servers v31 = meta-directory cho toàn corpus MCP consumption.
- **One-stop discovery** — thay vì search GitHub mỗi khi cần một MCP server mới, mở directory này.
- **Quality signal (baseline)** — được curated bởi một người có commercial incentive align với ecosystem growth.
- **Largest curated agent-ecosystem directory** — 1,200 servers × 50+ categories × 4-axis 15-badge legend = broadest structured vocabulary trong corpus.

---

## 2. MCP là gì, khác gì plugin truyền thống? / What is MCP vs traditional plugins?

**VN:** MCP (Model Context Protocol) là một **protocol mở** do Anthropic công bố, cho phép AI agent (Claude Desktop, Claude Code, Cursor, Cline, Continue, Zed, và các client khác) kết nối đến một MCP **server** — chương trình chạy local hoặc cloud, expose tools + resources theo schema thống nhất.

So với plugin truyền thống:
- Plugin cũ = bound với một IDE hoặc một client cụ thể
- MCP server = client-agnostic, bất cứ MCP-capable client nào cũng dùng được
- MCP server nói chuyện qua stdio hoặc HTTP/SSE — dễ deploy, debug, và sandbox

**EN:** MCP is an open protocol for AI agents to connect to resources via a standardized schema. Unlike IDE-specific plugins, MCP servers are **client-agnostic** — any MCP-capable client (Claude Desktop, Claude Code, Cursor, Cline, Continue, Zed, etc.) can connect. Transport via stdio or HTTP/SSE.

### Stack 3 layers đang consolidate / Emerging 3-layer stack

Pattern #18 Agent Runtime Standardization post-v31 view:

| Layer | Standard | Scale signal |
|-------|----------|--------------|
| **Transport/resource protocol** | **MCP** | 85K stars directory + 1,200 servers + ≥6 corpus wikis consume |
| **Agent-runtime (community)** | OpenClaw | 5 corpus wikis integrate |
| **Agent-framing/protocol sibling** | Hermes | 3 corpus wikis integrate |

Ba layer complementary, không cạnh tranh. MCP = resource access; OpenClaw + Hermes = agent-running conventions.

---

## 3. Cách browse directory hiệu quả / How to browse efficiently

### 3.1 Hiểu legend vocabulary / Understand the legend

4 axes, 15 badges total:

**Axis 1 — Official status (1 badge):** 🎖️ = official implementation

**Axis 2 — Ngôn ngữ lập trình (8 badges):** 🐍 Python · 📇 TypeScript/JavaScript · 🏎️ Go · 🦀 Rust · #️⃣ C# · ☕ Java · 🌊 C/C++ · 💎 Ruby

**Axis 3 — Scope/hosting (3 badges):** ☁️ Cloud Service · 🏠 Local Service · 📟 Embedded Systems

**Axis 4 — Operating system (3 badges):** 🍎 macOS · 🪟 Windows · 🐧 Linux

Ví dụ: một server Python chạy local cho macOS carry `🐍 🏠 🍎`.

### 3.2 Start with categories gần workflow của bạn / Start with categories close to your workflow

Nếu bạn là Scrum coach / dev-team lead (Storm Bear operator target):
1. **Product Management** — Jira / Linear MCP servers → sprint status, backlog queries
2. **Version Control** — GitHub MCP server → DORA metrics, PR context
3. **Communication** — Slack / Discord / Teams MCPs → team sync automation
4. **Workplace & Productivity** — Google Workspace MCPs (overlaps gws v13)
5. **Knowledge & Memory** — vector store + knowledge-graph MCPs cho vault-query

Nếu bạn là ML engineer: Biology/Medicine, Data Science, Research categories.

Nếu bạn là web/dev generalist: Browser Automation, Code Execution, Developer Tools, Databases.

### 3.3 Đọc entry format / Read entry format

Mỗi entry có format:
```
- [{owner/repo}]({url}) {optional badges} - {one-line description}
```
Không có star count, last-updated, security-audit, hay Anthropic-official flag. Directory is **discovery layer, not quality gate**.

---

## 4. Top MCP server categories cho Storm Bear Scrum coach workflow

### 4.1 Product Management (PRIORITY HIGH)

**Sử dụng case:**
- Lấy sprint burndown data vào planning meeting
- Query "tickets bị blocked trên 3 ngày" trong retro
- Cross-reference Jira issues với Git commits

**What to look for when browsing:**
- `jira` keyword → Atlassian Jira MCP servers
- `linear` keyword → Linear MCP servers (Linear-analog pattern corpus-relevant, multica v15)
- `azure-boards` / `github-projects` / `notion` for broader PM tools

**Evaluation:** 🎖️ (official from vendor) thường đáng tin hơn community. Đọc README + CHANGELOG + stars trên GitHub để sanity-check trước khi install.

### 4.2 Version Control (PRIORITY HIGH)

**Sử dụng case:**
- DORA metrics (deployment frequency, lead time, MTTR, change failure rate)
- PR review assistance khi coaching junior dev
- Git history analysis cho technical debt conversations

**What to look for:**
- Official GitHub MCP server (keyword: `github-mcp-server`, Anthropic-published hoặc GitHub-published)
- `gitlab-mcp` cho GitLab enterprise

**Caveat:** GitHub tokens cần least-privilege scope. Đừng wire một MCP server với admin-org scope cho casual experimentation.

### 4.3 Communication (PRIORITY MEDIUM)

**Sử dụng case:**
- Auto-posting standup summaries to Slack channel
- Mining Slack history cho retro evidence
- Team pulse survey automation

**What to look for:**
- `slack-mcp` / `discord-mcp` / `teams-mcp`
- Consider OAuth app permissions — MCP server thường cần token hoặc bot user

### 4.4 Workplace & Productivity / Google Workspace

Overlap với gws v13 (Google Workspace CLI corpus entry). Có thể dùng gws + MCP server GWS cùng lúc — gws cho CLI scripted workflows, MCP server cho inside-agent interactive.

### 4.5 Knowledge & Memory (PRIORITY HIGH — vault-query relevant)

Vector-store + knowledge-graph MCPs cho Storm Bear vault search:
- `chroma-mcp`, `qdrant-mcp`, `weaviate-mcp` (vector DBs)
- `neo4j-mcp` (graph DB)
- **Cross-ref:** graphify v16 ship MCP server as first-class output — bạn có thể dùng graphify MCP server để query Storm Bear vault as knowledge graph.

---

## 5. Cách evaluate MCP server quality TRƯỚC KHI install / How to evaluate before install

Directory là discovery, không phải trust gate. Pattern #66 Supply-Chain Security Incident Response (observation-track sau v29 crawl4ai + genre-wide awareness ở v31) → **treat mỗi MCP server như một untrusted dependency**.

### 5-point sanity check

1. **Star count + age** — khuyến nghị tối thiểu 500+ stars HOẶC 6+ tháng active. Reject nếu < 50 stars + < 1 tháng age.
2. **Last pushed date** — nếu > 6 tháng không commit, assume stale (MCP spec đã evolve).
3. **README transparency** — liệt kê rõ tools exposed + permissions required. Mơ hồ = skip.
4. **License** — ưu tiên MIT / Apache-2.0 / BSD. Custom non-OSI hoặc missing license = skip cho production.
5. **Maintainer identity** — real name hoặc known-pseudonym preferable. 🎖️ official từ vendor đáng tin nhất.

### Red flags / Cờ đỏ

- ❌ MCP server yêu cầu root permissions hoặc unrestricted filesystem access
- ❌ Hard-coded secrets hoặc plaintext credential handling
- ❌ No sandboxing hướng dẫn + no Docker image
- ❌ Fetches code từ random URL at runtime
- ❌ Publishes to PyPI/npm với user name khác với GitHub repo owner
- ❌ README có promo links / affiliate links / crypto-solicitation

### Pattern #66 reminder

Corpus đã có 1 documented supply-chain incident (crawl4ai v29 via `unclecode-litellm` fork response after LiteLLM tampering). **1,200 community-contributed MCP servers = 1,200 trust boundaries.** Directory NOT audit. You are audit.

---

## 6. Install + test workflow / Install + test workflow

### 6.1 Sandboxed-first principle

Luôn test MCP server trong sandboxed environment trước khi wire vào Claude Code production config:

```bash
# Docker-based isolation
docker run --rm -it --network=none -v $(pwd)/sandbox:/sandbox python:3.11-slim \
  bash -c "pip install some-mcp-server && some-mcp-server --help"
```

### 6.2 Check Claude Desktop / Claude Code config

MCP servers thường config trong `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) hoặc project-level `.mcp.json`. Format:

```json
{
  "mcpServers": {
    "example": {
      "command": "npx",
      "args": ["-y", "some-mcp-server"],
      "env": {"API_KEY": "..."}
    }
  }
}
```

Principle: **least-privilege env vars**, không paste master token.

### 6.3 Companion reference: `modelcontextprotocol.io`

Directory này cross-reference với [modelcontextprotocol.io](https://modelcontextprotocol.io) (Anthropic official registry). Khi có conflict, tin spec official hơn community directory.

---

## 7. 2-week exploration roadmap / 2-week exploration roadmap

### Week 1 — Discovery + first install

**Day 1-2:** Browse directory end-to-end. List 5 MCP servers match workflow của bạn (ví dụ: jira-mcp + github-mcp + slack-mcp + gdrive-mcp + qdrant-mcp).

**Day 3-4:** Đọc README + 5-point sanity check cho từng server. Rút xuống 2-3 servers để thử.

**Day 5-7:** Install 1 server trong Docker sandbox. Test 3 tool calls via CLI hoặc Claude Desktop. Note latency + error rates.

### Week 2 — Production wiring + Scrum use case

**Day 8-10:** Wire 1 server vào Claude Code project-level `.mcp.json`. Run một Scrum workflow end-to-end (e.g., "lấy sprint status từ Jira → draft standup notes → post Slack").

**Day 11-12:** Đánh giá: có lặp lại hàng tuần không? Có save thời gian không? Nếu không → gỡ, thử server khác.

**Day 13-14:** Document kinh nghiệm vào Storm Bear vault. Consider contributing back nếu phát hiện gaps.

---

## 8. Ecosystem companion repos / Companion repos

Fiegel maintain 7 repos related-to-MCP:

| Repo | Stars | Role |
|------|-------|------|
| awesome-mcp-servers | 85,323 | Primary server directory (this wiki) |
| awesome-mcp-clients | 6,394 | Client directory (sister) |
| fastmcp | 3,054 | TypeScript framework for building MCP servers |
| pipenet | 484 | Localhost tunnel |
| awesome-mcp-devtools | 445 | Dev-tool directory |
| mcp-proxy | 251 | stdio↔HTTP/SSE transport proxy |
| mcp-ping | 7 | Host ping utility |

Nếu bạn muốn **build** MCP server: check `fastmcp` TypeScript framework (maintainer bias: Fiegel published directory + framework — xem như ecosystem-strengthening, nhưng caveat rằng có conflict-of-interest tension).

Commercial companion: **Glama Chat** (glama.ai/chat) — multi-modal AI client với MCP support. **Glama MCP Servers** (glama.ai/mcp/servers) — web UI sync với repo. **State-of-MCP-2025** report (glama.ai/blog) — ecosystem-historian artifact.

---

## 9. Storm Bear vault use cases / Storm Bear vault use cases

**VN:** Nếu bạn đang maintain Storm Bear (hoặc vault Obsidian tương tự):

1. **Vault-query via MCP** — wire qdrant-mcp hoặc chroma-mcp vào Claude Code, index markdown files, query natural-language. Alternative: graphify v16 ship MCP server out-of-the-box.
2. **GitHub MCP cho Storm Bear repo operations** — Claude agent có thể read issues, draft PR descriptions, run checks.
3. **Google Workspace MCP** — cross-post Scrum ceremony notes từ vault → Google Docs → share client.
4. **Slack MCP cho team update automation** — auto-post weekly retrospective summary.

**Potential contribution:**
- Vietnamese README translation (README-vi.md) — directory có 7 languages, không có VN. Low-effort high-signal PR.
- Publish VN Scrum MCP server nếu bạn build: `vn-scrum-coach-mcp` (hypothetical) với facilitation prompts.

**EN:** Storm Bear / vault operators: wire vector-store MCP for vault-query, GitHub MCP for repo ops, Google Workspace MCP for client distribution, Slack MCP for team automation. Contribution opportunity: `README-vi.md` translation.

---

## 10. Caveats + honest framing / Caveats + honest framing

### What the directory DOES well

- ✅ Most comprehensive MCP server discovery surface in ecosystem
- ✅ Transparent legend vocabulary (4-axis 15-badge)
- ✅ 7-language i18n (ties fish-speech v20 + oh-my-claudecode v27 + LlamaFactory v22 top-tier)
- ✅ Active maintenance (pushed 2026-04-15, ~1 week before this wiki)
- ✅ Paired client directory `awesome-mcp-clients` — both sides of connection

### What the directory does NOT do

- ❌ Curate quality per-entry — listing ≠ endorsement
- ❌ Security audit — 1,200 servers review-debt very high
- ❌ Pin MCP spec compatibility version per server
- ❌ Include star count / last-updated per entry
- ❌ Distinguish Anthropic-official vs community-official (only binary 🎖️)

### Fiegel incentive awareness

Fiegel = curator + Glama founder. Directory proximity có thể ngầm favor Glama-adjacent listings. Không có evidence bias but operators should cross-reference:
- `modelcontextprotocol.io` (Anthropic official)
- GitHub search `topic:mcp`
- Community discussions (r/mcp subreddit, Discord)

### Sustainability risk

- **Solo maintainer bus factor = 1.** If Fiegel departs or Glama pivots, directory may stall. Fork path cheap.
- **Review debt compounds with scale.** 1,200 entries at 5K stars/month growth → difficult review capacity.
- **MCP spec evolves.** Some listed servers may be stale vs current spec.

### Recommendation

Use directory as **starting point**, not authoritative source. Browse via category → 5-point sanity check → sandbox test → production wire. Treat each install as supply-chain event per Pattern #66.

---

## 11. Nếu bạn muốn contribute / If you want to contribute

Fiegel expose `🤖🤖🤖` **agent-PR fast-track protocol** trong CONTRIBUTING.md — corpus-first explicit governance cho automated-agent-authored PRs. Nếu PR của bạn do Claude Code / Codex / Cursor agent tạo, suffix title với `🤖🤖🤖` để fast-track review.

Low-cost contribution ideas:
1. **README-vi.md** translation (no VN currently)
2. **Missing-server PRs** trong Product Management / Communication categories
3. **Typo / broken-link fixes** — calibrate review latency trước khi commit bigger work
4. **Badge corrections** nếu thấy server mis-classified

Workflow: fork → edit README.md → respect alphabetical ordering → PR với clear description + `🤖🤖🤖` suffix nếu agent-authored.

---

## 12. Cross-references to Storm Bear corpus

### Aggregator peers (awesome-list-genre meta-pattern candidates)

- [[03 Projects/build-your-own-x - Beginner Analysis/|build-your-own-x v8]] — 10-year education-aggregator, 491K stars, human-directed
- [[03 Projects/awesome-design-md - Beginner Analysis/|awesome-design-md v25]] — 20-day extreme-viral design-template aggregator cho AI agents, 60K stars

### MCP-consumer peers (wikis đã tích hợp MCP hoặc MCP-adjacent)

- [[03 Projects/goclaw - Beginner Analysis/|goclaw v4]] — Multi-tenant platform, MCP-capable
- [[03 Projects/multica - Beginner Analysis/|multica v15]] — Anthropic skills registry import
- [[03 Projects/graphify - Beginner Analysis/|graphify v16]] — **MCP server as first-class output**
- [[03 Projects/spec-kit - Beginner Analysis/|spec-kit v17]] — MCP ecosystem reference
- [[03 Projects/TrendRadar - Beginner Analysis/|TrendRadar v19]] — 21+ MCP tools + 4 MCP Resources
- [[03 Projects/OpenHands - Beginner Analysis/|OpenHands v30]] — MCP-capable agent loop

### Pattern peers

- Pattern #17 Ecosystem-Layer Orgs: safishamsi v16 / VoltAgent v25 / Yeachan v27
- Pattern #50 Commercial-Funnel Companion: VoltAgent + getdesign.md v25 (N=2 with this wiki)
- Pattern #66 Supply-Chain Incident observation-track: crawl4ai v29

### i18n peers (7-language tier)

- fish-speech v20 / oh-my-claudecode v27 / LlamaFactory v22

---

## 13. One-line takeaway

**VN:** awesome-mcp-servers là nơi bắt đầu discovery MCP server, không phải nơi kết thúc evaluation. Dùng directory → 5-point sanity check → sandbox test → production wire, mỗi install như supply-chain event.

**EN:** awesome-mcp-servers is where you START MCP discovery, not where you finish evaluation. Directory → 5-point sanity check → sandbox test → production wire, treating each install as a supply-chain event.

---

_Published guide. Storm Bear LLM Wiki v31. Written by Claude (C). 2026-04-22. ~440 lines, 13 parts, bilingual VN/EN._
