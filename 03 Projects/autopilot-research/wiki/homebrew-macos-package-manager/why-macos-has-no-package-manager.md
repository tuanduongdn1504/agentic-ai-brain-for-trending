# Why macOS ships without a package manager

## The question the anchor actually asks

> *"Tại sao Marcos, một hệ điều hành Unix chính hiệu lại không có sẵn thứ như thế này? Câu trả lời không phải là Apple lười."*
> ("Why does macOS, a genuine Unix operating system, not ship with something like this? The answer is not that Apple is lazy.")

Kunkka's answer: **Apple did solve dependency management — it solved it differently from the rest of the Unix world, and only for the layer it cared about.**

## First, what a package manager is for

The anchor's framing is the load-bearing idea of the whole video, and it is aimed at a specific misconception:

> *"Đa số mọi người nghĩ nó như kiểu là một cái App Store cho dân kỹ thuật. Điều này sai và cái sai đó làm bạn bỏ lỡ những điều sau đây."*
> ("Most people think of it as an App Store for technical people. This is wrong, and that error makes you miss the following.")

⚠️ **Another source in this same bundle opens with exactly the misconception being corrected** — Easy Tech Steps' first sentence is *"Home Brew is basically like a second App Store for your Mac."* See [[caveats-and-corrections]]; the disagreement is not averaged here.

The worked example: ImageMagick needs `libpng` to read PNGs, FreeType to draw text, and `libtiff` for TIFFs. Each of those three needs the same compression library underneath. One copy on the machine, hundreds of things using it.

Then the cost of sharing:

> *"chính cái cơ chế dùng chung đó lại đẻ ra một cơn áp mộng khác mang tên Dependency Hell."*

The OpenSSL case: your new tool needs OpenSSL 3, an old company script still runs on 1.1, both live on one machine with one OpenSSL. Update for one and you break the other. Uninstall one program and you take out a library four others depend on. Windows has the same disease under a different name — DLL Hell.

Which produces the definition:

> *"Giá trị của một package manager không nằm ở chỗ nó tải file, tải app về vì tải thì trình duyệt nào mà chả làm được. Giá trị của nó nằm ở chỗ nó giống như một cuốn sổ kế toán."*
> ("A package manager's value is not that it downloads files or apps — any browser can download. Its value is that it is like an accounting ledger.")

It knows what you have installed, at what version, who depends on whom, and what becomes garbage when you remove something. His image: *"người giữ tấm bản đồ đường ống ngầm của cả thành phố"* — the keeper of the city's underground pipe map. **"App Store chỉ là cái cửa hàng thuần thủy, còn Package Manager thì giống như một bộ phận quy hoạch đô thị"** — an App Store is just a shop; a package manager is an urban-planning department.

This is worth holding onto because it predicts the weaknesses in [[the-three-weaknesses]]. If the value is the ledger, then a ledger that **records names without versions** is a ledger with a hole in it.

## Apple's answer: the app bundle

A `.app` is not a file, it is a directory — right-click, Show Package Contents. Inside: compiled code, icons, localizations, and *"quan trọng nhất là tất cả các thư viện mà app đó sử dụng để chạy"* (most importantly, every library the app uses to run).

The lineage: the idea comes from **NeXTSTEP**, the OS of the company Jobs founded after being pushed out of Apple, and it returned to Apple with him in **1997**.

The philosophy: every app carries its own luggage, shares with nobody, steps on no neighbour. Photos has its own `libpng`; Preview has its own; *"hai app này thậm chí còn không biết đến sự tồn tại của nhau"* — the two do not even know the other exists.

The price is disk space, and it is enormous. What Apple buys with it is quiet: on a Mac, installing one app essentially never breaks another. **And that is why you install software on a Mac by dragging an icon** — a gesture the anchor notes Unix people find *"khá ma thuật và hài hước"*, rather magical and funny.

## But underneath, it is still Unix — and that layer is starved

macOS still has git, Python, bash. That world does not play by app-bundle rules; it plays by shared-library rules. Apple ships some Unix tools, and here is the problem:

