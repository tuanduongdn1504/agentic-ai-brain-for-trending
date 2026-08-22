# (C) TencentDB Agent Memory — Deep Dive

**Wiki v265** · subject `TencentCloud/TencentDB-Agent-Memory` · shipped 2026-08-22 · routine v2.8
**Verdict:** GOAL-ALIGNED INCLUDE 3/4 · **NO MINT** · counts 46/12 UNCHANGED

---

## 0. Source verification

Two independent clones, identical HEAD `97f94654280b2932c35ba4806a491999ed244cc9`, `diff -rq` clean **both** ways. No git-LFS. Nothing executed except one local, read-only `git` experiment described in §3 (reverted; clones re-verified identical afterwards).

| Fact | Value | How derived |
|---|---|---|
| HEAD | `97f9465` (2026-08-15, `kentyhuang <kentyhuang@tencent.com>`) | `git log -1` |
| **Default branch** | **`feat/server_team`** — *not* `main` | `git branch -r` → `origin/HEAD -> origin/feat/server_team` |
| Tracked files | 930 | `git ls-files \| wc -l` |
| TypeScript | 639 `.ts` + 59 `.tsx` | extension tally |
| Lines (ts/tsx) | **183,339** across 5 dirs | `wc -l` per dir |
| **Test files** | **0** | see §4 |
| Tags | 13 (`v0.1.4` … `v2.0.1-beta.2`) | `git tag` |
| Licence | **MIT** (Tencent) | `LICENSE` |

**Package sizes:** MemoryCore 300 files / 95,918 lines · MemoryProxy 161 / 41,719 · MemoryPanel 160 / 30,535 · MemoryKnowledge 58 / 11,289 · sdk 19 / 3,878.

---

## 1. What it is

Tencent Cloud's MIT-licensed **agent memory platform**: a self-hosted memory server that gives AI coding agents — **Claude Code**, DeepSeek Harness, Codex, CodeBuddy, WorkBuddy, Hermes, OpenClaw — a shared, team-scoped, persistent memory.

Four **Memory Assets**, unified under one ownership/ACL/versioning model:

- **Chat Memory** — conversations distilled through **L0 Conversation → L1 Atom → L2 Scenario → L3 Core/Persona**
- **Skill** — reusable procedures extracted from completed work, with versions and trigger boundaries
- **Wiki** — documents turned into linked structured pages *(README: "Inspired by Karpathy's LLM knowledge base")*
- **CodeGraph** — symbols, files, call relationships, impact paths

The integration model is the thesis: **"One Proxy, unchanged protocol, zero-code integration — point the Agent's base URL to the Proxy and it's done. No plugin, hook, or MCP server is required."**

---

## 2. ⭐⭐⭐ HEADLINE 1 — Three disjoint histories, and the default branch is the newest orphan

`merge-base origin/main origin/feat/server_team` → **no common ancestor.**

| Ref | Commits | Root commit | Layout |
|---|---|---|---|
| `main` | **108** | `7a5fce9` 2026-04-09 *"feat: init Agent-Memory"* | flat `src/` |
| `feat/server` | 20 | `36b0537` = the `v1.0.0-beta.1` release | flat `src/` |
| **`feat/server_team` (DEFAULT)** | **17** | `41444344` = the **`v2.0.0-beta.1` release** | `MemoryCore/…` monorepo |

Three roots, verified by `git rev-list --max-parents=0 --all`. `git diff --stat origin/main origin/feat/server_team` = **954 files changed, 209,564 insertions, 16,188 deletions**. `main` has **zero** files under `MemoryCore/`.

⇒ **Each major version was published as a fresh orphan branch, not a continuation.** A plain `git clone` therefore reports **17 commits and 4 authors, all `@tencent.com`**. The repository actually holds **148 commits and 26 authors**.

**Commit counts re-verified three ways** after a fleet verifier disputed them: `rev-list --count`, `log --oneline | wc -l`, and `log --format='%H' | wc -l` all return **108** for `main`. The verifier's "50" is not reproducible here.

### 2.1 What that costs — 21 stranded contributors

`comm -23` of the author sets: **24 authors on `main`, 4 on the default branch, and 21 who have committed *only* to `main`** — Akhilesh Arora, Andy He, Maxwell-Code07, MicroGrey, Porun, Radian, Rocke Dong, Ruida Xu, Siren.W, Willow Lopez, YOMXXX, **Ziyang Guo**, fei121, honchow, jackson-jia-914, jackyangjie, noFloat, yuanrengu, zhangxiaoshuai, 李冠辰, 杨俊杰.

