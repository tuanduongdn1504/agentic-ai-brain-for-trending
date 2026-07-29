# (C) hermes-webui — Verdict (LLM Wiki v227)

**Rating: GOAL-ALIGNED INCLUDE 3/4** — `[(a) FAIL · (b) MODERATE keys the tier · (c) STRONG ⚠️MODERATE-reviewable · (d) STRONG]`. **NO MINT.** Counts **46/11 UNCHANGED**; §C live standalones **47** unchanged.

Cleanly GOAL-ALIGNED via §31 on (b) MODERATE+ (no §40 operator-direction needed). ⚠️ An **OFF-GOAL reading is defensible** and recorded as the reviewable alternative (see below).

---

## The four axes

**(a) FAIL** — Nathan Esquenazi (`nesquena`) is a disclosed individual (CodePath.org co-founder), **NOT Anthropic** (§41 — no Anthropic affiliation, no registered (a)-7 vendor-direct source; the disclosed-individual (a)-axis is answered NO; #19 19a first `nesquena`/Nathan-Esquenazi author). ⚠️ The lone "CEO of Nous Research" search snippet is UNVERIFIED/likely-confabulated and is not relied upon — and even if true, Nous Research ≠ Anthropic, so (a) FAILs either way.

**(b) MODERATE — keys the tier.** hermes-webui is the **web-UI layer for a self-hosted autonomous agent** (Hermes) that runs **Claude as a first-class provider** — it lands on the agent-infrastructure substrate the vault studies (self-hosted-agent-UI family OpenHuman v118 / PilotDeck v175 / lobehub v222; the GUI-client family CodePilot v161 §C#27) and is a genuine architecture study for the operator (a web dev building hireui). Held **below STRONG** because: it is a **front-end/GUI wrapper, not the agent** and not the Claude/agent substrate itself; it fronts a **general-purpose personal agent, not a software-development coding agent** (off the Goal-#1 core); and Claude is **one of several** providers, inherited from the underlying Hermes install. Calibrates just below lobehub v222 (b) STRONG (a flagship full platform) and at the meetily v196 / AIRI v210 MODERATE band — a goal-adjacent UI/infra layer.

**(c) STRONG (⚠️ MODERATE-reviewable)** — a real, feature-rich, self-hosted web app: streaming chat, session management, workspace file browser + Git, voice, profiles, passkeys/WebAuthn/OIDC auth, themes, cron/Tasks, mobile-responsive, multi-deploy (Docker/Nix/systemd/launchd) — all on a deliberate **no-build vanilla-JS + Python-stdlib-HTTP** architecture. Caveats keeping it reviewable: it is a **thin front-end** whose hard parts (memory, skills, scheduling, model orchestration) live in the underlying **Hermes Agent**, not here; the "unofficial community UI" framing; **⚠️ NOT source-cloned** (WebFetch/README/site/landscape-verified); **stats page-stated + likely inflated** (§37.4) → NOT #52.

**(d) STRONG** — the GUI-client family (CodePilot v161 §C#27 — the direct-but-distinct boundary) · the self-hosted-agent-web-UI family (OpenHuman v118 / PilotDeck v175 / lobehub v222 / the LibreChat/Open WebUI genre) · the provider-agnostic-seam thread (#84 84c; cc-switch v73 / meetily v196 / AIRI v210 xsAI / lobehub v222) · **the Hermes-ecosystem thread** (Hermes-Agent-as-named-harness in cc-switch v73 / ECC v78 / open-design v83) · the WebAuthn/OIDC/SSH-tunnel access-model thread · hireui as the web-app architecture contrast.

## Pattern outcome: NO MINT

- **NOT a clean N=2 of §C#27** (CodePilot's "Desktop GUI Client / Visual Front-End for a CLI **Coding** Agent"). hermes-webui is DISTINCT on **two** axes: it fronts a **general-purpose personal agent** (not a *coding* agent — §C#27's scoped criterion), and it is a **web** UI (browser + mobile), not a **desktop** app. It is recorded as an **ADJACENCY / instance-strengthening** of the GUI-client-for-an-agent genre, not a §C#27 N=2.
- **No new §C standalone.** The candidate mint — *"Web GUI Front-End for a Self-Hosted General-Purpose Personal Agent (browser + mobile, provider-agnostic, no-build)"* — is **DECLINED** and recorded as the operator/audit-reviewable **alternative**: it LOSES on (i) **form-factor-within-genre** (web-vs-desktop + general-vs-coding-agent are delivery choices within the GUI-client / self-hosted-agent-UI families — the camofox v179 / lobehub v222 draw-the-circle discipline; §C vocab is agent-capability-shaped, and "a web front-end for one specific agent" is packaging, not a new capability), (ii) **NOT world-first** (Open WebUI / LibreChat / lobehub v222 saturate "self-hosted web chat UI for an agent/LLM"; plus Hermes's own surfaces), and (iii) **§28** anti-inflation on a thin single-agent front-end. The **lobehub v222 precedent is decisive**: a far larger, flagship self-hosted provider-agnostic web agent *platform* was itself NO MINT ("world-canonical NOT world-first, fame ≠ mint") — hermes-webui is a much thinner, single-agent-specific version of that.
- **No new top-level pattern** (max #85). Counts **46/11 UNCHANGED**; §C live standalones **47** unchanged; §C surface unchanged.

## Secondary (recorded, NOT minted)

- **#19 19a** first `nesquena` / Nathan-Esquenazi author.
- **Hermes-ecosystem cross-ref** — the first numbered-wiki subject in the Hermes ecosystem (Hermes Agent = a named harness in cc-switch v73 / ECC v78 / open-design v83 + an unmerged autopilot topic, never a subject); this is its **UI layer**, a companion/satellite. **NOT #57** (it is a front-end for Hermes, not an influence-citation of a corpus subject).
- **#84 84c** provider-agnostic (Claude one of OpenAI/Google/DeepSeek/…; inherited from Hermes; **NO N-bump**).
- **No-build / vanilla-JS + stdlib-HTTP architecture** = a genuine data-point + a hireui contrast (heavy Next.js monorepo vs zero-toolchain agent front-end).
- **#66** supply-chain/security — `git clone` + `python3 bootstrap.py` install (no `curl|bash` binary); the surface it exposes (an agent with file r/w + cron + tool-calling to a browser) is the real risk, MITIGATED by optional password/**WebAuthn/OIDC** auth + the localhost + **SSH-tunnel** access model. Benign-to-moderate; **NOT source-cloned** → treat as untrusted-until-inspected.

## Non-claims

NOT #52 (stats page-stated §37.4 + likely inflated) · NOT #57 (a UI for Hermes, not a corpus-subject citation) · NOT #18 B1-MCP (a web front-end, ships no MCP server) · NOT world-first (Open WebUI/LibreChat/lobehub v222 precede) · NOT corpus-first for a mintable class · NOT a §C#27 N=2 (coding-agent + desktop scoped) · NOT the agent itself (Hermes Agent) · NOT a new top-level pattern (max #85) · NOT source-cloned (flagged).

## Reviewable OFF-GOAL alternative

If the operator/audit weights it as *a web front-end for a non-coding personal agent, Claude one of many, the front-end not the substrate* → **(b) FAIL → OFF-GOAL CAPTURE** → `GA:84 · OG:14`, and §35 would then need checking (window {v225 GA, v226 GA, v227 OG} = 1 OG ≤ 1 → still CLEAR). Recorded **GOAL-ALIGNED primary on the merits** (agent-UI infrastructure + Claude-capable + a real architecture study for the operator's own web-app work).

## Tier

**T2 Service** (self-hosted web app / GUI client for an agent — the CodePilot v161 / lobehub v222 / OpenHuman v118 / PilotDeck v175 family), with a T5-application facet.

## Streak

v226 **GA:84** → **`GA:85 · OG:13 [7 ov]`** (cleanly GA on (b) MODERATE+; **8 consecutive GA post the v219 OG break**). **§35 CLEAR** (window {v225 GA, v226 GA, **v227 GA**} = 0 OG).
