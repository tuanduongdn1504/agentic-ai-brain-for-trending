# Caveats and corrections

## 1. The bundle contradicts itself on the first sentence, and it is not averaged

The anchor spends its first minute arguing against a specific framing:

> *"Đa số mọi người nghĩ nó như kiểu là một cái App Store cho dân kỹ thuật. **Điều này sai** và cái sai đó làm bạn bỏ lỡ những điều sau đây."*

Easy Tech Steps' very first sentence:

> *"Home Brew is basically like a second App Store for your Mac."*

**Which is right?** The anchor, on the merits — and the disagreement is not symmetrical. Easy Tech Steps' framing is *adequate for its own audience*: it is a video about installing Chrome and Firefox from the terminal, where "App Store you type into" is a serviceable mental model. It becomes wrong exactly when you need the thing a package manager does that a store does not — resolve a dependency graph, know what becomes orphaned on removal, tell you what will change before it changes.

Per Rule 7, the resolution is stated rather than blended: **the ledger framing is the one this wiki uses**, because everything else in the topic depends on it. C1–C2 in [[claims-scorecard]] (no version pinning, no lockfile) are only interesting *because* the thing is supposed to be a ledger. Under the App Store framing they are not defects at all — app stores do not pin versions either.

## 2. Caption garble that had to be normalized

The anchor's Vietnamese auto-captions mangle nearly every proper noun. Normalizations applied, all phonetically transparent:

| Caption | Actual |
|---|---|
| Home Ru / Hom Ru / Hom Brew / HRU | **Homebrew** |
| Max Hell / Maxell / Max Soell / Hwell / How well | **Max Howell** |
| Mark Post / MaP / Marpost | **MacPorts** |
| F ra / Fing | **Fink** |
| Marcos / Maos / MOS OS / M OS / Maxell (context-dependent) | **macOS** |
| Katanina | **Catalina** |
| Nyx / Nick | **Nix** |
| Bass | **bash** |
| lip PNG / relip / silip | **libpng** / library |
| free type | **FreeType** |
| lip tip | **libtiff** |
| seller | **Cellar** |
| tab | **tap** |
| c / thùng gỗ | **cask** |
| Botter | **bottle** |
| IMH Magic | **ImageMagick** |
| note | **node** |
| log file / package log.jonation | **lockfile** / `package-lock.json` |
| Camfile | **Gemfile.lock** |
| "brew version install" | **`brew version-install`** |
| lead code số 226 | **LeetCode #226** |
| "JP" | ⚠️ **unresolved — see below** |

⚠️ **One garble was NOT resolved and must not be guessed at in prose.** The anchor names a compression library, born 1995, written by two people, sitting underneath `libpng`, FreeType and `libtiff`. The captions render it *"JP"* / *"JPI"* throughout. **zlib** is the only library matching every stated property, and all three named consumers do depend on zlib — but that identification is this ingest's inference, and neither the 1995 date nor the two-author detail was verified. Graded **UNVERIFIED** (B11). The wiki refers to it as *"one compression library"* rather than naming it.

Per the project's **discard-as-garble guard**, garble was not used as grounds to discard substance: every claim behind a mangled name was checked on its merits, and the anchor's ideas survived even where its audio did not. That asymmetry is the headline result of [[claims-scorecard]] — **4 of 5 CORRECTED grades are rendering failures, not reasoning failures.**

## 3. Better Stack's audio produced two wrong command names

Distinct from the anchor's Vietnamese captions — these are English:

- *"brew execute"* → the command is **`brew exec`**
- *"brew volumes"* → the command is **`brew vulns`**

Both would fail if typed as heard. `brew vulns` is also **more qualified** than presented: the announcement calls it *"a new Homebrew tap and subcommand"*, so it is not straightforwardly core.

## 4. Better Stack misdates its own breaking change

Graded MISLEADING (A10) rather than false, because every component is true. Tap-trust enforcement merged **2026-05-30**; the trust option appeared as early as **5.1.15**; the default landed in *"Homebrew 6.0.0 or 5.2.0, whichever comes first."* The 6.0.0 announcement is dated **2026-06-11** and the video is **2026-07-29**.

**Why it matters practically:** anyone diagnosing "when did my CI start failing?" from the 6.0 date will search five-plus weeks too late.