`main`'s log shows a real community programme — multiple commits tagged **`[good first issue]`**, PR numbers into the 900s. **None of that history is on the branch the world clones.**

⚠️ **The fair correction, which I made against my own first reading:** the *files* mostly survived — `hermes-plugin/`, `openclaw.plugin.json` and the rest exist on the default branch under a `MemoryCore/` prefix. This is not lost code. It is lost **history, attribution, and — as §5 shows — one lost security fix.**

### 2.2 The internal mirror, visible in the log

- `d0588e2` / `915d613` — *"Merge remote-tracking branch **'github/feat/server_team'** into **public_server_team**"*
- `ce93615` — **`内部更新package.json`** ("internal update package.json")

⇒ the public repo is an **export of an internal one**: community PRs are pulled *in*, and releases are pushed *out* as squashed orphans. §6 shows what that export breaks.

---

## 3. ⭐⭐⭐ HEADLINE 2 — A CI guard that reports PASS on the exact change it exists to block. Proven by running it.

One workflow exists: `.github/workflows/pr-ci.yml`. Two lines decide everything:

- `:4-5` → `on: pull_request: branches: [main]`
- `:12-14` → `defaults: run: working-directory: MemoryCore`

**The default branch is `feat/server_team`.** A PR opened against it — GitHub's default base for every contributor — matches no trigger and runs **nothing**. Meanwhile `main`, the only branch the workflow fires on, has **no `MemoryCore/` directory at all**.

⇒ **The CI is aimed at a branch whose layout it does not fit, and fits a branch it is not aimed at.**

Jobs: `install`, `pack`, `manifest`, `size`, `isolation`. **There is no test job.**

### 3.1 The isolation guard, run rather than read

`isolation` runs `scripts/ci/check-skill-queue-isolation.sh` (139 lines, present on the default branch, **absent from `main`**). It defines red-line files:

```
FORBIDDEN_FILES=( "src/core/state/types.ts" "src/core/state/local-backend.ts" "src/services/pipeline-worker.ts" )
```
tested with `grep -qx` — an **exact whole-line match**. On this branch those files live at `MemoryCore/src/…`, and `git diff --name-only` always emits **repo-root-relative** paths.

I appended one line to `MemoryCore/src/core/state/types.ts` — the **first entry on the forbidden list** — and ran the guard exactly as CI does:

```
--- git diff --name-only, from inside MemoryCore ---
MemoryCore/src/core/state/types.ts
--- guard, MODE=working-tree ---
[skill-queue-isolation] BASE_REF=origin/main MODE=working-tree
[skill-queue-isolation] PASS
GUARD EXIT=0
```

⇒ **A guard that runs, prints `PASS`, and is checking a path prefix that has not existed since the v2 restructure.** Red-lines 2 and 3 fail identically (`case src/integrations/redis/*`, `grep -E '^src/core/skill/'` — both anchored to the old root).

Three independent ways for one guard to never protect anything: **the script is missing on the branch CI fires on; CI never fires on the branch the script is on; and where it does run, its paths cannot match.**

⚠️ One hypothesis of mine **refuted** by that same run: I expected bash 3.2 to fail on the empty-array `set -u` path. It did not. Not claimed.

### 3.2 The remediation pointer is itself dangling

The guard's failure message (`:134`) ends:
> `参考 ADR：docs/design/2026-06-16-skill-extract-queue.md / 2026-06-16-skill-storage-adapter.md`

Neither has **ever existed on any commit on any ref** (searched every tree of every commit on `--all`). ⇒ **The broken pointer is protected from discovery by the broken gate** — the one moment a developer would read that line is a moment the guard cannot produce.

---

## 4. ⭐⭐⭐ HEADLINE 3 — Four vitest configs, five test scripts, zero tests. The fourth species of gate.

| | `main` | default branch |
|---|---|---|
| Test files | **7** (4 `.test.ts` + 3 Python under `hermes-plugin/…/tests/`) | **0** |
| `vitest.config.ts` | 2 | **4** |
| `"test": "vitest run"` scripts | — | **5** |

`passWithNoTests` appears **nowhere** in the tree ⇒ `npm test` in any of those five packages exits **non-zero** ("No test files found"). `MemoryCore/package.json` also declares `"test:oss": "vitest run -c vitest.oss.config.ts"` — and **`vitest.oss.config.ts` does not exist.**

⇒ **The v2 rewrite kept the entire test *harness* and discarded every test.** `npm test` here is a command guaranteed to fail, in a repository where nothing ever runs it — which is precisely why there is no test job in CI. A test job would have gone red on day one of v2.

**This completes the run's ladder:**

