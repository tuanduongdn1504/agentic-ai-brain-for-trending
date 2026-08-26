# (C) ComfyUI — Pilot Methods Menu (v281)

Ordered by increasing footprint. Everything through Rung 3 is zero-install and zero-risk. **Nothing here goes near candidate or production data.**

---

## A. Read-only (zero install, zero risk)

**A1. The four AI surfaces, in order (40 min).** Read them as one system, not four files:
`AGENTS.md` (361 lines — the instruction) → `.coderabbit.yaml` `path_instructions` + `knowledge_base` (the enforcement) → `.github/workflows/ci-cursor-review.yml` (the second reviewer) → `.github/scripts/check-ai-co-authors.sh` (the erasure). The point only appears when you read them together.

**A2. The nineteen minutes (10 min).** `git log -1 --format='%ai' 2bd4d82b` (12:34:04) then `7d5f5252` (12:53:13), same day. Then `git merge-base --is-ancestor 2bd4d82b 7d5f5252`. The clearest specimen the corpus holds of a gate written directly from a dated incident.

**A3. `SECURITY.md` as a threat-model template (20 min).** Four assumptions, six non-vulnerability categories with reasons, and an honest admission that there is no auth. Then verify its central claim yourself: `awk 'NR==63' comfy/cli_args.py`.

**A4. `AGENTS.md:57-73` — the privacy rule (10 min).** The strongest anti-telemetry statement in 281 subjects, ending *"These labels do not make internet access acceptable."*

**A5. `AGENTS.md:304-346` — security guidance written for a machine (15 min).** Treat `io.Combo` values as untrusted at the filesystem boundary; *"Do not rely only on the advertised combo options or prompt validation."* Ends with the mascot rule.

**A6. Verify the offline claim yourself (20 min).** README says *"core does not download anything unless you request it."* Check `app/frontend_management.py:370`, then `git grep -E '\bdownload_file\b'` and watch the only core network function turn out to have no caller.

---

## B. Write-it-down (no install; produces a vault artifact)

**⭐ B1. The vault's AI-provenance policy (30 min) — THE VAULT ITEM.**
This corpus has now found left-on default Claude trailers four times (v243: 905 · v273: 599 · v280: 1 of 2,055) and **has never stated its own policy.** Two poles now exist in the corpus: **v239** treats AI authorship as *required* provenance metadata; **v281** strips it and tells you to force-push. Write the vault's answer into `CLAUDE.md`. Include the mechanism note: ComfyUI's gate covers 875 of 899 commits *because it runs on pull requests* — a single-operator vault that commits directly would need a pre-commit hook, not a PR check.

**⭐⭐ B2. Bind `CLAUDE.md` to a reviewer (45 min) — STRONGEST BORROW.**
`.coderabbit.yaml` is the cleanest working example the corpus has of making a prose policy enforceable:

```yaml
knowledge_base:
  code_guidelines:
    enabled: true
    filePatterns:
      - files: "AGENTS.md"
        applyTo: "**"
```

plus a repo-wide instruction that says *"treat it as mandatory policy, not optional style guidance"*, plus per-directory focus lists. The vault has `CLAUDE.md`, `_state/`, `_patterns/` — and nothing that enforces any of it. Copy the **binding**, not the vendor: the same shape works as a `/code-review` instruction block or a review skill.

**B3. Lift the fail-loudly rule (15 min).** Three instances in one repo: `fail_commit_status: true` (*"a throttled review is indistinguishable from a clean one"*), `_coerce_bool` raising on `'ture'`, ruff selecting `S307`/`S102`. Add the principle to `hireui/evals/METHOD.md`: **a check that cannot fail is worse than no check** (v262's rule, independently rediscovered here).

**B4. The basis-declaration habit (10 min).** README: *"This is a representative list."* `pytest.ini` declares `testpaths`. Both state their own basis. Apply to the vault's own count-drift problem — and to `_state/03c-projects-v61-v183.md`, whose filename still says `-v183` while it holds entries through v281.

---

## C. Local run (install, fenced, ~$0)

**C1. Offline smoke run (45 min, ~$0).**
```bash
git clone https://github.com/Comfy-Org/ComfyUI.git && cd ComfyUI
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python main.py --cpu --disable-api-nodes
```
Verified safe from the code: binds `127.0.0.1` (`cli_args.py:63`), makes no outbound request at startup (`frontend_management.py:370` returns the local pip package), and `--disable-api-nodes` severs the `api.comfy.org` path. With no models present it will start and have nothing to run — which is the point: you are testing the offline claim, not generating images.
⚠️ `torch` is unpinned in `requirements.txt`; expect a large download and use a throwaway venv.

**C2. Run its own test suite (30 min).** `python -m pytest tests-unit` — the 1,141 that CI runs. Then `python -m pytest` bare and watch it collect **1,301**, including the 21 CI never sees. That contrast *is* the finding.

**C3. Read the `ClaudeNode` (20 min).** `comfy_api_nodes/nodes_anthropic.py` — 320 lines, nine current models, Messages API, graceful safety-refusal handling at `:307`. A compact reference implementation of a vendor node routed through a broker.

---

## D. Deliberately excluded

**D1. Custom nodes — DO NOT.** `nodes.py:2263` executes them as arbitrary Python. The project says so; believe it.
**D2. `--listen` — DO NOT.** Bare `--listen` binds `0.0.0.0,::` and **there is no authentication of any kind**.
**D3. API nodes — not for this vault.** They route through `api.comfy.org` on a Comfy Org account with `X-Comfy-Credits-Used` billing. Real money, no benefit here.
**D4. hireui integration — NO.** GPL-3.0 and wholly off-domain. Nothing about this engine belongs in a recruitment product.
**D5. Model downloads — skip.** Tens of GB, and every idea worth taking is in the text.

---

## Recommended path

**A1 → A2 → B1 → B2.** About two hours, zero installs, and it ends with two artifacts the vault does not currently have: a written AI-provenance policy, and a `CLAUDE.md` that something actually enforces. Add **C1** only if you want to confirm the offline claim with your own eyes rather than mine.
