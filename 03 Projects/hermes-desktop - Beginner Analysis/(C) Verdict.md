# (C) Verdict — hermes-desktop (Hermes One) — v268

**`fathah/hermes-desktop`** · MIT · Electron · 1301 commits / 82 authors / 50 tags / 4.1 months · HEAD `3aaadb01` (2026-08-06)
**GOAL-ALIGNED INCLUDE 3/4** — (a) FAIL · (b) STRONG *(MODERATE reviewable)* · (c) STRONG · (d) STRONG
**NO MINT.** Counts **46 / 12 UNCHANGED** · §C-1 **12** unchanged · §C-2 **39** unchanged
**Streak `GA:124` → `GA:125 · OG:13 [7 ov]`** — 48 consecutive GA (v220→v268) · **§35 CLEAR** ({v266, v267, v268} = 0 OG) · no override

---

## The one-line verdict

A community Electron desktop app that installs, configures and drives **someone else's** open-source agent — and, in passing, the corpus's first subject to carry a **third-party productisation of this vault's own founding pattern**: a 597-edge repo-resident knowledge graph with a link/code-ref validator, which is **immaculate**, and which **nothing has ever enforced**.

---

## What is actually new here

**1. ⭐⭐⭐⭐⭐ The first clean documentation-integrity result in 268 subjects — measured across history, not at HEAD.**
I re-implemented the four rules `lat check` documents and ran them over **25 commits spanning the graph's entire life** (2026-06-17 → 2026-08-06). **Dangling wiki links: 0 at every probe. Dangling `@lat:` code refs: 0 at every probe** — while the graph grew from 7 edges to **597 links + 79 bidirectional prose↔code refs**. After v239's 97 dangling pointers and v265's 97 citations into a directory that never existed, and after v267 became *"the first subject to pass the v240 inventory check in both directions"*, this is a far harder test passed continuously.

**2. ⭐⭐⭐ And the only rule ever broken is the one whose breach breaks nothing.** Two leading paragraphs exceed the documented 250-character budget (256 and 258 bytes), introduced 2026-06-19 and ~2026-07-07, **still present 48 and 30 days later** across ~500 commits. Same tool, same checklist, no gate for either — and the split is clean: **a dead `[[link]]` announces itself to the next agent that follows it; a 256-character paragraph announces itself to nobody.**

**3. ⭐⭐⭐⭐ The coverage finding, which is the one that matters.** Of the 169 commits touching `lat.md/`, **149 (88.2%) are the owner's**; 20 come from five outside contributors — so the convention *did* travel. But **`pmos69` is the #2 contributor to this repository — 187 commits, 159 touching `src/` across `shared`, `renderer`, `main` and `preload`, plus tests — with ZERO commits touching the knowledge graph.**
⇒ **An ungated documentation convention did not produce WRONG documentation. It produced INCOMPLETE documentation — and incompleteness is the one failure mode no link-checker can see.** `lat check` validates every edge that exists and is structurally blind to the subsystem nobody wrote down. **This is v240's inventory rule arriving from the opposite direction, and now confirmed empirically.**

**4. ⭐⭐⭐ The gate ladder gains a new rung: the gate that was never switched on.** `require-code-mention: true` is `lat`'s only enforcement primitive. It appears **12 times in the repository and all 12 are inside documentation about the feature**; **zero of the 29 graph files have frontmatter at all.** The cost is exact: `remote-dashboard-oauth.md` declares 12 test specs, **10** have a test, and **`Atomic first-run connection`** and **`Raw gateway classification`** do not. One line of frontmatter — a feature documented four times over in this very repo — would have named exactly those two.

| ship | shape |
|---|---|
| v261 | the claim without the test |
| v262 | the gate that cannot fail |
| v263 | the test without the gate |
| v265 | the gate that prints `PASS` on the file it exists to block |
| v267 | the number computed, displayed, never compared |
| **v268** | **the gate that was never switched on** |

**5. ⭐⭐⭐⭐ THE SHIP'S SENTENCE — and it supplies the mechanism v267 was missing.**
The same repository contains the best example in 268 subjects of a discipline that *persists*: `src/main/secrets/securityInvariants.test.ts:4-24` takes **three real security bugs found in review**, generalises each into a **named permanent invariant (INV-1/2/3)**, encodes them as property-based tests, writes down which bug taught which invariant, and states *"a red line here is a security regression, not a style nit."* Four source files, nine test files, `fast-check`, and **CI runs it on every PR**.

