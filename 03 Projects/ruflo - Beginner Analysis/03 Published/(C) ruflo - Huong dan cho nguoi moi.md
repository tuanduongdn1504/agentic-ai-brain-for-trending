# (C) Ruflo — Hướng dẫn cho người mới / Beginner Guide (VN+EN)

> **Đối tượng / Audience:** Solo developers + small teams muốn tìm hiểu Ruflo, 42nd wiki của Storm Bear corpus.
> **Trạng thái / Status:** v3.5.80 (2026-04-11) stable. MIT. ~500+ primitives — **EXTREME scope** (largest in corpus).

---

## Phần 1 | Ruflo là gì / What is it?

**VN:** Ruflo (trước đây tên là Claude Flow) là một **nền tảng AI agent orchestration tự học** biến Claude Code (hoặc OpenAI Codex CLI) thành môi trường phát triển đa-agent với swarm coordination, vector memory, 313 MCP tools, và governance quy mô doanh nghiệp. Quan trọng: Ruflo **không tự thực thi code** — nó là **bộ điều phối (coordination ledger)** giúp các agent (Claude/Codex/khác) làm việc thực tế.

**EN:** Ruflo (formerly Claude Flow) is a **self-learning AI agent orchestration platform** that turns Claude Code (or OpenAI Codex CLI) into a multi-agent development environment with swarm coordination, vector memory, 313 MCP tools, and enterprise-grade governance. Crucially, Ruflo **does not execute code itself** — it is a **coordination ledger** that orchestrates agents (Claude/Codex/others) doing the actual work.

**Author:** Reuven Cohen (RuvNet) — senior cloud-computing industry operator, founder of Agentics Foundation, commercial entity Cognitum.One.

---

## Phần 2 | Signals độc đáo trong Storm Bear corpus / Corpus-first signals

1. **313 MCP tools** — nhiều nhất trong corpus, gấp ~20× số cao thứ hai (GitNexus v33 = 16 tools)
2. **100+ specialized agents** trong một project — cao nhất trong corpus
3. **9-component RuVector intelligence stack** (SONA / EWC++ / Flash Attention / HNSW / ReasoningBank / Hyperbolic / LoRA / Int8 Quant / SemanticRouter + 9 RL algorithms) — corpus-first stack hoàn chỉnh
4. **WASM kernels in Rust** cho policy engine + embeddings + proof system
5. **IPFS/Pinata decentralized plugin marketplace** — first corpus decentralized agent-plugin distribution
6. **Triple-package parallel distribution** (claude-flow + ruflo + @claude-flow/cli) — smooth rebrand
7. **70+ ADRs** với `hooks progress` validation gates — largest ADR surface in corpus
8. **5-way explicit competitor comparison** trong README (vs CrewAI / LangGraph / AutoGen / Manus)
9. **Dual-mode Claude + Codex first-class** via dedicated `@claude-flow/codex` sibling package
10. **"Extend Claude Code subscription by 250%"** + token optimizer 30-50% savings — first explicit dollar-value ROI claim
11. **EXTREME primitive-count tier** (~500+ primitives) — corpus-methodology-first precedent
12. **3-layer commercial structure** (Cognitum.One parent + Flow Nexus SaaS + Agentics Foundation community) — corpus-most-elaborate
13. **Largest README in corpus** — 280 KB / 7,541 lines
14. **Triple-identity author profile** (ruv.io personal + Cognitum.One commercial + Agentics Foundation community)

---

## Phần 3 | Định vị trong tiers / Tier placement

**Primary: T2 Agent-as-service.** Ruflo chạy như daemon + MCP server trên port 3000 với 6 provider adapters + cost-based routing + enterprise governance (70+ ADRs + 5 DDD bounded contexts).

**Secondary: T1 Agent-as-assistant.** Ruflo cũng extends Claude Code (bắt buộc cài trước) + tạo `.claude/` + CLAUDE.md + registers MCP.

**Kết luận:** Ruflo là **dual-classification** đầu tiên trong corpus. T2 extends N=2 → N=3 (joins goclaw v4 + multica v15).

---

## Phần 4 | Installation / Cài đặt

**VN:** Chọn 1 trong các cách sau:

**EN:** Choose one:

