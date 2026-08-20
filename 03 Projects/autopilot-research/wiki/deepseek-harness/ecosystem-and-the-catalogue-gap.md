# The plugin ecosystem — and a 6.3× gap the vault had not measured

> **Original finding of this ship.** The vault's v240 analysis measured the *curated catalogue*. This ship measured the *GitHub topic* the catalogue indexes. They differ by more than six times, and the difference is invisible from inside either one.

## The two numbers

Both verified 2026-08-20:

| Surface | Count | What it is |
|---|---|---|
| **`dsh-plugin` GitHub topic** | **8,874 public repositories** | Every repo that self-applied the topic tag |
| **`awesome-dsh-plugin` catalogue** | **~1,400 entries** | The community-curated list (v240's subject) |

**The curated catalogue covers roughly 16% of the tagged ecosystem.** ~7,470 topic-tagged repositories are not in it.

The VN source watched the catalogue grow live: *"hôm qua mình mới thấy có 1200, 1000 hơn nghìn thôi mà hôm nay đã 1400 rồi đấy"* (yesterday ~1,200, today 1,400), and later on screen: *"1401 rồi à."* He also reports the catalogue repo itself at **8,400 stars in 4 days**.

**This independently corroborates v240's recorded count of 1,390 entries** — from an operator's screen two days later, arriving at ~1,400. Two methods, same number. Good.

## Why the gap matters

This is a direct, N=2 instance of **the v240 inventory rule**: *a check between two views of one source is blind to what is MISSING from it.*

v240 audited the catalogue's prose against the catalogue's code. Both views agreed. Neither could see that the catalogue is a **16% sample** of the topic it indexes. The gap is only visible from outside both — which is what this ship did by fetching the topic page.

**Practical consequence:** any statement of the form "there are ~1,400 DSH plugins" is wrong by a factor of six. The vault should say **"~1,400 curated entries out of 8,874 topic-tagged repositories"** and never the first number alone.

**Security consequence, and this is the serious one:** [[deepseek-harness/plugin-security-model]] establishes that plugins get full shell and filesystem access, and that DeepSeek's own docs disclaim the sandbox as a security boundary. If a user's mental model of "the ecosystem" is the curated list, they are reasoning about 16% of the attack surface. Curation is doing far less work than its prominence implies.

## Top of the topic, and two cross-corpus surprises

The topic's largest repos by stars (2026-08-20):

| Repo | Stars | Note |
|---|---|---|
| `deepseek-ai/deepseek-harness` | 169k | the host itself |
| `nexu-io/open-design` | 89.4k | **already a vault topic** — see [[open-design/_index]] |
| `amruthpillai/reactive-resume` | 41.2k | privacy-focused résumé builder |
| `esengine/DeepSeek-Reasonix` | 34.9k | *"DeepSeek-native AI coding agent for your terminal"* |
| `volcengine/OpenViking` | 30.4k | *"Self-evolving Context Database for AI Agents"* — volcengine = ByteDance |

**Two things worth flagging.** First, `open-design` — a project the vault already analysed on its own terms — now carries a `dsh-plugin` topic tag at 89.4k stars. The DSH ecosystem is absorbing pre-existing large projects, not only spawning new ones. That materially changes what "8,874 plugins in three weeks" means: **an unknown share of the topic is retrofitted tags on existing repos, not new plugin development.** Nobody in the bundle notices this, and neither did the vault.

Second, `reactive-resume` is a résumé tool sitting in the top five of an agent-harness plugin topic. Either it is genuinely integrated or the tag is opportunistic. Unresolved, and a good reason to distrust the topic count as a measure of plugin development.

## The VN source resolves his own uncertainty — and he was right to doubt

Browsing DSH Market, the VN source sees OpenViking listed at **28,995 stars** and stops to flag exactly the right doubt:

> *"cái này không biết là số sao của GitHub hay là số sao ở trong cái nội bộ này mình cũng không rõ"*
> *(I don't know whether this is GitHub's star count or an internal count for this catalogue.)*

**Answer: they were GitHub stars.** OpenViking reads 30.4k on GitHub on 2026-08-20; his screen showed 28,995 two days earlier. Consistent growth. His doubt is resolved in his favour — but the doubt was correct to raise, because the same UI shows plugins at *"7 sao"* and *"300 sao"* alongside a 29,000-star entry, and nothing on screen distinguishes the metric's provenance.

## DSH Market — a runtime marketplace, new to the corpus

The VN source documents something the vault's v240 (static catalogue) and v241 (desktop installer) analyses do not cover: **`dsh-market`, a plugin that installs a plugin marketplace into DSH's own web UI.** Version observed: **1.13.1**.

*"Thằng DSH Market này chính nó là một cái market luôn. Và cái plugin này… sẽ cài thêm một cái plugin market này vào trong cái web UI."* One command, and the awesome-list becomes a browsable, one-click-install store inside the harness.

He is impressed — *"mọi người chỉ cần cài cái chợ này vào một phát là mọi người dùng plugin là turbo luôn"* — and the mechanism is a clean demonstration of everything-is-a-plugin. **It is also the shortest possible path from "browsing a community list" to "arbitrary code with full shell access running in your harness,"** with the plugin-security caveats of [[deepseek-harness/plugin-security-model]] applying in full and no review step in between.

**Corpus placement:** static catalogue (v240) → identity-checking installer (v241) → **in-harness one-click marketplace (this ship)**. The trend is monotonic toward lower friction, with the effect-measurement gap v242 identified still unfilled at every stage.

## Plugin quality is not correlated with stars

The VN source runs the only quality test in the bundle, accidentally. He tries a high-star novel-writing plugin; it fails to work. He falls back to a lower-star one; it works: *"nhiều khi là mấy cái gói này nó cùi quá nên là thằng AI nó không biết"* (some of these packages are junk, so the AI doesn't know them), and *"cái tool kia nó cùi nó không tìm thấy chứ cái tool này… nó đang đúng với cả cú pháp."*

He also hits plugins interfering with each other — *"Plugin kiểu đấm nhau ấy"* (the plugins are punching each other) — and a plugin that created its project files outside his selected workspace, leaving him unable to find them: *"Tạo xong không biết tạo chuyện ở đâu. Máy tính nhiều file tìm bằng niềm tin."* (created it, no idea where; my machine has a lot of files, searching on faith.)

**N=1, but it is the only empirical quality datum in the bundle, and it points the same way v242 did: identity and popularity are measured; effect is not.**

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/plugin-security-model]] · [[deepseek-harness/everything-is-a-plugin]] · [[deepseek-harness/install-and-operational-reality]] · [[deepseek-harness/hype-vs-source-scorecard]] · [[open-design/_index]] · [[agent-memory-architecture/_index]]
