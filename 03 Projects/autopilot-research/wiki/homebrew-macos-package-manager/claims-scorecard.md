# Claims scorecard

> **Method.** Every checkable factual claim made by the six sources, graded against primary sources where one exists. Grades: **CONFIRMED** (primary source agrees) · **CBI** (correct-but-incomplete, or corroborated only secondarily) · **CORRECTED** (substance right, detail wrong) · **MISLEADING** (true as stated but leads to a wrong conclusion) · **TIME-BOUND** (was true, expires) · **UNVERIFIED** (not checked this run — do not repeat as fact) · **FABRICATED** (no basis).
> Primary sources used: `brew.sh` 6.0.0 announcement (2026-06-11) · `docs.brew.sh/Versions` · `docs.brew.sh/Support-Tiers` · `docs.brew.sh/Tap-Trust` · `Homebrew/brew` issue tracker · Wikipedia (Homebrew, MacPorts, Fink) · `x.com/mxcl` · direct measurement of this machine.

## A — Homebrew 6.0 (Better Stack)

| # | Claim | Grade | Note |
|---|---|---|---|
| A1 | 6.0's headline is a security overhaul, not features | **CONFIRMED** | The announcement leads with tap trust and advisories |
| A2 | Third-party taps must now be explicitly trusted before their code is evaluated or run | **CONFIRMED** | Verbatim in the announcement |
| A3 | Before this, any tap's Ruby was executed *"without really any questions asked"* | **CONFIRMED** | Vendor's own framing: *"arbitrary, unsandboxed Ruby that runs on your machine"* |
| A4 | Official Homebrew taps are trusted out of the box | **CONFIRMED** | |
| A5 | `ask` mode is now default for developers — summary + confirmation before changes | **CONFIRMED** | Applies to `brew install` **and** `brew upgrade` |
| A6 | *"There's a brand new command **brew execute**"*, npx-like | **CORRECTED** | The command is **`brew exec`** |
| A7 | *"There's **brew volumes**"*, which scans for known advisories | **CORRECTED** | The command is **`brew vulns`**, and it is *"a new Homebrew tap and subcommand"* — not plain core |
| A8 | Internal metadata now default ⇒ one download instead of *"a dozen little network trips"* ⇒ faster `brew update` | **CBI** | The default-switch to the internal JSON API is confirmed. The mechanism and the speed claim are his gloss, not the announcement's |
| A9 | 6.0 patched three security holes, one allowing root code execution via the Mac installer package | **CONFIRMED** | Three advisories; **GHSA-6689-q779-c33m** — root execution via Git hooks in the macOS `.pkg` postinstall |
| A10 | `brew doctor` now errors on untrusted taps, and because GitHub Actions run it first, builds started failing | **MISLEADING** | Every element is true, but attributing it to **6.0** misdates it. Enforcement merged **2026-05-30**; the trust option appeared in **5.1.15**; default landed in *"6.0.0 or 5.2.0, whichever comes first."* Issue **#22494** |
| A11 | Homebrew is **not** being rewritten in Rust; that was an experiment | **CONFIRMED** | `brew-rs` *"has concluded"* — **no performance gains on representative full installs** |
| A12 | 6.0 *"spells out the timeline for retiring Intel support over the next couple of years"* | **CONFIRMED** | And sharper than stated: **Tier 3 September 2026**, unsupported entirely **September 2027** |
| A13 | *"It even adds support for the new M5 chips"* | **CORRECTED** | Narrower: *"M5 and M5 Pro/Max **CPU recognition**"* |
| A14 | Ask mode can leave scripts *"hanging forever"* | **CONFIRMED** | A prompt in a non-interactive context hangs rather than failing |

## B — History and design (anchor)

