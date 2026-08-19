# (C) Deep Dive — `cathrynlavery/diagram-design` (v250)

> **Wiki v250** · analysed 2026-08-19 · MIT · HEAD **`5f1b6dd`** ("feat(line): add slopegraph variant for change between two states (#106)")
> **Source verified THREE times** — two independent `git clone`s + one `codeload` tarball, **335 files each, byte-identical, zero diffs**. Exceeds the source-clone-twice discipline (two transports, not just two fetches).

---

## 0. What it is, in one paragraph

A Claude Code / Codex / Pi **agent skill** that makes diagrams. You ask for an architecture sketch or a quadrant; it picks one of **28 visual types**, writes a single self-contained `.html` file with inline SVG and CSS, and applies an opinionated "editorial" design system — one accent colour, three named fonts, 1px hairlines, no shadows, every coordinate divisible by 4. It can read your website and convert your brand into diagram tokens in about a minute. It can redraw existing `.drawio` and Mermaid sources at a chosen format, size, detail level and audience. The GitHub description sells it as *"27 editorial diagram types for Claude Code. Self-contained HTML + SVG. No shadows, no Mermaid-slop."*

The interesting thing is not the diagrams. It is that a designer-founder wrote **11,305 lines of Python** to check them.

---

## 1. Identity and provenance (source-verified)

| Fact | Value | Provenance |
|---|---|---|
| Repo | `cathrynlavery/diagram-design` | cloned ×2 + tarball |
| Licence | MIT | `LICENSE` |
| HEAD | `5f1b6dd` | `git log` |
| Commits (main) | **114** | `git rev-list --count HEAD` |
| Commits (all refs) | 125 | `git rev-list --count --all` |
| Git roots | **1** | `git rev-list --max-parents=0` |
| Tracked files | **335** | `git ls-files` |
| Repo size | 13 MB | `du -sh` |
| Plugin version | **2.5.6** | `.claude-plugin/plugin.json:4`, `.codex-plugin/plugin.json:4` |
| Stars / forks / watchers | 22.8k / 1.4k / 77 | ⚠️ **page-stated only** — §37.4, the GitHub API is mocked in this environment → **NOT a velocity claim** |
| Trendshift | repository 26141 | README badge |

**File composition:** 110 `html`, 87 `svg`, 62 `md`, 31 `py`, 30 `png`, 5 `yml`, 4 `json`, 2 `mmd`, 1 `txt`.

**Not a solo project.** `git shortlog -sne --all` shows **20+ contributors**:

- Cathryn Lavery — **69** commits across two identities (40 as `cathryn@bestself.co`, 29 as the GitHub noreply address)
- Praveen Bishnoi — 16
- Matt Van Horn — 8
- then a long tail: `buildnwrite`, `Mr-Neutr0n`, `0xDarkMatter`, `ActArtech`, Vitalii Filiuchkov, Daan Balm, Ngo Quoc Viet, Saveena Solanki, Steven Nkeneng, and ~7 more at 1 commit each.

⚠️ **Counting note (vault rule D26/D27):** the two Lavery identities must be summed. Counting only the `bestself.co` address understates her contribution by 29 commits — 42% of her total.

**Author.** Cathryn Lavery: founder of **BestSelf Co** (the Self Journal — $322K on Kickstarter, Inc 500 2019, endorsed by Daymond John, >$45M in product sold, acquired 2022, **repurchased by her in 2024**), writes at **littlemight.com**. Trained as an **architect** before e-commerce. Not an Anthropic employee; not a software engineer by training.

⚠️ **Criterion (a) is a FAIL and nothing rescues it** (routine §41): a disclosed individual who is not Anthropic and not a registered vendor-direct source answers (a) NO. Notability is explicitly not an (a) signal. The *interesting* fact — a non-engineer founder authoring one of the most-starred Claude Code skills — is a corpus-knowledge data-point, not a criterion pass.

---

## 2. ⭐⭐⭐ THE HEADLINE — the project drew the line exactly where decidability ends, and wrote down the criterion

The vault's last four ships all turned on one axis: **a guarantee written as prose addressed to a language model is not a guarantee; a guarantee compiled into a gate that can fail is.** v246 engineered loud failures for users and shipped behind a suite that could not fail. v247 wrote a mutation tester and wired it to nothing. v248 put "no exploit, no report" in code. v249 put its contamination firewall in code and its solvability promise in prose.

This ship is the first subject that **states the rule for which half is which.**

`SKILL.md:261` says of its six connector rules:

