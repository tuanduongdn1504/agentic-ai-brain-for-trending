# jasonlee-claude-mobile-app — Topic Index

> **Topic:** Jason Lee's "How I built an $80K/Mo mobile app with Claude Code (Full Vibe Code Tutorial)" (`UMjeSU6C4qU`, 2026-07-09, 26:04, ~24.9K views at ingest; channel **@jasonleefinance**, 189K subs) — a vibe-coding tutorial that clones a receipt/expense-scanning iOS+web app ("Track Rabbit") with Claude Desktop Code sessions, Claude Design, Opus 4.8/Sonnet 5 multi-agent cost-tiering, Claude vision, Supabase MCP, Expo Go, and Lottie.
> **Compiled:** 2026-07-11 from the full ~29.8K-char transcript (read in main loop) + double-dive into the first-party originals via Workflow `wf_8eed8f7a-008` (23 agents: 10 dives + 12 refute-first verifiers + critic; ~1.3M tokens, 670 tool calls; 2 agent deaths + 1 empty verifier closed by main-loop takeovers).
> **Scorecard (12 claims): 1 CONFIRMED · 4 CORRECT-BUT-INCOMPLETE · 1 OVERSIMPLIFIED · 6 MISLEADING · 0 fabricated.**
> **Headline:** the *toolchain* is real and reproducible as a prototype; the *business framing* is theater — the "$80K/Mo" belongs to a competitor's unverifiable revenue estimate, and the demo stops exactly where the business begins (auth, RLS, payments, QuickBooks review, App Store review).

## Articles

- [[overview]] — what the video is, what's real, what's theater; the five headline findings
- [[video-summary]] — annotated timestamped walkthrough of the build
- [[the-80k-title-and-revenue-claims]] — title forensics, SimplyWise ground truth, estimate-tool error margins, the channel's title formula
- [[workflow-plan-first-design-first]] — the actual reusable method: plan-first gate, competitor crawl, prompt-for-a-prompt, design-reference image, export-zip roundtrip
- [[claude-design-handoff]] — Claude Design 2.0 facts: June-17 upgrade, WYSIWYG canvas editing, ZIP export, responsive-mockup (not native iOS) scope, /design-sync
- [[multiagent-cost-tiering-reality]] — documented per-subagent model mechanisms vs chat-prompt theater; bugs #44385/#47488; current model lineup + pricing
- [[receipt-scanning-with-claude-vision]] — the correct vision + structured-outputs implementation and per-receipt cost arithmetic
- [[supabase-mcp-and-rls]] — official connector, "never connect to production," prompt injection, mandatory RLS the video never shows
- [[api-key-handling-in-mobile-apps]] — what .env actually protects, EXPO_PUBLIC_ extraction, the server-side proxy pattern
- [[expo-go-to-app-store-gap]] — preview mechanics reality + everything between an Expo Go demo and a shippable App Store product
- [[lottie-and-arcads-layer]] — Lottie mechanics/licensing; the sponsor layer (Seedance garble, Omni Flash mis-attribution, UGC economics)
- [[caveats-and-corrections]] — full verdict scorecard, verifier misfires, the Fable-5 garble-guard save
- [[source-provenance]] — channel forensics, key sibling videos, the affiliate/newsletter funnel

## Cross-links

[[external|Storm Bear: miai-cv-matching-agent]] (vision document-extraction sibling in the recruitment domain) · [[external|Storm Bear: mosh-ai-powered-apps]] (vendor-seam architecture vs this video's direct wiring) · [[external|Storm Bear: open-design]] (Claude Design verified real; OSS alternative) · [[external|Storm Bear: ai-web-design-workflow]] (design-quality gate) · [[external|Storm Bear: api-security-7-techniques]] (key handling, multi-tenant authorization) · [[external|Storm Bear: ai-engineering]] (demo→production discipline) · [[external|Storm Bear: fullstack-docker-cicd]] (the deploy half) · [[external|Storm Bear: hoidanit-fullstack-vibe-coding]] + [[external|Storm Bear: jsm-practical-vibe-coding]] (vibe-coding educator cohort) · [[external|Storm Bear: 10x-claude-code]] (tips-roundup cohort)
