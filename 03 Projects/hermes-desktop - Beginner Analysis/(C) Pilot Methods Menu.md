# (C) Pilot Methods Menu — hermes-desktop (Hermes One) — v268

**Verdict: ⭐ READ-AND-BORROW. Do NOT install the application.**
Two artifacts are worth taking, one dependency is worth evaluating, and the app itself is worth avoiding.

**Why not install:** the documented install path is `curl -fsSL …/main/scripts/install.sh | bash` (`src/main/installer.ts:942`) — from a **moving branch**, with **no checksum or signature** (`grep -i "sha256\|checksum\|gpg\|signature"` over `installer.ts` = 0 hits), executed with your shell profile sourced. On WSL the README asks you to grant **passwordless sudo**. The release pipeline has **0 of 34 Actions SHA-pinned** and **blanket `contents: write`** on both release workflows. Official builds ship **opt-out telemetry, on by default**. And a **first-party MIT desktop app has existed since 2026-06-02**, which the README does not mention. None of that is needed to get the value.

---

## Rung 0 — 20 minutes, read only, zero risk

Read these seven things in this order. They are the whole ship.

| # | Path | Why |
|---|---|---|
| 1 | `CLAUDE.md:6-12` | *"Post-task checklist (REQUIRED — do not skip) … Run `lat check` … Do not consider your task done until both are complete."* |
| 2 | `.github/workflows/ci.yml:33-44` | what is actually gated: typecheck + test. **`lat check` is absent.** Lint is non-gating **with a written reason.** |
| 3 | `.husky/pre-commit:1-4` | four lines that `exit 0` on every branch but `release` |
| 4 | `lat.md/lat.md:1` | *"Install the `lat` command with `npm i -g lat.md`"* — **the install instruction for the validator, inside the artifact it validates** |
| 5 | `Development.md` + `CONTRIBUTING.md` | the human path: lint and typecheck. **`lat` appears in neither.** |
| 6 | `src/main/secrets/securityInvariants.test.ts:4-24` | **the best twenty lines in the repository** |
| 7 | `src/main/security.ts:93-97` beside `CLAUDE.md` / `AGENTS.md` | one enforcement point for the settings a compiler reads; a duplicated blob for the ones only an agent reads |

**The takeaway to write down:** *a gate exists where a reader can refuse. Agents don't refuse.*

---

## ⭐⭐⭐ Rung 1 — 30 minutes, and it is about this vault

Three consecutive ships have handed over the same lesson. v263 found a nine-clause script nothing invokes. v267 found that the one surface with no gate is the one carrying the claims. **v268 supplies the half that was missing: integrity is cheap, coverage is what rots silently.**

A `lat check` for this vault would verify every `[[link]]` in `_state/` and `_patterns/` and say **nothing** about a ship whose findings were never filed. That is exactly how the v259 audit came to measure a count wrong — twice.

**Do both halves:**

**(a) Integrity — derive, don't restate.**
```bash
# counts that are currently hand-maintained in the shim
grep -c '\*\*C[0-9]*\*\*' "_patterns/06-library-vocab-registry.md"      # §C total
# then split §C-1 (N>=2) from §C-2 (N=1) off the N field, not off prose
```
Derive **46 / 12**, **§C-1 12**, **§C-2 39** and the **`GA:` / `OG:` streak** from the `C##` markers and the per-ship tags, and fail on mismatch.

**(b) ⭐ Coverage — the half v268 adds. Both directions, per D15.**
```bash
# every ship in the shim has an entry in 03c
# every entry in 03c is referenced by the shim
# neither direction is visible to a link checker
```

