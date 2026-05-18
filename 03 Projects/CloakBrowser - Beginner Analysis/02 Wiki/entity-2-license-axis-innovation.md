# Entity 2 — License-axis innovation: MIT wrapper + Proprietary Binary with Acceptable Use

> The v69 wiki's central license-axis observation: corpus-first dual-license-by-artifact-scope with Acceptable Use enumeration

## Two license files in repo root

CloakBrowser is the **corpus-first subject with two separate license files** at repo root:

```
LICENSE                  ← MIT (for wrapper source code)
BINARY-LICENSE.md        ← Proprietary + Acceptable Use (for compiled binary)
```

Compare corpus prior Pattern #45 Dual-Licensing exemplars:
- **Unsloth v23 (45a):** Apache-2.0 in single LICENSE file with commercial-use clauses inline
- **AutoGPT v59 (45b):** MIT with PolyForm-Shield-Restrictions in single LICENSE file
- **CloakBrowser v69 (45c):** **TWO SEPARATE LICENSE FILES** with artifact-scope split

The 2-file structure is structurally distinct from 45a/45b. In 45a/45b, **the same artifact (source) has hybrid clauses**. In 45c, **different artifacts have different licenses entirely.**

## License-scope mapping

| Artifact | License | Distribution channel |
|----------|---------|---------------------|
| Python wrapper source code | MIT | GitHub repo + PyPI |
| JavaScript wrapper source code | MIT (implied; not separately documented) | GitHub repo + npm |
| Compiled Chromium binary | **Proprietary + Acceptable Use** | GitHub Releases + cloakbrowser.dev |
| Docker image | (combination — implied wrapper MIT + binary proprietary) | Docker Hub |
| ungoogled-chromium upstream | BSD-3-Clause (transitive) | (upstream-attributed) |
| Chromium upstream | BSD-3-Clause (transitive) | (upstream-attributed) |

The **artifact-scope split** is intentional: users can fork the wrapper code (MIT permits modification + redistribution) but cannot redistribute or modify the binary (proprietary). This protects the patch-IP investment while keeping the wrapper code OSS.

## BINARY-LICENSE.md — 17 distinct clauses

Counting the structural elements of BINARY-LICENSE.md:

1. **Intellectual Property** — upstream attribution (Chromium + ungoogled-chromium)
2. **Grant of Use** — broad personal/commercial usage
3. **Restrictions** — 5 explicit prohibitions
4. **Cloud/Container/Integration Use** — internal-use carve-out
5. **Official Distribution** — channel discipline
6. **Trademark Notice** — name/logo limited to nominative use
7. **Attribution** — opt-in, "Powered by CloakBrowser" notice
8. **Acceptable Use** — 4 enumerated prohibited use cases
9. **Indemnification** — user assumes legal exposure for unlawful use
10. **Disclaimer** — standard "AS IS" disclaimer
11. **Limitation of Liability** — **$100 max aggregate liability cap (corpus-rare)**
12. **Data Collection** — no telemetry; explicit
13. **Updates** — no obligation
14. **Termination** — automatic on license violation
15. **Governing Law** — jurisdiction-floating
16. **Reservation of Rights** — catch-all
17. **Entire Agreement / No Waiver / Assignment / Severability** — standard contract scaffolding

This is **corpus-broadest legal scaffolding** at clause-count for a single license file. → OC-J "Acceptable-Use Enumeration as Risk-Mitigation Layer" observational candidate.

## The 4 Acceptable-Use prohibitions (corpus-first explicit enumeration)

> *"Without limiting the above, the following uses are expressly prohibited:*
> *- Unauthorized access to financial, banking, healthcare, or government authentication systems*
> *- Credential stuffing, brute-force login attempts, or automated account creation*
> *- Circumventing authentication on systems you do not own or have authorization to test*
> *- Any activity that constitutes fraud, identity theft, or unauthorized data collection"*

These enumerations are **legal-axis defensive** — they specifically address known attack vectors that bot-detection-evading tools are commonly misused for. By explicitly prohibiting these in the license + naming them as outside grant-of-use, CloakHQ:
1. **Reduces secondary liability** for user actions (claim: "we explicitly prohibited it")
2. **Signals legitimate-use intent** to regulators / lawyers / journalists
3. **Provides termination grounds** if a user is found to be violating

Prior corpus Pattern #45 instances did NOT have explicit prohibited-use enumeration. Unsloth v23 (45a) and AutoGPT v59 (45b) have liability disclaimers and standard "AS IS" framing but no prohibited-use enumeration.

→ **45c distinguishing mechanism #1: Acceptable Use enumeration**

## The $100 max-aggregate-liability cap (corpus-rare)

