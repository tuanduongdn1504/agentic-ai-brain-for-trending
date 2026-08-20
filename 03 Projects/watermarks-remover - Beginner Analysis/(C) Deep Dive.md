# (C) watermarks-remover — Deep Dive (REBUILT)

> **This document replaces the original v251 deep dive**, rebuilt from scratch at operator request on 2026-08-20.
> The original is recoverable: `git checkout 74c1b2a -- '03 Projects/watermarks-remover - Beginner Analysis/'`
>
> **Subject:** `guillaumemeyer/watermarks-remover` — an agent skill + stdlib-Python service that strips AI provenance marks (invisible Unicode, statistical text watermarks via rewrite, and C2PA/EXIF/XMP metadata). MIT.
> **Pin (this rebuild):** HEAD `d5563d2e129166cae737cc6ac604e75f5631c368`, 2026-08-20.
> **Pin (original v251):** `1cc2783`, 2026-08-19. **The subject moved 12 commits between the two.**

---

## 0. Method, and an honest limitation

Two independent `git clone`s into separate directories; `diff -rq --exclude=.git` run **both ways**, clean in both directions. Every number below came from a command I ran, not from recall.

A 19-agent fleet mapped six disjoint surfaces (architecture, Layer A/B, metadata/formats, benchmarks, CI/security, docs/claims), each surface then handed to an adversarial *contradiction* agent instructed to find what the mapper got wrong; three external-research agents were contradicted the same way; one critic synthesised.

**The limitation, stated plainly:** I intended the fleet to be blind to the original v251 findings. It was not fully blind. This vault's `CLAUDE.md` is auto-injected into every subagent, and it carries the v251 summary. The map agents derived their findings from files and line numbers independently — the architecture mapper contradicted v251 in its first pass — but the critic demonstrably read the vault's own state and argued with it. **A blind replication cannot be run inside a vault whose state file is auto-loaded into the workers.** That is a method finding in its own right, and it is the reason every conclusion below is one I re-derived with my own commands.

Errors the machinery produced, and I discarded, are listed in §9. No subject code was executed.

---

## 1. What it is

An MIT-licensed toolkit for removing machine-readable provenance from content, in three layers:

- **Layer A — invisible Unicode.** Deterministic. Strips zero-width characters, bidi controls, variation selectors, tag characters, noncharacters, reserved ignorables, and maps space homoglyphs to ASCII space. `service/scripts/text_unicode.py`, 724 lines.
- **Layer B — statistical text watermarks.** Best-effort. Rewrites prose with a model (paraphrase / humanize / back-translate / structural), optionally looping against an evaluator. `service/scripts/rewrite_text.py`.
- **Container and image metadata.** C2PA, EXIF, XMP, OOXML doc properties, ID3, ISOBMFF boxes, across 41 file extensions.

Delivery is a local HTTP service on `127.0.0.1:8765` plus agent skills that drive it.

### The scale, measured

| Measure | Value | Command |
|---|---|---|
| Commits (HEAD / all refs) | **140 / 167**, one root | `git rev-list --count` |
| Tracked files | **150** | `git ls-files \| wc -l` |
| Python files / lines | **74 / 25,873** | `git ls-files '*.py' \| xargs wc -l` |
| `service/scripts/` | **28 files / 14,141 lines** | `find … \| xargs wc -l` |
| `tests/` | **41 files / 10,592 lines** | `find … \| xargs wc -l` |
| Test functions | **549** | `grep -rh "^def test_"` |
| Test-to-source ratio | **0.749 : 1** | 10,592 / 14,141 |
| README | **72,836 bytes / 1,120 lines** | `wc -c`, `wc -l` |
| Contributor identities | **29 (HEAD) / 30 (all refs)** | `git shortlog -sn` |
| First commit | **2026-08-11 09:32:32 −0700** | `git log --reverse` |

Guillaume Meyer holds **81 of 140** HEAD commits (57.9%) across **two** git identities — `1385518+guillaumemeyer@users.noreply.github.com` (62) and `guillaume@dgx.tailbbceab.ts.net` (19). A **third** identity, `guillaumemeyer@users.noreply.github.com`, appears only in trailers and non-HEAD refs; across all refs the three sum to 108. *Summing is mandatory; the ref population must be declared.*

---

## 2. THE HEADLINE — three detectors, three closed loops, three confessions

The project's reason to exist is Anthropic's watermark. It has now built **three** independent detection paths, and **every one of them is a closed loop that can only detect a mark it planted itself** — and every one says so, in its own docstring, in the file a user would open.