The same person built both. The ungated one is immaculate. **The difference is not care — it is who the next reader is.** The invariant suite's next reader is `vitest`, which fails loudly and blocks the merge. The knowledge graph's next reader is an agent in a future session, which will read whatever is there and never object.

⇒ **A gate exists where a reader can refuse. Agents don't refuse.**
That is why v267's *"the discipline stops where the artifact stops being code"* is true — and this is the mechanism underneath it.

**6. ⭐⭐⭐ A community client that verticalised into a competing platform.** NousResearch shipped its own official *"Hermes Desktop"* on **2026-06-02**; this project's first commit is **2026-04-02**, 61 days earlier. On **2026-06-03 — the next day** — `1a6317d "complete Hermes One branding"` renamed the product. It now runs **seven `hermesone.org` subdomains**: its own inference gateway (listed *first* in the provider picker), an MCP registry, an analytics endpoint, a credits console — plus accounts, cloud agent sync, a token wallet and a `$HD` token. ⚠️ **The causal link between the rename and the official release is inferred from a one-day gap; no in-repo statement gives a reason.**

---

## What is genuinely excellent

- ⭐⭐⭐ **`securityInvariants.test.ts`** — the best twenty lines in the repository and the most portable artifact in it (§3)
- ⭐⭐ **Electron hardening**, safe at all five window sites, **enforced centrally** in `src/main/security.ts:93-97`, with `webviewTag: false` specifically in the sudo/askpass credential windows
- ⭐⭐ **The wallet cannot send funds.** Zero hits for any signing or sending primitive across `src/`, `tests/`, `scripts/`. Mnemonics encrypted with Electron `safeStorage`, **fail-closed** if unavailable, and the renderer never receives even the ciphertext. The exact inverse of the v231/v232/v265 broken-auth triad. **And the pattern was deliberately propagated** to the account-token store (`account-store.ts:11`) — a discipline that *did* travel.
- ⭐⭐ **`lat.md/analytics.md`** — removed a third-party SDK (PostHog) and tightened CSP on the way out; enumerates exactly what is collected and what never is; **silently disabled in builds from source**; explains *why* it is off on the dev server, with the mechanism
- ⭐⭐ **`worldActions.ts`** — the model→3D-world bridge is a **closed allowlist derived from one array**, so the prompt cannot advertise an ability that does not exist; unknown verbs inert; malformed input dropped fail-closed, with the reason written down
- ⭐ **CI gates typecheck and test on every PR** (1,841 test functions), and lint's non-gating status carries a **written reason**
- ⭐ **Honest disclosures**: the non-affiliation statement, the `--skip-setup` disclosure, the unsigned-Windows and unsigned-RPM warnings, and three `it.skip`s whose reason is documented in-file

## What is weak

- 🔴 **`installer.ts:942`: `curl … | bash` from a moving `main`, no checksum, no signature**, shell profile sourced first. This — not the wallet — is the risk surface.
- 🔴 **0 of 34 GitHub Actions are SHA-pinned**; both release workflows carry top-level `contents: write`; `ci.yml` has no `permissions:` block. The contrast with v267 (12/12 pinned, written threat model, read-only default) is stark.
- ⚠️ **`.husky/pre-commit` and `pre-push` exit 0 unless the branch is `release`** — inert on `main` and all 90+ feature branches. **D34 at N=2.**
- ⚠️ **Telemetry is opt-out, on by default** in official builds — disclosed, but a default worth naming.
- ⚠️ **The README never mentions that a first-party desktop app exists.** v267's silence-is-the-finding at N=2 — but **materially milder**, and it should be said so: the disclaimer exists, the upstream is linked, the installer is credited. v267's subject implemented a competitor's protocol namespace with zero mentions of it anywhere; this one merely doesn't advertise a rival.
- ⚠️ **`CLAUDE.md` and `AGENTS.md` are byte-identical copies, not v243's symlink** — a latent hazard only, because only 2 commits in 1301 ever touched either and they have never diverged. Safe because nobody edits them, which is not safe by construction.
- ⚠️ **A hash-based staleness detector detects EDITS, not OBSOLESCENCE** (§7): `lat_init.json`'s recorded hashes match exactly, while `CLAUDE.md:32` still explains an API-key requirement `lat` v0.12.0 removed on 2026-07-15. Low severity — the instruction is conditional and harmless — but the structure is the point.
- ⭐ **The README undersells itself**: it claims an *"English locale … ready for community translations"* while **12 locales** ship, including two RTL. v267's refinement at N=2: **claims verifiable from inside the repo drift toward underselling; the inflated ones live where the repo cannot check them.**

