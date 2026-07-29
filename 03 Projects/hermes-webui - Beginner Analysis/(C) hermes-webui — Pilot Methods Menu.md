# (C) hermes-webui — Pilot Methods Menu (LLM Wiki v227)

**Blunt framing:** hermes-webui is a **web front-end for a specific third-party self-hosted personal agent (Hermes, by Nous Research)** — NOT a hireui component and NOT a coding-agent tool. Its value to the operator is **read-and-borrow** (the no-build architecture + the auth/access model) + optionally running it as a **personal** Claude-backed agent surface. Hermes Agent itself is the **AVOID-for-hireui** subject already recorded (per the hermes-agent memory: hireui AVOID / borrow the Hermes-as-MCP-server pattern). This is an honest ~14-method menu, not a padded 24.

**⭐ One-thing path: A1 → B5** (read the no-build architecture, zero install → borrow the WebAuthn/OIDC/SSH-tunnel access-model + the zero-toolchain-front-end idea as a hireui/agent-surface reference). Optional personal-use: C10.

---

## A — Read & learn (zero install, on-goal)

- **⭐ A1** Read the README + ARCHITECTURE.md as a case study in a **full-featured agent web UI with no build step / no framework / no bundler** (Python stdlib HTTP server + vanilla JS + CSS-variable themes). The single most transferable takeaway for a web dev.
- **A2** Read the three-panel + composer-footer layout as a reference for an agent chat/workspace UI (sessions | chat | file browser).
- **A3** Read the Hermes-vs-Claude-Code comparison table as a landscape map (persistent cross-session memory + self-hosted scheduling = what a *personal* autonomous agent adds over a coding agent).
- **A4** Read the access model (localhost `:8787` + SSH tunnel + optional password/WebAuthn/OIDC) as the reference for exposing a self-hosted agent surface safely.

## B — Borrow patterns (zero/low install, on-goal)

- **⭐ B5** Lift the **WebAuthn/OIDC + SSH-tunnel + localhost-first** access-model into any note/spec on exposing a self-hosted agent or internal tool safely (composes with hireui's api-security thread — the standing BOLA/authz + CSP items).
- **B6** Record the **no-build vanilla-JS + stdlib-HTTP** architecture as a deliberate *contrast* data-point against hireui's heavy Next.js monorepo — a reminder that a full agent front-end need not carry a large toolchain (a reference, not a migration).
- **B7** Borrow the **theming-via-CSS-variables + multiple built-in skins** approach as a lightweight design-token pattern.
- **B8** Note the **provider-agnostic seam** (Claude one of OpenAI/Google/DeepSeek) as another data-point for hireui's vendor-seam file (composes with meetily v196 `generate_summary()` / AIRI v210 xsAI / lobehub v222 / the mosh-ai A2 seam).

## C — Hands-on / personal (scratch, off-goal-personal)

- **C9** Install-snapshot, then `git clone` + `python3 bootstrap.py` on a scratch machine to see the UI (⚠️ requires an existing Hermes Agent install; NOT source-cloned → inspect `bootstrap.py`/`start.sh` first; localhost-only).
- **⭐ C10** Run it as a **personal** Claude-backed self-hosted agent surface (BYO Anthropic key into Hermes; localhost + SSH tunnel; never a hireui/candidate-data context).
- **C11** Try the passkeys/WebAuthn auth flow as a working reference implementation.
- **C12** Compare it side-by-side with lobehub v222 / Open WebUI as self-hosted agent-UI options for personal use.

## D — hireui / Goal-#2 (fenced — read/borrow only, NOT adopt)

- **D13** Borrow the **auth/access-model** (B5) into hireui's own admin/internal-tool surface spec — architecture only, on an `agent-*` branch, per hireui's CONSTITUTION (I-2/I-8/GitNexus-first). hireui stays hand-built; hermes-webui is not a component.
- **D14** ⚠️ **Do NOT** put a personal-autonomous-agent web UI into hireui (a recruitment SaaS) or point Hermes at candidate data — Hermes has file r/w + cron + tool-calling; candidate PII + an autonomous agent = a data-residency/authz problem, not a feature.

## Fence

install-snapshot before `python3 bootstrap.py` + inspect `bootstrap.py`/`start.sh`/the Docker compose (NOT source-cloned → untrusted) + localhost-only + SSH-tunnel for remote + enable WebAuthn/OIDC auth + BYO key never a live/shared account + personal-use only, never a hireui/candidate-data context + pin a commit (stats/releases page-stated §37.4) + Hermes Agent itself stays AVOID-for-hireui (borrow the Hermes-as-MCP-server pattern instead, per the hermes-agent memory).
