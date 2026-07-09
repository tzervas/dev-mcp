# dev-mcp — Assessment & Gap Analysis

**Date:** 2026-07-08  
**Role:** **Docs-only umbrella** for the tzervas MCP server family  
**Not:** a runtime server monorepo  

---

## 1. What it is

Index + onboarding for:

| Server | Repo | Status (honest, 2026-07-08) |
|--------|------|-------------------------------|
| tero-mcp | tzervas/tero-mcp | **Published & usable** L1 MCP (was wrongly “not published”) |
| context-mcp | tzervas/context-mcp | Session memory OK; **not** legitimate RAG yet |
| agent-mcp | tzervas/agent-mcp | Alpha orchestration |
| security-mcp | tzervas/security-mcp | Alpha screener |
| webpuppet-rs-mcp | tzervas/webpuppet-rs-mcp | **Missing from inventory** — should add |
| search-box | tzervas/search-box | Real code on develop/dev; main was scaffold |

---

## 2. Gaps

| Gap | Sev |
|-----|-----|
| Stale status table (tero unpublished) | High |
| Missing webpuppet / search-box rows | Med |
| AGENTS.md may omit Python tero bring-up | Med |
| No single “clone all + doctor” script accuracy | Med |
| context-mcp RAG overclaim echoed | High |

---

## 3. Maturity as umbrella: **3 / 5** after refresh

Useful discovery; must track reality of leaf repos’ `docs/ASSESSMENT.md` + `docs/ROADMAP.md`.

See [ROADMAP.md](ROADMAP.md).

## Tero index

Layer-1 citation index: [docs/tero-index/](tero-index/) (`index.json`, `INDEX.md`, `MANIFEST.toml`).
