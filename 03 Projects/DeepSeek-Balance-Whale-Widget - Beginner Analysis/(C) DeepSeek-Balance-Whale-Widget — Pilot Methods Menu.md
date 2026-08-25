# (C) DeepSeek-Balance-Whale-Widget — Pilot Methods Menu

**Wiki v277 · 2026-08-25 · overall: ⭐⭐ READ-AND-BORROW, then ONE vault gate. Install NOTHING from this repository.**

---

## Why the install verdict is a flat no

Both products are un-installable for this vault on their own terms, and one is actively hostile to Goal #1:

- **The npm plugin** requires a **DeepSeek Harness web profile** and a `DEEPSEEK_API_KEY`. The vault runs Claude Code, not DSH. There is nothing to install it into.
- 🔴 **The desktop app** (`origin/For–WinDesktop`, tag `v1.0.0+win`) is **Windows-only** *and* its purpose includes rewriting your global `~/.claude/settings.json` to point **every Claude Code invocation** at `https://api.deepseek.com/anthropic`, with a plaintext key and all four model aliases (haiku/sonnet/opus/primary) remapped to DeepSeek models. For an operator whose Goal #1 is mastering Claude, installing this would silently reroute the entire toolchain to a different vendor.

**So the value here is entirely in reading it.** And there is a lot of value — this is better-engineered than most things the corpus reviews.

---

## Rung 0 — Read and borrow (35 minutes, zero install, zero risk)

Read these five things in the clone. All are short, all transfer.

1. ⭐⭐⭐ **`whale-widget-prompt.md` section 六 — the 12 「关键技术结论（踩坑记录）」.** Twelve hard-won conclusions, each stated as a rule *with its reason*. This is the single most transferable artifact in the repository: it is what a maintenance document looks like when the author expects an LLM to read it and act on it. **Note the form, not just the content** — every entry is `<rule> : <why> : <what breaks otherwise>`.
2. ⭐⭐⭐ **`lib/index.js:88-108` — `WEEKEND_VALLEY_FROM_SEC` and `isPeakTime(timeSec)`.** A pricing rule change implemented as a **date-versioned function of the event's own timestamp**, so historical buckets are costed under the rule in force when they happened — with a comment stating exactly why. **The vault's v270 rule was "the only defence is a date"; this is what putting the date in the code looks like.** Also worth stealing: `new Date(n*1000 + 8*3600*1000)` read with `getUTCDay()`/`getUTCHours()` — correct fixed-offset local time with no library and no host-timezone dependency.
3. ⭐⭐⭐ **`lib/index.js:1425-1482` — the per-turn cost aggregator.** Sixty lines where every one avoids a named bug: `Map` bucketing by session id *explicitly because subagents run in parallel*, a turn-number change settling the previous turn when `turn/end` never arrives, `if (agg.cost > 0)` suppressing no-op turns, `Number(x) || 0` everywhere, a whole-handler `try/catch` so a malformed event cannot kill the host, and a `session/disposed` listener that deletes stale aggregates with the comment 「避免内存泄漏」.
4. ⭐⭐ **`lib/index.js:1663-1698` — the ledger currency guard and the #13 story told at the fix site.** DeepSeek's `balance_infos` array order is unstable; taking `[0]` made the ledger book every CNY↔USD flip as a purchase, **fabricating thousands of yuan in a day**. The fix and the incident are documented *in the comment above the function, with the issue number*. **This is D44 done right: the artifact carries its own context.** Copy the habit — a guard whose comment names the incident it exists to prevent.
5. ⭐ **`whale-widget-prompt.md` lesson #5 + the `balance.json` handler** — the **never-throw route contract**. An async handler that throws gets swallowed into an empty 400, so every route returns `200` with `{ok:false,…}` instead. A clean statement of *fail visibly, not silently*.

---

## Rung 1 — ⭐⭐⭐ THE VAULT ITEM: gate the invariants the vault has already written down

**20 minutes. This completes a five-part arc, and this subject supplies the missing piece.**

> **v273** said *where* to put the check (a workflow, not a `package.json` script) · **v274** said *how* to write its clauses (derive the population from the tree, never a list you typed) · **v275** said *what to aim it at* (the claims nobody reads, not the ones your tests already cover) · **v276** said *which claims rot* (bare round floors — `N+`, `~N`, `≈N`) · **v277 says: an invariant you wrote down and never gated is a wish.**

**The subject's demonstration.** `whale-widget-prompt.md:27` states, in as many words, that `lib/index.js`'s exported `name` must be *「与 `package.json` 的 `name` 一致」* — consistent with `package.json`'s name. Three surfaces carry that identity. Two were renamed. **`lib/index.js:1417` still exports `whale-balance-widget`**, the dead pre-package name. The invariant was written by the person who understood it best, in the document everyone is told to consult, and **nothing compared the three copies.**

**The vault's own standing instance.** `_state/03c-projects-v61-v183.md` holds entries through **v277** while its filename says **`-v183`**. This has been flagged since **v239**, diagnosed at v240 and v242, given a fix pattern at v243, a third instance at v244, and mitigated at v245 by applying **D32** — a notice *inside the losing copy* declaring the entries authoritative and the filename stale. ⭐ **D32 was the right call and this ship shows why the alternative fails**: a declared invariant with no comparison is exactly what `whale-widget-prompt.md:27` is. And the vault's index row for that same file was *itself* stale for sixteen ships, along with the in-file notice that was supposed to protect it (both fixed at v271) — **the notice needed a notice.**

### The concrete change

Add **clause (f)** to `(C) proposed-verify-vault-inventory.sh`, alongside v276's clause (e):

