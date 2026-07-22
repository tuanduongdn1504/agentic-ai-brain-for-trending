# API types explained (REST, SOAP, GraphQL, gRPC, WebSocket, webhook)

**Notebook:** ed17cc3d-952c-4fe0-9572-27a418d0f390
**Sources:** 6 YouTube videos
**Generated:** 2026-07-21 (overnight orchestrator)
**Query:** `API types explained REST SOAP GraphQL gRPC websocket webhook`

## Sources

1. [20260717] **LetDiv - Học Lập Trình Đảm Bảo** — 7 Loại API Bạn Phải Biết: Giải Thích Đơn Giản 9 Phút!
   - https://www.youtube.com/watch?v=RsgyCswZBGA
   - 8,223 views, 12:38 duration
2. [20250927] **Codist** — Every Type of API Simply Explained in 9 Minutes!
   - https://www.youtube.com/watch?v=pBASqUbZgkY
   - 991,046 views, 9:53 duration
3. [20230512] **Learn with Whiteboard** — Difference Between REST API vs Web API vs SOAP API Explained
   - https://www.youtube.com/watch?v=2mqN7ZhDsUA
   - 489,737 views, 7:24 duration
4. [20231002] **Ulbi TV** — Что такое Rest API (http)? Soap? GraphQL? Websockets? RPC (gRPC, tRPC). Клиент - сервер. Вся теория
   - https://www.youtube.com/watch?v=XaTwnKLQi4A
   - 972,345 views, 57:30 duration
5. [20211118] **Be A Better Dev** — REST API (HTTP) vs Websockets - Concept Overview With Example
   - https://www.youtube.com/watch?v=fG4dkrlaZAA
   - 320,770 views, 7:07 duration
6. [20221110] **ByteByteGo** — What Is GraphQL? REST vs. GraphQL
   - https://www.youtube.com/watch?v=yWzKJPw_VzM
   - 530,138 views, 5:14 duration

---

## 1. Summary

The provided sources offer a comprehensive comparison of modern **API 
architectures** and **communication protocols** used to exchange data between 
software systems. **REST** is highlighted as the most popular, flexible 
architectural style for web services, while **SOAP** is described as a highly 
structured, secure protocol preferred by financial and government institutions. 
Emerging technologies like **gRPC** and **GraphQL** are examined for their high 
performance and efficiency, specifically in solving issues like over-fetching 
data or managing microservices. Additionally, the texts explain real-time 
interaction methods such as **Webhooks**, **WebSockets**, and **WebRTC**, which 
enable instant updates and peer-to-peer connectivity. Collectively, these 
materials serve as a technical guide for developers to choose the appropriate 
interface based on specific needs like **security**, **speed**, or **real-time 
functionality**.

---

## 2. Trends

Answer:
Across the sources, several dominant trends and shared patterns emerge regarding
API development. These focus on optimizing performance through binary protocols,
empowering clients with flexible data fetching, and utilizing specific tooling 
for documentation and real-time synchronization.

### 1. Performance Optimization through Binary Protocols
A major recurring theme is the tactical move away from text-based formats like 
JSON or XML toward **binary protocols** for high-performance systems.
*   **gRPC and Protocol Buffers:** Multiple speakers advocate for **gRPC** as 
the "Formula 1" of APIs due to its speed [1, 2]. **LetDiv**, **Codist**, and 
**Ulbi TV** all emphasize the use of **Protocol Buffers (Protobuf)**, which 
compresses data into a compact binary format that is 7 to 10 times faster to 
process than REST's JSON [1-4].
*   **HTTP/2 Advantage:** **LetDiv**, **Codist**, and **Ulbi TV** highlight that
gRPC leverages **HTTP/2**, allowing for multiple simultaneous requests over a 
single connection and supporting advanced communication patterns like 
**bidirectional streaming** [1, 2, 5, 6].

### 2. Client-Centric Data Control (GraphQL)
The sources frequently discuss the tactical shift from server-defined data to 
client-defined data to solve efficiency issues.
*   **Solving Overfetching and Underfetching:** **LetDiv**, **Codist**, 
**ByteByteGo**, and **Ulbi TV** all identify "overfetching" (receiving more data
than needed) and "underfetching" (not receiving enough data in one call) as 
primary weaknesses of REST [3, 7-9].
*   **The GraphQL Schema:** To address this, these speakers advocate for 
**GraphQL**, which uses a **schema** to define data types [8, 10]. This allows 
clients to write specific queries for exactly the fields they need, reducing 
bandwidth and improving mobile performance [7, 8, 11, 12].
*   **Tooling (Playgrounds):** **LetDiv**, **Codist**, and **Ulbi TV** point to 
the **GraphQL Playground** as a recurring tool of choice, providing 
self-documenting interfaces where developers can test queries instantly [7, 11, 
13].