| Ship | The gate |
|---|---|
| v263 | the test **without** the gate — 403 tests, nothing invokes them |
| v262 | the gate that **cannot fail** — `--passWithNoTests` |
| v264 | the gate that runs, checks real things, skips the rest, **and prints which** |
| **v265** | **the gate that is wired, would fail loudly, and is never invoked** |

---

## 5. ⭐⭐⭐⭐ HEADLINE 4 — A merged security fix, reverted by the rewrite, with its regression test deleted in the same move

On `main`, commit `823b478` (2026-06-15) — **`fix(security): enable L1 prompt injection filtering (#175)`**, by **Ziyang Guo**, an outside contributor — uncommented one line and added 22 lines of test:

```diff
-  // if (looksLikePromptInjection(text)) return false;
+  if (looksLikePromptInjection(text)) return false;
```
` src/utils/sanitize.ts | 2 +-`
` src/utils/sanitize.test.ts | 22 ++++++`

On the **default branch** — the published `v2.0.1-beta.2` — `MemoryCore/src/utils/sanitize.ts:150-153` reads:

```
  // ── Security filters ──
  // Reject prompt-injection payloads — prevent malicious content from being
  // persisted into structured memory and re-injected on future recalls.
  // if (looksLikePromptInjection(text)) return false;
```

**Commented out again. And `sanitize.test.ts` does not exist on this branch.**

### 5.1 Ruled out before claiming it

- `looksLikePromptInjection` is **defined and `export`ed** at `sanitize.ts:217`, and **called from exactly zero places** — the only other occurrence in the whole tree is the commented line.
- **No superseding filter exists.** Extent: `grep -rniE "ignore (all|previous) instruction|jailbreak|injection"` over `MemoryCore/src`, `MemoryProxy/src` and `MemoryKnowledge/src` returns only the *feature* ("context injection"), an SQL-injection table allow-list, and MMD markers.
- The detector is **expert work** — 17+ patterns across instruction-override, role-hijack, system-prompt probing, tool-invocation tricks, and `<\s*(system|assistant|developer|tool|function|relevant-memories)\b`, which **guards their own context-boundary tag**. Someone understood this threat precisely.

### 5.2 The live call-site still promises it

`l1-extractor.ts:161-164`:
> `// Quality gate: filter messages through L1 extraction rules (length, symbols,`
> `// prompt injection, etc.) before sending to the LLM. L0 deliberately captures`
> `// everything; the strict filtering happens here at L1 stage.`
> `const qualifiedMessages = messages.filter((m) => shouldExtractL1(m.content));`

Inside `shouldExtractL1`, the **length filters are also all commented out** (`// if (text.length > 5000) return false;` and the CJK checks). ⇒ **Of the three responsibilities the call-site names — length, symbols, prompt injection — exactly one is implemented.**

### 5.3 Why it matters more than the comment says — §7 is the amplifier

Memory is injected at **`system.suffix`** (§7). So the chain is:

> untrusted conversation text → L1 extraction *(filter off)* → persisted memory atom → **re-injected into the SYSTEM prompt of every future request, across sessions and across agents**

A single poisoned memory becomes a **persistent, cross-session, cross-agent, system-prompt-level instruction** — worse than the disabled filter's own comment implies, because the re-injection target is `system`, not a user turn.

⇒ **v258 code moves forward and never backward · v262 a practice does not transfer by proximity · v264 it does not transfer between two directories · v265 a *fix* does not transfer across a re-rooted branch — and the deleted test is why nobody noticed.** The first three found drift. This one found a reverted control.

---

## 6. ⭐⭐⭐ HEADLINE 5 — 97 pointers to a directory that has never existed

`grep -rn "docs/design/"` over the tree: **97 citations to 26 distinct documents.** The entire repository contains **2** files under any `docs/` path, and `docs/design/` has **never existed on any commit on any ref**.

These are load-bearing engineering references, not asides:

- `2026-07-12-cos-shark-sts-credential-plan.md` §3.1/§3.2/§3.6 — cited from **7 files**, about **credential handling**
- `2026-07-13-proxy-multinode-state-audit.md` **P0-1 / P0-2** — cited 5×; `storage/memory-storage.ts:10` calls the current state *"危险的兜底状态"* (a dangerous fallback state) by reference to P0-2
- `2026-08-03-internal-usage-telemetry-plan.md` §7.2 E / §7.2 F — cited from 5 files
- `2026-08-03-binding-flatten.md` — 8×, explaining why `Authorization` is no longer consumed

