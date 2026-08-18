# (C) deepseek-harness-desktop — Pilot Methods Menu

**Wiki v241** · 2026-08-18 · 🔴 **Install nothing. Read-and-borrow only.** Not a hireui component.

---

## A — Read (zero risk, ~40 min total)

| # | Action | Why |
|---|---|---|
| **A1** ⭐ | Read four files from the clone: `scripts/verify-layout.mjs` (136 lines), `dsh-community-fabric/scripts/verify-docs.mjs` (144), `AGENTS.md` (2.4 KB), `dsh-community-market/src/install/service.ts` install-gate section. | The highest-density doc-integrity + supply-chain machinery of the whole DSH run. Zero install. |
| A2 | Read `.agents/notes/implemented/process/2026-08-15-pinned-upstream-and-isolated-yarn-workspace.md` and `architecture/2026-08-15-windows-electron-acl-runner.md`. | The best-written decision records in the run; the second explains *why* upstream cannot use `CREATE_NO_WINDOW`. A template for lazy-ADR practice. |
| A3 | Read `dsh-community-fabric/docs/rfcs/0001` and `0004`. | A capability-negotiation model (support→request→grant→enforcement) and a provenance/validation/effect-ledger design — with enforcement honestly marked unimplemented. |

## B — Borrow into the vault / hireui (low risk)

| # | Action | Why |
|---|---|---|
| **B7** ⭐⭐ | Adopt **provenance-at-the-divergence-point** as a routine rule, and add the detector to the wiki method: (1) `git rev-list --max-parents=0 HEAD \| wc -l`, (2) look for heavy-history paths that no longer exist, (3) scan merge subjects for foreign org names, (4) report product-era counts, not repository counts. | **This corrects v240's own headline method.** Without it, every future source-cloned ship can publish a parent project's numbers as the subject's. |
| **B8** ⭐ | Write the **doc-integrity contract** into `CLAUDE.md` with all three pieces now available: v240's prose-vs-code equivalence, v240's **inventory rule** (v241 supplies working code for it), and v241's **divergence** check. | The vault's `C22–C27` disease. Seven consecutive ships have handed over parts. |
| B9 | Lift the install-gate checklist into hireui's dependency policy: reject packages declaring `preinstall`/`install`/`postinstall`/`prepare`; verify integrity hashes; require a repository backlink matching the registry manifest; pin exact stable versions (no ranges/tags/prereleases). | A concrete, already-implemented policy — and it is the discipline the project applies to *itself* (`enableScripts: false` + a 5-package allowlist). |
| B10 | Pair `.gitattributes` (`* text=auto eol=lf`) with **committed-blob** hashing (`git rev-parse HEAD:<path>`) for any vault integrity record. | Makes records line-ending-proof across hosts. Fixes v240's CRLF defect from both sides. |
| B11 | Adopt the Electron hardening defaults as a reference if hireui ever ships a desktop surface: `contextIsolation: true`, `nodeIntegration: false`, `sandbox: true`, `webSecurity: true`, minimal preload, strict CSP, no remote `loadURL`, crash upload off. | Correct-by-default, verified in source. |

## C — Build (the payoff)

| # | Action | Why |
|---|---|---|
| **C12** ⭐⭐⭐ | Build **`verify-vault-docs`** — the `C22–C27` retire pass, mechanised. Three checks: (1) **inventory** — enumerate `_state/`, `_patterns/`, `_goals/`, `03 Projects/` by directory walk and diff against every index that claims to list them (this catches `03c-projects-v61-v183.md` holding v240); (2) **prose-vs-code** — fail when a stated count/label disagrees with the derived one; (3) **link** — every relative link resolves. Adopt v240's decay doctrine as policy: *flag never remove · skip the inconclusive · evidence not doubt · one issue updated in place · removal is human.* | v241 supplies the missing piece as **working code** (`verify-docs.mjs` enumerates declared-list AND recursive-walk). The vault has been running a two-views-of-one-source check on itself for fifty wikis. |

