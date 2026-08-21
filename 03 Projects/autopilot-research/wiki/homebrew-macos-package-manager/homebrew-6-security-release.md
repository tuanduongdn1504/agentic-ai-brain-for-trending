# Homebrew 6.0.0 — the release that stopped trusting strangers

## Source

- **Better Stack**, *"Homebrew 6.0 Just Changed How Your Mac Installs Software"* — [`IwzVzvDw68w`](https://www.youtube.com/watch?v=IwzVzvDw68w), 2026-07-29, 5:13, 52,132 views. The most consequential source in the bundle.
- Verified against the primary announcement at `brew.sh` (**2026-06-11**), `docs.brew.sh/Support-Tiers`, `docs.brew.sh/Tap-Trust`, and the `Homebrew/brew` issue tracker.

Better Stack opens by eating its own words: *"we made a whole video that basically called Homebrew this Stone Age thing we use because Nix runs circles around it."* Note the direction — this is a Nix advocate conceding.

## The headline is not features

> *"The headlines isn't a pile of new features, it's a complete security"* overhaul.

For essentially Homebrew's whole life, adding a third-party tap meant Homebrew would execute that repository's Ruby. Better Stack: *"It would just execute their code. Any tap, arbitrary code, without really any questions asked."*

The announcement says the same thing in the vendor's own voice, which is more damning coming from them:

> *"A third-party tap can contain arbitrary, unsandboxed Ruby that runs on your machine, so Homebrew now requires taps (and tap-qualified formulae and casks) to be explicitly trusted before their code is evaluated or run."*

Better Stack's framing of why now: *"Package managers are the number one target for supply chain attacks right now. NPM, all of them getting hit over and over. We'll just run whatever code the repo hands us is a bad default."*

## What shipped

| Feature | Better Stack's description | Primary source |
|---|---|---|
| **Tap trust** | Untrusted taps blocked until `brew trust` | Confirmed. Official taps trusted out of the box |
| **`ask` mode** | Shows a summary and waits for yes; *"on by default for devs"* | Confirmed: *"Making `ask` mode the default for developers, so `brew install` and `brew upgrade` show a dependency summary and confirmation prompt before making changes"* |
| **`brew exec`** | *"basically is npx for Homebrew"* — run a tool once without permanently installing it | Confirmed, **but the command is `brew exec`, not `brew execute`** as the video says. Announcement: *"like `npx`"*, and it *"supports formulae environments"* |
| **`brew vulns`** | Scans installed packages against known advisories | Confirmed, **and the video's audio renders it "brew volumes"**. Also more qualified than stated: it is *"a new Homebrew tap and subcommand"* — not plain core |
| **Internal JSON API default** | *"all your package info comes down in one clean download instead of a dozen little network trips"* so `brew update` is faster | The default-switch is confirmed. The mechanism and the speed claim are the video's explanation, not the announcement's wording |
| **Three security fixes** | Including *"one that could run code as root through the Mac installer package"* | Confirmed — three advisories, and specifically **GHSA-6689-q779-c33m**: root code execution via **Git hooks in the macOS `.pkg` postinstall** |
| **M5 support** | *"It even adds support for the new M5 chips"* | Confirmed but narrower: *"Homebrew adds M5 and M5 Pro/Max CPU recognition"* — recognition, not a broader capability |
| **Intel retirement** | *"spells out the timeline for retiring Intel support over the next couple of years"* | Confirmed and far more specific: **Tier 3 in September 2026, unsupported entirely September 2027** |

## The Rust myth, killed

> *"A lot of things are getting rewritten in Rust. No, Homebrew is not getting rewritten in Rust, at least not now. That was a whole experiment. The focus is right back on the Ruby codebase as it always was."*

Correct, and the reason is more interesting than the fact: the `brew-rs` experiment *"has concluded"* because **Rust showed no performance gains on representative full installs.** A negative result, published. Worth noting next to the anchor's argument that Homebrew's Ruby formulae are the reason it won ([[why-homebrew-won]]) — the Ruby is load-bearing socially, not just technically.

## The breaking change, and where the video simplifies

Better Stack is right that this is the thing that bites:

> *"Tap trust is the breaking change. If you've got CI pipelines that lean on third-party taps, brew doctor now throws an error the moment it sees an untrusted one. And a huge number of standard GitHub actions run brew doctor as their very first step. So, people upgraded, and their build just started failing."*

All confirmed. The tracker has it as `Homebrew/brew` issue **#22494** — *"brew doctor untrusted-tap check fails test-bot CI for third-party taps"*, logged as a regression from #22470. `brew doctor` exits non-zero when untrusted taps are present, and the standard `brew test-bot` GitHub Actions workflow runs `brew doctor` first, so **essentially every third-party tap's CI failed at once.**

**Where the video simplifies:** it attributes this to 6.0. The enforcement actually merged **2026-05-30**, the trust option surfaced as early as **5.1.15**, and it became the default *"in Homebrew 6.0.0 or 5.2.0, whichever comes first."* So the breakage predates the 6.0 announcement for anyone tracking a development channel. If you are reconstructing a timeline of when your CI broke, 6.0.0's date will mislead you.

### Fixing it

| Fix | What it does |
|---|---|
| `brew trust user/repo` | Trusts the whole tap |
| `brew install user/repo/formula` | Installs one tap-qualified item **without** trusting the whole tap |
| `HOMEBREW_NO_REQUIRE_TAP_TRUST=1` | CI escape hatch — **explicitly temporary.** Homebrew's stated intent is to make trust mandatory |

`Homebrew/actions` PR **#860** fixed the official actions by using `brew trust` so setup output shows the trust decision, rather than by suppressing the check. That is the right pattern to copy: **make the trust decision visible, don't silence the checker.**

Two rough edges still open at time of writing: `brew trust --formula` — which `brew` itself suggests — returns `Error: Invalid usage` (issue **#22685**), and `brew bundle` has been failing for taps that *are* trusted (issue **#22631**). If you hit either, you are not doing it wrong.

## Ask mode's quieter hazard

> *"Same story with the ask mode. If you've got scripts that quietly assumed brew installs without asking, that new prompt can leave them hanging forever."*

A confirmation prompt in a non-interactive context does not fail — it **hangs**. That failure mode is worse than an error because nothing in the logs says what happened. Any unattended automation that shells out to `brew install` needs auditing for this, including scheduled jobs. This vault runs `brew`-provided binaries from a launchd job nightly; it does not invoke `brew install`, so it is not exposed today, but that is a property worth not losing.

## The verdict, and the sentence worth keeping

Better Stack's recommendation: upgrade — *"You're getting three security fixes and frankly brew update is going to walk you onto 6.0 whether you plan for it or not."* Slow down only if you run CI touching third-party taps, or automation expecting silent installs.

And the closing framing, which is the honest summary of the release:

> *"For years, Homebrew was a convenience … With 6.0, it looks like it's turned itself into more of a checkpoint, a place where the code coming onto the machine finally has to prove it's trusted. The package manager caught up to the threat model the rest of us have been living inside for years."*

## The six-year arc this bundle accidentally captured

Put the 2020 source next to the 2026 one. In [[why-macos-has-no-package-manager|the 2020 Hands-On Mac episode]], Leo Laporte names the `curl | bash` risk explicitly — *"you really don't want to run random installer programs you've downloaded on the internet"* — and then resolves it on brand reputation: *"in this case it's safe to do so because it's brew."*

Six years later Homebrew itself stopped accepting that argument on behalf of its users. Trust-the-brand was the 2020 answer; **trust-nothing-by-default is the 2026 answer, shipped by the brand being trusted.** Neither source knows about the other. That contrast is the most valuable thing the recency-relaxed bundle produced ([[source-provenance]]).

## Cross-links

[[this-machine-audit]] — three third-party taps live on this machine, and it is already on 6.0.3 · [[the-three-weaknesses]] · [[terminology-and-commands]] · [[../api-security-7-techniques/_index|api-security-7-techniques]] — tap trust is a supply-chain control of the kind that topic inventories · [[../fullstack-docker-cicd/_index|fullstack-docker-cicd]]
