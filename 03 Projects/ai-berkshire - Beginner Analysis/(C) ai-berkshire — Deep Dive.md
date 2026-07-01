# (C) ai-berkshire — Deep Dive (v187)

> **Wiki ship v187 · 2026-07-01 · operator-requested** ("build LLM wiki from `xbtlin/ai-berkshire` + double deep dive into the original resource for knowledge + show many methods to apply to my working flow").
>
> Source-verified against a fresh clone at commit **`0222260`** (last commit 2026-07-01). Repo metadata (page-stated, NOT API-verified per §37.4): **7.7k★ / 973 forks / 1 release (v1.0.0, 2026-04-07) / MIT / Python 97.2% + Shell 1.8% + Mermaid 1.0%**. Author **`xbtlin`** — a bare handle (an individual Chinese value-investor/creator; the repo carries WeChat-article drafts + a live-trading folder).

---

## 0. One-paragraph summary

**AI Berkshire** is a **domain-vertical agent-skill collection for value-investing research**, built for **Claude Code *and* Codex**. Its pitch: *"One person + Claude Code / Codex = an entire investment research team."* It systematizes the methodologies of **four investing masters — Warren Buffett, Charlie Munger, Duan Yongping (段永平), and Li Lu (李录)** — into **18 installable skills**, **8 Python tools**, and a documented **3-layer (Skill / Agent / Tool) architecture**. The headline mechanic is a **4-persona parallel multi-agent research team** where each agent analyses a company from a different master's lens and a *team-lead* synthesizes — deliberately engineered to produce **dialectical tension** ("Buffett says *genuinely cheap*, Li Lu says *if uncertain, don't buy*") rather than one both-sides-hedging answer.

**Two distinct bodies of knowledge live here, and they matter differently to you:**
- **The agent-engineering knowledge** (Part B below) — how to build a specialized, disciplined, multi-agent skill team with Claude Code. This is **dead-center on your Goal #1** and directly portable to software / the vault / hireui.
- **The value-investing knowledge** (Part C — the "original resource" you asked me to deep-dive) — the four masters, the Kelly formula, moats, the mirror test, concentration. **Off-goal for "software development," personally useful, and a template for building a skill collection in *your own* domain (recruitment).**

---

## Part A — What it actually is (the system)

### A.1 The 3-layer architecture (its own framing)

| Layer | What it holds | Concrete artifacts |
|---|---|---|
| **Skill layer** | "What you want to do," abstracted into 18 entry points by scenario | `skills/*.md` (Claude Code slash-commands), e.g. `/investment-team`, `/investment-checklist`, `/quality-screen` |
| **Agent layer** | Each skill fans out N agents that search + judge + challenge each other; a team-lead synthesizes | `TeamCreate` / `TaskCreate` / `Task(run_in_background:true)` inside the skill files |
| **Tool layer** | Exact-precision math + web search + report auditing so every number is verifiable | `tools/*.py` (zero-dependency Python stdlib) |

### A.2 The 18 skills, grouped

- **Deep research (5):** `/investment-research` (7-module single-company deep dive) · `/investment-team` (4 parallel agents — flagship) · `/management-deep-dive` · `/private-company-research` (7-agent "detective mode" for info-scarce private cos like SpaceX/Ant) · `/deep-company-series` (8-part, ~120K-word publication series).
- **Earnings (2):** `/earnings-review` (primary-source-only filing read — "like Buffett reads annual reports") · `/earnings-team` (4 masters → editor → reader-review → publish-ready).
- **Industry screening (5):** `/industry-research` (value-chain scan) · `/industry-funnel` (full market → ≤10 → 3 deep, chosen for *portfolio complementarity* not top-3 score) · `/quality-screen` (7 hard metrics) · `/bottleneck-hunter` (supertrend → physical supply-chain bottleneck) · `/investment-checklist` (6-gate 10-minute go/deep-dive).
- **Portfolio (3):** `/portfolio-review` (sizing/concentration/rebalancing) · `/thesis-tracker` (post-buy discipline — is the thesis falsified?) · `/news-pulse` (10-min price-move attribution, 4-dimension parallel recon).
- **Thinking tools (3):** `/dyp-ask` (think through anything "the Duan Yongping way") · `/financial-data` (2-source cross-validation, >1% deviation alert) · `/wechat-article` (author → editor → reader agents → publishable article).