> *"These six rules are **non-negotiable**."*

Of those six, **exactly one has a gate.**

| # | Rule (`SKILL.md:259-302`) | Enforced by |
|---|---|---|
| 1 | Rounded right-angle connectors mandatory; no diagonals; every bend a quarter-arc `r=8` | ❌ prose |
| 2 | Label-to-connector margin **6–10px, always** | ❌ prose |
| 3 | No overlapping connectors | ❌ prose |
| 4 | Shared edge → fan attach points **≥12px** apart | ❌ prose |
| 5 | No connector passes behind a non-endpoint box | ❌ prose |
| 6 | **A label mask must not overlap a node drawn after it** | ✅ **`verify-geometry.py`** |

*(Verified: `grep -in 'diagonal\|elbow\|r=8\|quarter-arc' scripts/lint-skin.py scripts/verify-geometry.py` returns no substantive hits. Five of the six "non-negotiable" rules are unguarded.)*

And the reason rule 6 is the one that got a gate is stated in the checker's own docstring — `verify-geometry.py:9-14`:

> *"**Paint order is what makes this a defect rather than a stylistic choice**: A mask overlapping a zone container is fine — zones are painted before labels, so the label stays on top. A mask overlapping a node declared *later* in the document is clipped by that node. That is the failure this check reports."*

**That is the principle, in the author's words.** A diagonal connector renders perfectly; it is merely ugly. A label mask under a later-painted node renders as *"text… as a fragment sitting on the node border"* — a determinate defect, independent of taste. **They gated the rules whose violation is a lie about the rendering, and left the rules whose violation is a preference as prose.**

The same criterion drives the second gate. `verify-treemap.py:9-10` opens:

> *"AREA FIDELITY — a cell's share of the drawn area must match the share its own label claims."*

Area fidelity is checkable **because area *is* the encoding**, so a mismatch is not a style choice — it is a chart that lies about its own numbers. The error message says so (`:313`): *"Area is the only encoding; resize the cell"* — naming cause and remedy in one line, the v246 pattern.

> ### The borrowable rule
> **You can only compile the part of your aesthetic that becomes a *lie* when violated. The rest stays prose.** Taste is not decidable; truthfulness is. Sort your quality rules into those two bins before you try to automate any of them — and when you leave one in prose, do not call it "non-negotiable."

⚠️ **The honest counterweight:** calling all six "non-negotiable" oversells five of them. An agent that emits a diagonal connector fails nothing, in CI or on your machine.

---

## 3. ⭐⭐⭐ The treemap verifier — a design tool that numerically checks its own chart does not lie

Verified in code, `verify-treemap.py:305-313`:

```python
area_share  = cell.area / drawn_total * 100
value_share = value / value_total * 100
relative    = (area_share - value_share) / value_share * 100
if abs(relative) > AREA_TOLERANCE:      # AREA_TOLERANCE = 8.0
    findings.append(... "draws {area_share:.2f}% of the area for a {value_share:.2f}% value"
                        " — {relative:+.1f}% relative. Area is the only encoding; resize the cell")
```

The README claims it measures error as a *relative* figure rather than percentage points, and gives a reason. **Both check out.** `verify-treemap.py:9-14`:

> *"This is checked as **relative** error, not percentage points: a 0.13pp slip is noise on a 59% cell and a quarter of a 0.5% cell, so **an absolute threshold passes exactly the cell most likely to be wrong**. The failure is real — the smallest cell absorbs the whole 4px-grid residue, because 4px is a third of a sliver and a rounding error on a giant."*

This is a real measurement-methodology insight and it is unusually self-aware: **their own aesthetic rule (the 4px grid) is the source of the error, the error lands disproportionately on the smallest cells, and they chose the metric that survives their own rule.** A design system creating a measurement artifact and the author identifying it is not something this corpus has seen before.

⚠️ **The catch, disclosed in its own comment** (`:78-82`): *"Grid snapping on a 1000x500 viewBox cannot do better than a couple of percent on a sub-1% cell; 8% is loose enough never to fire on [snapping]"* → `AREA_TOLERANCE = 8.0`. **An 8% relative tolerance catches gross area lies, not subtle ones.** Deliberately loose to avoid false positives from their own grid. State it that way; do not call it exact.

---

## 4. ⭐⭐⭐ The numbers ledger — every counter they aimed is right; every surface they did not aim at is stale

**The true type count is 28**, established by enumeration: `ls skills/diagram-design/references/type-*.md | wc -l` → **28**.

