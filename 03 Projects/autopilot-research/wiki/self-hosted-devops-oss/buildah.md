# Buildah — daemonless, rootless OCI image builds

## Source
- Raw: `raw/2026-06-04-self-hosted-devops-oss-8-repos.md` (item 3)
- Repo: https://github.com/podman-container-tools/buildah *(redirected from `containers/buildah` — the repo moved orgs; old URL still resolves)* · Site: https://buildah.io
- Metadata (GitHub API, 2026-06-04): **8,824★** · Go · Apache-2.0 · created 2017-01-26 · last push 2026-06-02 (Podman/containers family, active)

## What it is
- A command-line tool for building **OCI / docker-format container images**, part of the Podman ecosystem.
- Creates a "working container" from scratch or a base image, lets you run commands / add files, then commits it to an image — with or without a Containerfile/Dockerfile.

## The differentiator (why the operator flags it)
- **No daemon** — follows a simple fork-exec model; nothing runs in the background (unlike the Docker daemon).
- **No root required** — builds images rootless, which is exactly what hardened CI/CD wants.
- Build *without* a Dockerfile → integrate any scripting language into the build process.
- Comprehensive **Go API** that can be vendored into other tools (Podman itself uses it for Dockerfile builds).

## Buildah vs Podman (they're complementary)
- **Buildah** = *build* images. `buildah run` ≈ the `RUN` line in a Dockerfile.
- **Podman** = *run/manage* containers + images. `podman run` ≈ `docker run`.
- Podman calls Buildah's Go API to build from Dockerfiles; you can install either independently.

## Example (from README)
```bash
ctr1=$(buildah from fedora)
buildah run "$ctr1" -- dnf install -y lighttpd
buildah config --port 80 --cmd "/usr/sbin/lighttpd -D -f /etc/lighttpd/lighttpd.conf" "$ctr1"
buildah commit "$ctr1" "$USER/lighttpd"
```

## Key Takeaways
- Unlike the other 7, Buildah doesn't replace a *paid SaaS* — it removes a **dependency + attack surface** (the root Docker daemon) from your build pipeline. The "cost" it kills is operational/security risk, not a license bill.
- Best fit: rootless CI/CD container builds; Kubernetes/OpenShift build steps; any pipeline that shouldn't grant root or run a daemon.
- Linux-native, mature, CNCF-adjacent (Podman family) — low risk.
- Output images are consumed by deploy tools like [[coolify]] and [[ctrlplane]]; build-time secrets can come from [[infisical]]. See [[cost-displacement-thesis]].
