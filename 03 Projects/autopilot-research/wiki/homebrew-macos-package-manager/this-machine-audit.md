# This machine: a dual-install audit, and a deadline

> **This article is original to this ingest.** No source in the bundle discusses it. It exists because the topic was justified on the grounds that `brew` is this project's only system-wide dependency — so the ingest audited the actual machine instead of only reading about the tool.
> **All figures measured 2026-08-21** on the host running the autopilot-research pipeline.

## What was measured

```
uname -m                    arm64
machdep.cpu.brand_string    Apple M4 Pro
sw_vers                     macOS 26.3.1 (build 25D771280a)
```

Two Homebrew installations are present:

| | `/usr/local` | `/opt/homebrew` |
|---|---|---|
| `brew --version` | **6.0.3** | **5.1.9** |
| `brew config` → `macOS:` | `26.3.1-**x86_64**` | `26.3.1-**arm64**` |
| `brew config` → `Rosetta 2:` | **`true`** | `false` |
| `brew config` → `CPU:` | `dodeca-core 64-bit **westmere**` | — |
| Formulae in `Cellar` | **105** | **27** |
| Position in `PATH` | **first** | after |

`which -a brew` returns `/usr/local/bin/brew` before `/opt/homebrew/bin/brew`, every time it repeats.

## The diagnosis

**The primary Homebrew on an Apple M4 Pro is the Intel `x86_64` build, running under Rosetta 2 translation.** `westmere` is not this CPU — it is what Rosetta reports to a translated process. The native arm64 install exists but is secondary, holds a quarter as many packages, and is **a full major version behind** (5.1.9 vs 6.0.3), which means it has not been driven by `brew update` in a long time.

This is not cosmetic. It propagates all the way into this project's Python:

```
file /usr/local/opt/python@3.12/bin/python3.12
  → Mach-O 64-bit executable **x86_64**

file "03 Projects/autopilot-research/.venv/bin/python"
  → Mach-O 64-bit executable **x86_64**
```

So the entire research pipeline — `notebooklm-py`, `httpx`, Playwright and its bundled Chromium, every dependency in the ~700 MB project venv — is **x86_64 executing under translation on Apple silicon.** `yt-dlp 2026.6.9` likewise resolves through `/usr/local/Cellar`.

### This explains the note nobody had explained

The project `CLAUDE.md` setup section carries this workaround:

> *"NOTE: this user's `python3` shim was broken — use the absolute path to brew Python 3.12"*

and `bin/autopilot-env.sh` hardcodes `/usr/local/opt/python@3.12/bin/python3.12`.

Two Homebrew prefixes on one machine, with the Intel one winning `PATH`, is the textbook cause of exactly that symptom. `/opt/homebrew/Cellar` contains `python@3.14`; `/usr/local/Cellar` contains `python@3.12` at 3.12.13. Whichever `python3` a shell resolves depends on which prefix won the `PATH` race in that shell. The hardcoded absolute path is a correct workaround for an undiagnosed cause — **the cause is now diagnosed.**

A second, smaller finding: `PATH` contains **over 150 entries**, with `/usr/local/bin` and `/opt/homebrew/bin` each repeating roughly ten times. A shell profile is being sourced repeatedly. That is harmless until it isn't — it is also why the ordering is stable in favour of `/usr/local`.

### Why /opt/homebrew exists at all

Its `Cellar` is mostly a C++ dependency tree — `boost`, `folly`, `fbthrift`, `fizz`, `edencommon`, `fb303`, `glog`, `gflags`. Those are Meta libraries, and `~/Library/LaunchAgents/com.github.facebook.watchman.plist` is loaded on this machine. The native install looks like it was created as **collateral of installing `watchman`**, not as a deliberate migration. That matters for the recommendation below: there is no half-finished migration to resume, only an accidental second prefix.

## The deadline

Homebrew 6.0.0's announcement states the Intel timeline outright:

> *"In September 2026, macOS Intel `x86_64` moves to Tier 3 … in September 2027, macOS Intel `x86_64` will be unsupported entirely."*

And `docs.brew.sh/Support-Tiers` defines what Tier 3 means:

> *"A Tier 3 configuration is not supported. These configurations fall far outside Homebrew's testing infrastructure and may fail to function reliably."*
> *"CI coverage is unavailable; bottles will rarely be built or published."*
> *"Issues affecting only these configurations may be closed without response."*
> *"Functionality may regress intentionally if it benefits supported configurations."*

**September 2026 is next month.** Nothing breaks on that date. What changes is that the `/usr/local` prefix stops reliably receiving **bottles** — the prebuilt binaries — so `brew upgrade` there increasingly falls back to compiling from source.

Read that against the anchor's central argument. Homebrew beat MacPorts by **trusting the system and pouring prebuilt bottles instead of brewing everything from source** ([[why-homebrew-won]]). Tier 3 removes the bottles. A machine on Tier 3 gets the MacPorts experience — *"những buổi chiều ngồi nhìn máy build từ mã nguồn"*, afternoons spent watching it build from source — while paying Rosetta's translation cost on top.

This machine is on the deprecated platform **despite the hardware being Apple silicon**. That is the part worth sitting with: the deprecation is aimed at Intel *Macs*, and this is not one. It is caught by prefix, not by hardware.

## Tap trust status

Four taps are installed:

| Tap | Official? | Needs explicit trust under 6.0 |
|---|---|---|
| `homebrew/services` | **yes** | no — official taps are trusted out of the box |
| `dart-lang/dart` | no | **yes** |
| `heroku/brew` | no | **yes** |
| `oven-sh/bun` | no | **yes** |

Three third-party taps. Under the 6.0 regime their Ruby is not evaluated until trusted ([[homebrew-6-security-release]]). `brew update` still *updates* them — the observed auto-update refreshed `oven-sh/bun` and `dart-lang/dart` without complaint — because trust gates **evaluation and execution**, not fetching. The bill arrives at install time, and at `brew doctor`.

**Not verified here:** whether these three are already marked trusted in this machine's config. `brew doctor` was not run to completion during the audit. That check is listed as an unresolved item in [[claims-scorecard]] rather than guessed at.

## What to do

These are **recommendations, not applied changes** — per librarian discipline, and because a prefix migration is the operator's call, not an ingest's.

**Step 0 — decide the question, which is not "which is faster".** It is: *do you want this pipeline on a platform that upstream supports after September 2026?* If yes, the work is a migration. If no, the work is documenting the acceptance.

**Step 1 — see the actual scope, one command:**

```bash
/opt/homebrew/bin/brew bundle dump --file=/tmp/native.Brewfile --force && /usr/local/bin/brew bundle dump --file=/tmp/intel.Brewfile --force && wc -l /tmp/native.Brewfile /tmp/intel.Brewfile
```

**Step 2 — check the tap-trust exposure before it bites:**

```bash
/usr/local/bin/brew doctor
```

**Step 3 — if migrating, treat `/tmp/intel.Brewfile` as a *shopping list, not a manifest*.** It records names without versions ([[the-three-weaknesses]]), so `brew bundle install` against the native prefix installs *today's* versions, not the ones currently working. That is the reproducibility gap this bundle documents, met in practice. Reinstall deliberately, and rebuild the project venv from a **native** Python afterwards — the venv cannot be migrated in place, since its interpreter is an x86_64 Mach-O.

**Step 4 — fix `PATH` ordering and stop re-sourcing the profile.** Whichever prefix you choose, it must win unambiguously and once. Until then, `bin/autopilot-env.sh`'s hardcoded absolute path is doing real work and should stay.

**Do not** run `brew upgrade` on `/usr/local` as a first move. It is the single action most likely to change 105 packages under a translation layer on a platform heading to Tier 3, with no rollback ([[the-three-weaknesses]]).

## Cross-links

[[homebrew-6-security-release]] · [[the-three-weaknesses]] · [[why-homebrew-won]] · [[../local-llm-coding-hardware-ladder/_index|local-llm-coding-hardware-ladder]] — the same M4 Pro, measured for a different reason; that topic established the machine's identity as an M4 Pro by inference, and this one confirms it directly from `machdep.cpu.brand_string`.
