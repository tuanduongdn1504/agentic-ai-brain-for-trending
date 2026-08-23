# (C) Obscura — Deep Dive

**Subject:** `h4ckf0r0day/obscura` — "The open-source headless browser for AI agents and web scraping. Lightweight, stealthy, and built in Rust."
**Wiki version:** v267 · **Date:** 2026-08-23 · **Licence:** Apache-2.0
**Verdict:** GOAL-ALIGNED INCLUDE 3/4 · **NO new top-level pattern** · **one new §C-2 standalone at N=1**
**Pilot:** ⭐ **READ-AND-BORROW-AND-CONSIDER-PILOTING** — the first permissively-licensed subject in this class

---

## 1. Ground truth (source-verified)

Two independent clones; HEAD `39fe4d24` (2026-08-21).

| Fact | Value |
|---|---|
| Commits | **910** |
| Roots | **1** — `2e5d63cc`, 2026-04-13, by `h4ckf0r0day`: `.gitattributes` + `LICENSE` only |
| Merges / non-merges | 135 / 775 |
| Distinct author emails | **59** |
| Tags | 13 (`v0.1.0` … `v0.2.0`) |
| Span | 2026-04-13 → 2026-08-21 (**~4.3 months**) |
| Crates | **9** (`obscura`, `-browser`, `-cdp`, `-cli`, `-dom`, `-js`, `-mcp`, `-net`, `-render`) |
| Rust lines (crates/) | **138,078** in 107 files |
| Vendored lines (vendor/) | **33,543** in 75 files (`taffy` 0.12.1, `cosmic-text` 0.14.2) |
| Test functions | **1,264** `#[test]` / `#[tokio::test]`; 34 files under `*/tests/*` |
| CDP method arms | **189** across 16 domain files |
| MCP tools | **37** |
| Dependencies | 468 packages in `Cargo.lock`; **0 git dependencies** |
| CI | `ci.yml`, `release.yml`, `docker.yml` — all present and real |

**This is not a fork.** The root commit is the repo owner's own. D49 (a namespace is not a claim about authorship) does **not** apply.

### ⚠️ A measurement trap that produced a wrong first answer

`git log` on this repository **silently under-reports**. Under git 2.19, `git log --oneline | wc -l` returns **50** and `git log --reverse | head` reports a false "first commit" of **2026-08-08**, because the default date-ordered revision walk terminates early under this repo's commit-date skew. `git rev-list --count HEAD` returns the true **910** via the pack reachability bitmap.

My first three ground-truth numbers were therefore wrong (50 commits, 7 authors, a 13-day project). **Rule for the routine: `git log` is a display command, not a counting command. Derive counts from `git rev-list`, and roots from `git rev-list --max-parents=0`.** Note that `--max-parents=0` gave the correct root on the very first attempt — the root was already in hand while I mis-stated the date from `git log`.

A second, smaller instance of the same class: `grep -c '^commit '` over `git rev-list --format` output returned **912** because two commit-message bodies contain a line beginning `commit `. Anchoring the pattern (`'^commit [0-9a-f]\{40\}$'`) returns exactly **910**.

---

## 2. What it actually is

A **from-scratch browser engine**, not a wrapper. It owns its DOM (`obscura-dom`), its CSS cascade, layout and paint (`obscura-render`, 71,415 lines — 52% of the codebase), and its HTTP stack (`obscura-net`). It embeds **V8 via `deno_core` 0.350** for JavaScript (`obscura-js`, 24,280 lines, including a **15,118-line `bootstrap.js`** DOM/browser shim), and speaks **Chrome DevTools Protocol** (`obscura-cdp`) so Puppeteer and Playwright connect unmodified.

HTML parsing rides the **Servo stack** — `Cargo.toml:30-34`: `html5ever 0.39`, `markup5ever 0.39`, `selectors`, `servo_arc`, `cssparser`.

Four release configurations, gated by cargo features (`render`, `stealth`), shipped as four archive variants. **Stealth is opt-in, not the default** — the plain archive is documented "Stealth transport: No". `render` is likewise optional (104 `#[cfg(feature = "render")]` guards).

Delivery surfaces: a CLI (`fetch` / `serve` / `scrape` / `mcp`), a CDP WebSocket server, a **first-party MCP server** (37 tools), an embeddable Rust library, a distroless Docker image, and a **first-party agent skill** at `skills/obscura/SKILL.md`.

---

## 3. The agent-facing surface (why this is on goal #1)

Three distinct agent surfaces, all first-party:

1. **`crates/obscura-mcp` — 37 MCP tools.** `browser_navigate`, `browser_evaluate`, `browser_snapshot`, `browser_click`, `browser_fill_form`, `browser_extract`, `browser_markdown`, `browser_pdf`, `browser_screenshot`, `browser_get_cookies`, `browser_set_cookie`, `browser_storage_state`, `browser_set_storage_state`, `browser_interactive_elements`, `browser_network_requests`, tab management, and more. The README documents Claude Desktop configuration directly.
2. **`skills/obscura/SKILL.md` — 130 lines**, a genuine cross-harness agent skill with activation description and workflow guidance.
3. **`AGENTS.md` — 202 lines**, explicitly "Guidance for AI coding agents and contributors."

**Claude usage is disclosed in the history.** Across all 910 commits there are **47 `Co-Authored-By:` trailers, 6 of which name Claude** — `Claude Sonnet 4.6` ×3 and `Claude Opus 4.7 (1M context)` ×3 — across four commits:

| Commit | Date | Author | Subject |
|---|---|---|---|
| `25b6d58` | 2026-05-03 | pryceup | fix: enable request interception when `Fetch.enable` is called (#50) |
| `1da6032` | 2026-05-25 | Ben Younes | feat(cdp): implement `Network.setCookie` + `deleteCookies` (#170) |
| `ea89f05` | 2026-05-29 | Marc Bachmann | Fix puppeteer `exposeFunction` end-to-end (#166) |
| `a23dad7` | 2026-06-08 | johnnogueira | Stealth profile consistency (#269) |

⭐ **All four are outside contributors.** `SGavrl`, who authored 660 of the 910 commits, discloses no AI co-authorship anywhere. Whether that reflects non-use or non-disclosure is **not established**.

`CONTRIBUTING.md:25-26` sets an explicit policy: *"**Human oversight required.** AI-assisted contributions are fine, but low-quality or unreviewed agent output will be closed."* And `:178`: *"No AI-generated filler."* This is better-calibrated AI governance than most subjects in the corpus — compare v243, whose 905 Claude trailer lines were a default left on rather than a curated record.

---

## 4. What is genuinely excellent — and it is a lot

This section is longer than the defect section, which is the honest proportion.

### 4.1 ⭐⭐⭐ The best supply-chain posture in 267 subjects

`ci.yml` opens with a **written threat model** (`:6-8`):

> *"Pull requests execute contributor-controlled build scripts, proc macros, tests, and binaries. They must never receive a write token or repository secrets. Publishing remains isolated in the tag-only release workflows."*

And then it actually does that:

- **`permissions: contents: read`** at top level in both `ci.yml:9-10` and `release.yml:8-9`. In `release.yml`, `contents: write` appears in exactly one job (`:203-204`) carrying the comment *"This job never checks out or executes repository code. The write token is available only while collecting and publishing the completed artifacts."*
- **`persist-credentials: false`** on every checkout (`ci.yml:36, 123, 209, 217`).
- **All 12 distinct GitHub Actions pinned to full 40-character SHAs**, each with a version comment. Zero unpinned actions across all three workflows.
- ⭐ **The trusted-base pattern.** `ci.yml:54-55` reads the policy script and the dependency-ban list **from the base revision**, not the PR's checkout:
  ```
  git show "$base_sha:scripts/ci/pr_policy.py" > "$policy_root/pr_policy.py"
  git show "$base_sha:deny.toml"               > "$policy_root/deny.toml"
  ```
  ⇒ **a malicious PR cannot weaken the check that is judging it.** Same trick at `:249-250` for the perf scripts, and `:251-252` runs the base build from a separate trusted worktree *"so a PR-supplied `.cargo/config.toml` in the merge checkout cannot alter the compiler."*
- ⭐ **Cache poisoning closed** (`:143-145`): `save-if: false` — *"PR caches are restored but never saved. A contributor therefore cannot poison a cache later consumed by a release."*
- ⭐ **They anticipated evasion of their own gate** (`:92-94`): rename detection is deliberately disabled *"so both sides of a rename are classified. Otherwise moving runtime code to a documentation-looking path could incorrectly skip the runtime checks."* This is the corpus's first subject that pre-empted a path-classifier bypass.

### 4.2 The tests are real and they are gated

**1,264 test functions, and CI runs them on every pull request** — four builds and three test configurations (`ci.yml:147-187`): render, stealth transport, and no-render. This is not v263 (403 tests nothing ever ran) and not v265 (a wired gate never invoked).

`AGENTS.md:44-49` documents *why* the runner is unusual, with the cause:

> *"`cargo test` runs the whole test binary in one process, but the engine holds a single V8 isolate per process, so the runtime tests fail under it. `nextest` runs each test in its own process, which is the only supported way."*

⭐ A non-obvious constraint, written down with its mechanism. That is what an `AGENTS.md` is for.

### 4.3 A real SSRF gate that revalidates redirects

`validate_fetch_url` is enforced on the JS fetch path and on **every redirect hop** — `crates/obscura-js/src/ops.rs:2234, 2331, 2572, 2820`, with the comment at `:2469` explaining that *"reqwest's auto-follow would bypass `validate_fetch_url` on the redirect."* They disabled auto-follow to re-check each hop. Private-network access is **denied by default**, opt-in via `--allow-private-network`. CI keeps the default policy for the whole suite and opts in for exactly one focused test (`ci.yml:160-167`).

### 4.4 `deny.toml` distinguishes "unmaintained" from "vulnerable"

Five `RUSTSEC` entries are ignored — **each with a written reason and its transitive parent named** — under a header stating *"Real vulnerabilities fail the build. The advisories below are *unmaintained* notices for transitive crates with no available fix."* `[sources]` sets `unknown-registry = "deny"` and `unknown-git = "deny"`, and `Cargo.lock` confirms **0 git dependencies**. And because CI fetches `deny.toml` from the trusted base, a PR cannot add an ignore entry to smuggle a vulnerable dependency past.

### 4.5 Unimplemented CDP methods fail loudly

I went looking for the classic compatibility lie — a CDP method that returns empty success so Puppeteer proceeds on a false premise. It is not here. `dispatch.rs:521` returns `Unknown domain`, `:557` emits JSON-RPC **`-32601` (MethodNotFound)**, and `:812-813` is a test asserting exactly that. `lp.rs` likewise errors on unknown methods.

### 4.6 The docs inventory is immaculate

The vault's signature v240 inventory check — index-vs-content in **both** directions — comes back **clean**: every one of the 20 files `docs/SUMMARY.md` lists exists, and every `docs/*.md` on disk is listed. Zero drift. After v239, v254 and v265's 97 dangling pointers, this is the first subject to pass it perfectly.

### 4.7 Correctness evidence is in-tree

`render-repros/` holds **77 hand-written CSS conformance fixtures** — `box-sizing.html`, `fixed-table-layout.html`, `display-contents-cascade.html`, `font-shorthand.html`, `modern-containing-block-triggers.html`. `AGENTS.md:127` calls it *"the tracked public evidence harness."*

### 4.8 Honest limits, stated in public

`README.md` on the render engine: *"It remains an evolving independent engine: long-tail CSS, some Web APIs, media playback, compositor effects, and platform font rasterization **may differ from Chromium**."* `AGENTS.md:76-78` admits *"the tree is not rustfmt-clean"* and tells agents not to bulk-format. `AGENTS.md:99-101` states the benchmark noise floor is *"about plus or minus 10%."* The Dockerfile comment (`:52-54`) notes `0.0.0.0` is a container-only override and *"Native binary still defaults to 127.0.0.1 (loopback only)."*

---

## 5. ⭐⭐⭐⭐ THE HEADLINE — the repository implements a competitor's protocol namespace and never names the competitor

`README.md:403` publishes this row in the CDP capability table:

```
| **LP** | getMarkdown (DOM-to-Markdown conversion) |
```

`LP` is expanded nowhere. Not in the README, not in `docs/`, not in `AGENTS.md`, not in a code comment. The implementation is `crates/obscura-cdp/src/domains/lp.rs:13` (`"getMarkdown" =>`), and `crates/obscura-js/src/markdown.rs:1` comments *"Shared markdown extraction script used by the LP.getMarkdown CDP method"* — still without expanding it.

**`LP` is Lightpanda.** From Lightpanda's own blog, published **2026-03-11**:

> *"`LP.getMarkdown` is the first command in a new custom CDP domain called **LP**, which is home for **Lightpanda-specific** capabilities that go beyond what standard CDP offers."*

Lightpanda documents both access paths — *"from the CLI with `--dump markdown` or programmatically via a custom CDP command `LP.getMarkdown`."* Obscura ships **both**: `lp.rs` was present in `8749725 "Initial Release"` on **2026-04-13**, and `--dump markdown` arrived `d8b7c5f` on 2026-05-13.

**The priority is one month on the namespace, and about a year on the project.** The 2026-03-11 LP-domain date I verified myself. A prior-art lens additionally dated Lightpanda's first public announcement to mid-2025 and its development start to circa 2022 — ⚠️ agent-sourced, **not independently verified by me**, and not load-bearing: the LP date alone settles the namespace question.

**A grep for `lightpanda` across every `.rs`, `.md`, `.toml` and `.yml` in the repository returns zero hits.**

### Why this matters, stated fairly

Lightpanda is the nearest peer this project has, and the resemblance is not incidental:

| | Lightpanda | Obscura |
|---|---|---|
| Positioning | "the headless browser for AI agents" | "The headless browser for AI agents and web scraping" |
| Built from scratch, not a Chromium fork | ✓ | ✓ |
| Language | Zig | Rust |
| JS engine | V8 | V8 (`deno_core`) |
| HTML parser | html5ever (Servo) | html5ever (Servo) |
| CDP-native drop-in | ✓ (22 domains) | ✓ (16 domain files / 189 methods) |
| Native MCP in the binary | ✓ (announced 2026-03-11) | ✓ (`obscura-mcp`) |
| Markdown extraction | `--dump markdown` / `LP.getMarkdown` | `--dump markdown` / `LP.getMarkdown` |
| Speed claim vs Chrome | 9–11× | "~12x" (`AGENTS.md:98`) |
| **Licence** | **AGPL-3.0** | **Apache-2.0** |

⚠️ **What this is NOT.** There is **no evidence of code derivation** and I am not implying any. The languages differ (Zig → Rust), `lp.rs` is ~20 lines calling Obscura's own `HTML_TO_MARKDOWN_JS`, and implementing a protocol method name is compatibility work, not copying. html5ever and V8 are the obvious choices for anyone doing this in Rust. **There is no licence problem here.** Lightpanda's four LP commands (`getMarkdown`, `getSemanticTree`, `getInteractiveElements`, `getStructuredData`) are only one-quarter implemented here.

**The finding is legibility, not legality.** Implementing `LP.getMarkdown` is a *service to users* — a client written against Lightpanda works against Obscura. The defect is that the repository publishes a two-letter row in its public capability table that no reader can decode, and that the one comparison table it does publish benchmarks the competitor it beats (headless Chrome) while never mentioning the competitor it resembles. A reader deciding between these two projects — and the decision is real, because **one is AGPL and one is Apache-2.0** — gets no help from either.

---

## 6. The gate findings — and they all land on the same side of one line

### 6.1 ⭐⭐⭐ The number the rule names is computed, displayed, and never enforced

`AGENTS.md` states the project's behavioural standard twice:

- `:51-52` — *"The authoritative behavioral gate is the **obstacle course** in the companion repo `obscura-benchmark` (33 capability + speed stages, **must stay 33/33**)"*
- `:69` — completion requirement 4: *"The obstacle course still reports **33/33**."*

CI does run it, properly: `ci.yml:211-217` checks out `h4ckf0r0day/obscura-benchmark` **pinned to commit `6ebac829`**, and `:239-260` builds the *base* revision too for an interleaved comparison. That is real rigour.

Then `scripts/ci/compare_obstacle.py`:

- `:15` `EXPECTED_STAGE_COUNT = 33`, enforced for both sides at `:65-72`
- `:73-76` stage-name set equality — you cannot rename or drop a stage
- `:36-43` type validation that explicitly rejects `bool` for `median_ms`, because `isinstance(True, int)` is `True` in Python — an expert detail
- `:91-92` computes `base_passed` and `candidate_passed`
- `:97` renders them: `| Correct stages | {base_passed}/{len(base)} | {candidate_passed}/{len(candidate)} |`
- `:112-113` — **the only failure condition in the file:**
  ```python
  if regressions:
      raise SystemExit("candidate introduces new obstacle-course failures")
  ```
  where `regressions` (`:78`) = stages that **passed on base and fail on candidate**.

⇒ **`candidate_passed` is computed, printed into the step summary for a human to read, and never compared to 33.** The gate is purely *differential*. A candidate at 30/33 passes if base was 30/33. A candidate at 0/33 passes if base was 0/33. The absolute standard that `AGENTS.md` states twice as mandatory is the one thing the mechanism does not check.

One layer up, the same shape in the same job: `ci.yml:269-279` wraps both obstacle runs in `set +e`, captures `base_status` and `pr_status`, and then **`printf`s them**. Neither variable is ever tested. Only `json.tool` can fail the step afterwards — i.e. malformed JSON, not a failed run.

This is the corpus's running class — v256's staleness mark declared/persisted/displayed/unenforced, v264's two token accountings where the displayed one is not the acted-on one, v265's gate that prints `PASS` on the file it exists to block. Here it is unusually pure, because **the gate is otherwise excellent**: it validates stage count, set equality and types with real care, and it does fail on regressions. It simply never asks the question its own documentation asks twice.

### 6.2 Documentation changes are exempt from every check — by design

`ci.yml:86` classifies the following as neither `runtime` nor `audit`:

```
*.md|README*|LICENSE*|docs/*|.github/ISSUE_TEMPLATE/*|...|.gitignore|.gitattributes|.editorconfig)
```

⇒ a PR touching only `README.md` runs the policy script and **nothing else**: no build, no tests, no cargo-deny, no obstacle course. This is a defensible and common engineering decision — you don't compile V8 to fix a typo.

It is also where every performance claim in the project lives.

### 6.3 Four speed figures, no two the same

| Location | Claim | Implied ratio |
|---|---|---|
| `README.md:35` | Page load **85 ms** vs `~500 ms` | ~5.9× |
| `README.md:361` | Static HTML **51 ms** vs `~500 ms` | ~9.8× |
| `README.md:362` | JS + XHR + fetch **84 ms** vs `~800 ms` | ~9.5× |
| `README.md:363` | Dynamic scripts **78 ms** vs `~700 ms` | ~9.0× |
| `AGENTS.md:98` | *"~12x faster and uses ~6x less memory"* | ~12× |

The headline table's **85 ms** matches none of the three benchmark rows beneath it. `AGENTS.md`'s **~12×** exceeds all three. The memory claims are consistent (30 MB vs 200+ MB ≈ 6.7×, against "~6x").

⚠️ **Fair reading:** `AGENTS.md:98` says *"on framework pages"* — a workload none of the three benchmark rows measures, so ~12× may be a legitimately different measurement. And `README.md:365` points to a real external suite: *"The full benchmark suite (WPT conformance, obstacle course, real-world corpus, and vs-Chrome speed) lives in a separate repo."* That repo is SHA-pinned in CI, so it demonstrably exists. This is **far better than v262**, which published twelve template counts for six templates with no harness at all.

**But the consequence is structural:** the fidelity evidence is in-tree and checkable (77 fixtures, §4.7); the performance evidence is not, and the surface that quotes it has no gate. The claims verifiable from inside the repository are conservative — the README advertises ~10 CDP domains while the code implements **189 methods across 16**, *underselling* capability by a wide margin. The claims verifiable only from outside it are the inflated ones.

⭐ That is a refinement of v262's rule. v262 concluded *everything the code can check is right and everything only the prose asserts is inflated*. The sharper discriminator is not code-versus-prose but **verifiable-from-inside-the-repo versus verifiable-only-from-outside-it.**

### 6.3b The same table's other inflated cell — "Anti-detect: Built-in"

`README.md:34`, in the table whose whole purpose is to contrast Obscura with headless Chrome:

```
| Anti-detect  | **Built-in** | None          |
```

But `crates/obscura-cli/Cargo.toml:17` reads **`default = []`** — neither `stealth` nor `render` is on by default. Anti-detect requires a **compile-time feature** (`--features render,stealth`, which additionally pulls in CMake, Clang and a BoringSSL build) **and** a runtime `--stealth` flag (`README.md:457`: `| --stealth | off | Anti-detection mode |`).

"Built-in" against a column reading "None" implies you get it by default. You do not.

⚠️ **And again the detail beneath the headline is honest.** `README.md:167-172` publishes the release-archive matrix truthfully — the plain archive is listed "Stealth transport: **No**" — and both `AGENTS.md` and `SKILL.md` are explicit that stealth needs the feature build. So the accurate statement is narrow and consistent: **every inflated claim in this repository is in the top-of-README comparison table; every document beneath it is accurate.** That is the third instance of the same shape (85 ms, ~12×, Built-in) on the one surface with no gate.

⚠️ **Separately: no in-tree evidence of testing against real detection services.** A scoped search for `creepjs|fingerprintjs|bot.sannysoft|browserleaks|incolumitas|datadome` across `*.rs`, `*.md` and `*.html` (excluding `vendor/`) matches exactly one file — `docs/Configure-stealth-and-proxies.md`, prose. There are no automated detection-suite tests for a capability the comparison table advertises as a headline advantage. The external `obscura-benchmark` repo was not examined and may contain some; absence here is not proof of absence there.

### 6.4 ⭐⭐⭐ And the skill instructs the agent to preserve exactly those claims

`skills/obscura/SKILL.md` is genuinely good. Its verification guidance is some of the best in the corpus:

- `:117` — *"Confirm both engines navigated successfully and produced **nonblank** images before interpreting a diff."* ⇒ a guard against the false-success class (v251/v260): a blank capture would otherwise "pass."
- `:118` — *"Treat a pixel metric as a **regression tripwire, not a verdict**."*
- `:121` — *"**Do not introduce hostname-specific rendering logic.**"* ⇒ forbids the agent from special-casing sites to make a test go green. Excellent.
- `:123` — a whole section headed **"Set expectations accurately"**, telling the agent the engine's real limits.

And `:128`, five lines later:

> *"**Preserve the project's existing positioning and published benchmark claims** when editing its documentation."*

Charitably — and this reading is probably correct — that means *don't rewrite numbers you have not re-measured*, which is sound discipline, and the next sentence supports it: *"Use the benchmark suite and matched inputs when adding or updating performance or fidelity measurements."*

But note what it does in combination with §6.2 and §6.3: the agent is told to set expectations accurately about the engine, and to preserve the published positioning and benchmark claims — **the one set of statements it cannot check from inside this repository, on the one surface CI deliberately exempts.** The honesty instruction and the don't-touch-the-marketing instruction sit five lines apart, and only one of them is about something the agent can verify.

### 6.5 A fence made of a sentence

`AGENTS.md:134-135`:

> *"**Git-ignored** internal handover notes are private working material: do not edit them, link them from public documentation, stage them, or **commit them**. **Do not commit generated screenshots or reports.**"*

`.gitignore` is **18 bytes**:

```
target/
.DS_Store
```

Nothing ignores any handover note. `.git/info/exclude` in a fresh clone is the stock 250-byte git template. So on any clone, the private layer's only protection is the paragraph asking the agent not to commit it.

And the tree contains the proof it does not hold. **`build.log` — 283 lines, committed** at the repo root in `0df158e` (2026-07-24, *"Merge remote-tracking branch 'origin/main' into pr471-push"*) — is a generated build report, the exact category `:135` forbids. It leaks the maintainer's private workspace seven times:

```
Compiling obscura-browser v0.1.0 (/root/obscura2/merge471/crates/obscura-browser)
```

⇒ built **as root**, in a directory named **`obscura2/merge471`**. The `2` and the PR-numbered merge directory are consistent with `AGENTS.md`'s description of a private working layer.

This is v258's rule at N=2 and inverted: v258 found an ignore rule *deleted by the commit that added the files it named*; v267 has an ignore rule that **never existed** for files a document says are ignored.

### 6.6 The MCP server has 37 tools and no gate

A scoped grep across `crates/obscura-mcp/` for `approve|confirm|consent|read_only|readonly|dry_run|allowlist` returns exactly two things: the word "confirm" inside a tool *description* string (`lib.rs:575`), and a CORS **origin** allowlist. There is **no approval prompt, no read-only mode, and no URL allowlist** on any of the 37 tools — including `browser_evaluate` (arbitrary JS in the page), `browser_storage_state` / `browser_get_cookies` (read the session), and `browser_pdf` (write a file).

For comparison, v264's NeMo shipped a coding-agent config with plan mode, every mutating tool denied by name, and a $1 budget cap — and that was a *library*, not a browser.

### 6.7 ⭐⭐⭐ v265's rule at independent cross-organisation N=2 — and a stronger instance

`crates/obscura-mcp/src/http.rs:132-146`:

```rust
/// Origin allowlist for browser callers, read from `OBSCURA_MCP_ALLOWED_ORIGINS`
/// (comma-separated). Unset/empty → permissive (unchanged `*`) so hosted
/// dashboards keep working (issue #175).
...
/// When an allowlist is configured, a browser `Origin` must match one of its
/// entries (case-insensitive); this stops a malicious local web page from
/// driving the loopback MCP port.
fn origin_allowed(origin: Option<&str>, allowlist: Option<&str>) -> bool {
    match allowlist {
        None => true,
        ...
```

And `:161-167` — `cors_header` returns `Access-Control-Allow-Origin: *` when no allowlist is set.

⇒ The comment **names the attack its own default permits** — *"a malicious local web page … driving the loopback MCP port"* — in the same comment block that explains why the default stays permissive: *"so hosted dashboards keep working (issue #175)."*

**v265's sentence was:** *a discipline travels freely wherever it is FREE and stops wherever the safe choice would COST something.* v265's instance was an ACL default moved to `private` because nothing broke, beside an auth default left off because the proxy would break. **This is that rule again, from a different author, in a different language, in a different domain, two ships later — and it is the stronger instance, because here the cost and the attack are written in the same comment.**

The mitigations are real and should be stated: the native binary binds loopback by default, the Dockerfile documents `0.0.0.0` as container-only, and requests with no `Origin` (native MCP clients) are the normal path. The exposure is specifically a browser-origin caller reaching a loopback MCP port — which is precisely what the comment describes.

### 6.8 Vendored forks — declared properly, with narrow gaps

⚠️ **This section originally overstated the problem, and the fleet corrected me. See error ledger #5.**

`vendor/taffy` (0.12.1) and `vendor/cosmic-text` (0.14.2) are **not pristine copies**. After the initial vendoring, **14 commits patched 37 vendored source files** with subjects like *"Match grid replaced sizing semantics"*, *"Match CSS text breaking semantics"*, *"Respect auto margins on overflowing grid items"*, *"Honor variable font instances"* — browser-specific CSS semantics grafted onto general-purpose layout libraries.

**And the divergence is declared, in the right place, with reasons and an exit condition.** `Cargo.toml:59-64`:

```toml
[patch.crates-io]
# Keep the grid shrink-to-fit correction local until it lands upstream.
taffy = { path = "vendor/taffy" }
# Carry the same canonical variable-font coordinates through shaping and
# rasterization until the upstream API exposes them.
cosmic-text = { path = "vendor/cosmic-text" }
```

⭐ This is the single place a Rust developer looks, each fork carries a one-line reason, and both state the divergence is **temporary and name the condition for removing it** (*"until it lands upstream"*, *"until the upstream API exposes them"*). It also structurally defeats the hazard I first claimed: because `[patch.crates-io]` reroutes the dependency, a version bump cannot silently restore upstream and drop the fixes.

**Licence status: compliant.** `vendor/taffy/Cargo.toml:44` is `MIT`; `vendor/cosmic-text/Cargo.toml:27` is `MIT OR Apache-2.0`. All LICENSE files are preserved in-tree (`vendor/taffy/LICENSE`, `vendor/cosmic-text/LICENSE-MIT`, `LICENSE-APACHE`). MIT requires notice retention and that is satisfied; a licensee may elect MIT for cosmic-text, so Apache-2.0 §4(b)'s modified-file-notice clause need not bite. ⭐ **This is the corpus's cleanest vendoring** — better than v264 (D44 recurring) and v265 (prose credit, no NOTICE).

The remaining gaps are hygiene, and they are minor:
- No `NOTICE` or third-party licence file at the repo root.
- `grep -ri "obscura" vendor/` returns nothing — no marker inside the 37 patched files themselves, so a reader browsing `vendor/cosmic-text/src/shape.rs` sees no sign it is modified.
- `cosmic-text` appears in **no** user-facing document; `taffy` appears once, at `docs/Architecture-overview.md:47`.
- The 22,495-line taffy import landed inside commit `d6be828`, titled *"render: constrain shrink-wrapped grid items"* — the largest third-party code import in the project is invisible in its own commit message.

⭐ Relatedly, `Cargo.toml:66-71` pins `panic = "unwind"` in the release profile under a four-line comment explaining that the anti-panic op protocol **requires** it, and that `panic = "abort"` *"would turn every catchable op panic into a hard crash."* A load-bearing build setting with its reason attached.

### 6.9 Minor

- `Dockerfile:45` uses `gcr.io/distroless/cc-debian12` with no `USER` directive ⇒ the final image runs as **root**; `:nonroot` exists. Base tags `rust:1-slim-bookworm` and `cc-debian12` float (no digest pin) — inconsistent with the 40-char SHA pinning applied to every GitHub Action.
- `Dockerfile:33`'s `2>/dev/null || true` is a legitimate dependency-cache warm-up whose failure is expected; the real build at `:40` is unguarded. **Not** a gate-that-cannot-fail.
- `robots.txt` is **off by default** — `crates/obscura-browser/src/context.rs:131` sets `obey_robots: false`, opt-in via `--obey-robots`. The README documents this default accurately and there is a dedicated test file with four tests. Aggressive default, honestly documented, properly tested.
- `AGENTS.md:104` documents that `op_dom` is wrapped in `catch_unwind` *"so a DOM-op panic returns null instead of aborting the process inside V8's FFI frame."* The trade-off is right — the alternative is worse — but the observable consequence is that an engine bug surfaces to JavaScript as an empty result rather than an error. Worth knowing when debugging.

---

## 7. Corpus position and Pattern Library decisions

**Obscura is new to the corpus** — zero hits for `obscura` across `CLAUDE.md`, `_patterns/06`, `_state/03c` and `PATTERN_LIBRARY.md`. Lightpanda is likewise absent.

### 7.1 §C row C34 — HOLD at N=2

C34 is *"Anti-Detect / Stealth Browser — **a purpose-built fingerprint-spoofing browser** delivered for automation (**vs a general browser-automation tool that treats stealth as one feature**)"*, at N=2 (v69 CloakBrowser + v179 camofox), PROMOTION-ELIGIBLE at N=3. Its capability line: *"a browser whose **primary reason to exist** is fingerprint evasion."*

**Obscura sits on the wrong side of C34's own boundary.** Its headline is *"Native rendering is here. No Chromium required"*; anti-detect is **one row of seven** in its comparison table; and stealth is an **opt-in cargo feature** absent from the default release archive. It is precisely the "general browser-automation tool that treats stealth as one feature" that C34 defines itself against.

⇒ **C34 HOLDS at N=2. Not stretched to a promotion.** This upholds a boundary the way v257 and v259 did — and it is the third consecutive ship where reading a §C row's own definition prevented a false N (v262 C37, v263 C38, v267 C34). The v259 bifurcation's justification now has a demonstrated mechanism at N=3 in consecutive ships.

### 7.2 One new §C-2 standalone, MINTED at N=1

**"From-Scratch Non-Chromium Headless Browser Engine Built as AI-Agent / Scraping Infrastructure."**

Corpus-first for the surface. Every prior browser subject wraps, patches or drives an existing engine: CloakBrowser v69 (patched Chromium), camofox v179 (Camoufox/Firefox), browser-use v41 and Skyvern v24 (automation over existing browsers), crawl4ai v29 and firecrawl v214 (crawler library / API), page-agent v199 (in-page JS), ego lite v247 (a real browser), serve-sim v183 (the simulator analogue). **None owns its DOM, cascade, layout and paint.**

⚠️ **Decisively NOT world-first.** Lightpanda (AGPL-3.0, Zig) precedes it and is named in the row; servo, Verso and Ladybird precede as engine efforts. The mint follows the v206 OfficeCLI / v207 CLIProxyAPI / v224 open-lovable / v244 OpenSandbox discipline — *corpus-first for a capability surface, explicitly not world-first*.

**Why a capability and not a form factor:** the engine choice sets the resource envelope (~30 MB vs 200 MB+), and that is what makes one browser per agent task viable at concurrency. That is the same reasoning that justified v244 (execution substrate) and v215, and it is what distinguishes this from the declines at v222 (world-canonical ≠ world-first), v236 (form factor within a genre), v211 (technique) and v210 (domain).

**NO-MINT alternative recorded:** that Obscura is simply the second entrant in Lightpanda's existing, named class, and the honest act is to record a knowledge data-point rather than mint. I weighed it and it loses, because outside-corpus prior art does not create a corpus N=2 (the camofox precedent: *"Camoufox not a corpus subject; mentions ≠ recursion"*) — it makes a mint "corpus-first, not world-first," which is exactly how v206/v207/v224 were filed. Left for audit review.

⇒ **§C-2 38 → 39. §C-1 unchanged at 12. Counts 46 top-level / 12 CONFIRMED Library-vocab UNCHANGED.** `inflation_check` HELD; per §44 cl. 5, §28 does none of the work here.

### 7.3 Instance-strengthening — recorded, not self-incremented

- **#18 B1-MCP** — a first-party MCP server, 37 tools. ≈N=15 → ≈N=16.
- **#19 19a** — non-Anthropic author (pseudonymous individual + a genuine 59-author community).
- **#66 supply-chain — the corpus's strongest POSITIVE exemplar**, alongside pi v228. 12/12 actions SHA-pinned, read-only tokens, trusted-base policy, no-save PR caches, 0 git deps, reasoned `deny.toml`.
- **#83 honest-deficiency-disclosure — SPLIT.** Genuinely honest: the "may differ from Chromium" paragraph, "the tree is not rustfmt-clean", the ±10% noise floor, the reasoned RUSTSEC ignores, the CORS comment naming its own attack. Not honest: four mutually-inconsistent speed figures, and an unnamed `LP`.
- **#12** MIXED.

### 7.4 Non-claims

- **NOT CONFIRMED Library-vocab #24** (product-first native application retrofitted with a first-party MCP server). #24 requires a product *"whose primary function is not being an agent tool."* Obscura's primary function **is** agent infrastructure. Clean discrimination, not an instance.
- **NOT Pattern #52.** The README asserts "10,000 stars" and carries a Trendshift badge; per §37.4 this environment mocks the GitHub API, so stars and velocity are **page-stated only**. No velocity claimed or verified. (Search surfaced five mirror repos with the identical tagline — consistent with a trending project, still not a #52 claim.)
- **NOT #57.** No corpus subject is a dependency. taffy, cosmic-text, `deno_core` and html5ever are not corpus subjects; Lightpanda is not a corpus subject; C34's peers v69/v179 are peers, not dependencies.
- **NOT a new top-level pattern** — max stays **#85**.
- **NOT #68 / #88 / Domain-Vertical.**
- **Nothing was installed, built, or run.** No credential created; no third-party site contacted.

---

## 8. THE SHIP'S RULE

> **v264** — a discipline stops at the edge of the team that holds it.
> **v265** — a discipline stops where the safe choice would COST something.
> **v266** — the discipline was already at the door, written in a diff nobody opened.
> **v267** — **the discipline stops where the artifact stops being code.**

Everything a compiler reads here is defended to the highest standard in 267 subjects: a written threat model, twelve SHA-pinned actions, a read-only token, a security policy fetched from the trusted base so a contributor cannot weaken the check judging them, PR caches restored but never saved, rename detection deliberately disabled so runtime code cannot enter through a docs-shaped path, four build configurations, 1,264 tests actually gated, an SSRF check revalidating every redirect, and an interleaved base-versus-candidate benchmark against a SHA-pinned external suite.

Everything only a human reads is defended by nothing. `ci.yml:86` exempts every `*.md`. That exemption is where four different speed numbers live; where a `33/33` standard is stated twice that the gate computes, prints and never checks; where a fence around a private layer is a sentence and not a rule; and where a two-letter row names a competitor's protocol without naming the competitor.

None of that is negligence. It is the ordinary gradient: gates get built where failure is loud and cheap to detect. A wrong number in a table fails silently, in a reader, months later — and no one has ever written a CI job for that.

---

## 9. Method, and what I got wrong

**Hand-read** essentially the whole non-generated surface: README (544 lines), AGENTS.md (202), CONTRIBUTING.md, SECURITY.md, SKILL.md (130), all three workflows, all three CI scripts, `deny.toml`, `Dockerfile`, `.gitignore`, `build.log`, `docs/SUMMARY.md` plus targeted reads across all 9 crates. **Zero builds, zero executions, no network contact with any third-party site.**

**Fleet:** a workflow of 9 dimensions × assess→refute, 3 prior-art/identity lenses, a completeness critic, and an adversary pointed at the critic (per v261). **18 agents launched, 14 completed, 4 died on the StructuredOutput retry cap; 2.26M subagent tokens, 816 tool uses, 1,134s.**

⚠️ **Five of nine dimensions failed** — `cdp-protocol`, `render-engine`, `mcp-and-skill`, `ci-tests-gates`, `docs-vs-code`. **Those are the five I had already covered by hand, including the two that produced the headline.** This is the fourth consecutive ship where the fleet's failures landed exactly on ground already covered by hand — which is luck presenting as redundancy, not a design.

⭐ **The decisive finding — `LP` = Lightpanda — came from my own reading of a two-letter table row plus two web searches.** The prior-art lens *did* independently identify Lightpanda as the nearest peer and dated its public announcement to mid-2025, corroborating the not-world-first call from a second direction.

⭐⭐ **The fleet's single most valuable contribution was correcting me, not the subject.** The architecture agent surfaced `Cargo.toml:59-64`'s `[patch.crates-io]` comments, which reversed my §6.8 claim that nothing in the tree records the vendored divergence. That is precisely what a maker/checker split is for, and it is the first ship in this run where the fleet's net contribution was a retraction of the lead's finding rather than an addition to it.

⭐ **The refuter design earned its keep twice:**
- The js-engine refuter confirmed 21/21 claims *and caught two fabricated line citations* from its own assess agent (an op list claimed at `ops.rs:5000-5032` that is scattered across the file; panic handling claimed at `:1600-1625` that is at `:1078-1099`). **v266's rule — a subagent's line number is a claim, not a citation — held again, and this time the harness caught it rather than me.**
- The architecture refuter **REFUTED its own assess agent's** stated crate ordering. Verified: `Cargo.toml:3-13` is dom, net, browser, cdp, js, mcp, render, cli, obscura.

⚠️ **The critic fabricated, and the adversary caught it — v261's rule at N=2.** The completeness critic asserted a `Co-Authored-By` policy violation that does not exist; the adversary went to the source and returned *"the foundational claim … is completely fabricated,"* concluding the critic *"read other agents' claims rather than the source."* v261 found that the only stage producing factual errors was the one that read claims instead of files. Confirmed here, in a different repository, with the adversary-on-critic stage doing exactly the job it was added for.

⚠️ **And I did not adopt the adversary's number.** Its refutation says "zero such commits"; my own hand count is **6 Claude trailers across 4 commits**. Those are compatible — it was refuting a *policy-violation* claim, not a trailer count — but per v264 **D51**, a refuter's assertion is itself a claim, so the figure in §3 is mine, re-derived over all 910 commits.

⭐ **The critic's one genuinely useful contribution survived verification:** it flagged that "Anti-detect: Built-in" is a marketing claim for an opt-in feature. I had under-weighted it. Verified at `README.md:34` against `crates/obscura-cli/Cargo.toml:17` (`default = []`) and written up as §6.3b.

### Error ledger — 5, all mine, all caught pre-publication

1. 🔴 **"910 commits but only 7 authors and a 2026-08-08 root."** WRONG. I read the root date off `git log --reverse | head`, which under-walks this repository. Truth: 59 authors, root 2026-04-13. **The correct root was already in my hands** from `rev-list --max-parents=0` in the same tool call — I quoted the wrong one.
2. 🔴 **"The 59 authors come from absorbed vendored history."** WRONG, and I built a whole hypothesis on it because names like Igor Bukanov and Marc Bachmann looked like other projects' contributors. `vendor/` has only 15 commits, and Marc Bachmann's commit is a genuine Puppeteer `exposeFunction` fix (#166). They are real contributors. **I inferred provenance from the shape of a name — the exact inference §41 forbids for affiliation, committed on a different axis.**
3. ⚠️ **"Zero AI co-author trailers."** WRONG — an artifact of sampling the first 400 commits in topo order (the most recent). Full history: 47 trailers, 6 naming Claude, all four commits from May–June. **Generalising from where I chose to look: the same self-diagnosis as §43.1, for a fourth consecutive ship.**
4. ⚠️ **"912 commits"** from `grep -c '^commit '`. Two message bodies contain a line starting `commit `. Anchored: 910.
5. 🔴 **"No file records that these copies diverge from upstream"** (§6.8, as first written). WRONG. `Cargo.toml:59-64` declares both forks in `[patch.crates-io]` with a reason each and an explicit upstream exit condition — the canonical place for exactly this. I had grepped *inside* `vendor/` for a marker and concluded from its absence, without checking the manifest that reroutes the dependency. **Caught by a subagent, not by me.** I also claimed a maintenance hazard (an upstream bump silently reverting the fixes) that `[patch.crates-io]` structurally prevents. Both retracted above. ⭐ This is the same error shape as ledger #2 and #3 for a third time in one ship: **concluding from where I chose to look.**

### Not established

- Whether the engine actually runs, builds, or passes its own 1,264 tests — **nothing was built or executed**.
- The ~12×/85 ms/51 ms figures — the suite is in `obscura-benchmark`, which I did not clone. Its existence is confirmed (SHA-pinned in CI); its contents and methodology are not examined.
- Whether the `LP` naming was intended as a compatibility shim (overwhelmingly likely) or anything else. **No code derivation from Lightpanda is alleged or evidenced.**
- Whether `SGavrl` uses AI assistance without disclosing it, or does not use it.
- Star/fork counts, "10,000 stars", Trendshift standing, the "~57 MB compressed" image size — all page-stated (§37.4).
- What is in `Bwkyd`-style external surfaces: the `render` and `ci/fix-pr-check-scope` remote branches were not analysed.
- Whether real detection suites were run against stealth mode — no such evidence found in-tree, and absence of evidence in a repo is not evidence of absence.

### Sandbox notes

git **2.19** (`--show-current`, `--no-use-bitmap-index` unavailable; the `git log` truncation above). `python3` present here but **SIGKILLed in prior sessions** — all counting done with `awk`/`grep`/`sed`/`wc`. Vault shell drops stdout intermittently; several commands were re-run routed to a file.

---

## 10. Sources

- [h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura) — the subject
- [Lightpanda: New LP Domain Commands and Native MCP](https://lightpanda.io/blog/posts/lp-domain-commands-and-native-mcp) — 2026-03-11, establishes the `LP` namespace as Lightpanda-specific
- [Lightpanda: Markdown and AXTree docs](https://lightpanda.io/docs/guides/markdown-axtree)
- [Lightpanda: Native Markdown Output](https://lightpanda.io/blog/posts/native-markdown-output)
- [lightpanda-io/browser](https://github.com/lightpanda-io/browser) — AGPL-3.0, Zig, V8, html5ever
- [ScrapingBee on Lightpanda](https://www.scrapingbee.com/blog/lightpanda-headless-browser/)
- [Scrapeless: What Is Obscura?](https://www.scrapeless.com/en/blog/obscura-headless-browser)
