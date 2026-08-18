# (C) deepseek-harness — Pilot Methods Menu (v242 revisit)

**Standing posture: READ-AND-BORROW. INSTALL NOTHING.** Every option below is zero-install unless flagged. The subject is a developer-preview runtime from a competitor lab, closed to external PRs, with telemetry default-ON and no evaluation harness. Nothing here is a hireui component.

---

## ⭐ THE RECOMMENDED PATH — A1 → C12 → B7 (≈50 minutes, zero install)

**Eight consecutive ships have handed the vault the parts for one tool. This ship completes the set.**

### A1 — Read four files in the clone (≈25 min)
1. `CONTRIBUTING.md` (23 lines) — the governance sentence that produced the entire six-ship plugin chain.
2. `pnpm-workspace.yaml` — `strictDepBuilds` + `allowBuilds` (5 allow / **3 explicit deny, with reasons**) + `minimumReleaseAge` exclusions. The best supply-chain comment block in the run.
3. `docs/tool-catalog.md` — graduated least-privilege tool exposure, **implemented**: high-privilege toolsets absent from every shipped tree, activation gated on capability injection.
4. `docs/testing.md` — *"Product-visible plugins require a non-unit REAL-composition test"*, the doctrine behind ~299K lines of tests.

### C12 — Build `verify-vault-docs` (the payoff)
The vault's own documentation-integrity disease (C22–C27 stale rows; `_state/03c-projects-v61-v183.md` holding entries through v242 under a `-v183` label) now has **five** borrowed mechanisms:

| Piece | From | Rule to implement |
|---|---|---|
| Prose-vs-code check | **v240** | Fail the check when a prose list drifts from the code constant it documents |
| **The inventory rule** | **v240** (+ v241 as working code) | Enumerate **both** ways — a declared inventory **and** a recursive walk — and diff them. A consistency check between two views of one source cannot see what is *missing* from the source |
| Provenance at divergence | **v241 (D19)** | Measure a subject's provenance from its divergence point, not its repository root |
| **Language-basis declaration** | **v242 (D23)** ⭐ NEW | Every count over files or lines must state its language basis; check for `.zh.md` / `.i18n.yaml` siblings before quoting any doc count |
| **A pairing merge driver** | **v242** ⭐ NEW | DSH registers `merge.dsh-translation-pairing.driver` to keep `.md`/`.zh.md`/`.i18n.yaml` triples in sync — the *mechanism*, not just the rule |

**Concretely, three checks worth writing first:**
- **The label check** — assert every `_state/*.md` filename's version range matches the entries it actually contains. This alone catches the standing `-v183` drift.
- **The count check** — assert every numeric claim in `CLAUDE.md` that references a file count is regenerable by a command, and record the command beside it.
- **The staleness check** — flag §C rows whose N has not changed in more than N wikis (the C22–C27 backlog), using **v240's decay doctrine**: *flag never remove · skip the inconclusive · evidence not doubt · one issue updated in place · removal is human.*

### B7 — Adopt the decay doctrine as the retire-pass policy
Then run the retire pass the audit has deferred since v182.

---

## Option 2 — Apply D25 to the vault's own back catalogue (≈30 min, zero install, high value)

**The finding:** v235 disclosed "not source-cloned" honestly, then let four unverified third-party claims carry its entire risk assessment. Three failed.

**The action:** grep the corpus for ships that disclose no clone **and** carry critical caveats sourced from commentary rather than code. Mark those caveats as **inherited, unverified**. The vault already has the vocabulary — it just never applied a confidence discount to hearsay.

```bash
grep -rn "NOT source-cloned\|not source-cloned" "_state/03c-projects-v61-v183.md"
```

**Why it matters:** the corpus's most quotable risk statements are exactly the ones most likely to be inherited. Two ships in a row have now found a propagating unverified claim (v239's retracted 98/99, v240's "live token stats", v241's "4,120 plugins") — **and this ship found the vault propagating its own.**

---