```bash
# Cách 1: One-line curl install (recommended)
curl -fsSL https://cdn.jsdelivr.net/gh/ruvnet/ruflo@main/scripts/install.sh | bash

# Cách 2: npx (quick start, không cần install global)
npx ruflo@latest init --wizard

# Cách 3: Global npm install
npm install -g ruflo@latest
ruflo init --wizard

# Cách 4: Bun (nhanh hơn)
bunx ruflo@latest init

# Cách 5: Docker
docker-compose up  # sử dụng ruflo/docker-compose.yml
```

**Yêu cầu / Prerequisites:**
- Node.js 20+ (bắt buộc)
- npm 9+ hoặc pnpm hoặc bun
- Claude Code installed first: `npm install -g @anthropic-ai/claude-code`

**Install profiles:**
- `--omit=optional` ~45 MB (core CLI only, nhanh nhất ~15s)
- Default ~340 MB (full với ML/embeddings)

**Register MCP for Claude Code:**
```bash
claude mcp add ruflo -- npx -y ruflo@latest mcp start
claude mcp list  # xác nhận đã add
```

---

## Phần 5 | Core usage patterns / Cách sử dụng cơ bản

### 5.1 Swarm cơ bản (4 agents cho bug fix)

```bash
# Initialize hierarchical swarm
npx ruflo swarm init --topology hierarchical --max-agents 4

# Spawn 4 specialized agents
npx ruflo agent spawn --type coordinator --name lead
npx ruflo agent spawn --type researcher --name debug
npx ruflo agent spawn --type coder --name fix
npx ruflo agent spawn --type tester --name verify

# Start swarm với objective
npx ruflo swarm start --objective "Fix login timeout bug" --strategy development
```

### 5.2 Memory store + search (self-learning)

```bash
# Lưu pattern thành công
npx ruflo memory store \
  --key "auth-pattern-jwt" \
  --value "JWT auth với bcrypt, Zod validation, refresh token rotation" \
  --namespace "patterns"

# Search pattern khi cần
npx ruflo memory search --query "authentication JWT" --namespace patterns
```

### 5.3 Hooks automation

```bash
# Pre-task context load
npx ruflo hooks pre-task --description "Implement OAuth flow"

# Post-task với learning
npx ruflo hooks post-task --task-id "task-123" --success true --train-neural true
```

### 5.4 Dual-mode Claude + Codex (template)

```bash
# Run feature-development pipeline: Architect (Claude) → Coder (Codex) → Tester (Claude) → Reviewer (Codex)
npx @claude-flow/codex dual run --template feature --task "Add user authentication"
```

---

## Phần 6 | Novel concepts / Các khái niệm quan trọng

### RuVector self-learning stack
- **SONA:** Self-Optimizing Pattern Learning (<0.05ms adaptation)
- **EWC++:** Elastic Weight Consolidation (chống catastrophic forgetting)
- **HNSW:** Sub-ms vector search
- **ReasoningBank:** RETRIEVE → JUDGE → DISTILL trajectory learning
- **LoRA:** Low-Rank Adaptation cho fine-tuning nhẹ
- **9 RL algorithms:** Q-Learning, SARSA, A2C, PPO, DQN, etc.

### 3-Tier Model Routing (ADR-026)
- **Tier 1 (<1ms, $0):** Agent Booster WASM cho simple transforms (var→const, add-types, etc.)
- **Tier 2 (500ms-2s, $0.0002-$0.003):** Haiku/Sonnet cho bugs, refactoring, features
- **Tier 3 (2-5s, $0.015):** Opus cho architecture, security, distributed systems

**Tuyên bố:** "Extend Claude Code subscription by 250%" + token optimizer 30-50% savings.

### Anti-Drift swarm config
Default cho coding tasks:
```javascript
swarm_init({
  topology: "hierarchical",  // coordinator enforces alignment
  maxAgents: 8,              // nhỏ = ít drift
  strategy: "specialized"    // clear roles
})
```

### Division of labor
```
claude-flow = LEDGER (tracks state, coordinates, stores memory)
Claude / Codex = EXECUTORS (write code, run commands, implement)
```

---

## Phần 7 | So sánh với corpus frameworks / vs other Storm Bear frameworks

