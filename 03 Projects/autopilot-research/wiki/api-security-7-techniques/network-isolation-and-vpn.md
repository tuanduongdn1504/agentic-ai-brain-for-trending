# Network isolation & VPN — "network location is not identity"

## Source

Video technique #5. Verified against NIST SP 800-207 (Zero Trust Architecture), OWASP API Security guidance, and cloud private-networking docs (AWS VPC/security groups).

## What the video says (accurate parts)

- Some APIs are internal (admin dashboard, HR, accounting) and shouldn't be reachable from the public internet.
- Put them behind a **VPN**: only users inside the private network can reach the API; external users are blocked. *(The goal is right; internal APIs should not be publicly reachable.)*

## Canonical corrections

**Verdict: CORRECT-BUT-INCOMPLETE.** VPN-as-the-answer is a legacy, perimeter-trust model.

1. **Network location is not identity (NIST Zero Trust).** SP 800-207 explicitly rejects trusting a request because it arrived on a "privileged" network: *users/devices should not be trusted by default even on a corporate LAN.* A VPN provides **reachability + encryption in transit** — it does **not authenticate or authorize** the request.

2. **VPN alone leaves you open to insiders and compromised clients.** Anyone with valid VPN credentials (employee, contractor, a stolen laptop, a compromised VPN client) is "inside" and can hit every internal API. Without per-request authn/authz, one foothold = lateral movement across all internal services.

3. **You still need authn + authz on internal APIs.** Defense-in-depth = **network isolation** (VPC/private subnets/security groups) **+ authentication** (OAuth2/JWT on every internal endpoint) **+ authorization** (role/tenant checks — the same BOLA/BFLA discipline as public APIs).

4. **Cloud SaaS uses different primitives than "a VPN."** For a cloud-hosted product the modern stack is **VPC + private subnets + security groups + an identity-aware proxy / API gateway** (BeyondCorp-style zero-trust), not a legacy corporate VPN. VPN is *one* option, and the least identity-aware one.

## Correct model

- **Internal ≠ trusted.** Treat internal APIs with the *same* authn/authz rigor as public ones; network isolation just shrinks the attack surface.
- **Layer, don't substitute:** VPC/private networking (reachability) + IAM/OAuth (identity) + role/tenant authorization (access).

## hireui relevance

- **Recon finding:** hireui is a **public multi-tenant SaaS**, not an internal-only system — so a corporate VPN is largely **N/A** (Skip). The video's VPN advice maps, for hireui, onto: **role-guard admin endpoints** (`/api/admin/*` → `if user.role !== 'admin' → 403`) and, if truly-internal tooling emerges (bulk exports, salary reports), isolate that to a separate service with VPC + IAM. Network location must never be the only gate.
- This is where the videos' "network control" advice quietly re-routes to the **authorization** work they never named ([[what-the-videos-miss-owasp-api-top-10]]).

## Key Takeaways

- **VPN = reachability + encryption, not identity.** Necessary-not-sufficient.
- NIST Zero Trust: don't trust a request because of *where* it came from.
- Internal APIs need the **same authn/authz** as public ones.
- For cloud SaaS, prefer **VPC + security groups + IAM/identity-aware proxy** over a legacy VPN; for hireui, **role-guard admin routes** is the practical form.
