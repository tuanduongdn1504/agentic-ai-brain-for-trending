# (C) GitNexus — Hướng dẫn cho người mới / Beginner's Guide

> **Bilingual VN+EN** | **Wiki 33 của Storm Bear corpus** | **Date: 2026-04-23**
> **Source:** github.com/abhigyanpatwari/GitNexus (28,467 stars)
> **Author:** Abhigyan Patwari (Guwahati, Assam, India)
> **License: PolyForm Noncommercial 1.0.0** — ⚠️ đọc mục #8 trước khi dùng cho công việc thương mại

---

## ⚠️ Đọc mục này đầu tiên / Read this first

**VN:** GitNexus dùng license **PolyForm Noncommercial 1.0.0** — MIỄN PHÍ cho mục đích phi thương mại (cá nhân / học tập / nghiên cứu / phi lợi nhuận / chính phủ) nhưng **BẮT BUỘC phải có giấy phép riêng nếu dùng cho mục đích thương mại**. Nếu bạn là Scrum coach đang tính dùng GitNexus cho khách hàng trả tiền, hãy đọc Phần 8 và email `founders@akonlabs.com` để xác nhận trước khi dùng.

**EN:** GitNexus uses **PolyForm Noncommercial 1.0.0** license — FREE for noncommercial purposes (personal / educational / research / nonprofit / government) but REQUIRES a separate commercial license for commercial use. If you're a Scrum coach considering GitNexus for paid client work, read Section 8 and email `founders@akonlabs.com` to clarify before using.

---

## Phần 1 — GitNexus là gì? / What is GitNexus?

### VN

GitNexus là công cụ biến **source code** thành **knowledge graph** (đồ thị tri thức) — mỗi hàm, class, import, call-chain, và execution-flow đều được lưu trữ trong một database graph + vector có thể query. Sau đó, GitNexus expose graph đó qua **16 MCP tools** cho AI coding agents (Claude Code, Cursor, Codex, Windsurf, OpenCode), giúp agent hiểu cấu trúc codebase trước khi sửa code.

**Philosophy chính:** *"Building nervous system for agent context"* (Xây dựng hệ thần kinh cho agent context). AI agents hiện tại có "cảm nhận" code ở cấp độ text (grep + regex) nhưng thiếu **nhận thức kiến trúc** — khi agent sửa một function, nó không biết có 47 function khác phụ thuộc vào return type của nó. GitNexus lấp khoảng trống này bằng graph precomputed.

**Chạy ở 5 môi trường:**
1. **npm CLI:** `npm install -g gitnexus` (developer laptop)
2. **Browser:** gitnexus.vercel.app (zero-install, kéo thả ZIP)
3. **Docker Compose:** team-deployment container
4. **Kubernetes với Sigstore-signed images:** production multi-tenant
5. **Bridge mode:** `gitnexus serve` (local backend + browser UI)

### EN

GitNexus converts **source code** into a **knowledge graph** — every function, class, import, call-chain, and execution-flow is stored in a graph+vector database that can be queried. GitNexus then exposes this graph through **16 MCP tools** to AI coding agents (Claude Code, Cursor, Codex, Windsurf, OpenCode), enabling agents to understand codebase structure before modifying code.

**Core philosophy:** *"Building nervous system for agent context."* Current AI agents "sense" code at text level (grep + regex) but lack **architectural awareness** — when an agent modifies a function, it doesn't know that 47 other functions depend on its return type. GitNexus fills this gap with a precomputed graph.

**5 deployment modes:**
1. npm CLI global install
2. Browser-native (WebGPU + WASM, drag-and-drop ZIP)
3. Docker Compose
4. Kubernetes with Sigstore-signed image verification
5. Bridge mode (local backend + browser UI)

---

## Phần 2 — Tín hiệu độc đáo trong corpus / Corpus-first signals

GitNexus có **14 điểm đầu tiên** trong Storm Bear corpus (33 wikis):

