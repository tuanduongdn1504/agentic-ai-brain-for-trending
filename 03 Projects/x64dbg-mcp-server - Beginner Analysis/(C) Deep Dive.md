# (C) x64dbg-MCP Server — Deep Dive

**Subject:** `duty1g/x64dbg-mcp-server` — *"MCP-powered agentic reverse engineering for x64dbg."*
**Wiki:** v278 · **Date:** 2026-08-25 · **Licence:** MIT · **Language:** Zig

---

## 0. Source verification

✅ **SOURCE VERIFIED.** Two independent clones, `diff -rq` clean in **both** directions (only `.git` internals differ). HEAD `c350c9290a05a3e02692f132839235593f3603a0`.

| Fact | Command | Value |
|---|---|---|
| Tracked files | `git ls-files \| wc -l` | **19** |
| Commits | `git rev-list --count HEAD` / `--all` | **16 / 16** |
| Roots | `git rev-list --max-parents=0 --all` | **1** (`a926c61`) |
| Merges | `git rev-list --merges --count --all` | **0** |
| Branches | `git branch -a` | **1** (`main`) |
| Tags | `git tag` | **2** — `1.0` and `v1.1` (inconsistent prefix) |
| Authors | `git log --all --format=%ae \| sort \| uniq -c` | **16 × `dzc0d3r@hotmail.com`** — one hand |
| Age | first → last commit | **2026-08-22 17:32 → 2026-08-24 11:42 = 3 days** |
| Zig source | `find -name '*.zig' \| xargs wc -l` | **6,396 lines** |

Largest files: `src/mcp/tools.zig` 3,584 · `src/core/mcp_server.zig` 938 · `src/core/config.zig` 737 · `src/main.zig` 467 · `src/core/bridge.zig` 456 · `src/mcp/json.zig` 142.

**85% of the repository by bytes is `logo.png`** (1,723,577 of 2,028,362).

---

## 1. What it is

A **native x64dbg plugin** — a `.dp64`/`.dp32` DLL loaded into the debugger's own address space — that runs an HTTP server exposing **80 MCP tools** so a coding agent can drive a live Windows debugging session: set breakpoints, single-step, read and patch process memory, disassemble, walk the call stack, dump modules, detect OEP on packed binaries.

Written in Zig with **zero dependencies**, cross-compiling to both x86 and x86-64 from any host. It resolves every x64dbg SDK symbol at runtime via `GetProcAddress`, so one source file serves both architectures.

It ships a `SKILL.md` workflow guide and, in its MCP `initialize` response, an `instructions` block of twelve numbered rules for the agent.

---

## 2. ⭐⭐⭐⭐⭐ The ship's rule

> **Everything in this repository produced by enumerating is right. Everything produced by summarising is wrong.**

With **zero gates of any kind**, what survives is exactly the defect class a human cannot catch by looking — and a human cannot count eighty things by looking.

### The enumerated things — all correct

| Artifact | Measured | Result |
|---|---|---|
| README tool table | 80 rows vs 80 source definitions | **exact 1:1**, zero missing, zero phantom |
| SKILL.md tool table | 80 rows, 80 unique names | **exact 1:1**, zero missing, zero phantom |
| `read_only` classification | `36 true + 44 false` | **= 80**, every tool classified |
| Event callbacks | `main.zig:101-122` | **exactly 22** — matches README's "22 Event Callbacks" |
| `mcp_tool_names` guard list | 28 names | all 28 are **real** tool names, zero phantoms |

Two independently hand-maintained 80-row tables in two documents, plus 80 hand-set boolean flags, plus a 22-row callback table — **240+ enumerated rows with zero drift in either direction.**

### The summarised things — wrong

| Location | Claim | Truth |
|---|---|---|
| `README.md:38` | "**84** MCP Tools" | **80** |
| `README.md:119` | "**72** MCP tools" | **80** |
| `SKILL.md:124` | "All **84** Tools Reference" | **80** |
| `SKILL.md:136` | `WaitForPause` `timeout?` default **10000** | `tools.zig:717` `"default":30000` — and the param is **`timeoutMs`**, not `timeout` |
| `SKILL.md:180` | `Disassemble` `count?` default **16** | `tools.zig:741` `"default":10` |
| `SKILL.md:144` | `GetEventLog` `count?` default **20** | `tools.zig:701` "default: **all**, max 64" — no such default exists |
| `README.md:226` | "Requires **Zig 0.16-dev** or later" | `build.zig.zon` `.minimum_zig_version = "0.14.0"` |
| `build.zig.zon` | `.version = "1.0.0"` | tag is `v1.1`; served `serverInfo` says `"1.1"` (`mcp_server.zig:849`) |
| `README.md:267` | "**No polling**" | the event path is a `Sleep(100)` loop; `SKILL.md:7` says "HTTP clients **must poll**" |