### 3. Real-Time and Event-Driven Techniques
There is a shared emphasis on moving away from inefficient "polling" toward 
persistent or event-driven connections.
*   **WebSockets vs. Polling:** **Be A Better Dev** and **Ulbi TV** specifically
critique "short polling" (repeatedly asking the server for updates) as a 
resource-heavy and high-latency practice [14-16]. They advocate for 
**WebSockets** to establish a **full-duplex** or bidirectional line, allowing 
servers to push data to the client the moment an event occurs [17-19].
*   **Webhooks as "Reverse APIs":** For inter-system synchronization, **LetDiv**
and **Codist** highlight **Webhooks** as a critical tactical practice [20, 21]. 
They describe them as "reverse APIs" where the server calls the client via a 
**callback URL** immediately when a specific event (like a payment or code push)
happens [12, 20, 21].

### 4. Tooling for Documentation and Type Safety
Standardization and contract-based development are highlighted as essential for 
professional environments.
*   **REST Documentation:** **Ulbi TV** advocates for the use of **OpenAPI** 
specifications and **Swagger** to automatically generate and visualize API 
documentation, ensuring that the "contract" between client and server is clear 
[22].
*   **SOAP for Enterprise Reliability:** Despite being older, **SOAP** is 
consistently recommended by **LetDiv**, **Learn with Whiteboard**, and 
**Codist** for banking and government systems because of its strict **WSDL (Web 
Services Description Language)** contracts and built-in standards for security 
and error handling [23-26].
*   **Type Safety in RPC:** **Ulbi TV** introduces **tRPC** as a modern tooling 
choice for TypeScript developers, emphasizing "Type Safe" remote procedure calls
that maintain strict typing between the server and the client without manual 
synchronization [27, 28].

### 5. Architectural Principles (REST)
While discussing newer technologies, multiple sources reinforce the tactical 
foundations of **REST**.
*   **Statelessness:** **LetDiv**, **Learn with Whiteboard**, and **Codist** all
advocate for the **stateless** model, where every request is independent and 
contains all the information needed for the server to process it, which ensures 
scalability [29-31].
*   **Semantic HTTP Methods:** **LetDiv** and **Ulbi TV** emphasize the 
importance of using **standard HTTP methods** (GET, POST, PUT, DELETE) correctly
according to their intended semantics for CRUD operations [32, 33]

Resumed conversation: fc554d23-cded-4faf-a2bc-2427668a950d

---

## 3. Outliers

While the sources generally agree on the technical definitions of various API 
types, they diverge significantly on the practical suitability of certain 
architectures for specific use cases and the inherent risks of modern tools.

### 1. Suitability of REST for Real-Time Applications
A direct contradiction exists between speakers regarding whether REST is 
appropriate for real-time systems like chat or streaming.
*   **Learn with Whiteboard** claims that REST is "suitable for building 
applications that require **real-time communication**, such as chat applications
and streaming services" [1].
*   **Be A Better Dev** strongly disagrees, framing the REST "request-response" 
model as a **"primitive" and "outdated approach"** for chat [2, 3]. They argue 
that using REST for real-time requires "short polling," which is inefficient, 
causes latency, and puts undue "stress on your server and database" [4, 5]. They
advocate for WebSockets as the only viable professional alternative for these 
scenarios [6, 7].

### 2. The "Danger" and Hidden Costs of GraphQL
While most speakers present GraphQL as a modern evolution that solves REST’s 
efficiency problems, **ByteByteGo** provides a more contrarian and cautious 
take.
*   **LetDiv** and **Codist** focus almost exclusively on the benefits, such as 
the flexibility for front-end developers to get "perfect data every time" and 
the convenience of the "GraphQL Playground" [8, 9].
*   **ByteByteGo** identifies a **"great danger"** in this flexibility. They 
argue that allowing clients to define their own queries can lead to 
**"unexpected table scans"** that could "bring the database down" [10]. 
Furthermore, they argue that GraphQL requires a "sizable upfront investment" in 
heavy tooling that might **not be worth the cost** for simple CRUD applications 
[10, 11].
*   **ByteByteGo** also points out a technical disadvantage ignored by others: 
GraphQL is **"more difficult to cache"** than REST because it typically uses 
HTTP POST for everything, bypassing the well-defined caching behaviors of 
browsers and CDNs used by REST’s HTTP GET [11].

