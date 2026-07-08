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
