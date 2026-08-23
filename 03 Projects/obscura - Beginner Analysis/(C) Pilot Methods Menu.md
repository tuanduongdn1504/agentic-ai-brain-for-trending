# (C) Obscura — Pilot Methods Menu

**v267** · Apache-2.0 · **Verdict: ⭐ READ-AND-BORROW, AND THIS ONE IS ACTUALLY PILOTABLE**

Obscura is the **first subject in its class you could put in a product.** Its nearest peer, Lightpanda, is AGPL-3.0; firecrawl v214's core is AGPL; OpenMontage v188 is AGPL; PilotDeck v175 is AGPL. The vault has repeatedly recorded that AGPL blocks hireui. **Obscura is Apache-2.0.** That, plus a ~30 MB footprint, is the on-goal prize.

---

## Rung 0 — Read the six places that carry the ship (20 min, zero risk)

Read in this order; each one is short and each one is the evidence for a finding.

1. **`ci.yml:52-63`** — the trusted-base pattern. Policy script and `deny.toml` fetched from the base revision so a PR cannot weaken its own gate. *This is the single most transferable idea in the repository.*
2. **`ci.yml:86`** beside **`ci.yml:143-145`** — the docs exemption next to the cache-poisoning defence. The whole ship in two hunks: an excellent gate and the surface it excuses.
3. **`scripts/ci/compare_obstacle.py:91-97`** beside **`:112-113`** — `candidate_passed` computed, rendered into a table, and never compared to the `33` that `AGENTS.md:52` and `:69` both call mandatory.
4. **`README.md:34-35`** beside **`README.md:361-363`** and **`AGENTS.md:98`** — "Anti-detect: Built-in" and four speed figures, no two the same.
5. **`crates/obscura-mcp/src/http.rs:141-146`** — the comment that names the attack its own default permits. **v265's rule, in someone else's repository.**
6. **`README.md:403`** — `| **LP** | getMarkdown |`. Then `grep -ri lightpanda .` and get nothing.

---

## ⭐⭐⭐ Rung 1 — Turn the finding on the vault (30 min, highest ROI)

**This is the recommended action and it is not about Obscura.**

Obscura exempts every `*.md` from CI, and that exemption is where its claim drift lives. **This vault is entirely `*.md`.** `CLAUDE.md` hand-maintains: 46 top-level patterns · 12 CONFIRMED Library-vocab · §C-1 = 12 · §C-2 = 39 · a `GA:124 · OG:13 [7 ov]` streak · "47 consecutive GA v220→v267". Nothing checks any of it. The v259 audit *did* find a count wrong — twice — and fixed it by hand.

Do this:
1. Derive the §C counts mechanically from the `C##` markers v259 added: `grep -c` per section, assert `§C-1 + §C-2 == live total`.
2. Derive the streak from the per-ship `GA`/`OG` tags in `_state/03c`, and assert it matches the shim.
3. Assert the "consecutive GA" run length matches the ship range it names.
4. **Wire it into `(C) proposed-verify-vault-inventory.sh`** — the nine-clause script **v263 found nothing invokes** — and give that script a git hook.

⭐ **Three consecutive ships have handed the vault this same lesson from three directions:** v263 (a nine-clause script nothing runs), v266 (a next-action sentence copied forward while the fact moved — measured: `main` is at v226, not v204), v267 (the one surface with no gate is the one carrying the claims). It is time to stop recording it.

---

## ⭐⭐ Rung 2 — Steal the trusted-base pattern for hireui (45 min)

hireui's CONSTITUTION restricts skills to the operator and uses `agent-*` branches. If any hireui CI job reads its policy, lint config, or allowlist **from the PR's own checkout**, an agent-authored branch can weaken the check judging it.

Port `ci.yml:52-63` verbatim in concept:

```bash
git show "$BASE_SHA:.github/policy.py" > "$RUNNER_TEMP/policy.py"
git show "$BASE_SHA:deny.toml"         > "$RUNNER_TEMP/deny.toml"
```

Then add the two companions: `save-if: false` on caches, and **disable rename detection** in any path-based change classifier (`ci.yml:92-94`) so code cannot enter through a docs-shaped path. Compose with the **BOLA audit** already flagged as hireui's #1 risk.

