# agentmemory — Hướng dẫn cho người mới / Beginner's Guide

> **Chủ đề / Subject:** [`rohitg00/agentmemory`](https://github.com/rohitg00/agentmemory)
> **Wiki version:** v66 — Storm Bear vault — built 2026-05-14
> **Routine:** `llm-wiki-routine-v2.2`
> **Một câu / In one line:** Bộ nhớ bền bỉ (persistent memory) cho AI coding agent — agent của bạn "nhớ" mọi thứ giữa các phiên làm việc, không phải giải thích lại từ đầu.

---

## 1. agentmemory là gì? / What is it?

### 🇻🇳 Tiếng Việt

Mỗi khi bạn mở một phiên (session) mới với Claude Code (hoặc Cursor, Cline, Gemini CLI...), agent **quên sạch** mọi thứ từ phiên trước: kiến trúc dự án, sở thích của bạn, những bug đã gặp. Bạn phải giải thích lại từ đầu, mỗi lần.

**agentmemory** giải quyết đúng vấn đề đó. Nó là một **"động cơ bộ nhớ" (memory engine)** chạy nền dưới dạng một server:
- **Tự động ghi lại** (auto-capture) mọi việc agent làm — qua 12 "hook" tự kích hoạt, không cần thao tác tay
- **Nén & sắp xếp** các quan sát đó thành một kho kiến thức có thể tìm kiếm
- **Tiêm lại** (inject) đúng những ký ức liên quan vào mỗi phiên mới

Khẩu hiệu của dự án: *"Your coding agent remembers everything. No more re-explaining."* — "Agent của bạn nhớ mọi thứ. Không phải giải thích lại."

Điểm mấu chốt: **một server, nhiều agent dùng chung** — bạn cài một lần, và Claude Code, Cursor, Cline... đều kết nối tới cùng một kho ký ức.

### 🇬🇧 English

agentmemory is a **persistent memory engine for AI coding agents**. Every coding agent forgets everything when a session ends — agentmemory captures what the agent does (via 12 automatic lifecycle hooks), compresses those observations into a searchable knowledge base, and injects only the most relevant memories into each new session. One server runs in the background; 15+ agent platforms connect to it as clients. Tagline: *"Your coding agent remembers everything. No more re-explaining."*

It is classified as a **T2 Service** in the Storm Bear corpus — the **first dedicated agent-memory-system** across 65 wikis.

---

## 2. Ai là tác giả? Có gì đáng chú ý? / Who's the author? What's notable?

### 🇻🇳 Tiếng Việt

- **Tác giả:** Rohit Ghumare — một kỹ sư cá nhân (solo individual engineer), gắn email cá nhân `ghumare64@gmail.com`. Không phải công ty, không phải đội lớn.
- **Giấy phép:** Apache-2.0 (rất thoáng — dùng thương mại được).
- **Tuổi đời:** Cực kỳ trẻ — bản phát hành đầu tiên `[0.8.0]` ngày **2026-04-09**, tức là chỉ **~35 ngày tuổi** tại thời điểm wiki này.
- **Độ phổ biến:** 7,900 sao / 675 fork — tức **~226 sao/ngày**. Đây là tốc độ *rất cao* (chỉ thấp hơn một chút so với ngưỡng "viral cực đoan" 300 sao/ngày của corpus).

**Tín hiệu "corpus-first" (lần đầu xuất hiện trong 65 wiki):**
1. **Hệ thống bộ nhớ agent chuyên dụng đầu tiên** trong corpus.
2. **"Platform-Primitive Foundation"** — agentmemory được xây *hoàn toàn* trên nền tảng của một dự án khác (iii-engine), tự nhận mình *"là một iii instance đang chạy"*. Đây là quan sát cấu trúc mới — xem mục 4.
3. **Benchmark lĩnh vực bộ nhớ đầu tiên** — dùng LongMemEval-S (ICLR 2025), tuyên bố đạt 95.2% R@5.

### 🇬🇧 English

Author: **Rohit Ghumare**, a solo individual engineer. Apache-2.0. The repo is **~35 days old** (first release 2026-04-09) yet has **7,900 stars** — roughly **226 stars/day**, a very high velocity just under the corpus's 300/day "extreme-viral" threshold. Three corpus-firsts: first dedicated agent-memory-system; first "Platform-Primitive Foundation" (built entirely on iii-engine, self-identifying as an iii instance); first memory-retrieval-domain benchmark (LongMemEval-S, ICLR 2025, claimed 95.2% R@5).

---

## 3. Cài đặt & cách dùng / Installation & core usage

### 🇻🇳 Tiếng Việt

**Cài đặt — một lệnh duy nhất:**

```bash
npx @agentmemory/agentmemory
```

Lệnh này khởi động: server bộ nhớ ở **cổng 3111** (REST API) + một trình xem trực quan (viewer) ở **cổng 3113**.

**Yêu cầu:** Node.js ≥ 20, và *hoặc* binary `iii-engine` *hoặc* Docker.

**Cách dùng cơ bản:** Sau khi server chạy, bạn nối agent của mình vào:
- **Claude Code** — sâu nhất: 12 hook + MCP + skill (qua plugin)
- **Cursor / Claude Desktop / Cline / Roo Code / Windsurf / Gemini CLI / OpenCode** — qua cấu hình MCP server chuẩn
- **Codex CLI** — 6 hook + MCP
- **Bất kỳ agent nào** — qua REST API (107 endpoint)

Sau đó: bạn không phải làm gì cả. 12 hook tự ghi lại mọi thứ. Khi cần, agent gọi các MCP tool như `memory_recall`, `memory_smart_search`, hoặc skill `/recall`, `/remember`.

### 🇬🇧 English

One command: `npx @agentmemory/agentmemory` launches the memory server (port 3111) + viewer (port 3113). Needs Node ≥20 and either the `iii-engine` binary or Docker. Connect any of 15+ agent platforms: Claude Code gets the deepest integration (12 hooks + MCP + skills), most editors connect via a standard `mcpServers` config block, and any HTTP-capable agent uses the 107-endpoint REST API. After setup it is zero-effort — the 12 hooks auto-capture; the agent calls tools like `memory_recall` / `memory_smart_search` or skills `/recall` / `/remember` when needed.

---

## 4. Kiến trúc đặc biệt / The novel architecture

### 🇻🇳 Tiếng Việt

**(a) Bộ nhớ 4 tầng — mô phỏng giấc ngủ của con người.** Đây là ý tưởng đặc trưng nhất:

| Tầng | Chứa gì | Ví von trí nhớ người |
|---|---|---|
| **Working** (làm việc) | quan sát thô từ việc dùng tool | trí nhớ ngắn hạn |
| **Episodic** (giai thoại) | tóm tắt phiên đã nén | "chuyện gì đã xảy ra" |
| **Semantic** (ngữ nghĩa) | sự kiện & mẫu hình rút ra | "tôi biết gì" |
| **Procedural** (quy trình) | quy trình & cách ra quyết định | "làm thế nào" |

Ký ức **phai dần theo thời gian** (đường cong quên Ebbinghaus), **mạnh lên khi được dùng**, và **tự xóa khi cũ**. Đây không phải kho lưu trữ phẳng — mà là một *dây chuyền chưng cất* kiến thức.

**(b) Tìm kiếm 3 luồng (triple-stream).** Khi truy hồi ký ức, agentmemory chạy song song 3 tín hiệu: **BM25** (khớp từ khóa) + **Vector** (tương đồng ngữ nghĩa) + **Graph** (duyệt đồ thị tri thức) — rồi hợp nhất bằng Reciprocal Rank Fusion (k=60).

**(c) "Platform-Primitive Foundation" — phát hiện cấu trúc chính của wiki này.** agentmemory **không tự viết hạ tầng của mình**. Mọi thứ — phục vụ HTTP, lưu trữ, stream, giám sát tiến trình, observability, hệ thống plugin — đều giao cho các "primitive" của iii-engine. README nói thẳng: *"agentmemory **là một iii instance đang chạy**."* Bằng chứng rõ nhất: `package.json` chỉ có **6 dependency**, không có framework HTTP, không có driver database. Toàn bộ hạ tầng nằm gọn trong một dòng `iii-sdk`.

### 🇬🇧 English

Three novel pieces: **(a) 4-tier consolidation** modelled on human sleep — Working → Episodic → Semantic → Procedural, with Ebbinghaus decay, strengthen-on-access, auto-evict-when-stale. **(b) Triple-stream RRF search** — BM25 + Vector + Graph fused with Reciprocal Rank Fusion (k=60), session-diversified to max 3 per session. **(c) Platform-Primitive Foundation** — agentmemory rolls *none* of its own infrastructure; HTTP/storage/streams/supervision/observability/plugins are *all* delegated to iii-engine primitives. The README states it "is already a running iii instance"; the proof is a 6-dependency `package.json` with no HTTP framework and no DB driver. This is the wiki's PRIMARY corpus-first structural observation.

---

## 5. So với cách khác / vs other approaches

### 🇻🇳 Tiếng Việt

agentmemory tự đặt mình cạnh các đối thủ — bảng so sánh trong README:

| | agentmemory | mem0 (53K⭐) | Letta/MemGPT (22K⭐) | CLAUDE.md thủ công |
|---|---|---|---|---|
| Độ chính xác R@5 | **95.2%** | 68.5% | 83.2% | không có (chỉ grep) |
| Tự động ghi | 12 hook (0 công sức) | gọi tay | agent tự sửa | sửa tay |
| Chiến lược tìm | BM25+Vector+Graph | Vector+Graph | chỉ Vector | nạp hết context |
| Phụ thuộc ngoài | Không (SQLite+iii) | Qdrant/pgvector | Postgres+vector DB | Không |

**Lưu ý quan trọng cho Storm Bear:** cột cuối — "CLAUDE.md thủ công" — *chính là cách vault Storm Bear đang làm hiện nay*. agentmemory định vị mình đối lập trực tiếp với cách đó.

### 🇬🇧 English

agentmemory ships an explicit competitor table (vs mem0, Letta/MemGPT, and the manual "Built-in CLAUDE.md" approach). Note the last column — the hand-maintained CLAUDE.md + grep method — **is exactly what the Storm Bear vault does today.** agentmemory positions itself directly against it. (See section 8 for whether the vault should switch.)

---

## 6. Số liệu nhanh / Quick stats

| Field | Value |
|---|---|
| Repo | `rohitg00/agentmemory` |
| Tác giả / Author | Rohit Ghumare (solo) |
| License | Apache-2.0 |
| Stack | TypeScript 82.4% — `@agentmemory/agentmemory` v0.9.12 (npm) |
| Built on | iii-engine (Platform-Primitive Foundation) |
| Stars / forks / subscribers | 7,900 / 675 / 23 |
| Tuổi / Age | ~35 ngày (first release 2026-04-09) |
| Tốc độ / Velocity | ~226 sao/ngày (cao; dưới ngưỡng 300/ngày) |
| Releases | 34 (v0.8.0 → v0.9.12) |
| Quy mô / Scale | 118 files · ~21,800 LOC · 827 tests · 123 functions · 34 KV scopes |
| Kiến trúc | 4-tier memory + triple-stream RRF + 12 hooks + 51 MCP tools + 107 REST endpoints |
| Benchmark | 95.2% R@5 trên LongMemEval-S (ICLR 2025) — *tuyên bố của dự án, wiki chưa kiểm chứng độc lập* |
| Platforms | 15+ (Claude Code sâu nhất) |
| Tier (corpus) | T2 Service — hệ thống bộ nhớ agent chuyên dụng đầu tiên |

---

## 7. Điểm cần lưu ý & an toàn / Caveats & safety

### 🇻🇳 Tiếng Việt

Đây là phần **quan trọng nhất** cho người mới. agentmemory có kiến trúc tốt, nhưng là một repo **rất trẻ chạy theo sóng viral** — chất lượng chưa kịp "chín". Năm phát hiện:

1. **`DESIGN.md` bị "nhiễm" nội dung lạ.** File `DESIGN.md` của dự án chứa **288 dòng về một "hệ thống thiết kế lấy cảm hứng từ Lamborghini"** — bảng màu, font chữ, không liên quan gì tới bộ nhớ. Đã kiểm chứng 3 lần (2 WebFetch + 1 curl thô). Đây là dấu hiệu mạnh của repo "vibe-code" / scaffold bằng AI mà không ai đọc lại.

2. **README "nói quá" so với ROADMAP.** README quảng cáo *"ký ức chia sẻ giữa tất cả agent"* như đã có; ROADMAP lại liệt kê "chia sẻ ký ức giữa các agent" là **mục tiêu Q3 2026** và "cô lập đơn-agent" là **giới hạn hiện tại**.

3. **AGENTS.md lệch phiên bản.** AGENTS.md ghi "v0.8.9: 44 MCP tool"; README ghi "v0.9.12: 51 MCP tool". Tài liệu chưa đồng bộ.

4. **6 lỗ hổng CRITICAL/HIGH đã sửa ở v0.8.2** — phiên bản thứ 2 trong đời. Gồm: Stored XSS (CRITICAL), **RCE qua `curl|sh`** (CRITICAL), server mở mặc định ra `0.0.0.0` (HIGH), mesh sync không xác thực (HIGH), path traversal (MEDIUM), lọc bí mật không đầy đủ (MEDIUM). Đã sửa nhanh — nhưng từng tồn tại, công khai, trong một công cụ *ăn vào mọi thứ agent làm*.

5. **Nhưng** — CHANGELOG và ROADMAP lại **rất kỷ luật và trung thực** (theo chuẩn Keep-a-Changelog, ghi rõ breaking change, thừa nhận "default cũ đốt token"). Tác giả *biết* viết tài liệu tốt — nên 4 phát hiện trên là chuyện *chất lượng chưa theo kịp tốc độ*, không phải repo cẩu thả.

**An toàn:** agentmemory có "privacy by design" — API key, secret, và nội dung gắn thẻ `<private>` bị loại bỏ *trước khi* lưu. Nhưng với một repo 35 ngày tuổi vừa có RCE, **niềm tin vào bộ lọc đó còn mỏng** — cần tự kiểm chứng.

### 🇬🇧 English

This is the most important section for a newcomer. agentmemory has a sound architecture but is **a very young repo riding a viral wave — quality has not caught up**. Five findings: (1) `DESIGN.md` is contaminated — 288 lines of an unrelated "Lamborghini design system," verified 3 ways; a strong vibe-coded/AI-scaffolded signal. (2) README over-claims vs ROADMAP — "shared across all agents" is marketed as current but is a Q3 2026 roadmap item. (3) AGENTS.md is version-skewed. (4) Six CRITICAL/HIGH vulns — including an RCE — were fixed at v0.8.2, the second-ever version. (5) *But* the CHANGELOG and ROADMAP are genuinely disciplined and honest, which makes this a *maturity-lag* story, not a low-effort one. Safety: privacy-by-design strips secrets/`<private>` before storage — but trust in that filter is thin at 35 days old with a recent RCE. Verify it yourself before pointing it at anything sensitive.

---

## 8. Liên quan gì tới Storm Bear? / Storm Bear relevance + pilot recommendation

### 🇻🇳 Tiếng Việt

Đây là wiki **liên quan trực tiếp nhất tới vault Storm Bear** trong nhiều wiki gần đây. Lý do:

- Vault Storm Bear **chính là** một hệ thống bộ nhớ bền bỉ — chạy *trên* Claude Code, duy trì thư mục `memory/` và CLAUDE.md *bằng tay*.
- Đó *đúng là* cột "CLAUDE.md thủ công" mà agentmemory định vị đối lập (mục 5).
- Vault **đã từng gặp** đúng thất bại agentmemory mô tả: CLAUDE.md từng phình tới 584 KB / ~146K token và phải refactor (session 67).

**Phase 0.9 — 4/4 tiêu chí STRICT PASS** (lần đầu đạt đủ cả 4 trong cửa sổ gần đây): (a) tác giả là kỹ sư solo — ngang hàng cấu trúc với Storm Bear; (b) công cụ vận hành trực tiếp cho vault; (c) mô hình 4 tầng ảnh hưởng tới phương pháp tổ chức bộ nhớ của vault; (d) là tham chiếu trong corpus (tích hợp sâu với Claude Code; "anh em" với dự án `graphify`).

**Khuyến nghị pilot (thử nghiệm):** agentmemory **đáng để pilot** — nhưng là một **pilot có rào chắn**, không phải thay thế toàn bộ:
1. Chạy thử trên một **dự án nháp vứt đi** trước — kiểm chứng bộ lọc privacy *trước khi* cho nó thấy nội dung vault.
2. Nếu đạt — chạy **chế độ chỉ-đọc** trên vault qua 1-2 lần build wiki; giữ CLAUDE.md/`_state/` làm bản ghi chính thức; so sánh agentmemory *lẽ ra* nhớ gì với iteration log thủ công.
3. **Cổng quyết định:** recall của agentmemory có thắng `grep` trên vault không? Nếu có — đào sâu. Nếu không — hệ thống thủ công thắng, và *từ vựng 4 tầng* là thứ đáng giữ lại.

**Dù pilot hay không:** nên mượn **từ vựng 4 tầng** (Working/Episodic/Semantic/Procedural) làm công cụ tư duy cho bộ nhớ vault, và mượn kỷ luật **"tự xóa khi cũ"** — vault hiện *không có* cơ chế quên, và 584 KB CLAUDE.md là hậu quả.

### 🇬🇧 English

This is the most directly vault-relevant wiki in recent corpus. The Storm Bear vault *is* a persistent memory system, running on Claude Code, maintaining `memory/` + CLAUDE.md by hand — exactly the "Built-in CLAUDE.md" column agentmemory positions against, and the vault has already hit the failure mode agentmemory describes (the 584 KB CLAUDE.md refactor). Phase 0.9 scored **4/4 STRICT PASS** (widest criteria-coverage in the post-amendment window). **Pilot recommendation: pilot it behind a fence** — scratch project first (verify privacy filtering), then read-mostly on the vault for 1-2 builds, then a decision gate (does its recall beat `grep`?). Regardless of the pilot, adopt the 4-tier vocabulary as a thinking tool and the "auto-evict when stale" discipline — the vault has no forgetting mechanism, and the 584 KB CLAUDE.md is what that costs.

---

## 9. Lộ trình học 4 tuần / 4-week learning roadmap

### 🇻🇳 Tiếng Việt

**Tuần 1 — Hiểu vấn đề & kiến trúc.** Đọc README đầy đủ. Hiểu rõ "agent quên mọi thứ" là vấn đề gì. Vẽ lại sơ đồ 4 tầng bộ nhớ. Đọc Entity 1 của wiki này.

**Tuần 2 — Chạy thử cô lập.** `npx @agentmemory/agentmemory` trên một dự án nháp. Mở viewer cổng 3113. Quan sát hook nào ghi cái gì. Thử các MCP tool core (`memory_save`, `memory_recall`). **Kiểm chứng bộ lọc privacy** — tạo một file có API key giả, xem agentmemory có lọc không.

**Tuần 3 — Hiểu nền tảng.** Đọc Entity 2 (Platform-Primitive Foundation). Tìm hiểu iii-engine là gì. Hiểu vì sao `package.json` chỉ có 6 dependency. Đây là phần "corpus-first" — quan sát cấu trúc đáng giá nhất.

**Tuần 4 — Quyết định pilot.** Đọc Entity 3 (rủi ro) + Entity 4 (pilot). So sánh: agentmemory vs cách thủ công của bạn. Viết một quyết định ngắn: pilot có rào chắn, hay chỉ mượn từ vựng 4 tầng?

### 🇬🇧 English

**Week 1 — problem & architecture:** read the full README, internalize the "agents forget" problem, redraw the 4-tier diagram, read Entity 1. **Week 2 — isolated trial:** `npx` it on a scratch project, open the port-3113 viewer, watch which hooks capture what, try the core MCP tools, and *empirically verify the privacy filter* with a fake API key. **Week 3 — understand the foundation:** read Entity 2, learn what iii-engine is, understand why `package.json` has only 6 deps — this is the corpus-first structural payload. **Week 4 — pilot decision:** read Entity 3 (risks) + Entity 4 (pilot), compare against your manual method, write a short decision: fenced pilot, or just borrow the 4-tier vocabulary?

---

## 10. Đóng góp của wiki này / What this wiki contributes + next action

### 🇻🇳 Tiếng Việt

**Wiki v66 đóng góp vào Pattern Library:**
- **Ứng viên MỚI: Platform-Primitive Foundation** (N=1, stale-flagged) — quan sát corpus-first: một dự án xây *hoàn toàn* trên primitive của nền tảng khác, tự nhận là "instance đang chạy" của nền tảng đó. Đây là deliverable PRIMARY.
- **Pattern #18 — sub-archetype MỚI: shared-backend-service** — cơ chế đa-nền-tảng thứ 3 (cạnh Layer 1 coexistence + Layer 2 translation).
- **Pattern #8** — benchmark lĩnh vực bộ nhớ đầu tiên trong corpus.
- **Ứng viên quan sát MỚI: AI-Generated-Repo Artifact Contamination** — từ phát hiện DESIGN.md.
- **Phase 0.9** — 4/4 STRICT PASS, STRONG INCLUDE; streak lên 2.

**Hành động tiếp theo / Next action:** Nếu bạn là Storm Bear — quyết định pilot có rào chắn (xem Entity 4). Nếu bạn là người mới — chạy `npx @agentmemory/agentmemory` trên một dự án nháp trong tuần này, và mở viewer cổng 3113 để xem nó "nhớ" gì.

### 🇬🇧 English

The v66 wiki contributes to the Pattern Library: a **NEW candidate — Platform-Primitive Foundation** (N=1, the PRIMARY deliverable); a **NEW Pattern #18 sub-archetype — shared-backend-service**; **Pattern #8** first memory-domain benchmark; a **NEW observational candidate — AI-Generated-Repo Artifact Contamination**; and a Phase 0.9 4/4 STRICT PASS. **Next action:** if you're Storm Bear, decide on the fenced pilot (Entity 4); if you're a newcomer, `npx @agentmemory/agentmemory` on a scratch project this week and open the port-3113 viewer to watch it remember.

---

## Tài liệu tham khảo / Further reading

- Repo: [`github.com/rohitg00/agentmemory`](https://github.com/rohitg00/agentmemory)
- iii-engine (nền tảng): [`github.com/iii-hq/iii`](https://github.com/iii-hq/iii)
- Benchmark: LongMemEval-S (ICLR 2025)
- Wiki entities: [Entity 1 core](../02%20Wiki/entity-1-agentmemory-core.md) / [Entity 2 Platform-Primitive Foundation](../02%20Wiki/entity-2-platform-primitive-foundation.md) / [Entity 3 quality tension](../02%20Wiki/entity-3-distribution-and-quality-tension.md) / [Entity 4 Storm Bear meta](../02%20Wiki/entity-4-storm-bear-meta.md)
- Cross-wiki siblings: graphify (knowledge graph) / claude-code-system-prompts v65 / codex-plugin-cc v62 / free-claude-code v60 / n8n v56 / cc-sdd v61
