# (C) hermes-webui — Deep Dive (LLM Wiki v227)

**Repo:** `nesquena/hermes-webui` — *"Hermes WebUI: The best way to use Hermes Agent from the web or from your phone!"*
**Author:** Nathan Esquenazi (`nesquena`) — a disclosed individual (publicly co-founder of CodePath.org). **NOT Anthropic.**
**License:** MIT. **Stack:** Python (standard-library HTTP server) + vanilla JavaScript/HTML/CSS — *"No build step, no framework, no bundler."*
**Wiki:** v227, 2026-07-29. Operator-requested ("build LLM wiki for https://github.com/nesquena/hermes-webui").
**Verification:** INLINE + hand-verified per `feedback_wiki_verify_independently_check_collisions`. **⚠️ NOT source-cloned** — WebFetch (rendered repo + raw README) + the project GitHub-Pages site + WebSearch (identity + landscape) only, per the v200→v226 self-throttle (the ~205K shim overflows every subagent >200K → no workflow).

---

## What it is (one paragraph)

A lightweight, dark-themed, self-hosted **web front-end for Hermes Agent** — the autonomous personal agent by **Nous Research** ("a sophisticated autonomous agent that lives on your server, accessed via a terminal or messaging apps, that remembers what it learns and gets more capable the longer it runs"). hermes-webui gives that terminal agent **browser + mobile** access with, per its own framing, **full CLI parity** — a three-panel layout (left = sessions/nav, center = chat, right = workspace file browser), model/profile/workspace controls in the composer footer, streaming responses, session management, and a workspace file browser. It is **not the agent** — it is a UI layer over an already-installed Hermes install, reusing its existing models and config. The project's GitHub-Pages site labels it **"Hermes — Community Web UI (unofficial)."**

## The load-bearing identity facts (hand-verified)

1. **Third-party / community UI, not the agent.** Hermes Agent is built by **Nous Research**; hermes-webui is a separate repo by `nesquena` that fronts it. The project site self-labels **"(unofficial)"**. Whether strictly community or semi-official, it is a UI *for* a non-Anthropic third-party agent.
2. **⚠️ A search snippet claiming "Nathan Esquenazi is the CEO of Nous Research" is treated as UNVERIFIED / likely a confabulation.** It conflicts with the project's own "unofficial community UI" self-label, and Nathan Esquenazi is publicly known as the co-founder of **CodePath.org**. Nous Research's public leads are Quesnelle / Malhotra / Teknium. Nothing in this wiki relies on the "CEO" claim. What matters: **NOT Anthropic**.
3. **Hermes Agent is a recurring NAMED HARNESS across the corpus but has never been a wiki subject.** cc-switch v73 lists "Hermes Agent" as one of its 6 managed runtimes; ECC v78 ships a "Hermes operator v2.0.0-rc.1"; open-design v83 carries a `hermes-agent` topic. There is also an unmerged autopilot *topic* `hermes-agent` (NousResearch). hermes-webui is the **first repo in the Hermes ecosystem to be a numbered wiki subject** — but as its **UI layer**, not as the agent.

## Architecture (as documented; NOT source-cloned)

- **Backend:** a **Python standard-library HTTP server** (`server.py`, `api/` routes) — no Flask/FastAPI/Django framework dependency at the core (a README summary called the routing "Flask-like," i.e. a pattern, not the framework).
- **Frontend:** **vanilla JavaScript + HTML + CSS variables** for theming; **no bundler / no build step / no framework.**
- **State:** SQLite-backed sessions at `~/.hermes/webui/`.
- **Layout:** three-panel (sessions | chat | workspace), composer-footer controls always visible while composing.
- **Access model:** clones to `~/hermes-webui`, starts on `http://127.0.0.1:8787`; designed to be reached securely over an **SSH tunnel** (one command to start, one to tunnel).
- **Deployment:** Docker (single/multi-container), Nix flake, systemd, launchd.

## Features (documented)

- **Chat & streaming** — real-time token streaming; **multi-provider** (OpenAI, **Anthropic/Claude**, Google, DeepSeek, …) inherited from the underlying Hermes install.
- **Session management** — create / organize / search / pin / archive; projects + tags.
- **Workspace browser** — file preview / edit / create / delete, with Git detection/integration.
- **Voice input** — Web Speech API microphone.
- **Profiles** — switch agent profiles without restart.
- **Security** — optional password auth, passkeys / WebAuthn, OIDC login.
- **Themes** — multiple built-in skins (dark, light, Catppuccin, Geist, …).
- **Cron / Tasks** — background scheduling visible in a Tasks panel.
- **Slash commands** + mobile-responsive (feature parity on phones).

Its own comparison table contrasts Hermes (persistent cross-session memory, self-hosted scheduling) against **Claude Code** — i.e. it positions Hermes as a self-hosted-personal-agent alternative, with Claude available as one of several LLM providers underneath.

## Claude / Anthropic relationship

Claude is a **first-class supported provider** (Hermes's own setup wizard reportedly recommends Claude if you have an Anthropic API key, "one of the strongest models for agentic tasks"), but it is **one of several** providers, and the *subject here is the UI, not the model*. hermes-webui ships **no MCP server** — it is a web front-end, not an agent-tool.

## ⚠️ Stats caveat (§37.4)

The rendered page reported figures like ~16.7k★ / ~2.3k forks / ~7,568 commits / ~326 contributors (+ oddly specific "@rodboev 336 PRs" style contributor lines). These are **page-stated, likely inflated/confabulated by the fetch summarizer, and NOT relied upon** — the GitHub API is mocked in this environment (§37.4), so **no star/velocity claim is asserted and this is NOT a Pattern #52 subject.** Topics (page-stated): `agent`, `ai-agents`, `hermes`, `hermes-agent`, `nous-research`.

## The one genuinely transferable idea

The **"no build step, no framework, no bundler — Python stdlib HTTP server + vanilla JS"** architecture is a sharp *contrast* data-point against the operator's **hireui** (a heavy Next.js monorepo): it shows a full-featured, themeable, auth-gated, mobile-responsive agent front-end shipped with near-zero toolchain. Plus the **passkeys/WebAuthn + OIDC + SSH-tunnel** access model is a clean reference for exposing a self-hosted agent surface safely.
