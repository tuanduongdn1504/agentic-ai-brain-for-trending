# (C) Web-UI-Exclusive Capabilities

> Entity page — Value prop concept
> Sources: README "features web UI doesn't expose" section + SKILL.md key capabilities
> Format: 13-section canonical

## 1. What is it / Nó là gì

**Web-UI-Exclusive Capabilities** = chức năng mà notebooklm-py provides nhưng Google NotebookLM web UI KHÔNG provide. Đây là **core differentiation** — nếu ai cũng chỉ cần web UI, library không có value beyond convenience.

**9 main exclusive features:**

1. Batch downloads
2. Quiz/Flashcard structured export (JSON/Markdown/HTML)
3. Mind map JSON extraction
4. Slide deck PPTX export (editable PowerPoint)
5. Individual slide revision via NL prompt
6. Report template customization (append custom instructions)
7. Chat history persistence (save Q&A to notes)
8. Source fulltext programmatic access
9. Programmatic permission management (sharing)

## 2. Why it matters / Sao quan trọng

**Value prop defensibility.** If library just wrapped web UI 1:1, users could use web UI directly. Library provides:

- **Workflow acceleration** — batch ops (no manual clicks)
- **Data portability** — JSON/CSV/PPTX out of walled garden
- **Composability** — outputs feed other tools (visualization, LMS, etc.)
- **Automation** — agents + scripts do things humans can't at scale

**Strategic consequence:** Even if Google adds these to web UI eventually, library will find new gaps. Cat-and-mouse game = library stays valuable.

## 3. The 9 Exclusive Capabilities detailed

### Capability 1: Batch downloads
```bash
notebooklm download audio --all      # all audio artifacts
notebooklm download slide-deck --all # all decks
```
**Web UI:** Must click each artifact, download one at a time.
**Use case:** Archive entire notebook's artifacts for offline access.

### Capability 2: Quiz/Flashcard structured export
Formats: JSON, Markdown, HTML.
**Web UI:** Interactive quiz/flashcard widgets only; no export.
**Use case:** Feed quiz into LMS, print flashcards, bulk translate.

### Capability 3: Mind map JSON extraction
```bash
notebooklm download mind-map ./map.json
```
**Web UI:** Interactive visualization only.
**Use case:** Import into Obsidian, Miro, Mermaid, custom viz tools.

### Capability 4: Slide deck PPTX export
```bash
notebooklm download slide-deck ./slides.pptx --format pptx
```
**Web UI:** PDF only.
**Use case:** Edit in PowerPoint/Keynote/Google Slides, customize branding.

### Capability 5: Individual slide revision
```bash
notebooklm generate revise-slide "Make slide 3 more concise"
  --artifact <id> --slide 3 --wait
```
**Web UI:** Regenerate entire deck or not at all.
**Use case:** Targeted edit without regenerating whole deck (saves 10-20 min).

### Capability 6: Report template customization
```bash
notebooklm generate report
  --format briefing-doc
  --append "Include specific risk matrix for Q1"
```
**Web UI:** Choose preset templates only.
**Use case:** Company-specific reports, custom compliance reports, investor updates.

### Capability 7: Chat history persistence
```bash
notebooklm ask "Summarize all sources" --save-as-note --note-title "Summary"
notebooklm history --save
```
**Web UI:** Chat history disappears on new session.
**Use case:** Preserve chain-of-thought as notebook record.

### Capability 8: Source fulltext access
```bash
notebooklm source fulltext <src_id> --json
```
**Web UI:** Hover citations only; can't read full indexed text.
**Use case:** Verify source content, extract specific passages, cross-reference.

### Capability 9: Programmatic sharing
```python
await client.sharing.set_sharing_state(nb_id, public=True)
```
**Web UI:** Click-through sharing dialog.
**Use case:** Automated sharing in CI/CD, batch permission updates.

## 4. Strategic categorization

| Category | Capabilities | Value |
|----------|-------------|-------|
| **Portability** | 2, 3, 4, 8 (JSON/PPTX/CSV export + fulltext) | Data out of walled garden |
| **Automation** | 1, 7, 9 (batch, persistence, sharing) | Scale without manual clicks |
| **Customization** | 5, 6 (slide revision, report append) | Tailor to specific needs |

## 5. Real-world use cases

### Use case 1: Corporate training LMS integration
1. Research notebook with 30 sources (company policies)
2. Generate quiz → export JSON
3. Import JSON into LMS (Canvas/Moodle/etc.)
4. Track employee completion

**Without library:** Web UI → interactive quiz only → no LMS integration → manual recreation.

### Use case 2: Academic literature review
1. Notebook with 50 papers
2. Generate mind map → export JSON
3. Import into Obsidian as interactive knowledge graph
4. Cross-reference with own notes

**Without library:** Web UI mind map → screenshot → no cross-linking.

