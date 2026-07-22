# Webhooks (the 'reverse API')

**Source:** api-types-explained NotebookLM digest (LetDiv, Codist, ByteByteGo, Ulbi TV, Learn with Whiteboard, Be A Better Dev) · 2026-07-21

## The one framing

A webhook is **the server calling the client, not the other way around.** Instead of your code polling (repeatedly asking "is the payment done yet?"), the payment processor **POSTs directly to a URL you supply** the moment the event fires. Server → client push, not client → server pull.

- **Reverse API:** client registers a callback URL; server has your address and delivers events on its schedule, not yours
- **Event-driven:** triggered by specific external events (payment processed, git push, CI pipeline completed, Slack message sent)
- **Push, not polling:** eliminates the waste of checking every 5 seconds when the answer is "not yet" 99% of the time

## Mechanism

**How a webhook fires:**
1. You register a callback URL with the external service (e.g., Stripe, GitHub, AWS SNS)
2. The external service stores your URL + listens for events in its own system
3. When an event occurs (e.g., payment succeeds), the service makes an HTTP POST to your URL with a JSON/XML payload
4. Your endpoint receives the webhook, validates it (critical — see below), processes the data, returns 200 OK

**The payload** is typically structured JSON containing:
- Event type (e.g., `payment.succeeded`, `push`, `deployment.completed`)
- Timestamp of when the event occurred
- Data object with event-specific fields (charge ID, amount, user, etc.)
- Metadata (webhook ID, attempt number, retry-after header)

**From the service's perspective:** webhooks are "outbound API calls" that the external system makes on your behalf when something happens in their world.

## Webhook vs. polling (the key trade-off)

| Aspect | Polling | Webhook |
|---|---|---|
| **Who initiates?** | You ask repeatedly | Server notifies when ready |
| **Latency** | Minutes/hours (depending on poll interval) | Seconds to milliseconds |
| **Load on server** | High (redundant "is it done?" queries) | Low (event-triggered only) |
| **Bandwidth** | Wasteful (90% of polls say "nothing new") | Efficient (no payload unless event occurs) |
| **Implementation** | Simple (just loop + wait) | More complex (endpoint validation + retry logic) |
| **Reliability** | Easier (you control timing) | Harder (network failure, endpoint downtime require retry) |

**Real-world example:** GitHub could let you poll their API every minute asking "did someone push?" or send you a webhook when the push happens. Webhook is 60× more efficient.

## Webhook vs. WebSocket (the scope difference)

Do not confuse these — they solve different problems:

- **Webhook:** server→server event notification (Stripe → your backend when a payment completes). **Asynchronous, fire-and-forget.** Server does not expect a response; if your endpoint fails, the webhook provider retries.
- **WebSocket:** client↔server persistent bidirectional session (browser↔chat server for live messages). **Synchronous, continuous.** Either side can push; both are online at the same time.

Webhooks are often used to signal WebSockets: external event (payment) → webhook arrives at your server → server broadcasts via WebSocket to connected clients.

## Anatomy of a real webhook

**Incoming POST from Stripe when a charge succeeds:**

```
POST /api/webhooks/stripe HTTP/1.1
Host: yourserver.com
Content-Type: application/json
Stripe-Signature: t=1234567890,v1=abcd1234...

{
  "id": "evt_1234",
  "type": "charge.succeeded",
  "data": {
    "object": {
      "id": "ch_5678",
      "amount": 2000,
      "currency": "usd",
      "customer": "cus_9999"
    }
  },
  "created": 1234567890
}
```

**Your endpoint must:**
1. Verify the signature (check the `Stripe-Signature` header against a shared secret) — **MANDATORY in production**
2. Parse the JSON payload
3. Act on the event (update order status, send confirmation email, etc.)
4. Return HTTP 200 within a timeout (usually 30 seconds)
5. Be idempotent: if the webhook fires twice, don't double-charge or double-email

## Production caveats (critical — sources under-cover these)

The source videos emphasize the **simplicity and elegance** of webhooks but gloss over **operational reality**:

### Signature verification (HMAC-SHA256)

**The problem:** anyone on the internet can POST to `your.com/api/webhooks/stripe` pretending to be Stripe. Without verification, a malicious actor could trigger fraudulent refunds, cancel orders, or exploit your business logic.

**The solution:** Every webhook provider (Stripe, GitHub, Twilio, PayPal) signs the webhook body + timestamp with a shared secret:
- You store the signing secret safely (env var, secrets manager)
- On receipt, recompute the signature: `HMAC-SHA256(payload + timestamp, secret)`
- Compare against the header signature; reject if mismatch
- **All major providers require this; omitting it is a security vulnerability**