Plus two more of the same species: `vitest.oss.config.ts` (§4) and a **tsconfig path mapping + vitest alias** for `@context-proxy/cost-guard` → `./packages/cost-guard/src/index.ts`, where `MemoryProxy/packages/` does not exist and there is no `.gitmodules`. ⚠️ *That last one is intentional* — `deploy/dockerhub/publish.sh:229` calls it a *"Placeholder for the optional @context-proxy/cost-guard extension"* and `storage/factory.ts` degrades sqlite→fs→memory. **Closed core, open periphery** — the v242 shape.

⭐⭐⭐ **The rule, and it is new: v264's dangling pointer was one comment that went stale in place. These 97 were CORRECT in the repository they were written in, and were invalidated by the act of publishing.** Nothing rotted. The code was copied across a boundary and the thing it pointed at was not.

⇒ **When you export, mirror, or extract a subset of a repository, every internal cross-reference in the copied files silently becomes a dangling pointer — and no linter in either repository can see it, because in the source they all resolve and in the destination nothing knows they were ever supposed to.** That is **v240's inventory rule at the repository boundary**.

---

## 7. ⭐⭐⭐ HEADLINE 6 — How you give a coding agent new tools with no MCP, no plugin, and no client change

`MemoryProxy/src/injection/injectors/tdai-profile-memory-injector.ts`:

- `:27` → `point = "system.suffix" as const;`
- `:107` → `lines.push("<l3_core_memory>", truncate(g.l3.content, 6000), "</l3_core_memory>");`
- `:110-120` → `<l2_scene_index>` … `</l2_scene_index>` — **paths only**, not bodies
- `:164` → `export const MEMORY_TOOLS_GUIDE = \`<memory-tools-guide>`

L3 persona goes straight into the **system** field. L2 goes in as an **index**. And L0/L1 are not auto-recalled at all — the injected guide teaches the agent to fetch them itself:

> **`## ⚠️ 重要：这不是文档，这是你的可用能力`** — *"IMPORTANT: this is not documentation, this is your available capability."*
> *"…are capabilities you can actively invoke (not reference documentation). They are used via **Bash + curl**."*
> **`禁止`** *(forbidden)* *— answering things like* **`"我没有这个工具 / 需要 MCP / 需要斜杠命令"`** *("I don't have this tool / this needs MCP / this needs a slash command").*
> *"**Correct behaviour**: when you judge that memory needs querying, execute curl directly in Bash; the proxy will automatically inject identity and authentication."*

⇒ ⭐⭐⭐ **You append a curl recipe to the system prompt and rely on the shell the agent already has, while the proxy injects the credentials on the way out so the recipe needs no secrets in it.** The corpus's cleanest answer to *"how do you extend an agent you cannot modify."*

⭐ And a wonderful, honest artifact: **they discovered the model's trained instinct is to reply "I'd need an MCP server for that," and had to write a prohibition against it into the prompt.**

The write surface is genuinely fenced: `memory-bridge.ts:27-47` `ALLOWED_SUBPATHS` contains **only** `atomic/search`, `atomic/query`, `conversation/search`, `conversation/query`, `scenario/ls`, `scenario/read` — *"allowlist 限定只有 search / read 类只读 subpath"*. The agent can read memory by curl; it cannot write it.

### 7.1 Claude Code specifics, and one genuinely thoughtful detail

- `injection/adapters/anthropic.ts:~108-112` preserves **`cache_control` prompt-cache breakpoints** across the parse→serialize round-trip, with the comment *"Preserve prompt-cache breakpoint marker across the round-trip."* ⭐ **A naive rewriting proxy would silently destroy Claude's prompt caching and multiply the user's bill. They thought about it.**
- `common/cc-request-classifier.ts` classifies Claude Code traffic as **main / fork / sidequery** from the *position* of the `cache_control` marker; a `fork` request sets `readOnly` so a cache miss does not self-heal and corrupt the main branch's KV cache.
- `anthropicHandler.ts` is 2,129 lines and strips `thinking` blocks lacking a valid signature.

---

## 8. ⭐⭐⭐ HEADLINE 7 — The lock on the filing cabinet is excellent. The front door ships open. Both were decided on purpose.

### 8.1 The governance layer is exemplary

`MemoryCore/src/metadata/service/permission-checker.ts:66-84`, the `private` case:

> *"私密语义（2026-07 变更）：严格私密，只有 owner_user_id 能访问。**团队 admin 也不放行** —— 因为第 2 步 owner 判定已优先返回 ALLOW，走到这里说明当前 user 不是 owner，即使是 admin 也一律拒绝。"*

The README's strongest privacy claim — *"`private` — Only the Owner can read — not even team admins"* — is **TRUE**, and enforced by **ordering**: the owner check returns first, so admin-ness is never consulted. The comment then enumerates its own blast radius (`list-accessible` hides it from admins too) and states the **only** escape hatch: *the owner* switches to `team` or grants ACL.

