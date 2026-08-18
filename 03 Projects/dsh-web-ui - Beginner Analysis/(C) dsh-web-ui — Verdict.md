# (C) dsh-web-ui — Verdict

**Wiki v239 · 2026-08-18 · `zhu1090093659/dsh-web-ui`**

---

## 1. Phase 0.9 criteria — GOAL-ALIGNED INCLUDE 3/4

| # | Criterion | Call | Reasoning |
|---|---|---|---|
| **(a)** | Author is Anthropic / a registered vendor-direct source | **FAIL** | `zhu1090093659` ("Solitude") — no bio, company, location, or declared affiliation; commits under a QQ-mail address; npm under `@linxin666` / `linxin@linux.do`. **Routine §41** admits no name / heritage / locale / notability inference and answers the disclosed-individual axis NO. Building DeepSeek tooling is not an affiliation with DeepSeek. Pattern #19 19a. |
| **(b)** | Goal relevance | **MODERATE — keys the tier ⚠️ STRONG genuinely arguable** | The interaction surface of an autonomous **coding-agent** runtime = the Goal-#1 harness substrate (CodePilot v161 / hermes-webui v227 / dsh-TUI v236 / DSH-better-sidebar v237 family), plus a governance artefact (§9 of the Deep Dive) that lands squarely on Goal #1, plus doc-integrity machinery that lands on the vault's own maintenance problem. **Held at MODERATE for consistency with the v236→v238 DSH run** — a rival lab's rc-stage host, Claude present only as an example string in a PR template, nothing here a hireui component. ⚠️ **But this ship is the strongest (b) of the four**: unlike v236/v237 it is not presentation-only — it registers **real agent tools** (`ssh_*`, `describe_image`), a **host-side scheduler with fail-closed permission**, and an agent preset. STRONG is defensible; **flagged reviewable, operator's call.** Cleanly GA via §31 either way; §40 available as a backstop but **not needed**. |
| **(c)** | Substance / engineering quality | **STRONG** | 13 packages; 32 scripts; 8 CI workflows; 10 CI check steps + a job that **packs, mounts into a real DSH instance, and headless-renders under Playwright**; a doc-integrity gate using **git blob hashes** for translation pairing; a runtime-deps gate born from a real boot crash (#70); a 7-field `skin.json` contract hard-failed by the build; **exact-pinned** aggregate deps; pnpm **`allowBuilds` lifecycle allowlist + `minimumReleaseAgeExclude`** (the pi v228 playbook); one-time 16-byte pairing tokens with 10-minute expiry; **fail-closed scheduling**; `permissions: contents: read`, no publish job, no secrets. **Caveats foregrounded:** v0.2.0 on a ~6-day-old repo against a moving rc.7 target; plaintext SSH credentials with no approval gate; three inconsistent plugin counts and a stale root version; a tagline advertising a non-existent feature; a disputed benchmark carried into the npm registry; **NOT source-cloned**; stars page-stated. |
| **(d)** | Corpus fit / cross-reference density | **STRONG** | Four-way #57 (v235 host / v237 npm dep / v238 vendored code / v216 cited model) + lateral v236; instance-strengthening on three watch axes; a direct best-practice contrast with **v212 tabularis**; the fifth consecutive ship in the invariant-machinery theme (v234→v235→v236→v237→v239); the fourth in the fail-mode theme (v233/v234/v238); observability sub-flavor (b); Patterns #57 / #66 / #68 / #81 / #83 / #88 / #19. |

**Tier:** **T4 Plugin/Extension** — *multi-plugin suite* flavour (the `opencode-antigravity-auth` v67 / v237 bridge-plugin tier), with a **T2-client** facet (the mobile remote) and a **T1 preset/methodology** facet (`dsh-liangshen`). Tier reviewable.

**Streak:** v238 `GA:96` → **`GA:97 · OG:13 [7 ov]`** — **20 consecutive GA ships.**
**§35:** **CLEAR** — rolling 3-ship window {v237 GA, v238 GA, **v239 GA**} = **0 OG**.
**Overrides:** none consumed. Lifetime 10 (3 logged `[ceiling-override]`: v146/v148/v152); v153→v239 = **zero**.

---

## 2. Pattern outcome — **NO MINT**

**Counts 46 confirmed top-level / 11 CONFIRMED Library-vocab — UNCHANGED.**
**§C live standalones 49 — unchanged. Tracked surface ≈56 — unchanged.**

This is the **sixth consecutive NO-MINT in the DSH chain** (v235 → v236 → v237 → v238 → v239). Recorded explicitly so the audit does not read reflexive declines: the grounds differ each time. v236/v237 = presentation-not-capability. v238 = not-world-first + rationale-not-mechanism. **v239 = canonical-form-factor + component-not-subject.**

### 2.1 PRIMARY — instance-strengthening (recorded, **NOT** self-promoted)

A promotion is an audit act (the v232 / v235 / v237 rule). All of the following are **recorded and flagged**, not executed.

| Axis | Origin | New N | Note |
|---|---|---|---|
| *"Sanctioned in-process **UI-layer plugin** on a host agent's own extension kernel"* | v236, generalised at v237 | **N=2 → N=3** (v236 + v237 + v239) | **PROMOTION-ELIGIBLE.** v239 is the broadest instance: 13 plugins across four extension-point kinds (client-UI panels, skins, a tool, an agent preset) on the host's **primary** surface, plus it **consumes v237's plugin as an exact-pinned dependency.** |
| *"Harness-level inference-time trajectory conditioning"* | v238 | **N=1 → N=2** via `dsh-liangshen` | ⚠️ But an **openly-credited derivative with vendored MIT code** = the **OmniRoute v208 PORT situation** → promotion **deferred pending a non-derivative third instance**. ⚠️ **AND the corpus already held a third data-point it never connected: v236's entry records `presets/liangshen/` + `verify:minimal-preset-tools` + `verify:liangshen-bootstrap`** — the class is crowded *inside the corpus's own subjects*, which **strengthens v238's NO-MINT ground (5)** rather than weakening it. |
| *"Cosmetic customisation of AI-coding-tool clients"* | v216 | **N=1 → N=2** | But via a **sanctioned plugin path** (the host's official `turtle-ui`-style setup) rather than v216's **unsanctioned CDP injection** — a sub-flavour distinction, and v239 **openly cites v216's subject as its model**. |
| Observability sub-archetype, sub-flavour **(b) ambient/affective** | v154 agentpet + v155 + v156 + v164 + v166 = N=5 | **6th instance** | The whale pet — and the **first mounted in-process inside the host's own UI** rather than as a separate desktop app. N-tally is audit bookkeeping; **recorded, not self-incremented** (the v205 precedent). |
| Pattern **#68 Awesome-List Genre** | — | new form-factor sub-variant | `dsh-client-ui-community-plugins` is **an awesome-list compiled into a host-app panel**: a static `community.json` → build-time bundle, **index-only**, no runtime registry, manual install commands. Instance-strengthening (the v201 / v218 handling). |
| Patterns **#83** (self-disclosed plaintext-credential defect, both languages) · **#81** (three plugin counts, stale root version, phantom tagline feature) · **#66** (two-sided) · **#88** (the CI emoji ban as an AI-tell suppressor) · **#19 19a** · **#57** (widest fan-in) | — | instance-strengthening | See the Deep Dive. |

### 2.2 §C-mint alternative **A** — RECORDED + **DECLINED**

> *"Aggregate Multi-Plugin + Skin Suite for a Host Agent's Official GUI — one meta-row installing many individually-installable plugins, plus an in-app theme marketplace and a hosted gallery."*

**Declined on four grounds:**
1. **Emphatically NOT world-first — the form factor is canonical and decades old.** VS Code extension packs + the theme marketplace; **Obsidian's ~6,730 community plugins + ~698 themes**; Home Assistant HACS; Grafana's plugin catalog; JupyterLab extensions; Eclipse before all of them. "Plugin + theme pack for an extensible host application" is one of the most established patterns in modern software.
2. **Packaging, not capability.** §C vocabulary is agent-capability-shaped; an aggregate meta-package is a distribution decision (the PixelRAG v211 / meetily v196 domain-and-form-not-capability discipline).
3. **§28 draw-the-circle** anti-inflation, at 49 live standalones.
4. **The precedent chain now runs six deep** — Codex-Dream-Skin v216 → lobehub v222 → hermes-webui v227 → dsh-TUI v236 → DSH-better-sidebar v237 → v239.

### 2.3 §C-mint alternative **B** — RECORDED + **DECLINED** (the closer call)

> *"Agent-First Multi-Host SSH / Infrastructure-Operations Capability Layer — remote shell, file transfer, tunnelling and fleet-wide execution exposed to the agent as first-class tools."*

**Genuinely corpus-first by grep.** `SFTP` · `port forward` · `port-forward` · `cluster execution` · `bastion` · `ttyd` · `Guacamole` · `Cockpit` · `Portainer` · `Termius` = **all 0** across `_state/03c` + `_patterns/06`. The corpus's 12 `SSH` hits are **all** SSH-as-*transport-to-reach-an-agent* (ping-island v160's tunnel forwarding, herdr's disconnect survival, tabularis v212's DB tunnels, hermes-webui v227's access model, PilotDeck v175's SSH workspace) — **never SSH as a capability the agent itself wields.** Hand-checked distinct from **devspace v171** (remote chat host → *local* machine), **Agent-Reach v174** (web/social *read*), **serve-sim v183** (simulator), **OfficeCLI v206** (documents), **tabularis v212** (databases).

**Declined on four grounds:**
1. **NOT world-first.** Agent SSH tools are precedented (`badseal/ssh-skill`, an OpenHands SSH skill, `ai_ssh_skill`), and browser-based SSH consoles are a mature genre (WebSSH, ttyd, Wetty, Guacamole, Cockpit, ShellNGN). ⚠️ These precedents are **reported by the research pass and not independently re-verified by me**; the *canonical* half of the argument (browser SSH consoles are mature) is not in doubt.
2. **Component, not subject.** `dsh-ssh` is one package inside a 13-package suite. Minting here draws the circle around a component (§28; the camofox v179 don't-draw-the-circle discipline).
3. **It is the weakest-engineered part of the subject** — no allowlist, no approval gate, no audit log, no redaction, plaintext secrets. Minting vocabulary off a project's worst code encodes a liability as a class.
4. **§28** anti-inflation.

→ Recorded as a **DEFERRED watch axis:** *"agent-wielded multi-host infrastructure-operations capability layer (SSH / SFTP / tunnel / fleet-exec)."* **Flagged to the audit with emphasis** — this is the corpus's **first instance of an agent being handed production-fleet reach**, and the class deserves a considered ruling before a second instance arrives. **NOT executed.**

### 2.4 Also considered and rejected without a mint

- **A third-party-built in-app extension marketplace.** Both the skin centre and the community-plugin panel are **static, build-time, index-only** surfaces with no runtime registry and no automated install — an awesome-list in a panel (§2.1), not a marketplace. Kilo Code v177 ships a real MCP marketplace but *is* the agent product.
- **Multi-Vendor Coding-Agent Orchestration Platform (Paseo v150 + ai-maestro v163, N=2, promotion-eligible at N=3).** Row read **verbatim** before ruling: it requires *"heterogeneous third-party coding agents … as the orchestration UNITS."* This task board is **single-host, DSH-only**. **NOT a third instance** — the tempting near-miss of this ship, and the reason the row was read rather than skimmed.

---

## 3. Audit items this ship generates

1. **The v237 axis is at N=3 → promotion-eligible.** Decide: promote *"sanctioned in-process UI-layer plugin on a host agent's own extension kernel"* to a §C standalone, or hold.
2. **The v238 axis is at N=2-as-derivative**, plus the **un-connected v236 `presets/liangshen/` evidence**. Decide whether v236 counts as a third data-point (which would move the axis without a non-derivative instance).
3. **The new SSH-fleet-reach watch axis** (§2.3) — rule before a second instance lands.
4. **Still open from v238:** the **v140 §C row** (*graduated / least-privilege tool exposure*) is ~99 wikis stale at N=1, past both §28.3/§39 floors → retire or generalise.
5. **Still open:** the **v192 product-first-MCP row at non-port N=4** (tabularis v212 / voicebox v229 / worldmonitor v230) — promotion trigger doubly reinforced and still unexecuted.
6. **The ~v221 audit is now egregiously overdue** — last audit v212; v213–v239 have all shipped.
7. **A possible new #83 sub-mechanism** across v238→v239: *provenance correction upstream, un-propagated downstream* — the corpus has now captured both ends of one claim's lifecycle.

---

## 4. Verification record

✅ **Verdict produced INLINE and fully hand-verified**, per `feedback_wiki_verify_independently_check_collisions`.

**Research fan-out:** one `Workflow` run — 12 research lenses + 3 adversarial verifiers, **16 agents, 0 errors, ~1.73M subagent tokens, 352 tool uses, 411s**. ⭐ **This is the clean fresh-session confirmation the v238 ship asked for: the `Workflow` tool, which failed at v238 with all 18 agents *prompt-too-long* at ~207.2K against a 200K limit, now works — the v238 shim compaction (537,679 → ~132KB) was the fix.** Tested in a fresh session, so uncontaminated by the v167 session-start-snapshot trap.

**Hand-verified independently of the agents** (own fetches): the repo page and tagline · `README.md` / `README.en.md` / `packages/dsh-liangshen/README.zh.md` · root `package.json` · `.github/pull_request_template.md` · `.github/workflows/ci.yml` · the npm registry entries for `dsh-web-ui-all`, `dsh-liangshen`, `dsh-ssh`, `dsh-remote-web-ui`, `dsh-client-ui-community-plugins`, `dsh-skins`, and `cloudflared` · `deepseek-harness/releases` · **`xiaobright/dsh-anchored-standard` issue #60** · the author profile.

**Collision check — sanity-anchored hand-grep, CLEAN.** All 13 anchors hit (`deepseek-harness` 24 · `dsh-TUI` 20 · `better-sidebar` 12 · `Cordis` 30 · `anchored-standard` 8 · `Codex-Dream-Skin` 14 · `agentpet` 20 · `Paseo` 35 · `ai-maestro` 22 · `devspace` 46 · `Agent-Reach` 61 · `AionUi` 11) → grep works. Subject terms **0** (`linxin666` · `dsh-skins` · `skin center` · `skin-center` · `dsh-pet` · `dsh-ssh` · `task-board` · `全家桶` · `dsh-market` · `deepseek-pp` · `whitelonng` · `DreamSkin` · `gallery.dsh` · `dsh-liangshen` · `describe_image` · `turtle-ui`), with two expected non-zero: `dsh-web-ui` 3 and `zhu1090093659` 3 (**all inside v237's own entry**, discussing `aionui-panel`) and `dsh-routing-suite` 3 (inside v238's crowded-class argument). The **v140 / v237 / v216 / orchestration-platform** rows were read **verbatim** before ruling.

### Six errors caught

1. ⚠️ **The GitHub API.** Agents used `api.github.com` extensively; **§37.4 says this environment mocks it.** The **1,477-file** and **66-contributor** figures rest on the API alone → **discarded.** Replaced with the hand-verified 70-handle `README.en.md` block. (Several API figures *did* corroborate independently-verified page/registry facts — 4,419 ≈ "4.4k"; repo creation ~08-12 vs first npm publish 08-13 — so they are reported as page-stated-and-corroborated, never as API-verified.)
2. **My own early package count.** I first recorded **8 packages** from the README; the registry shows **13 `@linxin666` packages + `dsh-better-sidebar`**. Corrected in-session — and the discrepancy turned out to *be* a finding (§6 of the Deep Dive).
3. **A near-miss mint.** The task board's surface similarity made "N=3 of the Multi-Vendor Orchestration-Platform row" tempting until the row was read verbatim: it requires *heterogeneous third-party agents as the units*. Single-vendor → not an instance.
4. **An overstated risk of my own.** I initially framed the compound danger as *"unattended cron + `ssh_exec`"*; the source shows the scheduler **queues** (`mode:'queue'`) into the normal interaction flow and is **fail-closed on permission**. The SSH risk is real; the *unattended* framing was wrong and is corrected.
5. **An agent's characterisation of `prepare` as an install-time risk.** `prepare` runs for the publisher and on git installs, **not** for a registry consumer — the real transitive install-time actor is **`cloudflared`'s `postinstall`**, verified directly in its own manifest.
6. **A tempting identity inference declined.** The contributor list contains a handle `Chimney`; v236's author is `ccch1mneyyy` ("Chimney"). **Left UNVERIFIED** rather than asserted — §41 discipline applies to people, not just to criterion (a).

**Doc defects found by hand in the subject:** three inconsistent plugin counts (11 stated / 12 listed / 14 shipped) · root `version: 0.1.1` vs shipped `0.2.0` · a GitHub tagline advertising **"live token stats"** absent from `README.en.md` and from every published package · a PR template listing 2 affected-package checkboxes for a 13-package monorepo · **a benchmark pair carried into the npm registry description two days after its upstream attribution was publicly corrected.**

`inflation_check` **HELD** — 0 mints, counts unchanged, three watch axes strengthened but none promoted.

---

## 5. Blunt summary

Seventy people spent six days building a 13-package plugin suite for DeepSeek's web UI, and along the way built better process machinery than most funded projects: a **required AI-authorship field** in the PR template (naming Claude Code among four expected agent tools), a doc linter that **hashes translations so they cannot silently drift**, a CI job that **mounts the plugin into a real host and renders it headless**, a **lifecycle allowlist**, one-time pairing tokens with a ten-minute expiry.

Then they shipped an SSH plugin that hands the model **`ssh_exec` and `ssh_cluster` with no approval gate, no allowlist, no audit log**, and keeps your passwords in a **plaintext JSON file** — and said so plainly in the README. The corpus's own **v212 tabularis** solved that exact secret class with the OS keychain one ship earlier.

And the pattern underneath is the lesson: **everything the build can check is checked; everything only a human can check has already drifted.** Three different plugin counts, a stale root version, a tagline advertising a feature that does not exist, and a benchmark number whose upstream retracted its attribution two days after this project copied it — still sitting in the npm registry today. **That last one is a mirror, not a gotcha.** Take the doc linter and the disclosure field. Leave the SSH plugin, and the number.