1. **Tác giả Ấn Độ đầu tiên** — Abhigyan Patwari, Guwahati, Assam (joins Korean OMC v27, VN codymaster v12 + claude-howto v32 as regional observations)
2. **License PolyForm Noncommercial 1.0.0 đầu tiên** — standardized non-OSI commercial-gate family
3. **Archetype "CS-student + commercial-company" đầu tiên** — khác Pattern #44 academic-lab faculty
4. **LadybugDB database đầu tiên** — embedded graph+vector DB
5. **Browser-native knowledge-graph runtime đầu tiên** — WASM tree-sitter + WASM LadybugDB + transformers.js + WebGPU
6. **Sigstore-signed Docker đầu tiên** — supply-chain signing
7. **Kubernetes policy-controller enforcement đầu tiên** — admission control docs
8. **"Nervous system for agent context" philosophy đầu tiên** — khác graphify v16 "/raw folder answer"
9. **BM25 + semantic + RRF hybrid search đầu tiên** — hybrid search primitive
10. **Git-diff-impact as MCP tool đầu tiên** — `detect_changes` tool
11. **14 languages với capability matrix chi tiết nhất** — type-annotation + constructor-inference disclosed per-language
12. **16 MCP tools — nhiều nhất per-project** trong corpus
13. **Anti-crypto disclaimer on top của README đầu tiên** — scam-denial leading
14. **Bidirectional Claude Code hooks đầu tiên** — PreToolUse + PostToolUse

---

## Phần 3 — Scope: Tại sao GitNexus thuộc Tier 4 / Tier placement

**T4 Agent-as-bridge** — GitNexus bridges codebase (source) → knowledge graph → MCP → agent (consumer). Không autonomous execute task (không phải T5), không dạy học (không T3), không assistant framework (không T1), không host service (không T2). Peer trực tiếp là **graphify v16**.

**T4 7-way lineup sau v33:**

| # | Wiki | Version | Archetype |
|---|------|---------|-----------|
| 1 | gws | v13 | Corporate-broad (official Google, Rust) |
| 2 | notebooklm-py | v7 | Solo-narrow (teng-lin, Python) |
| 3 | graphify | v16 | Solo-broad-local (safishamsi, Python, 30K) |
| 4 | TrendRadar | v19 | Solo-broad-external (sansan0, Python, 52K CN) |
| 5 | markitdown | v28 | Corporate-narrow-utility (Microsoft AutoGen, Python, 114K) |
| 6 | crawl4ai | v29 | Solo-enterprise-scale (unclecode, Python, 64K) |
| 7 | **GitNexus** | **v33** | **Solo-student + commercial-entity (Abhigyan + akonlabs, TypeScript, 28.5K)** |

**T4 đã có 7 archetypes — tier đa dạng thứ 2 sau T1 (N=10).**

---

## Phần 4 — Cài đặt / Installation

### Bước 1 — Chọn deployment mode

**Cho developer cá nhân (nhanh nhất):**
```bash
npm install -g gitnexus
```

**Cho zero-install (browser):**
Truy cập https://gitnexus.vercel.app → kéo thả ZIP → index trong browser

**Cho team (Docker):**
```bash
git clone https://github.com/abhigyanpatwari/GitNexus
cd GitNexus
docker compose up -d
```

**Cho production (Kubernetes + Sigstore):**
Dùng K8s policy-controller (sigstore.dev/policy-controller) verify signed images. Config trong `kubernetes/` folder của repo.

### Bước 2 — Index codebase đầu tiên

```bash
cd /path/to/your/repo
gitnexus analyze
```

GitNexus sẽ:
- Parse code với tree-sitter (14 languages)
- Build knowledge graph trong LadybugDB
- Tính embedding với transformers.js
- Save ra `.gitnexus/` folder

### Bước 3 — Setup MCP cho AI editor

```bash
gitnexus setup
```

Command này auto-config:
- Claude Code: `.claude/settings.json` + hooks + 4 skills
- Cursor: `.cursor/mcp.json` + skills
- Codex: config file
- Windsurf: MCP-only
- OpenCode: MCP + skills

### Bước 4 — Thử query

Trong Claude Code session, type:
```
Use GitNexus to find all functions that call `authenticateUser`
```

Claude sẽ call `query` MCP tool của GitNexus và trả về process-grouped results.

---

## Phần 5 — Core usage pattern / Cách dùng cơ bản

### 5.1 — Tìm context cho function