**1. The MarkLLM harness** — `service/scripts/detect_text_watermark.py:8-10`:

> "MarkLLM is Apache-2.0. It is an independent verification harness: detection is only valid against the SAME scheme config + keys used at generation. **It cannot certify that a vendor detector will fail on the given text.**"

**2. The MarkDiffusion harness** — `service/scripts/markdiffusion_harness.py:12-15`:

> "Detection is only valid against the same scheme config, model, and keys used at generation — **it cannot certify that a vendor detector will fail** on the given image."

**3. The keyed-Gumbel detector — new since the original v251 pin** (`service/scripts/detect_gumbel.py`, 308 lines, commit `9dda608`, authored by Meyer on 2026-08-19). Its "Honesty caveat" block, lines 21-25:

> "detection is a *same-key replay* — it is valid only against the same key, tokenizer, and PRF layout used at generation (self-hosted engines such as arbi-serve). **A negative result establishes nothing**: unwatermarked text, another provider's key, and human text all sit at chance. **This detector is not a vendor oracle.**"

And the benchmark's own header, `service/scripts/bench_synthid_text.py:20-22`, closes the door explicitly:

> "Detection: same-config-only MarkLLM detection (reproducible, no vendor APIs). Google retired SynthID text watermarking on its API in Aug 2026, **so no vendor tier exists.**"

`bench_synthid_text.py` is 52,787 bytes of real measurement apparatus — it computes a **clear rate** (before-positive → after-negative), score deltas, lexical divergence, length ratio, numbers-preserved, attempt counts, and clears-per-million-tokens, and emits `report.md` / `results.json` / `results.csv`.

**None of those files exist in the repository.** `benchmarks/` contains exactly eleven files: one README, two shell scripts, eight ~500-byte corpus texts. The instrument ships. **No reading from it does.**

That is the shape of the thing: a genuinely careful measurement rig, aimed at a target that cannot be measured, saying so in four separate files, and publishing no numbers rather than publishing numbers it could not defend.

**Verified at the primary source, not from the repo.** Anthropic's own support article states it uses "(1) watermarks embedded in text, and (2) signed provenance metadata attached to files"; that marking covers "Claude models launched on or after August 2, 2026" across "Claude Platform (API), Claude, Claude Code, Claude Cowork, and Claude Tag", "wherever Claude is offered, worldwide" — and, decisively:

> "We're also working to enable users and other third parties to detect Claude's embedded watermarks… **We'll share details on detection mechanisms in forthcoming technical documentation.**"

Anthropic itself says third-party detection is *forthcoming*. The repository's central caveat is not modesty. It is correct, and the vendor confirms it.

---

## 3. THE SECOND FINDING — 4 hours 19 minutes, and the delta is one defect class

TechCrunch published Anthropic's watermarking announcement at **05:13 PDT on 2026-08-11**. The first commit here is **09:32:32 −0700 the same morning** — *"Initial skill: remove Claude text marks and C2PA metadata."* **Four hours nineteen minutes.** Causation is not claimed; the interval is the evidence.

More interesting is what happened in the **24 hours after the original v251 ship**. Twelve commits landed. **Nine of them are the same defect class — a failure being reported as a clean result:**

| Commit | Subject | PR |
|---|---|---|
| `ce90a71` | treat a failed c2patool run as inconclusive, not as "no C2PA" | #156 |
| `3d2bac7` | distinguish a failed cleaner from an already-clean file | #159/#161 |
| `546a9f1` | an unreadable text file is a failed scan, not a clean one | #169 |
| `1cf93d0` | keep collected evidence when a later zip member fails to read | #175 |
| `0f41bd3` | truncated ISOBMFF containers still run the C2PA byte-scan fallback | #176 |
| `8c9ff34` | route website binary formats to their real scanners | #177 |
| `b77ad4b` | a crashed cleaner blocks the commit instead of reading as clean | #179 |
| `d5563d2` | keep the truncated tail instead of dropping it in png/isobmff strips | #182 |
| `197c36e` | preserve MP4 media offsets when stripping metadata | #183 |

**Eleven of the twelve were authored by someone other than Meyer** — `yzxcj797` (5), Italo Rodrigues, codifly-network, 初心Yearth, its-stam, Pino De Francesco. Meyer wrote one: the Gumbel detector.

The new tests say why it matters better than any summary could. `tests/test_c2patool_report.py:171-174`:

> "`has_c2pa: False` next to a silently dead probe is the actual hazard: it reads as 'this asset carries no C2PA' **on the one check a user would trust**."

And `tests/test_truncated_tail_preserved.py:44-49`:

> "every input byte must survive byte-for-byte: nothing is silently dropped. … And the run says the tail was kept — **never 'already clean'**."

For a provenance-stripping tool, a false *clean* is the only failure that matters, because the user acts on it and cannot see it. A stranger-driven sweep closing nine of them in a day is the most encouraging fact about this repository.

**The `grep -rni "silent"` detector replicates a seventh consecutive time**, 7 hits, and two of them are these new tests. The doctrine is stated at `service/scripts/av_meta.py:16`: *"Known scope limits (documented, not silently mishandled)."*

---

## 4. THE THIRD FINDING — every guard on the file is code; every guard on the world is prose, and that is right

A grep of the entire Python surface for the vocabulary of the ethics document:

```bash
grep -rn "consent\|authoriz\|you own\|ethic\|fraud\|academic" --include=*.py .
```

returns **ten hits. All ten are `_authorized()` bearer-token checks** in the two HTTP servers. **Not one line of code implements "content you own."**

What *is* enforced in code is everything decidable from bytes: SSRF (`audit_website.py:282,286` — IPv4-mapped IPv6 unwrapped, `is_global` enforced), per-hop redirect revalidation with origin pinning (`:390-419`), zip bombs (`container_meta.py:772`, `MAX_ZIP_DECOMPRESSED_BYTES = 128 MiB`, checked **per member** at `:786` **and cumulatively** at `:809`), body and batch caps, unknown-format and binary-as-text refusals.

`ethics.md` is titled **"Intended use"**, not "Policy". It marks academic fraud and circumventing lawful transparency as *"Not appropriate"* (`:14-15`), states at `:18` that *"A removed mark does **not** mean the content was never AI-assisted"*, and closes at `:32`: *"The developers disclaim any liability for potential misuse by users."*

That last sentence is an admission of non-enforcement, and it is the correct one. **"Do you own this content?" is not decidable from the artifact.** A program handed bytes cannot answer it. The project compiles what can be compiled, leaves the rest as prose addressed to a person, and does not pretend the prose is a gate.

---

## 5. What the docs get right, and the one place the inventory check runs one way

**The capability matrix is the strongest structured limitation disclosure in this corpus.** `skills/remove-ai-marks/references/removal-matrix.md` has five columns, and the fifth is headed **"Verifiable today?"**. It answers, for the two features anyone came for:

- `:7` statistical text watermark → **"No without vendor key/detector"**
- `:19` pixel image watermark → **"No without official detector"**

Alongside `Yes` for Unicode and container metadata, `Partial` for PDF, and `—` for the out-of-scope rows (audio/video, C2PA soft binding, training backdoors). A capability table that answers *"no"* about its own headline features, in a dedicated column, is rare enough to be worth stealing outright.

**The README argues against its own product** (`:798`):

> "If the plan is to rewrite the text with a cheaper model anyway, why pay for a premium model in the first place? Generating directly with the cheaper model is simpler, cheaper, and produces the same — or better — end result."

In fairness — and the original v251 write-up did not quote this — `:800` immediately supplies the case *for* Layer B: it makes sense "when you specifically want the premium model's **thinking and drafting** and accept a rewrite pass to satisfy a hygiene or privacy requirement — not as a cheap route to mark-free text." The section is an honest cost-benefit, not only a self-demolition.

**Licence discipline, verified.** The Docker image table at `README.md:219` derives its **"Published?"** column from each upstream's licence — including `watermarks-remover-ctrlregen:local`, *"never published (`noai-watermark` ships no LICENSE)"*. They observed an upstream that ships **no licence at all** and correctly treated absence as all-rights-reserved. Repeated in `compose.yaml`, a dedicated README section, and the scorer's own module docstring.

**The one asymmetry.** I ran the format inventory in both directions:

- **Docs → code:** all 21 formats named in the README "File formats" table exist in the dispatch sets. **Zero phantom formats.**
- **Code → docs:** the code dispatches **41 extensions** (`IMAGE_EXTS` 11 + `CONTAINER_EXTS` 12 + `TEXT_EXTS` 12 + `AV_EXTS` 6). The README's File formats table names 21 and **omits `.xlsx`, `.pptx`, `.htm`, `.mdx`, `.markdown`, `.heif`, and the entire twelve-extension text class** (`.txt .text .css .js .py .rs .go .json .yaml .yml .toml .csv`).