### A.3 Repo footprint

- ~**100+ real research reports** in `reports/` (dated 2026-04-08 → 2026-06-30) — company deep-dives (by-company folders w/ 4 persona files + final report), industry funnels, screening pools (`筛选公司/` A-share + STAR-market recall pools), comparison studies, WeChat articles, and "mirror-test" (镜子测试) live records in `实盘记录/`.
- **8 Python tools:** `financial_rigor.py` (exact-decimal valuation + Benford), `report_audit.py` (exit-gate), `stock_screener.py` (momentum+value 2-layer), `morningstar_fair_value.py` (fair-value scraper), `momentum_backtest.py`/`_v2.py` (framework backtest vs NVDA/AMD/MU), `ashare_data.py` (A-share quotes/financials via Tencent/Eastmoney APIs), `xueqiu_scraper.py` (Playwright Xueqiu scraper).
- **Dual routing artifacts:** `CLAUDE.md` (Claude Code behavior + report naming conventions) · `AGENTS.md` (Codex behavior + compatibility rules) · `ai_CLAUDE.md` (a hand-maintained **session-memory file** — user persona, history, corrections; an L2/L3 memory artifact).

---

## Part B — The AGENT-ENGINEERING knowledge (on-goal; the transferable part)

This is the part that matters to *your* mastery of Claude + autonomous agents. Six patterns worth stealing:

### B.1 Persona-differentiated parallel multi-agent orchestration

`/investment-team` is a concrete, readable implementation of the multi-agent pattern you've been researching:

1. Show the team framework to the user, get confirmation.
2. Run an **"AI-researchability" pre-assessment** (A/B/C information-richness rating) that *changes each agent's strategy* (A-level → focus on the non-consensus/inversion; C-level → first-principles mode, don't fake completeness).
3. `TeamCreate` → 4 `TaskCreate` tasks (business/financials/industry/risk).
4. **Launch 4 `general-purpose` subagents in ONE message, `run_in_background:true`** — each carries a *persona prompt* ("you are the {master} lens") + a detailed task + a **mandatory 2-independent-source data rule**.
5. Agents report back via `SendMessage` to the team-lead (message-passing, not file collaboration).
6. Team-lead **synthesizes + resolves disagreements**, produces a structured verdict, then runs the **exit-gate audit**.

