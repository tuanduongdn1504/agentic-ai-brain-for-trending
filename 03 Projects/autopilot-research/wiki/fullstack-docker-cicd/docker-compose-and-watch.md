# Docker Compose, override "inheritance", and the Watch correction

## Source

Transcript [01:22:41]–[02:00:00] (compose + Mongo + volumes + seed) and [02:09:41]–[02:24:15] (dev/prod compose split + Watch); ground-truth `docker-compose.yaml`, `docker-compose.dev.yaml`, `docker-compose.prod.yaml`; cross-checked against `docs.docker.com/compose/file-watch`.

## Why Compose (the motivation the course gives)

Running the client and server as two separate `docker run` commands is "not ideal, especially as you scale." Compose replaces them with one `docker compose up` that builds a **network of containers** (`magic-stream-app_default`) and reads env values from a root `.env` via `${VAR}` interpolation. This part is taught correctly and demonstrated end-to-end.

## Containerized MongoDB + volumes + one-shot seed [01:45:11]

The base compose adds a `mongo:latest` service with:
- a **named volume** `movies:/data/db` — the course's explanation of volumes is accurate: "data survives container restarts, upgrades, and removals... stored on the host, mounted into the container."
- a **healthcheck** (`mongosh ... db.adminCommand('ping')`).
- a **one-shot seed service** gated on `depends_on: { db: { condition: service_healthy } }`, `restart: "no"`, running `mongosh .../seed.js` to import the movies/genres/rankings/users collections once.

The DB name changes from the local `magic-stream-app` to the containerized `magic-stream-movies`, and the Go connection string switches from `host.docker.internal`/localhost to `mongodb://db:27017` (service-name DNS on the compose network). All correct.

## Base + dev + prod as "inheritance" [02:09:41]

The strongest architectural idea in the course. One base `docker-compose.yaml` holds shared definitions (env vars, DB, seed); `docker-compose.dev.yaml` and `docker-compose.prod.yaml` **override** just what differs, merged with `-f base -f override`:

```bash
docker compose -f docker-compose.yaml -f docker-compose.dev.yaml watch   # dev
docker compose -f docker-compose.yaml -f docker-compose.prod.yaml up -d   # prod
```

- **dev override** — points at `Dockerfile.dev`, exposes 5173, and adds the `develop.watch` block.
- **prod override** — points at prod images pulled from DockerHub (`${IMAGE_TAG:-latest}`), maps nginx:80 → host:8081, `restart: always`, strips the watch block.

The instructor explicitly analogizes this to class inheritance ("override the appropriate settings"). It's a clean, real pattern and the most reusable takeaway in this article.

One honest caveat he states on camera [02:17:42]: the base file keeps the **seed service active for both dev and prod** "just for demonstration... I wouldn't advise you to include such functionality when you are deploying to production." (In the Mastery/Atlas variant the DB+seed services are commented out entirely — see [[the-originals]] and the C14 PARTIAL note in [[caveats-and-corrections]].)

## ⚠️ CORRECTION — Compose Watch does NOT hot-reload the Go server (verified CONFIRMED)

At [02:16:13] the instructor claims the watch feature hot-reloads **both** the React client and the Go server in real time: *"the same is true for the Go code. You can also run it in watch mode and make changes that will propagate through while you're running your code in real time."* The live demo only ever shows a React heading change reloading. Refute-first verification against the actual compose file and Docker's docs:

`docker-compose.dev.yaml` uses, for **both** services:
- `action: rebuild` on `package.json`/`go.mod`/`go.sum` (restarts the container), and
- `action: sync` on the source tree (copies files into the running container **without restarting it**).

- **Client:** works. The container runs Vite (`npm run dev`), which has its own file watcher + HMR, so synced files are picked up live. ✅
- **Server:** does **not** work as claimed. The container runs `CMD ["go", "run", "main.go"]` — a compiled process with no file watcher, and `go.mod` shows no `air`/`CompileDaemon`/reload tool. `action: sync` drops new `.go` files into `/app` but the already-running binary never recompiles. Only a `go.mod`/`go.sum` change (which triggers `action: rebuild`) restarts it. So editing Go source has **no effect until a manual restart**. ❌

**Correct fixes** (any one):
- `action: sync+restart` on the Go source (Compose ≥ v2.22.0) — simplest, restarts the container after each sync.
- Add **Air** (`cosmtrek/air`) to the dev image and `CMD ["air"]` — watches + recompiles, the Go-community standard, fastest DX.
- `sync+exec` with a custom rebuild command — most complex.

The underlying Compose Watch mechanics the course teaches are right; the **Go/React equivalence claim is the error**. Treat "watch gives you hot reload everywhere" as false-as-shipped for compiled backends.

## Key takeaways

- Compose-as-single-command and the volume/seed/healthcheck story are taught correctly.
- **Base + dev + prod override "inheritance"** is the best reusable pattern here.
- **Do not trust the Go hot-reload claim** — `action: sync` + `go run` = no reload; use `sync+restart` or Air for a compiled backend.
- Seeding is kept in the base file for demo convenience; the instructor himself flags it as prod-inappropriate.