### 3. Divergent Categorization of "Web API"
The speakers disagree on the hierarchy and terminology used to classify these 
technologies.
*   **Learn with Whiteboard** treats "Web API" as a **"broader term"** that 
encompasses REST, SOAP, and XML-RPC [1]. In their view, a Web API is a general 
category that doesn't follow a specific architecture and can use various 
protocols like TCP/IP [12, 13].
*   **Ulbi TV** acknowledges the difficulty of grouping these terms, noting that
critics would be right to say that HTTP, REST, and GraphQL are **"completely 
different"** things (some being protocols, others architectural styles or 
languages) [14]. However, unlike Whiteboard, most other sources treat REST, 
SOAP, and gRPC as parallel "types" of APIs rather than sub-categories of a 
broader "Web API" bucket [15, 16].

### 4. Enterprise Necessity vs. Legacy Burden
There is a slight divergence in how speakers frame the use of **SOAP**.
*   **LetDiv** and **Codist** emphasize that SOAP is used because it is "formal"
and "strict," acting like a "business contract" that provides "absolute 
precision" for banks [17-19].
*   **Learn with Whiteboard** takes a more functional view, suggesting SOAP is 
simply a choice for when you need **"complex data structures"** and "advanced 
security" like digital signatures, without necessarily framing it as an "old" or
legacy requirement [20, 21]. 
*   **Ulbi TV** adds a specific nuance, noting that while many think XML is 
dead, it is still a **standard choice in fintech** specifically because of its 
structured nature, not just because of legacy inertia [22, 23].

### 5. Emerging Tooling: tRPC vs. gRPC
While **Codist**, **LetDiv**, and **Ulbi TV** all advocate for **gRPC** as the 
high-performance choice for microservices [24-26], **Ulbi TV** introduces a 
potential outlier in **tRPC**. 
*   **Ulbi TV** highlights **tRPC** as a "Type Safe" alternative that provides 
many of the benefits of RPC (like calling functions directly) but is optimized 
specifically for **TypeScript environments**, allowing for automatic type 
synchronization between client and server without the complex "Protobuf" setup 
required by gRPC [27, 28].

Conversation: fc554d23-cded-4faf-a2bc-2427668a950d (turn 1)

---

## 4. Gaps

While the sources provide a solid conceptual foundation and some implementation 
examples for various API types, they primarily focus on **architectural 
definitions, basic pros/cons, and core mechanics**. For a production-ready 
implementation, there are several critical operational and security gaps you 
should be aware of.

### Gaps in the Provided Sources

Based on the videos, the following areas are missing or only briefly mentioned, 
which are vital for production environments:

