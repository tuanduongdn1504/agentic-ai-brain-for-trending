# (C) Deep Dive — HiThink-Tech/Financial-API (v271)

**Subject:** `https://github.com/HiThink-Tech/Financial-API`
**Brand:** 同花顺金融数据服务 (hithink finance) · service host `fuyao.aicubes.cn`
**Ship:** v271 · 2026-08-24 · GOAL-ALIGNED INCLUDE 3/4 · **NO NEW MINT** (C16 N=1 → N=2)

---

## 0. Source verification

Two independent clones, `diff -rq` clean in **both** directions.

| Fact | Value | How |
|---|---|---|
| HEAD | `9dbef74d2ce535857e610eec265bcb9302942d48` | `git rev-parse HEAD` |
| Commits | **21** | `git rev-list --count HEAD` (= `--all`) |
| Roots | **1** — `0615769`, 2026-06-15 | `git rev-list --max-parents=0` |
| Merges | **0** | `git rev-list --count --merges` |
| Tags | **6** — `v0.1.0` … `v0.1.5` | `git tag` |
| Author identities | **1** — `HiThink-Tech`, **email literally empty (`<none>`)** | `git cat-file -p` on raw author lines |
| Tracked files | **402** | `git ls-files` |
| Size | 11 MB (4.5 MB `.git`) | `du -sh` |
| Licence | MIT © 2026 HiThink-Tech — **but see §7** | `LICENSE` |

**v270's counting rule applied:** `git log --oneline | wc -l` and `git rev-list --count` **agree at 21** here. The 50-commit cap seen at v267/v269 did **not** reproduce — consistent with v270's narrowing that the cap is repo- or session-conditional, not environment-wide. `rev-list --count` remains preferred because it emits one line and cannot be truncated.

**Method constraints:** `python3` is blocked in this sandbox (permission denied), so the repo's own Python gate could not be *executed* — it was **hand-simulated instead** (§1). `wc -w` is meaningless on CJK; all text counts below state their basis (bytes or files).

---

## 1. What it is

A **vendor-official, multi-surface agent access layer for a hosted commercial A-share financial-data API.** One API key reaches the same data through **five parallel surfaces**:

| Surface | Delivery |
|---|---|
| REST API | remote `fuyao.aicubes.cn/api/...`; contract documented in-repo at `docs/api/` |
| Hosted MCP | **four remote servers** (`a-share`, `a-share-index`, `meta`, `fund`) — documented, **not implemented** here |
| CLI | `@hithink-tech/hithink-finance-cli` (Node ≥22.12, 10,141 LOC TS) |
| Python SDK | `python/` — remote toolkit + local `marketdb` DuckDB layer (5,051 LOC) |
| Local DB | DuckDB built and incrementally synced from full-market Parquet dumps |

Fronted by **one unified Agent Skill** (`skills/hithink-finance/`) whose primary job is to **route between those five surfaces** based on what the environment offers.

**There is no MCP server source in this repository.** `docs/mcp/` documents a remote service. The CLI exposes no MCP server either — agents invoke it as a **subprocess**, and the *skill* is the integration mechanism. That distinction is the point of the subject.

---

## 2. The governance gate — and the answer to the ship's central question

`AGENTS.md` and `README.md` declare a documentation-governance regime: `docs/api/` is the single source of the upstream REST contract; `skills/hithink-finance/references/api*` and `mcp*` are **generated mirrors** that must not be hand-edited; the gate is `python scripts/sync_skill_contracts.py --check`.

### 2.1 The gate is real

`scripts/sync_skill_contracts.py` (137 lines) is a genuinely well-built checker:

- **Byte-exact** — `read_bytes() != read_bytes()`, not fuzzy (`:53`, `:75`, `:80`).
- **Both directions** — reports `missing` (source has, mirror lacks) **and** `unexpected` (mirror has, source lacks) (`:41-45`). This is the v240 inventory rule handled correctly: it can see an *extra* file.
- **Fails closed** — `return 1` on any problem (`:130`).
- **The `--check` path recomputes the generator's own transform.** `api_entry_content()` (`:33-43`) derives `references/api.md` from `docs/api/README.md` by stripping `llms-full`/`llms.txt` lines, rewriting 「本目录是」→「本 Skill 内置契约是」, and rewriting `(file.md)`→`(api/file.md)`. The check compares against that function's output, so **the check cannot drift from the generator, because it *is* the generator.**

### 2.2 I hand-simulated it at HEAD — all 17 pairs pass

| Pair set | Result |
|---|---|
| `docs/api/*.md` (11) → `references/api/` | **11/11 byte-identical** |
| reverse (orphan mirrors) | **0** |
| `docs/mcp.md` → `references/mcp.md` | **identical** |
| `docs/mcp/*.md` (5) → `references/mcp/` | **5/5 identical** |
| reverse | **0** |
| `docs/api/README.md` → `references/api.md` (transform) | **diff = exactly the 3 documented transformations, nothing else** |

**The declared discipline is satisfied.** After four consecutive ships (v267–v270) documenting declared-but-unenforced rules, this one holds.

### 2.3 It is wired — twice

`.github/workflows/hithink-finance-python-ci.yml:36` runs `--check` on pull_request and push. And `python/tests/test_public_docs_governance.py:120-127` **also** runs it as a subprocess and asserts `returncode == 0` — belt, braces, and a third belt (the test *additionally* byte-compares all 11 files itself).

### 2.4 THE FINDING: the gate's trigger cannot see the documents it tests

`test_public_docs_governance.py` (215 lines) is the most comprehensive documentation-enforcement suite in the corpus. Nine tests:

| Test | Asserts |
|---|---|
| `..._brand_positioning_and_quick_start` | root README starts with the brand H1; all 4 access modes present; all 4 MCP server names present; ⭐ **`readme.index("npm install -g …") < readme.index("cd hithink-finance-cli")`** — the recommended path must appear *before* the from-source path |
| `..._changelog_preserves_history` | five specific ISO release dates still present — **a test that history is not rewritten** |
| `..._skills_are_consolidated` | `skills/` is **exactly** `{hithink-finance}`; `references/*.md` is **exactly** `{api,cli,mcp,python-sdk}.md`; subdirs **exactly** those four; 「渐进」or「按需」 present (the progressive-disclosure language) |
| `..._one_canonical_source_and_skill_mirror` | 11 files byte-identical + set equality both ways + runs the sync gate |
| `..._temporary_special_data_..._not_public` | internal endpoint paths (`/api/a-share/special-data/temporary-`) appear in **no** public markdown — **a leak-prevention test** |
| `..._obsolete_llms_..._legacy_skill_names_absent` | no `llms.txt` copies; four **legacy skill names** absent everywhere — **a test that a rename was completed**; and `llms-full` present in docs but **absent from the skill** (so the skill stays self-contained) |
| `..._python_docs_..._not_duplicate_upstream_contracts` | `python/toolkit/fuyao/docs` does not exist; `## 响应字段` absent from the Python README |
| `..._one_cross_mode_api_key_contract` | `HITHINK_FINANCE_API_KEY` in 8 named entry docs; `${API_KEY}` absent from README |
| `..._relative_links_resolve` | **a full relative-link checker over every public `.md`**, correctly excluding image links `(?<!!)`, anchors, `://`, `mailto:`, `<>`, `%20` |

**Now the trigger.** The Python CI `paths:` filter is exactly:

```
python/**  ·  docs/api/**  ·  docs/mcp.md  ·  docs/mcp/**
skills/hithink-finance/**  ·  scripts/sync_skill_contracts.py  ·  (its own yml)
```

**`README.md` is not in it. Nor `AGENTS.md`, `CHANGELOG.md`, `docs/README.md`, `docs/monorepo-migration.md`, `examples/**`, or `hithink-finance-cli/**/*.md`.**

So the three tests whose entire subject is the root README, the CHANGELOG, and *every markdown file in the repository* **do not run when you change the root README, the CHANGELOG, or most markdown files.** A commit touching only `README.md` triggers **neither** workflow.

**Empirical check, stated honestly.** Commit `7df0473` ("调整README") is one file, `README.md` only, and triggers nothing — but it predates the Python CI (added `2b626da`, 2026-07-24), so it *illustrates* the shape rather than proving a missed run. Of the three commits landing after the Python CI existed, two (`bb0a376`, `f8cdea9`) correctly didn't need it and one (`9dbef74`) ran it. **In practice the snapshot cadence masks the hole** — bulk commits touch `python/**` anyway. This is a verified finding about **design**, not observed damage.

⭐ **The rule: a `paths:` filter is a build-cost optimisation. Here it silently became the scope of a correctness gate.** The gate's scope is inherited from *where it lives* (next to the Python code), not from *what it asserts* (the whole repository's documentation).

### 2.5 The counter-example: how the CLI skills got it right

`hithink-finance-cli/skills/` holds **10 skill packages / 84 files**. The Python gate never touches them (zero mentions of `hithink-finance-cli` in the script). They are protected by a different, **better** mechanism.

`tests/contract/generated-contracts.test.ts`:
1. runs `node scripts/generate-contracts.mjs <tmpdir>` — regenerating everything;
2. byte-compares **8** checked-in files against the fresh output (after line-ending normalisation);
3. one of those 8 is **`skills/manifest.json`** — which pins **all 84 files by sha256**.

I verified the manifest both directions: **84/84 files on disk pinned; 0 missing; 0 orphaned entries** (the raw key count is 86 = 84 + `protocolVersion` + `cliVersion`).

⭐ **So a single byte-comparison covers 84 files by construction.** Change any skill file without regenerating and the fresh `manifest.json` differs → CI fails. This runs via `vitest` → `test:built` → `npm run verify` → CI on **10 matrix combinations** (5 OS/arch × Node 22 and 24).

**This is precisely the fix v269's subject lacked.** There, a byte-check's hardcoded list covered 82 of 103 files because the generator and the test each hardcoded the same four config lists and they diverged. Here the test **delegates the list to a generated artifact** instead of restating it. Cross-organisation, independent, and it is the single best engineering idea in the repository.

Two more tests in that file deserve naming:
- it asserts `fund-news.md` contains `` `has_more=false` `` and does **not** contain 「返回条数小于 limit」 — **a regression test that one specific piece of *wrong pagination advice* cannot come back**;
- it splits on `## Shortcuts` and asserts newly-routed intents appear **before** that heading — a test about *agent discoverability ordering* inside a generated skill.

### 2.6 ⚠️ A fleet error, corrected

My 12-agent fleet raised as **critical** that the CLI skills "merge without drift verification," that `detectSkillDrift()` is "never invoked as a gate," and that "two drift mechanisms exist that do not communicate." **Its adversarial verifier confirmed all three.** All three are wrong.

`drift.ts`'s own docstring settles it: it detects whether **已安装的** (*installed*) skill files differ from canonical, for causes 「用户手动修改 / 文件损坏或部分写入 / 更新不完整」, and its parameter is 「已安装技能的目标根目录」 (*the installed skills' target root*). **It is a runtime integrity check for the user's copy.** In CI it would have nothing to compare against — the repo *is* canonical. Two different problems, two correct mechanisms.

Both agents were asked "is `detectSkillDrift` invoked?" — correct answer, no. The question that mattered was "are the CLI skill files protected by a CI gate?" — answer, yes, by a different mechanism they never opened. **D51 (fabricated/confident-wrong refutation) and v241's D21 (*a verifier checks the claim you hand it, not the question*) in one event.** Caught because I read the test directory rather than grepping for one symbol name.

---

## 3. Workspace or destination — answered from inside the repo

**16 of 21 commit messages are 「快照 YYYY.MM.DD.N」 (*snapshot*).** One author identity with an **empty email**. Zero merges, zero branches, zero PR/issue references, zero `Co-Authored-By`, **zero AI-authorship trailers**. Commit sizes are bulk: `45d49cd` = 317 files, `77d9469` = 115, `9dbef74` = 78. `.gitignore` excludes named, project-specific paths — `refer-to/`, `feature/`, `sdd-docs/*`, `.workbuddy` — **none ever tracked**.

⭐ **And the repository proves the hypothesis itself.** `python/tests/test_monorepo_layout.py:87-93`:

```python
skill_root = MONOREPO_ROOT / "internal" / "skills" / "export-snapshot"
if not skill_root.exists():
    pytest.skip("internal export policy is intentionally absent from public snapshots")
```

The remaining assertions describe the export machinery: `scripts/sync_snapshot.py`, `references/public-policy.yml`, `source: git-tracked-files`, `default: include`, `- sdd-docs/**`, and — pointedly — `assert "PUBLIC_INCLUDE" not in sync_script`.

Three things follow.

1. **The public repository is generated by an agent skill** (`internal/skills/export-snapshot`) in a private monorepo. The 21 commits are 21 exports.
2. **The export polarity is the safer one, and it is *tested*:** default-include with an exclude list, and an assertion that no `PUBLIC_INCLUDE` allowlist exists. An allowlist silently drops new files; a denylist ships them. Someone thought about this and wrote a test to keep it that way.
3. ⭐ **That test is the only conditional skip in the entire Python suite** (1 of 137 test functions; the TypeScript suite has **zero** `.skip`/`.todo`). **It ships everywhere and can only run where it is not needed.** In the public repository's CI it always skips.

**This corrects my own first reading.** I initially flagged `README.md:571` — 「`internal/` 和 `sdd-docs/` 属于内部治理与开发记录，不是公开使用入口」 — as a v265-style phantom citation, since neither directory has ever been tracked. **It is not.** It is an accurate disclosure of a real private structure, now documented by the skip-test. My fleet flagged it as "documentation drift" in four separate dimensions; every one got the fact right and the interpretation wrong.

⭐ **A new shape for the ladder:** v268 = a gate nothing invokes · v269 = a gate whose list is incomplete · v270 = a claim no gate can fire on · **v271 = a gate that travels with the artifact and is inert exactly where it lands.**

---

## 4. The agent surface — the most transferable material here

### 4.1 Two tiers, 11 skills, 327,920 bytes

| Tier | Content |
|---|---|
| `skills/hithink-finance/` | **1** unified router skill — `SKILL.md` 14,495 B + 4 first-level entries + 20 detail files = **154,555 B / 26 files** |
| `hithink-finance-cli/skills/` | **10** domain skill packages — **173,365 B / 85 files**, generated from code, sha256-pinned |

*(Correcting myself: 10 CLI packages, not 11 — 10 + the unified skill = 11 skills total.)*

### 4.2 The progressive-disclosure ladder, measured

`AGENTS.md` rule: 「只加载 Skill 选择的一个接入方式或端点组，不要递归读取全部契约」. `SKILL.md`: 「选定方式后只读取对应的一级入口，由该入口继续按需披露详细契约」.

| Read | Bytes |
|---|---|
| router only | **14,495** |
| router + one first-level entry | ~18,000 |
| everything | **154,555** |

⭐ **A 10.7× reduction, and it is enforced by a test** — `test_root_skills_are_consolidated` asserts the words 「渐进」/「按需」 are present. Weak enforcement (the vocabulary, not the behaviour), but it is more than prose.

### 4.3 ⭐⭐⭐ The negative routing clause — the single best technique to steal

**All 10 of 10** CLI skill descriptions end by naming where to go **instead**. Verified programmatically:

| Skill | The clause |
|---|---|
| financials | 「价格行情转 hithink-finance-market，指数财务**不在本 skill 范围**」 |
| fund | 「A 股行情转 …-market，基金代码搜索转 …-symbol」 |
| index | 「个股行情转 …-market，股票代码搜索转 …-symbol」 |
| market | 「涨跌停、炸板、热榜、龙虎榜、异动…转 …-special-data」 |
| special-data | 「普通行情转 …-market」 |
| symbol | 「行情价格转 …-market，指数成分转 …-index」 |
| valuation | 「历史估值、ROE 和投资建议**不在本 skill 范围**」 |
| data | 「远端实时数据转对应业务 skill」 |
| research | 「**不用于**实时取数、荐股、择时、组合建议或投资结论」 |
| shared | 「**不要用于**行情、财务、指数、特色数据或研究取数」 |

Ten descriptions that collectively form a **routing mesh where every node names its neighbours.** This attacks the hardest problem in any multi-skill collection — the model selecting the wrong skill because two descriptions overlap — and it does so in the one field the model always sees.

### 4.4 Instructions aimed at the agent, telling it to distrust documentation

The repository repeatedly instructs the agent to prefer **runtime truth** over prose:

- `hithink-finance-cli/README.md:70` — 「**Agent 不应只凭 README 猜参数。** 先读取 `capabilities`，再对目标 capability 读取 `schema`。」 (*The agent must not guess parameters from the README alone.*) ⭐ **This is v269's rule** — *"filenames, type names, and README claims alone do not establish runtime behavior"* — independently written, aimed at the agent, in a vendor CLI. **Cross-organisation N=2 in three ships.**
- `AGENTS.md:52` — 「**离线测试不能证明线上认证或实时服务可用；只有实际授权请求才能称为线上验证。**」 (*Offline tests cannot prove online auth or live service availability; only an actual authorized request counts as online verification.*) ⭐ **And this one is mechanised** — `hithink-finance-cli-live-canary.yml` makes three real authorized requests weekly and asserts `ok` and `meta.request_id` on each.
- `hithink-finance-cli/README.md:29` — 「如果 `npm install` 返回 `E404` … **报告实际状态，不要在终端指引中把源码安装伪装成正式发布安装。**」 (*Report the actual state; do not disguise a from-source install as an official release install.*)
- `python/toolkit/fuyao/README.md:144` — 「**不要从旧文档推断当前签名。**」
- The same clause, templated across ~40 skill reference files: 「参数校验失败时按 `error.hint` 修正，**不要猜字段名**。」

### 4.5 The anti-fabrication regime, and where it is placed

The rule 「不使用模拟数据或静态示例冒充真实结果」 appears at `README.md:88`, `:419`, `:440`, `:610`. But the *effective* placements are narrower and better:

- `docs/api/README.md:62` — error code **`3002` 数据尚未准备**: 「保留 `request_id` 与口径，稍后再查，**不得补零或使用模拟数据**」
- `docs/mcp/capability-map.md:58` — on `2003`/revoked key: 「**不要改用模拟数据**」
- `examples/inspirations/02-financial-health/README.md:20` — 「**`null` 保持缺失，不补零**；不要混淆单季值、累计值或不同报告期，也**不要编造估值、行业均值和评分**」

