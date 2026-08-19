# (C) Pilot Methods Menu — `diagram-design` (v250)

**Verdict: ⭐ INSTALL, fenced.** Rare for this corpus, and justified by a near-empty risk surface plus a live need (the vault publishes an HTML artifact per wiki ship). Rungs are ordered by increasing footprint. Every rung is independently useful; stop wherever the value runs out.

---

## Rung 0 — Ninety seconds, zero install, answers the only question that matters

**Do you actually like the output?** Nothing else about this project matters if the answer is no, and no amount of CI machinery substitutes for looking.

```bash
open "/private/tmp/claude-501/-Users-Cvtot-KJ-OS-Template/a56dd26d-b6f6-4c8d-b3e7-e32dd58b6c41/scratchpad/clone/dd1/skills/diagram-design/assets/index.html"
```

The repo is already cloned and verified at HEAD `5f1b6dd`. That opens the tabbed gallery: 39 tabs, 28 types, each in light / dark / full-editorial. Flip through them. **Cost: 0. Risk: 0.**

If you like them, continue. If you do not, stop here and take Rung 1 anyway — Rung 1 is worth more than the diagrams.

---

## ⭐ Rung 1 — Two hours, zero install, the highest-value rung

Three rules from this repo aimed at the vault's own standing disease: doc drift. This does **not** require the skill, or Python (⚠️ `python3` is SIGKILLed in this sandbox — exit 137 even for `print("hello")`; `node`, `perl`, `awk`, `sed`, `grep` work). Everything below is `grep`/`awk`.

### 1a. The decidability test — write it into `CLAUDE.md`

Read `verify-geometry.py:1-25` and `verify-treemap.py:1-15` (both in the clone). Then add to the vault's rules:

> **Before automating any quality rule, sort it: does violating it produce a *lie*, or merely something *worse*?** Only the first kind is gateable. Gate those; leave the rest as prose — and do not call prose rules "non-negotiable."

The subject's own criterion, verbatim, is the citation: *"Paint order is what makes this a defect rather than a stylistic choice"* (`verify-geometry.py:9`).

### 1b. ⭐ Make every inventory check bidirectional — the one with teeth

This is the vault's exact disease. `_state/03c-projects-v61-v183.md` holds entries through **v250** while its filename says **v183**; `CLAUDE.md`'s chapter index can name files that moved; `MEMORY.md` can lose a memory file.

The subject proves the principle inside one file: `verify-docs-sync.py:91-103` (`check_gallery`) runs **both** set-differences and catches a missing example; `:116-125` (`check_readme_tree`) runs only tree→disk, and its README tree is missing **14 of 28** type files and **21 of 28** scripts, green.

**Write `bin/verify-vault-inventory.sh`** — three bidirectional checks, no Python:

```bash
#!/usr/bin/env bash
# Bidirectional inventory checks for the vault. Exit non-zero on drift.
set -u; cd "$(dirname "$0")/.." || exit 2; fail=0

# 1. Every _state/*.md and _patterns/*.md chapter is named in its index, AND
#    every file the index names exists. BOTH directions — this is the whole point.
for f in _state/*.md _patterns/*.md; do
  grep -qF "$(basename "$f")" CLAUDE.md PATTERN_LIBRARY.md 2>/dev/null \
    || { echo "DRIFT: $f exists but no index names it"; fail=1; }
done
grep -oh '_state/[A-Za-z0-9._-]*\.md\|_patterns/[A-Za-z0-9._-]*\.md' CLAUDE.md PATTERN_LIBRARY.md \
  | sort -u | while read -r t; do
      [ -e "$t" ] || echo "DRIFT: an index names $t but no such file exists"
    done

# 2. Every memory file has a MEMORY.md line, and every linked file exists.
M="$HOME/.claude/projects/-Users-Cvtot-KJ-OS-Template/memory"
for f in "$M"/*.md; do
  b=$(basename "$f"); [ "$b" = "MEMORY.md" ] && continue
  grep -qF "$b" "$M/MEMORY.md" || { echo "DRIFT: memory $b is not in MEMORY.md"; fail=1; }
done

# 3. The filename-label check that would have caught -v183 (the v242 A1->C12->B7 idea).
for f in _state/03*-projects-v*.md; do
  label=$(echo "$f" | grep -o 'v[0-9]*\.md$' | tr -d 'v.md')
  newest=$(grep -o '^\*\*v[0-9]\+ ' "$f" 2>/dev/null | grep -o '[0-9]\+' | sort -n | tail -1)
  [ -n "$label" ] && [ -n "$newest" ] && [ "$newest" -gt "$label" ] \
    && { echo "DRIFT: $f is labelled v$label but holds entries through v$newest"; fail=1; }
done
exit $fail
```