| Surface | Says | Machine-checked? |
|---|---|---|
| `SKILL.md` §`### Visual-type guide (28)` + its 28 rows | **28** | ✅ `verify-semantic-motion.py:194-205` — finds the heading, **counts the rows, requires exactly 28** |
| `SKILL.md` body ("Twenty-eight visual types") | **28** | (prose) |
| `SKILL.md` selection table | **28** | ✅ `verify-docs-sync.py:76` — *"expected 28 visual types in the selection table; found {n}"* |
| `README.md` ×**7** (lines 15, 33, 88, 188, 209, 373, 432) | **28** | partially |
| both `plugin.json` descriptions (types enumerated in full) | **28** | ✅ `verify-docs-sync.py:77-85` — per-type lexical hook required |
| `docs/adr/0002` Decision | 27 | ✅ correctly **amended** — *"2026-08-18 — the count is 28"* |
| **`commands/import-drawio.md:25`** | **27** | ❌ **no gate** |
| **`commands/import-mermaid.md:25`** | **27** | ❌ **no gate** |
| **GitHub repository description** | **27** | ❌ **structurally unreachable — it is not a file** |

Two independent scripts count this number. The project wrote an ADR declaring it *"a stable, verifiable claim."* And it is still wrong in three places: **two shipped agent-facing slash-command files, and the single most-read string the project has.**

*(Verified: `grep -rn '\b27\b' --include='*.md'` — the only in-tree hits are the two `commands/*.md` lines and the correctly-amended ADR prose. `commands/import-drawio.md:25`: "Type is chosen from the extracted structure; `--type` forces one of the 27.")*

> **The rule:** the number is correct in every surface a counter was pointed at and stale in every surface it was not. **A gate's aim, not a gate's quality, decides what rots.**

### 4.1 The asymmetry is inside one 236-line file

This is not a competence gap, and the proof is that the same file does it right one function earlier.

**`verify-docs-sync.py` → `check_gallery` (:91-103) is BIDIRECTIONAL:**
```python
reachable = {f"example-{name}{variant}.html" for name in types for variant in VARIANTS}
on_disk   = {path.name for path in ASSET_DIR.glob("example-*.html")}
for name in sorted(on_disk - reachable):          # ← filesystem → gallery
    errors.append(f"gallery cannot reach shipped example {name}; add a tab")
for name in sorted(types):                        # ← gallery → filesystem
    if f"example-{name}.html" not in on_disk: ...
```
Both set-differences. **This is the vault's inventory rule, implemented correctly.**

**`verify-docs-sync.py` → `check_readme_tree` (:116-125) is UNIDIRECTIONAL:**
```python
for token in sorted(set(tokens)):                 # ← tree → filesystem ONLY
    if not list(ROOT.rglob(token)):
        errors.append(f"README architecture tree names {token!r} but no such file exists")
```
**There is no `on_disk - tokens` check.** A file that exists but is absent from the tree passes green.

**The measured consequence:**

| Inventory | On disk | Named in the README tree | Missing |
|---|---|---|---|
| `type-*.md` | 28 | **14** | **14 (50%)** |
| `scripts/*.py` | 28 | **7** | **21 (75%)** |

The README's "Architecture" tree is a half-complete inventory of types and a quarter-complete inventory of scripts, and CI is green — because the only check runs tree→disk.

> **This is the sharpest form of the inventory rule the corpus has recorded**: not two repos, not two files, but **two functions in one file by one author**, one bidirectional and one not, with the drift measurable at exactly 14 and 21 files. v240 diagnosed the rule; this is the controlled experiment.

### 4.2 ⭐⭐ The best sentence in the repository

`docs/adr/0002`, Amendments:

> *"the two counters are this ADR's enforcement, so a PR that edits them without amending this file **has quietly made itself the authority**. Amend here in the same PR, or **the number in the test is just whatever the last contributor typed**."*

That is a genuinely deep observation about mechanised invariants: **a hardcoded expected value in a test is not a specification — it is a record of one person's intent at one moment, editable by the same PR that violates it.** The gate does not know the right answer; it knows the answer someone typed. So the ADR exists to put the number's *authority* somewhere a human must consciously amend.

It is also the v245 **D32** discipline, found independently: `:15` says *"27 when this record was accepted; **see Amendments for the current figure**"* — the document declares which copy of the fact wins, inside the copy that is allowed to go stale.

### 4.3 A second drift, same mechanism