⭐ **The instruction is attached to the specific error condition that would tempt fabrication.** Not "be honest" in the abstract, but "when the API returns 3002, here is exactly what you must not do." For financial data 「`null` 保持缺失，不补零」 is load-bearing: a zero is a real value, a null is absence, and conflating them corrupts analysis silently.

---

## 5. The examples: a disclosure that stops at the file boundary

16 numbered "inspiration" dashboards, each with `README.md` + `example.html` + `preview.jpg`. **16/16 complete, no missing asset.** All static — **zero** make network calls; **zero** leak credentials.

Two *different* claims, measured separately:

| Claim, **inside the `example.html`** | Result |
|---|---|
| Investment-advice disclaimer (either wording) | **16 / 16** ✅ |
| **Simulated-data disclosure** | **8 / 16** — examples 09–16 only |

⚠️ **A correction I caught before publishing:** my first grep used only 「非投资建议」 and reported 8/16 for the advice disclaimer too. Examples 01–08 use a *different* wording — 「仅供信息展示，不构成投资建议」. Grepping one phrasing produced a false negative on half the corpus. The advice disclaimer is universal; only the *simulated-data* label is partial.

**The chronology is sharper than "forward only."** Commit `77d9469` (2026-07-17) **added examples 07–16 and simultaneously modified 01–06's `example.html`**. So within one commit, by one author, on one day: the simulated-data label went into 09–16 (8 new files), **not** into 07–08 (2 new files in the same commit), and **not** into 01–06 (6 files whose HTML was open and being edited). ⭐ **The improvement failed to travel sideways within a single change** — v259's copy-forward problem compressed into one commit.

**And the consequence is load-bearing.** `README.md:471` offers, for the example it bills as the 默认示例 (default showcase):

```
- [直接打开静态 HTML](examples/inspirations/01-stock-overview/example.html)
```

That link **bypasses the README that carries the label.** `01`'s HTML is 70,049 bytes of a titled 「同花顺行情工作台」 workbench with no indication its data is synthetic. The data *is* synthetic — **616 of its 1,880 decimal values (32.8%) carry a repeating-sevenths fingerprint** (`192.72142857142853`, `193.1285714285714`), and Chinese exchanges quote to two decimals. Detectable only by reading the digits.

⭐ **The honesty label is welded into the documentation and absent from the artifact — and the README hands you a link that skips the documentation.** The exact inverse of v270, where the *freshness* claim was welded into the artifact nine times and the age was absent.

**In fairness:** 16/16 example READMEs carry both labels, so the repository's own rule (「冒充」 = *pass off as*) is discharged wherever a reader arrives via the README. This is a boundary defect, not a dishonesty finding.

---

## 6. Two implementations of one on-disk format

The TypeScript CLI (`src/infrastructure/duckdb/*`, `migrations/001-initial.sql`) and Python `marketdb` (`sql/schema.sql`, `views.sql`) **both** init/sync/query/migrate a DuckDB database, using **identical table and view names** and **incompatible definitions**.

`raw_kline_daily`:

| TS | Python |
|---|---|
| `open/high/low/close/volume` **NOT NULL** | same names, **nullable** |
| **`amount`** NOT NULL | **`turnover`** ← different name, same concept |
| **`batch_id`** | **`source_batch_id`** ← different name |
| **`prev_close`** | — |
| — | **`currency`, `interval`, `adjusted`** |
| 10 columns | 12 columns |

`raw_adjustment_events` — the table feeding the adjustment calculation:

| TS | Python |
|---|---|
| **`rights_ratio`** | **`allotment_ratio`** |
| **`rights_price`** | **`allotment_price`** |
| `batch_id` | `source_batch_id` |
| dividend/bonus **NOT NULL DEFAULT 0** | nullable |
| — | `ticker`, `currency` |

Also `stg_symbol` (TS) vs `stg_symbols` (Python); `_meta` gains `updated_at` only in Python. **Six diverging column names in total.** All four view names (`v_symbol`, `v_daily`, `v_daily_qfq`, `v_daily_hfq`) are **identical**, and `v_daily` selects different columns in each.

⭐ **Root cause is visible: 配股 renders into English as either "rights issue" or "allotment."** Two implementations were built from one Chinese specification and each chose independently. Nothing ever compared them — **no test in either suite reads both schemas.**

**Why collision is silent, not loud:** both use `CREATE TABLE IF NOT EXISTS` and `CREATE OR REPLACE VIEW`. The first tool's tables are silently accepted by the second; the second tool's views silently replace the first's. The DDL succeeds and reports nothing.

**The mitigating fact, which must lead the risk framing:** the **default paths differ.** TS uses `<platform dataDir>/market.duckdb` (`platform-paths.ts:164`); Python uses `./data/market.duckdb` (`config.py:48`). **The common case never collides.** You have to point them at one path — which `.env.example` (`MARKETDB_DB_PATH=./data/market.duckdb`) and every README `marketdb` example do use — and the README presents both as ways to manage "the local database" without saying they are different databases.

**And the elegant part:** the TS side has a *real* migration system — `_meta.schema_version` + `schema_checksum`, `SUPPORTED_SCHEMA_VERSION`, and `migrations/manifest.json` pinning `001-initial.sql` by **sha256**. It verifies the integrity of its own schema with a cryptographic hash **and cannot see the other implementation of the same schema in the same repository.** v264's rule (*a discipline stops at the edge of the team that holds it*) — here the edge is the **language**.

### 6.1 The Python data layer is genuinely good

`calculations/adjustment.py` (125 lines) is the best code in the repository and the highest-stakes:

