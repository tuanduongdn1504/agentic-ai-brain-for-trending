# (C) Pilot Methods Menu — `google/artemis` (v285)

**Verdict: ⭐⭐ READ-AND-BORROW.** Nothing here should be installed against a real device or real data. Five mechanisms are worth lifting, and two of them fix things in this vault.

**Install footprint if you ever did:** `uv sync` + ADB + FFmpeg + scrcpy, a helper **APK installed on the phone** (`ARTEMIS_HELPER_AUTO_INSTALL=true` by default), `start.sh` may request `sudo`, and every screenshot goes to whichever model provider you configure. **Do not point it at a phone with real accounts.**

---

## ⭐⭐⭐ Rung 1 — Port `check_dependency_sources.py`'s *shape* (45 min, zero risk)

The best single artifact in the repository, and the exact gate **v271** lacked when 206 lockfile URLs silently resolved to `registry.npmmirror.com`.

Three ideas, each independently worth having:

1. **Walk the lockfile; never trust a summary.** It iterates every package and every artifact URL rather than checking a config line.
2. **Assert the scheme, not just the host.** `if parsed.scheme != "https" or parsed.netloc != host` — which is why it catches the plaintext-HTTP internal mirror, not only the wrong domain.
3. **Run it BEFORE the install.** It is stdlib-only *specifically* so it can be CI's first step, ahead of `uv sync`. A supply-chain check that runs after you have installed is theatre.

**Apply to the vault:** we have no dependency-source gate at all. The direct analogue for `(C) proposed-verify-vault-inventory.sh` is idea 3 — **our clause-(h) derivation runs after the fact.**

---

## ⭐⭐⭐ Rung 2 — The anti-self-deception clauses into `hireui/evals/METHOD.md` (30 min, zero risk)

The operator prompt is a genuinely superior piece of prompt engineering about **not lying to yourself**, and it transfers wholesale to any eval or agent harness:

- *"Never write an action's expected outcome as if it had already been observed."*
- *"…so never declare a check passed or record a conclusion on its behalf."*
- *"Take no extra actions for `assert:` lines and **never construct state to satisfy one**."*
- *"Nothing is inferred on your behalf: it is recorded as your own statement."* — and self-described targets are **marked as self-described** in the record.
- A coordinate target must carry a human-meaningful `target_description`, *"never a generic 'element' or 'button'."*

⭐ The third is the best anti-gaming clause in the corpus and belongs in every rubric we write. The fifth is the same idea as the vault's own provenance discipline: **label the claim with who made it.**

⚠️ **And take the negative lesson with it:** these 25 KB contain **zero** words about passwords, payments, privacy or personal data. A prompt can be rigorous about epistemics and completely silent about harm. **Check both axes when we write ours.**

---

## ⭐⭐ Rung 3 — The three-list audit, on ourselves (30 min, zero risk)

v284 gave us *"every list DERIVED from the tree is correct; every list a person TYPED is correct only where omitting an entry breaks something loudly."* Artemis gives the **scope** variant:

- `quality_ratchet.py` covers **319 of 590** `.py` files. Its headline metric `silent_broad_exception_handlers: 0` is **exactly true in scope** and reads as a repository-wide property.
- `pyright-core.json` covers **~14 of 590 (2.4%)**. ⭐ CI names this honestly — *"Type-check protected core modules"* — while `make typecheck`'s help text says *"Run type checking."* **Same gate, two descriptions, one honest.**

**Ask of our own gates:** for each, what is its *declared* scope, what is its *actual* scope, and does any summary of it read as broader than it is? Start with `(C) proposed-verify-vault-inventory.sh`.

---

## ⭐⭐⭐ Rung 4 — Per-file provenance headers (15 min, zero risk) — **promoted; the evidence is now a controlled experiment**

Twenty-one byte-identical headers, inside the derived files:

```
# Portions of this file are derived from mobile-use (https://github.com/minitap-ai/mobile-use)
# Copyright 2025-2026 Minitap, Inc. Licensed under the Apache License 2.0.
```

⭐⭐⭐⭐⭐ **This repository ran the experiment for us, by accident.** A `NOTICE` file credited **two** upstream projects — `mobile-use` and `finalrun-agent` — and **eight** named individuals. It was bundled into a commit that also did a breaking rename; a different maintainer reverted the whole commit **3 h 12 m later**, deleting the `NOTICE`; and per-file headers were then added for **one** upstream only. At HEAD:

| | Hits | Files |
|---|---|---|
| Credited **inside the files** (mobile-use) | **44** | **23** |
| Credited **only in the central file** (finalrun-agent) | **0** | **0** |
| The **eight named individuals** | **0** | **0** |

**Same words, two locations, two fates.** ⇒ **v283's rule, positive half, with a control.** Contrast v181 (uncredited GitNexus), v267 (unnamed Lightpanda), v265 and v284 (credited, no NOTICE).

**Apply:** the vault's `05 Skills/` holds copied-and-re-versioned skills — the standing copy-forward problem the **v259** audit flagged, and the routine exists as v2.1→v2.8 as separate files. **A per-file provenance header inside each copy is the cheap first step**, and it is the same fix as **v243**'s symlink where a symlink will not do. ⚠️ **And take the negative lesson:** a single central index that records where everything came from is exactly the artifact that disappears when someone reverts a commit about something else — which is what `MEMORY.md` and the `03c` index row are.

---

## ⭐ Rung 5 — Two design ideas worth stealing outright

1. **The task-not-action MCP interface.** Five tools, and `mobile_run_task` takes a *goal*, not a tap. For hireui's eventual MCP surface this is the right default — **but note the cost Artemis pays: there is no approval checkpoint anywhere, because there is no per-action boundary to hang one on.** If we take the shape, we must add the gate Artemis lacks.
2. **`mobile_run_task`'s docstring.** It discloses its own missing safety net *in the text the agent reads* (*"no pre-execution safety net"*), gives honest latency, and ends by telling the caller to stop using it: *"run once to discover the path, then author a deterministic script instead."* That is **v271's *name where to go INSTEAD*, at N=2**, and the disclosure-in-frontmatter pattern from **v276**.

---

## 🔴 NEVERs

1. **Never cite the 99%+ AndroidWorld figure.** No harness, no dependency, no methodology; the evidence image lost its date and source.
2. **Never point it at a phone with real accounts.** No untrusted-content boundary; `--- User Guidance ---` is a documented escalation token; `open_link` reaches an unescaped `adb shell`.
3. **Never rely on `locked_app_package`.** Its accessor has zero call sites.
4. **Never deploy `playground/backend_manager/` as shipped** — published JWT key, `123456` OTP bypass, Docker socket mounted into a root container, and `APP_ENV` never read by a conditional.
5. **Never assume its tests ran.** They do not run on push or PR.
6. **Never wire it to candidate data.** A screenshot pipeline over a phone is the worst possible surface for PII.
7. **Never repeat the "228 of 229 files were exactly the same" figure.** Measured from both trees: **74** shared paths after normalising the `minitap/mobile_use/` → `artemis/` rename, **2** byte-identical. 229 is simply artemis's own file count.
8. **Never say "Google restored attribution" unqualified** — a second upstream (`finalrun-agent`) and all eight named individuals are credited **nowhere** at HEAD.

---

## Not attempted

Nothing was installed, built, or executed — **zero spend, zero footprint.** Therefore: *"2,063 tests pass"* is **UNVERIFIED**; only that they exist and that CI does not invoke them on push or PR is established. The live device behaviour, the helper APK, the Angular console and the minified bundle `artemis/resources/showcase_ui/main-BGAFACUZ.js` were not exercised. Whether 99.1% is **true** cannot be settled from this tree in either direction — only that **nothing in the repository can produce or check it**.