> *"CLOAKHQ'S TOTAL AGGREGATE LIABILITY SHALL NOT EXCEED ONE HUNDRED US DOLLARS (US $100)."*

This clause is **corpus-rare**. Most OSS license shapes use unbounded "AS IS, NO LIABILITY" framing. The $100 cap is more typical of B2B contractual SaaS agreements than OSS license files. Implications:
1. **Defensive against statutory damages** in some jurisdictions where "no liability" disclaimers are unenforceable
2. **Signals B2B revenue model** — separate OEM/SaaS licensing carries actual liability commitments
3. **Acknowledges nonzero baseline risk** that pure "AS IS" framing doesn't capture

→ **45c distinguishing mechanism #2: Bounded max-aggregate-liability**

## OEM/SaaS licensing carve-out (B2B revenue gate)

> *"OEM/SaaS license required — Bundling, embedding, or pre-installing the Binary into a product, hosted service, or cloud artifact distributed to third parties requires a separate OEM license. This includes running the Binary on your infrastructure to serve third-party customers (e.g., browser-as-a-service). Contact cloakhq@pm.me for OEM/SaaS licensing."*

This is the **primary revenue mechanism**. Free for direct use; commercial license required for embedding into third-party-distributed products. Distinguishing properties:
- **Use case discrimination** — same artifact, different terms based on downstream distribution
- **B2B revenue gate** — implicit market segmentation (free for end-users; paid for product-embedders)
- **Anti-piracy via license-violation termination** — non-compliant OEM use causes automatic license termination

→ **45c distinguishing mechanism #3: OEM/SaaS commercial-licensing carve-out**

## Internal-use carve-out (operational pragmatism)

> *"Internal use — You may store and run the unmodified Binary within internal infrastructure, including Docker images, VM templates, CI runners, container registries, and artifact repositories (e.g., Artifactory, Nexus), solely for your organization's internal operational purposes."*

This carve-out reduces friction for enterprise IT compliance:
- Permits caching in internal artifact repositories (Artifactory/Nexus)
- Permits VM/Docker image baking with the binary pre-included (for internal CI)
- Permits Docker image distribution within org boundary

But does NOT permit:
- Distribution of the binary OUTSIDE the organization
- Selling internal Docker images with the binary baked-in
- Hosting the binary on a public artifact mirror

→ **45c distinguishing mechanism #4: Internal-use carve-out with explicit boundary**

## Why these 4 mechanisms aggregate to a new sub-typology

Pattern #45 was promoted at v60 audit on the basis of N=2 structural-similarity (45a Unsloth + 45b AutoGPT — both single-file hybrid licenses with commercial-protection clauses).

CloakBrowser at v69 adds a **structurally distinct mechanism cluster**:
1. **Two-file license-split** (artifact-scope basis)
2. **Acceptable Use enumeration** (defensive-explicit)
3. **Bounded liability ($100 cap)** (statutory-defensive)
4. **OEM/SaaS commercial-licensing carve-out** (B2B revenue mechanism)
5. **Internal-use carve-out** (operational pragmatism)
6. **Indemnification + Termination** (defensive scaffolding)

This is **substantively more legal-axis machinery than 45a/45b** — Pattern #45 needs a sub-typology to capture the distinction. → Phase 4b PRIMARY proposes 45c sub-typology registration.

## Cross-axis: ungoogled-chromium upstream attribution (Pattern #66 strengthening)

> *"The Binary is built on Chromium, which is open-source software by The Chromium Authors under the BSD 3-Clause License, and incorporates components from the open-source ungoogled-chromium project."*

Pattern #66 meta-supply-chain-awareness gets corpus-strongest evidence at v69:
- 3-level upstream chain (Chromium → ungoogled-chromium → CloakHQ patches) documented in license itself
- Explicit BSD-3-Clause transitive license attribution
- Telemetry-removal claim sourced from ungoogled-chromium (rather than CloakHQ claim alone)

→ Pattern #66 strengthening evidence at corpus-broadest 3-level-upstream-attribution shape.

## Storm Bear lessons from Entity 2

For the vault operator:

- **Artifact-scope license splits enable hybrid IP protection + OSS contribution.** If Storm Bear ever builds a hybrid product (OSS scaffolding + proprietary core), this 2-file pattern is a reusable template.
- **Explicit prohibited-use enumeration is defensive-honest.** Rather than vague "for legitimate purposes only" framing, enumerating the specific prohibited uses both clarifies intent and reduces legal exposure. This is the Pattern #83 honest-deficiency-disclosure discipline applied at license-axis.
- **OEM/SaaS carve-out is the primary revenue mechanism for dual-licensed OSS-with-proprietary-core products.** This is corpus-rare but a reusable B2B revenue pattern for tools that have low-friction direct use but high-value commercial embedding scenarios.
