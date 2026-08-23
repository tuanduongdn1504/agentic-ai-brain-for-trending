# (C) Obscura — Verdict

**v267** · `h4ckf0r0day/obscura` · Apache-2.0 · 2026-08-23

---

## Phase 0.9 — GOAL-ALIGNED INCLUDE 3/4

| Axis | Call | Basis |
|---|---|---|
| **(a)** Anthropic-affiliated / registered vendor-direct source | **FAIL** | `h4ckf0r0day` is a pseudonymous individual; the 59 contributors are independent. Per **§41**, no inference from handle, name, or locale. Not Anthropic. |
| **(b)** Goal relevance | **STRONG** | Ships a **first-party MCP server (37 tools)** documented for Claude Desktop, a **first-party agent skill** (`skills/obscura/SKILL.md`), and a 202-line `AGENTS.md`. It *is* agent web-access substrate. Cleanly on the goal-#1 core — **no §40 needed, no override.** |
| **(c)** Quality / depth | **STRONG** | 138,078 Rust lines, 9 crates, 1,264 test functions gated on every PR, 910 commits, 59 authors, 4.3 months. The strongest CI posture in the corpus. |
| **(d)** Actionability | **STRONG** | Directly pilotable (Apache-2.0, single binary, MCP server). Several CI patterns are liftable into the vault and into hireui this week. |

**Cleanly GA. No override. No §40.**

**Streak:** v266 `GA:123` → **`GA:124 · OG:13 [7 ov]`** — **47 consecutive goal-aligned ships, v220 → v267.**
**§35:** CLEAR — window {v265 GA, v266 GA, v267 GA} = 0 OG.
**Override review:** nothing to discharge; v153 → v267 remains 0 overrides.

---

## Pattern Library — one mint, one hold

**Counts: 46 top-level patterns / 12 CONFIRMED Library-vocab — UNCHANGED. Max top-level still #85.**
**§C-1: 12 (unchanged). §C-2: 38 → 39.**

### HOLD — §C row C34 stays at N=2

C34 is *"Anti-Detect / Stealth Browser — a purpose-built fingerprint-spoofing browser delivered for automation (**vs a general browser-automation tool that treats stealth as one feature**)"*, capability line *"a browser whose **primary reason to exist** is fingerprint evasion."* At N=2 (v69 CloakBrowser + v179 camofox), promotion-eligible at N=3.

**Obscura is on the wrong side of C34's own boundary.** Its headline is "no Chromium required"; anti-detect is one row of seven in its comparison table; and stealth is an **opt-in cargo feature** (`crates/obscura-cli/Cargo.toml:17` — `default = []`) absent from the default release archive. It is the thing C34 defines itself *against*.

⇒ **C34 HOLDS at N=2. Not stretched.** ⭐ Third consecutive ship where reading a §C row's own definition prevented a false N (v262 C37, v263 C38, v267 C34) — the v259 bifurcation's justification now has a demonstrated mechanism three ships running.

### MINT — one new §C-2 standalone at N=1

**"From-Scratch Non-Chromium Headless Browser Engine Built as AI-Agent / Scraping Infrastructure."**

Corpus-first for the surface. Every prior browser subject wraps, patches or drives an existing engine — CloakBrowser v69 (patched Chromium), camofox v179 (Camoufox/Firefox), browser-use v41 / Skyvern v24 (automation over existing browsers), crawl4ai v29 / firecrawl v214 (crawler library / API), page-agent v199 (in-page JS), ego lite v247 (a real browser), serve-sim v183 (the simulator analogue). **None owns its DOM, cascade, layout and paint.**

⚠️ **Decisively NOT world-first.** **Lightpanda** (AGPL-3.0, Zig, V8, html5ever, CDP-native, native MCP) precedes it — publicly announced ~mid-2025, and its `LP` CDP domain published **2026-03-11**, one month before Obscura's root commit. servo, Verso and Ladybird precede as engine efforts. Filed on the v206 OfficeCLI / v207 CLIProxyAPI / v224 open-lovable / v244 OpenSandbox discipline: *corpus-first for a capability surface, explicitly not world-first, with the incumbent named in the row.*

**Capability, not form factor:** the engine choice sets the resource envelope (~30 MB vs 200 MB+), which is what makes one browser per agent task viable at concurrency — the same reasoning that carried v244 (execution substrate) and v215. That is what separates this from the declines at v222 (world-canonical ≠ world-first), v236 (form factor within a genre), v211 (technique) and v210 (domain).

**NO-MINT alternative recorded:** that Obscura is simply the second entrant in Lightpanda's already-named class. It loses because outside-corpus prior art does not create a corpus N=2 (the camofox precedent: *"Camoufox not a corpus subject; mentions ≠ recursion"*). Left for audit review. `inflation_check` HELD; per **§44 cl. 5**, §28 does none of the work.

### Instance-strengthening — recorded, not self-incremented

- **#18 B1-MCP** — first-party MCP server, 37 tools. ≈N=15 → **≈N=16**.
- **#19 19a** — non-Anthropic author.
- **#66 supply-chain** — **the corpus's strongest POSITIVE exemplar**, with pi v228. 12/12 actions SHA-pinned, read-only tokens, trusted-base policy, no-save PR caches, 0 git deps, reasoned `deny.toml`.
- **#83 honest-deficiency-disclosure — SPLIT.** Honest: "may differ from Chromium", "the tree is not rustfmt-clean", the ±10% noise floor, five reasoned RUSTSEC ignores, a CORS comment that names its own attack, `[patch.crates-io]` fork reasons. Not honest: four inconsistent speed figures, "Anti-detect: Built-in", an unexpanded `LP`.
- **#12** MIXED.

### Non-claims