## D — Rules to record

| # | Rule |
|---|---|
| **D19** ⭐ | **Provenance is measured at the divergence point.** A clone's git metadata is authoritative about the *repository*, never the *project*. Inherited history (fork/graft/re-purposing) makes commit counts, author counts and "age" describe the parent. |
| **D20** ⭐ | **A genre or form-factor label must never settle a subject question that source can settle.** Confirmed as a recurring intake failure: v237 dismissed v240's subject on its genre; v236 dismissed v241's subject as "a rival UI-layer plugin." Both were wrong on the facts, and both were one clone away from being checked. |
| **D21** | **An adversarial verifier checks the claim you hand it; it does not reframe the question.** R15 confirmed a false framing with correct arithmetic. Verify the *question*, not only the *claim*. |
| **D22** | **The agent-facing prose is the artifact most likely to go stale**, because machine contracts get updated in the same commit as the code and prose does not. Tie the prose to an inventory or it will drift. (`AGENTS.md` here; `CLAUDE.md` in the vault.) |
| D23 | Third-party directory figures are unreliable: this subject's stars were stated as 13.2k / 11,974 / 494 across three sources, and its own README inflated a peer's plugin count (4,120 vs the peer's stated 3,100+). Second instance of the v236 directory-metadata finding; third consecutive ship republishing a wrong downstream claim. |

## E — Audit flags

- **E26** The **v236 UI-layer-plugin watch axis** has a strong candidate **N=3** here → promotion-eligible. **Not self-executed** (promotion is an audit act).
- **E27** **v237's publish-your-own-extension-API axis → N=3.**
- **E28** **pi v228's supply-chain-hardening exemplar** gains an independent instance (`enableScripts: false` + curated allowlist + mirror-free lockfile).
- **E29** The stale **v140 §C row** (*Graduated / Least-Privilege Tool-Exposure*, N=1 for ~100 wikis): Fabric's capability model is **adjacent but a proposal with enforcement unimplemented** — recorded, **not** counted as N=2. Decide alongside v238's claim on the same row.
- **E30** **`#57` gains a new relation shape** — *history-inheriting re-purposing* — the deepest structural relation in the corpus.
- **E31** ⚠️ **Seven consecutive DSH-ecosystem ships (v235→v241), seven consecutive NO-MINTs, and the ~v221 audit is ~20 ships overdue.** Vary the domain or audit.

---

## 🔴 Hard fences

1. **Do not install the desktop app**, and never on a machine touching candidate data. Updates poll and download installers from **`dshdesktop.cn`** with **no GitHub Releases fallback** and **format-only** validation (DMG magic / PE header) — not signature or digest verification against a trusted manifest.
2. **Windows builds have no code-signing configuration** while NSIS sets `allowElevation: true`. macOS is hardened + notarized; Windows is not signed.
3. **Telemetry is opt-out, default-ON** — only `DSH_TELEMETRY_DISABLED` (non-empty) disables the upstream `session-telemetry-otel` plugin.
4. **`electronFuses: { runAsNode: true }`** — the packaged binary can be driven as plain Node. Plausibly required by the architecture, but it weakens the notarized/hardened posture.
5. **A catalogue listing is not a safety signal.** Nothing in this ecosystem scans plugin code — the publisher (v240) and this consumer both say so explicitly.
6. **Do not cite "12,637 commits / 69 days / 52 authors"** as facts about this product. They belong to DeepSeek Harness. The product is ~3.8 days old with 307 non-merge commits.
7. **Do not cite the "4,120 plugins"** figure from its Related Links table (the target repo states 3,100+), and cite **no** star figure as verified (§37.4).
8. **Do not repeat** the domain-registrant company name an agent reported — **UNVERIFIED**.

---

**Suggested next action:** **A1 → B7 → C12.** Read the four files, adopt the divergence rule into the routine, then build `verify-vault-docs` — and rename `_state/03c-projects-v61-v183.md` while you are in there, because it holds entries through v241 now.
