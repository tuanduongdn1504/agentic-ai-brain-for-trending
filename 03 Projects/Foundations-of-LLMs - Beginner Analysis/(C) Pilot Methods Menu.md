# (C) Pilot Methods Menu — v270 Foundations-of-LLMs

**2026-08-24 · verdict: READ-AND-BORROW · nothing to install · CC BY-NC-ND binding**

There is no software in this subject. The ladder below is reading, one hireui input, and — the highest-value rung — **the vault's own exposure to exactly the defect this ship diagnosed, already measured.**

---

## Rung 0 — Read the seven things worth reading (35 min)

Open `《大模型基础》教材/大模型基础 完整版.pdf` (290 pp.) and read only:

1. **§3.5.1 基于大语言模型的 Agent** — the four-component agent framework, the only agent architecture in the book.
2. **§3.3 思维链** — 按部就班 / 三思后行 / 集思广益 + Self-Consistency. ⭐ Then read its closing summary and see the error yourself: 「按部就班、按部就班以及集思广益」.
3. **§3.4 Prompt 技巧** — the four practical rules, the most directly reusable pages in the book.
4. **Ch6 §6.2** — the four RAG architectures (black-box no-tune / black-box retriever-tune / white-box LLM-tune / white-box co-tune). The cleanest taxonomy of the four I have read.
5. **Ch6 §6.3.5** — reranking: cross-encoder and RankGPT sliding-window.
6. **Ch6's LangChain pipeline** — WebBaseLoader → VectorStoreRetriever → ChatOpenAI + LCEL, end to end.
7. **`Arxiv 一周进展报告（大模型方向）/20241115-20241121/一键自动化：Claude 3.5与GUI Agent的破晓时刻.md`** — the correct Claude Computer Use briefing that the README never tells you exists.

⚠️ **Skip Ch4's PEFT chapter for practical purposes.** 109 mentions of LoRA and **zero** of QLoRA, quantisation, 4-bit or int4 — the configuration you would actually use.

---

## ⭐⭐⭐ Rung 1 — Turn the finding on the vault (45 min, already measured)

This ship's rule is *no gate can fire on a claim that was true when it was written.* The vault runs on such claims. **Here is its exposure, measured today:**

```
CLAUDE.md forward-looking commitments
  DEFERRED / deferred        22
  watch axis                  4
  eligible@N=                 3
  STILL pending               1
  Carried forward             1
                        ──────
                             31
  already self-flagged OVERDUE / PAST DUE: 8
  forward-commitment lines carrying an ISO date: 2 of 4
```

⭐ **And the vault has ZJU's link-text fossil, worse:**

```
_state/03c-projects-v61-v183.md
  name says          : v183
  highest entry held : v269      (86 ships past the name)
  size               : 2,779,918 bytes
  files citing it by the stale name: 31
```

ZJU has **one** stale anchor naming a directory that lived 116 minutes. The vault has **thirty-one** references to a filename that has been wrong for 86 ships. v245 already applied the cheap **D32** mitigation — a source-of-truth notice *inside the losing copy* — which is precisely the mitigation ZJU never applied to its two PDF copies. **The vault is one step ahead on the fix and identical on the defect.**

**Do this, in order:**

1. **Add a date to every forward commitment.** Not a fix — a *stamp*. `DEFERRED` becomes `DEFERRED (2026-08-24)`. Thirty-one edits, mechanical. This is the entire defence: a reader in 2027 can evaluate a dated promise in one second and cannot evaluate an undated one at all.
2. **Rename `03c` and sweep the 31 references** — the fix declared at v239/v240/v242, given a pattern at v243, an instance at v244, and a cheap mitigation at v245. It is the vault's own 「大语言模型相关论文」.
3. ⭐⭐ **Make something invoke the nine-clause script.** `03 Projects/HeadFirstAndroid - Beginner Analysis/(C) proposed-verify-vault-inventory.sh` was written at v255, re-asserted at v256, found un-invoked at v263, and asked for again in v269's Rung 2. **It is still in a project folder, still named "proposed", still invoked by nothing.** It is the vault's own 「持续进行月度更新」 — an honest intention that has now been true-when-written for five ships.

---

