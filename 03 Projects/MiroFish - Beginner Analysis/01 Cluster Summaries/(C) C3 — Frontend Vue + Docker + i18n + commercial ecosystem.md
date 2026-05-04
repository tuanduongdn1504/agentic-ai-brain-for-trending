# (C) C3 — Frontend Vue + Docker + i18n + Shanda commercial ecosystem

**Cluster source**: `00 Source/MiroFish/frontend/` + `locales/` + `Dockerfile` + `docker-compose.yml` + `.github/workflows/docker-image.yml` + `package.json` (root) + README acknowledgments + GitHub profile data for `666ghj`

---

## Frontend stack (verified from `frontend/package.json`)

```json
{
  "name": "frontend",
  "private": true,
  "version": "0.1.0",
  "type": "module",
  "dependencies": {
    "axios": "^1.14.0",
    "d3": "^7.9.0",
    "vue": "^3.5.24",
    "vue-i18n": "^11.3.0",
    "vue-router": "^4.6.3"
  },
  "devDependencies": {
    "@vitejs/plugin-vue": "^6.0.1",
    "vite": "^7.2.4"
  }
}
```

**Stack summary**:
- **Vue 3.5.24** (Composition API era; recent major version)
- **Vite 7.2.4** (modern build tooling; no webpack)
- **vue-i18n 11.3.0** (runtime localization)
- **vue-router 4.6.3** (SPA routing)
- **axios 1.14** (HTTP client)
- **D3 7.9** (data visualization — knowledge graph + simulation result viz)
- ESM-only (`"type": "module"`)

**Corpus-first observation**: **Vue 3 at T5**. Prior T5 frontends in corpus:
- deer-flow v9 — Next.js (React)
- Skyvern v24 — React (no specific framework cited; presumed React)
- DeepTutor v38 — Next.js + React 19
- browser-use v41 — none (Python-only; CLI + Python API)
- OpenHands v30 — React
- shannon v45 — none (CLI-only TypeScript monorepo, no UI)
- rowboat v43 — Electron + React 19 + Vite 7
- ruflo v42 — TypeScript backend, no first-class frontend documented
- aidevops v47 — TypeScript + Bun runtime, no first-class frontend

MiroFish = **first Vue 3 at T5 in corpus**. Vue is dominant in CN ecosystem (Alibaba, Tencent, ByteDance heavily use Vue) — consistent with CN-author + CN-corporate-incubation context.

## Frontend `src/` structure

```
frontend/src/
├── App.vue           # root component
├── main.js           # entry point, vue-i18n + router + axios setup
├── api/              # axios endpoint wrappers
├── assets/           # static images / styles
├── components/       # reusable components
├── i18n/             # vue-i18n config (consumes locales/*.json)
├── router/           # vue-router config
├── store/            # state management (Pinia / Vuex — not enumerated; not in package.json so likely Pinia in vue-router-paired ecosystem default)
└── views/            # page-level views
```

(Frontend per-component enumeration deferred; GREEN tier compression; cite directory not enumerate.)

---

## i18n surface (`locales/`)

Three files at top-level (NOT inside `frontend/`, but at repo root — shared by frontend + possibly backend locale.py):

### `locales/languages.json` — registered languages

```json
{
  "zh": { "label": "中文", "llmInstruction": "请使用中文回答。" },
  "en": { "label": "English", "llmInstruction": "Please respond in English." },
  "es": { "label": "Español", "llmInstruction": "Por favor, responde en español." },
  "fr": { "label": "Français", "llmInstruction": "Veuillez répondre en français." },
  "pt": { "label": "Português", "llmInstruction": "Por favor, responda em português." },
  "ru": { "label": "Русский", "llmInstruction": "Пожалуйста, отвечайте на русском языке." },
  "de": { "label": "Deutsch", "llmInstruction": "Bitte antworten Sie auf Deutsch." }
}
```

**7 languages**: zh + en + es + fr + pt + ru + de.

**Architectural insight**: each language has a **`llmInstruction` field** that the backend injects into prompts to steer LLM responses to match user UI language. Corpus-first explicit "language steering instruction per locale" pattern. The `utils/locale.py` (2 KB) likely consumes this for backend-side prompt construction.

### `locales/en.json` (38 KB) + `locales/zh.json` (36.8 KB)

Two languages with full UI strings populated. **Other 5 languages** (es / fr / pt / ru / de) are registered in `languages.json` but **lack corresponding translation files**. This means:
- Selecting es/fr/pt/ru/de likely falls back to en (or breaks; depends on vue-i18n config)
- The 7-language registration is **aspirational / partial** — only en+zh fully implemented
- LLM-response language steering still works for all 7 (since `llmInstruction` is present)