⭐⭐ And `canBindAsset` (`:155-172`) closes the other door — the one an ACL over human reads would leave open: a `private` asset binds only to an agent with the **same owner and team**, and `restricted`/`task` assets **cannot be bound to an agent at all** (`return false`). They saw that "who may read this" and "which agent may be equipped with this" are different questions.

⭐ `metadata-service.ts:1396` — *"默认 visibility = private（2026-07 变更）"*: **a default that was changed *to* the safe value.**

### 8.2 And the perimeter around it ships open — because the safe setting breaks the product

`MemoryCore/src/gateway/config.ts:249` — *"**Default: undefined** — authentication is disabled, all routes are open (preserves legacy behaviour)"*; `:425` — *"both default to 'disabled' so existing setups keep working."* `server.ts:1117-1118` — `if (!expected) return "ok"; // auth disabled`.

The team did **not** overlook this. `server.ts:709-753` is the best security-posture logging I have read in a corpus subject: it logs `auth=…  host=…  cors=…` at startup, warns when no key is set, **warns harder when non-loopback *and* no key — naming the four exposed endpoints `/capture`, `/search/conversations`, `/recall`, `/seed`** — warns on wildcard CORS, and states *"Never log the key itself."* Its own comment says that combination *"is what **the security audit flagged as a real exposure**."*

**And the documented one-command install produces exactly that combination.** `deploy/global-images/.env.example:80` is:

```
MEMORY_CORE_GATEWAY_API_KEY=
```

`start-memory-core.sh:133` passes it (`-e TDAI_GATEWAY_API_KEY="$MEMORY_CORE_GATEWAY_API_KEY"`); `config.ts:815-818` coerces `""` → `undefined` (`return v || undefined`); the generated `tdai-gateway.yaml` has no `apiKey`; the gate returns `"ok"`. The port is published with `-p "${MEMORY_CORE_PORT}:8420"`.

⚠️ **Two of my own drafts died here, and the truth is better than both.** *(a)* "the installer makes it unsafe" — wrong; a container binding `0.0.0.0` behind `-p` is normal Docker, and the installer **does** set the variable. *(b)* "they forgot" — wrong, and `.env.example:74-79` says so outright:

> *"留空（默认）—— 关闭 Bearer gate（本地零配置体验）… 非空 —— 所有请求必须带 `Authorization: Bearer <key>`；**proxy 目前不发这个 header，因此 proxy 的 auth/sessionInit 会失败**。**生产环境后续需在 proxy 侧修复后再启用非空 key。**"*

⇒ ⭐⭐⭐ **Authentication is off by default because turning it on breaks the product.** The proxy — the component the README tells every user to route Claude Code through — does not send the header. The two available states are *auth off and working* or *auth on and broken*. And they wrote that down, including **"for production this must be fixed on the proxy side first"**, in the default configuration of a shipped v2.0.1 release.

⭐ Verified against their own claim: `grep -rn "Authorization" MemoryProxy/src` shows the proxy setting that header for **Opik** and for the **LLM upstream** — never for memory-core. `memory-bridge.ts:82` even notes it *"不再吃 Authorization"* (no longer consumes Authorization), citing `docs/design/2026-08-03-binding-flatten.md` — one of the 97.

### 8.3 The sentence this ship turns on

**The ACL default moved to safety in July because nothing broke. The auth default stayed unsafe because the proxy would break.** The difference between them is not care, competence, or awareness — the same organisation, in the same repository, in the same release, reasoned carefully about both and wrote both reasons down.

⇒ ⭐⭐⭐ **A discipline travels freely wherever it is free, and stops wherever the safe choice would cost something.** Which means *"do they take security seriously?"* is the wrong audit question. The right one is: **which of your safe defaults were free?**

⇒ And the seam is the same one as always: **MemoryCore built a careful auth gate with a constant-time compare and an escalating warning ladder; MemoryProxy never learned to send the header.** v264: a discipline stops at the edge of the team that holds it. **v265: we can prove it, because the `.env.example` says so in one sentence.**

---

## 9. What is *good* here — stated plainly, because most of it is