## ⭐⭐ Rung 2 — Add the one check this ship implies (30 min)

v269's rule needed a *list-omission* check. v270's needs a **staleness** check, and it is cheaper than it sounds because it needs no judgement:

> **Every forward-looking commitment must carry the date it was made. A commitment older than N ships is surfaced, not deleted.**

Add as clause 10 of the inventory script:

- grep `CLAUDE.md` for the commitment vocabulary (`DEFERRED`, `watch axis`, `eligible@N=`, `STILL pending`, `carried forward`, `OVERDUE`);
- **FAIL** any hit with no ISO date on the same line;
- **WARN** any dated hit older than 20 ships.

Follow v240's decay doctrine exactly: **flag, never remove · skip the inconclusive · evidence not doubt · removal is human.** The script must surface, not prune.

⭐ The check that would have caught ZJU is the same one: *does every maintenance claim carry the date it was made?* Eleven claims, zero dates, twenty months.

---

## ⭐⭐ Rung 3 — Ch6 into hireui (90 min)

hireui has **no LLM integration yet**, so this is a build-it-right input, not a retrofit.

- Take **§6.2's four-architecture taxonomy** and write the one-paragraph decision into hireui's LLM ADR: for CV↔job matching you want **black-box, no-tuning, retrieval-only** — no fine-tuning of anything, which composes with the **RATIFIED candidate-LLM legibility ADR** (fixed, legible, audited, human-in-loop, eval-gated).
- Take **§6.3.5's reranking split** — cheap dense retrieval, then a cross-encoder rerank on the top-k — as the shape for Match-Explain. It is the right shape and it is cheap.
- ⚠️ **The chapter's gaps are your risks:** no hybrid sparse-dense (you will want BM25 alongside embeddings for exact skill-token matches), and no long-context-vs-RAG trade-off (at hireui's per-candidate document sizes, long-context may beat RAG outright — the book cannot help you decide).
- 🔴 **Do not** copy its LangChain pipeline into hireui. Read it for the stage decomposition; the licence forbids redistributing the text, and the vendor-seam discipline (AIRI v210, lobehub v222) says do not bind to LangChain.

---

## ⭐ Rung 4 — The paper list as a bounded reading queue (20 min to triage)

`大模型经典论文列表/readme.md` — 202 entries, 201 with working PDF links, 121 with code, chapter-organised, 3.4% self-citation. It is a **good** list.

⚠️ **It stops in July 2024. Zero entries from 2025 or 2026.** Use it as a *foundations* queue — the pre-2024 canon it covers well — and never as a "latest progress" list, which is what it claims to be. Pull §Prompt 工程 and §检索增强生成 and read the code-linked entries only.

---

## ⭐ Rung 5 — Steal the digest format, not the digest (30 min)

The 60 weekly reports share a real template: one-line summary → 研究内容 → 研究动机 → 技术动机 → 解决方案 → 实验结果, with the arXiv link (98% of them) and named editors (45 of 60).

That is a better shape than most paper notes, and it is worth copying for the vault's own source intake. ⭐ **But copy the template and take the warning with it**: these were WeChat articles pasted into git, and **45 of 60 still end with 「阅读原文」 — "click Read Original" — a WeChat button that does not exist on GitHub.** *An artifact carries instructions that only make sense on the surface it came from.* When you lift a format across a boundary, strip the instructions that belonged to the old surface.

---

## 🔴 Never

- **Do not redistribute the book**, modified or unmodified, in anything commercial. **CC BY-NC-ND**, and the ND clause says verbatim: *"You do not have permission under this Public License to Share Adapted Material."* 1,600 forks do not change that.
- **Do not put its figures, tables, or prose into hireui material** — that is the commercial clause, directly.
- **Do not cite its currency.** No content since 2024-12-04; the paper list since 2024-08-14; the digests since 2025-01-14.
- **Do not trust the "English version"** for anything. **53,748 Chinese characters remain in it; 25.3% of its lines contain Chinese.** It is a hybrid, not a translation, and it has said "coming soon" for 20.9 months.
- **Do not rely on Ch4 for practical PEFT** — no quantisation at all.
- **Do not treat the 17.1k stars as a currency signal.** They measure how good the book was in 2024.