See [[api-security-7-techniques/_index]] for HMAC-based authentication + endpoint hardening.

### Endpoint durability

**The problem:** your webhook endpoint must be online and fast. If your server is down:
- The webhook provider retries (usually 3-5 times with exponential backoff)
- After retries exhaust, the event is lost (no guarantee of delivery) — payment processed but your order table was never updated
- Worse: if your endpoint is slow, the provider times out and retries, duplicating the webhook while you're still processing the first one

**The solution:**
- Make your webhook endpoint **fast and dumb**: validate signature, enqueue to a job queue (Redis, SQS, Kafka), return 200 immediately
- Process the webhook asynchronously in a worker, so network latency or database slowness never blocks the provider
- Use an idempotency key (the webhook ID) to deduplicate if the same webhook arrives twice
- Monitor webhook delivery: log every arrival, track success/failure rates

See [[aws-email-at-scale-sqs-lambda-ses/_index]] for an example: SNS webhooks → SQS queue → Lambda workers.

### Webhook discovery and versioning

**The problem:** if you change your webhook endpoint URL, the provider still sends to the old one. If you change your request schema, old client code might break.

**The solution:**
- Keep webhook endpoints stable (don't rename `/api/webhooks/stripe` to `/webhooks/v2/stripe` without maintaining the old one)
- Version your schema carefully: add new fields to the JSON, never remove old ones
- Document your webhook contract (what events you expect, what fields they contain) — treat it like an API contract
- Provide a "webhook tester" or replay mechanism so clients can resend past webhooks for debugging

## Webhook use cases (when to use them)

- **Payment processors** (Stripe, PayPal): charge succeeded, refund issued, dispute opened
- **CI/CD pipelines** (GitHub, GitLab): push to main, pull request opened, deployment completed
- **Communication services** (Slack, Discord, Twilio): message sent, user joined, SMS delivery confirmed
- **Email delivery** (SendGrid, Mailgun): bounce, complaint, open, click
- **Cloud infrastructure** (AWS via SNS, Azure via Event Grid): EC2 instance launched, S3 upload completed, storage quota exceeded
- **Monitoring / alerts** (DataDog, Sentry): error rate spike, deployment failed, uptime check failed

## When webhooks fail (failure modes)

Even with careful design, webhooks are **not guaranteed delivery**:

1. **Network failure between provider and your endpoint:** provider retries, but if they give up before your server comes back online, the event is lost
2. **Your endpoint crashes while processing:** partial state corruption (order marked as paid but inventory not decremented)
3. **Provider outage:** no webhook sent at all until they recover
4. **Clock skew:** if your server's time is far off from the provider's, signature verification can fail

**Mitigation:**
- Treat webhooks as a **convenience layer**, not the source of truth. Periodically reconcile via direct API call (e.g., daily: ask Stripe "which charges succeeded?" to catch any missed webhooks)
- Use event IDs + idempotency keys to survive duplicates and out-of-order delivery
- Design your business logic to be robust to missing events — e.g., "if order status is still 'pending' after 24 hours, investigate"

## Cross-links

- [[rest-and-web-api]] — standard HTTP POST method (the transport webhooks use)
- [[http-semantics-and-rest-conventions]] — idempotency (webhooks must be idempotent)
- [[websocket-and-realtime]] — contrast: WebSockets are bidirectional persistent; webhooks are push notifications
- [[selection-framework]] — when to choose webhooks vs. polling vs. WebSocket
- [[beyond-the-video]] — production-grade webhook design (idempotency, retry logic, security)
- [[api-security-7-techniques/_index]] — HMAC verification, endpoint hardening, CSRF
- [[aws-email-at-scale-sqs-lambda-ses/_index]] — concrete example: SNS webhooks triggering Lambda workers

## Key Takeaways

- Webhook = **reverse API**: server POST to client-supplied callback URL, not client polling
- **Event-driven push**: triggered by external events (payments, git pushes, alerts), eliminating waste of polling
- **Trade-off**: eliminates polling overhead but requires durable endpoint + signature verification + idempotency logic
- **Production caveat #1 — Signature verification (HMAC)**: validate the `Stripe-Signature` (or equivalent) header before processing; omitting this is a security vulnerability
- **Production caveat #2 — Async processing**: make the endpoint fast; enqueue to a job queue and return 200 immediately; process asynchronously in workers
- **Idempotency is required**: the same webhook may arrive twice (retries); use webhook ID to deduplicate
- **Webhooks are not guaranteed delivery**: treat them as a convenience layer; periodically reconcile via direct API call to catch missed events