Three of six documented defaults in `SKILL.md` are wrong — **in the file whose entire purpose is to be loaded into an agent's context.** The three that are right (300000, 30000, 64) are the distinctive values; the three that are wrong (10000, 16, 20) are plausible round guesses. He typed the table from memory and got right the ones that were memorable.

### ⭐⭐⭐ The mechanism, and it is reproducible

`grep -c '\.name = "'` over `tools.zig` returns **84**. The real count is **80**. The difference is four register-name struct literals at `tools.zig:2792-2795` (`rcx`, `rdx`, `r8`, `r9`) that match the same pattern.

**80 + 4 = 84. The published number is exactly what the obvious command returns.**

Measured at every commit, the naive grep is always `real + 4`:

| commit | real tools | naive grep | README "Features" | README header | table rows |
|---|---|---|---|---|---|
| `a926c61` root | **51** | 55 | 51 ✅ | 51 ✅ | 51 ✅ |
| `9e3699e` tag `1.0` | **71** | 75 | 71 ✅ | 71 ✅ | 71 ✅ |
| ×3 mid commits | 71 | 75 | 71 ✅ | 71 ✅ | 71 ✅ |
| **`eb63792` tag `v1.1`** | **80** | **84** | **84** ❌ | **72** ❌ | **80** ✅ |
| `c350c92` HEAD | 80 | 84 | 84 ❌ | 72 ❌ | 80 ✅ |

For the first five commits all three numbers agreed **exactly**, three times over. The divergence happened in **one commit** — the release commit — and in **two directions at once**: "84" from a contaminated command, "72" from bumping 71 by one.

⚠️ **This is not laziness. It is a number that *feels derived*.** A count produced by a command that silently over-counts is worse than a guess, because it carries the authority of measurement. **I ran that exact grep myself, got 84, and believed it** until I looked at the matches.

---

## 3. Security

### 🔴 The v1.0 window: 23 h 35 m 42 s of released, unauthenticated RCE

At tag `1.0` (`9e3699e`, 2026-08-22 18:08:35):

- **Zero authentication anywhere.** Extent: every `.zig` file in the tree at that commit. The only hits for `Bearer|auth_token|Authorization` are the CORS `Allow-Headers` string and `std.mem.tokenizeAny`.
- **Default bind `0.0.0.0`** — in *two* places: `mcp_server.zig:35` and `config.zig:167` (`const default_ip = "0.0.0.0"`).
- **71 tools**, including all seven of the most dangerous: `ExecuteDebuggerCommand`, `WriteMemToAddress`, `AllocateMemory`, `Assemble`, `LoadBinary`, `AttachProcess`, `DumpMemory`.

Auth arrived at `e1daba0`, **2026-08-23 17:44:17** — a window of **23 h 35 m 42 s**. The download-count badge went up at `b658091` (2026-08-22 19:12), **64 minutes into that window**, which is only meaningful if a Release with binaries already existed.

The author named it himself. The commit subject is: *"Add Bearer token authentication to **prevent RCE on 0.0.0.0**"*.

### ⭐⭐⭐ And 149 seconds later he deleted his own escape hatch

`e1daba0` (17:44:17) shipped **deliberately optional** auth — `if (auth_token_len > 0) { … }` — and documented it at `README.md:219`:

> *"Leave the token empty to disable auth (safe for `127.0.0.1`)."*

`ensureToken` (`config.zig:250`) already auto-generated a token, so the default state was protected. **This was a documented policy, not a fail-open bug.**

`1aad0f8` (17:46:46) — **149 seconds later** — made auth unconditional by moving the `auth_token_len > 0` test *inside* the comparison, so an empty token now authorises nothing. The README line was rewritten to *"required on every request."*

**That is a policy change, not a bug fix, and it runs in the rare direction: most projects accumulate opt-outs; he removed one two minutes after shipping it.** On a tool with arbitrary memory write, a user-disableable safety control is not a defensible default, and he worked that out on reread.

### ✅ What is actually correct

