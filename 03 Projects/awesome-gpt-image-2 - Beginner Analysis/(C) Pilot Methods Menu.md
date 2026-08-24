# (C) Pilot Methods Menu — v272 `awesome-gpt-image-2`

**Verdict: ⭐ READ-AND-BORROW. Do not treat the catalogue as licensed content. The agent skill is installable at low risk if you install it deliberately.**

---

## Why not a full pilot

The code is clean but it is *someone else's SaaS*: 33 Vercel handlers wired to his Supabase project, his Stripe account, his Alipay merchant id and his Ciyuan API key. There is nothing to adopt wholesale. The value is in five specific mechanisms and one rule about ourselves.

**And one hard fence:** `README.md:528` grants MIT while `README.md:512` and `:520`, sixteen lines earlier, say the project does not own the third-party content and that commercial use requires the original rights-holder's permission. **MIT covers the 10,666 lines of code. It does not and cannot cover 543 images the same file says belong to someone else.** Treat the code as MIT and the images and prompts as unlicensed third-party content.

---

## Rung 0 — read these five things (35 min, zero install)

1. **`api/_lib/api-imports.test.js`** — 32 lines, and the cheapest correct answer to the defect v269 and v271 both circled. It recurses `readdir` over `api/` and imports everything. **No list to drift.** Compare it against v271's sha256 manifest: same guarantee, one twentieth the machinery.
2. **`scripts/generate-style-skill.mjs:20-73`** — five fail-closed invariants including a **cross-document reference check** (every template anchor must exist as `<a name=…>` in another file) and an **on-disk existence check** for every cover image. Then `:30-35`, `assertNoPattern()`: a build-breaking assertion against one named AI-slop construction.
3. **`api/_lib/community.test.js`** — read the 26 test names. `'payment kill switch defaults closed and changes only on explicit true'` and `'browser roles have no direct table grants for orders or QR bytes'` are the two worth stealing outright: **a test that a fail-closed default is fail-closed, and a test that the untrusted client role cannot reach the table.**
4. **`api/generate-image.js:186-244`** — reserve → generate → complete, with a compensating `releaseReservation` in the catch and 429 distinguished from 502. The credit-metering pattern, in 60 readable lines.
5. **`202605090002_auth_policy_lints.sql`** — a migration whose entire purpose is to clear an external advisor's warning list. Read it next to the fact that the repo has **no linter of its own**, and the ship's rule writes itself.

---

## Rung 1 — ⭐⭐⭐ about us, 30 minutes, and it is now eighteen ships old

**Move `(C) proposed-verify-vault-inventory.sh` into the path of something that already happens, and delete the word "proposed."**

v271 said this. v255 wrote the script. It has not run once. This ship explains why, and the explanation is not laziness: **a check that requires you to remember it is a check you do not have.** HiThink's validators run because Vercel needs a build. Our script runs because… nothing.

Concretely:
- Move it to `bin/verify-vault-inventory.sh`, drop `proposed`.
- **Put its invocation in the per-ship append itself** — the one procedure that provably executes every single ship — not in a hook nobody installs and not in a document nobody re-reads.
- Add **clause 10** from v271 (*for every declared gate, assert its trigger covers the files it asserts on*) and **clause 11** from this ship: **for every declared check, name the thing that already requires it — and if nothing does, either wire it to something that does or delete it.**

⭐ **A worked demonstration is already in this ship:** the `_state/03c` source-of-truth notice was stale by seven ships at v271 because nothing guarded the notice. v271 fixed it by making the bump *part of the per-ship append*. That is the right mechanism and it worked. Apply the same move to the script.

---

## Rung 2 — ⭐⭐ the agent-surface borrow (45 min, zero install)

Three things to lift into `05 Skills/`:

1. **Generate the skill's reference from a schema, and validate the schema on the way through.** `data/style-library.json` → `references/style-library.md` is exactly the vault's own shape (`_patterns/06` → the routine's skill files), except **his generator refuses to run if a cross-reference is dangling or a referenced file is missing.** Ours has no such step. The v243 symlink and the v271 sha256-manifest are the two prior answers to this; **his is the third and the cheapest: make the artifact derived, and put the derivation in the build.**
2. **Steal the anti-slop assertion and aim it at the right file.** `assertNoPattern()` is nine lines. Its lesson is not the regex, it is the *placement*: an assertion inside the generator, on the generated output, that stops the build. ⚠️ And its lesson is also the failure: **it guards the 26 KB that cannot contain the defect and not the 930 KB that does.** If we add one, aim it at what we actually write.
3. **Add the negative routing clause his skill lacks.** v271's subject had one in 10 of 10 skill descriptions; this one has none. Our nine `05 Skills/` descriptions have none either, and **the eight routine files v2.1→v2.8 are still the acid test** — each older one should say *"superseded — use v2.8"* in one line. This is the v271 Rung-2 item, still open, and this ship is the second consecutive subject to demonstrate what its absence costs.

---

## Rung 3 — ⭐⭐ into hireui (60 min)

1. **The three payment tests, verbatim in shape:** a test that each fail-closed flag defaults closed; a test that the anon/browser role holds no direct grants on any table it must not reach; a test that a callback's amount is re-checked against the stored order. hireui has none of these and will eventually need all three.
2. **`set search_path` on every function, no exceptions** — and a check that counts functions against pinned search paths, because *26 of 26* is only meaningful if something recounts it.
3. **The reservation pattern for any metered LLM call** — reserve, call, complete-or-release, with the upstream-busy case distinguished. This composes directly with the **RATIFIED candidate-LLM legibility ADR**: the reservation row is already the audit record.
4. 🔴 **And the caveat to carry with it:** his ledger has **no advisory lock and no reaper**, and the prompt column is `not null` with **no retention path anywhere in 12 migrations**. If we borrow the pattern, borrow it with `pg_advisory_xact_lock` (which he wrote two months later, in the newer migration, and never back-ported) and with a retention policy. **For hireui, a candidate's typed text retained indefinitely with no deletion path is not a defect, it is a compliance problem.**

---

## Rung 4 — ⭐ the ten-minute check on ourselves

Run the three cheapest measurements this ship used, against the vault and hireui:

```bash
grep -rc 'set search_path' supabase/migrations/ 2>/dev/null; grep -rc 'create or replace function' supabase/migrations/ 2>/dev/null
```

If those two numbers differ, that difference is a privilege-escalation surface.

Then the one that found this ship's headline — **compare the artifact you validate against the artifact that changes:**

```bash
git show $(git describe --tags --abbrev=0):path/to/generated-artifact | md5; md5 -q path/to/generated-artifact
```

If the tagged copy and HEAD agree while the input grew, your gate is pointed at something frozen.

---

## Rung 5 — the agent skill itself (10 min, low risk, install deliberately)

`npx gpt-image-2-style-library install claude-code` writes **one** directory: `~/.claude/skills/gpt-image-2-style-library`. I read all 92 lines of `bin/install.mjs`: `rmSync` targets **its own subdirectory only**, it honours `CLAUDE_HOME`, it throws if a package entry is missing, and it rejects unknown targets. **There is no `postinstall` in either `package.json`** — so `npm install` alone writes nothing.

⚠️ **Name the target explicitly.** Bare `npx gpt-image-2-style-library` defaults to `all` — Codex **and** Claude Code **and** `~/.agents` — with no prompt, and the payload includes a **2,023,093-byte** example PNG, so the default writes ~6 MB across three home directories for 29 KB of text.

⚠️ **And know what you are getting: a May snapshot.** The published skill is byte-identical to the `v1.0.4` tag of **2026-05-08**. Its newest referenced example is **case 378**; the catalogue now runs to **532**. Its 22 templates are current only because they have not changed. **154 cases the skill has never heard of.**

---

## 🔴 Never

- **Never treat MIT as a licence over the 543 images or the 529 prompts.** `README.md:512` and `:520` say plainly that the project does not own them and that commercial use needs the original rights-holder's permission. Sixteen lines later the same file grants MIT. **The code is MIT; the content is not the author's to license.**
- **Never copy `.env.example` to `.env` unedited.** `SUPER_ADMIN_EMAILS` is the one populated value in the file, and it is populated with the upstream author's two real addresses. A deployment that keeps it and enables Google sign-in grants him `super_admin` on your instance.
- **Never quote the `Cases-532` badge.** The number is 529; three ids were never written.
- **Never cite a copied prompt as ready to use** without checking for `{argument name="…" default="…"}` — 70 of 529 contain it, nothing substitutes it, no document explains it, and the copy button hands it to you with the braces in.
- **Never point this product's generation path at anything sensitive.** The prompt is stored `not null` with no retention path, and forwarded unfiltered to a third-party sponsor's API.
- **Never read "100% Original AI Rewritten" as a provenance claim about the images.** The AI was Claude Opus 4.6, the artefact was the prompts, and the attribution is in a git trailer on the root commit.
