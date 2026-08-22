# (C) TencentDB Agent Memory — Pilot Methods Menu

**v265** · read-and-borrow subject · nothing here requires installing TencentDB Agent Memory
Ordered by (value ÷ effort), lowest footprint first. Rungs 0–3 need **no install at all**.

---

## ⭐ Rung 0 — 30 minutes, zero install, highest ROI

Read five things in the clone, in this order. Each is one screen.

1. `MemoryCore/src/metadata/service/permission-checker.ts:43-105` — an ACL enforced by **ordering**, with its blast radius enumerated in-comment and an owner-only escape hatch. Then `:155-172` `canBindAsset`, which closes the door an ACL over human reads would leave open.
2. `MemoryProxy/src/credit-reporter.ts:37-44` — a default chosen by **asymmetric harm**, reasoning included.
3. `MemoryProxy/src/injection/injectors/tdai-profile-memory-injector.ts:27, :107, :164` — `point = "system.suffix"`, the `<l3_core_memory>` paste, and the curl-recipe guide that has to forbid the model from asking for MCP.
4. `MemoryCore/src/utils/sanitize.ts:150-153` beside `:217` — an exported, working prompt-injection detector with **zero callers**, three lines under the comment explaining why it matters.
5. `deploy/global-images/.env.example:74-80` — a safe setting that is documented as **unavailable**, because turning it on breaks the other half of the product.

**Then run this against your own repositories:**

```bash
grep -rn "docs/design/\|see docs/\|详见 docs/" . --include=*.ts --include=*.py --include=*.md | wc -l
```

Every hit is a pointer that resolves *here* and may not resolve wherever this file gets copied to.

---

## ⭐⭐⭐ Rung 1 — 45 minutes — the export-boundary pointer check, into the vault

**The v265 rule generalised:** when you export, mirror, or extract a subset of a repository, every internal cross-reference in the copied files silently becomes a dangling pointer, **and no linter in either repository can see it** — in the source they all resolve; in the destination nothing knows they were ever supposed to. That is v240's inventory rule at the repository boundary.

**The vault has exactly this exposure**, and it is the operator decision v259 left open: `05 Skills/` holds copied-and-re-versioned skills, and the routine exists as v2.1 → v2.8 as **separate files**. A cross-reference written in v2.8 does not exist in v2.7's copy; a fix in the newest copy never reaches the older ones.

**Do:** add a clause to `(C) proposed-verify-vault-inventory.sh` that extracts every `_state/`, `_patterns/`, `05 Skills/` and `04 Reviews/` path referenced from any vault markdown file and asserts it exists. It is a ten-line clause and it would have caught the `03c` filename drift, the five unindexed `_state/` files found at v255, and any future one.

**Composes with:** the v264 Rung 3 exemption audit (write the justification beside every `grep -v`) — a reference check and an exemption check are the two halves of the same instrument.

---

## ⭐⭐⭐ Rung 2 — 45 minutes — "which of my safe defaults were free?" into the RATIFIED ADR

**The finding:** this project moved its asset-visibility default *to* `private` in July because nothing broke, and left gateway auth open because the proxy would break. Both were reasoned. Both were written down. The difference was cost.

**Do:** add one section to the RATIFIED hireui candidate-LLM legibility ADR — a **default-cost register**. For each safety-relevant default in the hireui LLM path (retention, redaction, who-can-read, human-in-loop, eval gate), record three fields: *the safe value*, *what it costs*, *and whether we took it*. Where the answer is "no", record **what would have to change for the safe value to become free** — because that, not a warning, is the actual remediation.

**Why it belongs in that ADR specifically:** it already mandates fixed + legible + audited + human-in-loop + eval-gated. It does not yet record which of those were cheap. Under **Art. 50(4)** deployer duties, "we knew and shipped the warning" is a materially worse position than "we knew and it cost us X."

**Pairs with v264 Rung 1** (the asymmetric consent rule): that one stamps a disclosure version; this one records why a default is what it is. Same ADR, adjacent sections, 75 minutes total.

---

## ⭐⭐ Rung 3 — 45 minutes — the curl-recipe capability pattern, evaluated not adopted

**The mechanism (§7 of the Deep Dive):** give an agent a new capability by appending a curl recipe to its **system prompt**, relying on the shell it already has, with a proxy injecting credentials on the way out so the recipe contains no secrets.

**Do:** write a one-page comparison for the vault — *system-prompt curl recipe* vs *MCP server* vs *skill file* — on five axes: client changes required, credential exposure, token cost per turn, whether the model reliably *uses* it, and auditability. TencentDB's own prompt is evidence on axis four: they had to write **"forbidden: answering 'I don't have this tool / this needs MCP'"**, which tells you the model's default is to refuse.

**Don't adopt it for the vault.** The vault's own tool surface is already the ~54K floor problem; the honest read is that this pattern trades an install for permanent system-prompt weight. But it is the right answer for *"extend an agent you do not control"*, and worth having written down before you next need it.

---

## ⭐⭐ Rung 4 — 60 minutes — the hireui candidate-data ACL, modelled on §8.1

The single most directly transferable artifact. hireui will need exactly this: an asset (a candidate record) with an owner, a team, a visibility, and an agent that may or may not be equipped with it.

**Do:** port the *shape*, not the code — (i) owner check **before** the visibility switch, so admin-ness is never consulted for `private`; (ii) the blast radius written in the comment, including the list endpoint; (iii) an owner-only escape hatch; (iv) a **separate** `canBindAsset` predicate governing which agent may be given the asset, defaulting `restricted` to `false`. Then write the test that (iv) prevents: *a private candidate record must not be bindable to a shared screening agent.*

**This closes a real gap:** the API-security thread records **BOLA authz absent from all 7 techniques as hireui's #1 risk**. This is a worked example of the fix, from a subject that got it right.

---

## Rung 5 — 90 minutes, higher footprint — a fenced local look

Only if reading is not enough. **Not on any machine holding candidate data.**

```bash
# scratch VM or throwaway container host only
git clone https://github.com/TencentCloud/TencentDB-Agent-Memory.git
cd TencentDB-Agent-Memory/deploy/global-images && cp .env.example .env
```

**Then, before `./start-all.sh`:**
- edit `start-memory-core.sh` to publish loopback only: `-p 127.0.0.1:${MEMORY_CORE_PORT}:8420`
- same for the proxy and panel start scripts
- set `MEMORY_CORE_GATEWAY_API_KEY` to a random value **and expect the proxy's session init to fail** — that is the documented trade, not a misconfiguration
- point `MEMORY_LLM_*` at a throwaway key with a hard spend cap
- assume every conversation you feed it is retained in plaintext in a Docker volume with the injection filter off

**Needs:** Docker, Node ≥ 22.16. Watch `docker logs -f tdai-memory-core` **at startup** — the security-posture line and its warnings only print once, and they are the only place the auth state is announced.

🔴 **NEVER:** run it against a repo containing candidate PII · leave the memory-core port on `0.0.0.0` · treat "memory returned nothing" as "no relevant memory" (it is indistinguishable from session-bypass) · cite its benchmark · rely on the ACL without testing it, since there are no tests to run.
