# Firewall / WAF — signature-based L7 defense-in-depth, not a solution

## Source

Video technique #4. Verified against the AWS WAF Developer Guide + FAQ, the OWASP ModSecurity Core Rule Set project, OWASP XSS/SQLi evasion pages, and Cloudflare's WAF Learning Center.

## What the video says (accurate parts)

- A firewall is the "gatekeeper" between incoming traffic and your API; a **WAF** inspects requests and blocks those matching known attack patterns (suspicious SQL keywords, strange HTTP methods).
- Don't build your own — use a managed service (**AWS WAF**, **Cloudflare**). *(Good advice: managed > custom.)*

## Canonical corrections

**Verdict: CORRECT-BUT-INCOMPLETE.** The description is accurate; the framing ("use AWS WAF / Cloudflare" as *the* firewall step) is missing four caveats.

1. **WAF is not a complete solution.** AWS's own docs: WAF "is meant to be used in conjunction with other network perimeter security solutions." It's **one L7 layer** in defense-in-depth alongside network ACLs/security groups (L3/L4), DDoS protection (AWS Shield), rate limiting, authn/authz, and secure code.

2. **WAF is signature-based and evadable.** It matches known patterns, so it has **false positives** (blocks legitimate traffic → needs tuning) and **false negatives** (attackers bypass via UTF-8/hex encoding, base64, obfuscation, alternate event handlers). OWASP's XSS/SQLi evasion catalogs exist precisely because signatures don't understand intent.

3. **WAF ≠ network firewall.** The video lumps "firewall" as one thing. A **WAF operates at Layer 7 (HTTP)**; a **network firewall operates at Layer 3/4** (ports, protocols, network-layer DDoS). Different threat classes. AWS separates them explicitly: WAF for L7, Shield for L3/4 DDoS, Security Groups for network access.

4. **WAF cannot see application logic.** It cannot detect **authorization bypasses (BOLA/BFLA)**, race conditions, or workflow flaws — which are the dominant real API risks ([[what-the-videos-miss-owasp-api-top-10]]). A WAF would happily pass `GET /api/candidates/456` from a user who should only see `123`.

## Correct model

WAF = a useful **perimeter signal + virtual-patching layer** (buys time before you fix code), deployed as a **managed service**, **tuned per app**, as **one layer** among network controls, rate limiting, and — most importantly — secure code and authorization. It is a complement to, never a replacement for, the app-code defenses in the other articles.

## hireui relevance

- **Recon finding:** deploy target is **ambiguous** — the repo has both `vercel.json` (active per recon) *and* `appspec.yml` (AWS CodeDeploy) + Dockerfile + compose. **Confirm the real production edge before choosing a WAF.** Vercel provides platform DDoS mitigation and can front Cloudflare; AWS would use AWS WAF on CloudFront/ALB.
- WAF is a **later** priority for hireui (a scaling/attack-driven decision), *behind* authorization (BOLA), rate limiting, and parameterized queries. See the pilot menu's Tier-C "WAF escalation trigger."

## Key Takeaways

- WAF is **evadable, signature-based L7 defense-in-depth**, not a complete solution.
- **WAF (L7) ≠ network firewall (L3/4)** — the video conflates them.
- A WAF **cannot stop authorization bugs** — the biggest real API risk.
- Managed > custom (the video's one clean win). Deploy it *and* fix the code.