- **`credit-reporter.ts:37-44`** — a fail-safe default chosen by reasoning about **asymmetric harm**, with the reasoning in the code: the OpenAI branch is the fallback because *"Anthropic 分支假设 input_tokens 已扣缓存，若被错误应用到 OpenAI usage 上会把 cache 部分按 input 高价重复计费；反之…仅退化为等价旧逻辑，**风险不对称**"* — i.e. **pick the default that fails toward under-charging the user.** In the *billing* path.
- **Telemetry is off by default.** `clickhouse.enabled: false`, endpoint an `example.com` placeholder. Its "hard constraints" (`clickhouse.ts:912-920`): writes **never throw**, internal helpers never throw, old code paths untouched; 90-day TTL; `request_body` truncated to 512 bytes; `bypass_reason` capped *"防止 log 文案改动导致列基数爆炸"* (to stop a log-wording change exploding column cardinality). **No covert phone-home anywhere** — egress strings are localhost and `example.com`.
- **The SDK does not default to Tencent's cloud.** `memory.tencentyun.com` appears **only in docstring examples**; `endpoint` is a required parameter in both SDKs (`HttpStub.__init__`, and `endpoint: string` in the TS interface).
- **Keys are not cached or logged** (`auth.ts`: every request verified against `/v3/meta/auth/verify`, key in the POST body, only the result logged).
- **1 MiB request-body limit**, configurable (`server.ts:158-172`) — and its implementation note is a curiosity worth keeping: env access is delegated to `utils/env-config.ts` *"to avoid **a known OpenClaw security-scanner false positive**."* ⇒ ⭐ **when agent-ecosystem scanners become gates, their false positives become architectural forces.**
- **Container runs as non-root** (`tdai`, uid 10001); CI uses `npm install --ignore-scripts`; CORS defaults to **no headers at all**.
- **Attribution is disclosed, not hidden** — see §10.
- **Known limitations are unusually honest** (§11).

---

## 10. Attribution — a corpus-recursive triple, openly credited

README Acknowledgements name three sources, and two are corpus entities:

1. ⭐⭐ **[CodeGraph](https://github.com/colbymchenry/codegraph)** — *"our CodeGraph asset module **uses code from this project**"* — **this is corpus subject v70**, and the anchor of **CONFIRMED Library-vocab #23**. Verified **MIT** (Colby Mchenry) ⇒ licence-compatible.
2. **Hermes Agent** (Nous Research) — *"uses part of the Skill-related code."* Hermes is a corpus entity via v227.
3. ⭐⭐⭐ **Karpathy's ["LLM Wiki"](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)** — *"directly informed how our Wiki layer is built and kept up to date."* **This vault's founding pattern, cited by gist URL, productized by a major cloud vendor.**

⭐ **The sharp contrast:** v181 cortex-hub **silently** bundled the corpus's GitNexus v33 as an uncredited engine. v265 does the same class of act and **credits it in the README.** Same corpus, opposite disclosure behaviour.

⚠️ **But prose credit is not licence compliance.** MIT requires the copyright notice *"be included in all copies or substantial portions."* There is **no NOTICE file and no third-party licence file** — `git ls-files | grep -iE "notice|third|attribution|licen"` returns only `LICENSE`, which names only *"Copyright (C) 2026 Tencent. All rights reserved."* ⇒ **the acknowledgement is in the README; the obligation is in the LICENSE file.** (v264's D44 — *the licence travels with the artifact* — inverted.)

---

## 11. Claims audit

**TRUE, and worth recording as such:**
- The `private`-visibility claim (§8.1) — fully implemented, plus the agent-binding door closed.
- *"No plugin, hook, or MCP server is required"* — true; the generic path needs only a base URL and headers.
- L2/L3-injected, L0/L1-on-demand, BM25+vector+RRF, and the caps on injected context — all present in code.
- The `+59%` PersonaMem arithmetic (48→76) checks out.

**Inflated, stale, or unverifiable:**
- ⚠️ **PersonaMem 48% → 76%** appears in exactly **2 files, both READMEs**. No harness, no model named, no config, no link, no reproduction script — while the README explicitly invites *"benchmark reproductions."* **Do not cite this number.**
- ⭐⭐ **Four surfaces disagree on the version:** `README.md:297` *"Current release is **v2.0.0**"* · `ROADMAP.md:6` *"Current release: **v2.0.1-beta.1**"* · latest tag **`v2.0.1-beta.2`** · `MemoryCore/package.json` **`"2.0.0-beta.1"`**. The **npm manifest — the one a machine reads — is the oldest of the four**, two releases behind the tag on the very commit it sits in. *(v260/v262's manifest-fossil pattern, at N+1 and quantified.)*
- **7 agents are presented as equals; 5 have dedicated adapters.** `agent-adapters/` holds `claude-code`, `codebuddy`, `codex`, `dsh`, `workbuddy` + `default`; `injection/agents/` holds only 3. ⚠️ **Fairly read this is not a support gap** — Hermes and OpenClaw work through the generic path, which is the architecture's whole point. It is an *investment* asymmetry (file mentions: codebuddy 64, claude-code 45, codex 33, workbuddy 28, dsh 17, openclaw 6, **hermes 2**).
- ⚠️ **The README's clone URL says `github.com/Tencent/` (10 occurrences) vs `TencentCloud/` (12).** **The command WORKS** — `git ls-remote` on the `Tencent/` URL returns the identical HEAD SHA (an org-transfer redirect). The finding is not a broken command; it is that commit `a7d7d85` is titled *"docs(install): **fix repo URL to TencentCloud/**"* and fixed **only** `INSTALL.md`/`INSTALL_CN.md`, leaving 10 occurrences in five other files including the README's first command.
- **Known limitations (honest, and material):** `x-task-id` is *"Required in the current version"* — without it *"the Proxy falls back to an interactive form flow — which Hermes / OpenClaw cannot respond to, resulting in **session bypass (no memory injection or conversation recording)**"*; and *"**Some clients may not carry extra headers on tool-call follow-up requests**, causing those turns to skip memory injection and conversation recording."*

⇒ ⭐⭐ **The product's failure mode is SILENCE.** When session registration fails you do not get an error — you get an agent with no memory that looks exactly like an agent with memory. They documented that plainly. *(v260's FALSE-SUCCESS class: `spawn()` returning `Ok`.)*

---

## 12. Mint decision — **NO MINT**, on four independent grounds

**Counts UNCHANGED: 46 top-level patterns / 12 CONFIRMED Library-vocab. §C-1 = 12, §C-2 = 38.**

1. **NOT world-first.** Letta/MemGPT (2023), Zep (2023), mem0 (multi-tenant, pre-2024), Cognee, **supermemory (= corpus v132)**, Graphiti (Jan 2025), LangMem (2025) all predate the 2026-04-09 root on the memory-layer surface. And the vault's **own verified record** (memory `agent-memory-architecture`, 2026-07-04) has Anthropic's Managed Agents memory stores shipping **30-day versions + redact** — i.e. persistent memory *with versioning* as a first-party product. ⚠️ *I did not re-verify the fleet's "team memory + audit trails, April 2026" phrasing and do not rest anything on it; the conclusion stands on the other legs.*
2. ⭐⭐⭐ **The corpus already has a rule for exactly this shape, and this is its strongest instance.** `_patterns/06`, the v163 ai-maestro note: *"**corpus-recursive capability absorption** — CozoDB memory ↔ v66 agentmemory/#85/v132 + ts-morph code-graph ↔ v70 codegraph; the platform **ABSORBS prior-standalone capabilities as sub-features → NOT double-counted (components, not the product)**."* v265 absorbs **four**: codegraph v70 (literally its code), a Karpathy-wiki generator, a Hermes-derived skill store, and a chat-memory engine.
3. **Scale and vendor weight are not a class** — v222 lobehub (world-canonical ≠ world-first, fame ≠ mint); v196 meetily (domain-not-capability); v227/v236 (form-factor within a genre).
4. ⭐ **The novel parts are components, not the product** (v242 **D25**): the system-prompt-curl tool-delivery mechanism (§7) and the asymmetric-risk billing default (§9) are the two ideas worth reusing, and **neither is a capability the platform delivers to a user.**

`inflation_check` HELD. **Per §44 cl. 5, §28 does none of the work.**

**Recorded as the operator/audit-reviewable alternatives, not self-executed:**
- a §C-2 N=1 mint for *"Team-Scoped Multi-User Agent-Memory Platform with Owner/ACL/Version Governance over Memory Assets"* (collision grep clean: no prior corpus row covers team-scoped multi-user agent memory — C08 supermemory v132, C31 PilotDeck v175, v66 agentmemory, v118 OpenHuman are all single-user);
- a §C-2 N=1 mint for *"Agent Capability Delivered as a System-Prompt Curl Recipe Instead of MCP"* — collision grep found **no** prior corpus instance of a proxy that **mutates** the agent's request to add memory (`intercept`-to-**observe** = C29 claude-tap v173; intercept-to-**re-authenticate** = v207/v208/v231/v232). Corpus-first for the mechanism; declined per ground 4.

**Instance-strengthening recorded, not self-incremented:**
- **CONFIRMED Library-vocab #23** — candidate N=6 via the v70 code reuse ⚠️ *with two caveats: it is a component here, and it is queried by HTTP `/v3/tools/call` + curl, not MCP.*
- ⭐ **Pattern #57 Karpathy generate-vector → 6th instance** (v118 → v134 → v234 → v252 → **v265**), and the **first from a major cloud vendor citing the gist by URL**. Also a genuine **#57 corpus-recursive dependency** (openly credited code reuse from v70).
- **Pattern #18 B1-MCP — the MCP-*exclusion* pole**, joining pi v228: here "no MCP" is the stated design thesis, and §7 is the substitute mechanism.
- **Pattern #83** honest-deficiency-disclosure — **STRONG** (Known limitations; the `.env.example` auth disclosure; *"not production-ready"* in shipped config).
- **Library-vocab #13** *"OSS-with-hosted-Pro-SaaS-tier-on-MIT-base"* (the v78 candidate) — a strong instance: `README.docker.md:32-33` ships **both** a `standalone` profile (*"零外部依赖"*) **and** a `service` profile (*"K8s 多副本、多租户云服务"*), and `credit-reporter.ts` exists to meter *"(e.g. TDAI MemoryPlus)"*. ⭐ **You can read the vendor's multi-tenant billing path in the open-source repo.**
- **#19** 19a corporate-not-Anthropic · **#12** POSITIVE · **#66** MIXED · **#84** cross-vendor tolerance (7 agents incl. rivals).

**NON-CLAIMS:** NOT **#52** (stars page-stated only, GitHub API mocked §37.4) · NOT a new top-level pattern (max #85) · nothing executed beyond the local guard experiment · NOT world-first on any axis.

**Phase 0.9 — GOAL-ALIGNED INCLUDE 3/4:** **(a) FAIL** §41 (Tencent Cloud, corporate-not-Anthropic; the v169 NVIDIA / v213 Intel precedent) · **(b) STRONG** (agent-memory infrastructure with a first-class Claude Code path) · **(c) STRONG** · **(d) STRONG**. Cleanly GA — **no §40, no override.** Streak **v264 `GA:121` → `GA:122 · OG:13 [7 ov]`**, **45 consecutive GA** v220→v265; **§35 CLEAR** ({v263 GA, v264 GA, v265 GA} = 0 OG).

---

## 13. Method, and my own errors

**Hand-verified throughout**, with a **20-agent fleet** (9 dimensions × assess→refute + 2 prior-art lenses; 2.23M subagent tokens, 782 tool uses, 647s). **16/18 agents completed; 2 (memorycore, panel-auth) hit the StructuredOutput retry cap** — the same failure as v264; **both were dimensions I had already covered by hand**, so nothing was lost. Every `path:line` in this document was read in my own session. Corpus-collision greps done by hand per the standing instruction.

⭐⭐ **D51 confirmed live, and refined.** A refuter disputed my `main` commit count with a `reproduction` string showing `git log origin/main --oneline | wc -l → 50`. The same command here returns **108**, as do two other methods. ⇒ **A refuter's *reproduction string* is itself a claim, not a check.** D51 said a refuter cannot distinguish "false" from "my command returned nothing"; this adds: **it will also present a wrong number in the format of a verified one.** The same fleet was excellent where refuting required it to *find* something — it correctly caught a 954-vs-957 file count, a wrong author count, an over-claim that the CI file existed only on `main`, an over-claim that `hermes-plugin/` was lost, and a DoS claim refuted by a real 1 MiB body limit.

**ERROR LEDGER — 4, all mine, all caught pre-publication:**
1. 🔴 "the README's first command is broken" — **wrong**, the `Tencent/` URL redirects and resolves.
2. 🔴 "the installer takes the safe loopback default and makes it unsafe" — **wrong**; `0.0.0.0` behind `-p` is normal Docker and the installer *does* set the variable.
3. ⚠️ "Hermes/OpenClaw are unsupported" — **wrong**; they use the generic path by design.
4. ⚠️ "Zep appears in 404 vault files" — a case-insensitive substring inflation; the meaningful figure is **27 files** on `\bZep\b`.

⭐ **Three of the four are one shape: I inferred the absence of a capability from the absence of a file.** That is the same failure D51 names in refuters, committed by the orchestrator — and #4 is the v264 `RATIFIED` substring trap recurring. ⇒ **the fix is not "search harder," it is "open the thing the measurement measured."**

**NOT ESTABLISHED:** whether any of it runs · whether the ACL holds under adversarial testing (no execution, no tests to run) · the PersonaMem figure's provenance · star/fork counts (API mocked, §37.4) · what the internal repo's CI enforces · whether `looksLikePromptInjection` was disabled deliberately or lost in the port — **the commit history that would answer it does not exist on this branch** · whether the hosted TDAI MemoryPlus tier shares this code.

**SANDBOX:** `python3` unusable; bash 3.2; git 2.19. Nothing installed, nothing executed except the local read-only guard experiment.
