# Caveats and corrections

> Rule-12 fail-loud record. What not to take at face value — in the sources, in the verification agents, and in this vault's own tooling.

## A. Corrections to the sources

1. **"Warp open-sourced their entire code base" (ForrestKnight) — overstated.** Warp open-sourced the **client** on **2026-04-28** under **AGPL-3.0** (UI framework crates MIT). **Oz**, their cloud agent-orchestration platform, remains **fully proprietary**. Say "open-sourced its client", never "its entire codebase".
   ⚠️ **AGPL-3.0 matters for this operator.** Per the standing vault position (see the ToolJet and Firecrawl threads), AGPL blocks vendoring into hireui. Warp is fine to *use*; do not copy code out of it.

2. **The Ollama integrations list (anchor) — FALSE as read.** Actual index: **Claude Code · OpenCode · DeepSeek Harness · OpenClaw · Hermes Agent · VS Code**. Codex, GitHub Copilot and Xcode are **not** listed. He was reading a screen quickly mid-demo; the error is transcription-level, not analytical.

3. **"M4 Max = 546 GB/s" (Tech With Tim) — needs its qualifier.** That is the **40-core-GPU** M4 Max. The **32-core** variant is **410 GB/s**. He uses the higher figure in a Mac-vs-PC comparison without saying which bin.

4. **"Mac mini M4, 64 GB" (anchor) — impossible as stated.** Base M4 tops out at **32 GB**. His machine is necessarily a **Mac mini M4 Pro** (273 GB/s). This is a correction *toward* him — the M4 Pro number explains his results better than the base-M4 number would.

5. **The VRAM ladder (Tech With Tim) — quantization-dependent.** 8→7B / 12–16→14B / 24→32B / 64+→70B only works at roughly 4-bit. At FP16 a 7 B model needs ~14 GB. And it is a *chat* ladder; agentic context pushes every rung up. See [[the-hardware-ladder]].

6. **"75–80% of unified memory is usable" — unsourced.** No Apple primary documentation states this. It may well be a good rule of thumb; it is not a citable fact. Same for any `iogpu.wired_limit_mb` default.

## B. Sponsorship and incentive disclosures

Recorded because they shape framing, not because they invalidate measurements:

- **ForrestKnight is AMD-sponsored** for the video — he discloses it on camera and the entire test rig is AMD (Threadripper 9980X, Radeon AI Pro R9700, ROCm). His *measurements* on real codebases are the most rigorous in the bundle; his *hardware recommendations* are paid placement.
- **Tech With Tim** carries two sponsor reads (here.now hosting, WhisperFlow dictation) plus an affiliate link.
- **Zen van Riel** promotes a paid AI-engineering community.
- **Apple's session is vendor marketing for Apple silicon** — specifically for the M5 generation. The 4× matmul claim is first-party and unaudited. It is still the best-sourced statement in the bundle about the agentic bottleneck, because Apple is the only party here with visibility into the silicon.

**No source in this bundle is disinterested.** Three of seven sell hardware, tooling, or community adjacent to the conclusion.

## C. ⚠️ Verification-agent errors caught in the main loop

The maker/checker split earned its keep twice. Both errors would have shipped falsehoods into the wiki.

7. **"No Qwen3.6 model exists" — FALSE, and it would have contradicted an existing corpus topic.** The `verify:qwen-models` agent returned UNRESOLVED on C4, asserting Qwen3.6 does not exist and listing the Qwen3 lineup (0.6B–32B, 30B-A3B, 235B-A22B) as the current state of the art. That is the **April-2025 Qwen3 release**, recited from stale training data.

   **Reality, checked in the main loop:** **Qwen3.6-27B** was released **2026-04-22** under Apache-2.0 — dense, 262K context extensible to 1M, natively multimodal, published at `Qwen/Qwen3.6-27B`. There is also a Qwen3.6-35B-A3B, a Qwen3.5-397B-A17B, and a QwenLM/Qwen3.8 repo.

   **Why this was caught:** three independent sources in the bundle said "Qwen 3.6", and the corpus *already has a `local-ai-coding-agents/qwen3.6-27b` article*. An agent verdict that contradicts three sources **and** an existing corpus page is a signal to check the agent, not the sources. Logged per the standing discipline: *lens/critic agents and web summaries confabulate — verify identity claims yourself.*

