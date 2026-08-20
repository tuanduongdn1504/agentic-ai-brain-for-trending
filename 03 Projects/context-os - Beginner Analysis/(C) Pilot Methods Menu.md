# (C) context-os — Pilot Methods Menu (v252)

**Verdict: ⭐ READ-AND-BORROW. Do NOT install the CLI.**

Not on security grounds in the v234 sense — this is TLS, not plaintext `http://`. The reason is simpler: **the binary is closed-source, unversioned, unpinnable, and its own author says it is "not fully finished yet."** There is nothing to gain by running it that you cannot get by reading the repo, and the two documents worth having are plain markdown.

The repo itself is safe to clone and read. It ships no `postinstall`, no telemetry, and 641 lines of shell that only print.

---

## Rung 0 — 15 minutes, zero risk, do this first

```bash
git clone https://github.com/jacob-dietle/context-os.git /tmp/context-os && cd /tmp/context-os && git diff --stat v1.0-ceremony..v2.0-stigmergic
```

Then read exactly two files:

1. **`.claude/skills/eval-loop/eval/statistical-validity-checks.md`** (256 lines) — the best artifact in the repo
2. **`.claude/skills/code-service-defrag/references/landmine-patterns.md`** — the best engineering content

Then recover the deleted evidence, which is the whole story:

```bash
git show f7619ba^:eval_results.jsonl
```

Eight rows, all `"version": "new"`, seven with `tool_count: 0`. That is the entire measured basis of the README's comparison table.

---

## ⭐⭐⭐ Rung 1 — 2 hours, ZERO install, THE RUNG THAT PAYS

### (a) ⭐⭐⭐ Write the ground-truth contamination gate into the candidate-LLM ADR

**This is the highest-value borrowable in three ships, and it is not close.**

The RATIFIED candidate-LLM legibility ADR requires eval-gating and **still has no implementation**. v251 offered a *"Verifiable today?"* column. This offers the actual runbook — and hireui's Match-Explain / CV-matching feature is **exactly** the predictive-scoring problem it addresses.

**The transfer is direct and alarming.** Substitute recruitment terms into their contaminated-source table:

| Their contaminated source | The hireui equivalent | Why it's fatal |
|---|---|---|
| *"Contacts associated with closed/won deals"* | **"candidates we hired"** | *"Pre-filtered on the outcome you're predicting. Using outcomes as predictors = tautology."* |
| *"Leads that our sales team engaged with"* | **"candidates our recruiters shortlisted"** | *"already scored informally — you're copying existing bias"* |
| *"Companies we consider good-fit"* | **"candidates we consider good-fit"** | *"Circular — unless labeled before any data was seen, it's hindsight"* |

**Every ground-truth set a recruitment matcher would naturally reach for is on their contaminated list.** And training on "people we hired" is not merely a statistical error — it is the precise mechanism by which a hiring model encodes historical hiring bias, which is the EU AI Act Art. 50 / high-risk exposure the ADR exists to manage.

**Do this:** copy §1 (Ground Truth Provenance — The First Gate), §5 (Holdout), and §8 (Backwards Reasoning Detector) into `hireui/evals/METHOD.md`, rewritten for candidates. The three questions that must be answerable before any matcher ships:

1. Was this label produced **blind** to the score, and **before** any model saw the data?
2. What is the **base rate** in the full candidate universe? *(Without it you cannot compute discriminative power at all.)*
3. **What would falsify this rule?** *(If you cannot say, the rule is unfalsifiable — do not use it.)*

Plus their §5 hard floor: **N < 30 → do not iterate; label the output "directional".**

### (b) ⭐⭐⭐ Adopt the critical-fail regression test — for the vault itself

Their best idea: **when you delete an abstraction, the test is that the agent does not resurrect it.** Each of their 8 test cases carries a `critical_fail` naming a deleted thing.

The vault has a large graveyard: retired patterns C22–C27, superseded routine versions v2.1–v2.6, `/graph-health`-style commands that no longer exist, and the `-v183` label. **Write a `critical_fail` list for the vault** — a short file naming the abstractions that must never reappear in generated work — and check generated output against it. Ten lines of prose, immediately useful.

### (c) ⭐⭐ Put "Context drift fails silent" in `CLAUDE.md`, then finally write the inventory script

`code-service-defrag/SKILL.md:25` — *"Code drift fails loud (eventually — when a deploy detonates). **Context drift fails silent** — an agent reads the wrong context and nothing announces it."*