**(c) Wire both into `(C) proposed-verify-vault-inventory.sh`** — the nine-clause script that reports 0 FAIL and that **nothing invokes** (v263's finding, restated at v267, still open). A git hook or a `bin/` move; either closes it.

⚠️ **Note the shape of the trap before you build it:** a checker that only validates links will report a clean vault forever, exactly as `lat check` reports a clean 597-edge graph in a repository whose #2 contributor's 159 commits appear nowhere in it.

---

## ⭐⭐ Rung 2 — 45 minutes, the most portable artifact in the repository

**Port the security-invariant suite pattern into hireui.** From `src/main/secrets/securityInvariants.test.ts`:

1. One file. Each `it` encodes **one invariant that must hold forever**, for any implementation — not one test of one function.
2. A header comment that **maps each past review finding to the invariant it taught**:
   > *"All three review-found bugs on this feature were violations of an invariant below: `resolvedSecrets()` bypassed the spawn floor → INV-2 (single spawn path); `list()`/`get()` disagreed on whitespace → INV-3; S2 guard leaked a comment-prefixed wrong key → INV-1."*
3. **Property-based** where the input space is wide (`fast-check`), example-based where it is narrow.
4. A stated stakes line: *"A red line here is a security regression, not a style nit."*
5. Split the layers deliberately — parser invariants property-style in one file, **system** invariants behind a fake implementation *"so a future provider can't silently break the contract."*

**Compose it with the standing BOLA authorization audit** (recorded as hireui's #1 risk: authorization absent from all 7 OWASP techniques). Every BOLA finding becomes **INV-n** rather than a patch — which is the difference between fixing a bug and making it unrepeatable.

---

## ⭐⭐ Rung 3 — 60 minutes, evaluate `lat.md` seriously (scratch repo only)

`lat.md` is the closest thing the corpus has found to a **productised version of this vault's founding pattern**: a repo-resident cross-linked markdown knowledge graph, `[[wiki links]]` between sections *and into source symbols*, `@lat:` code refs pointing back, semantic search, and **`lat check`** — the validator the vault has wanted for five ships. Author: **Yury Selivanov** (`1st1`) — CPython core developer (`asyncio`, PEP 492), ex co-founder/CEO of Gel/EdgeDB and MagicStack, now at Vercel; published as **`vercel-labs/lat.md`**, MIT, ~1.8k★.

**Fence it:**
```bash
# BEFORE anything: snapshot, then vet the package
```
Run the **`install-snapshot`** skill first (this is a global `npm i -g` of a package you have not read), and **`npm-security-check`** before that.

**Evaluate on a scratch repo, never on the vault.** The two questions that actually decide it:

1. **Does it survive `_state/03c`?** That file is ~2.3 MB with individual entries that are single enormous lines. A section parser and a ≤250-char leading-paragraph rule may be structurally incompatible with how this vault writes. **Test that first — it is the cheapest disqualifier.**
2. **Does bidirectional linking work when the "code" is prose?** `lat`'s power comes from `@lat:` refs in *source files* tying code to concepts. The vault's "code" is markdown. The analogue would be per-ship entries referencing pattern rows — which is what the `C##` markers now make possible.

⚠️ **And carry v268's own warning into the evaluation:** adopting the tool gets you integrity, not coverage. If you adopt it, adopt the flag too — **`require-code-mention: true` is the one primitive that catches what is missing, and the subject documented it four times and used it zero times.**

---

## ⭐ Rung 4 — 20 minutes, close a decision v259 left open

The subject ships `CLAUDE.md` and `AGENTS.md` as **byte-identical copies, not symlinks**. It is safe only because nobody has edited either in 1301 commits. v243 solved this with a **9-byte symlink to a canonical file**.

v259 recorded that `05 Skills/` holds copied, re-versioned skills and that the routine exists as v2.1→v2.8 separate files, *"so a fix in the newest copy will not reach the older ones"* — and left the decision open. **Close it:** either the shared surfaces become single-owner files referenced by the rest, or the duplication is declared with a which-copy-wins notice (the v245 **D32** pattern already used in `_state/03c`). Both are acceptable; leaving it undecided is what is not.

---

## Rung 5 — the natural next subject

⚠️ **The ~v268 audit is DUE.** v259 named it; v260→v268 have all shipped without one. It has real business waiting:

- **CONFIRMED #22** — hermes-desktop is the strongest candidate yet for generalising it on **both** axes (non-Tauri *and* non-coding-agent); the row's own text anticipates the first
- **C42** — a *validate-and-retrieve* vs *generate* watch axis
- a **business-model** mint alternative near **LV-C2**: *a client author monetising someone else's OSS by becoming its default provider*
- the **fourth pass** at the community-front-end genre (v222 / v227 / v236 / v241 / v268) — five declines; is the genre settled enough to say so in the routine?
- **§43.1** now has five consecutive confirmations, and **v268 broke the four-ship run of "fleet failures landed on covered ground"** — two of eleven dimensions died on ground I had not covered, and only a manual diff of the failure list against my own coverage caught it

**Alternative if the audit waits:** the upstream **`NousResearch/hermes-agent`** itself — a corpus *entity* since v227, referenced by two subjects now, never wikied. It is the thing both front-ends exist to drive, and the corpus has never read it.

---

## 🔴 The NEVER list

- **NEVER** install the app to try it — `curl | bash` from a moving branch, unverified, shell profile sourced
- **NEVER** grant the passwordless sudo the README's WSL workaround requests
- **NEVER** treat its release binaries as coming from a hardened pipeline — 0/34 pinned, blanket write
- **NEVER** point its 16 messaging gateways or its cron scheduler at anything touching candidate data — untrusted inbound messages reaching an agent with tools
- **NEVER** forget telemetry is **opt-out, on by default** in official builds
- **NEVER** read *"community maintained"* as *"the only option"* — a first-party MIT app has existed since 2026-06-02
- **NEVER** cite the wallet as a fund-loss risk — **there is no signing primitive anywhere in `src/`, `tests/` or `scripts/`**
- **NEVER** cite my 0/0 sweep as *"`lat check` passes"* — it is my reading of four documented rules, not the tool's output
- **NEVER** cite star or download counts (§37.4)