- The standard A-share ex-rights formula, stated in a header comment with every variable defined **and the net effect spelled out**: `ratio = ((1+s+r)·close_pre) / (close_pre − d + r·p)`, `hfq_close[t] = raw_close[t]·backward_factor[t]`, `qfq_close[last] = raw_close[last]`.
- **Ex-dates mapped to the next real trading day** — `MIN(k.date) WHERE k.date >= e.ex_date`. Frequently got wrong.
- `prev_close` via `LAG(close) OVER (PARTITION BY thscode ORDER BY date)` — previous *trading* day, from the actual series.
- **`EXP(SUM(LN(ratio)))`** for the cumulative product (DuckDB has no `PRODUCT()`), used twice — same-day event combination and the running product.
- **Log-domain guard** `WHERE ratio IS NOT NULL AND ratio > 0`; **divide-by-zero guard** `NULLIF(...)`.
- `forward_factor = backward_factor / LAST_VALUE(backward_factor)` — correct 前复权 normalisation.
- **`factor_version = '1.0'` stored per row**, so a future formula change is distinguishable in the data.
- Full recompute (`DELETE` then `INSERT`) — idempotent, no partial-state drift — with batch provenance (`record_batch_start/finish`, `set_meta('last_adjust_factor_batch_id')`).

⚠️ **A caveat I raised and then refuted myself.** I suspected the SQL assumes unadjusted input without checking the `adjusted` column. It doesn't need to: `importers/parquet.py:41-77` scopes every operation to `WHERE adjusted = 'none'`, with a comment saying why, and `test_adjustment.py` seeds `adjusted='none'`. The narrow residual: `adjustment.py` itself doesn't filter it, so **the guard lives at the writer, not the reader** — safe today because nothing writes a non-`'none'` row.

---

## 7. ⭐⭐⭐ The licence — MIT as far as the publication mechanism could see

| Declaration | Value |
|---|---|
| `LICENSE` (root) | **MIT** © 2026 HiThink-Tech |
| `hithink-finance-cli/LICENSE` | **MIT**, byte-identical |
| `package.json` | `"license": "MIT"` |
| `README.md` (final line) | 「本仓库采用 MIT License」 |
| **`python/pyproject.toml:11`** | **`license = { text = "Proprietary" }`** |
| SPDX headers in source | **0** |

**Chronology, verified commit by commit:**

- **2026-06-15** `b837e7b` (first code commit): `pyproject.toml` says **Proprietary**. **No `LICENSE` file exists anywhere.**
- **2026-07-10** `45d49cd`: `hithink-finance-cli/LICENSE` (MIT) arrives — the npm subpackage only. Root `pyproject.toml` moves to `python/`, carrying **Proprietary**.
- **2026-07-13** `05903e9` ("发布 hithink finance CLI 0.1.1"): root `LICENSE` (MIT) arrives — **28 days after the first commit, in an npm-publication commit.**

**Why:** `hithink-finance-cli/docs/maintainers/npm-publishing.md:1` — *"Obtain team approval for an open-source license and add `hithink-finance-cli/LICENSE`; **publishing is blocked until this exists**."* The MIT grant arrived **because publishing required it**, and it was applied at the two paths npm cares about. `pyproject.toml` was outside npm's field of view, so nothing prompted it.

**And the gate:** `scripts/check-license.mjs` is **ten lines**. It calls `access('../LICENSE')`. It never reads the file. It cannot see a licence contradiction, a wrong SPDX id, or a mismatch with `package.json`. Its error message says *"an **approved** LICENSE is required"* — but the doc's sentence had two clauses (*obtain team approval* **and** *add LICENSE*) and the script implements only the mechanical one. **The approval is the half a script cannot check, and the message claims it anyway.** It runs in `prepublishOnly`, the highest-stakes moment.

⚠️ **Pilot consequence:** `pip install -e ./python` builds a distribution whose declared licence is **Proprietary**. Any licence scanner over a dependency tree (pip-licenses, FOSSA, Snyk) reports Proprietary for `marketdb` — the 5,051-line half a researcher would actually vendor. This is v245's "Apache metadata over an AGPL wheel" inverted, and stronger than v269's licence-by-omission: it is an **affirmative contrary declaration**.

### 7.1 The data licence is entirely off-repository

Only **7 lines** in 402 files touch data rights, and the substantive ones say the same thing twice (`README.md:501`, `:612`):

> 「数据权限、调用频率和可访问 capability 以官网与账号授权为准。」 — *Data permissions, call frequency and accessible capabilities are governed by the website and account authorization.*

**Zero hits** for 商用 (commercial use), 转售 (resale), 再分发/redistribution, 服务条款/ToS. **There is no terms-of-service document in the repository**, and nothing states whether an API key is free, metered, or paid.

**State it plainly: MIT on the client says nothing about the data.** For any pilot that would put A-share data into a product, the binding term is an off-repository account agreement this repository does not reproduce.

### 7.2 One named human

**`python/pyproject.toml:12` — `authors = [{ name = "haoruilee" }]`.** The **only** named individual in 402 files; zero email addresses anywhere in the tree; all 21 commits are `HiThink-Tech <>`. The snapshot export leaked exactly one identity, through the same file that carries the contradictory licence.

---

## 8. ⭐⭐ Supply chain: all 206 dependencies resolve to a Chinese mirror

`npm-shrinkwrap.json` — which, unlike `package-lock.json`, **is always included in the published tarball and is authoritative for consumers**:

| Measure | Value |
|---|---|
| `resolved` entries | **206** |
| pointing at **`registry.npmmirror.com`** | **206** |
| pointing at `registry.npmjs.org` | **0** |
| carrying a `sha512` integrity hash | **206** |

**What this is not:** a code-substitution risk. All 206 have integrity hashes verified after download; a hostile mirror cannot serve different bytes.