| File | Version | Touched by `bump-plugin-version.py`? |
|---|---|---|
| `.claude-plugin/plugin.json:4` | **2.5.6** | ✅ |
| `.codex-plugin/plugin.json:4` | **2.5.6** | ✅ |
| `skills/diagram-design/SKILL.md` frontmatter `metadata.version` | **"2.4"** | ❌ **stale** |

The two files a script maintains agree exactly. The one it does not has fallen a minor version behind. Contrast v247, which had **five** disagreeing version strings and no machine at all — here the machine works, and the drift is precisely at its edge. **Same repo, same author, same commit: whatever the machine maintains is correct; whatever a human maintains has drifted.** This is v247's **D35** (staleness tracks *contact*, not audience) confirmed by a within-repo controlled comparison.

---

## 5. ⭐⭐ ADR 0004 — compressing a skill's description silently broke its own invocation

The most transferable single artifact for anyone who writes agent skills. `docs/adr/0004`:

> *"`SKILL.md` loads into an agent's context on every skill invocation, so it must stay lean; a byte cap keeps growth honest. But v2.3 initially set the cap at 35,000 bytes and slimmed the frontmatter `description` to fit — **deleting all 27 type names**. The description is the only text an agent sees *before* deciding to load the skill: **removing "flowchart", "Gantt", "org chart" from it removes the lexical hooks that make "make me a flowchart" invoke the skill at all**."*

The decision, in priority order:

1. The frontmatter `description` **must** name every visual type in the selection table (enforced by `verify-docs-sync.py`) — *"Routing surface is never traded for body prose."*
2. `MAX_SKILL_BYTES` is **40,000** (enforced by `verify-semantic-motion.py`).

**The lesson: a skill's frontmatter description is not documentation — it is the routing surface, the only text the agent sees before deciding whether to load the skill. Compress it and you silently break invocation.** They found this by regression, wrote it down, ranked it above their own byte budget, and mechanised it.

This is the exact inverse of **v238**, which found that *blanking* an agent's tool injections improved reasoning style. Both are true and they bound the problem from opposite ends: **strip the tool catalogue and the model reasons better; strip the skill description and the model never reaches the skill.** A real contrast pair for the vault's standing ~54K tool-catalogue thread.

### Verified, against a fleet claim that said otherwise

An agent in the fleet reported the byte cap *"NOT ESTABLISHED… no stated byte limit or ADR reference found… aspirational, not enforced."* **Refuted by hand:**

- `scripts/verify-semantic-motion.py:23` → `MAX_SKILL_BYTES = 40_000`
- `:187-189` → `if len(skill_bytes) > MAX_SKILL_BYTES: errors.append(f"SKILL.md exceeds {MAX_SKILL_BYTES} bytes: {len(skill_bytes)} bytes")`
- the check lives in `verify_markdown()` (`:180`), dispatched by `--markdown-only` (`:406-411`)
- `ci.yml` runs `python scripts/verify-semantic-motion.py --markdown-only` on every push and PR to `main`, across 6 matrix runners

**Current state: `SKILL.md` = 37,778 bytes = 94.44% of the 40,000 cap, 2,222 bytes of headroom.** The agent searched `SKILL.md` for the cap, did not find it there, and concluded it did not exist — absence of evidence read as evidence.

⚠️ **Token-cost note for the operator:** progressive disclosure means a routine diagram request loads `SKILL.md` (37.8 KB) + one type reference (~5 KB) ≈ **43 KB ≈ 11K tokens**. The `references/` directory totals **479,811 bytes**; you never load more than a small slice of it, which is the point of the architecture — but the floor per diagram is ~11K tokens, not trivial.

### And a gate on the *order* of prose

`verify_markdown()` also asserts (`:199-200`) that *"semantic-pattern router must precede the visual-type guide"* — it compares string positions and fails if the routing section drifts below the type table. **A CI gate on the sequence of instructions in an agent-facing file**, mechanising the ADR-level intent that behaviour is chosen before layout. Unusual and worth stealing.

---

## 6. The scale of the machinery, hand-counted

| Body of code | Lines |
|---|---|
| **All Python verification** (`scripts/*.py` + skill scripts) | **11,305** |
| — the checkers (`verify-*` + `lint-*`) | 5,058 |
| — **tests of the checkers** (`test-*`) | **2,861** |
| **The skill itself** (`SKILL.md` + all 41 `references/*.md`) | **7,268** |
| Shipped example assets (HTML) | 18,668 |