## Option 3 — Borrow the supply-chain posture into hireui (≈20 min read, then a real change)

Three independent instances now agree — **pi v228**, **v241's desktop**, and **this host** — on one posture:

1. **Deny install scripts by default**, then allow-list with a written reason per exception. (`pnpm` ≥10: `strictDepBuilds` + `allowBuilds`; Yarn 4: `enableScripts: false` + `dependenciesMeta`; npm: `--ignore-scripts` + explicit rebuilds.)
2. **A release-age cooldown** (`minimumReleaseAge`) with named, justified exclusions — the single cheapest defence against a freshly-compromised package.
3. **Exact pinning + a committed lockfile**, and audit it for mirror resolutions.

**hireui action:** add the deny-by-default gate and a release-age cooldown to hireui's package manager config, and write the *reasons* inline the way DSH does. This is the third consecutive ship to hand over the same playbook; it is overdue.

---

## Option 4 — The eval gap as a hireui design rule (≈15 min, spec-only)

The chain's structural hole, stated plainly: **the host ships no evaluation harness, the catalogue checks metadata, the installer checks identity — so nothing measures whether a plugin makes the agent worse.**

**The transferable rule, and it composes with the RATIFIED candidate-LLM legibility ADR:**

> Any component that can change model-visible input to a hireui LLM path — a prompt template, a tool schema, a retrieval source, a plugin — **must ship with an eval that gates its own change.** Identity checks (integrity, pinning, provenance) are necessary and are **not** sufficient. Verify effect, not just origin.

Pair with **v233's fails-closed eval gate** and **v238's** finding that a ~9KB tool-catalog injection destroyed a measured behaviour: *tool surface is a reasoning variable, not just a token cost.*

---

## Option 5 — The `worktree/` + `codex/` development workflow (≈15 min, observation only)

Of 1,008 PR merges: **`worktree/` 216** and **`codex/` 211** are the two largest branch prefixes (`claude/` = 3). The project runs a worktree-per-task workflow with agent-created branches namespaced by tool.

**Worth borrowing:** the **branch-prefix convention as durable provenance.** A `codex/`-prefixed branch records the tool in every merge commit subject forever — more durable than v239's PR-form field. If the vault ever wants to know which ships were built with which harness, encoding it in the branch name costs nothing and survives.

⚠️ Do **not** over-read it: a prefix marks branch tooling, not authorship of the code.

---

## Explicitly NOT recommended

| Action | Why not |
|---|---|
| `pnpm install` / running `dsh` | Developer preview; `postinstall`; telemetry default-ON; PRC-default egress; no eval harness. Read the source instead — it is all public. |
| Installing any `dsh-plugin` | **Nothing in the ecosystem reviews plugin code** — verified across host, catalogue (v240) and installer (v241). A listing is not a safety signal. |
| Adopting dsh as a hireui runtime | Closed to external PRs → no upstream recourse; competitor-lab default models; breaking changes promised in bold. |
| Citing its scale or popularity figures | "1,386 records" → 693. "~170K doc lines" → ~90.9K English. Stars are page-stated (§37.4). |
| Citing the retired caveats | "~19% compatibility", "~10× tokens", "context-duplication bug" — no in-repo basis / fixed before rc.5. |

---

## Clone location (this session)

```
/private/tmp/claude-501/-Users-Cvtot-KJ-OS-Template/d4e5c492-cc2f-4b8f-89ad-710b63abe0dd/scratchpad/dsh-host
```

201MB, full history, HEAD `99f6f02fecdb7dff40c3fbc9470f5907c29f74ca` (= v241's recorded submodule pin). Scratchpad is session-scoped — re-clone if needed:

```bash
git clone https://github.com/deepseek-ai/deepseek-harness.git
```

---

## Suggested next action

Run **A1 → C12 → B7**: read the four files, then build `verify-vault-docs` with the label check first — it catches the `-v183` drift the vault has flagged in three consecutive ships and fixed in none.
