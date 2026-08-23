# (C) Deep Dive — ZJU-LLMs/Foundations-of-LLMs 《大模型基础》

**Wiki v270 · 2026-08-24 · GOAL-ALIGNED INCLUDE 3/4 · NO MINT**

> Source verified: two independent clones, `diff -rq` clean outside `.git` internals.
> HEAD `1109bfa8e1c5b83fd25f66435601eef2a5905d5b`. Nothing installed, built, or executed.

---

## 1. What it is

`ZJU-LLMs/Foundations-of-LLMs` is **《大模型基础》** ("Foundations of Large Models"), a free Chinese-language LLM textbook from the **DAILY Lab** (Database and Big Data Analytics Laboratory) at **Zhejiang University**. The GitHub organisation describes itself as *"Share research achievements related to LLMs of Database and Big Data Analytics Laboratory (DAILY Lab), Zhejiang University."*

At **17.1k stars / 1.6k forks / 185 watchers** (page-stated; this environment mocks the GitHub API — §37.4, so these are page-scrapes, **not** Pattern #52 velocity claims), it is one of the most-starred Chinese-language LLM educational resources on GitHub.

The repository holds four things:

| Artifact | Form | Size |
|---|---|---|
| The textbook | 6 chapter PDFs + 1 complete PDF (290 pp.) | 22.2 MB complete |
| English edition | 1 PDF (368 pp.) | 45.8 MB |
| Paper list | 1 markdown file, 202 entries | 72,367 B |
| arXiv weekly reports | 60 markdown files in 12 week-directories | ~350 KB |

**Licence: CC BY-NC-ND 4.0** — Attribution-NonCommercial-**NoDerivatives**.

### Ground truth (all counts via `git rev-list --count`, never `git log | wc`)

```
HEAD              1109bfa8e1c5b83fd25f66435601eef2a5905d5b
commits (main)    86          commits (all refs)   93
roots             1 (a365a32, 2024-06-30, "create", wenyi <wenyisir@gmail.com>)
merges            4           tags                 0
author emails     12          author names         11
distinct humans   7 (+1 org bot)                   tracked files  75
remote branches   main, readme (0 ahead), readme_fix (7 ahead, 32 behind)
span              2024-06-30 → 2025-12-12          NOT a fork
```

### Authorship

The **book** credits ten people; the **repository** contains commits from about seven. The PDF front matter states the division of labour verbatim:

> 本书作者分工情况如下：第一章作者为：毛玉仁、高云君；第二章作者为：李佳晖、毛玉仁、宓禹；第三章作者为：张超、毛玉仁、胡中豪；第四章作者为：葛宇航、毛玉仁；第五章作者为：宓禹、樊怡江、毛玉仁；第六章作者为：董雪梅、徐文溢、毛玉仁。高云君为本书编撰总指导。

**毛玉仁 (Mao Yuren) is an author on all six chapters**; **高云君 (Gao Yunjun)** is editorial director. Funded by NSFC grants **62025206, U23A20296, 62302436**.

Only **one** commit author uses an institutional address — `a11en0 <yuhangge@zju.edu.cn>`, 9 commits. The contact address printed in the README (`xuwenyi@zju.edu.cn`) belongs to someone who commits from QQ Mail.

**AI provenance: zero.** Across all 93 commits on all three refs: `Co-Authored-By` 0, `claude` 0, `gpt` 0, `generated with` 0, 🤖 0. ⭐ Yet the English edition's own readme says the entire book was translated **by GPT**. **AI authorship is disclosed in the prose and invisible in the version control** — the exact inverse of v269 (1,068 trailers, no `CLAUDE.md`) and v243 (905 trailers nobody asked for).

---

## 2. The measurement that organises everything

The README makes a maintenance promise. It has been possible to check it for twenty months.

> 作者团队将认真听取开源社区以及广大专家学者的建议，**持续进行月度更新**
> *"The author team will carefully heed the suggestions of the open-source community and experts, and carry out **continuous monthly updates**."*

Measured against the actual content history:

| Artifact | Last content change | Commits touching it | Age at 2026-08-24 |
|---|---|---|---|
| 6 chapter PDFs | **2024-08-14** | **1 each** | 24.3 months |
| Paper list | **2024-08-14** | 2 | 24.3 months |
| English PDF | 2024-11-29 | 1 | 20.9 months |
| **Complete book PDF** | **2024-12-04** | 2 | **20.7 months** |
| Weekly reports | 2025-01-14 | 14 | 19.4 months |
| README | 2025-12-12 | 36 | 8.4 months |

**Commits per month, whole repository:**

```
2024-06  19  ###################
2024-07  37  #####################################
2024-08   9  #########
2024-09   0
2024-10   4  ####
2024-11  10  ##########
2024-12   3  ###
2025-01   1  #
2025-02 … 2025-11   0   ← eleven consecutive months, zero commits
2025-12   3  ###
```

⭐⭐⭐ **The three commits in December 2025 — the only activity in the repository's final eleven months — do not touch the book.** They are:

```
2025-12-08 20:45  Update README with Agent-Kernel announcement
2025-12-08 20:48  Revise README with updated project information
2025-12-12 09:55  Revise news section in README for Agent-Kernel
```

Someone returned after **328 days** of silence, edited the README three times to get an **advertisement for a different project** right, and did not touch the monthly-update sentence sitting fifteen lines below it.

**The sentence has never been edited.** It is present, unchanged, in every one of the **17 README revisions** that contain it, from 2024-07-25 to 2025-12-12.

**The version badge has had exactly one value in its entire life** — `https://img.shields.io/badge/version-1.0.0-blue`, from 2024-07-31 to today. ⭐ Decoding the three camo'd badge URLs in a live browser shows the other two are `shields.io/github/stars/…` and `…/forks/…` — **dynamic endpoints that update themselves. The one badge that needs a human is the one frozen at 1.0.0.**

---

## 3. ⭐⭐⭐⭐⭐ The gratitude list

At `readme.md:107-116`:

```
 107: ## 致谢
 108:
 109: 本书的不断优化，将仰仗各位读者的帮助与支持。您的建议将成为我们持续向前的动力！
 110:
 111: 所有提出issue的人，我们都列举在此，以表达我们深深的谢意。
 112:
 113:
 114:
 115:
 116: 如果有此书相关的其他问题，请随时联系我们，可发送邮件至：xuwenyi@zju.edu.cn。
```

Line 111 reads: *"**Everyone who has raised an issue, we list them all here, to express our deep gratitude.**"*

Lines 112–115 are **four blank lines**.

I scanned every revision of `readme.md` in the repository's history. The sentence first appears **2024-07-25 22:49**. In all **17 revisions** containing it, the count of non-blank lines between it and the contact line is **zero**. **The list has never held a single name.**

Meanwhile, on the live repository: **53 open issues + 9 closed = 62 issues raised.**

And they are not noise. They are precisely the contribution the README asked for (「如有谬误，恳请大家多提issue」 — *"if there are errors, please raise issues"*):

| # | Date | Report |
|---|---|---|
| **68** | **2026-07-21** | Ch3 §3.3 summary typo: the second 按部就班 should be 三思后行 |
| 67 | 2026-01-13 | "My reading notes are being updated" |
| 65 | 2025-12-15 | 「公式 1.21 错误」 — Formula 1.21 is wrong |
| 63 | 2025-08-16 | 「继续更新」 — *keep updating* |
| 62 | 2025-07-05 | Request for DeepSeek content |
| 61 | 2025-06-24 | Ch5 Figure 5.11, patcher position looks wrong |
| 60 | 2025-06-11 | §1.4 sampling methods, typo |
| 59 | 2025-05-21 | T-Patcher loss-function description problem |
| 58 | 2025-04-30 | `ZJU-LLMs/DAgent` returns **404** |
| 55 | 2025-04-10 | 「内容更正，20页，73页，165页」 — corrections at pages 20, 73, 165 |

⭐ **Issue #65 was filed three days after the maintainers' last commit.** They were in the repository on 12 December 2025. A formula error was reported on the 15th. Nothing since.

⭐ **Issue #58 is still open after 16 months, and I confirmed it: `ZJU-LLMs/DAgent` does not exist.** The organisation's five public repos are Foundations-of-LLMs (17.1k), Agent-Kernel (467), OpenStory (383), Awesome-LoRAs (278), Machine-Learning-Paradiagms (7 — *"Paradiagms"* is misspelled in the repository name itself). The pattern is: link to a repo → the repo disappears → someone files an issue → the issue stays open → the link stays broken. **The current README's top banner is a link to the next repo in that sequence.**

### ⭐⭐⭐⭐⭐ I verified the newest errata report against the shipped PDF

Issue #68, filed by YYGCui on **2026-07-21 — one month ago** — claims that in §3.3's closing summary the second 按部就班 should read 三思后行.

The three chain-of-thought modes taught in §3.3 are **3.3.2 按部就班** (step by step), **3.3.3 三思后行** (think thrice), **3.3.4 集思广益** (pool ideas). Extracting the chapter PDF, the closing summary reads verbatim:

> CoT 方法包含了多种模式：**按部就班、按部就班**以及集思广益。
> *"CoT methods include several modes: **step-by-step, step-by-step**, and pool-ideas."*

**The reader is right.** The summary lists mode one twice and omits mode two. The error is still in the PDF, the issue is still open, and the reporter's name is not in the gratitude list — because the gratitude list has never had a name in it.

And **they cannot fix it themselves.** There is no LaTeX source in the repository, CC BY-NC-**ND** forbids sharing a corrected version, and the artifact is a compiled binary. 1,600 people have forked a book that nobody is licensed or technically equipped to amend.

> ⚠️ **NOT ESTABLISHED:** I attempted to verify issue #65 (Formula 1.21). `pdftotext` mangles the equation layout into unordered fragments. **I will not claim a formula is right or wrong from garbled output.** Unverified, not refuted.

---

## 4. The freshness claim is welded into the artifact

`pdfinfo` reports both PDFs were built with **`LaTeX with hyperref` / `xdvipdfmx`**, template **ElegantBook**. So a LaTeX source exists. **It is not published.**

Inside the 290-page compiled book, the string 「本书持续更新」 (*"this book is continuously updated"*) appears **nine times** — once in each chapter's front-matter block:

> \* 本书持续更新，GIT Hub 链接为：https://github.com/ZJU-LLMs/Foundations-of-LLMs。

Counting both artifacts, the project asserts ongoing maintenance **eleven times**: twice in the README (monthly updates; the paper list "currently being continuously updated") and nine times inside the PDF.

⭐⭐⭐ **And the book states its own age zero times.** No changelog, no 第一版, no `v1.0`, no year string anywhere in 551,065 extracted characters. The only date is in the PDF metadata, which a reader would need a tool to inspect.

⭐⭐⭐⭐ **The README could be fixed in seconds — and was edited three times in December 2025, none of them to fix it. The nine copies inside the PDF cannot be fixed by anyone outside the lab, because the source is withheld and the licence forbids derivatives.**

---

## 5. Three link-text fossils, and the honest version of the two-copies problem

The README contains exactly **two markdown headings** (`## 本书目录`, `## 致谢`); its table of contents is an HTML table. Its three prose links all resolve correctly — and **all three name their target by a name the target does not have:**

| Anchor text | Actual target |
|---|---|
| 大模型基础.pdf | `大模型基础 完整版.pdf` |
| 大语言模型分章节内容 | `《大模型基础》分章节内容` |
| **大语言模型相关论文** | `大模型经典论文列表` |

The third is a fossil with a measurable lifespan. On **2024-08-14**, in 143 minutes:

```
12:10  0989cc0  LJHzju  adds 大语言模型相关论文/ with 6 per-chapter readmes + 7 .DS_Store
12:17  bfb17d1  LJHzju  deletes the 7 .DS_Store files
14:06  12e5ed4  wenyi   R100 renames all six → 大模型经典论文列表/
14:33  d923503  wenyi   deletes all six, adds one flat 987-line readme.md
```

**The directory named in the anchor text existed for one hour fifty-six minutes.** Two years later the link text still says it.

> ⚠️ **A correction to my own first reading.** I initially took the six deleted files as work abandoned on the unmerged `readme_fix` branch. Checking `--name-status` instead of the truncated diffstat shows they were **on main** and were **deliberately flattened**. And checking the flat file's contents shows its internal structure has **six `##` chapter sections whose `###` subsections match the book exactly** — so the README's promise of *"a Paper List for each chapter's content"* is **satisfied in substance**. Only the file layout changed. My near-miss claim would have been an overstatement.

**Similarly on the two PDF copies.** The six chapter PDFs are frozen at 2024-08-14; the complete PDF was rebuilt 2024-12-04 — built from source revisions 3.7 months apart. I was going to write that nothing declares which wins. **A refuter caught me, and it was right:** `readme.md:23` says 「**当前**完整的本书PDF版本路径为…」 — *"the **current** complete PDF version is at…"*. Precedence **is** declared for the whole.

The narrower finding that survives: precedence is declared for the whole and **withheld for the parts**. The next clause offers the chapter folder flatly — *"contains the PDF versions of each chapter"* — with no hint that those files are 3.7 months older. Page counts: 31+63+54+33+43+55 = **279**, complete = **290**. This is v245's **D32** unmet on one side: *declare which copy wins, inside the copy that loses.*

---

## 6. The English edition

`Foundations_of_LLMs(English_version)/readme.md`, in its entirety:

> This book is the English version of the chinese book 《大语言模型基础》。Now, It is stiil a draft version, which is directly translated from the chinese version by using GPT. We will refine the English writting of this book later. **It will be coming soon!**

Written **2024-11-29**. "Coming soon" has stood for **20.9 months**. (Two typos — *stiil*, *writting* — in four sentences, and the title it gives the Chinese book, 《大语言模型基础》, **is not the Chinese book's title**, which is 《大模型基础》.)

I measured the translation myself:

```
English PDF   368 pages   638,066 extracted chars   53,748 CJK chars
Chinese PDF   290 pages   551,065 extracted chars  429,841 CJK chars
lines containing CJK in the ENGLISH pdf: 3,570 of 14,130  = 25.3%
```

⭐ **One line in four of the "English version" still contains Chinese** — 53,748 characters, 12.5% of the original Chinese text, concentrated in figures (Figure 2.3 Encoder-only, Figure 2.15 RLHF, the Chapter 3 Zero-Shot CoT examples) and worked examples. It is not a translation with gaps; it is a hybrid. It is also the largest file in the repository at 45.8 MB.

---

## 7. What the book actually contains — and it is good

This section matters for fairness. **The artifacts are genuinely good. It is the claims about them that fail.**

**Structure** (290 pp.): Ch1 語言模型基础 (31 pp.) · Ch2 大语言模型架构 (63 pp.) · Ch3 Prompt 工程 (54 pp.) · Ch4 参数高效微调 (33 pp.) · Ch5 模型编辑 (43 pp.) · Ch6 检索增强生成 (55 pp.). Every chapter's printed section list **matches the README table exactly** — checked chapter by chapter.

**The animal conceit is real and carried through:** Ch1 giraffe (长颈鹿) in the n-gram corpus and sampling walkthroughs · Ch2 capybara (水豚) in the in-context-learning contrasts · Ch3 raccoon (小浣熊干脆面, a Chinese snack) in the CoT arithmetic examples · Ch5 zebra in the model-editing error example.

**Ch1** teaches n-grams → RNN → Transformer, then sampling (greedy, beam, Top-K, Top-P, temperature) and evaluation (Perplexity, BLEU, ROUGE, BERTScore, G-EVAL) with derivations. **Ch2** frames three eras, derives scaling laws (Kaplan; Chinchilla `L(N,D) = E + A/N^α + B/D^β`), then Encoder-only / Encoder-Decoder / Decoder-only / non-Transformer (Mamba, RWKV). No factual error was identified with certainty in either chapter; GPT-3 175B, the June-2020 date, and the Chinchilla presentation all check out.

**Ch3 (Prompt engineering)** is the most goal-relevant chapter: 3.1 definitions and tokenisation · 3.2 in-context learning (demonstration selection, performance factors) · 3.3 CoT (按部就班 / 三思后行 / 集思广益, incl. Self-Consistency) · 3.4 practical technique · **3.5 applications: 3.5.1 LLM-based Agent · 3.5.2 data synthesis · 3.5.3 Text-to-SQL · 3.5.4 GPTS.** Term counts: `Agent` 32, `Text-to-SQL` 18. ⭐ **A database lab wrote an LLM textbook, and you can see the database lab in which applications it chose.**

**Ch4 (PEFT)**: additive (input/model/output) · selective (rule-based/learned) · low-rank (LoRA, variants, LoRA-plugin generalisation) · practice. Counts: `LoRA` 109, `Adapter` 29, `Prefix` 15, `BitFit` 7, `DoRA` 6, `AdaLoRA` 4. 🔴 **`QLoRA` 0, `量化` 0, `4-bit` 0, `int4` 0** — a PEFT chapter with 109 LoRA mentions and **no quantised fine-tuning at all**, which is the single most-used PEFT configuration on consumer hardware.

**Ch5 (Model editing)**: T-Patcher and ROME, conceptual and mathematical, **no code examples**, only 2 citations from 2024.

**Ch6 (RAG)** is the strongest practical chapter: four architectures (black-box no-tune / black-box retriever-tune / white-box LLM-tune / white-box co-tune), knowledge retrieval, generation augmentation, **reranking via cross-encoder and RankGPT sliding-window**, an **agentic-RAG section** (memory/planning/action, citing Lei Wang et al. 2024), and a **complete runnable LangChain pipeline** — WebBaseLoader → VectorStoreRetriever → ChatOpenAI + LCEL. ⚠️ It does **not** cover hybrid sparse-dense retrieval or the long-context-vs-RAG trade-off.

### What it says about Claude

Across 551,065 extracted characters:

```
Claude 1     Anthropic 0     MCP 0     ReAct 0     "tool use" 0
"function call" 0     AutoGPT 0     多智能体 0     test-time 0
LLaMA 123    GPT-3 57    GPT-4 46    ChatGPT 35    o1 2
CoT 90       思维链 22    Agent 58    智能体 7
```

**The single Claude mention is the string "Claude 3" as a label in Figure 2.1**, a diagram of emergent-capability stages. That is the whole of it.

The paper list stops the same way: 202 entries, years peaking at 2023 (50) and 2024 (32), **zero from 2025 or 2026** — under the heading 「以跟踪相关技术的**最新进展**」 (*"to track the latest progress"*) and the status 「当前正处于不断更新中」 (*"currently being continuously updated"*), unchanged for 24.3 months.

⭐ Credit where it is due: the paper list is **fair work**. 202 entries, 201 with a working `[PDF]` link (99.5%), 121 with `[Code]` (59.9%), 45% arXiv / 46% peer-reviewed venues, structure matching the book's chapters exactly — and **self-citation of only 7 entries in 203 (3.4%)**, which is modest for an academic reading list.

---

## 8. ⭐⭐⭐ The goal-relevant content is in the part the README never mentions

The `Arxiv 一周进展报告（大模型方向）` directory holds **60 markdown files in 12 week-directories** — 80% of the repository's tracked file count.

**The README mentions it zero times.** Greps for `Arxiv`, `arxiv`, `进展报告`, `一周`, `周报` against `readme.md` all return 0. The README has two headings and neither is this.

The reports are substantive:

```
60 files    59 cite an arXiv URL (98%)    58 use the jsdelivr CDN for figures
55 share an identical section ordering    45 carry an editor credit
12 are about agents or tool use (20%)
```

They ran **2024-10-04 → 2025-01-09** — 12 of the 14 weeks in that span; **20241122-20241128 and 20241129-20241205 are missing**. Then they stopped.

⭐ **They are republished WeChat articles.** 45 of the 60 end with 「查看 Arxiv 原文请点击"**阅读原文**"」 — *"to read the original arXiv paper click **Read Original**"* — where 阅读原文 is a **WeChat UI button that does not exist on GitHub**. The content was pasted across without adapting the instruction to the new surface.

And the best of them is about the operator's exact subject. `20241115-20241121/一键自动化：Claude 3.5与GUI Agent的破晓时刻.md` summarises *The Dawn of GUI Agent: A Preliminary Case Study with Claude 3.5 Computer Use* (Hu, Ouyang, Gao — **Show Lab, NUS**, arXiv:2411.10323), and it is accurate: system prompt, screenshot-only observation (*"不依赖于元数据或HTML"*), observe-then-act, **the three Anthropic-defined tools (computer / text-editor / bash)**, full mouse-keyboard action space, history visual context, and the PE/AE/CE error taxonomy. Editors credited: 宓禹、毛玉仁 — the same people who wrote Chapters 2 and 5.

⭐⭐⭐ **So: the 290-page book that the README does document mentions Claude once, in a figure label. The 60-file directory the README does not document contains a full, correct technical briefing on Claude Computer Use. The repository's index points away from its most goal-relevant content** — v240's inventory rule from a third direction: index→content resolves for every link, and content→index fails for the largest directory in the repo.

---

## 9. The pivot

The banner now at the top of the README:

> ✨ News: 我们开源了一款多智能体开发框架Agent-Kernel，让大家轻松玩转大规模多智能体系统！**一百个智能体在自己的笔记本电脑上就能跑起来哦~** 科研、毕设、大创、SRTP都是让人眼前一亮的创新神器！

`ZJU-LLMs/Agent-Kernel` is real: **467 stars, Apache-2.0, Python, 53 commits**, described as *"A MicroKernel Multi-Agents System Framework for Adaptive Social Simulation Powered by LLMs."* It is a **social-simulation** framework, not a coding-agent framework.

⭐ **The claim that "a hundred agents run on your own laptop" is not substantiated on Agent-Kernel's own page** — no benchmark, no quantitative scale statement; its README says *"unlimited scalability of agents"* and nothing measurable. **The number exists only in the advertisement, on the other repository's README, where nothing can check it.** The ship's rule, one more time, at the smallest scale in the repo.

---

## 10. ⭐⭐⭐⭐⭐ The ship's rule

Every defect above is the same kind of statement.

> 「持续进行月度更新」 — we will do monthly updates
> 「当前正处于不断更新中」 — the paper list is continuously updating
> 「所有提出issue的人，我们都列举在此」 — we list everyone who filed an issue
> 「后续，作者团队还将继续探索…大模型智能体」 — later we will add agents
> 「It will be coming soon!」 — the English edition will be refined
> 「本书持续更新」 ×9, inside the PDF
> `version-1.0.0`

**Not one of these was false when it was written.** Every one of them was an honest statement of intent on the day it was typed. Each became false later, by the passage of time, while nobody was looking — because the last time anybody looked, it was true.

⇒ **A promise about the future is the only class of claim that cannot be wrong at write time. That is exactly why no gate catches it.** A wrong count is wrong immediately. A dangling link is dangling immediately. A missing list entry is missing immediately. A commitment is *correct* immediately, and rots on a clock that no CI job is watching.

This completes a four-ship arc:

| | The rule |
|---|---|
| **v267** Obscura | The discipline stops where the artifact stops being code. |
| **v268** hermes-desktop | A gate exists where a reader can refuse — and agents don't refuse. |
| **v269** OpenViking | Coverage rots by omission; no gate can see an entry that was never added. |
| **v270** Foundations-of-LLMs | **No gate can fire on a claim that was true when it was written.** |

**And the only defence is a date.** Had the sentence read *"monthly updates, as of July 2024,"* a reader in 2026 would evaluate it in one second. It doesn't. This book asserts its own freshness **eleven times** and states its own age **zero times** — v255's *"date your work"* rule, broken as completely as it can be broken.

---

## 11. Mint decision — **NO MINT**

**Governing precedent, verified verbatim in `_state/03c-projects-v61-v183.md`:** v197 mlsysbook — *"a single-domain educational curriculum is not a recurring capability class; §C vocab is tool/capability-shaped"* (line 2490); v191 AI-For-Beginners and v220 little-book-rl the same, under *"corpus-first for a DOMAIN is not mintable — domain-not-capability is DECISIVE."*

This is a domain textbook. **NO MINT.** Also not world-first: 动手学深度学习 (d2l), corpus **v74** LLMs-from-scratch, and Datawhale's materials (corpus **v77** easy-vibe, **v111** hello-agents) all precede it as open LLM educational books.

**Corpus-first check:** `ZJU-LLMs`, `Foundations-of-LLMs`, 《大模型基础》, `Mao Yuren` and `Wenyi Xu` have **never appeared in the 269-entry corpus** (grep-verified; the only `ZJU`/`Zhejiang` hits are v269's paper-authorship note and v111 Datawhale, both different subjects). It **is** the corpus's first Chinese-university-lab-authored LLM textbook — a corpus-first for a **domain**, which the rule above says is not mintable.

**Counts UNCHANGED: 46 top-level patterns / 12 CONFIRMED Library-vocab; §C-1 12; §C-2 39.** **§28 is a supporting ground only (§44.5)** and is not load-bearing here.

**Two deferred watch axes REGISTERED, not self-executed** (a mint is an audit act):

1. **"University-lab open textbook distributed as a compiled PDF only, LaTeX source withheld, under a NoDerivatives licence"** — N=1. A genuinely distinctive *publishing posture*, and the sharp contrast with the corpus's other textbooks (v197 mlsysbook published its Quarto source; v74 published every notebook). Posture, not capability → recorded.
2. **"Lab research digest republished from a WeChat public account into a git repository"** — N=1. A form-factor within Pattern #68 (awesome-list genre); the v201 awesome-llm-apps precedent says form-factor sub-variants do not mint → recorded and declined.

**Instance-strengthening recorded:** the **informal** T3 Education tier (established v74 for Educational-Book-Companion subjects; ⚠️ *informal* — the v203 audit has it "HOLD informal", formalisation deferred, and C04/C05 were retired at v151) · Pattern #68 (the paper list) · #19 19a (author org NOT Anthropic).

**NON-CLAIMS:** NOT a fork · **NOT Pattern #52** (§37.4 — star counts are page-stated, not velocity-verified) · NOT a new top-level pattern (46 unchanged, max #85) · nothing installed, built, or executed.

---

## 12. Method — corrections and environment findings

**Five corrections, all caught before publication.** Four were mine.

1. ⚠️ **The `}` in a git diffstat is rename-compaction syntax, not a filename.** I nearly wrote that a branch contained directories literally named `第1章 语言模型基础}`. `git ls-tree` showed clean names.
2. ⚠️ **The per-chapter paper list was not abandoned on a branch — it was on main and deliberately flattened**, and its content survives with chapter sections intact, so the README's per-chapter promise is *satisfied in substance*. I inferred abandonment from a truncated diffstat. `--name-status` corrected it.
3. ⚠️ **WebFetch reported the README's cover image and QR code as broken. They render.** A browser gives `naturalWidth: 1786` and `naturalWidth: 2023`. The Windows backslash paths (`.\figure\cover.png`) survive because the WHATWG URL parser normalises `\` to `/` for http(s) schemes — the browser's `resolved` src is `…/raw/main/figure/cover.png`. ⭐ **A markdown-converting tool asserted a visual fact it structurally cannot observe.** Do not take rendering claims from a text extractor.
4. ⚠️ **"Nothing declares which PDF copy is current" — refuted by a fleet refuter, correctly.** `readme.md:23` says 「当前完整的本书PDF版本路径为…」. The surviving finding is narrower: precedence declared for the whole, withheld for the parts.
5. ⚠️ **A fleet refuter claimed `git log --all` is capped at 50 in this environment. I ran that exact command three times and got 93 each time.** Fabricated. **D51 at N=3.**

### ⭐⭐⭐ The `git log` cap: a recorded corpus rule, narrowed again

- **v267** observed 50 commits and a false root on one repository, and attributed it to *"the date-ordered walk terminating early under commit-date skew."*
- **v269** observed 50 on two repositories, **refuted the skew mechanism** (`-n 3000` lifted the cap; skew never would), and concluded **"a `git log`-specific max-count of 50 in this environment."**
- **v270: the cap does not reproduce at all.** On git 2.19.0, this repository:

```
rev-list --count HEAD          86     log --oneline | wc              86
rev-list --all --count         93     log --all --oneline | wc        93
                                      log --all --oneline -n 500      93
three consecutive runs of log --all: 93, 93, 93
```

⇒ **v269's "in this environment" is too strong.** The cap is repo- or session-conditional, not environment-wide. What survives — and survives for a *structural* reason, which is why it is the half worth keeping — is the operational rule: **`git rev-list --count` emits one line, so there is nothing to truncate, and it is correct whichever mechanism is or is not active.**

⭐⭐⭐ **And note what the vault did here.** v269 generalised from two observations to a claim about every future repository. It was true of everything it had seen and became false on the very next subject — measured today, in the session that diagnosed this exact failure mode in someone else. **The vault made the same move ZJU made, in the same breath as naming it.**

### Two more environment facts, both already in the vault's own memory and both re-confirmed

- **`python3` is SIGKILLed in this sandbox** (exit 137, every invocation, heredoc or file). Use `awk`/`sed`/`grep` only. This is the v236 finding, still true.
- The shell mangles multibyte strings inside nested command substitution — write a script to `/tmp` and `bash` it.

### ⚠️ A counting error worth recording: `wc -w` on Chinese

The fleet's finder said the Claude Computer Use report contains "1,242 words"; its refuter said "117 words" and refuted on that basis. **Both numbers are meaningless.** Chinese does not delimit words with spaces, so `wc -w` counts whitespace-separated runs. The file is **5,079 bytes / ~1,700 Chinese characters** and is a substantial technical summary. The refuter's *substantive* point — that it quotes no evaluation metrics — is correct; I read the file and confirmed it. But **this is v242's D23 at N=2: declare the language basis of a count.**

### Fleet

12 dimensions dispatched, **9 returned; 3 died on the schema nudge** (`ch3-4`, `readme-claim-audit`, `currency-2026`). **45 agents, 5,237,698 subagent tokens, 897 tool uses, 7.4 minutes.** Two of the three dead dimensions I had already covered by hand; `ch3-4` I had not, and I covered it myself afterwards — §7's chapter-3 and chapter-4 analysis, the QLoRA gap, and the issue-#68 verification are all hand-work, not fleet output.

---

## 13. NOT ESTABLISHED

- Whether Formula 1.21 (issue #65) is actually wrong — `pdftotext` destroys the equation layout.
- Whether issues #55, #59, #60, #61 are correct — not individually verified against the PDFs.
- Whether the 9 closed issues were closed as fixed or as stale.
- Whether the LaTeX source exists privately, or whether the team intends to release it.
- Whether the English PDF's untranslated regions are the same in every chapter (measured in aggregate only).
- Star/fork/watcher counts are **page-stated**, not API-verified (§37.4).
- Whether 「张超」/「Chao Zhang」 in the paper list is the book's chapter-3 author or a different researcher of the same name — excluded from the self-citation count for that reason.
- Anything about the DAILY Lab's internal reasons for stopping. **The evidence shows what happened, not why.**

---

## 14. Fairness

This is a good book. Ten credited authors, NSFC funding, 290 careful pages, a genuine pedagogical device carried through six chapters, an honest 202-entry reading list with 3.4% self-citation, a runnable RAG pipeline, and 60 substantive paper summaries with a 98% arXiv-citation rate. It is free. 17,100 people starred it and they were not wrong to.

**The failure is not the artifact. It is the eleven statements about the artifact's future, none of which was false when written, all of which are false now, and none of which anything was ever going to check.**
