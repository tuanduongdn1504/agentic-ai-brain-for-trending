# (C) OpenMAIC — Verdict

**v284** · `THU-MAIC/OpenMAIC` · 2026-09-12 · MIT · HEAD `ebf665f3` (source verified, two clones, `diff -rq` clean both ways)

---

## Rating — GOAL-ALIGNED INCLUDE 3/4

| Axis | Call | Basis |
|---|---|---|
| **(a) Anthropic-affiliated / registered vendor-direct** | **FAIL** | Tsinghua MAIC. §41 is explicit: no name, heritage, locale or notability inference. Shipping an Anthropic-format `SKILL.md` and reading `ANTHROPIC_API_KEY` is **compatibility, not affiliation** (the v283 formulation). A shipped `vi-VN` locale does **not** rescue (§41 forbids locale inference; the v78 product-locale reading is superseded). |
| **(b) Goal relevance** | **STRONG** | 24 `SKILL.md` files incl. a distributable cross-harness skill package; an agent runtime built on **corpus v228 Pi**; a wired untrusted-content boundary; a three-point `fetch_url` origin gate; an 18-provider seam. Squarely goal-#1 agent substrate. |
| **(c) Substance** | **STRONG** | 543 commits · 94 authors · 2,929 files · 547,462 TS/TSX lines · 893 test files · 5 CI workflows · 4 GHSAs fixed with named external reporters · JCST 2026 paper. Active through the day before this wiki. |
| **(d) Pilotability** | **STRONG** | MIT. Several patterns lift by hand at zero cost; one is directly portable into the vault's own tooling. |

**Clean GA — no §40 invocation, no operator override.**

**Streak:** v283 `GA:140` → **`GA:141 · OG:13 [7 ov]`** — **64 consecutive goal-aligned ships v220→v284**.
**§35 CLEAR** — rolling window {v282 GA, v283 GA, v284 GA} = 0 OFF-GOAL.
**Override review: 24th consecutive discharge** (v153→v284 = 0 overrides; lifetime 10, 3 `[ceiling-override]` v146/v148/v152).

---

## MINT — **NO MINT**, by hand

**Counts 46 / 12 UNCHANGED. §C-1 13, §C-2 39 UNCHANGED.**

**Collision grep CLEAN** — `grep -rniE "openmaic|thu-maic|maic\.chat"` over the vault returns **zero** hits; standalone `\bMAIC\b` zero. First education-*platform* subject and first `THU-MAIC` author in 204 ships. (`Tsinghua` appears at v77 easy-vibe and v175 PilotDeck — different orgs, different subjects.)

### Four grounds

1. **Domain-not-capability** — course generation is a **domain**. Settled repeatedly and recently: **v212** (database GUI), **v196** (meetings), **v210** (AI companion/VTuber), **v197 / v191** (education). A corpus-first *domain* is a data-point, not a mintable class.
2. **⭐ v213 geti is the direct precedent** — Intel's computer-vision platform shipping a **first-party agent-skill suite** was ruled **NO MINT** on exactly this boundary. OpenMAIC is that shape: a product platform that ships first-party agent skills. Reading that row's own written definition is what decided it (the v262 demonstration of why §C-2 earns its keep).
3. **Not #24, not #18-B1 — verified, not assumed.** CONFIRMED Library-vocab #24 requires a **first-party MCP server**. OpenMAIC ships **none**: `git grep -c "McpServer"` over all `*.ts` returns **no matches** repo-wide, and `lib/web-search/doubao.ts:8` states they call the endpoint directly *"so it lights up as a one-click token-plan modality, **no MCP runtime**."* The `@modelcontextprotocol/sdk` dependency at `package.json:71` is not a server.
4. **Not world-first.** NotebookLM, Khanmigo, Coursera Coach and the wider AI-course-generator category precede in AI-generated learning content. The specific *multi-agent teacher-plus-AI-classmates delivery layer* may well be corpus-first, but **corpus-first-for-a-technique ≠ a mintable §C class** (the **v211 PixelRAG** discipline). ⚠️ A fleet web agent asserted "world-first"; it ran on Haiku and the claim is **explicitly not carried**.

### ⭐ Recorded, NOT executed — for the audit