| # | Claim | Grade | Note |
|---|---|---|---|
| B1 | Homebrew was written in **2009** by Max Howell | **CONFIRMED** | |
| B2 | Homebrew arrived **eight years** after the earlier package managers | **CONFIRMED** | Fink Dec 2000 → Homebrew 2009 |
| B3 | Fink began *"around 2001"* and took Debian's packaging wholesale | **CORRECTED** on date, **CONFIRMED** on substance | Started **December 2000** by Christoph Pfisterer; genuinely uses **dpkg and APT** |
| B4 | MacPorts began **2002** from the **OpenDarwin** project, i.e. with roots in Apple itself | **CONFIRMED** | Originally **DarwinPorts**; Apple employees involved (Landon Fuller, Kevin Van Vechten, Jordan Hubbard); later hosted on Apple's Mac OS Forge |
| B5 | A `.app` is a directory containing the app's own libraries; the idea came from **NeXTSTEP** and returned to Apple in **1997** | **CBI** | The bundle mechanism is uncontroversial; the NeXTSTEP lineage and 1997 date were not primary-verified this run |
| B6 | macOS shipped **bash 3.2** for ~13 years because bash 4+ moved to **GPLv3**, whose anti-tivoization and patent clauses Apple would not accept | **CONFIRMED** | Confirmed in detail, including the specific clause — *"prohibits vendors from using GPL-licensed code on systems that prevent third parties from installing their own software"* |
| B7 | macOS **Catalina, 2019**, quietly switched the default shell to one with a friendlier licence | **CONFIRMED** | zsh **5.7.1**, MIT |
| B8 | bash 3.2 was *"contemporary with the first iPhone"* | **CORRECTED** | bash 3.2 is **October 2006**; the first iPhone is **June 2007**. Same era, but it precedes it |
| B9 | **macOS 12.3** removed Python 2 and apps depending on it *"died the moment they opened"* | **CONFIRMED** | Monterey 12.3 removed Python 2.7 at `/usr/bin/python`; apps crashed on launch — and it landed in a **point release** |
| B10 | A formula is a short Ruby file an ordinary person can read | **CONFIRMED** | Ruby scripts on Homebrew's DSL |
| B11 | One compression library, born **1995**, written by **exactly two people**, sits under `libpng`, FreeType and `libtiff` | **UNVERIFIED** | ⚠️ The caption renders the library name as *"JP"* — unintelligible. zlib is the only candidate that fits every stated property, but **the identification is this ingest's inference and the 1995/two-authors details were not checked.** Do not repeat as fact |
| B12 | Apple ships Unix tools then freezes them, so *"Apple decides which version ships and for how long"* | **CONFIRMED** | B6 and B9 are two independent instances |

## C — The three weaknesses (anchor)

| # | Claim | Grade | Note |
|---|---|---|---|
| C1 | The exported package list records **names only, no versions**, so `brew install node` means "newest at the instant you press enter" | **CONFIRMED** | Demonstrated independently by Dev Neil A's `brew bundle dump` |
| C2 | Homebrew's docs say they have no lockfile and never will — a deliberate choice | **CONFIRMED** | `brew bundle` *"does not pin versions or add lock file support"* |
| C3 | There is no `dnf history undo` equivalent; `brew extract` / *"brew version install"* extract an old formula into your own tap rather than restoring state, and maintenance becomes yours | **CONFIRMED**, command **CORRECTED** | The command is **`brew version-install`** (hyphenated). Docs confirm the ownership transfer, including security patches |
| C4 | Homebrew explicitly advises against using its versions to pin | **CONFIRMED** | Verbatim: *"Homebrew's versions should not be used to 'pin' formulae to your personal requirements"* |
| C5 | Multiple versioned formulae exist for popular software (`node@20` beside latest) but the list is limited | **CONFIRMED** | |

## D — The Howell story (anchor)