> **(f) Multiply-stated facts.** For every fact the vault states in more than one place — the routine's current version, the pattern counts (`46`/`12`), the §C-1/§C-2 sizes, the streak, and every `_state/` chapter's declared version range — either (i) derive it by a printed command, or (ii) carry an explicit **D32 "which copy wins"** declaration. **FAIL when two stated copies of the same fact disagree. FAIL when a copy claims authority without naming the copies it overrides.**

The first thing it catches is the `03c` filename. The second is any ship where `CLAUDE.md`'s head-block counts drift from `_patterns/06`'s registry — which is precisely the **table-vs-log drift the v259 audit flagged and explicitly did not resolve.**

⭐ **And run it.** The script has now existed since **v255** — twenty-two ships — and v273's rule is why that matters: *a check is only as permanent as the place you put it.* It still lives in a project folder and is still invoked by nothing. **Move it to `bin/` and add the invocation to the per-ship append**, which is the item v272 and v273 both handed forward and no ship has executed.

**Method path: A1 → C12 → B7.** *(Read the subject's stated-but-ungated invariant → mechanise the vault's equivalent as a script clause → bump the per-ship append to invoke it.)*

---

## Rung 2 — ⭐⭐ Borrow the feature, not the code (60 minutes, low risk)

The main product's genuinely good idea is not the whale. It is **showing the cost of the turn that just finished, in the surface you are already looking at, from the model's real usage counts rather than an estimate.**

That is buildable for Claude Code today with **no third-party install**:

- A **`Stop` hook** to compute the finished turn's cost from the session's own usage data.
- The **statusline** to display it.

⭐ **Why bother, given `ccusage` exists:** ccusage answers *"what have I spent?"* on demand. This subject's insight is that the number lands **unprompted, immediately, next to the work** — which is what changes behaviour. That distinction is the borrow, and it composes directly with the vault's existing `ccusage → OTel → Grafana` observability thread (which answers the aggregate question well and the immediate one not at all).

⚠️ **Do NOT port the balance-delta ledger.** It is clever and it is the wrong tool here — its own spec discloses that it misses spend whenever the host is closed, and I derived two further undocumented gaps (a one-time bogus delta on upgrade from a pre-currency-aware ledger, and up-to-one-poll-interval of spend dropped at every midnight rollover). Claude Code emits real usage per turn; **count the tokens, do not difference a balance.**

---

## Rung 3 — Nothing above this rung

There is no Rung 4. There is no fenced-install option, because there is nothing to fence: the plugin has no host here, and the desktop app's core function is the thing you must not let it do.

---

## 🔴 NEVERs

- **Never install the desktop app** (`v1.0.0+win`). It writes `ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN` and all four Claude model aliases into your **global** `~/.claude/settings.json`, defaulting to `api.deepseek.com/anthropic`.
- **Never let it near `~/.codex/config.toml`.** That path is `fs::write` — a **wholesale overwrite**. Your MCP servers, profiles and approval policy are gone. (The Claude path merges; the Codex path does not, because `serde_json` was already a dependency and no TOML parser was.)
- **Never assume the Claude merge is safe either.** `serde_json::from_str(&raw).unwrap_or_else(|_| json!({}))` means **a `settings.json` that fails to parse is silently replaced with an empty object and written back.** One stray comma costs you the whole file.
- **Never expose a DSH web profile beyond loopback while this plugin is loaded.** Three routes serve account balance, today's spend and last-turn cost with `Access-Control-Allow-Origin: *` — the localhost bind is the control, and that header is the hole in it.
- **Never cite `v1.0.0` or `v1.0.0+win` as this project's current version.** `v1.0.0` is an orphaned commit containing a zip file, unreachable from every branch; the shipping version is **`0.2.10`**.
- **Never treat `whale-widget-prompt.md`'s 「当前版本：v0.2.5」 as telling you what the document covers.** It is the document's only false sentence, and it is wrong in both directions — the file already contains `v0.2.8`-era rules and omits `v0.2.6`-era prices.
- **Never assume the npm tarball matches the GitHub source.** The workflow publishes with `--provenance=false`, so there is no attestation to check — on a package that reads your API key.
- **Never redistribute the `assets/`** without settling provenance. Full-repository grep across all tracked files and all 30 commit messages found **no attribution** for the artwork or the four audio clips. MIT covers the code; it cannot grant what the project may not hold.
- **Never use `git show "origin/For–WinDesktop:path"`** in this sandbox — the **en dash (U+2013)** in the branch name mangles the revision argument. Resolve to a SHA first (`b4df1a2`).

---

## Suggested next action

**Review and merge the chain — `main` is at v226; v227 → v276 plus this ship are outstanding.**

Then ⭐ **Rung 1**: add clause (f), move the inventory script to `bin/`, and wire it into the per-ship append. It is twenty minutes, it closes an arc five ships long, and the first thing it flags is a filename this vault has been declaring-and-not-fixing since v239.

⚠️ **And the audit is now seventeen ships overdue.** It inherits from this ship the **v237 axis at N=4** (promotion-eligible since N=3), the **(a) metering N=7**, the **v73-class N=2**, and the **(b) STRONG-vs-MODERATE** call — on top of v274's **v107 Enforced-Gate N=2 watch, now 169 ships past its scheduled "~v115"**, v275's **#23 N=6**, and v276's **C26 mechanism-clause generalisation**. ⭐ *A vault whose newest finding is "a written invariant with no gate is a wish" is carrying a scheduled watch it wrote down 169 ships ago.*

---

*Prefix `(C)` — Claude-authored under operator direction.*