- **Token generation is sound crypto.** `config.zig:139` declares `SystemFunction036` — the real `advapi32` export name for **RtlGenRandom**, the Windows CSPRNG. `generateToken` (`:141-149`) takes 16 raw bytes → 32 hex chars = **128 bits of entropy**.
- **Auth fails closed.** `mcp_server.zig:460`: `auth_token_len > 0 and bearer.len == auth_token_len and std.mem.eql(...)`. An unset token authorises nothing.
- **No buffer overflow in the receive path.** `wsRecv` (`:440-455`) loops `while (result.len < result.buf.len)` into a fixed `[65536]u8` and clamps with `@min`. Structurally bounded. Oversized requests are **silently truncated**, not rejected — a correctness issue, not a memory-safety one.
- **No JSON injection.** `json.zig:76-77` escapes `"` and `\` **first** in the switch. A hostile binary's bytes cannot break out of a JSON string.
- **`defer parsed.deinit()`** at `mcp_server.zig:523` and `:614`, immediately after both `parseFromSlice` calls. No leak.
- **Error-handling hygiene:** across all of `src/` — `catch unreachable` **0**, `catch {}` **0**, bare `unreachable` **0**, `@panic` **1**. 52 × `catch return` — a coherent *never take down the host* discipline.

### 🔴 The data race

`build.zig:15` and `:43` set **`.single_threaded = true`** for both modules. The code creates threads at **three** sites: `mcp_server.zig:266` (server), `mcp_server.zig:395` (**one per accepted connection, unbounded**), `config.zig:408` (dialog).

**`grep -rn -iE "mutex|CriticalSection|atomic|Interlocked|volatile" src/` returns EMPTY.** Extent: all `.zig` files under `src/`.

The shared mutable state is the pending-events ring buffer at `mcp_server.zig:87-90` — `pending_events`, `pending_event_lens`, `pending_head`, `pending_count`.

- **Producer:** x64dbg's own debugger thread, via `main.zig:349,375,423,428,433,438` → `notifyEvent` → `pendingPush` (`:194-195`).
- **Consumer:** every HTTP client thread, via `pendingDrain` / `pendingDrainToBuffer`.

Unsynchronised producer/consumer on a ring buffer, with N consumers. `pending_count -= 1` racing a concurrent decrement **underflows a `usize`** — and the README's own build command is `zig build -Doptimize=ReleaseSafe` (`README.md:229`), where integer overflow is **checked and panics**. A panic in a DLL inside x64dbg **takes the debugger down**, mid-session.

And `.single_threaded = true` makes this worse, not better: it tells the compiler no other thread exists.

The queue also **silently drops the oldest event** when full at 16 (`:120-123`), while `SKILL.md:23` tells the agent *"Always read these"* without mentioning that events can vanish.

### 🟡 Precise, not inflated

- **`std.mem.eql` is not constant-time** (`:460`) — but it runs only after a length check, and it is a 128-bit token over HTTP with network jitter. **Low.**
- **`Access-Control-Allow-Origin: *`** on every response (`:845`), and `OPTIONS` returns 204 **before** the auth block (`:447-451`). That is *correct* CORS — a preflight cannot carry `Authorization`. The real consequence is that **any web page can fingerprint the server** without a token. **Modest.**
- **`DumpMemory` / `DumpModule` do not constrain `filePath`** (`tools.zig:2832-2847`; the path is interpolated into `savedata "{s}", …`), so an authenticated caller can write anywhere x64dbg can write, and a `"` in the path can break the quoting. **But this is no privilege escalation** — the same caller already holds `ExecuteDebuggerCommand`. Code hygiene, not a boundary crossing.
- **`isMcpToolName` guards 28 of 80 tools** (`tools.zig`, `mcp_tool_names`). Introduced fresh at `eb63792`, all 28 names real — a deliberate judgment sample against a known LLM failure mode, not drift. Nothing keeps it complete as tools are added.

### ⚠️ The escaping gap, stated exactly

