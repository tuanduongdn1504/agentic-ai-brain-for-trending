# jsm-practical-vibe-coding — Topic Index

> **Compiled:** 2026-07-03 · **Source video:** JavaScript Mastery (Adrian Hajdin) "How to Actually Build Mobile Apps with AI in 2026" (Q7AYc2kECDI, 2026-05-15, 3:40:48, ~330K views) — **FIRST-PARTY** methodology video
> **Subject:** the **"Practical Vibe Coding"** workflow — a single `AGENTS.md` context file + a four-part prompt structure + feature-by-feature build-and-verify — demonstrated by building a Duolingo clone ("Lingua") in React Native/Expo with an AI voice teacher powered by **GetStream Vision Agents** (the deep-dive original).
> **Sister topic:** [[jsm-six-file-context/_index|jsm-six-file-context]] (same channel, web-scale six-file system; this is the mobile-scale single-file variant)

## Articles

- [[overview]] — video, thesis, stack, and how this topic relates to the corpus
- [[practical-vibe-coding-workflow]] — the middle-path methodology: feature-by-feature, verify each, fix-prompt discipline, "a perfect prompt is an instruction with a defined scope"
- [[agents-md-anatomy]] — the single AGENTS.md anatomy + the REAL committed file from react-native-lingua + which tools actually auto-read AGENTS.md (Claude Code does NOT)
- [[four-part-prompt-structure]] — pointer → one task → behavioral constraints → design references; constraints-as-behavior; verification-infrastructure prompting
- [[when-ai-knowledge-ends]] — the version-drift problem: docs-pasting, vendor agent skills, Context7, AGENTS.md version-pin rules, committed Claude memory as cutoff countermeasure
- [[vision-agents-deep-dive]] — the ORIGINAL RESOURCE: GetStream/Vision-Agents (Apache-2.0, Python, ~8K★), 3-layer architecture, realtime providers, the two-mode teacher prompt, VAD tuning
- [[skills-supply-chain-second-observation]] — skills-lock.json #2 in production: 21 skills / 4 vendors, the `.well-known` domain mechanism VERIFIED end-to-end, Mintlify-generated vendor skills, PostHog-wizard-installed skill, committed Claude Code auto-memory
- [[stack-and-sponsors]] — Clerk/Stream/PostHog/CodeRabbit/NativeWind verified facts + the monetization structure (5 tracked links, playbook funnel)
- [[verification-and-review]] — the CodeRabbit security catch (token-minting impersonation vuln), fix loop, physical-device testing, and the missing test infrastructure
- [[caveats-and-corrections]] — Rule-12 fail-loud ledger: every refuted/partial claim + 3 verifier misfires overridden with primary evidence
- [[source-provenance]] — sources, workflow run wf_5993da5f-31c (21 agents), ground-checks, and verification method

## One-line takeaway

The video's teachable core is stack-agnostic prompt discipline (AGENTS.md + four-part prompts + one-feature-per-prompt); the load-bearing original is Vision Agents (open Python agent framework on Stream's commercial edge); and the quiet headline for this corpus is the **second production observation of the vendor-skills lockfile supply chain** — now with a live `.well-known/skills/` domain endpoint and committed Claude Code auto-memory.