| Feature | Ruflo v42 | OMC v27 | agency-agents v18 | multica v15 | spec-kit v17 |
|---------|-----------|---------|---------------------|-------------|---------------|
| Tier | T2 + T1 dual | T1 | T1 | T2 | T1 |
| Scale | 33K | 30K | 82.9K | 16.2K | 89.2K |
| Agents | 100+ | 19 | 144 persona | 8 teammate | 80+ community ext |
| MCP tools | **313** | via runtimes | 0 | explicit | 0 |
| Self-learning | ✅ SONA/EWC++ | ⛔ | ⛔ | limited | ⛔ |
| Commercial | ✅ Flow Nexus | ⛔ | ⛔ | ⛔ | GitHub-corp |
| License | MIT | MIT | MIT | MIT | MIT |
| i18n | EN-only | 7-lang | EN | EN+CN | EN |
| Governance | 6 files + 70+ ADRs | 7 files | 3 files | 3-4 files | 6 files |

**Ruflo's distinct positioning:** Chỉ framework duy nhất trong corpus với complete self-learning stack + 100+ MCP tools + explicit commercial tier + enterprise-ambition.

---

## Phần 8 | Ethical framing / Các lưu ý cần biết

**VN:** Ruflo là OSS MIT, author public (Reuven Cohen với LinkedIn profile + industry background), không có perverse-incentive cấu trúc. Tuy nhiên cần lưu ý:

- **Supply-chain awareness:** IPFS/Pinata plugin marketplace cho phép plugin decentralized — cài plugin từ marketplace cần vetting (Pattern #66 corpus observation-track)
- **Commercial tier pre-launch:** Flow Nexus chưa có pricing/SLA công khai. Nếu pilot cho production, cần contact Cognitum.One để verify status.
- **Bus factor 1:** RuvNet là solo-flagship. Nếu RuvNet stop, 33K-star codebase có thể thiếu maintenance. Risk thực tế nhưng không acute (55 alpha iterations đã prove consistency).
- **Complexity risk:** ~500+ primitives là learning-curve lớn. Nếu chỉ cần basic swarm, alternative nhỏ hơn (pi-mono v36 coding-agent) có thể phù hợp hơn.
- **Enterprise ambition:** Ruflo positions cho team+enterprise; solo operators có thể thấy overhead quá cao.

**EN:** Ruflo is clean MIT OSS with public author (Reuven Cohen, verifiable LinkedIn + industry history), no perverse-incentive structure. Caveats:

- **Supply-chain awareness:** IPFS/Pinata plugin marketplace enables decentralized plugins — vetting required before installing (Pattern #66)
- **Commercial tier pre-launch:** Flow Nexus has no public pricing/SLA. Production pilot should verify with Cognitum.One.
- **Bus factor 1:** RuvNet is solo-flagship. 55 alpha iterations suggest consistency but single-maintainer risk exists.
- **Complexity risk:** ~500+ primitives is a steep learning curve. Smaller alternatives (pi-mono v36) may suit basic needs.
- **Enterprise ambition:** Ruflo targets teams+enterprise; solo operators may find overhead disproportionate.

---

## Phần 9 | Storm Bear relevance / Liên quan đến Storm Bear

**Đánh giá / Assessment:** Pilot rank **#4 (MEDIUM-HIGH if team scales / MEDIUM for current 1-person state)**.

**Kịch bản pilot phù hợp / Good pilot scenarios:**
- ✅ Nếu Storm Bear mở rộng thành team 3+ Scrum coaches — swarm orchestration cho phân tích client
- ✅ Nếu Storm Bear cần multi-provider LLM (cost-optimized routing giữa Anthropic + OpenAI + Google)
- ✅ Nếu Storm Bear muốn persistent agent memory across sessions (ReasoningBank pattern)
- ✅ Nếu operator muốn học dual-mode Claude + Codex collaboration patterns

**Kịch bản không phù hợp / Poor pilot scenarios:**
- ❌ Solo Scrum coach hiện tại (overhead 2-4 tuần onboarding quá lớn)
- ❌ Nếu chỉ cần 1-2 specific agents (agency-agents v18 đơn giản hơn)
- ❌ Nếu cần VN-native experience (Ruflo EN-only)
- ❌ Nếu production-critical (Flow Nexus pre-launch → verify trước)

**Quyết định đề xuất:** **Defer Ruflo pilot đến khi có nhu cầu cụ thể về multi-agent coordination.** Observational value cao (pattern library insights), pilot value medium.

---

## Phần 10 | 2-4 week learning roadmap

### Tuần 1: Exploration (~8-10h)
- Day 1 (2h): Clone repo, đọc README (skim top 500 lines + details sections), run `npx ruflo init --wizard`
- Day 2 (2h): Register MCP, try basic swarm init + agent spawn
- Day 3 (2h): Run 1 swarm recipe (hello world / bug fix)
- Day 4 (2h): Explore AgentDB memory store/search
- Day 5 (2h): Read CLAUDE.md behavioral rules + understand coordination-ledger model

### Tuần 2: Intermediate (~8-10h)
- Day 1 (2h): Try 3-tier model routing, measure token savings
- Day 2 (2h): Explore RuVector components (SONA + HNSW)
- Day 3 (2h): Try dual-mode Claude + Codex collaboration template
- Day 4 (2h): Build custom skill in `.claude/skills/` or `.agents/skills/`
- Day 5 (2h): Read 5 key ADRs (001, 006, 026, 048, 049)

### Tuần 3: Advanced (optional, ~8-10h)
- Hive-mind with 3 queen types + 8 workers
- Byzantine consensus experiments
- Plugin marketplace browsing via IPFS
- Agent Booster WASM transforms
- Performance benchmarks

### Tuần 4: Decision (~4h)
- Compare to baseline (Claude Code alone) for your specific workflow
- Decide: pilot for real work, defer, or reject
- If pilot: define 2-week evaluation criteria with rollback plan

---

## Phần 11 | Tradeoffs / Limitations

### Strengths
- Complete self-learning stack (corpus-first)
- 313 MCP tools (maximum interop surface)
- Dual-mode Claude + Codex
- Enterprise governance (70+ ADRs)
- Open-core với Flow Nexus commercial path
- Triple-package backward-compat

### Weaknesses
- EXTREME complexity (~500 primitives) = steep learning curve
- Bus factor 1 (solo RuvNet)
- No VN/i18n
- Flow Nexus pre-launch status unclear
- MCP tool count hand-maintained (313/314/315 discrepancies)
- 70+ ADRs challenging to validate compliance
- Cognitum.One legal structure undisclosed
- No peer-reviewed benchmarks / no SWE-Bench score

### Gray zones
- Claims "89% accuracy routing" not independently verified
- "Extend Claude Code by 250%" = marketing claim, depends on workload
- RuVector sub-ms claims benchmarked in specific configs only

---

## Phần 12 | Caveats + safety notes

- **Supply-chain:** Plugin marketplace is IPFS-based; any plugin source should be vetted before install (Pattern #66 awareness)
- **Secrets hygiene:** Ruflo explicitly requires `NEVER commit secrets, credentials, or .env files` (CLAUDE.md rule)
- **API costs:** With 6-provider failover, monitor costs closely (can surprise at scale)
- **Daemon persistence:** Daemon stays running; `npx ruflo daemon stop` to kill explicitly
- **Memory DB growth:** AgentDB grows over time; monitor disk usage
- **Security contact:** Use security@cognitum.one for vulnerabilities, NOT GitHub issues

---

## Phần 13 | References + next action

**Primary sources:**
- Repo: https://github.com/ruvnet/ruflo
- npm: `npm info ruflo` + `npm info claude-flow`
- Docs: README (in-repo) + `docs/adr/` + `ruflo/docs/`
- Homepage: Cognitum.One (gated) + ruv.io
- Community: Agentics Foundation Discord (discord.com/invite/dfxmpwkG2D)

**Related Storm Bear wikis:**
- **v27 OMC** — closest T1 peer (multi-runtime orchestration)
- **v18 agency-agents** — solo-at-enterprise precedent
- **v15 multica** — T2 peer (managed-agents-platform)
- **v33 GitNexus** — MCP-heavy (16 tools) precedent
- **v41 browser-use** — RED primitive-count precedent

**Next action:**
- **Nếu Storm Bear là 1-person:** DEFER pilot. Observational value only. Watch for Cognitum.One + Flow Nexus commercial launch.
- **Nếu Storm Bear scales to 3+ coaches:** Start Week 1 exploration. Allocate 8-10h.
- **Nếu cần specific utility (e.g., swarm prototyping):** Use ruflo CLI + memory layer standalone; skip full enterprise surface.
- **For Pattern Library observation:** Already captured. Strengthening Pattern #17 v1 + Pattern #18 MCP scale-tier + Pattern #58 un-stale + Pattern #12 refinement at next mini-audit.

---

**Ruflo is remarkable as a coordination-ledger framework with corpus-most primitives. Its EXTREME scope is both its strength (complete self-learning stack) and risk (2-4 week onboarding). For Storm Bear, defer pilot until multi-agent coordination becomes concrete need.**