**Important caveat for v49 wiki**: 7-language i18n is **partial** (2 of 7 fully translated). Don't overstate. The runtime supports 7 languages worth of LLM instruction; the UI string layer supports 2.

### Documentation i18n (READMEs)

- `README.md` (EN, 9.1 KB)
- `README-ZH.md` (ZH, 8.2 KB)
- No README in es / fr / pt / ru / de despite locale registration
- No README in VN / JP / KR / Arabic / Hindi etc.

**3-tier i18n surface mismatch**:
1. LLM-instruction layer: 7 languages (full)
2. UI strings layer: 2 of 7 languages (partial)
3. Documentation layer: 2 languages (EN + ZH)

This is a **non-trivial corpus-observable architectural mismatch** worth noting in entity pages. Compare to corpus i18n leaders:
- LlamaFactory v22 — many language READMEs
- DeepTutor v38 — 9-language README
- oh-my-claudecode v27 / fish-speech v20 — 7-language README
- awesome-mcp-servers v31 — 7-language README

MiroFish has 7-language **registration** but only 2-language **README** = aspirational i18n at documentation layer.

---

## Docker + deployment

### `Dockerfile` (723 B)

```dockerfile
FROM python:3.11
RUN apt-get update && apt-get install -y --no-install-recommends nodejs npm \
  && rm -rf /var/lib/apt/lists/*
COPY --from=ghcr.io/astral-sh/uv:0.9.26 /uv /uvx /bin/
WORKDIR /app
COPY package.json package-lock.json ./
COPY frontend/package.json frontend/package-lock.json ./frontend/
COPY backend/pyproject.toml backend/uv.lock ./backend/
RUN npm ci && npm ci --prefix frontend && cd backend && uv sync --frozen
COPY . .
EXPOSE 3000 5001
CMD ["npm", "run", "dev"]
```

**Observations**:
- Single-stage Dockerfile (not multi-stage); could be optimized for production but adequate for dev/demo deployment
- Uses `uv:0.9.26` from official ghcr.io image (modern uv-bundling pattern; first corpus T5 explicit uv-bundled-Docker)
- Layer caching optimized: dependency files copied first, source copied after, `npm ci` for reproducible install
- **Runs `npm run dev` in container** — meaning Docker deployment uses the dev-mode concurrently-launched backend + frontend (Flask debug mode + Vite dev server). Not production-hardened; not behind nginx/gunicorn. **Deployment caveat**: this is not a production-grade Dockerfile despite GHCR registry distribution.
- Exposes both ports 3000 (frontend dev server) + 5001 (Flask)

### `docker-compose.yml` (371 B)

```yaml
services:
  mirofish:
    image: ghcr.io/666ghj/mirofish:latest
    # 加速镜像（如拉取缓慢可替换上方地址）
    # image: ghcr.nju.edu.cn/666ghj/mirofish:latest
    container_name: mirofish
    env_file:
      - .env
    ports:
      - "3000:3000"
      - "5001:5001"
    restart: unless-stopped
    volumes:
      - ./backend/uploads:/app/backend/uploads
```

**Observations**:
- Single-service compose (not multi-service; Zep is external SaaS, no DB needed)
- Pulls pre-built image from GHCR (no local build); CN mirror via `ghcr.nju.edu.cn` cited as comment (Nanjing University CDN-mirror = CN-friendly distribution)
- Volume mount: persists user uploads outside container
- `restart: unless-stopped` (production-light orchestration)

### `.github/workflows/docker-image.yml` (sole workflow)

Single CI job: build + push Docker image to GHCR on tag push or manual dispatch. Uses:
- `actions/checkout@v4`
- `docker/setup-qemu-action@v3` (multi-arch capable but no platforms specified; defaults to host-arch)
- `docker/setup-buildx-action@v3`
- `docker/login-action@v3` (logs into GHCR with `GITHUB_TOKEN`)
- `docker/metadata-action@v5` (auto-tags: ref-tag + sha + latest)
- `docker/build-push-action@v5`

**Single-purpose CI**: only Docker image build + push. **No test workflow, no lint workflow, no release workflow.** Consistent with light-minimal-governance observation. Pre-monetization product velocity.

---

## Commercial ecosystem (Shanda + mirofish.ai + multi-channel community)

### Commercial entity

**Shanda Group (盛大集团)** — major Chinese internet conglomerate (founded 1999; historically gaming + IP licensing + technology investment). README explicit: *"MiroFish has received strategic support and incubation from Shanda Group!"*

