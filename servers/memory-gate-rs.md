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
