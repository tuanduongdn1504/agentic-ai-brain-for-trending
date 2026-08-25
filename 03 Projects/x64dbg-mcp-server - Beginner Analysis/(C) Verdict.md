# (C) x64dbg-MCP Server — Verdict

**v278 · 2026-08-25 · `duty1g/x64dbg-mcp-server` · MIT · Zig · HEAD `c350c929`**

---

## Rating

**GOAL-ALIGNED INCLUDE — 3/4**

| Axis | Call | Basis |
|---|---|---|
| **(a)** Anthropic / registered vendor-direct | **FAIL** | `duty1g` (`dzc0d3r@hotmail.com`) is a pseudonymous individual. **Zero `Anthropic`/`Claude` hits across all 19 tracked files**; zero AI trailers in 16 commits. §41 — no name, heritage or notability inference. |
| **(b)** Goal relevance | **STRONG** ⚠️ *MODERATE-reviewable* | An MCP capability layer that hands a coding agent a genuinely new ability, plus a `SKILL.md` and a server-side `instructions` block both designed around **how the model actually fails**. Squarely the goal-#1 agent-capability substrate. ⚠️ The *domain* (Windows binary RE) is off the operator's own domain — the OFF-GOAL reading is defensible and recorded. |
| **(c)** Substance | **STRONG** | 6,396 lines of verified Zig; coherent architecture; correct CSPRNG; fail-closed auth; runtime symbol resolution with a required/optional split; dual-arch cross-compile from any host. |
| **(d)** Learning value | **STRONG** | A corpus-first domain, a new §C-2 class, and the sharpest counting finding in the run. |

**No §40. No override.** Streak `GA:134` → **`GA:135 · OG:13 [7 ov]`** — **58 consecutive goal-aligned ships v220→v278**. **§35 CLEAR** ({v276, v277, v278} = 0 OG). **Override review: 18th consecutive discharge.** Tier **T4 Plugin/Extension**.

---

## Mint

**ONE MINT — §C-2 row C58.** §C-2 **38 → 39** · §C-1 **13 unchanged** · counts **46/12 unchanged**.

> **Agent-First Live-Debugger / Binary Reverse-Engineering Perception+Control Layer — delivered as a native in-process plugin inside a third-party debugger's own address space.**

Corpus-first at full verified extent: **23,289 markdown files**, controls firing (`MCP` 6,246 · `Claude Code` 5,714), with `x64dbg`, `duty1g`, **`Ghidra`** and **`IDA Pro`** all at **0**. In 277 prior wikis the corpus has never covered a binary-RE tool.

**Declined CONFIRMED #24** on its own written definition — it requires *"whose **maker** also ships that same application's own MCP server"* and excludes *"a third-party wrapper."* duty1g is not x64dbg's maker.