Most of the gap is covered *somewhere* — `removal-matrix.md:15` does list DOCX/XLSX/PPTX, and Layer A's text handling is documented separately — so this is not a phantom-capability problem. It is the familiar shape: **the direction the check runs is the direction that stays true.** No single document is a complete inventory of what the code will accept, and the README table is the one a reader will treat as the list.

---

## 6. Security posture

**Low, and better than most tools this corpus has examined.**

- **No broken-authentication triad.** `grep -rni "cors\|access-control-allow"` across the repo returns **zero hits**. The core server defaults to `127.0.0.1:8765` (`server.py:988`), warns on any non-loopback bind (`:1002-1003`) and warns when no key is set (`:1007`). Auth **fails open** when unconfigured (`_authorized()` at `:836-840` returns `True` if `API_KEY` is empty) — but only behind loopback, and it says so.
- **Three listeners, correctly characterised.** Two HTTP: `server.py` (8765) and `synthid_score_server.py` (8766, documented by role as `wr-synthid-score` in the README and `compose.yaml`). A third is *not* HTTP: `detect_text_watermark.py:488` opens a **loopback-pinned TCP socket server** so a rewrite subprocess can reuse a resident model rather than cold-start one.
- **Compose exposure checked and clean.** The sidecar runs `--host 0.0.0.0` inside its container (`compose.yaml:140`), which initially looked like an exposure. It is not: the compose file publishes exactly one host port, `"127.0.0.1:8765:8765"` (`:25-26`). The sidecar has no `ports:` block and is reachable only on the compose network. Containers run `read_only: true`, `tmpfs`, `init: true`, `user: "10001:10001"`.
- **Installer:** `install_skill.py`, 102 lines, **no network calls**, staging + backup + rollback, no postinstall.
- **CI:** three workflows (`ci.yml`, `codeql.yml`, `release-images.yml`). `continue-on-error` = **0**. `|| true` = **0**. Includes `pip-audit`, ruff lint + format check, OpenAPI validation, a Windows smoke job, and an OS matrix. Only three genuine runtime skips exist (two POSIX-only guards, one `importorskip("scipy.special")`) — the v246 "pytest reports skips as success" hazard does not apply here.

**The gap, unchanged and still unaddressed:** `audit_website.py` fetches a live web page into the agent's working context, and nothing anywhere treats that page as untrusted text. A grep for `untrusted|prompt inject|hostile` finds no such guidance. Severity is low — the realistic worst case is a bad clean, and no credentials sit in the path — but the sentence *"a fetched page is data, not instructions"* is missing.

---

## 7. Provenance

