# (C) palmier-pro — Deep Dive

**Subject:** `palmier-io/palmier-pro` — *"The video editor built for AI."*
**Source-verified at commit:** `9a3ae5028...cf043b8d2` (clone HEAD, last commit 2026-07-01, "Add v0.5.2 to appcast")
**Requested:** 2026-07-03 — "build LLM wiki from this repo, double deep dive into the original resource, then pilot methods for my workflow."
**Method:** 6-agent read-only research fan-out (repo page, source-code clone+read, author identity, landscape/positioning, security/supply-chain, pricing/business-model) + hand verification per `feedback_wiki_verify_independently_check_collisions`.

---

## 1. What it actually is (corrects a wrong first guess)

The vault's project-history is full of *code*-context/*code*-graph MCP servers (graphify, GitNexus, codegraph, codebase-memory-mcp — CONFIRMED Library-vocab #23). Given the name and MCP angle, that was the first hypothesis. **It is wrong.** Palmier Pro is **not** a coding tool at all — it is a **native macOS video editor**, and the "for AI" in its tagline means two very different things at once:

1. It has **generative AI models wired directly into its timeline** (Seedance 2, Kling 3, Nano Banana Pro, GPT-image-2, Veo, Suno, etc.) — you can generate a clip, image, or audio track *in place* on the timeline instead of round-tripping through a separate tool and re-importing files.
2. It **ships its own MCP server**, so an external coding agent (Claude Code, Claude Desktop, Codex, Cursor) can open a real editing session and drive the timeline directly — read state, add/trim/reorder clips, generate media, apply color, export — via 51 well-scoped tools.

There is a **different, older product also called "Palmier"** from the same two-person team (a GitHub-integrated AI code-review tool, YC S24 2024 launch, "Be a 10x developer with Palmier"). It is a separate repo, appears less active, and is **not** the subject the operator linked. Don't conflate them.

---

## 2. Company & authorship (verified by hand)

- **Palmier, Inc.** — San Francisco, incorporated 2024, **Y Combinator S24** batch, 2 employees (as of Mar 2026).
- **Founders (fully disclosed):** Marcos Rico Peng (CEO, UC Berkeley EECS, ex-LinkedIn infrastructure engineer) and Harrison Tin (CTO, UC Berkeley EECS, ex-Microsoft).
- **Funding:** ~$500K pre-seed/seed. Investors: Y Combinator, Immeasurable, Interlace Ventures, Scale Asia Ventures, Giovanni Gardelli, Preetha Parthasarathy.
- **Not Anthropic-affiliated.** Verified explicitly — Palmier is not listed on Anthropic's partner hub/services track, and Claude is one of three supported agent backends (Codex and Cursor get equal billing in the README).
- Revenue ($440K/2025, per Latka) is company-self-reported and **not independently corroborated** — flagged, not relied on for anything.

## 3. License & business model (open-core, cleanly disclosed)

- **GPLv3** covers the editor, the MCP server, and the in-app agent chat — genuinely open source, no fork of it required.
- **Closed source:** the generative-AI processing backend (cloud-hosted). The repo's own words: *"The only thing that is closed source is the generative AI processing."*
- **Pricing:** editor is free forever, no login. Generation requires an account + subscription — Pro $29/mo (launch price, list $49) or Max $69/mo (list $99), both metered in credits across video/image/audio/upscale/chat. Enterprise is "contact us," with the FAQ admitting team/security features are still being built.
- Single repo — **no separate free-tier sibling repo** exists; the open/closed split is a feature split inside one codebase, not a repo split.

## 4. Architecture (from the source read, not just the README)

- **Native macOS app, Swift 6.2**, SwiftUI + AppKit hybrid, Metal shaders for compositing/color, requires **macOS 26 "Tahoe" on Apple Silicon** (this is Apple's real, current OS-version naming scheme since 2025 — not a typo or a future-dated placeholder, correcting an initial mis-read by one research agent).
- **~325 Swift files**, three real subsystems:
  - **Editor** — `EditorViewModel` + ~40 extension files (ripple/overwrite engines, snapping, keyframes, color grading, captions), `TimelineView`/`PreviewView` for frame-accurate AVFoundation compositing.
  - **Agent/MCP** — wraps the official `modelcontextprotocol/swift-sdk`; an HTTP MCP server on `127.0.0.1:19789/mcp` (not stdio); a `ToolExecutor` dispatcher (21 extension files) implementing **51 MCP tools** (`get_timeline`, `add_clips`, `remove_clips`, `generate_video`, `generate_image`, `apply_color`, `set_keyframes`, `add_captions`, `export_project`, `search_media`, `get_transcript`, `inspect_media`, …); a separate in-app `AgentService` chat panel that routes either straight to the Anthropic API or to Palmier's own cloud backend, and reads a `.agents/skills` folder for skill context.
  - **Generation** — a `GenerationService` abstracting multiple video/image/audio providers with per-model cost estimation and an async submit → poll → auto-import pattern (no webhooks).
- **Visual semantic search:** SigLIP 2 (Google, Apache-2.0) converted to Core ML, used to search the media library by content.
- **Dependencies:** `modelcontextprotocol/swift-sdk`, Sparkle (auto-update), Sentry (error reporting), Clerk (auth), Convex (real-time backend/persistence), `swift-transformers` (Core ML inference), Lottie.
- **Tests:** 13.9K lines across 90+ files; the MCP tool layer alone (`ToolExecutorTests.swift`) is 1,885 lines — the best-tested subsystem in the repo.
- **CI:** GitHub Actions on a `macos-26` runner, `swift build` + `swift test`, 40 min timeout — nothing exotic.
- **Distribution:** signed + notarized DMG via a release script; Sparkle appcast for auto-update. No `curl|bash`, no postinstall scripts, no binary downloads at install time. **No checksum/signature published for the DMG itself**, though — you download on trust, same as most Mac shareware.
- **Non-sandboxed** app (full file + network + camera entitlements) — a deliberate trade-off to support arbitrary file I/O and the MCP tool surface.

## 5. What's honestly unfinished / flagged

- Acknowledged by the team and early Hacker News commenters as early: missing transitions, masking, some graphics — this is a ~3-month-old product (created 2026-04-07, first public splash mid-June 2026).
- **No published benchmarks** anywhere (generation speed, export stability, credit efficiency, agent-edit accuracy) — the FAQ is candid about this.
- **Sentry is a shipped runtime dependency, but the README says nothing about telemetry consent or what's collected** — a real documentation-vs-code gap. `UserDefaults` key `io.palmier.pro.telemetry.enabled` defaults to `true`.
- Stars (~9.8k) / forks (~708) are **page-stated, not API-verified** (this environment mocks the GitHub API per the vault's §37.4 discipline) — not a velocity claim, just descriptive.
- macOS-only, Apple-Silicon-only, very-recent-OS-only — a narrow platform footprint by design.

## 6. What makes it interesting for this vault specifically

Every prior MCP server this vault has studied (code-graph tools, `google_workspace_mcp`, `devspace`, `cortex-hub`, `agentmemory`) was **built to be an agent tool first** — the MCP surface *is* the product. Palmier Pro inverts that: it is **a complete, independently valuable consumer product first** (a real, sellable video editor a non-technical creator could use and never touch an agent), and MCP-nativity is a **bolted-on feature for power users**, exactly like the trend now playing out across Figma/Notion/Linear/Blender-class tools shipping MCP servers alongside their existing GUI. That's the transferable lesson — see the Verdict doc for the exact pattern classification, and the Pilot Methods Menu for how to apply it.