Claude Code agent tự động call `context` tool trước khi edit một function. Agent nhận:
- Định nghĩa function
- List các function gọi nó (inbound calls)
- List các function nó gọi (outbound calls)
- Cluster mà function thuộc về
- Confidence score (EXTRACTED / INFERRED / AMBIGUOUS — inherited từ graphify v16 pattern)

### 5.2 — Phân tích blast radius trước khi sửa

```
Claude: "I'm going to change the return type of `getUser` from User to UserDTO"
GitNexus impact tool returns: "23 functions in 4 files will be affected. Top-affected:
- authController.ts (5 call sites)
- profileView.tsx (8 call sites)
- tests/user.test.ts (6 call sites)"
```

### 5.3 — Multi-file coordinated rename

```
gitnexus rename --old getUser --new fetchUser
```

Hoặc trong Claude Code via MCP tool. GitNexus đảm bảo tất cả call sites được update consistently.

### 5.4 — Git-diff impact

Sau khi operator làm `git diff`, GitNexus `detect_changes` tool map changed lines → affected processes:

```
Diff: modified src/auth/token.ts:L45-L62
Affected processes:
- Login flow (4 steps impacted)
- API authorization middleware (3 steps impacted)
- Session refresh (2 steps impacted)
```

### 5.5 — Multi-repo group operations

Cho org có micro-services:
```bash
gitnexus group create payments
gitnexus group add payments payments-auth payments-api payments-billing
gitnexus group_query payments "which services consume UserToken type?"
```

---

## Phần 6 — Novel concepts / Khái niệm mới

### 6.1 — "Nervous system for agent context" (Hệ thần kinh cho agent context)

Metaphor: Agent AI hiện tại có "giác quan text" (grep + regex) nhưng không có "nhận thức cấu trúc". GitNexus = hệ thần kinh cung cấp spatial awareness. Khi bạn sửa code, agent "cảm nhận" được 47 function khác phụ thuộc — giống như bạn cảm nhận tay mình khi chạm vào vật gì.

### 6.2 — Process-grouped search (Tìm kiếm nhóm theo process)

Traditional search: list flat các file matches.
GitNexus search: results grouped theo execution-flow.

Ví dụ: search "authentication" không trả về 50 file rải rác mà trả về 3 nhóm:
- **Sign-up flow:** 5 functions
- **Login flow:** 7 functions
- **OAuth flow:** 4 functions

### 6.3 — LadybugDB: graph + vector trong 1 embedded DB

Các solution khác cần Neo4j + Pinecone (2 systems). LadybugDB combine graph structure + vector similarity. WASM variant chạy trong browser.

### 6.4 — Claude Code bidirectional hooks (PreToolUse + PostToolUse)

- **PreToolUse:** trước khi Claude chạy Edit tool → GitNexus fetch context → append vào input
- **PostToolUse:** sau khi Claude hoàn tất → GitNexus detect file changes → incremental re-index

Graph không bao giờ stale. Agent luôn có context mới nhất.

### 6.5 — BM25 + semantic + RRF (Reciprocal Rank Fusion)

Hybrid search combining:
- **BM25** — keyword match (truyền thống, tốc độ cao)
- **Semantic** — embedding cosine similarity (hiểu nghĩa)
- **RRF** — re-rank results từ cả 2 nguồn

Kết quả: tìm được cả exact keyword match + semantic match.

---

## Phần 7 — So sánh với corpus frameworks / vs other corpus frameworks

| Use case | GitNexus v33 | graphify v16 | Recommendation |
|----------|--------------|--------------|----------------|
| Pure-code knowledge graph | ✅ Strong (browser + CLI + MCP) | ⚠️ Good (Python-local, broad file types) | GitNexus if code-only + browser |
| Markdown vault (Obsidian) | ❌ Not supported (code-only) | ✅ Native | **graphify** |
| Papers + images + videos | ❌ Code-only | ✅ Graphify "any folder" | **graphify** |
| Claude Code integration depth | ✅ Deepest (hooks + 16 MCP tools + 4 skills) | ✅ Good (skill + MCP) | GitNexus |
| Commercial use (MIT-compatible) | ❌ PolyForm gate | ✅ MIT unrestricted | **graphify** |
| Browser-native zero-install | ✅ gitnexus.vercel.app | ❌ pip local | GitNexus |
| Supply-chain signing | ✅ Sigstore + K8s policy | ❌ pip-only | GitNexus (for regulated) |