- **A §C-2 N=1 candidate** — *"Multi-Agent Synthetic-Classroom Course Generator (AI teacher + AI peer personas as the delivery layer)"*. **Argued against** on all four grounds above. Recorded so a future N=2 has an anchor to collide with.
- **⭐⭐ Pattern #57 corpus-recursive, and a second lab on Pi.** `@earendil-works/pi-agent-core` is **corpus v228** (itself the v36 revisit). Pi is now depended on by **DeepSeek (v235)** and **Tsinghua MAIC (v284)** — recorded as instance-strengthening; an N-tally is an audit act, not a ship act.
- **⭐⭐⭐ The AI-provenance axis (v281's) gains an inverted pole.** v281 commits agent *instructions* and uses CI to *erase* agent *provenance*; v284 has **zero** agent-instruction files and keeps **1,275** trailers while `.gitignore`-ing the agent's local files. With **v243** (symlinked instructions + uncurated default trailers) that is a three-point axis worth formalising or rejecting.
- **v243's "trailers are a Claude Code default, left on" observation reaches N=2** — independently, at Tsinghua.
- **T3 Education boundary** — every prior education subject (v6, v74, v77, v191, v197, v220, v270, v280) was a **curriculum or textbook**. This is the first education **product/platform**. Whether T3 should split product-from-curriculum is an audit question.

---

## What is true, plainly

**The rule:** *every list derived from the tree is correct; every list a person typed is correct only where omitting an entry breaks something loudly.*

✅ **Derived and correct:** the SSRF call-site scanner (with floors that stop it passing vacuously) · the skill loader checked against the directory listing (**23 = 23**) · i18n key parity over `locales/` (**1,921 keys × 12 files**).

✅ **Typed but forced, and correct:** `postinstall` and `publish-packages.yml` each name all **6** packages — omit one and the build fails or the package never ships.

🔴 **Typed, unforced, and wrong:**
- `README.md:52` claims **"20 built-in skills"**; there are **23**, and there were **22** at the commit that wrote the line — **false the day it was typed**.
- `ci.yml` tests **4 of 6** packages. **`@openmaic/editor` (49 test files) and `@openmaic/renderer` (15) are built by two lists and tested by none — 64 test files, never executed.**

⭐ **And the irony is the repo's own:** its flagship test exists *because* a guard "was once applied at several API routes from **a hand-written list that drifted from the code**." They killed that class for one invariant by deriving from the tree — and the list deciding **what gets tested** is still hand-written, and has drifted.

✅ **Genuinely excellent, and worth saying clearly:** a wired untrusted-content policy (the direct inverse of v283's dead fence) · a `fetch_url` gate enforced before, during and after the fetch · AI-generated HTML sandboxed **without** `allow-same-origin` · exported HTML under a `connect-src 'none'` CSP · **2,726/2,726** lockfile entries hashed with no mirror override · four GHSAs fixed and credited to outside researchers · no `paths:` filter excluding anything from CI · and a test-header comment that diagnoses its own failure class better than most post-mortems.

⚠️ **Honest calibration:** "multi-agent orchestration (LangGraph 1.1)" is **two nodes and one conditional edge**; the real routing is **nine English rules in a prompt** whose own header says it *"mirrors the old /api/chat director"* — routing moved out of code and into the model. Legitimate, explicit, and not what the phrase suggests.

🔴 **Never:** cite the skill count from that README · assume the editor or renderer packages are covered by CI · treat the LGPL-3.0 `mathml2omml` vendoring as attributed at the top level (there is no `NOTICE`) · point this at private candidate data (it ingests documents and web-search results into a tool-calling LLM, and the origin gate protects *fetching*, not *what you uploaded*).

**Blunt:** a Tsinghua lab shipped, in six months, a course-generation platform with better security engineering than most funded products in this corpus — it found its own declared-but-unenforced guard, fixed it in every environment, and then wrote a 260-line tree-walking test with anti-vacuity floors so the gap can never come back. That test's header names the disease exactly: a hand-written list that drifted from the code. Then they wrote a README saying twenty when the directory held twenty-two, and a CI file that tests four of the six packages two other files in the same repo both list completely. Nothing here is careless. The difference between what is right and what is wrong is not effort, and it is not skill — it is whether leaving an entry out makes something turn red. Build lists go red. Test lists go green.