### Use case 3: Sales pitch deck
1. Notebook with product research
2. Generate slide-deck (presenter format)
3. Export PPTX → customize branding + logos
4. Ship to clients

**Without library:** PDF-only export → can't edit → can't brand.

### Use case 4: Legal compliance reports
1. Notebook with regulation docs
2. Generate report with `--append "Include specific clauses from GDPR Article 17"`
3. Export Markdown
4. Send to legal team

**Without library:** Generic templates → manual post-editing → compliance risk.

### Use case 5: Team knowledge podcast
1. Scrum retro notebook (Storm Bear use case!)
2. Generate audio (deep-dive, long)
3. Download MP3
4. Team listens on commute

**Without library:** Web UI allows podcast playback only → no offline → no distribution → no accessibility.

## 6. Capability matrix by user type

| User | Top 3 capabilities |
|------|-------------------|
| **Researcher** | Fulltext access (8), Mind map JSON (3), Report customization (6) |
| **Educator** | Quiz export (2), Flashcard export (2), PPTX decks (4) |
| **Consultant** | Batch downloads (1), PPTX decks (4), Report customization (6) |
| **Scrum coach** | Audio batch (1), Chat persistence (7), Report customization (6) |
| **Dev team lead** | Sharing automation (9), Batch downloads (1), Chat persistence (7) |

## 7. Limitations / What's NOT exclusive

### Still requires NotebookLM plan
- Library provides NO compute — Google does
- Library provides NO models — Google does
- Library is interface, not engine

### Still constrained by plan tier
- Source limits: Standard 50 / Plus 100 / Pro 300 / Ultra 600
- Library does not bypass

### Still rate-limited
- Google throttles — library doesn't protect
- Bulk generation = graceful fail expected

## 8. Trade-offs / Limitations

### Strengths
- **Defensible value prop** — Google can't trivially match all 9 in web UI quickly
- **Composable outputs** — JSON/CSV/PPTX = standard formats
- **Breakage-isolated** — if Google breaks one, others still work

### Weaknesses
- **Google could add to web UI** — value shrinks over time
- **Undocumented APIs could disappear** — entire library dies
- **Browser auth requirement** — adds friction vs direct API keys

## 9. Comparison to sibling "unique features"

| Sibling | Unique value |
|---------|--------------|
| **ECC** | 48 agents + 185 skills ecosystem |
| **Superpowers** | 7-stage workflow + TDD enforcement |
| **gstack** | Specialist role system + sprint pipeline |
| **GSD** | Context rot solution + 14 harnesses |
| **goclaw** | Multi-tenant agent platform + Knowledge Vault |
| **course** | Comprehensive curriculum + VN translation |
| **notebooklm-py** | **Web-UI-exclusive features** for external service (NotebookLM) |

→ **Unique axis.** Siblings create new capabilities; notebooklm-py unlocks hidden ones in existing service.

## 10. Common pitfalls

1. **Assuming web UI parity** — library has MORE, not less; don't limit workflows to web UI features
2. **Overusing PPTX format** — export is editable but still AI-generated; review before ship
3. **Batch download over cellular** — MP3s can be 50+ MB each; 10 artifacts = 500 MB
4. **Public sharing automation** — check sharing state; don't accidentally leak private research
5. **Report custom append abuse** — long append = confused LLM output
6. **Trusting fulltext byte-exact** — indexed text may differ from original source

## 11. When NOT to use these capabilities

- **Quick ad-hoc research** — web UI faster, no install needed
- **One-off without distribution** — chat result in UI enough
- **Single artifact** — no batch value
- **No export destination** — exports unused = waste

## 12. Storm Bear vault relevance

**Highest-value capabilities for Storm Bear:**

### 1. Audio batch (capability 1, 4)
Generate N podcasts from N wikis → batch download → team listens async.

### 2. Chat persistence (capability 7)
Vault's research queries via NotebookLM → save as notes → cross-link in Obsidian.

### 3. Report customization (capability 6)
Custom templates for Scrum coaching reports (retro format, team health, delivery risk).

### 4. Fulltext access (capability 8)
Verify NotebookLM's source indexing matches original content (quality check cho research integrity).

### Scrum coaching workflow example
```
Retro transcript (Zoom) 
  → NotebookLM notebook 
  → Generate audio (deep-dive format) 
  → Batch download
  → Generate flashcards for team self-study
  → Generate report with --append "Focus on impediments and team health"
  → Export Markdown → import into Storm Bear vault
```

### Implementation status
- **Not adopted yet.** Storm Bear routine could optionally invoke after wiki build.

## 13. References / Nguồn

- Source: [[(C) README summary]] (exclusive features section) + [[(C) SKILL summary]] (key capabilities)
- Related entities:
  - [[(C) CLI Surface]] (commands that enable capabilities)
  - [[(C) Skill Integration (Claude Code + Codex + OpenClaw)]]
- External: [NotebookLM official](https://notebooklm.google.com) for web UI baseline comparison
