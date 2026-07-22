# HTTP semantics & REST conventions

**Source:** NotebookLM digest of 6 API-types videos (LetDiv, Codist, ByteByteGo, Ulbi TV, Be A Better Dev, Learn with Whiteboard)

REST is an **architectural style**, not a protocol. It sits on top of HTTP and codifies how to use HTTP's methods, status codes, and statelessness to build predictable, scalable web APIs. This article covers the conventions that distinguish well-behaved REST APIs from careless HTTP wrappers.

---

## HTTP Methods → CRUD Operations

The **semantic contract** between client and server: each standard HTTP method performs a specific class of operation.

| Method | Operation | CRUD | Idempotent | Safe |
|---|---|---|---|---|
| **GET** | Retrieve a resource | Read | ✓ Yes | ✓ Yes |
| **POST** | Create a new resource | Create | ✗ No | ✗ No |
| **PUT** | Replace entire resource | Update | ✓ Yes | ✗ No |
| **PATCH** | Partial update | Update | ✗ No* | ✗ No |
| **DELETE** | Remove a resource | Delete | ✓ Yes | ✗ No |

*PATCH **can** be designed idempotent, but is not idempotent by definition (unlike PUT/DELETE).

**Why semantics matter:** A GET request that creates side effects (e.g. consuming a credit or recording a log) violates the contract. Browsers and proxies assume GET is safe and may cache or retry it. POST, by contrast, signals "this changes state" and gets different cache / retry treatment. (Codist, LetDiv, Ulbi TV)

---

## PUT vs. PATCH (the critical distinction)

- **PUT:** Replaces the entire resource with the request body. If you send `{"name": "Alice"}` and omit `email`, the updated resource will have no email field (or it reverts to null/default).
- **PATCH:** Applies a partial update. Only the fields in the request body are changed; omitted fields retain their current values.

**Example:**
```
Resource: {"id": 1, "name": "Bob", "email": "bob@example.com"}

PUT /resource/1 with {"name": "Alice"}    → {"id": 1, "name": "Alice"}  (email gone)
PATCH /resource/1 with {"name": "Alice"}  → {"id": 1, "name": "Alice", "email": "bob@example.com"}
```

**Consequence:** PUT is idempotent (same full replacement every time). PATCH is **not** idempotent by definition (it depends on current state). If your API uses PATCH, document whether it's idempotent in practice. (Ulbi TV)

---

## Idempotency (and what it really means)

**Idempotent operation:** Multiple identical requests produce the same **server state** as a single request.

- **GET, PUT, DELETE** are idempotent by design.
- **POST is not** (sending the same POST twice creates two resources).

**Critical nuance:** Idempotency guarantees **state**, not **response**.

A DELETE request is idempotent:
- First call: returns `204 No Content` (deleted)
- Second call: returns `404 Not Found` (already gone)

Same server state achieved both times (resource gone), but different HTTP responses. A naive retry mechanism that checks "did I get the same response code?" will see the divergence and incorrectly assume the second call failed. **Idempotent ≠ idempotent response codes.** (RFC 7231 Section 4.2.2)

**Assumption:** Idempotency assumes identical request bodies. A PUT with `{"balance": 100}` then `{"balance": 200}` rightfully yields different states.

---

## Statelessness (the architectural bedrock)

Each request must be **self-contained**. The server must not rely on stored context from a prior request (session state inside the server).

- ✓ Client sends authentication token in every request (token is self-contained data).
- ✗ Server stores "user is logged in" in session memory and expects subsequent requests to reference that session.

**Why:** Statelessness enables **horizontal scaling**. Request N can land on any server; no server has irreplaceable state about a client. Replication, failover, and load-balancing all become trivial. (LetDiv, Codist, Learn with Whiteboard)

---

## Resource Naming & Versioning

### URI Conventions

- **Nouns, not verbs:** `/users/123` (resource), not `/getUser/123` (operation). REST uses HTTP methods to express the operation; the URI names the resource.
- **Hierarchies respected:** `/projects/42/tasks/7` (task 7 within project 42), not `/tasks/7?project=42`.

### Breaking Changes → New Version

When introducing non-backwards-compatible changes, signal via the API path:

- **v1:** `/api/v1/users/123` returns `{"id": 123, "name": "Alice", "role": "admin"}`
- **v2:** `/api/v2/users/123` returns `{"id": 123, "name": "Alice", "role": "admin", "permissions": ["read", "write"]}` OR removes a field entirely.

Existing clients continue hitting `/api/v1/`; new clients adopt `/api/v2/`. No forced migration. (Takeaways item #10, Ulbi TV)

---

## Documentation & Contract

### OpenAPI / Swagger

The **machine-readable contract** between server and client. OpenAPI is a standard format (formerly Swagger). It specifies:

- Every endpoint (method + path)
- Request parameters (query, body, headers)
- Response schemas (HTTP codes + body structure)
- Security requirements (API keys, OAuth, etc.)

Tools then auto-generate:
- Interactive documentation (try-it-now dashboards)
- Client SDKs (libraries to call the API)
- Server scaffolds (route handlers with validation)
- Contract tests (verify both sides match)

**Why:** Without a contract, clients guess. Clients guess wrong. Versions diverge silently. OpenAPI prevents this. (Ulbi TV)

---

## Status Codes (semantic signals)

REST doesn't invent status codes; it uses HTTP's. Key signals:

- **2xx Success**
  - `200 OK` — request succeeded, response body contains result
  - `201 Created` — POST succeeded, resource created, URI in `Location` header
  - `204 No Content` — request succeeded, no body to return (common for DELETE)

- **3xx Redirection**
  - `301 Moved Permanently` — resource permanently at new URI
  - `304 Not Modified` — client's cached copy is fresh

- **4xx Client Error**
  - `400 Bad Request` — malformed request (invalid JSON, missing required field)
  - `401 Unauthorized` — not authenticated
  - `403 Forbidden` — authenticated but not authorized for this resource
  - `404 Not Found` — resource does not exist
  - `409 Conflict` — request conflicts with current state (e.g., duplicate email on creation)

- **5xx Server Error**
  - `500 Internal Server Error` — something broke on the server
  - `503 Service Unavailable` — server temporarily down (client may retry)

Clients depend on these codes. Misusing them (e.g. returning 200 for an error) breaks tooling.

---

## Key Takeaways

- **HTTP methods encode semantics:** GET reads (safe + idempotent), POST creates (neither), PUT replaces (idempotent), PATCH updates partially (not idempotent by definition), DELETE removes (idempotent).
- **PUT replaces entirely; PATCH is partial.** Omitted fields in PUT disappear; omitted fields in PATCH are untouched.
- **Idempotency guarantees server state, not response codes.** DELETE returning 204 then 404 on repetition is still idempotent—same final state (gone), different responses.
- **Statelessness = horizontal scalability.** Each request carries all needed context (auth tokens, IDs); no server stores session state.
- **Versioning (/v1 vs /v2) decouples client migration from server deployment.** Non-breaking changes reuse the same version; breaking changes get a new path.
- **OpenAPI/Swagger is the contract.** Machine-readable + human-readable specification prevents client–server divergence and enables tooling (SDKs, documentation, contract tests).
- **Status codes are not suggestions.** Use 4xx for client error, 5xx for server error, 2xx for success. Clients and proxies depend on these semantics.
