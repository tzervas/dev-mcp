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

## W2 Rollout Update (chore/w2-rollout-docs-wiring, 2026-07-09)

W2 usage + cabal facade example + cross-repo (cabal+memory) notes appended to servers/*.md (esp. memory-gate-rs.md, context-mcp.md) + README + this + ROADMAP. 

- Documents W2 (StructuredResponse/CommonMemoryAdapter + AgentDomain mirrors) per plan.md w2 section.
- Cabal current impl referenced (schemas/agent: facade.query(AgentDomain.TERO) -> StructuredResponse always).
- Memory M1 domains mirror in memory-gate-rs/src/types.rs .
- Context session noted as W2 consumer.
- Tero cites: plan.md:44, wsfull-wave-2026-07-09-compact.md:30 (W2 schemas/facade start), dev-docs/schemas/.

All append-only; hygiene, update-tero, branch chore/w2-rollout-docs-wiring. Land/propagate to dev/main. Verify tero hits post.

## Orch Wiring + Inventory Truth Update (chore/orch-wiring-devmcp, 2026-07-09)

Advanced per plan.md §3 orch-wiring (parallel W2 tranche):

- Enhanced servers/README.md with orch inventory truth: cabal-devmelopner as consumer/leaf for dev-mcp tasks; explicit W2 facade matrix (6 consumers, domain scopes from memory-gate M1); doctor notes + links to leaf ROADMAP.md / ASSESSMENT.md (addresses D-A2, D-B2).
- Top README + this + ROADMAP appended with orch section + consumption matrix refs + tero cites.
- Inventory truth: cabal listed as # consumer; uses family (agent-mcp for orch, tero-mcp L1, memory-gate domains, context session) via W2 CommonMemoryAdapter (StructuredResponse always + citations/orchestration).
- Memory-gate domains: TERO/CONTEXT/MEMORY_GATE/LANG_*/WORKSPACE etc (prefix FromStr); mirrored in cabal; domain as key for facade-scoped orch.
- Links: added to servers/README (e.g. cabal-devmelopner AGENTS/ROADMAP); cross to plan.md §3, wsfull compact, dev-docs schemas.
- Doctor: notes fit in servers/README (grok mcp doctor + per-server --help; future scripts/doctor-all per ROADMAP).

Tero-first (MCP + /root/git/scripts/tero.sh dev-mcp): text_search "orch|inventory|w2|cabal consumption" + cite/explain pre-edits (hits on inventory, w2-mirror-to-cabal, leaf-orch-review, server-inventory anchors). Post will re-verify.

Cites: workspacecabalteroreadiness--w2-structured-schemas-orch-started-2026-07-08, dev-mcp readme--w2-rollout..., roadmap--w2..., plan.md orch section, cabal AGENTS (subagents tero).

All append-only, hygiene (check.sh), update-tero, branch-guard followed. Land --no-ff + propagate; verify tero "orch|dev-mcp|cabal|facade|inventory". Maturity bump candidate post.