**Verdict cho Storm Bear vault (markdown-heavy):** graphify v16 là lựa chọn tốt hơn.
**Verdict cho pure-code projects (TypeScript/React):** GitNexus excel hơn với hooks + MCP.

---

## Phần 8 — ⚠️ Ethical + License framing / Khung pháp lý + đạo đức

### VN — PolyForm Noncommercial 1.0.0 CHI TIẾT

**Được dùng MIỄN PHÍ khi:**
- ✅ Cá nhân (research, experiment, testing, hobby, amateur)
- ✅ Trường đại học / viện nghiên cứu / cơ quan chính phủ / charity
- ✅ Mục đích "không có anticipated commercial application"

**BẮT BUỘC có commercial license khi:**
- ⚠️ Dùng trong công việc commercial software development
- ⚠️ Bundle vào sản phẩm bán ra thị trường
- ⚠️ Distribute dưới dạng commercial derivative

### Cho Storm Bear operator (Scrum coach)

**Scenario permitted (free):**
- Index vault cá nhân để nghiên cứu
- Viết blog post về GitNexus để share public knowledge
- Thử nghiệm tool để quyết định có commercial-adopt hay không

**Scenario cần commercial license:**
- Sử dụng GitNexus trực tiếp trong session với khách hàng trả tiền Scrum consulting
- Bundle GitNexus trong commercial Scrum-coaching product
- Research codebase của khách hàng bằng GitNexus để deliver commercial report

**Scenario gray zone (clarify với akonlabs):**
- Research technical concept để chuẩn bị cho gig commercial (borderline)
- Personal productivity tool dùng trong workflow mà có cả commercial + personal

### Cách làm đúng

1. Email `founders@akonlabs.com` với use-case cụ thể
2. Yêu cầu pricing cho commercial license tier phù hợp
3. Compare với alternative (graphify MIT) trước khi commit

### Patent clause caution

License terminate ngay lập tức nếu bạn claim GitNexus xâm phạm patent của bạn. Lưu ý trước khi take legal action.

---

## Phần 9 — Storm Bear operator relevance

### Direct utility: **MEDIUM-LOW** cho vault (code-only không fit markdown) / **MEDIUM-HIGH** cho code projects (Claude Code integration sâu)

### Observational value: **HIGH**

- Pattern #31 Open-Core reaches N=4 — 4 distinct license strategies observed
- Pattern #72 NEW candidate — PolyForm Noncommercial Commercial-Gate
- Pattern #17 ecosystem-layer single-flagship variant
- Pattern #27 Community-Viral 10th data point (sustained ~3.3K/mo)
- Pattern #18 MCP runtime standard — largest per-project exposure (16 tools)

### Pilot ranking **#11 trong corpus** (lowest-priority)