> **The machinery that checks the design system is 1.56× the size of the design system**, and 2,861 lines of it exist to test the graders.

For a design skill by a non-engineer founder, that ratio is the story. Six ADRs — **exactly the six settled decisions the README names**, which is itself a small honesty check that passes.

---

## 7. ✅ The D34 check — every gate is wired, and none can go green on red

Vault rule **D34** (v247): *a committed CI rule is not an enforced one.* v247 shipped a mutation tester wired to nothing and a publish gate that had never fired. v246's release gate could not fail because pytest reports skips as success. **This subject passes both tests.**

| Check | Result |
|---|---|
| Scripts in `scripts/*.py` | 28 |
| Scripts invoked by `.github/workflows/ci.yml` | **26** |
| **Unwired gates** | **0** — the two absentees are `bump-plugin-version.py` (a developer utility, correctly not a gate) and the skill-internal `self_check.py` (whose test `test-self-check.py` *is* wired) |
| `continue-on-error` | **0** |
| `\|\| true` | **0** |
| `if: always()` | 25 steps |

The `if: always()` pattern **without** `continue-on-error` is the correct implementation of the README's claim that CI *"report[s] later gate outcomes even when an earlier gate fails"*: every gate runs so you get the full report in one push, and every gate's exit code still fails the job. Each step carries an `id:` feeding a `$GITHUB_STEP_SUMMARY` table.

**Triggers are boringly correct** — `push: branches:[main]` and `pull_request: branches:[main]`. No tag glob that could silently never match (the v247 failure mode).

