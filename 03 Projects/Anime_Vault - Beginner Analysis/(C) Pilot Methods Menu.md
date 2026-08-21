# (C) Pilot Methods Menu — v260 `mranex/Anime_Vault`

## 🔴 Verdict: **READ-AND-RE-DERIVE. Install nothing, run nothing, copy nothing.**

**Why not install:** the documented install path cannot work (`requirements.txt` omits FastAPI, uvicorn and pydantic — Deep Dive §3), and if you fixed that yourself you would be running an unauthenticated local HTTP API with `allow_origins=["*"]` that scans your filesystem and writes to a database, spawned automatically in a background process whose console is suppressed by design. **Not worth it for a media cataloguer.**

**Why not copy:** Apache-2.0 is a genuine, permissive grant — this is the *only* one of the four siblings where copying is legally clean. **The reason to decline is quality and fit, not licence.** There is nothing here hireui needs.

⚠️ And a plain fact for the operator: the README's register makes this repository unsuitable to cite, link or reference in any professional context.

---

## Rung 0 — 15 minutes, read four things in this order

1. **`README.md` §2** — the Mermaid diagram and the paragraph naming `CREATE_NO_WINDOW`. Accurate, and it documents the mechanism that hides the defect in step 4.
2. **`README.md:94-107`** — the three install commands.
3. **`requirements.txt`** — two lines. Now re-read step 2. ⭐ **That gap, held in your head for ten seconds, is the whole ship.**
4. **`movie_vault/server.py:14`** — the comment `# Import existing core modules`, and then `:35` (`from movie_vault.core.randomizer import pick_random_item`) beside `movie_vault/ui/random_page.py:37` (the same import). **One function, two UIs, called not copied.**

---

## ⭐⭐⭐ Rung 1 — 90 minutes, the only thing worth taking: settle the `05 Skills/` decision

The v259 audit left this open and this ship is the argument for closing it. v258 established that **code moves forward and never backward** — a fix in the newest copy does not reach the older ones, because copy-forward is a one-way ratchet. `05 Skills/` has exactly that shape: skills copied and re-versioned, and the routine as `llm-wiki-routine-v2.3 … v2.8` in eight separate files.

**This repository is the same author doing it right, and the mechanism is visible in one comment and one shared import.** Do the same:

1. **Name the single owner of each fact.** One file owns the Phase 0.9 criteria. One owns the streak notation. One owns the method rules D31–D48. Today §43's rules exist in `v2.8`, and the earlier deltas each restate their own era's rules — which is the ratchet.
2. **Make the deltas reference, not restate.** A v2.9 delta should say *"§43 as owned by v2.8, plus D48"* — not carry its own copy of D31–D47. That is `server.py:14`'s move: import the existing core.
3. ⭐ **Where you genuinely cannot share, apply D32 instead** — declare which copy wins, inside the copy that loses. v245 proved this works: its `BUDGET.md` went stale and the staleness was harmless *and self-diagnosing* because the file said which document beat it.
4. ⭐ **Then add the check, because this subject proves you will not maintain the invariant by hand.** One clause in `bin/verify-vault-inventory.sh`: **every routine-delta file's stated CURRENT version must match the version named in `CLAUDE.md`'s authoritative state line, and no delta file may restate a rule owned by a later one.** Four lines of `grep`, and it catches the exact class of defect this repository shipped.

**Cost:** 90 minutes. **Installs nothing. Copies nothing.** It closes an open v259 decision using an argument the corpus now has four data points for.

---

## ⭐ Rung 2 — 20 minutes, one CI clause for hireui

The defect in §3 is a **manifest–documentation divergence**, and it is one of the cheapest possible checks:

> *Every third-party module imported by the application's entry points must appear in the dependency manifest the README tells you to install.*

In hireui that is `grep`-able against `package.json` and takes one CI step. **This subject had bounded, well-formed pins for the wrong program and no CI to notice** — the best-formed manifest of the four siblings, describing an application its own README calls antiquated.

⭐ **And the transferable framing, which is the more useful half:** `spawn()` tells you a process **started**, not that it is **running**. Anywhere hireui launches a subprocess, a worker or a container and logs success on the strength of the launch, that log line is a **false success** — v251's class, now at N=2 in the corpus. Log success from a **readiness probe**, never from a spawn.

---

## Rung 3 — DECLINED

There is no third rung. The two biased shuffles (`Library.tsx:144`, `RandomPicker.tsx:144`) are worth knowing as a code-review reflex — `sort(() => Math.random() - 0.5)` is not a uniform shuffle and Fisher–Yates is four lines — but that is a fact you already have, not a pilot.

---

## 🔴 NEVER

- **Never** run `npm run tauri dev` or `python app.py` from this repository.
- **Never** fix the manifest and run it anyway — that gets you an unauthenticated wildcard-CORS local API over your filesystem.
- **Never** cite the architecture diagram as evidence the app works. It is accurate about the design and silent about the dependency gap.
- **Never** trust *"Successfully launched Python API server"* — it is printed on a `spawn()` result, not on a live server.
- **Never** copy either shuffle idiom.
- **Never** treat this repository's clean bookkeeping as evidence of discipline. It is a bulk import; the habits that were absent had nowhere to accumulate (Deep Dive §6).
