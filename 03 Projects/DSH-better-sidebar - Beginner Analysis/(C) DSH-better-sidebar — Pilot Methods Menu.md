# (C) DSH-better-sidebar — Pilot Methods Menu (v237)

**Honest sizing:** this is a **read-and-borrow subject, not an install subject.** It is a UI panel for a rival lab's agent runtime; it adds no agent capability, you don't run DSH, and it wants a native build + a `prepare` script + a release-candidate peer set. So this menu is 14 methods, most of them read/borrow/fence — not a padded 24.

**⭐ One-thing path: A1 → B5 → B6.**

---

## A — Read & learn (zero install, zero risk)

**A1 ⭐ — Read `docs/external-plugin-guide.md` + `AGENTS.md`.**
This is the payload. Roughly 30 minutes. It is the best worked example the corpus holds of *how to expose a stable public API from a plugin*: dogfooded built-ins, capability gates, optional-peer graceful absence, mandatory disposers, type-only imports across bundle boundaries, non-overridable IDs, orphan degradation, declarative settings. You are reading it for the seven design decisions in §5.2 of the Deep Dive, not for the sidebar.

**A2 — Read the boundary rules.**
「禁止修改 DSH 源码」 + mount-only-via-`cordis.patch.yml` + the build-purity gate. Compare against v236's `verify:boundary`. Note that v237's gate is *stronger* — an integration contract test, not a static check.

**A3 — Read the ecosystem, not just the repo.**
The `omdsh-dev` org page (106 repos, governance repo, own hub), `zhu1090093659/dsh-web-ui` (the rival collection), the two "awesome" lists. Fifteen minutes buys you a live picture of how a plugin ecosystem forms around a runtime in two weeks — including the runtime collisions (`aionui-panel` mutual exclusion) and the SEO directory sprawl.

**A4 — Read the disclosed limitations.**
The README's own "what this can't do" list (no file watcher, no git push/pull/fetch, terminal remount on drag, <768 px unusable). A short lesson in #83 honest-deficiency disclosure — the shape you want in your own READMEs.

---

## B — Borrow into your own work (zero install, high ROI)

**B5 ⭐ — Lift the public-API rules into hireui's agent-nativity / extension spec.**
If hireui ever exposes an extension surface (or an MCP tool surface, or a plugin slot for a client), this is the shape:
- namespaced IDs (`vendor:thing`) with **non-overridable built-ins**
- a **`features: string[]` capability list** consumers query, *plus* a version — never version-sniffing alone
- **optional peer dependency** so a consumer that depends on you still loads when you're absent
- **disposers mandatory** — registration returns an unregister function, wrapped in an effect
- **type-only imports** across bundle boundaries; all runtime interaction through method calls
- **your own features use the public API** — no privileged internal path
- **orphan degradation** — persisted references to a missing extension render as labelled placeholders and auto-restore

Composes with the palmier-pro **v192** `ToolExecutor` MCP template and the geti **v213** first-party-skill-suite template. On an `agent-*` branch per hireui's CONSTITUTION (I-2 / I-8 / GitNexus-first).

**B6 ⭐ — Steal the two CI gates.**
1. **Pack → mount into a real host → headless-render → assert no console errors.** `pnpm build && pnpm pack && pnpm test:mount` under Playwright. This is an *integration contract test* for a package, and it is materially stronger than the static boundary checks you took from v236. Generalizes to: *build the artifact you actually publish, install it into a real consumer, and drive it headlessly before you tag.*
2. **npm Trusted Publishing (OIDC) + `--provenance`, no `NPM_TOKEN` secret**, with the tag required to match `package.json`. This is the **publish-side complement to pi v228's consume-side hardening playbook** — together they cover both directions of the supply chain. Apply to anything the vault or hireui publishes.

**B7 — Steal the build-purity gate idea.**
"Client bundles may not value-import from these namespaces; type-only imports are erased and allowed." A cheap, mechanical way to enforce an architectural boundary that code review keeps missing. The vault's analogue: forbid a doc-generation path from importing state directly.

**B8 — Steal the lazy-load budget as a stated number.**
"~325 KB core at startup; terminal / editor / Mermaid load on demand." Publishing a startup budget as a documented contract (rather than a hope) is a small discipline worth copying into hireui's frontend spec.

---

## C — Hands-on, only if you actually want to (low value here)

**C9 — Inspect the tarball without installing.**
`npm view dsh-better-sidebar` and `npm pack dsh-better-sidebar@0.13.0 --dry-run` to see the shipped file list and confirm the `prepare` script and `node-pty` for yourself. Zero execution.

**C10 — ⚠️ Do NOT install it.** Stated plainly so it isn't left ambiguous: a global-ish plugin install into an agent runtime you don't run, against a **release-candidate 17-package peer set**, with a **`prepare` lifecycle script** and a **native `node-pty` compile**, inside a **two-week-old ecosystem** with ≥6 unvetted directories — for a nicer file panel. Not worth it.

**C11 — If you ever do (you shouldn't):** scratch container only · `--ignore-scripts` · pin `0.13.0` and the exact RC peer set · never point the host's default models at anything sensitive (PRC egress on DSH's defaults) · leave `browserNoSandbox` / `htmlViewerNoSandbox` / `htmlViewerDefaultUnsafe` **off** · treat the tree as untrusted (not source-cloned) · **never candidate data.**

---

## D — hireui (Goal #2)

**D12 — It is NOT a hireui component.** hireui is a hand-built recruitment SaaS; this is a panel for someone else's agent runtime. The only thing that crosses over is **B5** (the extension-API rules) and **B6** (the CI gates).

**D13 — Optional: the sandbox-with-visible-unlock model.**
If hireui ever renders untrusted candidate-supplied content (an uploaded HTML CV, a portfolio link), copy the model: **opaque-origin sandboxed iframe + CSP by default, sandbox status shown in the UI, unlock deliberate and temporary.** That is a better default than either "render it" or "don't". Composes with the api-security thread and the RATIFIED candidate-LLM legibility ADR.

---

## E — Off-goal / personal

**E14 — Skip.** There is no personal-use angle unless you start running DeepSeek Harness, which you don't.

---

## F — Vault-meta

**F15 — File the two DEFERRED watch axes for the overdue audit:**
1. v236's axis **generalized** to *"sanctioned in-process UI-layer plugin on a host agent's own extension kernel"* → **N=2** (v236 + v237), recorded not self-promoted.
2. **NEW:** *"plugin-as-platform — a third-party extension that publishes its own capability-gated extension API."*
Plus: the **#57 lateral sub-variant** question (v236 and v237 are unrelated sibling plugins in one host), and the **corpus correction** to v236's "four-day-old ecosystem."

**F16 ⭐ — Point the fourth consecutive gate-shipping subject at the C22–C27 backlog.**
v234 gave you staleness tracking. v235 gave you doc-verification gates. v236 gave you CI boundary gates. v237 gives you *build-the-real-artifact-and-mount-it* gates. Four ships in a row have handed the vault machinery for exactly the invariant it keeps deferring — the stale-row retire pass. At some point the corpus should take its own advice.

---

## Fence (applies to everything above)

Read-and-borrow only · MIT so the *ideas and code* are safe to borrow by hand · do not install · not source-cloned → treat the tree as untrusted · ignore the third-party directory metadata (v236 caught one publishing a wrong licence) · hireui stays hand-built per its CONSTITUTION (I-2 `agent-*` branch / I-8 operator-installs / GitNexus-first).
