# (C) OpenSandbox — Pilot Methods Menu

**Wiki v244** · 2026-08-19 · ranked by value-per-risk. **A1–A3 install nothing.**

---

## ⭐ A — Zero-install, do these now (≈30 min total)

### **A1 — `ln -s` the vault's own agent-context file. Four ships have diagnosed this; none of us has fixed it.**
The corpus now holds **three** independent instances of a committed, drift-proof bridge from the harness-specific filename to a canonical `AGENTS.md` (**v213** Intel geti, **v243** ToolJet, **v244** OpenSandbox). OpenSandbox shows both mechanisms side by side and demonstrates the ranking: the **symlink delivers content**, the **prose stub costs a second read**.

```bash
cd "/Users/Cvtot/KJ OS Template" && ln -s CLAUDE.md AGENTS.md && git add AGENTS.md
```
⚠️ Direction matters: the vault's canonical file is `CLAUDE.md`, so `AGENTS.md` becomes the view. (ToolJet and OpenSandbox go the other way because `AGENTS.md` is *their* canonical file.) Verify with `git ls-files -s AGENTS.md` → expect mode `120000`.

### **A2 — Add a "Content ownership — single source of truth" table to `CLAUDE.md`.**
Lift the root `AGENTS.md` §"Documentation Rules" shape: content type → owning location → rule. For the vault: per-wiki detail → `_state/03c` · pattern definitions → `_patterns/` · audit docs → `04 Reviews/` · the shim → `CLAUDE.md` (index only, never content). Then add their two guardrail lines verbatim in spirit:
> *Ask first: **intentional drift between a public contract and its implementation.***
> *Never: **edit generated output as the only fix.***

⭐ The second one is the rule that would have stopped the `-v183` filename problem from being "fixed" by editing the index instead of the name.

### **A3 — Fix the `-v183` label, and encode D29 while you are there.**
`_state/03c-projects-v61-v183.md` holds entries through **v244** — 61 versions of drift, flagged at v239/v240/v242/v243 and fixed by none. Rename + sweep references. Then write **D29** into the `verify-vault-docs` spec:
> *Staleness is content disagreeing with reality, not `mtime`. Test every path, command and count a doc names. A file unchanged for 67 days because it is still correct is not stale — and a file touched yesterday that names a deleted path is.*

⭐ This is the rule that separates a linter from a recency alarm, and it came from **refuting** an agent that called a perfectly accurate file stale.

---

## B — Read-and-borrow (no install, ~1–2 h)

### **B4 — Copy `startup_guard.py`'s consent pattern into the hireui LLM-feature spec.** ⭐⭐
~60 lines that convert an insecure-by-convenience default into **informed consent that fails closed**: an env-var path for CI, an ANSI-red TTY prompt demanding the exact string `YES`, a **30-second timeout that aborts**, a warning logged on every permissive start, and a link to the tracking issue. This is the corpus's **first positive answer** to the broken-auth failure mode that made **v231** and **v232** pilot-AVOID.
→ Apply to hireui wherever a dev-convenience switch could reach production: *if the unsafe mode is reachable, make starting in it require an act, log it, and abort on silence.*

### **B5 — Steal the `osb skills` copy-vs-append target model** for hireui's future first-party skill suite.
`cli/src/opensandbox_cli/commands/skills.py` renders one canonical Markdown skill into six harnesses and correctly distinguishes **copy** targets (a skills *directory*: Claude Code, Cursor, Codex) from **append** targets (a single instruction *file*: Copilot, Windsurf, Cline), at both project and user scope. Pair with the **v213 geti** template for shipping a product's own skills.

### **B6 — Read OSEP-0012 (credential vault, 76.6 KB) as a spec for secret handling.**
Injecting outbound credentials into a workload *without exposing the real secret to it* is exactly the shape hireui needs for third-party API keys. Read the OSEP, not the code, first — it is 76 KB of stated design with a recorded status.

---

## C — Fenced technical pilot (install; scratch host only)

### **C7 — Stand up the Docker runtime on a throwaway host and test the proxy-path bypass.** 🔴
The single most useful hour available. Steps, in order:
1. `install-snapshot` first; scratch VM or throwaway container host, **never** your machine.
2. **Set `server.api_key` immediately.** Never set `OPENSANDBOX_INSECURE_SERVER=YES` on anything reachable.
3. Bind to `127.0.0.1`, not the `0.0.0.0` default (`config.py:473`).
4. ⭐ **Then test this:** with a valid API key configured, request `/v1/sandboxes/{id}/proxy/{port}/` **without** the `OPEN-SANDBOX-API-KEY` header. `middleware/auth.py:82-83` skips auth on that route in single-tenant mode. Determine whether `[ingress.secure_access]` blocks it when unconfigured.
5. **If it is a real hole, report it upstream** — GitHub private security advisory; they commit to 48-hour acknowledgment. *(An unauthenticated path to sandbox ports would be worth a CVE.)*
6. Use published **cosign-signed images pinned by digest**; do not build their K8s images yourself (two Dockerfiles route through `mirrors.aliyun.com` / `goproxy.cn`).

**Do NOT:** point it at candidate data (the RATIFIED candidate-LLM legibility ADR governs any candidate-touching path); expose it to a network; use the K8s path for a first pilot.

### **C8 — Run one Claude Code session inside a sandbox** (`examples/claude-code/`) to see the containment story end to end. Low value for hireui, high value for understanding what the substrate actually buys — and it is the one example of the nine that is directly on our stack.

---

## ❌ Do not

- ❌ Adopt OpenSandbox as a hireui component today — Apache-2.0 permits it, but nothing in hireui needs untrusted code execution yet. **Solve a problem you have.**
- ❌ Trust the "Strong Isolation" README bullet — you install gVisor/Kata/Firecracker yourself, and **gVisor disables their egress policy** (validators reject the combination).
- ❌ Cite "340 Claude-co-authored commits" (197 commits / 340 lines), any git count without its ref population, or the star figures as verified velocity (§37.4).

---

## Recommended sequence

**A1 → A2 → A3** today (under 30 minutes, and it closes a defect four consecutive ships have flagged), then **B4** into the hireui spec. **C7** only when you want the sandbox question answered properly — and if you run it, the upstream security report is the highest-value output of the whole pilot.