`json.zig:72-90` escapes exactly five characters: `"`, `\`, `\n`, `\r`, `\t`. RFC 8259 requires **all** of U+0000–U+001F. So **29 control bytes pass through raw**, as does invalid UTF-8.

This tool reads bytes **from a debugged process's memory** — `GetStrings`, `SearchForStrings`, `GetImports`, `GetExports`, `ListSymbols`. A binary containing a `0x00`–`0x1F` byte in a symbol or DLL name produces **malformed JSON**. Not an injection; a denial of the tool call.

### ⭐⭐⭐⭐ The hazard nobody documents

Even with perfect escaping, **the content of an analysed binary flows into the analyst's agent context.** `GetStrings` on a malware sample faithfully delivers whatever that sample's author wrote — including text shaped like instructions.

The disclaimer (`README.md:272-278`) covers legal misuse and network exposure. Neither it nor `SKILL.md` mentions that **the artifact under analysis is hostile input to the agent doing the analysis.** For an agentic reverse-engineering tool that is the defining hazard, and it is unaddressed.

### 🔴 And the instruction that undercuts the annotations

`mcp_server.zig:715` ships MCP-conformant `readOnlyHint` / `openWorldHint` annotations for **all 80 tools** — 36 read-only, 44 mutating. That is the protocol field whose entire purpose is letting a client decide when to interrupt and ask.

`mcp_server.zig:692`, twenty-three lines earlier in the same function's `instructions` string, tells the model:

> *"Never wait for user confirmation — monitor actively."*

and at rule 4: *"NEVER go idle or ask the user…"*

Read charitably these are **liveness** instructions about not idling while polling for debugger events, and that is almost certainly the intent. But they are delivered unqualified, as CRITICAL RULES, to a model holding 44 mutating tools including `WriteMemToAddress`. **He classified all 80 tools correctly — an enumerated task — and then wrote one summary sentence that reads across the whole surface.** The same pattern again.

---

## 4. The gate census: zero

Full extent — `ls -a` at root and every directory, `grep` for test/lint/ci/fmt/workflow across all 19 tracked files, `grep -rn '^test "'` across all `.zig` files, `grep addTest\|b.step` in `build.zig`:

- **No `.github` directory at all.**
- **Zero test blocks.** Zero `addTest`. No custom build step.
- No linter, no formatter, no CI, no release workflow, no provenance.

**6,396 lines of Zig, running inside a debugger's address space, parsing network input, giving arbitrary memory write to remote callers — and the only thing that verifies any of it is `zig build` succeeding.**

This is more extreme than v276, which at least *had* 349 tests and wired one.

---

## 5. Provenance

- Author **`duty1g`** / `dzc0d3r@hotmail.com` — pseudonymous, with a disclosed presence (`duty1g.online`, `@duty_1g`, self-styled Red Team / Reverse Engineering). **NOT Anthropic** (§41).
- **Zero AI-authorship trailers** in all 16 commits. **Zero `Anthropic`/`Claude` hits across all 19 tracked files** (extent stated) — an MCP server for coding agents that names no agent at all.
- ✅ **`bridge.zig:1-2` credits the x64dbg SDK by source URL** (`.../src/bridge/bridgemain.h`). Honest attribution.
- ⚠️ **`SKILL.md` has no YAML frontmatter.** It uses Anthropic's Agent Skill *filename* without Anthropic's Agent Skill *format* — a skill loader would not register it. It is a workflow guide wearing the standard's name.
- ⚠️ **Licence interaction, facts only:** x64dbg is GPLv3; this plugin is MIT and re-declares SDK constants and structs in Zig, resolving every symbol at **runtime** via `GetProcAddress` rather than linking. No `NOTICE`, no compatibility statement. Stated as facts; no legal conclusion drawn.
- `bridge.zig:327` — the codebase's single `@panic`, on a missing bridge symbol. It distinguishes required (`resolve`) from optional (`resolveOptional`) symbols, which is thoughtful; but a required-symbol miss **panics inside x64dbg**. That failure lives on a boundary he does not own — x64dbg's export table — and he cannot test it, because it depends on which x64dbg build the user has.

---

## 6. Method

**Fleet:** 12 dimensions × (read → adversarially refute) = **77 agents, 75 completed, 2 errors, 10 empty, ~9.18M subagent tokens, ~825 s.**

The adversarial layer earned its cost — and so did checking it.

**It corrected me.** I read `e1daba0` as fail-open auth caught in 149 seconds. Its refuter found `ensureToken` already present at that commit and `README.md:219` documenting the opt-out explicitly. **I verified both myself and rewrote the finding**: it was a documented policy, deliberately reversed. That reframing is more interesting than my version and it exonerates the author.

**And I had to refute the fleet.** Discarded after my own checks:

- A **HIGH**-severity "malformed JSON — trailing comma in the `initialize` capabilities object." `json.zig:26` **explicitly strips a trailing comma** before writing `}`. The output is valid. Refuted by reading the function the claim depended on.
- *"released on npm"* — there is no npm anywhere (extent: all 19 tracked files). This is a Zig project shipping plugin DLLs via GitHub Releases.
- *"2,023 lines"* — that is **v277's** figure, not this subject's 6,396.
- *"page_allocator memory leak accumulates unbounded pages"* — `defer parsed.deinit()` sits on the very next line after both `parseFromSlice` calls.

**Confirmed from the fleet after my own verification:** the `WaitForPause` / `Disassemble` / `GetEventLog` default drift, and `isMcpToolName` covering 28 of 80.

### ⚠️ My own errors, all caught by re-measurement (§43.1)

1. **`grep -c '.name = "'` → 84.** Believed it. The real count is 80; four register literals matched. **The author's published number has the same origin.**
2. **`grep -c` of `C##` markers in the registry → 65**, against v2.8's stated 51 live rows — contaminated by prose references like *"from §C row C40"*. The anchored form (`^| **C##**`) gives 61 physical rows.
3. **`RtlGenRandom` → zero hits**, and I nearly recorded the commit message as unsupported. It is exported as `SystemFunction036`; the commit message was accurate and I was not.
4. **The collision check's controls returned zero** — `MCP` => 0 files in a 278-wiki MCP corpus. `ARG_MAX` blew on 23,289 paths and the command failed silently. **The controls caught it; the subject terms alone would have "confirmed" corpus-first on a broken command.** Redone with `xargs -0`.

