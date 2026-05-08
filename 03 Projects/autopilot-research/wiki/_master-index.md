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

Unified 4-layer stack for controlling Claude Code/Desktop from a phone via Telegram: interface (Telegram/Discord/native Remote Control) → engine (headless Claude Code SDK + Ralph loop) → integration (MCP / Channels / fastmcp) → network (Tailscale / Cloudflare Tunnel / VPS). Includes 4 end-to-end recipes (solo+local-free, solo+VPS-99%, team+private-99.9%, observation-only) and production gaps (secrets vaults, RBAC, audit logs, FinOps, HA). 7 articles, compiled 2026-05-08 from 4 overnight-drained YouTube bundles (23 unique videos across the stack). → [[telegram-remote-control-stack/_index]]