**Lý do:**
1. Markdown vault không fit (graphify v16 #6 tốt hơn ở vai trò này)
2. PolyForm commercial-gate friction cho Scrum consulting
3. Code-only focus limit vault applicability

**Nếu vẫn pilot:** personal exploration mode (free), compare với graphify, quyết định dựa trên operator workflow preference.

---

## Phần 10 — Lộ trình học 4 tuần / 4-week learning roadmap

### Tuần 1 — Observational
- Đọc README + CONTRIBUTING của GitNexus
- Xem demo ở gitnexus.vercel.app (browser, không install)
- So sánh với graphify v16 wiki trong corpus
- Quyết định: có lý do pilot cụ thể không?

### Tuần 2 — Personal pilot (optional)
- Nếu có code project pilot: `npm install -g gitnexus` + analyze
- Cấu hình Claude Code: `gitnexus setup`
- Thử 3-5 query scenarios
- Note: zero-cost nếu personal use

### Tuần 3 — Compare + commercial decision
- Email `founders@akonlabs.com` nếu có commercial use case
- Get pricing tier
- Compare với graphify v16 trade-off
- Decide: adopt GitNexus commercial / adopt graphify MIT / build custom

### Tuần 4 — Apply hoặc move on
- Nếu adopt: integrate vào daily workflow
- Nếu không: extract pattern observations (Pattern #31 N=4 là tài sản) rồi move on

---

## Phần 11 — Trade-offs + limitations

### Strengths
- Deepest Claude Code integration (hooks + 16 MCP tools + 4 skills)
- Browser-native zero-install
- Sophisticated search (BM25 + semantic + RRF)
- Multi-repo group operations (corpus-first)
- Sigstore supply-chain signing (corpus-first)
- Active development (weekly commits)

### Weaknesses
- **Code-only** (14 languages; no markdown / docs / images / videos)
- **PolyForm Noncommercial license gate** — commercial use requires akonlabs agreement
- **Browser mode 5K file limit** (backend mode needed for large repos)
- **No SECURITY.md** — vulnerability disclosure channel undocumented
- **Solo-student author bus factor** — akonlabs commercial entity mitigation partial
- **No quantitative benchmark** — "token-efficient" claim without data
- **EN-only docs** — at 28.5K scale, absence notable

---

## Phần 12 — Caveats + safety notes / Lưu ý an toàn

### Supply-chain awareness

GitNexus ingests codebases as INPUT — potential risks:
- **Trusted repos (own code):** low risk
- **External repos (3rd-party clone for analysis):** low-medium risk (static analysis only; no execution)
- **MCP server output → agent consumption:** inference risk (if GitNexus classifies malicious code as safe, agent downstream decisions affected)

### Positive supply-chain signals
- Sigstore Cosign keyless signing
- Kubernetes policy-controller admission enforcement
- Transparent build process (Docker image verification via Rekor)

### Privacy
- **CLI mode:** everything local, no network except optional LLM for wiki generation
- **Browser mode:** in-browser, no server
- **Bridge mode:** local HTTP (127.0.0.1)
- **Docker:** container isolation
- **K8s:** multi-pod isolated

### PolyForm license termination clause
- Patent claim by licensee → license terminates immediately
- Think before legal action against GitNexus or akonlabs

---

## Phần 13 — Tham khảo + Next action / References + next action

### References

- **Repo:** github.com/abhigyanpatwari/GitNexus
- **Homepage:** gitnexus.vercel.app
- **npm:** npmjs.com/package/gitnexus
- **Discord (community):** discord.gg/MgJrmsqr62
- **Commercial:** akonlabs.com (founders@akonlabs.com)
- **License:** polyformproject.org/licenses/noncommercial/1.0.0/

### Storm Bear cross-references

- [[graphify - Beginner Analysis]] v16 — DIRECT PEER (MIT, Python-local, markdown-friendly)
- [[markitdown - Beginner Analysis]] v28 — document-ingestion peer
- [[crawl4ai - Beginner Analysis]] v29 — web-crawler peer (Apache)
- [[fish-speech - Beginner Analysis]] v20 — Pattern #31 #1 data point (custom research license)
- [[Skyvern - Beginner Analysis]] v24 — Pattern #31 #2 data point (AGPL)
- [[OpenHands - Beginner Analysis]] v30 — Pattern #31 #3 data point (MIT + enterprise directory)

### Next action cho operator

**STOP**: Đừng install GitNexus nếu chưa rõ PolyForm commercial constraint
**READ**: Mục #8 của guide này về license trước khi pilot
**COMPARE**: Đọc [[graphify - Beginner Analysis]] v16 wiki để quyết định tool nào fit vault

### Next wiki candidate

Pattern Library ở 0.73:1 ratio (healthy). Sau v33 sẽ ở ~0.76:1 (nếu +1 candidate). Next wiki options:
1. **HIGH:** Execute deferred v27 diagnostic HIGH bundle (9 sessions deferred — BLOCKING recommendation)
2. **MEDIUM:** Observer Indian-ecosystem OSS for 2nd regional observation
3. **MEDIUM:** Monitor for 2nd PolyForm-family adoption (Pattern #72 un-stale trigger)
4. **LOW:** Additional T4 or T1 wiki (corpus structurally complete)

---

**Hướng dẫn này là phần của Storm Bear corpus (33 wikis). Maintained by Claude via routine v2.1. Questions or feedback: see vault root CLAUDE.md.**