| # | Claim | Grade | Note |
|---|---|---|---|
| D1 | June 2015 tweet, wording as quoted | **CONFIRMED** | [status 608682016205344768](https://x.com/mxcl/status/608682016205344768) |
| D2 | Howell studied **chemistry**, not computer science | **CONFIRMED** | Master's in chemistry; left the field, came to software via open source (Last.fm, then TweetDeck) |
| D3 | Howell later spoke in Google's defence, and said the feedback raised **several** weaknesses, not just the one problem | **CONFIRMED** | This is the claim the video exists to make, and it holds |
| D4 | He said he did not really know what a binary tree **was** | **CBI** | Substance corroborated; that exact self-description not primary-sourced here |
| D5 | Inverting a binary tree is **LeetCode #226** | **CBI** | ⚠️ `leetcode.com` returned **HTTP 403** to this ingest. Secondary references agree on #226 |
| D6 | Millions grind #226 *"partly because in 2015 a guy was annoyed on Twitter"* | **UNFALSIFIABLE** | His interpretation. The defensible weak form is in [[the-howell-interview-story]] |

## E — Tutorials and ecosystem

| # | Claim | Grade | Note |
|---|---|---|---|
| E1 | Formulae are CLI tools; casks are GUI apps | **CONFIRMED** | Stated by three sources independently |
| E2 | `brew bundle dump` writes a `Brewfile` listing formulae, casks **and VS Code extensions** | **CONFIRMED** | Demonstrated on screen (Dev Neil A) |
| E3 | Some casks self-update (Chrome, Firefox, VS Code), so `brew upgrade` does not manage them; others (pgAdmin 4) Homebrew tracks — set per cask | **CONFIRMED** | Demonstrated; the only source to surface this trap |
| E4 | Homebrew installs into its own tree and **symlinks** into `PATH`, making uninstall easy and avoiding collisions with Apple's utilities | **CONFIRMED** | Laporte, 2020 — still the design in 2026, and the reason `--prefix` is the isolation boundary |
| E5 | `formulae.brew.sh` 365-day analytics: PowerShell **655,000**, Chrome **347,000** | **TIME-BOUND** | Point-in-time, ~2026-03, rolling window. The method transfers; the numbers do not |
| E6 | *"Homebrew is the missing package manager for macOS"* | **TIME-BOUND** | Was the tagline. `brew.sh` now reads **"The Package Manager for Everywhere"** — Linux and WSL are supported |
| E7 | `exa` is the modern `ls` replacement to install | **UNVERIFIED** | Warp, 2023. Not checked this run; treat as a staleness flag, not a recommendation |
| E8 | There are *"at least nine"* macOS package managers | **UNVERIFIED** | Laporte's own count, 2020 |
| E9 | Homebrew is *"basically like a second App Store for your Mac"* | **CONTRADICTED IN-BUNDLE** | The anchor's opening argument is that this framing *"is wrong"*. Not averaged — see [[caveats-and-corrections]] |

## F — This machine (measured directly, not source claims)

All measured 2026-08-21. These are observations, not gradeable claims, and are recorded so the audit in [[this-machine-audit]] is reproducible.

| Measurement | Value |
|---|---|
| Hardware / OS | **Apple M4 Pro**, `arm64`, macOS **26.3.1** (25D771280a) |
| `/usr/local` prefix | Homebrew **6.0.3**, `macOS: 26.3.1-x86_64`, **`Rosetta 2: true`**, `CPU: dodeca-core 64-bit westmere`, **105** formulae, **first on `PATH`** |
| `/opt/homebrew` prefix | Homebrew **5.1.9**, `macOS: 26.3.1-arm64`, `Rosetta 2: false`, **27** formulae |
| `python@3.12` | 3.12.13, `Mach-O 64-bit executable **x86_64**` |
| Project `.venv/bin/python` | `Mach-O 64-bit executable **x86_64**` |
| `yt-dlp` | 2026.6.9, resolved from `/usr/local/Cellar` |
| Taps | `homebrew/services` (official) + `dart-lang/dart`, `heroku/brew`, `oven-sh/bun` (third-party) |
| `PATH` entries | **>150**, with both prefixes repeating ~10× each |

## Theses (not gradeable, recorded as positions)

- **Anchor:** a package manager's value is the ledger, not the download — *"giống như một cuốn sổ kế toán"*. Recorded as the topic's organising idea; it predicts C1–C2.
- **Anchor:** Homebrew won on **contribution cost**, not correctness. Argued in [[why-homebrew-won]]; the `brew-rs` outcome (A11) is consistent with it 16 years on.
- **Anchor:** *"no free lunch — only which invoice you choose to pay"*, Homebrew for laptops, Nix for build servers. Better Stack independently places the boundary in the same place.
- **Anchor:** good naming is a form of documentation. Demonstrated live by `Pouring` during this ingest ([[terminology-and-commands]]).

## Tally

**46 gradeable claims:** **29 CONFIRMED** · **5 CORRECTED** · **4 CBI** · **3 UNVERIFIED** · **2 TIME-BOUND** · **1 MISLEADING** · **1 UNFALSIFIABLE** · **1 CONTRADICTED IN-BUNDLE** · **0 FABRICATED.**

Per section: A=14, B=12, C=5, D=6, E=9. Counted mechanically from this file's own table, not by hand — the first hand-tally of this scorecard was wrong (38), which is why the corpus rule from `deepseek-harness` is *"tally the table, don't hand-count it."* The script is at `scratchpad/tally.py`; re-running it against this file reproduces the figures above.

Two patterns worth naming:

1. **The anchor's substance survived verification almost intact; its *audio* did not.** Every one of the four CORRECTED grades is a caption-rendering failure or an off-by-months date, not a wrong idea. Its three central critiques (C1–C4) are confirmed verbatim by Homebrew's own documentation — which is the strongest result any source in this bundle achieved.
2. **The single MISLEADING grade is a dating error, not a factual one.** Better Stack attributes the CI breakage to 6.0; it began five weeks earlier on a development channel. Anyone reconstructing when their CI broke from the 6.0 date will look in the wrong place.
