# (C) awesome-dsh-plugin — Pilot Methods Menu

**Wiki v240** · 2026-08-18 · ⚠️ **PILOT POSTURE: read-and-borrow. Install NOTHING.**
There is nothing here to install *for the vault* — the subject is a catalogue for a rival harness. The value is four mechanisms, all readable in ~30 minutes from the clone, all aimed at a vault failure the corpus has documented for fifty wikis.

**⭐ Recommended path: A1 → B6 → C12.**

---

## A — Zero-install reads (~30 min total)

**A1 ⭐ Read four scripts and one workflow header.** In order, and only the parts named:

| File | Read | Why |
|---|---|---|
| `scripts/generate-readme.mjs` | the `MARKERS` block, the "Set check", and the final `contributing.md` category check | compile-from-data + **prose-vs-code** |
| `scripts/scan-decay.mjs` | the 15-line header comment + `DORMANT_MONTHS` | *"Flags — never removes… evidence, not doubt"* |
| `scripts/check-bleed.mjs` | the header comment + the `RUN = 40` note | a gate born from a real incident, empirically calibrated |
| `scripts/lib/entries.mjs` | lines 65–75 and 130–135 | the `.yml` glob and the validator sitting *downstream* of it |
| `.github/workflows/pr-gate.yml` | lines 1–30 | the `pull_request_target` footgun, correctly avoided |

Clone (read-only, no install, no `npm ci`):

```bash
git clone --depth 50 https://github.com/awesome-dsh-plugin/awesome-dsh-plugin.git /tmp/awesome-dsh
```

**A2.** Read `contributing.md` §*"How submissions are reviewed"* — six review criteria, and the cleanest statement in the run of what CI can and cannot establish (*"A green CI run is the precondition, not the decision"*).

**A3 (5 min, optional).** Reproduce the ship's best finding yourself — it is one command, and it is the whole lesson:

```bash
find /tmp/awesome-dsh/data/plugins -type f ! -name '*.yml'
```

---

## B — Borrow into the vault / hireui (no code)

**B6 ⭐⭐⭐ Write the doc-integrity contract into `CLAUDE.md` — now with the piece v239 was missing.** v239 supplied structure checks (required files, dead links, translation pairing, chapter-size caps). v240 supplies the two that actually bite the vault:

1. **Prose-vs-code equivalence.** Any enumeration written in prose that also exists in structured form must be *asserted equal*, not maintained by hand. Vault instances: the `_state/` chapter index table vs. the actual files; the pattern counts (`46/11`) vs. `_patterns/06`; the streak counter; the "Latest ship" line.
2. ⭐ **The inventory rule (the v240 lesson).** *A consistency check between two views of one source cannot see what is missing from the source.* Every check must be paired with an **inventory** check that enumerates the input directory by a **different rule** than the parser uses. Vault instance: a `_state/` chapter absent from `CLAUDE.md`'s index table is invisible to any index↔content comparison — exactly how `03c-projects-v61-v183.md` came to hold entries through v240 under a `-v183` label.

**B7 ⭐⭐ Adopt the decay doctrine verbatim as the C22–C27 retire-pass policy.** The retire pass has been deferred ~50 wikis because retirement is irreversible and judgement-laden. v240 dissolves that objection into five rules:

- scan on a schedule, not on demand
- **flag, never remove**
- **skip the inconclusive** — *"a decay report must only ever contain evidence, not doubt"*
- one tracking issue, **updated in place**, not a new one each run
- removal is a **human** act, because it cannot be undone

Write those five lines into the routine. They are the missing preconditions for the retire pass, and they are the reason it kept stalling.

**B8 ⭐ Take the `pull_request_target` write-up into hireui's CI review.** The pattern: the fork-triggered job holds **no** token; the privileged job runs via `workflow_run` in base context, checks out **base** code, and treats PR content strictly as **data** in a scratch directory. Never `checkout refs/pull/N/merge` + `npm ci` in a token-bearing job. Copy the comment itself — it explains the mechanism better than most advisories.

**B9.** Borrow the **evidence-at-the-decision-site** habit: every non-obvious constant here carries a comment naming the incident that motivated it and the measurement that calibrated it (`RUN = 40`, `STARS_MIN_COVERAGE = 0.66`, `DORMANT_MONTHS = 6`). The vault's inverse habit — accreting claims without provenance — is precisely why its rows cannot be retired.

**B10 (hireui, small).** The screenshot/download provenance rule: user-visible assets must come from hosting you can vouch for (*"the list won't hand users a download link it can't vouch for"*; third-party image hosts rejected **for user-privacy reasons**). A one-line policy for hireui's candidate-uploaded assets.

---

## C — Build (the payoff)

