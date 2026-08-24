# (C) Pilot Methods Menu — HiThink-Tech/Financial-API (v271)

**Verdict: ⭐ READ-AND-BORROW. Do not `npm install -g`. One narrowly-fenced live pilot is available if you actually want A-share data.**

Everything in Rungs 0–2 costs nothing, installs nothing, and needs no API key. Rungs 3–4 touch the vault and hireui. Rung 5 is the only rung that installs anything, and it is fenced.

---

## Rung 0 — Read the four best things (40 min, zero install)

Clone is already at
`/private/tmp/claude-501/-Users-Cvtot-KJ-OS-Template/84006d40-b519-4af6-8676-6dd2a563d0d7/scratchpad/v271/cloneA`
(HEAD `9dbef74d`; treat as read-only; it will be garbage-collected with the session — re-clone if you want it kept).

1. **`hithink-finance-cli/tests/contract/generated-contracts.test.ts`** — the manifest-delegation gate. Read the second test. Eight files byte-compared; one of them is a sha256 manifest of eighty-four. **This is the fix v269's subject lacked.**
2. **The ten skill descriptions** — `for f in hithink-finance-cli/skills/*/SKILL.md; do sed -n '/^description:/p' "$f"; done`. Every one ends by naming where to go instead.
3. **`python/marketdb/calculations/adjustment.py`** — 125 lines, the A-share ex-rights formula, `EXP(SUM(LN()))` cumulative products, ex-dates mapped to the next real trading day, `factor_version` stored per row.
4. **`hithink-finance-cli/src/infrastructure/fuyao/retry.ts`** — jitter with a written explanation of *why*, both `Retry-After` formats, `random` and `sleep` injected for determinism.

Then read `python/tests/test_monorepo_layout.py:87-93` — five lines that tell you the whole repository is a snapshot export, and that the test guarding the export can only skip where it ships.

---

## Rung 1 — ⭐⭐ The vault's own gate-scope audit (30 min) — **do this one**

This ship's rule turned on us: *a gate's scope is inherited from its location, not its subject.*

**Step 1 — stop the sixteen-ship embarrassment.** `03 Projects/HeadFirstAndroid - Beginner Analysis/(C) proposed-verify-vault-inventory.sh` has nine clauses, was written at v255, re-asserted at v256, found un-invoked at v263, and asked for again at v269 and v270. Move it out of a project folder, drop `proposed-` from the name, and give it one caller. HiThink at least wired theirs to the wrong paths.

**Step 2 — add clause 10, the v271 clause:**

> For every declared gate, assert that its trigger covers the files it asserts on. FAIL a gate whose assertions name files outside its trigger scope.

Follow v240's decay doctrine: **flag never remove · skip the inconclusive · evidence not doubt · removal is human.**

**Step 3 — run it and act.** v270 already measured the backlog: 31 forward-looking commitments in `CLAUDE.md`, 8 self-flagged OVERDUE, and `_state/03c-projects-v61-v183.md` holding **v271** — 88 ships past its name — cited by the stale name in 31 files. The v245 D32 notice mitigates it; the rename still hasn't happened.

---

## Rung 2 — ⭐⭐⭐ Negative routing clauses for `05 Skills/` (45 min) — **the highest-value borrow**

The vault has nine skills and a routine that exists as **v2.1 → v2.8 as eight separate files**. v259 named the consequence: *"a fix in the newest copy will not reach the older ones."* That is a routing problem, and HiThink solved the sibling half of it in the one field the model always reads.

**Do this:** for each skill in `05 Skills/`, rewrite its `description` to end with an explicit redirect naming its nearest siblings and what it is *not* for. Pattern, verbatim from the subject:

```
description: 用于 …<what it IS for>…；<adjacent concern> 转 <sibling-skill-name>，<out-of-scope thing> 不在本 skill 范围。
```

In English, for the vault:

```
description: Use for <X>. For <adjacent concern> use <sibling>. <Out-of-scope thing> is NOT in this skill's scope.
```

The eight routine files are the acid test: each older version's description should say *"superseded — use llm-wiki-routine-v2.8; this file is retained for historical reference only."* That is a negative routing clause, and it costs one line per file.

**Then check `SKILL_LOCK_POLICY.md` still describes reality** — it is a nine-row table asserting facts about nine files, and nothing verifies it. Exactly the class clause 10 is for.

---

## Rung 3 — ⭐⭐ Two patterns into hireui (60 min)