*   **Deep Security Implementation:** While the sources mention using headers 
for tokens [1] and SOAP’s support for encryption and digital signatures [2], 
they do not cover the industry-standard protocols for securing modern APIs, such
as **OAuth2** or **OpenID Connect**. There is no discussion on **JWT (JSON Web 
Token)** lifecycle management (signing, rotating keys, or revocation).
*   **Infrastructure and Deployment:** The sources explain that systems can have
multiple layers [3], but they do not detail how to manage these in production. 
Missing topics include the use of **API Gateways** for request routing, 
**Service Meshes** (like Istio) for microservice communication, and **Load 
Balancing** strategies beyond a high-level mention.
*   **Observability and Monitoring:** Although there is advice on testing 
queries in "playgrounds" [4, 5], the sources lack information on how to monitor 
APIs once they are live. Real-world production requires **distributed tracing** 
(to follow a request through multiple services), structured logging, and 
**health check** endpoints to ensure the system is running correctly.
*   **Resilience and Traffic Management:** Only **ByteByteGo** briefly warns 
about the "danger" of a single GraphQL query bringing down a database [6]. 
However, there is no broader discussion on **Rate Limiting**, **Throttling**, or
**Circuit Breakers**—essential techniques to prevent one bad client or a traffic
spike from crashing your entire infrastructure.
*   **API Governance and Testing:** **Ulbi TV** highlights documentation tools 
like **Swagger** [7], but production requires a more robust strategy for 
**Contract Testing** (ensuring changes don't break clients) and automated 
integration testing pipelines.

### 5-7 Specific Follow-up Topics for Investigation

To move from a conceptual understanding to a production implementation, the 
following topics (which are **not detailed in the sources**) are worth 
investigating:

1.  **API Security (OAuth2 & JWT):** Learn how to implement secure authorization
flows. Since the sources only mention "authorization headers" [1], you should 
independently verify how to securely issue, validate, and refresh tokens in a 
production environment.
2.  **API Gateway Architecture:** Investigate tools like NGINX, Kong, or AWS API
Gateway. These tools handle the "cross-cutting concerns" that the videos 
describe individually (like authentication, rate limiting, and protocol 
translation) in a centralized way.
3.  **Observability (The "Three Pillars"):** Research how to implement 
**Metrics, Logging, and Tracing** for your APIs. This is critical for debugging 
the performance gains promised by gRPC [8] or the complex query paths allowed by
GraphQL [9].
4.  **Resilience Patterns:** Look into **Circuit Breakers and Retries**. When 
implementing a "Formula 1" API like gRPC [10], you need to know how to 
gracefully handle the situation when a service becomes unavailable so the 
failure doesn't cascade.
5.  **Contract Testing:** While the sources advocate for documentation [7] and 
schemas [9, 11], investigate tools like **Pact** or **Postman collections** to 
automate the verification that your server and client actually adhere to those 
schemas during every deployment.
6.  **CI/CD for APIs:** Investigate how to automate the deployment of these 
different API types, including how to handle **blue-green deployments** or 
**canary releases** to ensure that new API versions [12] don't negatively impact
existing users.
7.  **Database Performance Tuning for APIs:** **ByteByteGo** mentions the risk 
of "unexpected table scans" [6]. Investigate how to optimize database indexing 
and query execution plans specifically for the flexible, nested data fetching 
allowed by GraphQL.

Conversation: fc554d23-cded-4faf-a2bc-2427668a950d (turn 1)

---

## 5. Takeaways

Based on the sources provided, here are 10 actionable rules and configurations 
for modern API development:

1.  **Enforce Strict REST Semantics:** Use standard HTTP methods correctly by 
utilizing GET for data retrieval, POST for creation, PUT or PATCH for updates, 
and DELETE for removal [1, 2]. **Ulbi TV** notes that PUT should replace a 
resource entirely, while PATCH should only update specific fields [3].
2.  **Maintain Stateless Architecture:** Design REST APIs to be stateless, 
ensuring each request is independent and contains all necessary information so 
the server does not need to store client context between calls [4-6].
3.  **Adopt gRPC for High-Performance Microservices:** Use **gRPC** and 
**Protocol Buffers** for internal systems where speed is critical, as its binary
format is 7 to 10 times faster than REST’s JSON [7, 8].
4.  **Eliminate Data Inefficiency with GraphQL:** Implement **GraphQL** to allow
clients to query exactly the fields they need, which solves the common REST 
problems of "overfetching" and "underfetching" [9-11].
5.  **Safeguard GraphQL Queries:** When using GraphQL in production, you must 
factor in the complexity of safeguarding against "unexpected table scans" that 
can crash a database if a client sends an overly complex query [12].
6.  **Prioritize WebSockets for Real-Time Data:** Avoid inefficient "short 
polling" for chat or live updates; instead, use **WebSockets** to establish a 
persistent, full-duplex connection where the server can push data instantly 
[13-15].
7.  **Automate Synchronization via Webhooks:** Configure **Webhooks** with a 
callback URL to receive immediate event-driven POST notifications from external 
services (like payment processors) rather than repeatedly checking for updates 
[16, 17].
8.  **Ensure Request Idempotency:** Design your API so that **PUT** and 
**DELETE** methods are idempotent, meaning multiple identical requests must 
result in the same server state as a single request [18, 19].
9.  **Implement Standardized Documentation:** Use the **OpenAPI specification** 
and tools like **Swagger** to automatically generate and visualize your API 
"contract," ensuring clear communication between server and client developers 
[20].
10. **Use Versioning for Breaking Changes:** Always change the API version 
(e.g., from `/v1` to `/v2`) when introducing non-backwards-compatible changes to
ensure existing integrations do not break [21].

Conversation: fc554d23-cded-4faf-a2bc-2427668a950d (turn 1)

---