---

## Mint reasoning, in one paragraph

**NO MINT.** The form factor is a genre ruled on four times — **v222** lobehub (world-canonical, not world-first), **v227** hermes-webui (*a community web front-end for this same upstream* — "an adjacency, not an instance"), **v236** dsh-TUI (presentation-not-capability), **v241** dsh-desktop (an Electron client for a general agent runtime it also launches). Two candidate rows were tested and **both declined on their own written definitions** — the fourth-plus consecutive ship where reading a row's definition prevented a false N: **CONFIRMED #22** *"Tauri-Desktop Management-GUI for a **Coding** Agent"* triggers its own non-Tauri generalisation clause here but is scoped to coding agents, and Hermes Agent is a general personal agent; **C42** *"Agent-First Codebase-Documentation **Generator**/Maintainer"* requires an agent that authors autonomously via a git-diff-scoped CI loop, and `lat.md` authors nothing — it **validates and retrieves**. And decisively: **`lat.md` is a dependency, not the subject** (the v181 cortex-hub discipline). ⭐ **Recorded for the audit, not self-executed:** (i) hermes-desktop is the strongest candidate yet for generalising **#22** on *both* axes; (ii) a **C42 validate-vs-generate** watch axis; (iii) a business-model alternative near **LV-C2** — *a client author monetising someone else's OSS by becoming its default provider*, which is a genuine twist on v78's *author monetising their own*.

**NON-CLAIMS.** NOT **#57** — no corpus subject is a dependency. Hermes Agent and Superpowers are corpus **entities**, which is **convergence, not recursion** (the v264 precedent by name), and `lat.md`'s publication under **`vercel-labs`** — the same org as corpus subject **v68 `zero`** — is an **org-level coincidence**, explicitly declined as a #57 because inferring recursion from the shape of a namespace is precisely the v267 error. NOT **#52** (stars page-stated, §37.4). Not a new top-level pattern. **Nothing installed, built or executed; no third-party service contacted beyond public web pages.**

---

## Pilot

**⭐ READ-AND-BORROW. Do not install the app.** Two things are worth taking, and one is worth evaluating:

1. **⭐⭐ Take the security-invariant suite pattern** into hireui — every past review finding becomes a named permanent invariant with the bug→invariant mapping written down, property-tested. It composes directly with the standing **BOLA authorization audit**.
2. **⭐⭐⭐ Take the coverage lesson into the vault.** v267 asked for derived counts; v268 supplies the missing half. Integrity is the cheap half; **coverage is the half that rots silently.** For every `vNNN` in the shim, assert an entry in `_state/03c`; for every entry in `03c`, assert the shim references it — **both directions, per D15** — and wire it into `(C) proposed-verify-vault-inventory.sh`, the nine-clause script **v263 found nothing invokes**.
3. **⭐⭐ Evaluate `lat.md` itself**, on a scratch repo, fenced with `install-snapshot` + `npm-security-check`. It is the closest thing yet to a productised version of this vault's founding pattern, from a highly credible author (Yury Selivanov — CPython `asyncio`, ex-CEO of Gel/EdgeDB, now at Vercel). The two questions that decide it: does it survive `_state/03c`'s 2.3 MB single-line entries, and does `@lat:`-style bidirectional linking work when the "code" is prose?

---

**Blunt:** *this is the best documentation-integrity result the corpus has ever measured, and it was produced with no gate at all — which is the most uncomfortable finding of the run, because five ships in a row have been about building gates. Five hundred and ninety-seven cross-references and seventy-nine prose-to-code links, clean at every one of twenty-five probes across seven weeks, held up by one developer's habit and a hook on his own laptop. And in the same repository, the one enforcement flag the tool offers — documented four times over, one line to switch on — is used in zero files, which is why two of twelve declared test specifications have no test. The two things sit side by side and they are not a contradiction. The links held because a broken link fails in the face of the next agent that follows it. The missing frontmatter and the missing coverage and the second-biggest contributor's hundred and fifty-nine commits that appear nowhere in the graph cost nothing, ever, to anyone, because the only reader who would notice is a machine that was never asked. So the question this ship puts to you is not "did you build a gate?" — it is narrower and worse. This vault's reader is an agent. Every count in it, every streak, every C-marker, is read by something that cannot refuse. That is not a hypothetical: the v259 audit found a count wrong, twice, and the thing that found it was a person deciding to look. Which of your numbers has a reader that can say no?*