> *"Apple đóng băng trúng lại và gần như không bao giờ cập nhật."* (Apple freezes them and almost never updates them.)

### The bash 3.2 case, which is a licensing story

For over a decade macOS shipped **bash 3.2**, a version from **2006** — the anchor places it *"cùng thời với chiếc iPhone đầu tiên"* (contemporary with the first iPhone; strictly, bash 3.2 predates it by months) — while the outside world reached bash 5.

The reason is not technical:

> *"Thú vị là lý do ở đây không phải kỹ thuật mà là license. Từ Bash 4 trở đi, dự án chuyển sang giấy phép GPL version 3."*

**All of this checks out.** Apple stayed on bash 3.2 because it is GPLv2; bash 4 and later are GPLv3. Apple has kept clear of GPLv3 in macOS because it is more restrictive for a vendor that signs its own code, and it carries explicit patent grants. The specific clause the anchor names — *"cấm dùng phần mềm trên các hệ thống chặn người dùng cài phần mềm bên thứ ba"* — is the anti-tivoization provision, and it is the right one to name.

Apple stood still for **13 years**. Then in **2019, macOS Catalina** quietly changed the default shell to **zsh** (5.7.1, MIT-licensed).

The message the anchor reads into it:

> *"công cụ dòng lệnh à tự lo đi"* — "command-line tools? Sort it out yourself."
> *"Và cái lỗ hổng đó thì vừa khít với hình dạng của Home Brew."* — "And that hole is exactly Homebrew-shaped."

### The Python 2 case, which is about who controls your dependencies

The sharper example, because it shows the risk is not just staleness but **removal**:

> *"Ở bản MacOS 12.3, Apple đã gỡ luôn Python 2 ra khỏi hệ thống. Thế là hàng loạt app đang chạy dựa vào nó thì chết ngay khi vừa mở lên."*

Confirmed. macOS Monterey **12.3** removed Python 2.7 at `/usr/bin/python`. Apps depending on it crashed immediately on launch, and the change landed **in a point release** — which is what made it notable at the time. Python 3 does not help, because code tied to Python 2.x is tied to that version specifically.

The anchor's conclusion is the argument Fink and MacPorts were built on, and it is a genuinely good one:

> *"Mấy thư viện sẵn có kia không phải của Apple nhưng Apple lại là người quyết định ship bản nào và ship tới bao giờ."*
> ("Those pre-existing libraries are not Apple's, but Apple is the one who decides which version ships and for how long.")

Every macOS upgrade can move a library to a different version or delete it. If you compile everything yourself into your own directory, *"Apple có làm gì thì cũng kệ nó"* — whatever Apple does, your machine survives.

**That reasoning is why the losing design was the defensible one.** See [[why-homebrew-won]].

## The 2020 view of the same gap

Leo Laporte's *Hands-On Mac* episode ([`1uvr9-zUB3w`](https://www.youtube.com/watch?v=1uvr9-zUB3w), 2020-05-08) frames it as pure upside — Homebrew is *"probably the single most useful tool for command line users on the Macintosh"*, giving access to *"all of the old friends like wget and curl, updated versions of Python and Perl."* He counts *"at least nine"* macOS package managers, having started with Fink, and lands on Homebrew as best-supported and most-loved — *"and maybe it's because its icon is a stein of frothy beer."*

He also describes the mechanism precisely, which is the part still true in 2026:

> *"brew … installs these programs locally only and then puts a link in the directory that you're searching for binary files, so it's very easy to uninstall them. It's also easy to keep them from colliding with official Macintosh utilities."*

Install into a Cellar, symlink into `PATH`, stay out of Apple's way. **That is the whole design in one sentence**, and it is why the `--prefix` question in [[this-machine-audit]] matters so much: the prefix *is* the isolation boundary.

⚠️ This source predates Apple silicon by six months and is stale in the specific ways [[caveats-and-corrections]] lists.

## Cross-links

[[why-homebrew-won]] · [[the-three-weaknesses]] · [[terminology-and-commands]] · [[homebrew-6-security-release]] · [[this-machine-audit]]