**What it is:** every consumer of `@hithink-tech/hithink-finance-cli` inherits a lockfile directing all 206 dependency fetches to a third-party host in the PRC — a **privacy/observability** exposure (the mirror sees the installer's IP and complete dependency graph) and an **availability** coupling to a host the publisher doesn't control.

**Cause, visible in the repo:** `README.md` recommends 「国内用户可使用 npmmirror 镜像加速」 with `--registry=https://registry.npmmirror.com`. The maintainer installed with that registry configured; the lockfile recorded it; it was committed and published.

**Why nothing caught it:** CI runs `npm ci --ignore-scripts`, which happily *uses* the lockfile as written (fetching from npmmirror inside GitHub Actions) and passes. `npm pack --dry-run` passes. `tests/release/package-contents.test.ts` checks package *contents*, not registry *hosts*. `check-license.mjs` checks a filename. **Nothing in this repository looks at where its dependencies come from.**

⭐ This is the v260 §42 **workspace leak** at its purest — an artifact of *where the work was done*, published to everyone — in a repository whose commits are bulk exports from a private monorepo.

⚠️ **My fleet asserted the opposite** ("All network calls use HTTPS; no plaintext HTTP" — true but irrelevant) and never inspected `resolved` hosts.

### 8.1 The rest of the supply-chain posture is strong

**Genuinely good:**
- **All 5 direct deps and 206 locked packages exact-pinned** — no `^`, no `~`.
- API keys in the **OS keychain** via `@napi-rs/keyring`; `redact.ts` + `tests/security/secret-leak.test.ts`; `auth login --api-key-stdin` so a key never enters argv.
- `update-check.mjs` (23 lines): hits **only** `registry.npmjs.org`, 15 s timeout, cache written at **mode `0o600`**, **atomic temp+rename with the PID in the temp name**, and a swallowed catch **with a written rationale** (*"Update checks are advisory; failure is represented only in the cache."*). It records a version; it does not install.
- Three dedicated security test files: `injection`, `path-traversal`, `secret-leak`.
- Release: `npm publish --provenance`, Trusted Publisher, protected environment, tag↔version equality check, idempotent republish guard, and *"Never use a long-lived npm token."*
- `npm ci --ignore-scripts` **everywhere** in CI.

**Weaknesses:**
- **9 `uses:` clauses, 0 SHA-pinned** (`checkout@v4` ×4, `setup-node@v4` ×3, `setup-python@v5`, `upload-artifact@v4`).
- **2 of 4 workflows have no `permissions:` block** (`cli-ci`, `python-ci`) → repo-default token. The canary correctly sets `contents: read`; release sets `contents: write` + `id-token: write` (needed for provenance).
- **The postinstall writes 85 skill files into your global agent skills directory, and the word "postinstall" appears in *zero* markdown files.** `scripts/postinstall.mjs` detects a global install and runs the bundled `skills` CLI with `add … --global --copy --all --full-depth`. No prompt, no documented opt-out. ⭐ In the same 27 lines it **sets `DISABLE_TELEMETRY: '1'`** on that dependency and stays **non-fatal** on failure — it protects your privacy from a third party while writing to your home directory without telling you.

---

## 9. Code quality

| Area | LOC | Method |
|---|---|---|
| CLI `src/**/*.ts` | **10,141** | `find … -name '*.ts' \| xargs wc -l` |
| CLI `tests/**/*.ts` | **2,879** (45 files) | ratio **0.28** |
| `python/` marketdb+toolkit+tools | **5,051** | |
| `python/tests` | **3,156** (23 files) | ratio **0.62** |
| Test functions | **116** vitest (`^\s*(it\|test)\(`) + **137** pytest (`^def test_`) = **253** | |

**Strengths:**
- ⭐ **`vitest` include is `tests/**/*.test.ts` — all 7 subdirectories covered** (unit, integration, contract, e2e, performance, release, security). **No orphaned test directory**, unlike v264 where a whole language's tests never ran. `npm run verify` = `format:check && lint && typecheck && build && test:built`, on **10 matrix combinations**.
- **0 skipped tests** in the TS suite; **1** in Python (the structurally-necessary export skip).
- `retry.ts` — exponential backoff `min(1000·2^attempt, 8000)` with **±20% jitter and a written explanation of *why*** (thundering herd), worked delay examples, **both `Retry-After` formats** (seconds and HTTP-date), `random` and `sleep` **injected as parameters** for determinism, and `RETRYABLE_BUSINESS_CODES` as a named export with a per-code rationale.
- A uniform JSON **envelope** on every command (`ok`, `meta.request_id`, `error.code/category/hint`), schema **generated from code** and CI-verified fresh, `ErrorCategory` mapped to stable POSIX exit codes.
- `source-policy.ts` — the local-vs-remote decision is a **pure function**, not delegated to the model. ⭐ v263's rule (*routing is code, deciding is the model*) at N=2.
- **Bilingual CLI** (`zh-CN`, `en`) with a written rule at `i18n.ts:23` — *"when adding a new string you must add it in both branches"* — and `tests/e2e/help-locales.test.ts`.

**Weaknesses:**
- ⭐ **The architecture is declared in directory names and enforced nowhere.** `src/{application,domains,infrastructure,contracts,ports}` — there is even an `application/ports/auth-provider.ts`, the explicit ports-and-adapters marker, proving they know the pattern. And `src/application/**` imports from `src/infrastructure/**` **12 times** (`data-sync.ts` pulls in 5 infrastructure modules; `config.ts` imports `platform-paths`). **`eslint.config.js` is 12 lines with no boundary rule** — no `no-restricted-imports`, no zones. `npm run lint` runs and has no opinion about layering.
- ⭐ **`ruff` is declared at `pyproject.toml:26`, installed by CI (`pip install -e "./python[dev]"`), and invoked by nothing.** No ruff, no mypy, no format check on the Python side — while TS gets format+lint+typecheck across 10 combos. `.gitignore:47-48` anticipates `.mypy_cache/` and `.ruff_cache/`, so the tooling is expected to run *locally*. **The visible evidence:** `test_public_docs_governance.py:104-105` — two entries of the `contract_files` set literal indented **12** spaces while the other nine sit at **8**. Semantically harmless, inside the file that enforces the repository's documentation consistency. ⭐ **The only rule broken is the one whose breach breaks nothing** — v268's rule at N=2, different repository, different language.
- **`scripts/verify_project_tests.py` (137 lines) is referenced by nothing.** The only match outside its own file is `.git/index`. It is careful code — `Gate` dataclass, `ThreadPoolExecutor`, `--dry-run`, `--json`, correct `all(...)` exit-code aggregation — and its docstring even justifies its *scope* (*"this entrypoint intentionally governs only the Python SDK and public CLI tests"*). ⭐ **And it is the only automated caller of `release-smoke.mjs`**, which appears in no workflow and no npm script. So the "release smoke test" **does not run at release** — the release workflow runs `npm run verify` and `npm pack --dry-run` instead. A gate named for the moment it exists to protect, whose one automated caller nothing calls.
- A minor doc/code drift the sync gate structurally cannot see: `docs/api/README.md:64` defines `4001` as **限流 (rate limit)**; `retry.ts`'s comment calls it 「服务暂时不可用」 (*service temporarily unavailable*). Behaviour is identical (retry with backoff); only the comment disagrees. **The gate that keeps docs and skills in sync does not read TypeScript comments.**

---

## 10. Claim audit — the countable claims are accurate

This is where the subject diverges sharply from v262 and v270.

| Claim | Measured | Verdict |
|---|---|---|
| 「新增… **21 项**基金…能力」 (`README.md`) | commit `9dbef74` adds **exactly 21** fund reference files | ✅ **exact** |
| …plus 集合竞价快照 / 短期基准 / 跌停池 / 炸板池 | `market-auction-snapshot`, `market-auction-benchmark`, `special-limit-down-pool`, `special-limit-break-pool` | ✅ **4/4, and 21+4 = 25 = every skill file added in that commit** |
| 4 hosted MCP servers | 4 files in `docs/mcp/`, 4 names in README's JSON, all 4 asserted by a test | ✅ |
| 16 numbered examples | 16 dirs, all 3 assets each | ✅ |
| Node ≥22.12 badge | `package.json` `engines: ">=22.12.0"` | ✅ |
| Python 3.11+ badge | `pyproject.toml` `requires-python = ">=3.11"` | ✅ |
| 69 capabilities | asserted by `generated-contracts.test.ts` | ✅ (test-enforced) |
| Performance / speed / coverage claims | **none found anywhere** | ✅ nothing to inflate |

⚠️ **A fleet error, corrected.** The fleet raised as high-significance that "README claims 21 fund capabilities, but `endpoints-fund.md` contains 28 sections." The README says 「**新增**…21 项」 — ***added* 21**, a release delta, not a total. The fleet compared a delta against a total. **Not a discrepancy; the claim is exactly right.**

### 10.1 Forward-looking commitments — the v270 test, passed

Applying v270's rule directly: **this repository makes essentially no rotting promises.** Its scope statements are in the **present tense with an explicit temporal qualifier**:

> 「分钟 K、tick、海外行情、宏观数据、新闻公告原文和研报**目前**不在公开能力范围内。」 — *…are **not currently** within the public capability scope.*

That is a statement about the present, honestly hedged with 目前/当前 — not a commitment to future action. And the repository **dates itself**: `CHANGELOG.md` carries ISO dates per entry (and a test asserts five specific ones survive), all 6 tags are dated, and the CLI reports its own version.

⚠️ One caveat on the freshness *mechanism*: the weekly live canary is the strongest staleness detector here, but it publishes to a **7-day GitHub artifact visible to maintainers**. There is no badge, no status page, no committed result. **A freshness check whose result the reader cannot see does not inform the reader.**

---

## 11. Documentation: excellent, and Chinese-only

**Language census** (method: `tr -d '\000-\177'` per file, counting remaining non-ASCII bytes; cross-validated with `grep -cP '[\x{4e00}-\x{9fff}]'`):

| | Count |
|---|---|
| Tracked `.md` files | **164** |
| Containing Chinese | **161** |
| Pure ASCII (English-only) | **3** |

The three: `hithink-finance-cli/AGENTS.md` (11 lines), `SECURITY.md` (**3 lines**), `docs/maintainers/npm-publishing.md` (7 lines) — **21 lines of English in total**, all stubs. No `en/`, no `README.en.md`, no language switcher.

⚠️ **My fleet's docs agent claimed "all 164 files contain both Chinese and English, zero English-only documentation."** I have all three English files in hand and read them verbatim. The fleet is wrong.

⭐ **The honest impact statement:** an LLM reads Chinese fluently, so **the agent is unaffected** — the skills work as designed. It is the **human** who cannot audit what the agent is being told. For an operator whose whole discipline is *verify the claim yourself*, a **327,920-byte Chinese-only skill surface** installed globally by a postinstall is a real barrier. **The CLI is bilingual at runtime; its documentation is not.**

---

## 12. The ship's rule

> **Every gate in this repository is correct about what it checks, and silent about the adjacent thing you would assume it checks. Each gate's scope is inherited from where it lives, not from what it claims.**

| Gate | Checks correctly | Cannot see |
|---|---|---|
| `sync_skill_contracts.py --check` | 17 mirror pairs, byte-exact, both directions | `references/cli*`, `python-sdk*` — the parts describing what this repo changes every release |
| `test_public_docs_governance.py` | 9 structural doc assertions + a real link checker | its own trigger excludes README, CHANGELOG, AGENTS.md, `examples/**` |
| `generated-contracts.test.ts` | 84 skill files, transitively, via a sha256 manifest | ⭐ nothing — **this is the one that got it right** |
| `check-license.mjs` | a file named `LICENSE` exists | that `pyproject.toml` says **Proprietary** |
| `migrations/manifest.json` | `001-initial.sql` by sha256 | the other implementation of the same schema, in the same repo |
| `eslint` | format, style | 12 layering violations |
| `npm ci --ignore-scripts` | reproducible install | that all 206 `resolved` URLs point at a Chinese mirror |
| `test_monorepo_layout` export test | the export policy's denylist polarity | ⭐ it **skips** wherever it actually ships |

**The ladder:**
- **v267** — the discipline stops where the artifact stops being code
- **v268** — a gate exists where a reader can refuse; agents don't refuse
- **v269** — no gate can see an entry that was never added
- **v270** — no gate can fire on a claim that was true when it was written
- **v271** — **a gate's scope is inherited from its location, not its subject**

⭐ **And the thing that makes this subject different from the previous four: I could not find a single declared-but-absent discipline.** Everything this repository declares, it implements. Every countable claim is accurate. The gaps are *scope* gaps — a `paths:` filter, a directory boundary, a language boundary, a registry field — and they are the kind you get from building carefully in one place and shipping to another.

---

## 13. Mint decision — NO NEW MINT; **C16 N=1 → N=2**

**Corpus-first check (grep-verified):** `hithink` / 同花顺 / `fuyao` / `aicubes` / `Financial-API` have **never** appeared in the corpus. First appearance of this vendor and of the A-share market-data domain.

**The decisive collision is §C row C16 — "Agent-Native Vendor CLI (CLI surface co-designed for AI-agent consumption)"**, N=1, anchored on **v143 `larksuite/cli`**, and explicitly marked ***"PROMOTION-ELIGIBLE at N=2 (a 2nd explicitly agent-native vendor CLI with comparable agent-auth affordances)."***

v271 matches C16's defining conjunction:

| C16 axis | v271 |
|---|---|
| A vendor's **official** CLI | ✅ HiThink's own data service |
| Command surface **architected for agents** | ✅ `capabilities --format json` → `schema <id>` machine-readable discovery; uniform JSON envelope; stdout/stderr separation; stable codes → POSIX exit codes |
| **Agent-auth affordance** | ✅ `auth login --api-key-stdin --replace` (atomic, so an agent never re-asks); one canonical credential source; a skill rule forbidding a second prompt when switching surfaces |
| **Bundled agent-Skills layer** | ✅ **stronger** — 10 packages + a router skill + a `skills` command + sha256 manifest + runtime drift detection + CI generation-freshness |
| Distributed via **`npx skills add`** | ✅ `npx skills add HiThink-Tech/Financial-API --skill hithink-finance -g --yes` — **and it takes `skills@1.5.15` as a runtime dependency**, invoked directly from `postinstall.mjs` |

That last row is a **mechanically checkable** link to the C16 anchor, which C16's own note flags as the `npx skills` distribution chain.

**Comparison:** v271 is **stronger** than the anchor on skill integrity (generated-from-code, hash-pinned, CI-verified) and **weaker** on auth/identity (one API key; no `--as user|bot` identity switching).

**Decision: instance-strengthening, C16 N=1 → N=2. NO NEW MINT.** Per v235 (*a promotion is an audit act*) and the v259 precedent (C40 promoted at N=4), **the promotion question is RECORDED and NOT self-executed.** This is a fully independent, cross-vendor, cross-domain, **non-port** N=2 — the strongest form — and C16's own text makes it promotion-eligible. **Flagged for the overdue audit.**

**Alternatives considered and declined:**
- A new §C row for *"vendor-official multi-surface agent access layer for a hosted commercial data API"* — declined: the five-surface fan-out is a **delivery** shape, and C48 (firecrawl v214) already covers hosted-API + OSS client + SDKs + first-party MCP + Skill for a different domain. Domain-not-capability (v191/v197/v220, decisive).
- CONFIRMED **#24** *"Product-First Native Application Retrofitted with a First-Party MCP Server"* — declined: the MCP servers here are **hosted and remote**, and the product is a data API, not a native application.
- **#18 B1-MCP** — declined for the same reason: **no MCP server is implemented in this repository.**

**Secondary instance-strengthening (recorded, not self-incremented):** **#19** 19a (non-Anthropic vendor) · **#66** supply-chain awareness · **#88** anti-slop machinery-with-enforcement (the doc-governance suite).

**Two DEFERRED watch axes registered, not self-executed:**
1. *"Public GitHub repository generated from a private monorepo by an agent skill, carrying a test of its own export policy that can only skip where it ships"* (N=1) — a **publishing posture**, the counterpart to v270's PDF-only/ND posture.
2. *"Negative-routing skill descriptions — a multi-skill collection where every description names its sibling destinations"* (N=1) — a **skill-authoring technique**; sharply distinct from the domain-vertical skill-collection family because the novelty is in the `description` field, not the corpus of skills.

---

## 14. Method notes

**Fleet:** 12 dimensions, **9 returned, 3 died** on the StructuredOutput retry cap (`phantom-refs`, `agent-surface`, `vendor-context`). **21 agents, 2.73M subagent tokens, 777 tool uses, 42.9 min.** All three dead dimensions were hand-covered; `vendor-context` produced §7's licence chronology, the ship's most pilot-decisive finding, entirely by hand.

**Five fleet errors caught, three of them substantive:**
1. ⭐ **CLI skills "merge without drift verification"** (raised critical, **confirmed by its own adversarial verifier**) — refuted by `generated-contracts.test.ts` + the sha256 manifest. **D51 + D21.**
2. ⭐ **"21 fund capabilities vs 28"** — a delta compared against a total. The claim is exact.
3. ⭐ **"All 164 md files contain both Chinese and English, zero English-only"** — three pure-English files, read verbatim.
4. Line numbers 107/109 for the sync script's exit codes (actual 130/133) — its verifier caught this one.
5. `internal/`/`sdd-docs/` as "documentation drift," in four separate dimensions — the fact right, the interpretation wrong.

**Four corrections to my own work, all pre-publication:**
1. ⭐ **The simulated-data disclaimer count.** I grepped one phrasing (「非投资建议」) and got 8/16 for the *advice* disclaimer. Examples 01–08 use 「不构成投资建议」. Corrected: advice **16/16**, simulated-data **8/16**. **Grepping a single phrasing for a semantic property produces false negatives.**
2. ⭐ **`internal/`/`sdd-docs/` as a v265-style phantom citation** — refuted by `test_monorepo_layout.py:87-93`. An honest disclosure of a real private structure.
3. **"11 CLI skill packages"** — it is **10**.
4. **The `adjusted`-column caveat** — refuted by `importers/parquet.py:41-77`.

**Two method failures worth recording:**
- ⚠️ **`LC_ALL=C grep '[\xe4-\xe9]'` silently reported all 164 files as English-only** — zsh does not interpret `\xNN` in a bracket expression, so the pattern matched literal characters. It produced a confidently wrong answer with no error. Replaced with `tr -d '\000-\177'` and cross-validated. **v242's D23 needs a companion: declare the language basis of a count *and* prove the counting method fires.**
- ⚠️ **The vault's flaky shell dropped piped-grep output repeatedly** ("N matches in 0 files"), once producing an internally inconsistent census (206 total, 0+0+3 by host). Every load-bearing count in §8 was re-derived by routing to a file and using `awk`.

**Confirmed again:** `python3` is blocked in this sandbox (permission denied, not the v236 SIGKILL) → `awk`/`sed`/`grep`/`git`/`node` only. The repo's Python gate was **hand-simulated**, not executed.
