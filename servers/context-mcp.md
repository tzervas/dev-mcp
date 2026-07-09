# context-mcp

**RAG context store.**

MCP server for context management: store/retrieve context items with temporal metadata (creation
time, age, expiration) and text-based query/filtering. Multi-tier storage (in-memory LRU always;
optional sled-based disk persistence). Note: embeddings/semantic search are not yet implemented —
retrieval today is literal text matching (see the server's own README for the current "what it
does / does not do yet" split).

## Status

Production-ready for context storage and lightweight RAG; APIs stable.

## Repo

<https://github.com/tzervas/context-mcp>

## Install

```bash
cargo install context-mcp
# or build from source
git clone https://github.com/tzervas/context-mcp
cd context-mcp
cargo build --release
```

See the repo's own `INSTALL.md` for VS Code configuration details.

## Register in `.mcp.json`

```jsonc
{
  "mcpServers": {
    "context-mcp": {
      "command": "context-mcp",
      "args": ["--stdio"]
    }
  }
}
```

Or run it as an HTTP server: `context-mcp --host 127.0.0.1 --port 3000`.

## W2 Usage (session as W2 consumer)

Context-mcp acts as W2 consumer for session memory in the CommonMemory facade rollout. Integrates with StructuredResponse via tero + memory-gate domains (see plan.md w2-rollout). Session items can feed MemoryContext in cabal's facade (AgentDomain.CONTEXT). Future: real RAG under W2 contract (always cited Structured incl refusal).

Cross-repo: cabal-devmelopner uses for session alongside memory-gate-rs (AgentDomain) and tero. See dev-docs/schemas/structured-response.schema.json + cabal schemas/agent.py run_structured (mem_contexts from facade), wsfull-wave-2026-07-09-compact.md.

Tero cite: plan.md:44, wsfull-wave §W2 Common Memory.