- **NOT CONFIRMED Library-vocab #24** — #24 requires a product *"whose primary function is not being an agent tool."* Obscura's primary function **is** agent infrastructure. Clean discrimination.
- **NOT #52** — "10,000 stars" and the Trendshift badge are **page-stated** (§37.4). No velocity claimed or verified.
- **NOT #57** — no corpus subject is a dependency; Lightpanda is not a corpus subject.
- **NOT a new top-level pattern** (max #85). **NOT #68 / #88 / Domain-Vertical.**
- **Nothing installed, built, or executed. No third-party site contacted.**

---

## The ship's rule

> **v264** — a discipline stops at the edge of the team that holds it.
> **v265** — a discipline stops where the safe choice would COST something.
> **v266** — the discipline was already at the door, in a diff nobody opened.
> **v267** — **the discipline stops where the artifact stops being code.**

⭐⭐⭐ **And v265's rule earned an independent cross-organisation N=2 here** — `crates/obscura-mcp/src/http.rs:141-146` names the attack its own permissive CORS default allows (*"this stops a malicious local web page from driving the loopback MCP port"*) in the same comment that explains why the default stays permissive (*"so hosted dashboards keep working (issue #175)"*). Different author, different language, different domain, two ships later — and a **stronger** instance than v265's, because here the cost and the attack are written in the same comment block.

---

## Blunt

**This is the best-engineered subject in a long run, and I want to say that before anything else.** A pseudonymous developer and fifty-eight contributors built a working browser engine from scratch in four months — their own DOM, their own CSS cascade, their own layout and paint, 71,415 lines of it, V8 embedded for JavaScript, 189 CDP methods so Puppeteer connects unmodified, 1,264 tests that CI actually runs across four build configurations. The CI is the most carefully hardened I have read in 267 subjects: a written threat model at the top of the file, twelve GitHub Actions pinned to full SHAs, a read-only token, the security policy and dependency-ban list fetched from the *trusted base* so a pull request cannot weaken the check judging it, PR caches restored but never saved so a contributor cannot poison a release, and rename detection deliberately switched off because someone realised runtime code could otherwise be smuggled in through a documentation-shaped path. The SSRF gate revalidates every redirect hop. `deny.toml` distinguishes "unmaintained" from "vulnerable" and gives a reason per entry. The docs index passes the vault's inventory check perfectly — the first subject to do so. Unimplemented CDP methods return a proper `-32601` and there is a test asserting it. The vendored forks are declared with reasons and an upstream exit condition. The agent skill forbids hostname-specific rendering hacks and tells the agent not to read a pixel diff as a verdict.

Now the other half. Every one of those gates defends something a compiler reads. Nothing defends what a reader reads — and `ci.yml:86` says so out loud, routing every `*.md` change to zero checks. That exemption is where the whole claims surface lives, and the claims surface is where all the inflation is. Four different speed multiples across two documents, no two the same, and the one in the headline table matches none of the three benchmark rows printed 300 lines below it. "Anti-detect: Built-in" opposite a column reading "None", for a feature that needs a compile-time flag and a runtime flag, with no in-tree test against any real detection service. A `33/33` standard stated twice in `AGENTS.md` as mandatory, which the CI script computes, renders into a results table for a human to read, and never compares to 33 — the only thing that can fail it is a regression against a base that may itself be broken. A private working layer fenced by a sentence asking the agent not to commit it, with `.gitignore` at two lines and a root-owned `build.log` from `/root/obscura2/merge471` sitting committed in the tree as proof the sentence did not hold. And a row in the public CDP table labelled `LP`, expanded nowhere, which is Lightpanda's own vendor namespace — the AGPL project that did this first, in Zig, on the same JS engine and the same HTML parser, with the same positioning and the same markdown command, whose name appears zero times in this repository.

That last one is not theft and I want to be precise: implementing someone's protocol method is compatibility work, it helps users, and there is no licence issue. It is the *silence* that is the finding, and the silence is load-bearing, because the difference between these two projects is AGPL versus Apache-2.0 — which is the single most decision-relevant fact for anyone choosing between them, and the reason this one is the first subject in this class you could actually put in a product.

Five ships have now asked variations of "did you build a gate?" This one asks something narrower and more uncomfortable. These people built better gates than we have. They gated the compiler's input to a standard almost nobody meets, and then wrote four different numbers about their own performance on the one surface they had explicitly excused from checking — not out of carelessness, but because a wrong number in a table fails silently, in a stranger, months later, and no one has ever written a CI job for that. **Which of your own claims lives on the surface you exempted?**

For this vault, measured: the ship chain is still unmerged. `main` is at **v226**; **45 commits / 41 ships (v227 → v265)** were outstanding before this run, plus v266 and now v267.

---

## Suggested next action

**Review and merge the chain** — `main` is at v226; `wiki/v267-obscura` sits off the v266 tip (`0a6ff9a`), and v227 → v267 merge in order. **Not auto-merged.**

Then ⭐ **Rung 1 (30 min), and it is this ship's finding turned on the vault:** Obscura exempts `*.md` from every check, and that is where its claim drift lives. This vault is *entirely* `*.md`. The shim carries four Pattern Library counts, a streak, and a `§C-1`/`§C-2` split — all hand-maintained prose, none of it checked by anything. Write the counter that derives them, and wire it to the inventory script v263 found nobody invokes. **Three consecutive ships have now handed the vault the same lesson from three directions** (v263: a nine-clause script nothing runs; v266: a next-action sentence copied forward while the fact moved; v267: the one surface with no gate is the one carrying the claims).

⭐ **And a forward pointer for ~v268:** **Lightpanda** is now the obvious next subject — the AGPL incumbent of the class minted here, goal-relevant, and the one comparison this ship could not make from inside the repository.
