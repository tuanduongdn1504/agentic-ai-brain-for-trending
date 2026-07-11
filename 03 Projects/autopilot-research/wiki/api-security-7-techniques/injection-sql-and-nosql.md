# Injection — SQL and NoSQL are different beasts

## Source

Video technique #3. Verified against the OWASP SQL Injection Prevention Cheat Sheet, OWASP Input Validation Cheat Sheet, the OWASP NoSQL / SQL-Injection community pages, and PortSwigger's NoSQL-injection material.

## What the video says (accurate parts)

- Injection happens when user input is concatenated directly into a query without validation. The `--` comment trick disables the password check so any valid username logs in; worst case the attacker reads/modifies/drops all data. *(Classic, correct, well-illustrated.)*
- Fix: **"always use parameterized queries or ORM safeguards."**

## Canonical corrections

**Verdict: MISLEADING** — because it presents "parameterized queries **OR** ORM" as interchangeable, and applies one fix to two different attack classes.

1. **Parameterized queries / prepared statements are the #1 defense — not equivalent to "use an ORM."** OWASP's priority order: (1) prepared statements/parameterized queries, (2) safely-implemented stored procedures, (3) allow-list input validation (secondary only), (4) escaping (**"strongly discouraged"**). ORMs are a *valid tool that generates parameterized queries for you* — **but only when used correctly.** The moment a developer drops to `$queryRawUnsafe`, `.raw()`, a string-interpolated query builder, or `sequelize.query('...' + input)`, ORM protection evaporates. ORM ≠ automatic safety; it requires discipline.

2. **Input validation is a *secondary* defense.** OWASP: "Input validation should not be used as the primary method of preventing SQL injection." It complements parameterization (and is required for the parts that *can't* be parameterized — table/column names).

3. **NoSQL injection is a different attack the SQL fix does not cover (major).** SQL parameterization does nothing against **operator injection**: passing `{"$ne": null}`, `{"$gt": ""}`, or `{"$where": "…JS…"}` where the app expected a string. Example: `db.users.find({ email: req.body.email, password: req.body.password })` — send `password: {"$ne": null}` and you match any user. NoSQL defenses are distinct:
   - **Type-check / schema-validate** every input (reject objects where you expected a string).
   - **Operator allow-listing** (reject keys starting with `$`).
   - **Disable server-side JavaScript** (`$where`, `mapReduce` with JS) unless strictly needed.
   - Use the driver's typed query objects, never string-built queries.

4. **Least-privilege DB accounts** are a critical complementary control the video omits (a read-only account for list queries can't `DROP`).

## Correct model

Injection ≠ one fix. **SQL → parameterize (primary) + validate (secondary) + least privilege.** **NoSQL → type/schema validation + operator allow-list + disable JS eval.** WAF signatures ([[firewall-and-waf]]) catch *some* payloads but are evadable and are not a substitute for parameterization.

## hireui relevance

- **Recon finding:** the frontend repo has **no ORM** (it's a Next.js client calling a separate backend) — so injection risk lives on the **backend**. One frontend smell was found: `searchLocation(name)` interpolates `?name=${name}` directly into the URL (`AccountLocation.service.tsx:57`) while sibling services correctly use axios `params: { name }`. That's not SQLi (it's the backend's job to parameterize) but it's an inconsistent, injection-adjacent habit worth fixing.
- **Action:** on the backend, grep for raw-query escape hatches; if MongoDB is used anywhere, add operator allow-listing + schema validation. Add a TDD test that injects `' OR '1'='1` and `{"$ne":null}` and asserts zero/expected results (see the Scrum angle in the pilot menu).

## Key Takeaways

- **Parameterized queries are primary; "use an ORM" is only safe if you never escape the ORM.**
- **NoSQL injection is a separate attack** — operator injection — that SQL parameterization does not fix.
- Input validation is a *secondary* layer; least-privilege DB accounts limit blast radius.
- Test injection, don't assume the ORM handles it.
