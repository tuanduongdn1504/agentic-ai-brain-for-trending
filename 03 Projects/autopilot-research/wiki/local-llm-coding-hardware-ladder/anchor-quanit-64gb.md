# The anchor — Quân IT tests local coding on a 64 GB Mac mini against a real production repo

> **Source:** Quân IT, *"Thử local LLM, coding trên Mac mini M4, 64GB ram"* ([`GBf_mKxGqtk`](https://www.youtube.com/watch?v=GBf_mKxGqtk)), 2026-08-19, 48:34, 1,755 views at ingest. Vietnamese, `vi-orig` captions read in full.
> **Operator-submitted anchor.** Anchor validation PASS 1/1.
> **Creator prior:** 2nd Quân IT topic in the corpus — see [[../quanit-becoming-ai-engineer-2026/_index|quanit-becoming-ai-engineer-2026]] (0 FALSE / 0 FABRICATED, 1 MISLEADING, 1 UNVERIFIABLE). Directionally reliable; tends to overstate specific figures. Weight his **verdict** heavily and his **numbers** loosely.

## Why this video matters more than its 1,755 views suggest

It is the **only source in the bundle that points a local model at a large, real, multi-service production codebase** — and he says so deliberately:

> *"mấy cái ông YouTube mà cứ build mấy cái game nhỏ nhỏ build con rắn... nó không giải quyết được cái bài toán thực tế"*
> — those YouTubers who just build little snake games; it doesn't solve the real problem.

The repo he uses has many services, GitHub Actions, CI/CD, and git submodules. Every other source in the bundle — including [[apple-mlx-stack|Apple's own]] — demos greenfield or toy work.

## Setup

- **Mac mini, 64 GB unified memory**, ~400 GB free storage. He calls it "M4"; **Apple's specs make it necessarily an M4 Pro** — base M4 caps at 32 GB. See [[the-hardware-ladder]].
- Stated cost: **"65 củ"** ≈ 65 million VND.
- **Ollama** as host — he notes it now has a GUI and an **Ollama Cloud** tier ([[the-tooling-layer|both confirmed]]).
- Models: a `qwen coder 30B` (~18 GB, downloaded ~8 months earlier), then **Qwen3.5**, which advertises a **1M-token context window** (confirmed: Qwen3.5 is 262,144 native, extensible to 1,010,000).
- Driven through **Claude Code** pointed at the local endpoint via environment variable.
- Restarts the machine first to free RAM; runs only OBS and one window.

## What actually happened

**Latency.** First response to `hello`: **2 minutes 45 seconds** — cold-loading weights. He accepts the trade explicitly:

> *"nếu mà mất 1 phút mấy thì mình cũng ok... so với việc phải trả vài trăm đô cho Claude Code"*
> — a minute-plus is fine, versus paying several hundred dollars for Claude Code.

**Thermals.** RAM hit ~80-something percent. The mini ran *"rất là nóng"* — very hot — and became audible:

> *"con Mac mini này hồi xưa... nó im re mà bây giờ nó hú lên"* — it used to be dead silent, now it howls.

Screen capture visibly stuttered (*"nó giật"*).

**The failure mode.** Repeated **API errors**. He initially suspects the endpoint, then self-diagnoses correctly:

> *"cái context của mình nó bị lớn quá"* — my context got too big.

Re-prompting with a short prompt worked. This is [[why-agentic-differs-from-chat|the prefill/KV-cache mechanism]] in the wild. He notes his 256 K context is *"khoảng 1/4"* — about a quarter — of Claude Code's.

**It partially worked, and the partial success is informative.** Claude Code launched a **background general-purpose subagent** against the local model, which read the repo and correctly connected *"Grafana dashboard"* → deploy monitoring → GCP cloud logging. On camera: *"nó hiểu nè"* — it understands. The comprehension was real; the throughput and reliability were not.

**Vision.** He pasted a dashboard screenshot; Qwen3.5 advertises vision + tools + thinking. Result: `invalid tool parameter` errors.

**Harness mismatch.** Claude Code warned that the model *is not one this version recognises* — which he links to auto-compact and context-window assumptions breaking. **Confirmed first-party:** Anthropic documents that sessions on an unrecognized model ID *"compact at the context window Claude Code assumes for the ID"*, with `CLAUDE_CODE_MAX_CONTEXT_TOKENS` as the override.

## The security observation — unprompted, and the best thing in the video

Mid-run, the agent requested access to his **iCloud Drive** and **Music** folders:

> *"tại sao nó lại đòi vào trong iCloud của mình? Nó đòi vào trong music của mình. Nó đòi access hết luôn"* — why is it asking for my iCloud? My Music? It wants access to everything.
> *"hơi bị nguy hiểm"* — rather dangerous.

He reasons correctly that the agent only needs the project folder, and **denies it** — and the denial is what produces the final "no data" answer. He accepts the worse answer over the broader grant.

This is a **local-model-specific risk that the privacy framing usually obscures.** The corpus's [[../local-ai-coding-agents/privacy-data-residency|privacy-data-residency]] article treats local inference as the strongest privacy posture because weights never leave the machine. True — and incomplete. *Filesystem* scope is a separate axis, and a local agent running with your user's permissions has **more** reach over your personal data than a cloud agent confined to a repo checkout. Local ≠ contained.

## His verdict

Stated twice, unambiguously: locally-hosted open models are **not good enough** for his production environment right now. His bar is **parity with Sonnet**, not the frontier:

> *"ít nhất là nó cũng phải ngang ngửa được với con Sonnet thì mới đủ trình"* — it has to at least match Sonnet to be good enough.

He is happy to trade **speed** for cost. **Quality** is what fails.

## The aside worth keeping — harness over model

Before benchmarking anything, he argues most of Claude Code's power is **not the model**: prompt analysis, subagent launching, logging subagent results, context management, compaction, per-session note-taking.

> *"Với con Sonnet là đủ rồi"* — Sonnet is enough for me. The real strength is *"các cái setup xung quanh nó, architecture đó"* — the setup around it, the architecture.

This is an **independent re-derivation of the corpus's own harness-over-model thesis** from a source with no contact with it. Cross-reference [[../harness-engineering/_index|harness-engineering]] and [[../engineer-of-the-future/_index|engineer-of-the-future]].

## What he plans next

Cloud-hosted open models (**Kimi K3**, which he says is far cheaper than the frontier), **OpenCode**, Kimi's native CLI, and an **Unsloth** quantization run. He notes a 1-bit K3 quant needs ~610–665 GB — **confirmed exactly** against Unsloth's published table (Dynamic 1-bit S = 610 GB, 1-bit M = 665 GB combined RAM+VRAM) — and that this needs his 3-node, ~1 TB-RAM cluster, not the mini.

## Key Takeaways

- **The only real-production-repo test in the bundle, and it returned a negative verdict** at the exact memory tier the corpus never measured.
- **His machine is an M4 Pro (273 GB/s), not a base M4** — his own title is imprecise; Apple's specs settle it.
- **He self-diagnosed the context/KV-cache mechanism correctly** without naming it, matching Apple's first-party framing.
- **Comprehension worked; throughput and reliability did not.** The subagent read and understood a large repo — slowly, hot, and with context-blown API errors.
- **The iCloud/Music access prompt is a genuine finding:** local inference protects your *weights and prompts*, not your *filesystem*. Local ≠ contained.
- **His bar is Sonnet-parity, and local misses it** — while he explicitly accepts the speed penalty.

## See also
[[the-hardware-ladder]] · [[why-agentic-differs-from-chat]] · [[quality-ceiling-and-failure-modes]] · [[claims-scorecard]] · [[../quanit-becoming-ai-engineer-2026/_index|quanit-becoming-ai-engineer-2026]] · [[../local-ai-coding-agents/privacy-data-residency|local-ai-coding-agents/privacy-data-residency]]
