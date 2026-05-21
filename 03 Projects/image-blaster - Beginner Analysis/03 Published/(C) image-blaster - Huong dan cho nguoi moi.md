# image-blaster — Hướng dẫn cho người mới / Beginner's Guide / 入门指南

**Subject**: [`neilsonnn/image-blaster`](https://github.com/neilsonnn/image-blaster)
**Tagline**: *"An image-to-world skillset for Claude"*
**License**: MIT
**Stars / Forks / Age**: 3,836 / 379 / 30 days (Phase 0 fetch 2026-05-21)

> ⚠️ **Honest note**: This wiki was built under **operator-elected Phase 0.9 override** — routine v2.2 SKIP gate would have triggered (0 clear PASS criteria). Operator chose to force-build. See `CLAUDE.md` audit trail.

---

## 🇬🇧 English

### What is image-blaster?

`image-blaster` is a **Claude Code skillset** by SF-based indie developer Neilson K-S that turns a **single input image** into a **complete 3D environment**: Gaussian-splat static environment (`.spz`), per-object 3D meshes (`.glb`/`.obj`), and ambient + object-specific SFX (`.mp3`). It's designed for jumpstarting 3D work in Unity, Unreal, Godot, Blender, 3DS Max, Maya, Three.js, or Electron — the assets are local-first and engine-portable.

### How does it work?

Eight pipeline-step skills run in order:

1. **image-blast-project** — initializes the project envelope (run first)
2. **image-blast-plate** — generates clean-plate from source image
3. **image-blast-uncover** — extracts objects from the scene
4. **image-blast-world** — generates explorable static environment via **World Labs Marble 1.1** (Gaussian splat)
5. **image-blast-3d** — generates per-object 3D meshes via **FAL Hunyuan-3D** (or Meshy alternative)
6. **image-blast-sfx** — generates ambient + object SFX via **ElevenLabs**
7. **image-blast-image-edit** — helper for image edits (nano-banana default / gpt-image-2 alt)
8. **image-blast-wildcard** — escape-hatch skill

### What do I need?

- A Claude Code session (CLI installed via `curl -fsSL https://claude.ai/install.sh | bash`)
- An API key for **World Labs** ([platform.worldlabs.ai](https://platform.worldlabs.ai/))
- An API key for **FAL** ([fal.ai](https://fal.ai/))
- An input image
- Bun runtime (for `bun install` + `bun run dev`)

### Install + run

```bash
git clone https://github.com/neilsonnn/image-blaster
cd image-blaster
claude
# (paste World Labs + FAL API keys when Claude asks)
# Put image in input/ directory
# Tell Claude: "blast it and confirm each step with me"
```

### When should I use it?

✅ **Good fit**:
- You need a fast jumpstart on 3D environment art (game level / film scout / arch viz)
- You have an image and want < 5-minute scaffolding before manual refinement
- You're comfortable in Claude Code CLI + game engines or DCC software

❌ **Not a good fit**:
- You need production-quality final assets (this is "jumpstart" not "finished")
- You don't have World Labs + FAL API keys
- You don't work in 3D / game-dev / VFX / arch-viz domains

### Storm Bear verdict

**NOT a vault pilot candidate**. v84 image-blaster is creative-tech vertical (image-to-3D-world for game-dev/VFX/arch-viz); Storm Bear's vault is Scrum/dev-coaching focused. **0 clear Phase 0.9 PASS criteria → operator-elected override INCLUDE for corpus-knowledge purposes only**. v84 joins corpus-knowledge-only tier alongside v63 Karpathy + v74 Raschka + v75 impeccable + v77 easy-vibe + v79 autoresearch + v80 SmartMacroAI + v81 taste-skill.

---

## 🇻🇳 Tiếng Việt

### `image-blaster` là gì?

`image-blaster` là **Claude Code skillset** do Neilson K-S (developer indie ở SF) phát triển, chuyển **một ảnh đầu vào** thành **môi trường 3D hoàn chỉnh**: Gaussian-splat môi trường tĩnh (`.spz`) + mesh 3D cho từng object (`.glb`/`.obj`) + SFX môi trường + per-object (`.mp3`). Thiết kế để jumpstart công việc 3D trong Unity, Unreal, Godot, Blender, 3DS Max, Maya, Three.js, hoặc Electron — assets local-first + portable across engines.

### Hoạt động thế nào?

Tám skill pipeline-step chạy theo thứ tự:

1. **image-blast-project** — khởi tạo project envelope (chạy đầu tiên)
2. **image-blast-plate** — generate clean-plate từ ảnh nguồn
3. **image-blast-uncover** — extract objects từ scene
4. **image-blast-world** — generate môi trường tĩnh explorable qua **World Labs Marble 1.1** (Gaussian splat)
5. **image-blast-3d** — generate mesh 3D cho từng object qua **FAL Hunyuan-3D** (hoặc Meshy)
6. **image-blast-sfx** — generate SFX môi trường + per-object qua **ElevenLabs**
7. **image-blast-image-edit** — helper cho image edits (nano-banana default / gpt-image-2 alt)
8. **image-blast-wildcard** — escape-hatch skill

### Cần gì để dùng?

- Phiên Claude Code (CLI cài qua `curl -fsSL https://claude.ai/install.sh | bash`)
- API key cho **World Labs** ([platform.worldlabs.ai](https://platform.worldlabs.ai/))
- API key cho **FAL** ([fal.ai](https://fal.ai/))
- Một ảnh đầu vào
- Bun runtime (cho `bun install` + `bun run dev`)

### Cài + chạy

```bash
git clone https://github.com/neilsonnn/image-blaster
cd image-blaster
claude
# (paste API keys World Labs + FAL khi Claude hỏi)
# Bỏ ảnh vào thư mục input/
# Nói với Claude: "blast it and confirm each step with me"
```

### Khi nào nên dùng?

✅ **Phù hợp**:
- Cần jumpstart nhanh trên 3D environment art (game level / film scout / arch viz)
- Có ảnh và muốn scaffolding < 5 phút trước khi refine bằng tay
- Thoải mái với Claude Code CLI + game engines hoặc DCC software

❌ **Không phù hợp**:
- Cần asset production-quality final (cái này là "jumpstart" không phải "finished")
- Không có API key World Labs + FAL
- Không làm việc trong 3D / game-dev / VFX / arch-viz

### Storm Bear verdict

**KHÔNG phải vault pilot candidate**. v84 image-blaster là creative-tech vertical (image-to-3D-world cho game-dev/VFX/arch-viz); vault Storm Bear focus vào Scrum/dev-coaching. **0 PASS Phase 0.9 rõ ràng → operator-elected override INCLUDE chỉ phục vụ corpus-knowledge**. v84 thuộc tier corpus-knowledge-only như v63 + v74 + v75 + v77 + v79 + v80 + v81.

---

## 🇨🇳 中文

### `image-blaster` 是什么？

`image-blaster` 是 SF 独立开发者 Neilson K-S 制作的 **Claude Code skillset**，将**单张输入图片**转换为**完整 3D 环境**：Gaussian-splat 静态环境（`.spz`）+ 每个 object 的 3D mesh（`.glb`/`.obj`）+ 环境与 per-object SFX（`.mp3`）。设计用于在 Unity、Unreal、Godot、Blender、3DS Max、Maya、Three.js 或 Electron 中快速启动 3D 工作 — assets local-first + 跨引擎可移植。

### 工作原理？

八个 pipeline-step skills 按顺序运行：

1. **image-blast-project** — 初始化 project envelope（首先运行）
2. **image-blast-plate** — 从源图生成 clean-plate
3. **image-blast-uncover** — 从场景中提取 objects
4. **image-blast-world** — 通过 **World Labs Marble 1.1** 生成 explorable 静态环境（Gaussian splat）
5. **image-blast-3d** — 通过 **FAL Hunyuan-3D**（或 Meshy）生成每个 object 的 3D mesh
6. **image-blast-sfx** — 通过 **ElevenLabs** 生成环境 + per-object SFX
7. **image-blast-image-edit** — image edits 助手（nano-banana 默认 / gpt-image-2 备用）
8. **image-blast-wildcard** — escape-hatch skill

### 需要什么？

- Claude Code session（CLI 通过 `curl -fsSL https://claude.ai/install.sh | bash` 安装）
- **World Labs** API key（[platform.worldlabs.ai](https://platform.worldlabs.ai/)）
- **FAL** API key（[fal.ai](https://fal.ai/)）
- 一张输入图片
- Bun runtime（用于 `bun install` + `bun run dev`）

### 安装 + 运行

```bash
git clone https://github.com/neilsonnn/image-blaster
cd image-blaster
claude
# （在 Claude 询问时粘贴 World Labs + FAL API keys）
# 将图片放入 input/ 目录
# 告诉 Claude: "blast it and confirm each step with me"
```

### 何时使用？

✅ **合适场景**：
- 需要快速启动 3D environment art（game level / film scout / arch viz）
- 有图片且想要 < 5 分钟脚手架后再手动 refine
- 熟悉 Claude Code CLI + game engines 或 DCC software

❌ **不合适场景**：
- 需要 production-quality 最终 asset（这是 "jumpstart" 不是 "finished"）
- 没有 World Labs + FAL API key
- 不在 3D / game-dev / VFX / arch-viz 领域工作

### Storm Bear 评定

**非 vault pilot 候选**。v84 image-blaster 是 creative-tech vertical（image-to-3D-world for game-dev/VFX/arch-viz）；Storm Bear 的 vault focus 在 Scrum/dev-coaching。**0 clear Phase 0.9 PASS criteria → operator-elected override INCLUDE 仅用于 corpus-knowledge**。v84 与 v63 + v74 + v75 + v77 + v79 + v80 + v81 同属 corpus-knowledge-only tier。

---

## Sources

- Repository: <https://github.com/neilsonnn/image-blaster>
- Owner: <https://github.com/neilsonnn> + <https://neilsonks.com/>
- External services: World Labs <https://platform.worldlabs.ai/> + FAL <https://fal.ai/>
- README + settings.json + 8 sub-skill SKILL.md fetched 2026-05-21

🤖 Generated by Claude under routine `llm-wiki-routine-v2.2` (TWENTIETH execution; FIRST under operator-elected Phase 0.9 override).
