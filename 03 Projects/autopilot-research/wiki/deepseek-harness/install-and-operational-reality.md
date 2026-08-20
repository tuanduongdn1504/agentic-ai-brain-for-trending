# Install and operational reality — the failure log

> **The Vietnamese source is the only one in the bundle that shows the thing breaking.** Five English videos demo a working harness in a clean environment; one 77-minute Vietnamese screencast documents a real install on Windows with real failures. For pilot-decision purposes it is the most valuable source in the bundle.

## Hard requirements the bundle establishes

| Requirement | Evidence |
|---|---|
| **Node.js ≥ 22.19** | VN hit the failure on 22.15: *"cảnh báo dependency… cần Node lớn hơn 22.19"*; resolved by upgrading to **24.19.0** |
| **pnpm** | Firecrawl: *"you may have to install pnpm if you don't have it already because that's how the harness installs plugins in the background."* VN hit the same requirement mid-install. |
| Web UI on localhost | Cef: port **3080**. VN: *"port 3000 gì đấy."* Unresolved. |
| A model provider API key | Web search requires a **DeepSeek** key specifically, or a plugin substitute — see below |

The README's own stance, verified: **developer preview**, with *"THERE WILL BE COMPATIBILITY-BREAKING CHANGES."*

## The web-search gate — a real friction point, found by two sources independently

Out of the box, **web search requires a DeepSeek API key**, even if you are running an entirely different model.

Chase AI: *"If you want to be able to use web search out of the box, you need to provide the DeepSeek API key. Well, if you don't have that and you're using some sort of other model, well, you now need to find a plugin."* He installs a free-search plugin (Bing/DuckDuckGo).

Firecrawl: *"right now you need to have a DeepSeek API key in order to search the web… And because I haven't added one, I'll get this error whenever I need to do a search."* They install their own first-party Firecrawl plugin, and note it needs a config edit to expose a generic web-search tool *"since it's off by default"*, then a restart.

**So "model-agnostic" is true of the model and false of the built-in tooling.** The harness is provider-neutral at the inference layer and DeepSeek-coupled at the tool layer, and closing that gap requires third-party plugins — which are exactly the artifacts with full shell access. Two sources hit this independently; neither connects it to the security page. **The vault should: the most common first-day friction pushes users straight into the least-reviewed part of the ecosystem.**

## The RC6 → RC7 episode

The VN source recorded on 2026-08-18, one day after upgrading:

> *"Cái bản hôm qua RC6 mình chạy mình vẫn thấy ngon mà hôm nay sang RC7 nó đã lỗi tùm lum rồi."*
> *(Yesterday's RC6 ran fine; today on RC7 it's throwing errors everywhere.)*

He also observed the version churn itself: *"Hôm trước mình mới thấy hôm qua mới RC6 hôm nay đã RC7 rồi. Thế đội này đẩy cũng nhanh."*

**This looks like counter-evidence to the vault's v242 finding (D24) that rc.6 → rc.7 was "4 days, zero breaking changes, zero package delta." It probably is not — and the distinction is the useful part.**

His observed failures were: a Node-version peer-dependency error, and a version mismatch between the harness and a plugin's pnpm-resolved Cordis (*"Setting RC7 nhưng PNPM cái RC01"*). **Both are ecosystem-resolution failures, not harness-core code changes.** v242's claim was about the *repo diff*; the VN evidence is about the *installed graph*.

**Reconciliation, and it is a genuine finding: a version bump with zero code delta can still break users, because plugins pin Cordis versions and resolve independently.** v242's D24 rule ("a version-number delta is not a code delta") holds for the repository and is *insufficient* for the ecosystem. The inverse rule this ship adds:

> **A zero-code-delta version bump is not a zero-impact version bump when third-party plugins pin your kernel's version.**

That is a new, transferable rule and it did not require re-cloning anything.

## The sandbox observation — flagged, deliberately unresolved

The VN source noticed a permission-behaviour difference and reasoned about it out loud:

> *"Thế hôm nay là cái bản DC0.7 này nó còn hỏi nhá. Cái bản 0.6 mà mình mà chọn cái đấy là nó từ chối luôn… khả năng ra là bản 0.7 nó mới nâng cấp đấy. Sandbox vừa mới nới lỏng."*
> *(Today on 0.7 it asks. On 0.6, if I chose that, it refused outright… probably 0.7 upgraded it. The sandbox has just been loosened.)*

**Then he half-retracts it himself**, mid-sentence: *"à không mình mới đổi full access phát là nó biết"* — he had just switched his own permission tier to full-access, which is a sufficient explanation without any version change.

**The vault records this as UNRESOLVED, not as a finding.** Two live hypotheses: (a) RC7 relaxed the out-of-workspace write policy from hard-refuse to prompt-and-allow, or (b) his own permission-tier switch explains it entirely. He flagged his own uncertainty; we preserve it rather than resolving it in the direction that would be more interesting.

**This is the single most pilot-worthy question in the bundle**, because hypothesis (a) would be a security-relevant regression in a developer-preview tool, and it is cheap to settle: install rc.6 and rc.7 side by side, attempt an out-of-workspace write at workspace-write tier, diff the behaviour. See [[deepseek-harness/hireui-relevance]].

## Other operational findings

- **Permission tiers**: read-only / workspace-write / full-access. The VN source's advice is the bundle's best security hygiene: use workspace-write, not full-access, because full-access *"sẽ truy cập được cả ra cái folder bên ngoài… ghi ra bên ngoài là rủi ro."*
- **Plugins escape the workspace anyway.** He selected a workspace, and the novel plugin created its project elsewhere, leaving him unable to locate the output. Workspace selection did not constrain plugin file placement in his run.
- **Plugin-level credential sprawl.** The novel-writing plugin demanded **its own separate API key** and its own config patch file, distinct from the harness's provider config. Each plugin is a potential new secret to manage — and each plugin has filesystem access to all the others' secrets.
- **Rate-limited installs.** He repeatedly hit what he read as a per-day install restriction on very new plugins, and worked around it by choosing older entries.
- **Install-via-agent as a workaround.** His most practical trick: rather than fighting the terminal, he drove the install from *another* harness (opencode desktop) and let it resolve missing dependencies: *"mình cài cái harness open code này phát là mình muốn cài cái gì là nó tự tìm lỗi, nó tự tìm gói rồi nó tự cài cho mình."* Using an established agent to install an experimental one is a genuinely good pattern.

## The honest summary of day-one DSH

Two sources say the quiet part. Firecrawl: *"the whole process of installing plugins is a bit fiddly."* The VN source, after an hour of it: *"Mới quá nên là nó vẫn còn đang bất ổn."* (It's too new, so it's still unstable.)

Better Stack's *"It's in beta right now, so there are a few problems with it, but that's expected"* is the fair framing. **Nothing here is a scandal for a developer-preview tool. All of it is disqualifying for production use, exactly as the vault's standing read-and-borrow position already assumes.**

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/plugin-security-model]] · [[deepseek-harness/ecosystem-and-the-catalogue-gap]] · [[deepseek-harness/hype-vs-source-scorecard]] · [[deepseek-harness/hireui-relevance]] · [[local-ai-coding-agents/_index]] · [[fullstack-docker-cicd/_index]]
