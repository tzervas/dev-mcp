# Servers index

One stub per server in the family — purpose, repo, install, and the `.mcp.json` snippet to
register it with an MCP client (Claude Desktop, VS Code, etc.). These stubs are documentation
only; the actual server source lives in each linked repo.

| Stub | Server repo |
|---|---|
| [`tero-mcp.md`](tero-mcp.md) | [tzervas/tero-mcp](https://github.com/tzervas/tero-mcp) (new) |
| [`context-mcp.md`](context-mcp.md) | [tzervas/context-mcp](https://github.com/tzervas/context-mcp) |
| [`agent-mcp.md`](agent-mcp.md) | [tzervas/agent-mcp](https://github.com/tzervas/agent-mcp) |
| [`security-mcp.md`](security-mcp.md) | [tzervas/security-mcp](https://github.com/tzervas/security-mcp) |
| [`memory-gate-rs.md`](memory-gate-rs.md) | [tzervas/memory-gate-rs](https://github.com/tzervas/memory-gate-rs) |

## Submodules vs. links

This directory links to each server's repo rather than checking it out as a git submodule. That
keeps `dev-mcp` a lightweight index: no pinned SHAs to bump, no `--recurse-submodules` clone
friction, and no coupling between this repo's visibility (about to flip public) and a server repo
that may still be private or mid-rename (`tero-mcp` doesn't exist yet).

If the family stabilizes and you want reproducible multi-server checkouts from one `git clone`,
submodules are a reasonable upgrade — e.g.:

```bash
git submodule add https://github.com/tzervas/context-mcp servers/context-mcp
git submodule add https://github.com/tzervas/agent-mcp servers/agent-mcp
git submodule add https://github.com/tzervas/security-mcp servers/security-mcp
```

That's a maintainer call, not made here — flagged in the PR that introduced this scaffolding.

## Orch Inventory Truth (chore/orch-wiring-devmcp)

cabal-devmelopner is the canonical consumer / leaf executor for dev-mcp tasks (see top-level README.md family clone layout: `cabal-devmelopner/   # consumer`).

W2 facade matrix (cross-repo consumption of StructuredResponse/CommonMemoryAdapter + AgentDomain mirrors from memory-gate-rs M1):

| Consumer          | W2 Facade Role                  | AgentDomain Scopes (memory-gate mirror)          | Notes / Links |
|-------------------|---------------------------------|--------------------------------------------------|---------------|
| cabal-devmelopner | Primary leaf (query + orch)    | TERO, CONTEXT, MEMORY_GATE, LANG_RUST, LANG_PYTHON, WORKSPACE, INFRASTRUCTURE, GENERAL | Uses CommonMemoryAdapter for tero L1 cited -> StructuredResponse (cites+orchestration); see cabal-devmelopner/core/schemas.py, agent.py |
| agent-mcp         | Future orch hints consumer     | via facade (orchestration field)                 | Multi-LLM routing will consume domain-scoped memory; Roadmap: https://github.com/tzervas/agent-mcp/blob/*/docs/ROADMAP.md |
| context-mcp       | Session memory W2 consumer     | CONTEXT                                          | Temporal KV feeds MemoryContext; not full RAG yet; Roadmap: https://github.com/tzervas/context-mcp/blob/*/docs/ROADMAP.md |
| memory-gate-rs    | Domain provider / Rust mirror  | All (FromStr prefixes e.g. "layer:tero")         | M1 complete; thin facade for retrieve/learn; Roadmap: https://github.com/tzervas/memory-gate-rs/blob/*/docs/ROADMAP.md |
| tero-mcp          | L1 cited source for facade     | TERO (primary)                                   | Provides provenance; consumed by cabal facade; Roadmap: https://github.com/tzervas/tero-mcp/blob/*/docs/ROADMAP.md |
| security-mcp      | Screening in W2 orch paths     | pre/post facade calls                            | Cross with cabal+memory; Roadmap: https://github.com/tzervas/security-mcp/blob/*/docs/ROADMAP.md |

Memory-gate domains (M1): Workspace, Tero, Context, MemoryGate, LangRust, LangPython + legacy (see servers/memory-gate-rs.md, memory-gate-rs/src/types.rs).

Doctor notes: Per-server doctor via `--help` / `grok mcp doctor <name>` (see AGENTS.md). Future: `scripts/doctor-all.sh` (ROADMAP D-A4). Each servers/*.md lists "Doctor: ..." where applicable; prefer leaf repo's LOCAL_CHECKS / check.sh.

Links added: each consumer's leaf ROADMAP/ASSESSMENT referenced above + per servers/*.md (D-A2).

Tero cites (from dev-mcp + global): readme--server-inventory, contributing--adding-a-new-server-to-the-inventory, workspacecabalteroreadiness--leaf-orch-review-tranche-wsfull, plan.md §3 (orch-wiring), wsfull-wave-2026-07-09-compact.md.

Append-only; hygiene + update-tero. See dev-mcp docs/ROADMAP.md (Wave B D-B2 cabal consumption matrix), ASSESSMENT. Cross: cabal AGENTS/ROADMAP (as leaf).