⚠️ **NOT world-first** (Ghidra/IDA MCP servers precede; x64dbg's own creator authored `ida-pro-mcp`) — knowledge-based, **UNVERIFIED without network**, flagged for the audit. §28 was not a ground for any decline (§44.5).

**Recorded, not self-promoted:** Pattern **#18 B1-MCP ≈N=15 → ≈N=16**.

---

## The one sentence

> **Everything in this repository produced by enumerating is right; everything produced by summarising is wrong — because with zero gates, what gets caught is exactly what fits in one person's head at one moment.**

240+ hand-maintained rows across two documents and three tables carry **zero drift**: the README's 80-row tool table and SKILL.md's 80-row tool table are both an *exact* 1:1 with the 80 source definitions, no phantoms and no omissions in either direction; all 80 tools carry a hand-set `read_only` flag (36 + 44 = 80); the 22 event callbacks are exactly 22, matching the README.

And in the same two files: **"84 MCP Tools", "72 MCP tools", "All 84 Tools"** — three numbers, none of them 80 — plus three of six documented parameter defaults wrong, a Zig version that contradicts the manifest, and a version string that disagrees with its own tag.

⭐⭐⭐ **The mechanism is reproducible and I reproduced it.** `grep -c '.name = "'` returns **84** because four register literals at `tools.zig:2792-2795` match the tool pattern. **80 + 4 = 84.** I ran that command, got 84, and believed it. *A count produced by a command that silently over-counts is worse than a guess, because it carries the authority of measurement.*

---

## What is genuinely good

- ⭐ **`1aad0f8`: he deleted his own escape hatch in 149 seconds.** `e1daba0` shipped *documented* optional auth (`README.md:219`: *"Leave the token empty to disable auth"*). Two and a half minutes later he made it unconditional. **A policy reversal, not a bug fix, and in the rare direction** — most projects accumulate opt-outs.
- ✅ **Correct crypto**: `SystemFunction036` = RtlGenRandom → 16 bytes → 32 hex = **128 bits**, auto-generated, persisted.
- ✅ **Fails closed** (`mcp_server.zig:460`).
- ✅ **No JSON injection** — `"` and `\` escaped first (`json.zig:76-77`).
- ✅ **No buffer overflow** — `wsRecv` is structurally bounded into a fixed 64 KB buffer.
- ✅ **Hygiene**: zero `catch unreachable`, zero `catch {}`, zero bare `unreachable`, one `@panic`; `defer parsed.deinit()` on both JSON parses.
- ✅ **MCP-conformant `readOnlyHint` / `openWorldHint` on all 80 tools.**
- ✅ **Credits the x64dbg SDK header by URL** (`bridge.zig:1-2`).
- ⭐ **`isMcpToolName`** — a guard built against a *real observed LLM failure mode* (the model passing tool names to `ExecuteDebuggerCommand`), and `SKILL.md`'s "Common Mistakes" table does the same thing in prose.

## What is wrong

- 🔴 **Tag `1.0` shipped a released, downloadable, badge-advertised plugin with ZERO authentication, binding `0.0.0.0`, exposing 71 tools including `ExecuteDebuggerCommand` and `WriteMemToAddress` — for 23 h 35 m 42 s.** The author named it: *"prevent RCE on 0.0.0.0"*.
- 🔴 **A live data race.** `.single_threaded = true` (`build.zig:15,43`) while three sites call `CreateThread` — one **per connection, unbounded**. `mutex|CriticalSection|atomic|Interlocked|volatile` returns **empty across all of `src/`**. Producer is x64dbg's debugger thread; consumers are the HTTP threads; the ring buffer at `mcp_server.zig:87-90` is unprotected. A `pending_count` underflow **panics under the README's own `ReleaseSafe` build — inside x64dbg**.
- 🔴 **Zero gates.** No `.github`, zero test blocks, no `addTest`, no linter, no CI. Extent: `ls -a` everywhere + grep over all 19 files + all `.zig` files.
- 🔴 **`SKILL.md`'s defaults are wrong 3 of 6** — in the file built to be loaded into an agent's context. `WaitForPause` is documented as `timeout?` default 10000; it is `timeoutMs`, default **30000**. An agent following the doc passes an ignored key and blocks for 30 s expecting 10.
- ⚠️ **`mcp_server.zig:692` tells the model *"Never wait for user confirmation"*** — 23 lines from the `readOnlyHint` annotations whose whole purpose is helping a client decide when to ask. Charitably a liveness rule about not idling; written unqualified to a model holding 44 mutating tools.
- ⚠️ **The analysed artifact is hostile input to the analyst's agent.** `GetStrings` on a malware sample pipes that sample's own bytes into the agent's context. The disclaimer covers legal misuse and network exposure and never mentions this. For an agentic RE tool it is *the* hazard.
- ⚠️ 29 of 32 control bytes unescaped (`json.zig:72-90`) → malformed JSON from hostile binary content. **Not** an injection.
- ⚠️ `isMcpToolName` guards **28 of 80**. `DumpMemory`/`DumpModule` do not constrain `filePath` — but that is **no privilege escalation**, since the caller already holds `ExecuteDebuggerCommand`.
- ⚠️ `SKILL.md` has **no YAML frontmatter** — Anthropic's skill filename without Anthropic's skill format.

---

## Pilot

⚠️ **READ-AND-BORROW. INSTALL NOTHING — and here it is not even possible.** x64dbg is Windows-only; this machine is darwin. Beyond that: a **3-day-old, single-author, zero-test** plugin that grants network callers arbitrary process memory write.

**The vault item completes a six-part arc** — v273 *where* to put the check → v274 *how* to write its clauses → v275 *what to aim it at* → v276 *which claims rot* → v277 *which invariants you only wrote down* → **v278 which defects a human cannot catch at all.**

Add **clause (g)** to `(C) proposed-verify-vault-inventory.sh`: *every count stated in vault prose must be emitted by the command that derives it, with the command shown; and every counting pattern must be anchored (D47), because an unanchored `grep -c` silently over-counts.*

⭐ **This is not borrowed theory — it is the vault's own v259 incident.** That audit hand-reconciled the §C row count through 50, then 52, before landing on 51, for exactly this reason. **I hit it twice more today** (84-not-80; 65-not-61). A stranger's three-day-old repository reproduced the vault's counting failure, from the same command.

🔴 **NEVERs:** never install · never cite "84 tools" or "72 tools" (it is **80**) · never trust `SKILL.md`'s defaults · never run tag `1.0` binaries · never expose past loopback (the default is `0.0.0.0` in **two** places) · never assume `readOnlyHint` gates anything — it is advisory and this server enforces nothing · never let an agent read `GetStrings` output from an untrusted sample without treating it as hostile text.

---

**Shipped on `wiki/v278-x64dbg-mcp-server` off the v277 tip (`df09808`); NOT auto-merged.**
