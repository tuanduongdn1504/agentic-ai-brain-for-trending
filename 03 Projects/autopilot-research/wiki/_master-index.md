# Knowledge Base Index

> Topics will be listed here as they are created.
>
> **Index format:** `## <Topic>` heading per topic + 1-line description + link to `wiki/<topic>/_index.md`.
> **Maintained by:** Claude Code per the rules in `../CLAUDE.md`. The autopilot-research-routine updates this file at the end of every `compile` cycle.

---

## claude-code-hooks

Claude Code's deterministic event-driven shell command system — 9 lifecycle events (session start/end, pre/post tool use, stop, etc.), command-vs-prompt-hook split, common patterns (notifications, CLI enforcement, code quality, destructive-command blocking). 5 articles, compiled 2026-05-07 from a 5-video YouTube bundle. → [[claude-code-hooks/_index]]

## workflow-ai-coding

How senior practitioners (Matt Pocock, Ryan Lopopolo @ OpenAI, Anthropic Skills team, Boris from Claude Code, Greg Isenberg) actually steer AI agents through software development. Covers the Ralph Wiggum loop, planning-first workflow, persistent memory (`claude.md`), skills-over-agents architecture, harness engineering, and 6 axes of expert disagreement (code-is-free vs code-is-expensive, plan-mode vs grill-me, etc.). 5 articles, compiled 2026-05-07 from a 6-video YouTube bundle. → [[workflow-ai-coding/_index]]

## 10x-claude-code

Tactical tips/tricks roundup from 6 creators (Sean Kochel, Nate Herk, Eric Tech, Boris Cherny via YC, Chase AI, AI LABS) — concrete configurations to 10x Claude Code workflows. Covers status lines, git worktrees, custom skills, hooks with Exit Code 2, MCP CLI mode, the Karpathy LLM-wiki pattern, adversarial fact-checking agents, and 5 axes of creator disagreement (Opus-everything vs model-switching, plan-mode lifespan, claude.md minimalism, browser strategy, terminal vs GUI). 5 articles, compiled 2026-05-07 from a 6-video YouTube bundle. → [[10x-claude-code/_index]]

## telegram-remote-control-stack

Unified 4-layer stack for controlling Claude Code/Desktop from a phone via Telegram: interface (Telegram/Discord/native Remote Control) → engine (headless Claude Code SDK + Ralph loop) → integration (MCP / Channels / fastmcp) → network (Tailscale / Cloudflare Tunnel / VPS). Includes 4 end-to-end recipes (solo+local-free, solo+VPS-99%, team+private-99.9%, observation-only) and production gaps (secrets vaults, RBAC, audit logs, FinOps, HA). **Pilot-verified Recipe A end-to-end 2026-05-08** — caught 5 deviations from bundle's published commands; corrected ritual lives in [[telegram-remote-control-stack/setup-recipe-a]]. 8 articles, compiled 2026-05-08 from 4 overnight-drained YouTube bundles (23 unique videos) + live pilot deployment. → [[telegram-remote-control-stack/_index]]

## harness-engineering

Ryan Lopopolo's (OpenAI Frontier & Symphony) discipline of restructuring code, workflow, and organization around the assumption that **humans steer and agents execute** — codified as an anchor research thread. Anchored on the AI Engineer 2026 keynote (46:20) + Latent Space podcast (1h12m) — same speaker, two media, three weeks apart. Covers 8 falsifiable claims (zero-code at 1M LOC, $2-3K/day token cost, 1-min build-loop constraint, 5-10 PRs/day/eng via Symphony, hyper-modular 750-package architecture, post-merge review, dependency vendoring, GPT-5.2 isomorphism), 10 defined terms (Harness Engineering, Token Billionaire, Symphony, Frontier, Ghost Libraries, Agent-Legibility, Dark Factory, Ralph Loop, Skills, Isomorphic), 35+ cited references (downstream research surface), 10 open questions, and 10 contrarian stances. **Designed for ongoing ingestion** — each article structured so future ingests slot into existing buckets (claims/terms/references/questions/stances). Includes prioritized 10-candidate research roadmap. **9 articles** as of 2026-05-09 — adds [[harness-engineering/blog-talk-evolution]] (Feb→Apr Lopopolo evolution) + [[harness-engineering/symphony-architecture]] (6-source triangulation: 3 OpenAI + 3 community Elixir/Go/Rust implementations). Symphony architecture article documents falsifier check on claim #4 throughput (NOT INDEPENDENTLY CORROBORATED) and demonstrates pivot pattern when "open-source spec" pages fail bypass — pivot codified into bypass-403 skill Phase 4.5. → [[harness-engineering/_index]]
