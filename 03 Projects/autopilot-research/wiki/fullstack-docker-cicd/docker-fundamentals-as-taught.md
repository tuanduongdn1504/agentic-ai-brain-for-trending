# Docker fundamentals, as taught

## Source

Transcript [00:57:41]–[01:22:41] (Dockerfiles + build + run) and [02:00:31]–[02:09:41] (dev/prod split); ground-truth Dockerfiles in the MagicStream repo family (`repo-truth/`).

## The mental model the course installs

- **Image = declarative recipe** ("the environment for the container plus the commands to get the app running"); **container = a running instance of the image** in memory. Stated repeatedly and correctly.
- **Each Dockerfile line = a layer**, cached if unchanged; changing a line invalidates that layer and everything after. Demonstrated with the classic `COPY go.mod go.sum → RUN go mod download → COPY .` ordering so dependency downloads cache across source edits.
- **Port mapping** `-p host:container` maps the container's `EXPOSE`d port to a host port; the container port is "the one on the right." Taught at length because it's the #1 beginner confusion.
- **Docker Desktop** is used as the primary GUI throughout (view/stop/delete images and containers) alongside the CLI — the course is explicit that Docker Desktop must be installed to run any of the commands.

## The dev Dockerfiles (ground truth)

**Server** (`Server/MagicStreamServer/Dockerfile.dev`):
```dockerfile
FROM golang:1.24.2-alpine
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
EXPOSE 8080
CMD ["go", "run", "main.go"]
```
**Client** (`Client/magic-stream-client/Dockerfile.dev`):
```dockerfile
FROM node:20-alpine
WORKDIR /app
RUN apk add --no-cache gettext        # provides envsubst — see [[vite-runtime-env-injection]]
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 5173
CMD sh -c "envsubst < public/env.template.js > public/env.js && npm run dev -- --host"
```

## The build/run choreography (with the preserved mistakes)

The course walks `docker build -t magic-stream-api:1.0.0 .` (the trailing `.` = build context, forgotten twice on camera and corrected), then `docker run -d -p 8080:8080 --name magic-stream-api --env-file .env magic-stream-api:1.0.0`. Two live errors are left in as teaching moments:

- `docker run -d --p ...` → **"unknown flag"** → corrected to single-dash `-p` [01:09:37].
- `docker build ... Docker file.dev` → **"no such file"** because the flag is case-sensitive `-f` not `-F` [02:53:04], and separately a forgotten build-context `.` [02:31:56].

These are genuinely useful — they show the actual failure text a learner will hit — but they also signal a hand-typed, unrehearsed style that lines up with the "very fiddly, trial and error" admission later ([[cicd-github-actions-pipeline]]).

The recurring pain point the course names explicitly: **two `docker run` commands for two components is cumbersome** — which motivates Compose ([[docker-compose-and-watch]]).

## The dev/prod split and multi-stage prod builds

At [02:00:31] the single `Dockerfile` becomes `Dockerfile.dev` + `Dockerfile.prod` per component, selected at build with `-f`. The prod files are **multi-stage** and materially better than the dev ones:

**Client prod** — build in Node, serve static from nginx:
```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
COPY public/env.template.js /usr/share/nginx/html/env.template.js
CMD sh -c "envsubst < /usr/share/nginx/html/env.template.js > /usr/share/nginx/html/env.js && nginx -g 'daemon off;'"
EXPOSE 80
```
**Server prod** — compile a static Go binary, ship it on bare alpine:
```dockerfile
FROM golang:1.24-alpine AS build
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o api-golang
FROM alpine:latest
WORKDIR /app
COPY --from=build /app/api-golang .
EXPOSE 8080
CMD ["./api-golang"]
```

This is a legitimately good pattern: dev images run interpreters/dev-servers for iteration; prod images are small (nginx-static / single Go binary on alpine). The prod client exposes port **80** (nginx) vs. the dev client's **5173** (Vite), mapped to host **8081** in the prod compose override.

## What's missing from the images (see [[security-and-production-gaps]])

- **No non-root `USER`** in either prod image — nginx and the Go binary run as root inside the container.
- **`FROM alpine:latest` / `nginx:stable-alpine`** — unpinned/floating base tags; reproducibility and supply-chain drift risk.
- **No `HEALTHCHECK`** in the app images (only the Mongo service gets one in compose).

## Key takeaways

- The image/container/layer/port model is taught cleanly and correctly, GUI-and-CLI both.
- The multi-stage prod Dockerfiles (nginx-static client, single-binary Go server) are the strongest, most transferable part of the course.
- The dev images run `go run` / `vite` for iteration — which sets up the Compose Watch correction in [[docker-compose-and-watch]].
- Image hardening (non-root user, pinned bases, healthchecks) is entirely absent and unmentioned.