**3a. Delegate the list, don't restate it.** Wherever hireui has generated artifacts checked in (schemas, types, fixtures, API clients), don't hardcode filenames in the freshness test. Emit a manifest that hashes every generated file, commit it, and byte-compare **the manifest**. One assertion, complete coverage, and a new file cannot silently escape.

**3b. The capability/schema discovery protocol.** `capabilities --format json` → `schema <id>` → run, with 「Agent 不应只凭 README 猜参数」 written into the skill. If hireui ever exposes a tool surface to an agent, this is the shape: a machine-readable capability index, per-capability schemas, a uniform result envelope (`ok`, `meta.request_id`, `error.code/category/hint`), and stable error codes mapped to exit codes. **It composes directly with the RATIFIED candidate-LLM legibility ADR** — every call gets a request id and a typed error category, which is what "audited" needs to mean in practice.

**3c. Steal the placement, not the platitude.** Put the anti-fabrication rule on the specific failure that tempts invention. For hireui's CV parsing: *"when a field is absent, emit `null` — never zero, never an inferred value, never a plausible default"* attached to the extraction step, not to a general style guide. 「`null` 保持缺失，不补零」 is one line and it prevents a whole class of silent corruption.

🔴 **Do not copy their code into hireui.** `python/marketdb` declares `Proprietary`.

---

## Rung 4 — ⭐ The dependency-provenance check you don't have (20 min)

This ship's sharpest supply-chain finding was invisible to four CI workflows: **all 206 `resolved` URLs in the published lockfile point at `registry.npmmirror.com`.** Integrity hashes made it harmless; nobody had checked.

Run this against hireui and the vault's own Node projects:

```bash
grep '"resolved":' package-lock.json | grep -v "registry.npmjs.org" | sort -u
```

Empty is the answer you want. If it isn't empty, someone's local `--registry` leaked into a committed lockfile. Add it as a one-line CI step — it is the cheapest gate in this entire menu.

---

## Rung 5 — The only live pilot, heavily fenced (60 min) — **only if you want A-share data**

You almost certainly don't. There is no hireui use case, no vault use case, and the data licence is an off-repository account agreement this repository does not reproduce. Do this **only** out of genuine interest in the market data.

**Fences, all of them:**

1. **Never `npm install -g`.** The postinstall writes 85 skill files into your global agent skills directory, undisclosed. Instead build from source, which the repo documents and which never runs postinstall:
   ```bash
   cd hithink-finance-cli && npm ci --ignore-scripts && npm run build
   node dist/cli/main.js capabilities --format json
   ```
2. **Before that, run the Rung 4 check on their lockfile** and decide whether you accept 206 fetches from `registry.npmmirror.com`. If not, `npm install --ignore-scripts --registry=https://registry.npmjs.org` instead of `npm ci` — you lose the lock, you gain the host.
3. **Run `/install-snapshot` first** regardless. Node 22.12+ required.
4. **Never let the CLI's `skills` command near your real `~/.claude/skills`.** Use `--target` into a throwaway directory, or skip the skills entirely — you can drive the CLI as a subprocess without installing a single skill file.
5. **Key handling:** `printf '%s' "$KEY" | node dist/cli/main.js auth login --api-key-stdin` — never argv, never a file, never the conversation. It lands in the OS keychain via `@napi-rs/keyring`.
6. **Pick exactly one path.** Either the TS CLI *or* Python `marketdb` — never both against one `.duckdb` file. Their defaults differ; keep them differing.
7. **Assume every query is observed.** The endpoint is PRC-hosted and each call reveals which securities you're looking at.
8. **Never point anything here at candidate data.** No hireui data, no CV content, no PII. This is a market-data client; there is no reason for it to see anything of yours.

**If you do run it, the one thing worth measuring:** whether `capabilities` + `schema` actually lets Claude call a 69-capability surface correctly with no README in context. That is the interesting question — it is the closest thing in the corpus to a controlled test of *machine-readable capability discovery versus prose documentation*, on a real vendor surface. Log what the agent gets wrong.

---

## Never

🔴 Redistribute the data. 🔴 Vendor `python/marketdb` (declares `Proprietary`). 🔴 Treat MIT as a data licence. 🔴 Cite `01-stock-overview/example.html` as real output — 70 KB of synthesised data, no in-file label, 616 of 1,880 decimals carrying a repeating-sevenths fingerprint. 🔴 Install the skills globally. 🔴 Read 「官方」 as a verified corporate identity — the org name, the npm scope and an `aicubes.cn` domain are **assertions**, not verification, and the only named human in 402 files is one `authors` field.
