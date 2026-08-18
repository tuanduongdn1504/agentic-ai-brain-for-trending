# (C) deepseek-harness-desktop — Verdict

**Wiki v241** · 2026-08-18 · `anywhere-labs/deepseek-harness-desktop` · MIT · v2.0.1 (npm `dsh-plugin-desktop` latest **2.0.0**; tags `v0.1.0`, `v2.0.0`)
**Method:** ✅ SOURCE-CLONED full history · 16-agent workflow (0 errors, ~1.77M tokens, 549 tool uses, 639s) · every load-bearing claim hand-verified.

---

## Phase 0.9 — GOAL-ALIGNED INCLUDE 3/4

| Criterion | Call | Reasoning |
|---|---|---|
| **(a)** author is a structural peer to the operator | **FAIL** | `anywhere-labs` ("Creating awesome AI APPs", China, `dshdesktop.cn`, 3 public repos, **no listed members**); lead `t4wefan@qq.com`, with `Qiuner` (Fuzhou, independent full-stack dev). **NOT Anthropic**; no registered (a)-7 vendor-direct axis. §41 is decisive — and note the inherited history's 10 `@deepseek.com` addresses would not rescue (a) even if current, because (a) is about *Anthropic*, not any vendor. |
| **(b)** operational tool the vault could deploy | **MODERATE** — keys the tier ⚠️ *STRONG genuinely arguable* | A desktop client for a **rival** agent runtime; Claude appears only as a transitive `@anthropic-ai/sdk@0.91.1` in the lockfile. MODERATE for consistency with the v235→v240 DSH run. STRONG is arguable: the *architecture* (CI-enforced doc/structure gates, deny-by-default install scripts, provenance-at-divergence) is directly portable, and one finding lands squarely on a live vault defect. |
| **(c)** methodology-influence node | **STRONG** | The clearest of the run. It supplies (i) the **provenance-at-the-divergence-point rule** that corrects v240's own method, (ii) a **two-way inventory check implemented as working code**, and (iii) an `AGENTS.md`-goes-stale-while-the-machine-contract-advances case that is the vault's `C22–C27` disease exactly. |
| **(d)** in-corpus reference | **STRONG** | Cites **four** prior corpus subjects (v235 upstream/submodule, v236 dsh-TUI, v237 DSH-better-sidebar, v239 dsh-web-ui) — ties v239's widest `#57` fan-in — **plus** a new relation shape: its repository *is* v235's repository, re-purposed. |

**Tier:** **T4 Plugin/Extension** with a strong **T2 desktop-client** facet and a **T3 standards-draft** facet (`dsh-community-fabric`). Tier reviewable.

