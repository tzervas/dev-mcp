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
