# The beer metaphor, and the actual command surface

## Naming as documentation

The anchor's best-argued small point. Homebrew means brewing beer at home, and the naming is not decoration — installing this way *"về bản chất chính là bạn tự nấu nó ra từ mã nguồn"*, is essentially cooking it yourself from source.

| Term | Beer | Software |
|---|---|---|
| `brew` | to brew | the command |
| **formula** | the recipe | the file describing how to build a package — a short Ruby script on Homebrew's DSL |
| **Cellar** | the wine/beer cellar | the directory holding everything installed |
| **tap** | opening a beer tap | a third-party repository |
| **cask** | the wooden barrel | a GUI application |
| **bottle** | the bottle | **a pre-built binary** |

The payoff is `bottle`:

> *"Bottle là bản binary đã được build sẵn từ trước, nên thay vì để máy bạn ngồi nấu lại từ đầu thì Homebrew chỉ việc tải bản có sẵn đó rồi rót ra cho bạn. Cho nên lần tới khi bạn cài phần mềm và thấy hiện lên dòng chữ `Pouring` — nghĩa là đang rót — thì nó đang nói với bạn theo nghĩa đen rằng: khỏi nấu đâu, có chai sẵn rồi."*

> *"Điều mình thích ở đây là phép ẩn dụ này không phải là một trò đùa trang trí. Nó thật sự dạy bạn khái niệm … Đúng là đặt tên tốt cũng là một dạng tài liệu."*
> ("What I like is that the metaphor isn't a decorative joke. It actually teaches you the concept … Good naming really is a form of documentation.")

**This was observed live during this ingest.** Running `brew outdated` triggered an auto-update which printed:

```
==> Pouring portable-ruby-4.0.6.catalina.bottle.tar.gz
```

Pouring, not brewing — and the bottle tag `catalina` is itself diagnostic, since it is the x86_64 bottle line. The metaphor carried real information at the moment it appeared. See [[this-machine-audit]].

The formula/cask distinction, from Easy Tech Steps: *"formulae, which are command line tools without a graphical interface, and casks, which are standard apps with a user interface."* Homebrew's own terminology confirms bottle = binary package and tap = third-party repository.

> **Why this matters beyond trivia:** `bottle` is the unit that Tier 3 deprecation takes away. *"Bottles will rarely be built or published."* Knowing that `Pouring` means "a bottle existed" makes its absence legible — when installs start compiling, you will recognise what you lost.

## The command surface

Assembled from all four tutorial sources; each command was stated by at least one, and the semantics below reflect the most careful description given.

### Install and setup

```bash
xcode-select --install        # prerequisite: Xcode command line tools
```
Dev Neil A is the only source that puts this first as a deliberate step; the brew installer will also pull it. Then the install command from `brew.sh`, which asks for your login password (*"no characters will show up on the screen while you type"*).

**The step everyone emphasises, and the one that matters most:** after installing, the output prints a "Next steps" block of shell lines you must run.

> Easy Tech Steps: *"This step helps your Mac recognize where Home Brew is located, so you don't get command errors later on."*
> Dev Neil A: *"Under next steps, run each of those commands … Lastly, close your terminal window and open a new one so that all the changes take effect."*

Both are describing adding Homebrew's prefix to `PATH`. **This is the single most consequential step in the whole topic**, and neither source explains that the prefix differs between Intel (`/usr/local`) and Apple silicon (`/opt/homebrew`) — because neither source discusses architecture at all. Skipping it gives "command not found". Doing it twice for two different prefixes gives the collision in [[this-machine-audit]].

### Daily use

| Command | What it does | Gotchas from the sources |
|---|---|---|
| `brew update` | updates **Homebrew itself** and its package database | Dev Neil A: *"This is not to be confused with updating"* — always update before upgrade |
| `brew upgrade` | upgrades **installed packages** | No rollback ([[the-three-weaknesses]]) |
| `brew outdated` | lists what is upgradable, with version numbers | The one to run *before* `brew upgrade` |
| `brew search <name>` | is it available, as formula or cask | |
| `brew info <name>` | version, source, dependencies, caveats, install analytics | The most under-used command in the set |
| `brew install <name>` | install a formula | Under 6.0, now shows a dependency summary and asks first |
| `brew install --cask <name>` | install a GUI app | Needed when a formula and cask share a name: *"if there is a package with the same name, it will conflict and not install anything"* |
| `brew list` / `brew list <name>` | what is installed / where a package lives | |
| `brew uninstall <name>` | remove | |
| `brew cleanup` | clear the download cache and superseded versions | Reports space freed; empty output means nothing to clear |
| `brew doctor` | diagnose problems | **Under 6.0 this exits non-zero on untrusted taps** ([[homebrew-6-security-release]]) |
| `brew bundle dump` | write a `Brewfile` of formulae, casks and VS Code extensions | Names only, **no versions** |
| `brew bundle install` | install everything in a `Brewfile`, skipping what is present | |

### New in 6.0

```bash
brew trust user/repo        # trust a third-party tap
brew exec <tool>           # run a tool once without installing it (npx-like)
brew vulns                 # scan installed packages against known advisories
brew version-install       # extract and install a specific older version into your own tap
```

## The cask gotcha nobody else mentions

Dev Neil A alone surfaces this, and it is a genuine trap:

> *"some apps have built-in update tools. So in those cases, Homebrew will only be used to install them. After that, the app will update itself … For example, Chrome, Firefox, and Visual Studio Code will all update themselves rather than via Homebrew. On the other hand, PG Admin 4 does not update itself. So, the cask specifies that homebrew will track the version and upgrade when required."*

So **`brew upgrade` does not keep all your casks current**, and which ones it manages is a per-cask decision recorded in the cask, not a rule you can infer. If you assume Homebrew is your update path for GUI apps, you will be wrong for exactly the apps most likely to matter.

He also notes casks *"typically don't have dependencies. They should be bundled in with a Mac OS app"* — which is the app-bundle model of [[why-macos-has-no-package-manager]] showing through: casks inherit Apple's isolation, formulae inherit Unix's sharing. **One tool, two dependency philosophies, depending on which half you use.**

## Discovery, and a number that expires

`formulae.brew.sh` publishes install analytics. Easy Tech Steps demonstrates browsing the 365-day GUI leaderboard and cites **PowerShell at 655,000 installs and Google Chrome at 347,000**.

⚠️ Point-in-time figures from a rolling 365-day window as of ~2026-03. Do not treat them as durable; the method (*"You can easily find highly downloaded apps here"*) is the transferable part. `brew info` surfaces the same analytics per package.

## GUI frontends

Easy Tech Steps closes with **AppLite** (`brew install --cask applite`), a graphical browser for Homebrew casks with an installed/updates tab. Leo Laporte's 2020 equivalent is **`mas`**, a CLI for Mac App Store apps — *"really handy … for keeping your App Store applications up to date"* — which is a different thing: not a Homebrew frontend but a bridge to Apple's store.

Warp's video is where the ecosystem-tools angle lives: `brew install` for `fzf`, `bat`, `exa`, `diff-so-fancy`, plus Oh My Zsh and powerlevel10k. ⚠️ It recommends **`exa`**, which this ingest did not verify as current; treat as a staleness flag rather than a recommendation ([[caveats-and-corrections]]).

## Cross-links

[[the-three-weaknesses]] · [[homebrew-6-security-release]] · [[why-macos-has-no-package-manager]] · [[this-machine-audit]]
