# (C) Open Questions — Rowboat v43

## Product strategy

1. Does Rowboat Labs have a paid SaaS tier yet? Landing page minimal — only download links. If undeclared paid tier coming, Pattern #31 Open-Core data point firms up; if pure-OSS-with-no-monetization-yet, observation-only.
2. Why did the product pivot from multi-agent SaaS (`apps/rowboat`) to personal-AI-coworker desktop (`apps/x`)? Is the legacy SaaS deprecated or maintained-in-parallel?
3. What's the relationship between `apps/x` (Electron) and `apps/rowboatx` (Hono CLI server, npm v0.16.0)? Are they competing surfaces or complementary?
4. Is `@rowboatlabs/rowboatx` v0.16.0 npm package deployable as a self-hosted backend that the Electron app connects to, or is it standalone?

## Architecture

5. Track Blocks: 4 trigger types (manual / cron / window / once / event). Does this generalize beyond rowboat — should Storm Bear vault adopt YAML-fenced live-updating regions?
6. Knowledge graph: hybrid mtime+hash change detection. What's the throughput — how many notes can rowboat process before state file becomes bottleneck?
7. Pass-1 routing classifier (LLM batched at 20-track-batch) + Pass-2 agent veto. Does this 2-pass pattern generalize to other event-driven LLM systems?
8. Single-writer invariant (renderer never writes; backend single writer). Why this discipline? Was there a race condition that motivated it?

## Integrations

9. Composio integration: is rowboat one of Composio's major customers, or just a generic MCP-server-bridge user?
10. Klavis API key support (in start.sh, USE_KLAVIS_TOOLS=true). What is Klavis? (Cloud agent infra not surfaced in README.)
11. Fireflies meeting-notes integration alongside `Rowboat meeting notes` — does Rowboat have its own meeting-notes capture, or is this a placeholder?
12. Voice: Deepgram (STT) + ElevenLabs (TTS). What's the latency/cost profile? Is local-Whisper option planned?

## Commercial / org

13. Rowboat Labs team size — README acknowledges Twitter @rowboatlabshq (org) but only one contributor publicly visible (Ramnique Singh via PyPI metadata).
14. YC S24 — what's the seed-funding amount? Affects bus-factor + sustainability assessment.
15. Discord (https://discord.gg/wajrgmJQ6b) — community size signal for Pattern #50 Commercial-Funnel companion-platform observation.

## Pattern observations

16. Knowledge-graph-as-Markdown explicitly Obsidian-compatible — is Karpathy /raw folder an acknowledged inspiration? Check Discord, Twitter, blog posts.
17. Local-first + bring-your-own-model — does this position rowboat as Mem0/Letta/MemGPT competitor, or distinct category?
18. Triple-package divergence (rowboat repo + @rowboatlabs/rowboatx npm + rowboat PyPI) — Pattern #58 3rd data point candidate; observational only at v43.
19. 4-surface distribution at T5 (desktop binary + Docker + npm + PyPI) — corpus-first; is this YC-startup-pragmatism (cover all bases) or deliberate strategy?

## Storm Bear pilot

20. Can rowboat point at existing markdown vault (Storm Bear corpus) without overwriting it?
21. Does rowboat's auto-tagging conflict with Obsidian-property syntax used elsewhere in vault?
22. Track Blocks — could YAML-fenced live-updating regions be back-ported into Storm Bear vault as a manual-Claude-Code-skill convention?
23. What happens if rowboat's Pass-1 routing classifier hallucinates relevance for a Storm Bear vault note? Is there a kill-switch?
24. Multi-vault support — can rowboat manage Storm Bear vault + a separate scratch vault simultaneously?

## Routine v2.2 implications

25. YELLOW primitive-count 2nd execution (after pi-mono v36) preserves velocity plateau. When does informal discipline become routine v2.2 formalization (variable entity count)?
26. 7-streak zero-registration — at what streak length does the discipline become structural (vs sustainable strengthening run)?
27. Implicit-Karpathy-touchpoint observation at T5 (rowboat's Obsidian-vault parallel without explicit citation) — should Pattern #19 archetype 1 add new sub-classification "implicit structural parallel" alongside "explicit citation"?
