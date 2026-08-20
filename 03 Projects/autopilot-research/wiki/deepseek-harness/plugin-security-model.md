# The plugin security model — the one finding with primary-source confirmation

> **This is the page that should govern any decision about DSH.** It is the only major claim in the bundle that four independent videos, three prior vault ships, *and DeepSeek's own documentation* all agree on.

## DeepSeek's own words

Verified from DSH's own documentation (`packages/extensions/tool-cordis`):

> *"The sandbox is containment for honest code, not a security boundary — host-realm helpers on the sandbox global are reachable, so package code can reach Node."*

**Read that twice.** "Containment for honest code" is not a security posture; it is an explicit disclaimer of one. Turing Post paraphrases it accurately: *"DeepSeek also says that creator sandbox is not a security boundary. Treat this access much like shell access."*

## Four independent video confirmations

**Chase AI** — the anchor, and the most explicit:
> *"as of right now, out of the box, remember this is in developer preview. Every single plugin you add to DeepSeek Harness gets full shell access and full access to your entire file system… if there is a bad actor that has some sort of sketchy plugin that can take a look at your API keys because it will essentially have permission to do so, you can be in a bad spot."*

He also names the precedent, which is a vault-relevant comparison: *"this is very reminiscent to like when OpenClaw first came onto the scene, be wary."*

**Firecrawl** — draws the architectural conclusion:
> *"right now the plugin architecture is completely different from sandboxing, meaning every plugin gets full shell access and access to your file system. Now considering plugins are found and installed via GitHub, this means that you can install a rogue plugin that can find access to your API keys."*

And the line that belongs in the vault's permanent vocabulary:
> *"the job of a harness is to prevent prompt injection, not make it easy for people to do so."*

**The VN source** — the operator's-eye version, with the mechanism spelled out:
> *"bởi vì là cái plugin do cộng đồng viết ý nên là khả năng cả nhiều khi nó có virus hoặc là nó chưa được uy tín lắm… bởi vì đây ở trong nó là chạy code JavaScript ở trong mà nó làm được hết các cái trò hay là nó gọi đi server nào đấy nó lấy hết dữ liệu mọi người luôn nên là rủi ro khá là cao."*
> *(community-written plugins may carry viruses or be untrustworthy — it runs JavaScript inside, it can do anything, it can call out to some server and take all your data, so the risk is quite high.)*

He also gives the only **operational mitigation** anyone in the bundle offers: use the workspace-write permission tier, not full-access. *"Full access hơi nguy hiểm tí… thì nó sẽ truy cập được cả ra cái folder bên ngoài. Thì mọi người mà dùng thử mọi người chỉ cần dùng Workspace Write thôi."*

**Turing Post** — via DeepSeek's own docs, quoted above.

## What Chase AI actually did about it

Worth recording as behaviour, not just advice. Installing a third-party search plugin, he says: *"does that seem somewhat sketchy that I'm installing some random Chinese plugin? Well, first of all, I actually had Claude Code take a look at it to make sure it wasn't sketchy."*

**Using one agent to audit another agent's plugin before install.** That is a real, cheap, portable practice and the bundle's most transferable operational habit. It is also an incomplete control — an LLM read of plugin source is not a dependency-tree audit — but it is strictly better than nothing, which is what the ecosystem otherwise provides.

## Convergence with three prior vault ships

The YouTube layer and the source layer arrive at the same place from opposite directions:

- **v240** (`awesome-dsh-plugin`, the catalogue): the catalogue checks *metadata*.
- **v241** (`dsh-desktop`, the installer): the installer checks *identity* — and states plainly that they *"do not review the plugin or its dependency tree for malicious or unsafe behavior."*
- **v242** (source clone): *"nothing anywhere in this stack measures whether a plugin makes the agent worse. Identity verified end to end; effect unmeasured end to end."*

**The videos add the missing piece: DeepSeek's own docs concede the sandbox is not a boundary.** So the chain is now complete from catalogue to installer to runtime to vendor disclaimer, and every link says the same thing.

## Standing vault position — unchanged, now better-evidenced

**Read-and-borrow. Install nothing.** The v242 rationale (developer preview, no eval harness, telemetry default-ON, `postinstall`, PRC-default egress, closed to external PRs so no upstream recourse) is fully intact, and this bundle adds the vendor's own sandbox disclaimer to it.

**Never treat a `dsh-plugin` topic listing as a safety signal.** This bundle strengthens that rule considerably — see [[deepseek-harness/ecosystem-and-the-catalogue-gap]], where the topic turns out to be **6.3× larger** than the curated catalogue.

## Cross-links

[[deepseek-harness/_index]] · [[deepseek-harness/ecosystem-and-the-catalogue-gap]] · [[deepseek-harness/install-and-operational-reality]] · [[deepseek-harness/hireui-relevance]] · [[api-security-7-techniques/_index]] · [[prompt-evaluation/_index]] · [[claude-code-plugins-stack/_index]]
