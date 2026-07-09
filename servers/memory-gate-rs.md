# memory-gate-rs

**Dynamic memory learning layer.**

Persistent knowledge accumulation for AI agents with vector retrieval and automatic consolidation. Dual-stream Complementary Learning Systems (CLS) architecture (fast + slow via background consolidation). Pluggable storage (in-memory default; Qdrant, sqlite-vec) and adapters. Domain filtering for scoped operation.

## M1 domains/facade

Extended `AgentDomain` (Workspace, Tero, Context, MemoryGate, LangRust, LangPython + legacy) with prefix-aware `FromStr` ("layer:tero", "lang:rust", "repo:xxx"). Thin facade: domain filters on `retrieve_context` / `learn_from_interaction` for tero-first cited reads + gate-persistent scoped writes (no bloat). See tero-cited `readme--agent-domains`.

## W2 mirror to cabal, tero

Py mirror: `CommonMemoryAdapter + AgentDomain` in `cabal-devmelopner/core/schemas.py` (W2). Domain as scoping key for shared `StructuredResponse` + citations across orch. Integrates tero (L1) + memory-gate + context-mcp. See dev-docs WORKSPACE_CABAL_TERO_READINESS.md and wsfull-wave-2026-07-09-compact.md.

## Status

M1 complete (feature/mint-m1-domain-facade, PR #26; merged dev→main 2026-07-09). v1.0.0 published on crates.io. Active development (M2+ pending per roadmap). All changes tero-first + append-only.

## Repo

<https://github.com/tzervas/memory-gate-rs>

## Install

```bash
cargo install memory-gate-rs
# or (as library, common):
# [dependencies]
# memory-gate-rs = "1.0"

# or build from source
git clone https://github.com/tzervas/memory-gate-rs
cd memory-gate-rs
cargo build --release
```

See the repo's own `README.md` (M1 section), `AGENTS.md`, `CHANGELOG.md`, and `docs/ROADMAP.md`.

## Register in `.mcp.json`

Core library (no standalone MCP binary today). Family servers surface memory via tero-mcp (cited L1), context-mcp (session), and integrations (cabal W2 facade + agent-mcp). Use via dependency + facade in Rust/Python agents. See memory-gate-rs examples and cabal-devmelopner for wiring.

## W2 Rollout Usage Notes (chore/w2-rollout-docs-wiring)

W2 advances StructuredResponse + CommonMemoryAdapter + AgentDomain mirrors across repos (per plan.md §2 w2-rollout). 

- Cabal facade example (current impl from cabal-devmelopner/src/cabal_devmelopner/core/schemas.py + agent.py):
  ```python
  from cabal_devmelopner.core.schemas import AgentDomain, CommonMemoryAdapter, StructuredResponse
  facade = CommonMemoryAdapter(tero_client)
  resp: StructuredResponse = facade.query(AgentDomain.TERO, "query for orch", {"limit": 5})
  # always Structured (kind=answer|refusal); .citations, .orchestration, extended["domain"]
  if resp.is_refusal(): ...  # C0 emit to EventBus
  ```
- Cross-repo (cabal + memory): memory-gate-rs provides Rust AgentDomain M1 (types.rs:167+) with FromStr prefixes ("layer:tero", "lang:rust"). Cabal Py mirrors + uses for domain-scoped tero queries. Context-mcp as session consumer for W2. See dev-docs/schemas/W2-STRUCTURED-SCHEMAS.md, common_memory_facade*.example, wsfull-wave-2026-07-09-compact.md:30.
- Usage: domain-scoped via facade.query -> tero L1 cited -> StructuredResponse for orch hints. Evolve thin facade in memory-gate.
- Tero cites: plan.md:44 (W2 / Common Memory Facade Rollout), wsfull-wave-2026-07-09-compact.md §W2, dev-docs/schemas/W2-STRUCTURED-SCHEMAS.md.

See also: memory-gate-rs AGENTS/ROADMAP (facade evolution), cabal AGENTS (post-PR#12), context-mcp as W2 session consumer.
