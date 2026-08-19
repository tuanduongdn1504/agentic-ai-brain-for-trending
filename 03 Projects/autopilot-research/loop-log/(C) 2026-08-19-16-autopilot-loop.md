# (C) Autopilot Loop — 2026-08-19-16

> **Trigger:** `/loop` (manual, operator-submitted anchor + operator-elected 4-video bundle)
> **Topic:** wecommit-tokens-and-context-window
> **Started:** 2026-08-19 16:34:15 +07
> **Ended:** 2026-08-19 17:01:43 +07
> **Duration:** ~27 min
> **Status:** COMPLETE — all 8 phases; `gaps_closed_ratio` = 1.0

---

## Phase 0 — Pre-flight

| Check | Result |
|---|---|
| Scope | `03 Projects/autopilot-research/` — writes bounded to project. PASS |
| `AUTOPILOT_ROOT` | env shim sourced; var echoed empty in the tool shell (known flaky-zsh stdout drop) — paths used absolute instead. NON-BLOCKING |
| `yt-dlp` | `/usr/local/bin/yt-dlp` PASS |
| `notebooklm` | present in `.venv/bin/notebooklm` (first `which` ran pre-activation → false MISSING). PASS, **not used this run** |
| Queue state | **0 pending topics** (`autopilot-drain.py --list-only`); last overnight drain 2026-08-18 23:35 exited `Nothing to drain` rc=0; no drain/caffeinate process alive. Nothing preempted. |
| launchd | `com.cvtot.autopilot-research` loaded, next fire 23:35 daily |

**Rule 6 budget breach — SURFACED, not hidden:** vault CLAUDE.md sets a 30K-token/session budget. A 4-video / 2h21m / 36,373-word bundle cannot be compiled inside it. Operator explicitly elected the 4-video bundle over the single-video scope, so the breach is instructed. Mitigation: transcripts are read by per-video subagents, NOT in the main loop, keeping main-loop context lean.

## Phase 1 — Wiki state read

- Topics before: **77** (`wiki/` dirs, excl. `_master-index.md`)
- `gaps_at_start`: **1** (the topic itself — new topic, cold start for this subject)

## Phase 2 — Source ingestion (Path 1 `/loop`, yt-dlp only; NO NotebookLM, NO yt-search)

All 4 videos from ONE creator — **@tranquochuywecommit** / "Learning Database with Tran Quoc Huy", channel `UCtsYzL7iN7rBCPnkjYp4XYw`, **189,000 subscribers** (largest VN-language source in the corpus to date — pending grep confirmation).

