# dev-mcp

**The umbrella index for the `tzervas` MCP (Model Context Protocol) server family.**

This repo does **not** contain server implementations. It is documentation-first: it names the
servers that make up the family, points to where each one actually lives, tracks their status, and
gives you the shortest path to standing the whole family up locally. Each server is developed and
released in its **own repository** — dev-mcp aggregates/indexes them, it does not vendor their
code.

## Server inventory

| Server | Purpose | Repo | Status |
|---|---|---|---|
| **tero-mcp** | Transparent, cited-memory MCP server — provenance-carrying answers over a project's decisions/docs/issues, never a silent empty answer | [tzervas/tero-mcp](https://github.com/tzervas/tero-mcp) | **New** — planned; repo not yet published |
| **context-mcp** | RAG context store — multi-tier (in-memory + optional disk) context/memory service for agents, with temporal metadata and text-based retrieval | [tzervas/context-mcp](https://github.com/tzervas/context-mcp) | Production-ready for context storage / lightweight RAG; APIs stable |
| **agent-mcp** | Multi-LLM orchestration — routes/parallelizes/consensus-builds prompts across multiple AI providers (Claude, ChatGPT, Gemini, Grok, …), with workflow support | [tzervas/agent-mcp](https://github.com/tzervas/agent-mcp) | Active development |
| **security-mcp** | Content screening — prompt-injection defense, PII/secrets detection, screens input/output text for other servers | [tzervas/security-mcp](https://github.com/tzervas/security-mcp) | Alpha / active development |
| **memory-gate-rs** | Dynamic memory learning layer — persistent knowledge accumulation, vector retrieval, consolidation; M1 domains/facade (Tero/Context/MemoryGate/Lang* scoping), W2 cabal mirror | [tzervas/memory-gate-rs](https://github.com/tzervas/memory-gate-rs) | M1 complete (PR #26); v1.0.0; active |

Per-server details (purpose, install, `.mcp.json` registration snippet) live under
[`servers/`](servers/) — see [`servers/README.md`](servers/README.md) for the index.

### Why links, not submodules

Each server above is linked, not vendored as a git submodule. The family spans independent
release cadences and (for now) a mix of public/private visibility, and a submodule pin adds
maintenance overhead (pinned SHAs to bump, `git submodule update --init` friction) that this
umbrella doesn't need yet — see [`servers/README.md`](servers/README.md#submodules-vs-links) for
the tradeoff and how to revisit it.

## What this repo is for

- **Discovery** — one place to see every MCP server in the family, its purpose, and its status.
- **Onboarding** — a single set of instructions to clone, build, and register the whole family
  locally (see [`AGENTS.md`](AGENTS.md)).
- **Cross-cutting docs** — conventions shared across the family (naming, licensing, MCP
  registration format) that don't belong in any one server's repo.

## What this repo is *not* for

- Server implementation code (that lives in each server's own repo).
- A build/release pipeline for the family (each server ships independently).

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT — see [`LICENSE`](LICENSE). Matches the licensing of the sibling server repos.

## Status & roadmap

- [Assessment & gaps](docs/ASSESSMENT.md)
- [Product roadmap & API plans](docs/ROADMAP.md)

## W2 Rollout (StructuredResponse/CommonMemoryAdapter + AgentDomain mirrors)

Append for chore/w2-rollout-docs-wiring: W2 usage notes added to servers/*.md (memory-gate-rs.md with cabal facade ex + cross-repo cabal+memory; context-mcp.md as session W2 consumer; agent/tero/security updated). 

Cabal facade example (mirrors memory-gate M1): see servers/memory-gate-rs.md and cabal-devmelopner/core/schemas.py:CommonMemoryAdapter + AgentDomain (from_str prefixes). Integrates tero L1 -> StructuredResponse (citations, orchestration) for cross (cabal + memory-gate-rs + context-mcp).

Refs (tero-cited): plan.md §2 (w2-rollout — in_progress), wsfull-wave-2026-07-09-compact.md §W2, dev-docs/schemas/W2-STRUCTURED-SCHEMAS.md + *.example.

Hygiene + tero update + land --no-ff dev/main + propagate per task. All append-only.

## Orch Wiring + Inventory Truth (chore/orch-wiring-devmcp appended)

Per plan.md §3 (orch-wiring — pending): flesh dev-mcp for Wave A inventory truth + Wave B cabal consumption matrix. This advances orch in dev (dev-mcp/cabal).

- cabal as leaf/consumer: family layout marks `cabal-devmelopner/   # consumer`; used for dev-mcp tasks (inventory discovery, W2 facade orch memory, server registration via servers/ snippets). Cabal exercises tero + memory-gate + context in W2 paths.
- Enhanced servers/README.md with full W2 facade matrix + memory-gate domains + links to leaf ROADMAPs (D-A2) + doctor notes (D-A4 sketch).
- See servers/README.md#orch-inventory-truth for matrix (cabal primary, agent-mcp future orch, context session, memory-gate provider, tero L1, security screen).
- Cross consumption: cabal facade (schemas.py CommonMemoryAdapter.query(domain) -> always StructuredResponse) feeds orch hints; mirrors memory-gate M1 domains.
- Tero-first verified: text_search "orch|inventory|w2|cabal consumption" (dev-mcp index + global) + cite/explain; hits include readme--server-inventory, workspacecabalteroreadiness--w2-structured-schemas-orch-started..., plan sections.
- Links: ASSESSMENT/ROADMAP here; per-server to https://.../docs/ROADMAP.md + ASSESSMENT.md; cabal-devmelopner AGENTS.md, docs/ROADMAP.md.

Doctor: run per-server binary --help or grok mcp doctor <server>. See AGENTS.md for family cold-start.

Follow-on: land --no-ff, propagate (dev<-chore, main<-dev --no-ff, dev<-main), update-tero, verify tero "orch|dev-mcp|cabal|w2|facade". Cites: plan.md:60-80, dev-mcp ROADMAP Wave A/B, wsfull compact.

All append-only per dev-workflow.
## Semver + Releases (2026-07-10 appended)

Baseline v0.1.0 for this dev support/toolchain component (extracted from mycelium; agnostic dev tooling).

See AGENTS.md##Semver.