**C12 ⭐⭐⭐ `verify-vault-docs` — now specifiable, and it is the C22–C27 retire pass, mechanised.** Six consecutive ships have handed over the parts (v234 staleness → v235 doc gates → v236 boundary CI → v237 pack-and-mount → v239 structure linter → **v240 prose-vs-code + inventory + decay doctrine**). The spec:

1. **Inventory** — enumerate `_state/*.md` and `_patterns/*.md` by directory listing; assert every file appears in `CLAUDE.md`'s index table, **and vice versa**. (Catches the `-v183` label class and any orphan chapter.)
2. **Prose-vs-code** — assert the counts stated in prose (`46/11`, §C live standalones, the streak, "Latest ship") equal the values computed from `_patterns/06` and `_state/03c`.
3. **Structure** (from v239) — dead internal links, required sections, chapter-size caps against the ~35K-token discipline.
4. **Decay** — flag rows past their stale floors with **evidence** (row, last-touched wiki, wikis-since); **skip the ambiguous**; write **one** report; **remove nothing**.
5. `--write` only for mechanically derivable fixes (index table, counts). Never for prose.

Rung 1 and 2 alone would have caught the four drift instances the corpus has recorded about itself.

**C13 (optional, later).** If the corpus ever takes an MCP-registry subject (modelcontextprotocol/registry, Smithery, mcp.so), this ship is its **N=1 precedent** for the *"runtime-consumed registry + agent-callable package discovery"* watch axis (Verdict §3.1). Credit it then.

---

## D — Decisions / ADR lines

**D15 ⭐ Into the vault routine:** *"A consistency check between two views of one source is blind to what is missing from the source — pair every equivalence check with an inventory check that enumerates by a different rule."* Cite v240 §7.3 as the reference case.

**D16 ⭐ Into the vault routine (intake):** *"Do not settle a subject question on form-factor alone when the form factor is cheap to verify."* v237 dismissed this repo as *"not a subject"* on its genre label; the source held a registry API. Same shape as v216 → v236/v237/v239.

**D17 (hireui):** *"Automation establishes evidence; humans make decisions that cannot be undone."* The one-ship-apart evidence is in the corpus: **v239's `pr-review.mjs` auto-closed a substantive bug report**; v240's decay scan refuses to auto-remove an entry. Pair this with the standing **D14** (*an agent that can reach production must be gated at the tool, not the prompt*) and the RATIFIED candidate-LLM legibility ADR.

**D18 (hireui, dependency hygiene):** never commit a lockfile whose `resolved` URLs point at a mirror registry. v240 ships `registry.npmmirror.com` for 2 of 3 packages with `npm ci` in four workflows — integrity-hashed, so the exposure is availability and install-traffic visibility, not integrity, but it is unintended and invisible until someone reads the lockfile.

---

## E — Flags to the (egregiously overdue) audit

**E20.** The §3.1 **registry watch axis** — DEFERRED, N=1, credit-on-next-instance.
**E21.** **Pattern #16** — a striking but **non-qualifying** recurrence (not a framework; the manifest is not load-bearing). Recorded, revival declined; the audit should decline too, or restate the criterion.
**E22.** **#68 gains a second form-factor sub-variant in two ships** (v239 static host-app panel / v240 runtime registry) — they are complementary; reconcile the N-tally.
**E23.** **#57 — a new relation shape: mutual indexing** (the subject catalogues v236/v237/v239; the corpus had already named the subject in v237's Verdict).
**E24.** The **intake method note** (D16) — worth a routine amendment, not just a ship note.
**E25.** **#83 sub-mechanism question:** v239 and v240 are now a matched pair on *claims propagating downstream through a live dependency graph faster than anyone re-checks them* (a retracted benchmark; an unsubstantiated feature). Two instances, one ship apart, both caught by the corpus. Worth registering as a sub-mechanism.

---

## 🔴 Hard fences

- **Do NOT install any plugin from this list**, and do not treat a listing as a safety signal. The list says so itself: *"Being on this list is not a security review… Tool approvals don't sandbox plugin code."* No listed artefact is scanned — `probe-tarballs.mjs` only confirms a URL resolves (`GET bytes=0-0`).
- **Do NOT run `npm ci` in the clone.** Read-only. (Two of three packages resolve from a mirror registry.)
- **Do NOT cite "live token stats"** for `dsh-web-ui` — hand-verified absent from its live README; the list propagated it from the tagline.
- **Do NOT cite star/fork figures** as velocity (§37.4, mocked API). The commit/contributor numbers are git-derived and safe: 1,662 commits, 853 unique author emails, ~5 days.
- **Not a hireui component.** Nothing here ships into the product. B8/B10/D17/D18 are policy borrowings only.
- **Do not lean on this registry.** Bus factor 1 (`fkysly`, 243 commits, 86 of ~93 touching the machinery), 5 days old, serving a live API to a 967★ storefront and an agent tool.