8. **"Qwen 3.5 does not exist" — overturned by the workflow's own refuter.** The same agent denied Qwen3.5; the adversarial pass found the official model cards (Qwen3.5-9B/4B/2B) stating *"262,144 natively and extensible up to 1,010,000 tokens."* **The anchor's on-screen "1 million context" reading was correct.** The refute-first stage worked exactly as designed — one agent's stale inventory, overturned by another agent forced to argue the opposite.

**Pattern:** both errors are the same failure — an agent's *model-inventory knowledge* lagging reality by roughly a year, expressed with confidence. Model-existence claims from agents are now to be treated as low-trust by default in this project.

## D. ⚠️ A tooling bug in this vault, found by this ingest

**`bin/autopilot-drain.py` silently dropped any video whose title contains a pipe character.**

The `yt-dlp --print` template used `|` as its field delimiter. This anchor's title — *"Thử local LLM, coding trên Mac mini M4, 64GB ram **|** quanIT"* — split into 9 fields where the parser required exactly 8, so `yt_meta()` returned `None` and the run logged **"anchor unreachable"**. The URL was perfectly reachable.

The same `len(parts) != 8: continue` existed in `yt_search()`, so **search results with pipes in their titles were silently discarded from the candidate pool** — a very common YouTube title convention.

**Observed impact on this run:** before the fix, the rubric selected 6 videos of which **3 were from 2025** and it logged *"only 5 pass recency filter; relaxing"*. After the fix, **all 6 picks were from 2026** and no relaxation was needed. The shrunken pool had been forcing the rubric to reach backwards in time.

**Fix applied 2026-08-20:** delimiter changed to `|@@|` in both `yt_meta()` and `yt_search()`; the silent `continue` in `yt_search()` now increments a counter and emits a `WARN` line; the misleading *"anchor unreachable"* message now reads *"anchor probe returned no usable metadata"*. Original backed up to `/tmp/autopilot-drain.py.bak`.

**This bug predates this ingest and has been degrading bundle quality for the corpus's entire history.** Every past bundle was selected from a pool with pipe-titled videos silently removed. Prior topics are not wrong, but their *source selection* was narrower than the logs implied.

## E. Scope limits of this topic

- **Nobody demonstrated success on a large pre-existing repository** — not the six YouTubers, not Apple. The two sources that tried (anchor, ForrestKnight) hit walls. Positive verdicts in this bundle are all greenfield or toy.
- **Every source was screen-recording while benchmarking**, and at least three say so degraded their own results. Treat all throughput figures as pessimistic-but-uncalibrated.
- **No M5-generation agentic-coding measurement exists here.** Apple claims 4× matmul on M5; nobody in the bundle tested an M5 against a real repo. This is the single biggest open question — see [[_index]] deepen candidates.
- **Costs were not modelled.** The economics live in [[../local-ai-coding-agents/hardware-economics-and-tco|local-ai-coding-agents/hardware-economics-and-tco]] and this topic does not revisit break-even, only the hardware premises underneath it.

## Key Takeaways

- **Zero fabrications from the sources; one FALSE** (the anchor's off-screen list read).
- **The dominant source error is a dropped qualifier**, not a false statement — "546 GB/s", "entire codebase", the VRAM ladder.
- **Two verification agents got model existence wrong** in the same direction (stale inventory, stated confidently). One was caught by the main loop, one by the workflow's own refuter.
- **A real bug in this vault's own drain script was found and fixed** — and it had been quietly narrowing source selection for the whole corpus.
- **No source here is disinterested**, Apple least of all.

## See also
[[claims-scorecard]] · [[the-hardware-ladder]] · [[source-provenance]] · [[quality-ceiling-and-failure-modes]]