**Extent not overcome:** no network — GitHub Releases contents, download counts, star velocity, and world-first priority are all **UNVERIFIED**. Windows-only artifact, **never built and never run** — every behavioural claim is from source reading. `python3` is SIGKILLed in this sandbox (D41); line-based tools only. This git lacks `--show-current`.

---

## 7. Corpus placement

**Corpus-first at verified full extent** — 23,289 markdown files, controls firing hard (`MCP` 6,246 · `Claude Code` 5,714 · `agent` 11,455):

| term | files |
|---|---|
| `x64dbg` · `duty1g` · `dzc0d3r` · `x32dbg` · `OllyDbg` | **0** |
| **`Ghidra`** | **0** |
| **`IDA Pro`** | **0** |

**In 277 prior wikis the corpus has never covered a binary reverse-engineering tool.** The two canonical RE platforms return zero.

### ⭐ ONE MINT — §C-2 row **C58**

> **Agent-First Live-Debugger / Binary Reverse-Engineering Perception+Control Layer — delivered as a native in-process plugin inside a third-party debugger's own address space.**

**N=1.** §C-2 **38 → 39**. §C-1 **13 unchanged**. Counts **46/12 unchanged**.

**Grounds:** (1) corpus-first at the extent above; (2) it is a **capability**, not a domain, product or technique — it passes the meetily v196 / PixelRAG v211 / TimesFM v193 tests by giving an agent an ability no prior subject provides; (3) **direct seven-row precedent** — C30 web/social, C35 mobile simulator, C37 video production, C43 video editing, C45 job-search, C46 Office documents, C48 web crawl, each minted at N=1 as *"corpus-first for the surface, NOT world-first"*; (4) structurally distinct **within** that family — all seven siblings are external processes, CLIs or skills, while this runs **in-process inside a third-party host via that host's own plugin ABI**.

**DECLINED — CONFIRMED #24** *"Product-First Native Application Retrofitted with a First-Party MCP Server."* Decisive **on the row's own written definition**, which requires *"whose **maker** also ships that same application's own MCP server"* and explicitly excludes *"a third-party wrapper."* `duty1g` is not x64dbg's maker. *(The v262/v277 discipline: reading the row's definition changed the answer.)*

⚠️ **NOT world-first.** MCP servers for Ghidra and IDA Pro are widely known prior art — and notably x64dbg's own creator authored `ida-pro-mcp`. **Knowledge-based, UNVERIFIED without network**, and flagged for the audit.
⚠️ **§28 was not a ground for any decline** (§44.5).

**RECORDED, not self-promoted** (a promotion is an audit act): **Pattern #18 sub-archetype B1-MCP ≈N=15 → ≈N=16.**

**Tier:** T4 Plugin/Extension.

---

## 8. The ladder

> v273 — a check is only as permanent as **the place you put it**
> v274 — a claim is safe when a gate covers it **or a habit covers it**
> v275 — a check cannot survive **someone with standing to overrule it**
> v276 — the reliability of a number is predicted by **its audience**
> v277 — **a written invariant with no gate is a wish**
> **v278 — WITH NO GATES, WHAT GETS CAUGHT IS EXACTLY WHAT FITS IN ONE PERSON'S HEAD AT ONE MOMENT.**

He found an RCE in his own released binary in a day. He reversed a security policy 149 seconds after publishing it. Both are single-glance defects — reachable by rereading what you just wrote.

He still ships three wrong tool counts, three wrong parameter defaults, a `single_threaded = true` contradicting three `CreateThread` calls, and an unsynchronised cross-thread ring buffer. Those require holding eighty items, or two threads, or two files, at once.

**Gate what does not fit in one head. Do not bother gating what a careful reader catches on reread.**

And v277's rule still appears here, once: `bridge.zig:327` panics on a symbol x64dbg may or may not export — the one failure he genuinely could not have tested.
