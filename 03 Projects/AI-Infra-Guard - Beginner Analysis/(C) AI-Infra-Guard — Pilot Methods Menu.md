# (C) AI-Infra-Guard — Pilot Methods Menu

**v276** · Apache-2.0 (+ `NOTICE` attribution rider) · skills are **MIT** · HEAD `32df94d3`

Ordered by increasing footprint. Rungs 0–2 are the recommended stopping point.

---

## Rung 0 — Read, install nothing (45 min) ⭐⭐⭐

| Read | Why |
|---|---|
| `Research/deepseek-harness-security-assessment/results/RESULTS.md` | **14,560 runs, two independent evaluators reported side by side.** Skills channel = **16.0%** successful prompt injection. This is a number about *your* working surface. |
| `skills/aig-agent-redteam/SKILL.md` 操作原则 1, 3, 5 | Authorization-first, canary-not-real-secrets, evidence-before-conclusion. The best safety framing on an offensive artifact in the corpus. |
| `skills/edgeone-clawscan/SKILL.md` frontmatter + `skills/edgeone-skill-scanner/SKILL.md` "Security Declaration" | Two sibling skills, two egress profiles, **each declared in the frontmatter the agent reads**. Copy this pattern into `05 Skills/`. |
| `SECURITY.md:60-90` | A genuine trust model: what it trusts, what it does not, per-deployment-mode boundaries, explicit out-of-scope list. |
| `README.md:199-210` **beside** `Research/RESULTS.md` | The ship's whole lesson in two files: a bolded 0.9848 with no methodology, and a 14,560-run study that publishes its own disagreements. |

---

## Rung 1 — The vault item (20 min) ⭐⭐⭐

**This ship completes a four-part arc:**

> v273 — *where* the check lives (`bin/`, invoked by the per-ship append)
> v274 — *how* to write its clauses (derive every population from the tree, never a typed list)
> v275 — *what to aim it at* (your own published claims, not only generated files)
> **v276 — which claims rot: the ones written as round floors.**

**Add to `(C) proposed-verify-vault-inventory.sh`:**

```
clause (e): every numeric claim in the CLAUDE.md CURRENT HEAD block must be
            either (i) re-derivable by a command printed next to it, or
                   (ii) written as an exact figure with the date measured.
            FAIL on any bare round floor: "N+", "~N", "over N", "≈N".
```

**Why this clause and not another:** A.I.G published exact figures and round floors from the same keyboard in the same month. **Every exact figure was right** (130, 1888, 9 categories, 9 operators, 14,560 runs). **Two of three floors were false when typed** — "2000+" against 1,916, and "60+" against 51. The floor is the form a number takes when nobody derived it. Our head block is almost entirely floors: *"~197.6KB"*, *"≈19"*, *"≈N=15"*, *"31 such sentences"*.

Borrow verbatim from `src`-style discipline — A.I.G's own best habit, `cmd/yamlcheck/main.go:20`: *"Used in CI pipelines to verify the format of YAML files under the data directory."* A tool that states its own scope cannot be mistaken for one that checks more.

---

## Rung 2 — Install ONE skill, zero egress (30 min, LOW risk) ⭐⭐

**`skills/edgeone-skill-scanner/`** — a **single `SKILL.md`**, MIT, **no scripts, no network calls**, declaring *"Local-only analysis … No file contents, credentials, or personal data are sent externally."* Verified: the directory contains exactly one file.

```bash
cp -r "<clone>/skills/edgeone-skill-scanner" ~/.claude/skills/
```

Then: *"scan skill"* over each directory in `05 Skills/`.

**Why this is the right first pilot:** it is the lowest-footprint artifact in the repository, it is the only corpus subject that can vet the vault's **own** skills, and it needs no API key, no server, no Docker, and no Python. Note that skill contents necessarily enter your own agent's context — that is inherent to any skill, and nothing goes to Tencent.

---

## Rung 3 — The CLI, fenced (60 min, MEDIUM risk) ⭐

```bash
# run the install-snapshot skill FIRST
python -m venv /tmp/aig && /tmp/aig/bin/pip install aig-skill-scan
DEFAULT_MODEL=<your choice> /tmp/aig/bin/aig-skill-scan --repo /tmp/scratch-skill -o result.json
```

⚠️ **This one IS LLM-driven** — `skill-scan` is a regex pre-scan (`utils/pre_scan.py`) feeding an **LLM agent with `read_file`/`grep`/`base64_decode` tools**. It sends skill source to a model provider. Default is `deepseek-v4-flash` (`skill_scan/utils/config.py:57`) — set it deliberately. Output supports **SARIF** (`to_sarif()`, `main.py:217`) and a 0–100 score (`project_analyzer.py:89`).

**Fences:** throwaway venv · scratch copy of the target, never a real credential-bearing repo · choose the model explicitly · `npm-security-check`/`install-snapshot` first.

---

## Rung 4 — The platform (NOT recommended) 🔴

If you ever do run it, **change these two things first**:

```yaml
# docker-compose.yml:8   — BEFORE
    ports: ["8088:8088"]              # binds 0.0.0.0 — unauthenticated UI on every interface
# AFTER
    ports: ["127.0.0.1:8088:8088"]
```

```yaml
# docker-compose.yml:48-51 — the agent container
    cap_add: [SYS_ADMIN]              # for Chromium's sandbox; undisclosed in SECURITY.md
    security_opt: [seccomp:unconfined]
```

`README.md:149` states plainly: *"It currently lacks an authentication mechanism and should not be deployed on public networks."* Believe it. Mitigation that does exist: both workloads drop to non-root via `gosu agent:agent`.

---

## Rung 5 — The bake-off (the standing corpus item)

**C26 now has two instances and neither has ever been piloted.** Run **SkillSpector v169** (static: AST + taint + YARA, 64 patterns) and **AIG skill-scan v276** (regex → LLM agent) over the *same* skill directory and diff the findings. The mechanisms are inverted, so the disagreement is the interesting output — and it is the evidence the audit needs to decide whether C26's *"two-stage static + optional-LLM"* clause should be generalised.

---

## 🔴 NEVERs

- Never run `docker-compose up -d` as shipped.
- Never point any A.I.G scanner at infrastructure you do not own — the red-team skill's own principle #1: *"确认用户拥有目标或被授权测试."*
- Never cite **"2000+ CVE rules"** (1,916 at `v4.5.2`; 1,662 distinct CVEs), **"3 official skills"** (4), or **"10 skills total"** (4 dirs + 10 detection types).
- Never quote **0.9848** as A.I.G's score — it is **Claude Opus 4.6's** F1, on Tencent's own benchmark, published with no dataset size, baseline, or method.
- Never treat `CLAUDE.md`/`AGENTS.md`/`CODEBUDDY.md` as current — one commit each, 2026-03-20, and they omit Skill-Scan.
- Never assume a `data/vuln` entry means detection: **10 rules under-match their own advisories**.
- Never integrate the code without the **`NOTICE`** attribution: *"Based on Tencent Zhuque Lab AI-Infra-Guard"* + a repo link.
- Never run `git log` to count anything in this sandbox — use `git rev-list --count`.
