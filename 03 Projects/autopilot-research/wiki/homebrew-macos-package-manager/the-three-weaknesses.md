# The three weaknesses — all three confirmed by Homebrew's own docs

The anchor names three, and frames them not as bugs:

> *"Nhưng ba thứ đó không phải là lỗi. Đó là hóa đơn của canh bạc đã giúp Homebrew chiến thắng."*
> ("But those three are not bugs. They are the invoice for the gamble that made Homebrew win.")

Every one of the three was checked against `docs.brew.sh`. **All three hold**, and the documentation is blunter than the video.

## 1. No version pinning

> *"Cái file danh sách phần mềm mà bạn chép sang máy mới nếu mở ra xem thì bạn sẽ thấy nó chỉ ghi mỗi tên thôi. Ví dụ như `node`, `ffmpeg` — không hề có số phiên bản nào cả."*

So `brew install node` does not mean "install node 20". It means **install whatever is newest at the instant you press enter.**

> *"Cho nên nếu bạn chạy nó hôm nay còn đồng nghiệp bạn chạy nó ba tháng sau, hai máy sẽ ra hai kết quả khác nhau mà chẳng ai làm sai cái gì hết."*
> ("So if you run it today and your colleague runs it three months later, the two machines come out different, and neither of you did anything wrong.")

And the crucial part — this is deliberate:

> *"Tài liệu của Homebrew nói thẳng rằng họ không có và sẽ không bao giờ có thứ như … `package-lock.json` bên Node hay `Gemfile.lock` bên Ruby. Đây là lựa chọn có chủ đích."*

**Confirmed.** `docs.brew.sh` states that `brew bundle` *"does not pin versions or add lock file support."* There is no `package-lock.json` analogue and none is planned.

This is the hole in the ledger. [[why-macos-has-no-package-manager]] establishes that a package manager's value **is** the ledger — it knows what you have, *at what version*, and who depends on whom. Homebrew keeps the dependency graph and the installed-version state, but the **portable artifact** — the `Brewfile` — carries only names. So the ledger is authoritative about *this machine now* and says almost nothing about *another machine later*.

Dev Neil A demonstrates the artifact without noticing the gap. `brew bundle dump` produces a `Brewfile` in the current directory listing formulae, casks, **and VS Code extensions** — *"the next time Visual Studio Code is installed, Homebrew will also install those extensions."* Then: *"You can now use that brew file on other Macs."* Which is true, and which reproduces a **package list**, not a machine. Useful; just not what "reproducible" means.

> This is not academic here. [[this-machine-audit]] recommends a prefix migration whose only inventory is a `Brewfile` — 105 names, no versions. The migration therefore installs today's versions of everything, not the versions currently working.

## 2. Rollback is painful

> *"Giả sử bạn gõ `brew upgrade`, một công cụ nào đó nhảy lên bản mới và project của bạn chết ngay lập tức. Bây giờ thì bạn làm gì?"*

The comparison he draws is the right one. On Fedora, `dnf history undo` reverses the last transaction and restores the machine — one command. **Homebrew has no equivalent undo.**

What it has instead:

| Command | What it actually does |
|---|---|
| `brew extract` | *"the lower-level workflow"* — extracts an old formula version for you to **manage yourself in a tap** |
| `brew version-install` | *"a simpler workflow to extract a specific older formula version into your own tap and install it"* |

Note the correction: the anchor's audio renders this as *"brew version install"*; the real command is **`brew version-install`**, hyphenated.

Both confirmed, and the anchor's characterisation of what they mean is exactly right:

> *"Nó không trả máy bạn về trạng thái cũ mà nó nôi cái công thức cũ ra rồi bảo bạn tự tạo một tap riêng để chứa. Và kể từ lúc đó cái bản cũ ấy là việc của bạn, không phải việc của Homebrew nữa."*
> ("It does not return your machine to its old state — it pulls out the old formula and tells you to make your own tap to hold it. From that moment the old version is your job, not Homebrew's.")