**§40:** operator-requested, goal-adjacent (agent-runtime substrate), (b) MODERATE+ → **GOAL-ALIGNED per operator direction.** No override consumed; no §35 pressure. The OFF-GOAL reading is recorded as the reviewable alternative (a desktop GUI for a rival model's runtime).

---

## Pattern outcome: **NO MINT** — the EIGHTH consecutive DSH decline, on new grounds

**Counts UNCHANGED: 46 confirmed / 11 CONFIRMED Library-vocab. §C live standalones 49 unchanged. Surface ≈56 unchanged.**

### The §C-mint alternative, RECORDED and DECLINED

*"Container-as-Plugin Desktop Shell — an installable desktop application that composes its own window/tray/terminal/update shell as an ordinary plugin of the agent runtime it launches, with the runtime pinned as an unmodified submodule behind a CI-enforced published-package boundary."*

**Declined on five grounds:**

1. ⭐ **Decisive external prior art, verified not assumed.** **Eclipse RCP/OSGi** — the official Eclipse plug-in-architecture article names the workbench UI itself as a self-extending plug-in contributing to its own extension points; Eclipse 1.0 shipped 2001-11-29, Eclipse 3.0 (2004-06-21) made the platform OSGi bundles. The space is further populated by **JupyterLab/lumino** (the shell is provided by a plugin) and **Theia** (DI-composed core). Adversarial verdict: **REFUTED**.
2. ⭐⭐ **The subject does not claim novelty.** `dsh-community-fabric/docs/research/` holds `mature-plugin-frameworks.md` **and `vscode-extension-model.md`** — they studied Eclipse, Chrome and VS Code and built on them. 「桌面本身也是「插件」」 is a **design commitment, not a priority claim.** Minting would over-claim *on the subject's behalf* — the discipline that killed the v211 PixelRAG mint.
3. **Form-factor-within-genre, ruled on twice.** **hermes-webui v227** (community front-end for someone else's agent — DECLINED) and **lobehub v222** (decisive: world-canonical ≠ world-first), plus **Codex-Dream-Skin v216** (a UI layer for a rival's tool is not a mintable capability class; §C vocab is capability-shaped).
4. **§28 anti-inflation** + the **DSH chain now EIGHT deep** (v216→v222→v227→v236→v237→v239→v240→v241) and **seven consecutive DSH-ecosystem ships** (v235→v241).
5. **Domain/packaging-not-capability** — the meetily v196 / TimesFM v193 / AIRI v210 discipline. Desktop packaging is a form factor.

→ Recorded as a **DEFERRED watch axis at N=1**, credit-on-next-instance.

### Instance-strengthening — RECORDED, NOT self-incremented

- ⭐ **The v236 watch axis (generalized to N=2 at v237) gains a strong candidate N=3.** v241 is a UI/presentation-layer plugin mounted in DSH — but structurally distinct: v236/v237/v239 are plugins you install *into* a DSH you already run; v241 is a product you install that *contains* DSH and composes itself into it. **N=3 would make that axis promotion-eligible. NOT self-executed — a promotion is an audit act** (the v232 rule; the v235 grok-build precedent).
- **v237's publish-your-own-extension-API axis → N=3** (`desktopProfiles` / `desktopPnpm`, generation-scoped, routed through the DSH CLI to preserve its authority).
- **pi v228's supply-chain-hardening exemplar → an independent instance** (`enableScripts: false` + a curated 5-package `dependenciesMeta` allowlist + 1,001 mirror-free resolutions). Arguably a cleaner instance than v240's partial third.
- **`#57` — a NEW relation shape: history-inheriting re-purposing** (see below). Prior shapes: dependency fan-in (v239), port (v207→v208), credited priority (v231→v232), host↔plugin (v235↔v236), mutual indexing (v240).
- **`#83`** two-sided: exemplary self-disclosure (Fabric's "no runtime, no SDK, enforcement not implemented"; the market's "these checks do not review the plugin or its dependency tree") against the patches disclosed only to agents.
- **`#66`** two-sided: the best lockfile hygiene of the run against an unsigned Windows installer and a third-party update domain.
- **`#81`**, **geti v213** committed cross-harness symlink, **`#19` 19a**.

### ⚠️ Flagged to the audit — a stale row this ship touches

The **v140 §C row** *"Graduated / Least-Privilege Tool-Exposure"* has sat at N=1 for ~100 wikis with a long-blown stale-watch. v241's Fabric RFC proposes an explicit **support → request → grant → enforcement** capability model — and **discloses that enforcement is not implemented**. That is *adjacent* but is a **proposal, not a shipped mechanism**, so I did **not** treat it as N=2. Recorded for the audit alongside v238's claim on the same row.

---

## The two findings that matter

### 1. ⭐⭐⭐ Provenance must be measured at the divergence point

The clone reports **12,637 commits, 69 days old, 52 authors, 2,219 commits from 10 `@deepseek.com` addresses, top author 41%.** All true of the **repository**; all false of the **product**.

One root commit (2026-06-10) whose first five messages are *"microkernel architecture"*, *"Yarn 4 workspaces"*, **"Vendor Cordis framework packages as source"** — DSH itself being born. **`packages/`, a directory that no longer exists, carries 8,103 commits.** 915 merges "from `deepseek-harness/`" vs **11** from "`anywhere-labs/`". Then **`4e3eb91`, 2026-08-15 01:07:13**, *"refactor(repo): isolate upstream and desktop workspace"* — **7,405 files deleted**, `.gitmodules` and `dsh-plugin-desktop/` created in the same commit.

**The product: 343 commits (307 non-merge) over ~3.8 days, ~6 authors, and ZERO `@deepseek.com` commits.**

> **THE RULE.** A clone's git metadata is authoritative about the repository, never the project. Where history is inherited, measure from the divergence point. **Detector:** find paths with heavy commit history that no longer exist in the tree; check the root-commit count; scan merge subjects for foreign orgs.

**This corrects v240's headline method** ("a clone carries authoritative git metadata") one ship after it was adopted. And it **exonerates the project**: the disclaimer is accurate, and the repo advertises no commit count anywhere.

⚠️ **Both assigned agents failed** — the reader was incoherent (25+22+3 ≠ 12,637, excused by an impossible claim about an empty submodule); the adversarial verifier then **CONFIRMED my own wrong framing** with correct arithmetic. **A verifier checks the claim you hand it; it does not reframe the question.** The answer came from hand-analysis.

### 2. ⭐⭐⭐ The inventory rule exists here as working code — where the index cannot see it

**`dsh-community-fabric/scripts/verify-docs.mjs` declares an explicit 33-file inventory AND walks the tree recursively** — enumerating **both ways**. That is exactly v240's derived rule, implemented, one ship later.

Those 33 files include a **4-RFC suite**. **`docs/README.en.md` — the self-described full documentation map — contains ZERO occurrences of "rfcs"** (hand-verified). ~25 files are absent from it. Fabric's own README indexes all four RFCs at lines 46–49.

**The workspace that solved the inventory problem is invisible from the front door**, because the top-level index is hand-maintained with no inventory check.

Counter-balance, and it is real: **67 relative markdown links tested across five index files — ZERO dead**, versus v240's `README.ja.md` broken on line 5 of both READMEs. And the recorded bilingual blob hashes **match**. Its failure is omission, not breakage.

**Plus:** `AGENTS.md` still calls the shipped ~18,748-LOC marketplace *"a private documentation scaffold [that] must not declare loadable DSH or package entry points"* — while `verify-docs.mjs` **flipped polarity in the same commit that added the runtime** (from forbidding `main`/`exports`/`dsh` to requiring them). The machine contract advanced as a state machine; **the agent-facing prose did not.** `CLAUDE.md` *is* an `AGENTS.md`, and `_state/03c-projects-v61-v183.md` holds entries through **v240**.

---

## Streak & governance

**Streak: v240 `GA:98` → `GA:99 · OG:13 [7 ov]`** — **22 consecutive GA** (v220→v241).
**§35 CLEAR** — window {v239 GA, v240 GA, **v241 GA**} = 0 OG. No override consumed (§40).

⚠️ **THE STANDING LEVER, now loud:** this is the **7th consecutive DSH-ecosystem ship** (v235→v241) and the **8th DSH-chain ship**. Seven consecutive NO-MINTs in one ecosystem. **The corpus is mining a two-month-old ecosystem while the ~v221 audit is ~20 ships overdue** (last audit v212; v213–v241 all shipped). The pilot half of the lever also still stands: **zero piloted.**

⚠️ **A governance note this ship owes itself — and it is now a PATTERN, not an incident.** v236's Deep Dive called this repo *"a rival UI-layer plugin (`dsh-desktop`)"* and used it to argue dsh-TUI's anchor was *"weak, undistinctive."* Identity confirmed: npm `dsh-plugin-desktop` ships **`bin: dsh-desktop`**. That characterization **materially understates** a three-workspace desktop product with a pinned-upstream distribution model, ~46K LOC, seven verify gates, a 4-RFC draft standard, and 12 bilingual decision records.

That is the **second consecutive ship to falsify an earlier ship's dismissal-by-label**:
- **v237's Verdict** ruled v240's subject *"Ecosystem-formation data-point, not a subject"* → v240 shipped it and found infrastructure.
- **v236's Deep Dive** ruled this subject *"a rival UI-layer plugin"* → v241 ships it and finds a distribution architecture.

→ **v240's D16 method note is confirmed as a recurring intake failure, not a one-off.** *Do not let a genre or form-factor label settle a subject question that only source can settle — especially when the source is one clone away.* This is the most valuable governance output of the ship and belongs in the routine.

---

## Pilot verdict: 🔴 **read-and-borrow. Install NOTHING. NOT a hireui component.**

**Never:** install the desktop app on a machine that touches candidate data. The update path polls and downloads installers from **`dshdesktop.cn`** with no GitHub Releases fallback and **format-only** artifact validation (DMG magic / PE header), and **Windows builds carry no code-signing configuration** while the NSIS installer sets `allowElevation: true`. Telemetry is **opt-out, default-ON**. Do not treat any DSH catalogue listing as a safety signal — **nothing in this ecosystem scans plugin code**, and both the publisher (v240) and this consumer say so plainly.

**Borrow, at zero risk:** the provenance-at-divergence rule; the two-way inventory check; `enableScripts: false` + a curated build allowlist; the install-gate list (reject lifecycle scripts, verify integrity, require a repository backlink, pin exact stable versions); the Electron hardening defaults; and the `.gitattributes` + committed-blob-hash pairing that makes bilingual records line-ending-proof.

⭐ **A1 → C12 → B7** — read `scripts/verify-layout.mjs`, `dsh-community-fabric/scripts/verify-docs.mjs`, `AGENTS.md` and the market's install service (~40 min, zero install) → **build `verify-vault-docs`**, now with **three** pieces the vault lacked: v240's prose-vs-code equivalence, v240's inventory rule **as working code**, and v241's **provenance-at-divergence** check → adopt v240's five-rule decay doctrine as the retire-pass policy. **Seven consecutive ships have now handed over the parts.**

---

## Bottom line

**Blunt:** the numbers on this repository are a trap, and I walked into it before walking out. A clone says twelve thousand commits, sixty-nine days, fifty-two authors, a fifth of them at DeepSeek — and every one of those facts belongs to DeepSeek Harness, not to this product. One command found it: a directory called `packages/` with eight thousand commits and no files, and a single commit on 15 August that deleted seven thousand four hundred files and put upstream back as a submodule. The product underneath is three days and eight hours old, six people, three hundred commits. It is also, in the parts that exist, better engineered than most of what this run has looked at: install scripts denied by default with five deliberate exceptions, a thousand-package lockfile with no mirrors, a marketplace that refuses any package carrying a `postinstall`, and a CI check that makes "we don't modify upstream" a property of the build instead of a sentence in a README.

And then the same failure the vault has, one directory up from where the fix already lives. A workspace whose doc-checker enumerates its files twice — once declared, once by walking the tree — which is exactly the rule I wrote down last ship. Its four RFCs are the most formal thing the project has produced. The top-level index, which calls itself the full documentation map, does not contain the string `rfcs`. The `AGENTS.md` the agents read still calls an eighteen-thousand-line shipped marketplace a documentation scaffold, because the machine contract was updated in the same commit as the code and the prose was not.

**Take the rule, not the app: measure provenance at the divergence point, and never let a genre label settle a question a clone can answer. Two ships in a row have now proved the second one the hard way.**