**Recruiting via `mirofish@shanda.com`** = email domain `@shanda.com` rather than `@mirofish.ai` indicates Shanda is the legal-employer entity. MiroFish.ai homepage = product-facing brand. Two-layer commercial architecture:
- Brand: mirofish.ai
- Operational entity: Shanda Group

### mirofish.ai homepage

Listed as `homepage` field in repo metadata. README cites the live demo at `https://666ghj.github.io/mirofish-demo/` which is a GitHub Pages deployment under the author's personal account, NOT under mirofish.ai. The relationship between mirofish.ai (commercial site) + 666ghj.github.io/mirofish-demo (personal-account demo) + Shanda recruiting funnel = 3 distinct surfaces.

### Multi-channel community

- **Discord**: discord.gg/ePf5aPaHnA (Western community channel)
- **X (Twitter)**: @mirofish_ai
- **Instagram**: @mirofish_ai
- **QQ Group**: image in README footer (CN-native community channel — Tencent QQ messaging platform)
- **Bilibili**: 2 demo videos cited in README (CN-native video platform; Western corpus-first Bilibili demo video at T5)

**5+ community surfaces** spanning Western (Discord + X + Instagram) + CN-native (QQ + Bilibili). **Pattern #50 strengthening — N=9** with multi-region-channel-mix sub-variant.

---

## BaiFu (`666ghj`) GitHub profile (probe data)

| Field | Value |
|-------|-------|
| **Real name** | BaiFu |
| **Location** | Shanghai, China |
| **Bio** | "Do what you love, and love what you do." |
| **Followers** | 3,838 |
| **Public repos** | 7 (small portfolio; MiroFish is the breakout) |
| **Affiliation** (per profile) | BUPT + Shanda |
| **Email** | `mirofish@shanda.com` (project email; personal email not publicly disclosed) |

**BUPT (Beijing University of Posts and Telecommunications)** — major CS-tech university in CN, well-known for AI/ML + multi-agent simulation research. The BUPT affiliation suggests **academic-foundation-with-commercial-pivot** archetype (BaiFu likely BUPT alumnus or current researcher; OASIS / CAMEL-AI is associated with similar CN academic AI-research circles). Cannot verify without external research; documenting per profile self-description.

**Cross-tier observation**: BaiFu is **3rd CN-author at scale in corpus** after:
- TrendRadar v19 sansan0 — solo CN-author at 52K (T4)
- DeepTutor v38 HKUDS — CN-academic-lab-ecosystem at 21K (T5)
- MiroFish v49 BaiFu — solo CN-author with conglomerate-incubation at 57K (T5)

Distinct from claude-howto v32 (Luong / VN-diaspora) and codymaster v12 (VN-in-VN). MiroFish strengthens **CN-author cross-tier presence** — 4 CN-cluster wikis across 3 tiers (T4 TrendRadar, T5 DeepTutor + MiroFish + dive-into-llms v39 multi-institutional CN/SG/HK/HW). Not registered as new pattern; observation noted.

---

## Architectural commitments observable from this cluster

1. **Vue 3 + Vite 7 modern frontend** (corpus-first Vue at T5)
2. **D3 visualization first-class** (knowledge graph + simulation viz)
3. **uv-bundled Docker** (modern Python packaging in container)
4. **GHCR distribution + CN mirror** (geographically-aware delivery)
5. **Dev-mode-as-deployment Docker** (not production-hardened; demo-and-self-host positioning)
6. **Single-purpose CI** (Docker build only; no test automation)
7. **Multi-region community surface** (Western + CN dual presence)
8. **2-layer commercial structure** (mirofish.ai brand + Shanda Group operational)
9. **Aspirational 7-language i18n** (registered, partially translated)
10. **3-surface deployment**: source clone + Docker + (implicit) hosted demo at github.io/mirofish-demo

---

## Cluster takeaways for downstream entity pages

1. **Architecture + dependencies** entity should ground Vue+Vite+D3 stack alongside backend stack
2. **BaiFu + Shanda + BUPT** entity should treat 5+ community surfaces + Shanda corporate structure + BUPT affiliation as primary signals
3. **Commercial-funnel observation** (Pattern #50 N=9) belongs to Phase 4b deliverable
4. **i18n mismatch** (7 registered / 2 translated / 2 README'd) belongs in entity page or Phase 4b as observation

---

**Cluster summary status:** ✅ complete. Frontend + Docker + i18n + commercial ecosystem fully mapped. 1 explicit caveat on partial-i18n-translation (don't overstate "7 languages"). 0 fabrications.
