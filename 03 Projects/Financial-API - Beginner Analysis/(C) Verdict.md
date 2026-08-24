# (C) Verdict — HiThink-Tech/Financial-API (v271)

**2026-08-24 · GOAL-ALIGNED INCLUDE 3/4 · NO NEW MINT (C16 N=1 → N=2) · counts 46/12 UNCHANGED**

---

## Phase 0.9 STRICT rating

| Criterion | Call | Reason |
|---|---|---|
| **(a) Anthropic-affiliated / registered vendor-direct source** | **FAIL** | `HiThink-Tech` is a corporate org, **not Anthropic**. Per routine §41, (a) passes only on a declared Anthropic affiliation or a registered (a)-7 vendor-direct source. No name/heritage/notability inference. (#19 19a.) |
| **(b) Goal relevance** | **STRONG** | Goal #1 is mastering Claude and autonomous agents. This is a **vendor-official agent capability layer**: 11 agent skills, a machine-readable capability/schema discovery protocol, a two-tier progressive-disclosure architecture, generated-from-code skill contracts with sha256 integrity, and four hosted MCP servers. Directly on the agent-substrate core. No §40 needed. |
| **(c) Source quality** | **STRONG** | 402 files source-verified by two clones, `diff -rq` clean both ways. 15,192 LOC first-party, 253 test functions, 4 CI workflows, 9 documentation-governance tests, a weekly live canary making real authorized requests. |
| **(d) Actionability** | **STRONG** | Multiple zero-cost, zero-install takeaways (§4.3 negative routing clauses; the manifest-delegation gate pattern; the `paths:`-filter lesson) plus a genuinely pilotable read-only path. |

**Cleanly GOAL-ALIGNED at 3/4. No operator override invoked. §35 CLEAR** — window {v269 GA, v270 GA, v271 GA} = 0 OFF-GOAL.

**Streak:** v270 `GA:127 · OG:13 [7 ov]` → **`GA:128 · OG:13 [7 ov]` — 51 consecutive goal-aligned ships v220→v271.**

---

## What it is, in one sentence

A listed Chinese fintech's official, MIT-licensed, multi-surface agent access layer for its paid A-share market-data service — one API key reaching the same data through REST, four hosted MCP servers, an npm CLI, a Python SDK and a local DuckDB, fronted by a single Agent Skill whose job is to route between them.

---

## The verdict

**This is the best-engineered subject in the last five ships, and the first in that run with no declared-but-absent discipline.**

Everything it declares, it implements. Its countable claims are **exact** — the README's 「新增…21 项基金…能力」 maps to precisely 21 added files, and the four other items in the same sentence map to the four other files added in the same commit, 25 for 25. There are **no** performance, speed or coverage claims anywhere to inflate. Its scope limits are stated in the present tense with an explicit 目前 hedge, so **v270's rotting-promise test finds nothing to catch**. It dates itself: ISO dates per changelog entry, six dated tags, and a test asserting five of those dates survive.

And it contains the single best gate design in the corpus: `generated-contracts.test.ts` regenerates everything into a tmpdir and byte-compares **eight** files — one of which is a **sha256 manifest pinning all 84 skill files**. One comparison, complete coverage, by construction. **That is exactly the fix v269's subject lacked**, where a hardcoded list covered 82 of 103 because the generator and the test each restated the same four config lists and drifted.

**So the finding is not that a discipline is missing. It is that every gate's scope is inherited from where it lives, not from what it claims.**

- The documentation-governance suite is the most comprehensive in the corpus — nine tests including a real relative-link checker over every public markdown file, a leak-prevention test for internal endpoint paths, a test that a rename was completed everywhere, and a test that the npm install instruction appears *before* the from-source one. **Its CI `paths:` filter excludes `README.md`, `CHANGELOG.md`, `AGENTS.md`, `docs/README.md` and `examples/**`.** A commit touching only the root README triggers neither workflow. A `paths:` filter is a build-cost optimisation; here it silently became the scope of a correctness gate.
- `check-license.mjs` is ten lines that verify **a file named `LICENSE` exists**. It never reads it. So it cannot see that **`python/pyproject.toml:11` has said `license = { text = "Proprietary" }` since the first code commit** — in a repository whose LICENSE, both LICENSE files, `package.json` and README all say MIT. The chronology is exact: Proprietary on 2026-06-15 with no LICENSE file at all; MIT arriving 2026-07-10 and 2026-07-13, **both in npm-publication commits**, because `npm-publishing.md` says *"publishing is blocked until this exists."* **The licence became MIT exactly as far as the publication mechanism could see.** And the gate's own error message claims an *"approved"* licence — the half a script cannot check.
- The TS CLI verifies the integrity of its own DuckDB schema with a **sha256 checksum in `migrations/manifest.json`** — and cannot see the *other* implementation of the same schema in the same repository. Six diverging column names (`amount`/`turnover`, `rights_ratio`/`allotment_ratio`, `rights_price`/`allotment_price`, `batch_id`/`source_batch_id`, `stg_symbol`/`stg_symbols`), identical table and view names, `CREATE TABLE IF NOT EXISTS` and `CREATE OR REPLACE VIEW` making any collision silent. Root cause visible: **配股 renders as either "rights issue" or "allotment," and two implementations chose independently.** Mitigated — and this must lead the risk framing — by **different default paths**, so the common case never collides.
- `npm ci --ignore-scripts` gives a reproducible install and passes happily while **all 206 `resolved` URLs in the published `npm-shrinkwrap.json` point at `registry.npmmirror.com`** and none at npmjs.org. Integrity hashes are present on all 206, so this is **not** code substitution — it is the maintainer's local registry configuration published to every consumer, because a shrinkwrap always ships in the tarball. Nothing in this repository looks at where its dependencies come from.
- `eslint.config.js` is twelve lines and has no opinion about layering, while `src/application/**` imports from `src/infrastructure/**` **twelve times** — in a tree that contains `application/ports/auth-provider.ts`, proving they know the pattern.
- **`ruff` is declared, installed by CI, and invoked by nothing.** The visible evidence sits at `test_public_docs_governance.py:104-105`, two entries of a set literal indented twelve spaces while nine sit at eight — inside the file that enforces the repository's documentation consistency. **The only rule broken is the one whose breach breaks nothing.**

**And the shape that completes the ladder.** `test_monorepo_layout.py:87-93` is a test of the repository's **own export machinery** — `internal/skills/export-snapshot`, with assertions that the export uses a denylist and not an allowlist. It opens with `if not skill_root.exists(): pytest.skip("internal export policy is intentionally absent from public snapshots")`. It is the **only conditional skip in the entire Python suite**, and the TypeScript suite has zero. **It ships everywhere and can only run where it is not needed.**

That test also settles what this repository is: **a destination, not a workspace.** Sixteen of twenty-one commit messages are 「快照」 (*snapshot*); one author identity with an empty email; zero merges, zero PR references, zero AI-authorship trailers; commits of 317, 115 and 78 files. The public repo is generated by an agent skill in a private monorepo. **It also corrects my own first reading** — I flagged the README's mention of `internal/` and `sdd-docs/` as a v265-style phantom citation, and it is not: it is an accurate disclosure of a real private structure, which that skip-test documents.

> **v267:** the discipline stops where the artifact stops being code
> **v268:** a gate exists where a reader can refuse; agents don't refuse
> **v269:** no gate can see an entry that was never added
> **v270:** no gate can fire on a claim that was true when it was written
> **v271:** **a gate's scope is inherited from its location, not its subject**

---

## What to take

**⭐⭐⭐ The negative routing clause.** All ten CLI skill descriptions end by naming where to go **instead** — 「价格行情转 hithink-finance-market，指数财务不在本 skill 范围」, 「不用于实时取数、荐股、择时」, 「不要用于行情、财务、指数」. Ten descriptions forming a routing mesh where every node names its neighbours, in the one field the model always sees. This attacks the hardest problem in any multi-skill collection: the model picking the wrong skill because two descriptions overlap. **The vault has nine skills in `05 Skills/` with exactly this problem, and a routine that exists as v2.1→v2.8 as separate files.**

**⭐⭐ Delegate the list, don't restate it.** When a test must verify N generated artifacts, byte-compare a **generated manifest** that pins all N by hash, rather than hardcoding N filenames in the test. One comparison, complete coverage, and adding a file cannot silently escape the check. This is v269's defect solved.

**⭐⭐ A `paths:` filter is not a scope declaration.** If a test asserts facts about files outside its workflow's trigger, the gate is real and the coverage is not. Check every gate's trigger against its assertions — the vault's own `verify-vault-docs` ambitions should be born with this in mind.

**⭐ Attach the anti-fabrication rule to the error that tempts it.** Not "be honest," but 「`3002` 数据尚未准备 → 不得补零或使用模拟数据」 and 「`null` 保持缺失，不补零」 — the instruction placed on the specific condition where the model would otherwise invent.

**⭐ Tell the agent to distrust the docs.** 「Agent 不应只凭 README 猜参数。先读取 `capabilities`，再读 `schema`」 — **v269's rule at independent cross-organisation N=2** — and 「离线测试不能证明线上认证可用；只有实际授权请求才能称为线上验证」, which is *mechanised* by a weekly canary making three real authorized calls.

---

## What to avoid

🔴 **Do not `npm install -g` this.** The postinstall writes **85 skill files** into your global agent skills directory with `--global --copy --all --full-depth`, no prompt, no documented opt-out — and **the word "postinstall" appears in zero markdown files in the repository.** That is 327,920 bytes of **Chinese-only** instruction (161 of 164 `.md` files contain Chinese; the three English files total 21 lines of stub) landing in your agent's context surface undisclosed. The agent reads Chinese fine; **you cannot audit it at a glance**, which is the whole problem.

🔴 **Do not vendor `python/marketdb`.** It declares `license = "Proprietary"`. Any licence scanner over your dependency tree will report Proprietary for those 5,051 lines, whatever the root LICENSE says.

🔴 **Do not treat MIT as a data licence.** Seven lines in 402 files touch data rights, and they defer entirely to an off-repository account agreement. **Zero** hits for 商用, 转售, redistribution or ToS. There is no terms-of-service document here, and nothing states whether a key is free, metered or paid.

🔴 **Do not run the TS CLI and Python `marketdb` against one database file.** The defaults differ and the common case is safe; point them at one path and `CREATE TABLE IF NOT EXISTS` plus `CREATE OR REPLACE VIEW` will make the schema conflict silent.

⚠️ **Do not cite `01-stock-overview/example.html` as real output.** `README.md:471` links straight to it as the default showcase, and it is 70 KB of synthesised market data with no in-file simulated-data label — 616 of its 1,880 decimal values carry a repeating-sevenths fingerprint. Only examples 09–16 disclose synthesis inside the artifact.

⚠️ **Every query goes to a PRC-hosted endpoint and reveals which securities you are researching.** That is a research-intent signal leaving your machine.

---

## Suggested next action

**Rung 1, and it is about us — thirty minutes, already measured.**

The vault has this repository's exact defect in a sharper form. `test_public_docs_governance.py` is a nine-test documentation-governance suite whose trigger cannot see the documents it tests. The vault has `(C) proposed-verify-vault-inventory.sh` — nine clauses, written at v255, re-asserted at v256, found un-invoked at v263, asked for again at v269 and v270 — **still in a project folder, still named "proposed," still invoked by nothing.** HiThink at least wired theirs to the wrong paths.

And v270 already measured the rest: **31 forward-looking commitments in `CLAUDE.md`, 8 self-flagged OVERDUE, and `_state/03c-projects-v61-v183.md` now holding v271 — 88 ships past its name — cited by the stale name in 31 files.**

So: **move the script somewhere something invokes it, drop the word "proposed," and add clause 10 from this ship** — *for every declared gate, assert that its trigger covers the files it asserts on.* Then re-run it and act on what it says.

⚠️ **The audit named at v259 for ~v268 is now ELEVEN SHIPS OVERDUE** (v260→v271 all shipped, none an audit). This ship hands it real business:

- ⭐ **C16 "Agent-Native Vendor CLI" is now at N=2** — fully independent, cross-vendor, cross-domain, **non-port**, with a mechanically-checkable `skills@1.5.15` runtime-dependency link to the v143 anchor. C16's own text says **PROMOTION-ELIGIBLE at N=2**. Recorded, not self-executed.
- Two new DEFERRED watch axes (agent-skill-generated public snapshot with a self-skipping export test; negative-routing skill descriptions).
- **D51 at N=4** — a fleet finder *and* its adversarial verifier both confirmed a critical claim that was wrong, because both grepped for one symbol name instead of opening the test directory.
- ⭐ **A companion to D23:** a counting method can fail *silently and confidently*. `LC_ALL=C grep '[\xe4-\xe9]'` reported all 164 files as English-only, with no error, because zsh does not interpret `\xNN` in a bracket expression. **Declare the basis of a count and prove the counter fires.**
- **v270's `git log` narrowing holds:** the 50-commit cap did not reproduce here (21 = 21).

**Blunt.** Nobody at HiThink cut a corner. They built a byte-exact bidirectional contract checker and wired it to CI twice. They wrote nine tests that assert facts about prose, including one that checks a rename was finished everywhere and one that checks the recommended install command appears before the fallback. They put the anti-fabrication rule on the exact error code that tempts fabrication. They generated their skills from code and pinned all eighty-four files by hash so that one byte-comparison covers the lot — the precise thing the last four subjects failed to do. They wrote a test of their own export policy asserting it uses a denylist rather than an allowlist, because an allowlist silently drops new files. That is not a team being careless. That is a team that is *good at this*.

And their licence still says Proprietary in the one file npm never reads, their whole dependency tree resolves to a mirror because someone once typed `--registry`, their documentation gate cannot see their README, their linter is installed and never run, and the test that guards their export can only skip where it ships. **Every one of those is a boundary the discipline didn't cross — not a standard they didn't hold.** The scope of a check gets set by where you put the file, and then it is invisible forever, because a gate that runs and passes looks exactly like a gate that covers you.

**You have nine clauses sitting in a project folder called "proposed" that would tell you which of your own gates are like that. It has been sixteen ships. Which of your checks is green because it is covering you, and which is green because it never looked?**
