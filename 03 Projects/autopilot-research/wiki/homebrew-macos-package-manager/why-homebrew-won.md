# Why Homebrew won — and the lesson the anchor is actually selling

## Homebrew was eight years late

This is the fact the anchor builds on:

> *"Home Brew không phải là phần mềm đầu tiên. Nó đi sau những phần mềm khác tận 8 năm vậy mà nó vẫn thắng."*
> ("Homebrew was not the first. It came eight years after the others, and it still won.")

| | Started | Origin | Design |
|---|---|---|---|
| **Fink** | **December 2000** (anchor says "around 2001") | Christoph Pfisterer | Lifted Debian's system wholesale — uses **dpkg and APT**, with a Perl frontend |
| **MacPorts** | **2002**, as **DarwinPorts** | The **OpenDarwin** project, with **Apple employees** involved — Landon Fuller, Kevin Van Vechten, Jordan Hubbard. Name from Darwin + FreeBSD Ports | Own tree, compile everything |
| **Homebrew** | **2009** | Max Howell, one person, on GitHub | Trust the system's libraries; prefer prebuilt bottles |

All three columns check out. The anchor's characterisation of MacPorts as *"có gốc gác từ chính Apple"* — having roots in Apple itself — is accurate: it began inside OpenDarwin with Apple engineers, was hosted on Apple's Mac OS Forge after OpenDarwin shut down in 2006, and was renamed to signal its macOS focus. Fink taking Debian's packaging *"nguyên"* (wholesale) is likewise exactly right: dpkg and APT, unchanged.

## The shared philosophy of the two that lost

Fink and MacPorts agreed on the thing that mattered: **do not depend on macOS.**

Software is source code — *"phần mềm thì cũng chỉ là mã nguồn tức là chữ"*, just text. To run it you compile it. So both compiled everything into their own directory, touching nothing else. Ask MacPorts for ImageMagick and it compiles `libpng` and the rest **even when your machine already has a copy.**

> *"Nghe thừa thãi nhưng lý do đằng sau rất chính đáng."* ("It sounds redundant, but the reason behind it is entirely legitimate.")

The reason is the Python 2 removal and the bash freeze in [[why-macos-has-no-package-manager]]: those libraries are not Apple's, but Apple decides which version ships and for how long. Compile your own and you are immune.

**The price:** every small tool costs half an hour of compiling.

## Homebrew's bet

> *"Cứ tin Maos đi, máy đã có sẵn thư viện rồi thì dùng luôn cái đó. Đừng xây lại cả thế giới để làm gì cả."*
> ("Just trust macOS — the machine already has the library, so use it. Don't rebuild the whole world for nothing.")

Less to compile, therefore fast. The anchor calls it *"một canh bạc về mặt kỹ thuật"* — a technical gamble. It is the same gamble in both directions: Homebrew is faster **because** it is exposed to Apple's decisions, and Fink/MacPorts are slow **because** they are not.

## But the technical bet is not why it won

This is the anchor's actual thesis, and it is why the video exists:

> *"Đó là một canh bạc về mặt kỹ thuật nhưng thứ thực sự làm nên chiến thắng của Homebrew thì lại không phải kỹ thuật."*

Two reasons, and he flags which one he believes.

**First — the formula is readable.** A formula is a short Ruby file. *"Người bình thường đọc vào là hiểu được ngay chứ không phải học một ngôn ngữ cấu hình bí hiểm nào cả"* — an ordinary person reads it and understands immediately, rather than learning some cryptic configuration language. (Confirmed: formulae are Ruby scripts built on Homebrew's DSL.)

**Second — and he says this is the real one — the timing and the venue:**

> *"Home Brew sinh ra trên GitHub vào năm 2009, đúng lúc GitHub đang trở thành trung tâm của cả thế giới Open Source. Bạn thấy thiếu một phần mềm nào đó à? Chỉ cần sửa một file text rồi gửi pull request."*
> ("Homebrew was born on GitHub in 2009, exactly when GitHub was becoming the centre of the open-source world. Notice a missing package? Just edit a text file and send a pull request.")

Then the line the whole video is built to deliver:

> *"Cho đến tận bây giờ, nhiều engineer cho rằng MacPorts mới là thứ được thiết kế tốt hơn, chặt chẽ hơn và an toàn hơn. Nhưng người thắng cuộc lại là Homebrew — không phải vì nó đúng hơn mà đơn giản vì nó dễ đóng góp hơn."*
> ("To this day many engineers hold that MacPorts is the better-designed, stricter, safer thing. But the winner was Homebrew — not because it was more correct, but simply because it was easier to contribute to.")

> **"Trong phần mềm, công cụ được thiết kế đẹp nhất, nhanh nhất, hay nhất thường không phải là công cụ thắng cuộc. Kẻ thắng cuộc đôi khi chỉ là một công cụ mà người lạ có thể sửa giúp bạn lúc 2:00 sáng."**
> ("In software, the best-designed, fastest, finest tool is usually not the tool that wins. The winner is sometimes just a tool a stranger can fix for you at 2am.")

## Why that claim is worth taking seriously here

It is an unfalsifiable-sounding thesis stated without evidence, and it would be easy to dismiss. Two things make it worth keeping.

**One: the design record supports the direction.** MacPorts' isolation genuinely is the more defensible engineering position, and the Python 2 removal proves it empirically — MacPorts users were immune to an event that broke apps for everyone else. The anchor is not claiming MacPorts was bad. He is claiming being right lost.

**Two: Homebrew's own 2026 behaviour is consistent with it.** The `brew-rs` experiment was abandoned because Rust delivered **no performance gains on representative full installs** ([[homebrew-6-security-release]]) — so the project stayed on Ruby, the language that makes formulae readable and the contribution barrier low. Sixteen years on, when performance and modernity pointed one way and contributor accessibility pointed the other, the project chose contributor accessibility. That is the thesis, still operating.

There is an irony worth naming: **the same open contribution model that won is precisely what tap trust exists to contain.** *"A third-party tap can contain arbitrary, unsandboxed Ruby that runs on your machine"* is a restatement of "a stranger can fix it for you at 2am" from the threat-model side. The strength and the vulnerability are one property. 6.0 does not remove it; it puts a door on it.

## The corroborating outside view

Warp's terminal-setup video ([`d4bTkiftBOk`](https://www.youtube.com/watch?v=d4bTkiftBOk), 2023-07) reaches for Homebrew in one line and, incidentally, confirms both halves:

> *"Homebrew is the missing package manager for Mac OS. It's really easy to use and install and has a huge Community behind it."*

and

> *"if you code in Ruby then Homebrew is even better for you because everything is simple Ruby scripts so you can customize everything to your liking."*

⚠️ *"the missing package manager for macOS"* was Homebrew's long-standing tagline. **It is no longer the tagline** — `brew.sh` now reads **"The Package Manager for Everywhere"**, reflecting Linux and WSL support. A 2023 source quoting the old tagline is a dating marker, not an error. See [[caveats-and-corrections]].

## Cross-links

[[why-macos-has-no-package-manager]] · [[the-three-weaknesses]] — the invoice for this bet · [[the-howell-interview-story]] — the same "the record does not match the legend" move, applied to a person · [[homebrew-6-security-release]] · [[../system-thinking-ai-coding/_index|system-thinking-ai-coding]] — the anchor's claim is a theory-building claim: the artifact that survives is the one whose theory is cheapest for a stranger to reconstruct