**This is the load-bearing distinction and it is easy to miss:** these are not rollback commands. They are *fork* commands. They do not restore state; they transfer ownership.

He is fair about the mitigation: for popular software Homebrew ships multiple versioned formulae — `node@20`, `node@21` alongside latest — and *"nếu có sẵn thì bạn nên dùng cái đó"*, if it exists you should use it. But *"danh sách này là có hạn"* — the list is limited.

## 3. Pinning is hard, and Homebrew tells you not to do it

The third weakness is not a missing feature; it is an explicit instruction. `docs.brew.sh/Versions`:

> **"Homebrew's versions should not be used to 'pin' formulae to your personal requirements."**

And the consequence the anchor states — that if you extract an old version into your own tap, *"việc cập nhật, vá lỗi và vá bảo mật cho nó là trách nhiệm của bạn"* (updating it, and patching its bugs and security holes, is your responsibility) — is confirmed by the docs' own framing of `brew extract`: you gain control of the formula file and **assume responsibility for updates and security patches.**

That last clause deserves emphasis in a post-6.0 world. [[homebrew-6-security-release]] documents Homebrew shipping `brew vulns` to scan installed packages against known advisories, and fixing three of its own. **A formula you pinned into a personal tap is a formula whose advisories are now yours to track.** Pinning for stability buys a security-maintenance obligation.

## The bill, and where Nix takes over

> *"Họ đổi khả năng ghim, khả năng quay lui và khả năng tái lập để lấy lại sự nhanh và sự đơn giản. Trên chiếc laptop của bạn thì như thế là hời, nhưng trên một build server thì đổi như thế là dại."*
> ("They traded pinning, rollback and reproducibility for speed and simplicity. On your laptop that is a bargain; on a build server that trade is foolish.")

Hence:

> *"Và đó là lý do dân hạ tầng chuyển sang dùng Nix. Mà Nix thì cũng có những nỗi đau riêng. Nó dựng lại cả thế giới trong thư mục riêng — y hệt như MacPorts ngày xưa — nên bạn sẽ có những buổi chiều ngồi nhìn máy build từ mã nguồn."*

**Nix is MacPorts' philosophy, vindicated.** Rebuild the world in your own directory, accept the compile time, get reproducibility. The design that lost the desktop won the build server. [[why-homebrew-won]] argues Homebrew beat the better-engineered option on contribution cost; this is where the better-engineered option collects.

The closing line is the one to keep:

> **"Không có bữa trưa nào miễn phí cả, chỉ có việc bạn chọn trả hóa đơn nào mà thôi."**
> ("There is no free lunch — only which invoice you choose to pay.")

Better Stack, independently and from the other side, corroborates the framing: its own prior video *"basically called Homebrew this Stone Age thing we use because Nix runs circles around it."* Two sources in this bundle, one Vietnamese essayist and one English DevOps channel, place the Homebrew/Nix boundary in the same place.

## What this means for this vault

The autopilot pipeline depends on `brew`-installed `yt-dlp` and `python@3.12`, and pins its Python by **hardcoding an absolute path** in `bin/autopilot-env.sh` rather than by any Homebrew mechanism.

Given the above, that is **the correct choice**, not a hack — Homebrew's docs explicitly tell you not to use their versioning to pin to your requirements. The hardcoded path is a pin implemented outside the tool that refuses to provide pins. What it does not do is protect against `python@3.12` being upgraded within the 3.12 series or removed; it protects against *resolution ambiguity*, which — per [[this-machine-audit]] — is the actual failure that was occurring.

## Cross-links

[[this-machine-audit]] · [[homebrew-6-security-release]] · [[why-homebrew-won]] · [[terminology-and-commands]] · [[../local-llm-coding-hardware-ladder/_index|local-llm-coding-hardware-ladder]]