---

## ⭐⭐ Rung 3 — The gate-aim audit, generalised (30 min)

Obscura's failure is not a bad gate; it is a gate **aimed one degree off** the rule its documentation states. v250 established that *a gate's aim, not its quality, decides what rots.*

Run this over hireui and the vault: **for every threshold stated in prose, find the code that enforces it and check the comparison is the same one.** Specifically hunt the shape found here:

```python
passed = sum(...)          # computed
print(f"{passed}/{total}") # displayed
if regressions: fail()     # a DIFFERENT question
```

⇒ **A value that is computed and displayed but never compared is a gate-shaped hole.** `grep` for counters that reach a `print`/log and never reach an `if`. This composes with v246's one-command idea (`grep -rni "silent" .`).

---

## ⭐⭐ Rung 4 — Actually pilot it, fenced (60–90 min)

The first genuinely pilotable subject in this class. **Do not install from a script; use a release binary or Docker.**

**Safest first contact — Docker, loopback, no MCP:**
```bash
docker run --rm -p 127.0.0.1:9222:9222 h4ckf0r0day/obscura
```
Then point Puppeteer at `ws://127.0.0.1:9222/devtools/browser` against **your own** page and compare a `--dump markdown` extraction to your current pipeline.

**Fence, and these are not optional:**
- 🔴 **Do not enable the MCP server against anything sensitive.** 37 tools, **zero approval gate, no read-only mode, no URL allowlist** — including `browser_evaluate` (arbitrary JS), `browser_get_cookies` and `browser_storage_state`.
- 🔴 **If you run `obscura mcp --http`, set `OBSCURA_MCP_ALLOWED_ORIGINS`.** Unset, CORS is `*` and any web page you visit can drive the loopback MCP port — the attack the code's own comment describes (`http.rs:141-146`).
- ⚠️ **`--obey-robots` is OFF by default** (`crates/obscura-browser/src/context.rs:131`). Turn it on for anything resembling third-party scraping.
- ⚠️ **Never point it at candidate data or a logged-in session.** It is a browser with cookie and storage-state tools and no consent model — the same fence the vault put on voicebox v229 and worldmonitor v230.
- ⚠️ **Treat the 30 MB / 85 ms / ~12× numbers as unverified.** Measure your own workload; the suite is in a separate repo this analysis did not clone.
- ⚠️ The Docker image runs as **root** (no `USER`, and `distroless/cc-debian12` is not the `:nonroot` variant), and base tags float. Pin a digest if you keep it.

---

## Rung 5 — The comparison this ship could not make (~v268)

Wiki **Lightpanda** (`lightpanda-io/browser`). It is the AGPL incumbent of the class minted at v267, it is goal-relevant on the same axis (CDP + native MCP + agent-oriented extraction), and it is the one comparison unavailable from inside Obscura's repository — because Obscura never names it.

The specific question worth answering: **is the Apache-2.0 licence the whole of Obscura's advantage, or is the Rust engine genuinely better?** That decides whether hireui should use Obscura or wait.

---

## 🔴 Never

- Cite **85 ms**, **~12×**, **30 MB**, **"10,000 stars"**, or **"~57 MB compressed"** as established. All are page-stated or externally-sourced; none is verifiable from the repository.
- Read **"Anti-detect: Built-in"** as meaning you have anti-detect. It needs `--features render,stealth` **and** `--stealth`; `crates/obscura-cli/Cargo.toml:17` is `default = []`.
- Read a green CI run as meaning the obstacle course scored **33/33**. It means no stage regressed against base.
- Assume the stealth mode defeats a real detection service. There is **no in-tree test against one**.
- Run the MCP server with default CORS on a machine where you browse the web.
- Expect a bare `cargo build` to give you screenshots or stealth — both are off by default.
- Assume `vendor/taffy` or `vendor/cosmic-text` match upstream. **37 files are patched**; the reasons are in `Cargo.toml:59-64`, not in the files.
- Trust `git log` for counts in *any* repository after this one. Use `git rev-list`.