**Three jobs:** `plugin-package`, `python39-compat` (Python **3.9** — they test the *oldest* interpreter a user might have, which is right for a script that ships to strangers' machines), and `validate` on a **3-OS × 2-Python matrix = 6 runners** (ubuntu/windows/macos × 3.11/3.12). `GIT_CONFIG_KEY_0: core.autocrlf` is pinned in checkout — **exactly the consequence ADR 0004 promised**, implemented.

⚠️ **The one admission:** `scripts/lint-skin-baseline.txt` grandfathers **20 files** (of 103 examples, 19.4%) out of the skin linter. Honestly explained at `lint-skin.py:4-5`: *"Pre-2.0 examples may legitimately fail because they were built against an older skin. Use `--all --baseline` to skip those documented legacy files."* A named, committed, bounded exemption is the good form of a baseline.

---

## 8. ⭐⭐ The `silent` detector replicates at a 5th repo — with a new species

v246's one-command detector, `grep -rni "silent" .`, now has five consecutive hits. Here the yield is the richest yet, **and it is a different species**: in v246 the silences were places the author engineered a loud failure *for the user*. Here, almost every hit is a place the author found a way **their own checker could silently pass a wrong diagram.**

- **`verify-slopegraph.py:170-176`** — *"`float("nan")` succeeds and then every `abs(x) > tolerance` comparison is False, so **a NaN coordinate silently satisfied every check in the file**. Any non-finite value is treated as unreadable instead."*
  A real, general bug class: **NaN defeats every threshold assertion, so any verifier built out of `abs(delta) > tol` has this hole.** Rarely written down.
- **`verify-slopegraph.py:319-328`** — *"A `<line>` with no data-series is scenery… and skipping it is correct. But one whose raw text DOES declare data-series and still parsed to nothing is markup this checker cannot read, and **dropping it silently is how a lie ships**."*
  The precise distinction between *not in scope* and *in scope but unreadable*, with the rule that the second must fail loudly. **This is exactly the bug that bit v240**, where a catalogue loader silently skipped a merged submission because its file extension was wrong and the entry vanished from six downstream surfaces. An unrelated author, in an unrelated repo, wrote the rule that prevents it.
- `verify-treemap.py:2` — *"Verify the two invariants a treemap can silently break."*
- `verify-treemap.py:219` — *"would silently attribute it to a neighbour, or to nothing at all."*
- `test-verify-treemap.py:174` — *"area check went silent when a cell was unlabelled."*
- `test-verify-dumbbell.py:105` — *"The other polarity: garbage in must raise, not return a silent domain."*
- `README.md:163`, `:192` and `onboarding.md:94` — the user-facing side: *"verified after rendering rather than **silently** replaced with generic system fonts"*, *"won't **silently** ship default-skinned diagrams"*, *"**never silently** add a remote font URL."*

> **The refinement: their checkers' comments are a changelog of the checkers' own blind spots.** The most valuable comments in this repository are not about diagrams; they are about the ways a verifier can return green on garbage.

---

## 9. What ships to your machine vs what stays in the repo

This is the honest calibration of §2, and **the project states it itself.**

**Installed footprint — 3 files, 2,603 lines:**

| File | Lines | Role |
|---|---|---|
| `mermaid_extract.py` | 1,325 | Mermaid → structured IR |
| `drawio_extract.py` | 889 | draw.io → structured IR |
| **`self_check.py`** | **389** | the **only** output checker that ships |

`self_check.py` asserts the **accessible-SVG contract** (`role="img"`, `<title>` as first child, non-empty title *and* desc, diagram-prefixed IDs never bare, `aria-labelledby` naming title then desc), **single-file safety** (at most one `<script>`, and it must byte-match the canonical controller), and the **motion contract** (mode validity, step contiguity, a 12-item budget, reduced-motion behaviour, aria on semantic items).

**What does not ship:** `lint-skin.py` (747 lines of skin/token/colour rules), `verify-geometry.py`, `verify-treemap.py`, `verify-slopegraph.py`, `verify-dumbbell.py`, `verify-motion.py`, `verify-semantic-motion.py`, `verify-docs-sync.py`, and all 15 `test-*` files.

**So: every check of the *aesthetic* stays in the repository. What ships to you checks accessibility and safety.** And the §9 checklist says so, item by item — *"In **this repository**, `python3 scripts/verify-geometry.py <file>`"* versus *"from an **installed skill**, manually check print and static-query states on top of the self-check."*

> The distinction is defensible and even principled — accessibility structure is decidable, taste is not — but say it plainly: **the "editorial quality" promise is prose-enforced at the point of use.** The 37-item taste gate is what governs your diagram. The 11,305 lines govern their gallery.

**The §9 taste gate is 37 checkboxes** (`grep -c '^\- \[ \]'`), and all 37 in `SKILL.md` live in that one section: Technical 17, Type fit 7, Typography 6, Remove test 4, Signal 3. *(Three independent estimates in this run — a mapper's 28, the critic's 35, my own 41 — were all wrong. Settled with one command.)*

The "Remove test" is the best-designed part, and it is pure editorial judgement: *"Can I remove any node? Can I merge any two nodes? Can I remove any arrow? Can I remove any label?"* — preceded by the gate that matters most, *"Would a table / paragraph do the same job? (If yes — don't draw.)"*

---

## 10. Security — LOW, structurally clean, with one named gap

**No broken-auth triad, structurally**: there is no server, no port, no socket, no CORS surface. The v231/v232 failure mode cannot occur here.

**Genuinely careful output safety:**
- `onboarding.md:93` — the single-file allowlist *"accepts only a parsed HTTPS URL whose hostname is **exactly** `fonts.googleapis.com` and whose path is **exactly** `/css2`; **prefix/lookalike hosts** and other paths fail."* A precise allowlist that anticipates `fonts.googleapis.com.evil.tld`.
- `onboarding.md:94` — *"**never silently add a remote font URL** or claim an exact match"* — a remote URL in your diagram HTML is a beacon; this is an exfiltration guard.
- `self_check.py` rejects `<base>`, `<embed>`, `<object>`, `<iframe>` and `on*` attributes; the motion path pins the controller byte-for-byte and rejects CSS `@import`, non-fragment `url()`, and remote assets.
- The approval gate is real and repeated (`onboarding.md:28`, `:103-131`, `:239`, `:294`): propose a diff, **write only after the user approves**. A recoverable `default` snapshot is taken before overwriting a pristine guide (`:156`).
- Import parses text only — *"no rendering, JavaScript, browser, network, or followed click targets."*

**🔴 The gap — agent safety, not output safety.** Brand onboarding fetches a live website (`onboarding.md:54`: *"Use `agent-browser` (preferred) or a plain `fetch`"*) and pulls its content into the agent's context. **Nothing anywhere treats that page as untrusted text.** Every guard concerns what gets *written* (fonts, colours, contrast); none concerns what the page might *say*. The same holds for `.drawio`/`.mmd` node labels: the machinery is about escaping them safely into SVG, not about a label that instructs the model. This is v247's gap exactly.

**Severity: LOW**, and I want to be fair about why — the worst realistic outcome is an ugly diagram or an attempted remote font URL that the allowlist blocks. There are no credentials in this path. But the sentence *"a fetched page is data, not instructions"* is not in the repo, and it should be.

**Other:** export requires `pip install playwright && playwright install chromium` (disclosed). README links carry `utm_source` parameters; no telemetry, analytics, or phone-home found. No `postinstall`/`prepare` lifecycle scripts. Writes are confined to `~/.diagram-design/profiles/`, the skill's own `style-guide.md`, and diagram files you asked for.

*(Byte-cap constants for the import path — `MAX_INPUT_BYTES` 32 MB, `MAX_XML_BYTES` 64 MB, and pre-parse rejection of `<!DOCTYPE`/`<!ENTITY` — were reported by the fleet from `drawio_extract.py`. Consistent with my reading of the file's structure, but I did not independently confirm the numeric constants; treat as fleet-sourced.)*

---

## 11. Multi-harness packaging, and one genuinely useful platform disclosure

Four install paths: **Claude Code** (`/plugin marketplace add`), **Codex** (`codex plugin marketplace add`), **Pi** (`pi install <url>`), and **Claude Cowork** via an organization marketplace. `.claude-plugin/` and `.codex-plugin/` carry near-identical manifests (the long type-enumerating description appears **three times** across them, plus a fourth copy in `SKILL.md` frontmatter) — duplication that `verify-docs-sync.py:183-192` reconciles by comparing manifest descriptions, which is the mechanised answer rather than the symlink answer v243 used.

**Pi is corpus subject v36/v228** (`earendil-works/pi`) — a genuine Pattern **#57** dependency: the repo ships a `prompts/` directory of Pi prompt templates alongside `commands/` for Claude Code. The README also documents migrating *off* a standalone `npx skills add` copy onto the marketplace path.

**⭐ The Cowork disclosure** — unusually precise operator knowledge about a first-party Anthropic surface, quoted from the README:

> *"Organization GitHub marketplaces currently require a private or internal repository, so first mirror this public repository into one owned by your organization… **Automatic sync runs when a pull request containing a plugin version bump is merged to the mirror's default branch; direct pushes do not trigger the webhook.**"*

That second sentence is the kind of thing you normally learn by losing an afternoon. Worth keeping regardless of this skill.

---

## 12. Reception and growth — what is and is not established

Page-stated: 22.8k stars, 1.4k forks, 77 watchers, Trendshift repository 26141. **The GitHub API is mocked in this environment (§37.4)**, so these are page assertions, not verified measurements, and **no viral-velocity claim (Pattern #52) may be made.**

The star-to-commit ratio (22.8k over 114 commits) is unusual and suggests a launch spike rather than accretion, but **I could not establish the timeline, the originating share, or the discourse with confidence.** The fleet's reception report was put through an independent verification pass and did not survive it cleanly enough to publish specifics. Treat the following as **NOT ESTABLISHED**: which post or thread drove adoption, when, what substantive criticisms were made, and whether the author has written about building it.

Also **not established**: the star count's accuracy, the fork/watcher figures, release cadence and tag history, issue/PR counts and their content, and whether Lavery's GitHub bio reads as any agent quoted it.

---

## 13. Where this sits against the corpus

| Ship | Code-vs-prose position |
|---|---|
| v246 needle | Exemplary loud-failure doctrine **for users**; its own release gate could not fail (skips = success) |
| v247 ego lite | Wrote excellent checks, **wired none**; a committed gate its own history contradicted (D34) |
| v248 Strix | *"No exploit, no report"* as a **code gate**; but a hardcoded authorization it never performed |
| v249 arc-task-gen | Contamination firewall in **code**; solvability guarantee in **prose** |
| **v250 diagram-design** | **Every gate wired, no soft-fail, 6-runner matrix — and the project states the criterion for which half is which. The drift lives in exactly the three surfaces no counter was aimed at.** |

The set is now five. The distinctive contribution of this one is that it is the **first subject to articulate the boundary rather than merely fall on one side of it** — and the first where the finding is not "they failed to wire their gates" but "the gates are excellent, so the drift moved to where the gates are not."

**Second corpus contribution:** the inventory rule (v240) gets its controlled experiment — two functions, one file, one author, one bidirectional and one not, drift measured at 14 and 21 files.

---

## 14. Error ledger for this analysis

**Mine — 3, all self-caught before publication:**

1. **"The `27` exists only in GitHub settings."** Wrong. A broader grep found `commands/import-drawio.md:25` and `commands/import-mermaid.md:25`. My first grep pattern (`27 (editorial|visual|diagram)`) missed the phrasing *"one of the 27"*. The corrected finding is stronger.
2. **"`verify-slopegraph.py`/`verify-dumbbell.py` are gates for missing or removed types."** Wrong. Both are documented variants inside `type-line.md` and `type-bar.md`, and slopegraph is the feature *at HEAD*. This was evidence *for* the project's discipline, not against it.
3. **Estimated the taste gate at 41 items.** Actual **37**.

**The fleet's — 4:**

4. **Byte cap "NOT ESTABLISHED… aspirational, not enforced."** Refuted: ADR 0004 + `verify-semantic-motion.py:23,187-189`, CI-wired. The agent searched only `SKILL.md`. *Absence of evidence as evidence.*
5. **Checklist counts of 28 (mapper) and 35 (critic).** Both wrong; **37**. Adjudicated with `grep -c`, not authority.
6. **`datalake` escalated as an undocumented type / inventory violation** by the mapper, then the contradiction pass, then the critic. It **is** documented — `type-high-level.md:459-461` describes all three variants as examples of the high-level type. Three stages agreed on a defect that dissolves on reading the parent file.
7. **The critic named the GitHub description as the only stale count surface**, missing the two in-tree `commands/*.md` instances.

**⭐ Method finding.** Errors 2 and 6 are the same trap, and it caught **me and three agents independently**: `example-datalake.html` and `example-slopegraph.html` do not name their parent type, so a documented child looks orphaned to *any* inventory check — human or agent. **A naming convention that omits the parent defeats inventory reasoning.** The fix that worked both times was the same: stop diffing filenames and go read the parent type file.

**⭐ The v249 lesson replicated a third time.** The single worst error in this run (#4, a real CI gate declared aspirational) was produced by the fleet and caught by me running the check myself. The contradiction stages did useful work — the `datalake` escalation was at least *investigated* rather than asserted, and the critic corrected a mapper's checklist count — but the errors that would have embarrassed the ship were all caught at the keyboard.

**Fleet statistics:** 19 agents (6 map → 6 pipelined contradiction → 3 situate → 3 contradiction-over-situate → 1 critic), **19/19 completed, 0 errors, ~2.27M tokens, 470 tool uses, 1,169 s**. The v249 refinement — pointing the contradiction stage at the *situating* reports too — was implemented and did suppress the fabrication class: **no invented paper, project, or person survived into this document.** Its cost was that the reception surface returned little publishable.

---

## 15. Verified numbers appendix

| Claim | Value | Source |
|---|---|---|
| `type-*.md` files | **28** | `ls … | wc -l` |
| `references/` files total | 41 | `ls | wc -l` |
| `example-*.html` files | **103** | `ls | wc -l` |
| Gallery `data-type` tabs | **39** | `grep -o 'data-type="[a-z-]*"' index.html | sort -u | wc -l` |
| Tabs with no `type-*.md` | 11 — all variants/demos, all documented in a parent type file | `comm -23` |
| `type-*.md` with no tab | **0** | `comm -13` |
| `SKILL.md` | **37,778 bytes** (94.44% of the 40,000 cap) | `wc -c` |
| §9 taste-gate checkboxes | **37** | `grep -c '^\- \[ \]'` |
| Python verification lines | **11,305** | `cat …/*.py | wc -l` |
| — `test-*` only | 2,861 | `cat scripts/test-*.py | wc -l` |
| — `verify-*`/`lint-*` only | 5,058 | `cat scripts/verify-*.py scripts/lint-*.py | wc -l` |
| Skill instruction lines | **7,268** | `cat SKILL.md references/*.md | wc -l` |
| **Verification : instruction ratio** | **1.56 : 1** | derived |
| `references/` total bytes | 479,811 | `awk` sum |
| Shipped skill scripts | 3 files / 2,603 lines | `find` + `wc -l` |
| Scripts in `scripts/` | 28 | `ls scripts/*.py | wc -l` |
| Scripts wired in `ci.yml` | **26** | `grep -oh 'scripts/[a-z0-9_-]*\.py' | sort -u` |
| `continue-on-error` / `\|\| true` | **0 / 0** | `grep -c` |
| `if: always()` steps | 25 | `grep -c` |
| CI matrix | 3 OS × 2 Python + a 3.9 job | `ci.yml:79-82` |
| Lint baseline exemptions | 20 files | `wc -l lint-skin-baseline.txt` |
| ADRs | 6 (= the six the README names) | `ls docs/adr/` |
| `AREA_TOLERANCE` | 8.0 (relative %) | `verify-treemap.py:82` |
| `MAX_SKILL_BYTES` | 40,000 | `verify-semantic-motion.py:23` |
