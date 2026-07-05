# Runtime env injection for the SPA — the pattern, and the mis-framing

## Source

Transcript [01:33:33]–[01:45:11] (the fix) + [02:36:33] onward; ground-truth `env.template.js` usage in both client Dockerfiles; cross-checked against Vite docs, CRA/webpack DefinePlugin docs, and the official nginx Docker image docs.

## The problem (real)

The React client reads its API base URL from an env var. Because Vite **statically replaces** `import.meta.env.VITE_*` at *build* time, the value gets **baked into the compiled bundle**. That means the image built on the dev machine carries `localhost`, and you can't override it when the same image runs on the VPS — where the API host must be the VPS name/IP. This breaks the whole point of one-image-many-environments.

## The taught fix (a legitimate, standard pattern)

Inject the value at **container start**, not build:

1. `public/env.template.js`:
   ```js
   window.__ENV = { API_URL: "${API_URL}" };
   ```
2. Container `CMD` runs `envsubst` to expand `${API_URL}` (from the runtime environment) into `env.js`, then starts the server:
   ```dockerfile
   CMD sh -c "envsubst < .../env.template.js > .../env.js && nginx -g 'daemon off;'"
   ```
   (The dev image installs `envsubst` via `apk add --no-cache gettext`.)
3. `index.html` loads `<script src="/env.js">` **before** the app bundle.
4. App code reads `window.__ENV?.API_URL` instead of `import.meta.env.VITE_*` — changed in two places (`axiosConfig.js` for public endpoints, `useAxiosPrivate` hook for protected ones).

This is a well-established community pattern for runtime-configurable containerized SPAs, and the course implements it correctly.

## ⚠️ CORRECTION — this is NOT a Vite problem (verified CONFIRMED)

At [01:35:08] the instructor attributes the whole issue to Vite: *"the whole root of the issue is because we used Vite... this is a problem with Docker specifically regarding when creating a react component in Vite."* Refute-first verification:

- **Build-time env baking is inherent to every statically-built SPA**, not Vite. Create React App's own docs say the same thing ("environment variables are embedded during build time... it can't possibly read them at runtime"), because the underlying mechanism is a bundler doing **static text substitution** (webpack `DefinePlugin`, Vite's `import.meta.env`, Parcel, Next.js `NEXT_PUBLIC_` export — all identical). Vite is one of many, not the cause.
- **The `window.__ENV` + `envsubst` workaround is framework-agnostic** and documented across many independent sources; it's a general SPA pattern, not a Vite escape hatch.
- **The official nginx image does this natively since 1.19** — it runs `/docker-entrypoint.d/20-envsubst-on-templates.sh` over `/etc/nginx/templates/*.template` at startup. So the hand-written `envsubst` CMD partly re-implements a feature nginx already ships.

Net: the *fix* is correct; the *diagnosis* ("Vite's fault") is wrong and will mislead a learner into thinking switching bundlers avoids the issue. It doesn't.

## Three gotchas in the taught version (worth patching)

1. **Unguarded `envsubst`** — with no variable allowlist (`envsubst '$API_URL'` or `NGINX_ENVSUBST_FILTER`), *any* `$TOKEN` in the target file gets substituted. Inside a JS file that's a latent foot-gun (framework tokens like `$state`, template literals) — scope the substitution to named vars.
2. **No cache-busting on `env.js`** — no `Cache-Control: no-cache` and no content hash. If a browser caches `env.js` across a deploy that changed `API_URL`, the stale URL persists until the cache expires. Add a no-cache header for that one file.
3. **`apk add gettext` rationale undocumented** — the course installs it without saying why (`gettext` provides `envsubst`), and only in the dev image; the prod path leans on the nginx entrypoint. Minor, but a learner won't know what `gettext` is doing.

## Key takeaways

- The runtime-injection pattern (`env.template.js` + `envsubst` + `window.__ENV` + a `<script>` before the bundle) is correct and reusable for any static SPA that must stay one-image-many-environments.
- **Ignore the "it's a Vite thing" framing** — it's every statically-built SPA; nginx even does it natively since 1.19.
- If you lift the pattern: scope `envsubst` to named vars, add a no-cache header on `env.js`, and prefer nginx's built-in template mechanism over a hand-rolled CMD.