| # | Video | Role | Date | Dur | Views | Transcript |
|---|---|---|---|---|---|---|
| 1 | [`yxQGugIwFaU`](https://www.youtube.com/watch?v=yxQGugIwFaU) — "Mỗi lần chat, AI phải đọc toàn bộ lịch sử & cách tối ưu Token (Claude, ChatGPT, Gemini)" | **ANCHOR** (operator-submitted) | 2026-08-15 | 26:58 | 5,887 | 747 cues → 59 ¶ / 6,948 words |
| 2 | [`4PKT7vFo334`](https://www.youtube.com/watch?v=4PKT7vFo334) — "Claude: Cách Tôi Cho AI Vận Hành Cả Kênh YouTube (Demo thực tế và kỹ thuật tối ưu chi phí Token)" | sibling (longest) | 2026-08-02 | 59:26 | 4,267 | 1,678 cues → 129 ¶ / 15,291 words |
| 3 | [`MshYeoy8g2o`](https://www.youtube.com/watch?v=MshYeoy8g2o) — "Điểm yếu chí tử \"hay quên\" của AI Agent & chiến lược của các tập đoàn công nghệ" | sibling (oldest) | 2026-04-22 | 33:11 | 5,189 | 916 cues → 72 ¶ / 8,411 words |
| 4 | [`QgDsHhy9Cpo`](https://www.youtube.com/watch?v=QgDsHhy9Cpo) — "15 năm kinh nghiệm các dự án ngân hàng dạy tôi 1 nguyên tắc giúp AI Agent làm đúng \| Demo thực tế" | sibling | 2026-08-13 | 21:52 | 2,607 | 625 cues → 47 ¶ / 5,723 words |

**Total: 2h21m27s / 36,373 words** across 4 `vi-orig` auto-caption tracks (no manual subs on any of the 4 — ASR garble expected and tracked).

**Provenance detail caught at ingest:** the anchor's description links video 4 as *"Vì sao AI Agent của anh em làm sai hoài? Bản chất ở đây & Demo thực tế"*, but its current title is *"15 năm kinh nghiệm các dự án ngân hàng dạy tôi 1 nguyên tắc giúp AI Agent làm đúng"* — **the video was retitled after the anchor was published.** Link-text ≠ current title.

**Bundle selection:** siblings were NOT chosen by yt-search rubric — they are the 3 videos the anchor's own description links as related, i.e. creator-declared siblings. Higher precision than search-rank, and it makes the bundle a coherent single-author series rather than a topic sweep.

## Phase 3-6 — pending

Workflow `wf_2bd9115e-d48` — 13 agents (4 per-video extractors → 7 refute-first cluster verifiers + 1 corpus-collision grep → 1 completeness critic).

## Pre-registered verification target (the reason this bundle needs a refute-first pass)

The anchor's description claims every number was counted **"trên đúng bộ mã hóa mà Claude đang dùng"** (= on the *exact* encoder Claude uses). **Anthropic does not publish Claude's tokenizer.** The vault already carries the opposing standing pin at `wiki/mosh-ai-powered-apps/tokens-and-cost.md:18` — *"never use tiktoken for Claude — it undercounts by ~15–20%. Use `POST /v1/messages/count_tokens`."* Either he used `count_tokens` (legitimate) or a third-party/approximate tokenizer (his VN-vs-EN ratios then carry that error). This is claim #1 to break, not to accept.

---

## Phase 3-4 — Compile + cross-link (COMPLETE)

**Workflow `wf_2bd9115e-d48`** — 13 agents: 4 per-video extractors → 7 refute-first cluster verifiers (live WebSearch/WebFetch against first-party docs) + 1 corpus-collision grep → 1 completeness critic. **0 errors / 0 empty / 0 skipped.** ~968K subagent tokens, 177 tool calls, 454s (7.6 min).

**+ Opus main-loop adjudication (maker/checker):** re-read the raw transcripts, re-checked pricing against the `claude-api` skill's authoritative table, date-checked the vendor claims, and **overrode 6 verifier verdicts**.

Wiki output: **16 files** in `wiki/wecommit-tokens-and-context-window/`; **197 wiki links filesystem-validated, 0 broken**; `_master-index.md` updated (74 → 75 topics); `raw/_inventory.md` row raw → compiled.

## Phase 5 — Audit

| Metric | Value |
|---|---|
| `gaps_at_start` | 1 (new topic, cold start) |
| `gaps_at_end` | 0 |
| **`gaps_closed_ratio`** | **1.0** |

Two claims are recorded as UNVERIFIED rather than closed — they are honest boundaries, not gaps in the compile: `count_tokens` was not runnable in this environment (no `ant` CLI, no `ANTHROPIC_API_KEY`), and no video frames were analysed so the on-screen tokenizer cannot be identified.

## Phase 6 — Stop decision

**Stopped on condition 1:** `gaps_closed_ratio` (1.0) ≥ `target_ratio` (0.5) after cycle 1. No recursion (invariant #6).

## Phase 7 — Findings worth carrying forward

### ⭐ The methodological finding (most transferable)

**Our own extraction stage produced the only fabrication in the run.** Reading video 2's pricing table it reported "Claude 3.5 Opus" ($10/$50), "Claude 3 Opus" ($5/$25) and "Claude 3.5 Sonnet" ($2/$10). He says **Fable 5, Opus 5, Sonnet 5, Haiku** — and "Claude 3.5 Opus" never existed. It recorded the error **inside its own `asr_garble` field**, in the wrong direction (`Fable 5 → Claude 3.5 Opus`): it treated **current model names as ASR corruption** and restored them to its training prior. The safeguard became the vector.

Caught by an independent refute-first verifier → settled by `grep` on the transcript → first-party pricing then confirmed his *numbers* were correct throughout.

**Carry-forward rule: extraction cannot be trusted on any fast-moving proper noun — model names, versions, prices, product names. Grep the transcript.** This also makes the run live evidence for the source's own thesis (video 4) that a generator must never be its own verifier — the same doctrine as this project's `loop-verifier`.

### Verifier reliability (recorded, not hidden)

**5 excellent catches** (the fabrication above; the per-token-vs-volume precision on Vietnamese cost; the ACID naming gap) vs **6 over-reaches**:

- 2 verdicts asserted with **no URL** in a run whose instructions required one ("never let AI self-check" → FALSE; "AI doesn't know your criteria" → MISLEADING). Both refuted the theory while their own corrections conceded the practice.
- 1 **date-check never performed** — ChatGPT-timestamps called MISLEADING against a feature that shipped 2026-06-04, six weeks *after* the 2026-04-22 video.
- 1 **misreading of the source** — accused him of quoting cache *write* prices where *read* applies, when he says verbatim *"cách **phần ghi** này"* ("this cache **write** part"). His $6.25/$10 are exactly 1.25×/2×.

Pattern: **strongest checking a fact against a document, weakest arguing against a judgement.**

### Completeness critic earned its slot

It caught that video 2 (59:26) was **severely under-extracted** — 15 claims vs 28 for the 26:58 anchor — and that its entire agent-architecture section ([50:32]–[57:48]) was missing. Recovered by direct transcript reading. **Without the critic, the most substantial content in the longest video would have been silently dropped** — a Rule 12 near-miss.

### Rule 6 budget breach (surfaced, per invariant)

The vault's 30K-token session budget was exceeded, as flagged in Phase 0. Operator elected the 4-video bundle over the single-video scope, so the breach is instructed. Mitigation held: transcripts were read by subagents, and the main loop read only the anchor in full plus 3 targeted passages.

### Housekeeping observed but NOT touched (Rule 3 — surgical changes)

`raw/_inventory.md`'s "Coverage summary" footer carries **pre-existing contradictory counters** — e.g. two different "Uncompiled / raw (awaiting compile)" bullets (one says 2, one says 1) and a "Total ingestions logged: 41 rows" line that no longer matches the table. I appended an accurate bullet for this run and **did not** rewrite the existing ones. Flagged for the operator rather than silently reconciled.

## Final metric

- **`gaps_closed_ratio` = 1.0**
- **Stop reason:** target_ratio reached on cycle 1
- **Duration:** 2026-08-19 16:34:15 → 17:01:43 ICT (**~27 min**)
- **Scorecard:** 43 source claims — 25 CONFIRMED / 13 CBI-or-imprecise / 2 stale-since-publication / 2 UNVERIFIED / 1 FALSE / **0 FABRICATED by the source**

## Suggested next action

**Fix the Sonnet 5 price wherever it lives before 2026-09-01** — his $2/$10 is introductory pricing that expires **2026-08-31, twelve days from now**; standard is $3/$15. Then, if you want the hireui payload cashed: write the Match-Explain acceptance criteria as a numbered quantifiable list *before* any prompt exists — per video 4, criteria are the durable asset and prompts depreciate, and that artifact doubles as the eval harness and the audit record the ratified ADR needs.