The design insight, stated plainly in the skill: the 4 agents get **the same data but different lenses** — so divergence reflects *analytical perspective, not information asymmetry*. That is the correct way to think about persona subagents. (Honest caveat: it is not a true adversarial *debate* — it's 4 parallel instructions synthesized by a 5th; the "four masters arguing" is framing.)

### B.2 Deterministic-tool-offload for tasks the LLM is unreliable at

`financial_rigor.py` exists because **"LLMs can't do mental math reliably. Getting a P/E wrong by one decimal or confusing HKD with CNY can lead to catastrophic decisions."** So the arithmetic is handed to deterministic Python (`decimal.Decimal`, `prec=28`, `ROUND_HALF_EVEN`) as a **mandatory gate the skill must call via Bash** — market-cap verification (price × shares vs reported, >5% = warning), valuation ratios, multi-source cross-validation, three-scenario target prices, a Benford's-Law first-digit anomaly check, and an exact calculator. **This is the single most portable idea in the repo:** identify what the model is bad at (precision, arithmetic, unit consistency), and make it call code instead of guessing.

### B.3 A verification / exit gate before "publish"

`report_audit.py` is a **3-step publish gate**: (1) `extract` parses the finished report and pulls a **15% random sample** (min 3, max 30) of its numeric claims into a checklist; (2) the agent re-fetches each from a reliable source (macrotrends/stockanalysis US · aastocks HK · eastmoney A-share) and fills a JSON; (3) `verdict` computes percent-diff at a **1% tolerance** and emits **PASS (publishable) / FAIL (reject + exact offending lines)**, with a non-zero exit code for CI. This is the productized form of *your own* `feedback_wiki_verify_independently_check_collisions` rule and Addy Osmani's *doubt-driven-development* (v184) — evidence-gated, adversarial, before-ship.

### B.4 Cross-harness skill distribution from one canonical source (#84 84c)

`skills/*.md` is the **single source of truth**. `scripts/sync-codex-skills.py` **generates** `codex-skills/*/SKILL.md` (auto-adds `name`/`description` frontmatter + prepends a *"Codex adapter note"* mapping Claude-Code primitives → Codex equivalents), and `sync-codex-prompts.py` generates optional Codex slash-prompts. `install-claude-commands.sh` copies `skills/*.md` → `~/.claude/commands/`; `install-codex-skills.sh` regenerates + copies → `~/.codex/skills/`. A `--check` mode verifies generated artifacts are current without rewriting. **Rule enforced:** never hand-edit generated files; change the source and regenerate. This is clean provider-agnostic distribution.

### B.5 Forced-verdict / anti-fence-sitting discipline

The whole system exists to defeat the "on one hand… on the other hand… DYOR" non-answer. Every skill forces **Pass / Fail / Gray Zone** with **specific price ranges and tiered recommendations** (aggressive / moderate / conservative). The **"mirror test"** is the gate: *if you can't articulate the thesis in 5 sentences, don't buy.* The engineering lesson: **build the required output shape into the skill** (scorecards, verdict tables, decision memos) so the model can't wriggle out with hedging.

### B.6 Structured anti-bias mechanisms

Baked into `CLAUDE.md`'s "highest-priority principles" and every skill: **objectivity over opinion** (banned phrases: "I think", "obviously"; required: "data shows", "per source X"), **fact-vs-opinion separation**, **present both sides**, **honest "I don't know" over speculation**, the **A/B/C information-richness rating** (resource-abundance ≠ certainty), **Munger inversion** ("how could this die?"), a **quick-kill checklist** (any red line = veto), and a **contrarian check** ("why are smart people shorting this?").

---

## Part C — The VALUE-INVESTING knowledge (the "original resource," deep-dived)

You asked to double-deep-dive the original resource. Here is the crystallized philosophy the repo encodes — verified against upstream sources, with the retail-lore overstatements flagged.

### C.1 The four masters

**Warren Buffett** — *circle of competence* (only invest in what you genuinely understand), *economic moat* (durable competitive advantage), *margin of safety* (buy well below intrinsic value — Graham's "three most important words"), *owner earnings* (1986 letter: earnings + D&A − maintenance capex), *intrinsic value via DCF*, *Mr. Market* (the market serves you, doesn't instruct you), and the Munger-driven shift from Graham "cigar-butts" to **"a wonderful company at a fair price."** Signature: *"Price is what you pay; value is what you get."*

**Charlie Munger** — *inversion* ("invert, always invert"), a *latticework of mental models* from many disciplines, the *Psychology of Human Misjudgment* (~25 cognitive biases + the **Lollapalooza effect** when they stack), **concentration over diversification** ("diversification is a rule for those who don't know anything"; he personally held ~3 positions), quality over cheapness, "sit on your ass" investing.

**Duan Yongping (段永平)** — Chinese entrepreneur (Xiaobawang → BBK/步步高, backer of OPPO/vivo; mentor to Pinduoduo's Colin Huang/黄峥 and NetEase's William Ding/丁磊); won the **2006 Buffett charity lunch ($620,100, under the handle "fastisslow")**. Philosophy: **本分 (benfen)** = do the right thing / integrity; **"买股票就是买公司"** (buying a stock is buying a business, = buying its discounted future cash flow, full stop); the **stop-doing list (不为清单)** — **No margin** (never borrow), no shorting, don't invest in what you don't understand, don't over-trade, don't predict macro or prices; **毛估估** (rough estimation beats false precision); **平常心** (equanimous mind); **封仓十年** (if you won't hold it 10 years, don't hold it 10 seconds). Real wins: NetEase (~$1 → 100×+), Apple (~$13.75, 14-yr hold, ~18×), Moutai.

**Li Lu (李录)** — founder of **Himalaya Capital**; the man who brought **BYD** to Munger; **Munger's protégé** (Munger invested ~$88M with him). Framework: **civilizational trends / modernization** (his book *Civilization, Modernization, Value Investing & China*; "Civilization 3.0 = market economy + scientific breakthroughs"), **10-year certainty** ("will it still exist and thrive in 10 years?"), deep concentration, strict margin of safety, three sell rules (bought wrong / fundamentals changed / found something better). ⚠️ **Honesty flag:** his long-run alpha is *overstated in Chinese retail circles* — the publicly disclosed Munger investment (~$88M → ~$400M over ~15 yrs ≈ 10–11% CAGR) roughly matched the S&P over the same window; **BYD was the genuine home-run**, not a steady 30% machine.

### C.2 The Kelly formula — the math of survival (`公众号-凯利公式`)

The repo's most rigorous quant piece. Binary form: **f\* = (b·p − q) / b** (fraction to bet; b = payoff odds, p = win prob, q = 1−p). Continuous/stock form used loosely: **f = (E[R] − Rf) / σ²**. The counter-intuitive core:

| Bet size | Long-run growth | Volatility |
|---|---|---|
| Half-Kelly (0.5×) | ~75% of max | ~50% |
| Full Kelly (1.0×) | 100% (theoretical max) | 100% (brutal drawdowns) |
| 1.5× Kelly | ~75% of max | 150% (**same growth as half-Kelly, 3× the pain**) |
| 2× Kelly | **zero** | 200%+ |
| >2× Kelly | **negative → certain ruin** | extreme |

**Loss asymmetry** (why survival dominates): −50% needs +100% to recover; −75% needs +300%; −90% needs +900% — investing is multiplicative, not additive. **Three operational rules:** no information advantage → position = 0; even with an edge use **only half-Kelly** (your parameter estimates are wrong — Rotando & Thorp: half-Kelly ~90% avoids ruin vs full-Kelly's ~50%); **never exceed 2× Kelly**. Duan's plain-English version: *"If you understand it, volatility is small → concentrate; if you don't, volatility is large → diversify or don't touch it."* ⚠️ The continuous-Kelly stock formula is theoretically loose (Thorp's 19-yr record is the empirical warrant, not a clean derivation).

### C.3 Concentration — "少即是多" (Liu Junning)

The lens principle: **concentrated capital + deep focus = a focal point** (heat), scattered capital = scattered returns. **优存优汰 vs 劣存优汰** — concentrated investors trim losers and keep winners (superior survives); diversified investors sell winners early (+30%) and hold losers (inferior survives → backwards wealth destruction). But concentration only works if you understand the business, know why competitors can't replicate it, and bought with a margin of safety — else diversify or avoid. Fisher: *buying a company you don't understand can be more dangerous than under-diversifying.*

### C.4 The moat — the filtering principle

Five buckets: **brand/pricing-power** (Moutai, Apple) · **switching costs** (Microsoft, Shopify) · **network effects** (Tencent, Visa) · **scale/cost** (Amazon, Costco) · **tech/patents** (Nvidia, Broadcom). **The test:** *"If I gave a competitor $10B, could they replicate this in 5 years?"* → yes = moat too narrow. **Trajectory matters:** widening > stable > narrowing > eroding.

### C.5 The three decision-discipline mechanisms

- **The mirror test (镜子测试)** — a 5-part audit you must complete in one clear sentence each: (1) I understand the business's cash machine; (2) its moat is X and widening/stable; (3) management is trustworthy because Y; (4) price = Z% of fair value (margin sufficient); (5) if wrong, downside is controllable because W. **Can't fill all 5 → don't buy.** Kills FOMO.
- **The 6-gate checklist** (`/investment-checklist`) — Circle of competence → Good business (ROE >15%, GM >40%, FCF≈NI, light assets, net-debt/NI <3) → Moat → Management (integrity = hard veto) → Margin of safety (three-scenario valuation; price must be <70% of base case, ideally <50%) → Emotional discipline. Red vetoes at gates 1 & 4.
- **The thesis tracker** (`/thesis-tracker`) — post-buy quarterly discipline. Build a ≤200-word thesis + 3–7 verifiable assumptions + severity-tiered red lines (🔴 fatal → exit / ⚠️ serious → 50% cut / 🟡 warning → investigate). Each quarter, score each assumption (🟢 intact / 🟡 decaying / 🔴 damaged / ⚫ broken) → **thesis-health score** = 10 − (broken×3 + damaged×2 + weakened×1 + redline×5) → decision (add/hold/reduce/exit). Duan's sell rules: only sell if you bought wrong, fundamentals changed, or found something better.

### C.6 The 7-metric quality screen (`/quality-screen`)

Brutal exclusion (eliminate if): 10-yr avg ROE <8% · 5-yr cumulative FCF negative · interest coverage <2× · long-term GM <15% · OCF/NI (5-yr) <0.7 · long-term net margin <5% · 5-yr non-M&A dilution >20%. Plus three **exemption rules** for reinvesting-phase companies (Meituan/Amazon-type) and thin-margin-high-turn models (Costco-type). Goal: *don't kill any first-tier company, but exclude the definitely-not-first-tier* — inversion applied to screening.

### C.7 The "AI five-layer cake" (bonus — a genuinely useful field map)

A synthesis of Jensen Huang's five-layer AI-industry pyramid, mapped to concrete picks per layer, ranked by *certainty*: **① Energy** (most underrated bottleneck — transformer lead times 2–5 yrs; Eaton, GE Vernova, Constellation, NuScale, 特变电工) → **② Chips** (most value-dense — Nvidia, Broadcom, AMD, TSMC, SK Hynix) → **③ Infrastructure** ($725B hyperscaler capex — Arista, Vertiv, 中际旭创, Dell, CoreWeave) → **④ Models** (fastest revenue growth, most unpriced — Anthropic, OpenAI, Google, Meta, DeepSeek) → **⑤ Applications** (real AI earners rare, bubble risk highest — Palantir, Salesforce, ServiceNow, Tesla, Adobe). The recurring insight, echoing 1995–2000: *the biggest application-layer winners are incumbents with distribution/data/workflow, not AI-native startups.*

---

## Part D — Honest caveats (read before you act on any of it)

1. **The +69.29% (2024) / +66.38% (2025 YTD) / ¥1.46M returns are UNVERIFIED marketing.** No trade logs / P&L are in the repo; the evidence is brokerage screenshots. The repo's own `ai_CLAUDE.md` (line 64) admits *"README中的输出示例是虚构的"* — **the README's sample outputs are illustrative/fictional.** Treat the performance claims as unproven (like page-stated star counts — §37.4). **This is not investment advice; the repo says so (DYOR).**
2. **"Four masters arguing" is framing, not true adversarial debate** — it's four parallel persona-instructions on the same data synthesized by a fifth.
3. **The reports are time-bound** (2026-04 → 06 stock picks/valuations); the *frameworks* are durable, the *picks* are not.
4. **Li Lu's long-run alpha is overstated in retail lore** (see C.1).
5. **Supply-chain / operational notes** (see the Verdict): pure-Python stdlib tools (safe), but the README recommends `claude --dangerously-skip-permissions` (a real footgun), `financial_rigor.py`'s `calc` uses `eval()` behind a char-allowlist (minor), and `xueqiu_scraper.py` is a Playwright scraper of a Chinese finance site (ToS/dual-use). Install scripts copy skills into `~/.claude/commands/` and `~/.codex/skills/`.

---

## Where this sits in the corpus

- **NOT corpus-first for finance/investing agent tooling** — `anthropics/financial-services` (**v141**, Anthropic-official reference agents for IB/equity-research/PE/wealth-mgmt) precedes it in the finance domain.
- **A clean instance of the CONFIRMED T1 Domain-Vertical-Skill-Collection sub-archetype** (SEO v64 / academic-research v90 / cybersecurity v98 / … → **value-investing** is the next vertical).
- **Cross-refs:** multi-persona subagent library (agency-agents **v185**), 4-review-personas + doubt-driven-dev (agent-skills **v184**), skill-collection genre (karpathy v63 / mattpocock v57 / CodexKit v121 / claude-seo v64), your live **multi-agent-orchestration** + **CC-memory-systems** pilot threads.

See the **Verdict** doc for the routine bookkeeping and the **Pilot Methods Menu** for how to apply all of this.