## 5. Staleness, which the rubric guaranteed

Three of six sources predate Homebrew 6.0 substantially, and one predates Apple silicon. This was not an accident — see [[source-provenance]]: the recency filter could not be satisfied on this topic and relaxed on every query tried.

| Source | Date | Stale in what way |
|---|---|---|
| Hands-On Apple (Laporte) | **2020-05** | **Six months before the M1.** Nothing on `/opt/homebrew` vs `/usr/local` — the distinction did not exist. On screen: *"these are the four processors, actually there's eight because of hyper threading"* — an Intel Mac. Everything it says about the Cellar-plus-symlink design remains accurate |
| Warp | **2023-07** | Quotes the old tagline (*"the missing package manager for macOS"*; now **"The Package Manager for Everywhere"**). Recommends `exa`, unverified here |
| Dev Neil A | **2025-12** | Pre-6.0: no tap trust, no `ask` mode. Its command coverage is otherwise the best in the bundle |
| Easy Tech Steps | **2026-03** | Pre-6.0. Install analytics figures are point-in-time |
| Better Stack | **2026-07** | Current, with the dating error above |
| Anchor (Kunkka) | **2026-08** | Current. ⚠️ **Does not mention 6.0 at all** — see below |

## 6. The anchor's most significant omission

The anchor's whole third act is that Homebrew traded away pinning, rollback and reproducibility, and that its openness is the price of its success. It was published **2026-08-10, two months after 6.0.0**, and **never mentions 6.0 or tap trust.**

That matters because 6.0 is a *partial answer to his own critique*: `brew vulns` addresses the security-maintenance burden he correctly identifies as falling on the user (C4), and tap trust puts a gate on precisely the "a stranger can fix it at 2am" openness he names as the winning property. His argument is not refuted by 6.0 — the pinning and rollback gaps are untouched and Homebrew still says don't pin — but it is **incomplete as of its own publication date.**

## 7. A silent-failure bug in this ingest's own fetch method

Found and worked around during this run, and worth recording because it is a **fail-loud violation** of the kind CLAUDE.md Rule 12 exists to catch.

Fetching captions for all six videos with:

```bash
yt-dlp --write-auto-subs --write-subs --sub-langs "en.*,vi.*" ...
```

produced caption files for the five English videos and **nothing at all for the Vietnamese anchor** — no error, no warning, **exit code 0**. The glob `vi.*` matched no track. Naming the track explicitly worked immediately:

```bash
yt-dlp --write-auto-subs --sub-langs "vi-orig" ...   # → 158 KB
```

**The hazard:** a `--sub-langs` glob that matches nothing is indistinguishable from success. Had this run not checked the output file list, the anchor would have been "ingested" with an empty transcript, and a wiki would have been written about five sources while claiming six. The anchor-validation grader in `bin/autopilot-drain.py` would **not** have caught it — it validates that anchors survive *selection*, not that their *content* was retrieved.

**Recommended (not applied):** the caption-fetch step should assert that one output file exists per selected video before compiling, and fail loudly otherwise. That is a code grader of exactly the shape `validate_anchors()` already establishes. Filed as a deepen candidate in [[source-provenance]].

## 8. Sponsored content in one source

The 2020 Hands-On Mac episode carries read advertisements for LastPass and Hover, and repeated `hover.com/twit` calls to action. No technical claim in it appears sponsor-influenced, and none of the graded claims derive from ad segments — but the source is a sponsored consumer show, not independent documentation.

## 9. What this ingest did not check

Stated so the gaps are not mistaken for coverage:

- **Whether this machine's three third-party taps are already marked trusted.** `brew doctor` was not run to completion ([[this-machine-audit]] step 2 recommends it).
- **`exa`'s current status** (E7).
- **zlib's identity, birth year and authorship** (B11).
- **LeetCode #226 directly** — `leetcode.com` returned HTTP 403 (D5).
- **NeXTSTEP app-bundle lineage and the 1997 date** (B5).
- **Laporte's "at least nine package managers" count** (E8).
- **Rosetta 2's own deprecation timeline**, which would sharpen [[this-machine-audit]]'s urgency in either direction. Deliberately not asserted, since an unverified claim about it would be the most consequential possible error in this topic.
