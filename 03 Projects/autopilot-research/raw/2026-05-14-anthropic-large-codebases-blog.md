---
source: webfetch-tier-0
url: https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start
title: "How Claude Code Works in Large Codebases: Best Practices and Where to Start"
publisher: Anthropic (claude.com/blog)
published: 2026-05-14
language: en
fetched: 2026-05-21
path: 3-webfetch
notes: First-party authoritative Anthropic guidance on harness engineering at large-codebase scale. 7-component decomposition (CLAUDE.md hierarchy / hooks / skills / plugins / LSP / MCP / subagents) + 3 configuration patterns (navigable / actively maintained / assigned ownership). Designed for enterprise rollout. Companion video by Cole Medin (2026-05-21) walks through every component; helpline repo (coleam00/helpline) implements every component with end-to-end validation.
---

# How Claude Code Works in Large Codebases: Best Practices and Where to Start

> **Source:** Anthropic blog, published 2026-05-14
> **URL:** https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start

## Overview

Claude Code operates in production across multi-million-line monorepos, legacy systems, and distributed architectures with thousands of developers. This article outlines patterns for successful adoption at enterprise scale.

## How Claude Code Navigates Large Codebases

Claude Code navigates codebases like a software engineer — traversing the file system, reading files, using grep to find needed content, and following references. It operates locally without requiring a centralized index.

Unlike RAG-powered tools that embed codebases and retrieve chunks at query time, agentic search avoids outdated results. However, it works best when Claude has sufficient starting context to know where to look. Quality navigation depends on proper codebase setup using CLAUDE.md files and skills.

## The Harness Matters as Much as the Model

The ecosystem around Claude Code — the harness — determines performance more than the model alone. Seven components comprise this extension layer:

### 1. CLAUDE.md Files

Context files Claude reads automatically each session. Root files provide big-picture overview; subdirectory files specify local conventions. Keep them focused to prevent performance degradation.

### 2. Hooks

Scripts triggering at key moments. Most valuable for continuous improvement — reflection hooks can propose CLAUDE.md updates, while start hooks load team-specific context dynamically.

### 3. Skills

Packaged instructions for specific task types, loaded on-demand. They prevent bloating every session with specialized expertise and can be scoped to specific code paths.

### 4. Plugins

Bundled skills, hooks, and MCP configurations distributed as installable packages. Enable new engineers to access the same context and capabilities as experienced team members immediately.

### 5. Language Server Protocol (LSP)

Real-time code intelligence giving Claude symbol-level precision. Enables "go to definition" and "find references" capabilities, preventing pattern-matching errors on identically named functions.

### 6. MCP Servers

Connections to internal tools, data sources, and APIs Claude cannot otherwise reach. Sophisticated teams expose structured search as a tool Claude calls directly.

### 7. Subagents

Isolated Claude instances with separate context windows. Split exploration from editing — a read-only subagent maps a subsystem while the main agent edits with full context.

## Three Configuration Patterns from Successful Deployments

### Making the Codebase Navigable at Scale

**Keep CLAUDE.md files lean and layered.** Load them additively as Claude moves through the codebase — root file for big picture, subdirectory files for local conventions.

**Initialize in subdirectories, not repo root.** Claude works best when scoped to relevant code sections. It automatically walks up the directory tree loading every CLAUDE.md file.

**Scope test and lint commands per subdirectory.** Running full suites when Claude changes one service causes timeouts. Subdirectory CLAUDE.md files should specify applicable commands.

**Exclude generated files and build artifacts.** Use `.claude/settings.json` to version-control `permissions.deny` rules, ensuring consistent noise reduction across the team.

**Build codebase maps for unconventional structures.** A markdown file listing top-level folders with descriptions helps Claude scan before opening files.

**Run LSP servers for symbol-based searching.** Grep returns thousands of matches; LSP returns only relevant symbols, filtering before Claude reads anything.

### Actively Maintain CLAUDE.md Files

As models evolve, instructions written for current models may constrain future ones. A rule telling Claude to break refactors into single-file changes might prevent newer models from making beneficial cross-file edits.

Teams should review configurations every three to six months, especially after major model releases.

### Assign Ownership for Claude Code Management

Technical configuration alone doesn't drive adoption. Successful rollouts had dedicated infrastructure investment before broad access.

Small teams wired tooling so Claude fit developer workflows on day one. At one company, engineers built plugins and MCPs available immediately. At another, an entire team managed AI coding tools before rollout.

**Establish a Dedicated Role:**

- Developer experience or developer productivity teams typically own this
- An emerging role is "agent manager" — a hybrid PM/engineer function managing the Claude Code ecosystem
- Minimum viable version: one DRI with ownership over configuration, authority on settings, plugin marketplace, and CLAUDE.md conventions

**Prevent Fragmentation:**

Without centralization, knowledge stays tribal and adoption plateaus. Someone must assemble and evangelize Claude Code conventions, preventing thousands of engineers from independently rebuilding the same solutions.

**Address Governance Early:**

In regulated industries, establish cross-functional working groups with engineering, information security, and governance representatives. Define requirements together and build rollout roadmap.

Start with approved skills, required code review processes, and limited initial access. Expand as confidence builds.

## Applying These Patterns to Your Organization

Claude Code is designed around conventional software engineering environments: engineers as primary contributors, Git-based repos, and standard directory structures. Most large codebases fit this mold.

Non-traditional setups — game engines with binary assets, unconventional version control, or non-engineers contributing — require additional configuration. For complex deployments, Anthropic's Applied AI team works directly with engineering organizations to translate patterns into specific requirements.

---

**Related Articles (linked from original):**
- How an Anthropic Sales Leader Uses Claude Cowork
- Deploying Claude Across the Legal Industry
- How Anthropic's Legal Team Cut Review Times
- Deploying Claude Across Financial Services
