# Off-the-shelf vs hand-built skills

The corpus's sharpest disagreement axis. Direct relevance to the vault's interest in skill-distribution ecosystems ([[external|Storm Bear: agent-skills-standard (v76)]]).

## Source

- Raw: [`raw/2026-05-29-ai-operating-system-5-skills-framework.md`](../../raw/2026-05-29-ai-operating-system-5-skills-framework.md), §Outliers-2

## The disagreement

The corpus splits cleanly into two camps on where skills should come from:

### Camp A — Pre-built / marketplace (N=2+)

**Ben AI** explicitly provides a **zip file of skills** for users to "copy and paste for free." Treats skills as **distributable artifacts**.

**Mani Kanasani** highlights the **vast ecosystem of thousands of open-source skills** available for **one-line installation** via tools like `npx playbooks`. Treats skill marketplaces as legitimate dependency-management infrastructure.

### Camp B — Build your own (Ross Mike, the contrarian)

Ross Mike's position is the strongest contrarian stance in the corpus:

> **"I don't install skills... I don't download skills"**

Reasoning:
- Pre-made skills lack the **specific context of a successful run** in the user's unique workflow
- Generic skills produce generic outputs
- Each operator's skill IP is **the trace of their actual successful runs**, not abstract best-practices

His receipt: he admits to **posting his own skill on GitHub just to get "stars"** while explicitly telling his audience: **"Do not download it... do not use it."**

This is the corpus's most-charged stance — Ross Mike is signaling that the **entire skill-marketplace ecosystem** is performative, not functional.

## Why this matters for vault

Storm Bear has explicitly invested in **portable skill standards**:

- `agent-skills-standard` (v76) — codifies the cross-vendor format
- Storm Bear's own `05 Skills/` curation cycle — locally-authored skills

If Ross Mike is right, the **portable-skill ecosystem is partly performative**. If Camp A is right, **skill marketplaces are the natural maturation of the field** (like npm for JS, pip for Python).

The reconciliation likely depends on **which skills**:

| Skill type | Ross Mike's view | Reasonable accommodation |
|---|---|---|
| Domain-specific (your workflow) | Build yourself — pre-built loses context | Camp A doesn't disagree; pre-built skills here are starting points, not endpoints |
| Tool-specific (e.g., gcloud-deploy) | Probably build-from-scratch | Pre-built may be acceptable IF you customize per-deploy |
| Format-specific (e.g., output-as-spreadsheet) | Marketplace OK | Pre-built is fine; the skill is mechanical |
| Methodology (e.g., security-review) | Marketplace OK | Pre-built encodes industry best-practice; legitimate to import |

So Camp A and Camp B may actually agree on a **gradient**:
- Mechanical / methodological skills → marketplace OK
- Domain / workflow skills → build via successful runs (Ross Mike's recipe)

## Build-via-failure as the intermediate path

[[skills-architecture-progressive-disclosure]] §Build-via-failure documents Ross Mike's authoring recipe:

1. Run the workflow manually
2. Let the agent fail
3. Correct
4. Codify the successful run

This produces skills that are **provably real for this operator** — pre-built skills can't make the same claim.

A balanced posture: **start with marketplace skills** for mechanical work; **build-via-failure** for everything domain-specific.

## The "stars-only" critique applied to vault

Ross Mike's "posting just for stars" critique is a **falsifiability test** any skill-marketplace should pass:

| Test | If yes → marketplace skill is real |
|---|---|
| Does the author USE it themselves in their own workflows? | YES |
| Are the example invocations from real operator runs, not toy examples? | YES |
| Does it ship with a worked example? | YES |
| Has it been updated recently? | YES — drift is real |
| Does the author respond to issues? | YES — distribution is a commitment |

Storm Bear's `05 Skills/` curation cycle has historically demanded most of these (skill files are usage-driven; `SKILL_LOCK_POLICY.md` tracks active vs archived). The pattern is sound.

## How to read the corpus on this

Both camps are partly right. The actionable synthesis:

1. **Skills marketplaces are real infrastructure** — don't dismiss them as Camp B implies
2. **Most operator-critical skills should be hand-built via successful runs** — Camp B's stronger claim
3. **Apply Ross Mike's falsifiability tests** to any marketplace skill before adopting
4. **Build-via-failure is the right authoring discipline** regardless of camp affiliation

## Vault implications

- Continue investing in `agent-skills-standard` (v76) — it's real ecosystem infrastructure
- For Storm Bear's own `05 Skills/`, prefer **build-via-failure-from-vault-workflows** over importing generic skills
- Track which skills come from where (`05 Skills/SKILL_LOCK_POLICY.md` already does this)
- For any skill imported from a marketplace, **run Ross Mike's tests** before promoting to active use

## Key Takeaways

- **The corpus's sharpest disagreement** — Camp A pro-marketplace vs Ross Mike's anti-distribution stance
- **Camp B's strongest argument**: pre-built skills lack the operator's unique-workflow context
- **Reconciliation**: marketplace OK for mechanical/methodological skills; build-via-failure for domain skills
- **Ross Mike's falsifiability tests** are a useful screening tool for any marketplace skill
- **Vault's posture**: continue investing in skill-distribution standards while preferring build-via-failure for operator-critical skills

## Related

- [[overview]] — AIOS framing
- [[skills-architecture-progressive-disclosure]] — build-via-failure recipe
- [[instruction-layer-markdown-files]] — Ross Mike's anti-heavy-context position complements his anti-marketplace stance
- [[../claude-cowork/skills-to-plugins-pipeline]] — sister-topic codify-after-success pattern (Bart Slodyczka)
- [[external|Storm Bear: agent-skills-standard (v76)]] — the vault's curated cross-vendor skill format
- [[external|Storm Bear: ECC (v78)]] — 232-skill operator system as Camp A's maximal expression