Run it once. It should immediately report the `-v183` drift — which is the point: **the vault's oldest known doc defect has never been mechanically detected, only re-described in prose ship after ship since v239.**

### 1c. Put the number's authority where a human must amend it

From `docs/adr/0002`, the best sentence in the repo:

> *"a PR that edits them without amending this file has quietly made itself the authority… **the number in the test is just whatever the last contributor typed**."*

Apply it: wherever the vault hardcodes a count (46 patterns / 11 Library-vocab / 51 §C standalones), the line that states it must also state **who is allowed to change it and where the change must be recorded.** The v245 D32 notice already in `_state/03c` is the same move; extend it to the counts in `CLAUDE.md`'s Pattern Library block.

---

## Rung 2 — One hour, install, fenced

Install into Claude Code and generate one diagram of something you already understand well, so you can judge fidelity.

```bash
# In Claude Code:
# /plugin marketplace add cathrynlavery/diagram-design
# /plugin install diagram-design@diagram-design
```

**Fence:**
- **Pin 2.5.6** — the version reviewed here. Leave third-party auto-update **off** (it is off by default); refresh manually via `/plugin` after reading a diff.
- Set brand tokens **by hand** — edit `references/style-guide.md` directly (the README documents this) rather than running URL onboarding. This sidesteps the untrusted-page gap entirely at no cost.
- Budget **~11K tokens per diagram request** (`SKILL.md` 37,778 bytes + one type reference ≈ 5 KB).
- Verify each output with the checker that actually ships: `python3 <skill-dir>/scripts/self_check.py <file>` — ⚠️ **not runnable in this sandbox** (python3 is SIGKILLed); run it in a normal terminal.

**First diagram to ask for:** the vault's own wiki-ship pipeline (source → clone ×2 → fleet → contradiction → critic → hand-verify → docs → branch). You know whether it is right, which makes it a fidelity test rather than a demo.

---

## Rung 3 — Half a day, the real payoff

**Prefer the editable install** so package updates cannot overwrite your style guide:

```bash
git clone git@github.com:cathrynlavery/diagram-design.git ~/code/diagram-design
ln -s ~/code/diagram-design/skills/diagram-design ~/.claude/skills/diagram-design
```

Then use it where it earns its keep:

1. **Diagram the hireui candidate-LLM path** — the RATIFIED legibility ADR demands the path be legible to a human reviewer; a data-flow or sequence diagram of it is a direct artifact of that clause. Use the `data-flow` or `sequence` type. **Metadata and architecture only — never candidate data.**
2. **Diagram the vault's state architecture** — the `CLAUDE.md` shim → `_state/` chapters → `_patterns/` relationship, as a `nested` or `layers` diagram. This is the map that every failed subagent fan-out since v200 needed.
3. **Replace one Mermaid block** in an existing wiki artifact and compare side by side. The subject's `import-mermaid` path exists precisely for this: `/diagram-design:import-mermaid <file> --size=doc-wide`.

---

## 🔴 Never

- Point brand onboarding at a **candidate's, client's, or employer's** website. It fetches a live page into the agent's context and nothing in the repo treats that page as untrusted text.
- Put **candidate data** — names, CVs, scores, decisions — into a diagram. Diagrams are files that get shared.
- Cite this repo's **star/fork figures** as verified. Page-stated only; the GitHub API is mocked here (§37.4).
- Repeat *"27 diagram types"*. It is **28**, verified by enumeration. The 27 survives in `commands/import-drawio.md:25`, `commands/import-mermaid.md:25` and the GitHub description.
- Claim the skill **verifies your diagram's geometry**. It does not. `verify-geometry.py`, `verify-treemap.py` and `lint-skin.py` stay in the repo; what ships is `self_check.py` (389 lines: accessibility contract, single-file safety, motion) plus a 37-item prose checklist.
- Describe its six connector rules as enforced. **One of the six is.**
- Trust an 8% relative area tolerance as precision. `AREA_TOLERANCE = 8.0` is deliberately loose so their own 4px grid does not trip it.

---

## Recommended path

**Rung 0 → Rung 1 → decide.**

Rung 0 costs ninety seconds and settles taste. **Rung 1 is the rung that pays**, and it pays whether or not you ever install the skill: it converts the vault's oldest, most-re-described documentation defect — a state file whose filename has lagged its contents for eleven ships — into a script that fails. The subject proved the principle in a controlled experiment inside one 236-line file. Borrow the direction, not the diagrams.
