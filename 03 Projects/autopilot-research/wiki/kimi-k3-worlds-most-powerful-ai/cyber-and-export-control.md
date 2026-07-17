# Cyber risk & export control — the other false claim

The video (~[30:27]–[32:47]) spends several minutes on a geopolitical story: *"the US government restricted this … we've seen it was able to hack many of our systems … only American people can use it."* This narration **conflates two different events and is factually wrong** about K3.

## What actually happened (COR6 / FALSE, UPHELD high)

- **US export controls were imposed on Anthropic's Claude Fable 5 and Mythos 5** — *Western* models — on **2026-06-12**, after **Amazon researchers discovered a jailbreak** that bypassed guardrails and exposed cyber-offensive capability (flagging software flaws + writing exploit code). Anthropic **globally disabled** Fable 5 / Mythos 5 to comply.
- Those controls were **lifted in late June / July 1, 2026** after Anthropic shipped safety classifiers blocking the jailbreak in >99% of cases.
- **No US export controls were placed on Kimi K3.** It is a **Chinese** company's model — the US **cannot** export-control a foreign lab's model via that mechanism. The video's own on-screen tweet even says this ("the White House must be having a real hard time figuring out how to put an export block on something that isn't their product") — yet the narration asserts the opposite.

**So the video takes the Fable/Mythos export-control story and mis-pins it onto K3.** The claim "the US restricted K3 because it hacked US systems, only Americans can use it" is FALSE.

## The real, open question: K3's own cyber capability

- The legitimate version of the concern (raised by researchers like "adi" on X): **is K3 dangerously good at cyber?** That's unresolved:
  - Moonshot **did not release a CyberGym score** at launch — possibly to avoid triggering scrutiny, possibly because it isn't impressive. Unknown.
  - **CyberGym** is a real benchmark (1,507 instances / 188 projects; model must generate a PoC input to trigger a known vuln). The **predecessor Kimi K2.5 ranked *behind* Claude Opus 4.5 and GPT-5** on Level 1, needing Level-2 hints (error traces) to exceed 50%. Claude Mythos Preview leads (~0.831).
  - So prior-generation Kimi cyber capability was **not** frontier; K3's is simply **undisclosed**.

## Key Takeaways

- **No US restriction exists on Kimi K3.** The video imports the Anthropic Fable/Mythos export-control episode and misattributes it — a clean FALSE.
- The genuine open question ("how cyber-capable is K3?") is **unanswered** because Moonshot withheld the CyberGym score; the predecessor was sub-frontier.
- This is the video's second outright-false thread (alongside [[open-weights-reality]]) — both are *plausible-sounding geopolitics* that dissolve on a single check.