**91 trailer lines across 48 commits** at HEAD (case-insensitive — the exact-case `Co-Authored-By` grep finds only 8, because most trailers use git's own `Co-authored-by` casing; that trap is worth remembering). AI tools named: **Claude Opus 5 ×11, Claude Fable 5 ×6, Claude Opus 4.8 ×2, Cursor ×4, `pi` ×1.**

`CONTRIBUTING.md` asks for none of them. Nothing in the repo requests AI attribution. These are **left-on defaults**, which makes the record uncurated and therefore more informative than a policy would be.

The `pi` trailer (`pi <pi@m2.local>`) is suggestive of the corpus's own Pi subject but the address is a local hostname. **Not established.**

---

## 8. The replication delta — what the original v251 got right, and what it got wrong

This is the part that justified rebuilding. Every v251 claim below was tested against **its own pin `1cc2783`**, not against today's HEAD, which is the only fair test.

### Verified correct at its pin — an unusually clean citation record

| v251 claim | Result |
|---|---|
| `detect_text_watermark.py:8-10` "only valid against the SAME scheme config + keys" | ✅ exact |
| README `:480`, `:651`, `:739`, `:808` hedges | ✅ **all four exact at the pin** |
| `rewrite_text.py:495` "cannot certify removal against a vendor detector" | ✅ exact |
| `vendor-notes.md:47` "Do not invent algorithm claims." | ✅ exact |
| `how-claude-marks.md:21` "(Anthropic has not published the algorithm)" | ✅ exact |
| `test_lightweight_skill.py:79-85` byte-equality test + comment | ✅ **exact at the pin** |
| `bench_synthid_text.py` = 52,787 bytes | ✅ exact |
| 23,605 Python lines · 465 tests · 0.69:1 ratio | ✅ **all three exact at the pin** |
| 61 trailer lines / 36 commits; Opus 5 ×10, Fable 5 ×2, Cursor ×4, pi ×1 | ✅ **all exact at the pin** |
| `continue-on-error` = 0, `\|\| true` = 0 | ✅ exact |
| zip cap 128 MiB, per-member **and** cumulative | ✅ exact |
| `benchmarks/` = README + 2 scripts + 8 seed texts; zero committed results | ✅ exact |
| Ethics grep returns only HTTP authorization | ✅ **exact — 10 hits, all `_authorized()`** |
| Docker "Published?" column derived from upstream licences | ✅ exact |
| The second HTTP server *is* documented, by role, as `wr-synthid-score` | ✅ exact |

### Wrong

**1. "An agent skill that ships ZERO code."** The repository ships **two** skills. `skills/remove-ai-marks/` is indeed code-free — SKILL.md plus six references. But `skills/clean-user-facing-text/` ships **four Python scripts, 1,038 lines**, including a **vendored byte-for-byte copy of the 724-line Layer A engine**, and its SKILL.md instructs the agent to run them locally with `python3` — no HTTP service involved at all. It was added on 2026-08-16 and was present at the v251 pin.

This compounds: v251 recorded the claim as a *correction of its own critic* ("the thin-client rule is enforced by ABSENCE"), and the critic was right. Worse, the byte-equality test v251 correctly cited and recommended as a takeaway — `test_lightweight_skill.py:79-85`, *"Any engine change must be applied to both copies in the same commit"* — **exists precisely because a skill ships vendored code.** The evidence against the headline was inside the artifact the headline's own takeaway was drawn from. It is the inventory trap that v251 itself flagged, one paragraph earlier, as "the v250 filename-inventory trap REPEATING".

**2. "Guillaume Meyer 106 of 128."** At the pin, by name, Guillaume is **80 of 128** (61 + 19). No counting method produces 106 against a 128 denominator: HEAD gives 81/140, all-refs gives 108/167. The numerator came from an all-refs population and the denominator from HEAD — a base mix, committed in the same sentence that invoked the rule about summing identities.

**3. "Redirects refused."** `audit_website.py:390-419` **follows** redirects up to `MAX_REDIRECTS`, re-validating and re-pinning the target on every hop. The security property is real and arguably stronger than refusal — the origin is pinned after the first hop, so a **cross-origin** redirect is rejected — but "refused" is the wrong verb for what the code does.

**4. "Format matrix checks BOTH ways — no phantom formats."** Half right. The docs→code direction is clean. The code→docs direction is not (§5).

### Overstated

- The `removal-matrix` cell was rendered as a flat **"No"**; it actually reads *"No without vendor key/detector"* followed by a clause describing what the MarkLLM harness **can** verify. The compression is defensible but harsher than the source.
- "The README argues against its own product" omits `:800`, which supplies the case for Layer B.

### What v251 could not have known

The subject moved: **12 commits, +2,268 Python lines, +84 test functions, +7,068 README bytes, a third detector, and the nine-commit false-clean sweep** described in §3.

**The pattern is worth naming.** v251's *quotations and line citations* were near-perfect — sixteen checks, sixteen passes. Its *counts and inventories* were where it broke. Reading a file and quoting it is reliable; enumerating a directory and generalising from one member is not.

---

## 9. Error ledger

**Mine, all self-caught before publication (4):**

1. Counted "51 test files" using a glob that swept non-`.py` files and the skill scripts. Correct: **41** `.py` files in `tests/`. *Settle a count with the right command, not a plausible one.*
2. Counted `Co-Authored-By` case-sensitively and got 8 lines / 3 commits. Correct: **91 / 48**. The corpus recorded this exact trap at v245 and I walked into it anyway.
3. Concluded the byte-equality test did not exist at the v251 pin, from a grep that returned nothing. It returned nothing because **zsh silently dropped the output** — a documented hazard in this sandbox. Routing to a file showed the test at pin lines 79-85. I was one step from accusing v251 of fabricating a quote it had cited correctly. *A shell that can drop output cannot produce a negative result.*
4. Flagged the compose sidecar's `--host 0.0.0.0` as a possible exposure. Tested it: no host port mapping exists. Dropped.

**The fleet's (26 corrections raised by the contradiction agents, plus 3 by the critic that I caught):**

- **A fabricated quote** attributed to Meyer ("treats authorship as a binary thing") sourced to a real Bleeping Computer article that does not contain it. Discarded.
- **Two unverifiable press URLs** (Cybernews 403, Digital Trends) asserted as VERIFIED coverage. Discarded.
- **A dead-link claim** that Claude refused to install the skill. Discarded — interesting if true, unsourced as given.
- **Nine "FABRICATED" citation verdicts that were themselves wrong**, because the contradiction agents checked v251-era line numbers against today's HEAD. The byte-equality test, `vendor-notes.md`, the README quotes — all correct at the pin, all "refuted" against a file that had since grown.
- **The critic invented an `ethics.md` quote**: *"This tool does not enforce consent; it documents the risks and trusts the user."* A grep for `enforce consent|does not enforce` across the whole repo returns **zero hits**. `ethics.md:18` actually reads *"A removed mark does not mean the content was never AI-assisted."* Discarded — caught only because I had read the file in full.
- **The critic asserted 15 contributors** against my 30. Every method — `%an` on HEAD, `%an` on all refs, `shortlog` both ways, distinct emails both ways — returns **29 / 30**. Adjudicated by command.
- **The critic declared the vault's "128 commits / 154 all-refs" wrong.** Those figures were correct at the v251 pin. The critic had no pin awareness and was comparing against HEAD.
- **A mapper reported 45 files in `service/scripts/`.** Actual: **28**.
- Two genuinely useful catches: the Google SynthID correction (Google documents **three** detection-deployment models — fully-private, semi-private, public — so "only Google can verify" is wrong), and the discovery of the third listener.

**One fleet finding I verified and kept:** `bench_synthid_text.py:20-22`, *"Google retired SynthID text watermarking on its API in Aug 2026, so no vendor tier exists."* Neither v251 nor my own first pass had this. It is the benchmark declaring its own structural ceiling in its header.

---

## 10. External facts, verified at primary sources

- **Anthropic** — support article "How Claude marks AI-generated content": two techniques (embedded text watermarks + signed C2PA file metadata); models launched **on or after 2026-08-02**; API, Claude, Claude Code, Claude Cowork, Claude Tag; **worldwide**; and third-party detection is **"forthcoming."**
- **EU AI Act Article 50** — effective **2026-08-02**; requires machine-readable marking that is "effective, interoperable, robust and reliable as far as technically feasible."
- **Kirchenbauer et al.**, arXiv:2301.10226, ICML 2023 — red/green vocabulary partitioning via a PRF over preceding context; detectable **without** model access.
- **C2PA** — the specification's own Security Considerations acknowledge manifest stripping as a real threat and propose manifest repositories as mitigation.
- **ExifTool** — Phil Harvey, first released 2003-11-19. Metadata stripping is a twenty-three-year-old capability.
- **arXiv:2607.16010** — *"AI Watermark Evidence Fails Forensic Readiness: An Empirical Evaluation"*, Tamim & Khan, 2026-07-17. **Verified: the paper exists and says what was claimed.** Paraphrase attacks achieved **100% conditional removal** on KGW and Unigram and **98.3%** on SynthID-Text. And the number that matters more: **baseline false-negative rates before any attack of 70% (KGW), 83% (Unigram), 80% (SynthID)** — the detectors miss most watermarked text with nobody attacking them at all.

**Not established:** star and fork accuracy (page-stated 15.4k / 1.7k / 66; the GitHub API is mocked in this environment, so **no viral-velocity claim**); the "4,102 stars in 48 hours" figure (single weak social source); whether removal defeats any real vendor detector; Meyer's role beyond his public profile; issue and PR contents; the EU Code of Practice publication dates.

---

## 11. What this means for hireui

**The direction is inverted, and that is the useful part.** This tool removes marks from output *you* generated. The live question in hireui is the opposite: detecting AI authorship in candidate *input*.

Read defensively, `image_meta.py` and `container_meta.py` are a 150KB+ per-format inventory of **where provenance actually lives** — which is exactly the map of what an upload pipeline must **preserve** rather than silently destroy on re-encode. `score_stylometry.py` is zero-LLM cadence scoring.

**The hard limit, and it is hard.** An absent mark is not evidence of human authorship — that is the converse of `ethics.md:18`, and the forensic-readiness paper puts numbers on it: detectors miss **70–83%** of watermarked text unattacked. A stylometric AI-detector pointed at candidates would produce false accusations, disproportionately against non-native English writers, on a legally protected decision. **Do not build one.**

The three things worth taking are in the Pilot Methods Menu. The tool itself should not be installed — not on security grounds, but because recruitment is precisely the context the subject's own `ethics.md:14-16` places out of bounds.