This is the vault's own disease, named. **v250 specified `bin/verify-vault-inventory.sh` (bidirectional) and it still does not exist.** This ship is the third consecutive argument for it. Write it now, in `node`/`awk` (**not `python3` — SIGKILLed here**), with four clauses:

1. `_state/` files ↔ the `CLAUDE.md` chapter index — **both directions**
2. memory files ↔ `MEMORY.md` — **both directions**
3. **filename label vs newest entry** — the clause that would finally detect `-v183`
4. byte-equality for any duplicated content, with the incident in the comment *(v251)*

### (d) ⭐ Run their monorepo landmine scan by hand against hireui

hireui lives in a monorepo — **exactly** Pattern 1's habitat: *"two configs in different directories declare the same deploy-target name and point at the same shared resources… A deploy from either location overwrites the other's code with zero warning."*

Do it by hand (their scanners only print, so there is nothing to install):
- Do any two directories declare the same deploy-target name? (`vercel.json` / `railway.json` / `fly.toml` / `wrangler.toml` / compose service names)
- Do any two services share a `DATABASE_URL` / Supabase project with **no designated schema owner**?
- Their test: *"If you ran the deploy command from each directory sharing a target name, would the same live deployment change?"*
- Their verification: **diff a live `/health` or version endpoint against each directory's source.**

---

## Rung 2 — 🔴 DO NOT. Now grounded in the installer itself.

I fetched and read `install-context-os.sh` (5.4 KB, **not executed**). The CLI does ship — but the installer's own lines make the trust model explicit:

- 🔴 **The only integrity check on the downloaded binary is `MIN_SIZE=20 20 12 61 79 80 81 98 33 100 204 250 395 398 399 400(10 * 1048576))`** — a size floor. No checksum, no signature, no GPG, no cosign (grepped; nothing else exists). **Any ≥10 MB blob served from that host installs and executes.**
- 🔴 **The version is resolved at install time** from `curl -fsSL "/latest.txt"`. Piping to bash installs whatever that mutable file points at, that second.
- 🔴 **The installer auto-registers a login-persistent daemon at a 30-second interval** (`daemon install --interval 30`, *"Register daemon to run on login"*) — the README presents this as a step *you* run later. It is not.
- ⚠️ A **staging channel** is one env var away (`TASTEMATTER_CHANNEL=staging`).
- The binary is **closed-source**, and there is **no privacy or telemetry statement anywhere in the repository**.

I did **not** establish that anything leaves the machine. But a closed binary polling your file access every 30 seconds from login, delivered by an unpinned pipe-to-shell whose sole integrity check is "is it at least ten megabytes," is not a footprint to accept on a machine holding client or candidate data.

✅ **In fairness:** the script is competently written — proper OS/arch detection, refuses truncated downloads, warns instead of failing hard, installs to one user-owned directory with no `sudo`. The objection is the trust model, not the craft.

**And you do not need it.** If you want file-heat data, `git log` plus access-time analysis on your own machine answers the same question with code you can read.

---

## 🔴 NEVER

- **Never point this at candidate data.** The ingest skill turns raw content into a persistent linked graph; hireui candidate data is governed by the RATIFIED ADR (I-2 / I-8, GitNexus-first).
- **Never train a candidate matcher on "people we hired."** The repo's own §1 names this as tautology; it is also textbook hiring-bias encoding.
- **Never cite the taxonomy access counts** (2 / 1 / 0 in 90 days) as measured. No artifact exists; it is unfalsifiable from the repository.
- **Never cite the v1-vs-v2 comparison as an evaluated result.** N=8, single-arm, no baseline, ungraded — and their own §5 says do not iterate below N=30.
- **Never cite "142 automated anti-slop tests" or "5 verified multi-agent builds."** Neither ships here.
- **Never cite the star count as verified** — page-stated only; the GitHub API is mocked in this environment.
- **Never run their anti-slop detection commands as written on macOS** — 20 use `grep -P`, which stock `/usr/bin/grep` rejects (`invalid option`, exit 2). Use `-E`, `ggrep`, or `rg`.
- **Never assume `eval-driven-scoring` is available** — the hard STOP in `eval-loop` routes to a skill that does not exist.

---

## The ladder in one line

**A1** (read the two documents, 15 min) → **⭐⭐⭐ C11** (the contamination gate into `hireui/evals/METHOD.md` — discharges the ADR clause that has had no implementation for months) → **B5** (critical-fail list + the inventory script v250 specified and v252 re-argues) → **D9** (hand-run the monorepo landmine scan on hireui).
