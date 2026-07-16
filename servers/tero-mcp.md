# tero-mcp

**Transparent, cited-memory MCP server.**

Serves provenance-carrying answers about a project's decisions, issues, docs, and changelog over
MCP (stdio JSON-RPC). Every answer carries a resolvable citation (anchor + `file:line` + guarantee
tag); a query that finds nothing citable returns a typed refusal rather than a silent empty answer.

## Status

**Published & usable.** Public repo ships **tero-mcp-lite** (Python ≥3.11, `uv`, stdlib-only runtime)
over a committed `index.json`, plus Rust sources under `rust/` for the full **tero-rs** binary when
you need parity with Mycelium's Layer-1 server. Layer-2 (VSA) is out of scope for lite.

## Repo

<https://github.com/tzervas/tero-mcp>

## Install

```bash
git clone https://github.com/tzervas/tero-mcp
cd tero-mcp
uv sync
# run (requires TERO_TOKENS and an index path):
TERO_TOKENS='local-dev:read' uv run tero-mcp-lite --index /path/to/index.json
```

Generate or refresh an index for your repo with `scripts/generate_lite_index.py` (see repo
`GENERATING-AN-INDEX.md`). For the Rust binary, build from `rust/` per that repo's README.

## Register in `.mcp.json`

```jsonc
{
  "mcpServers": {
    "tero": {
      "command": "uv",
      "args": [
        "run",
        "--project", "/path/to/tero-mcp",
        "tero-mcp-lite",
        "--index", "/path/to/index.json"
      ],
      "env": {
        "TERO_TOKENS": "local-dev:read"
      }
    }
  }
}
```

Rotate `TERO_TOKENS` for non-local use; the server refuses to start without tokens. Every
`tools/call` includes a `token` argument (see repo README).

## Assessment / roadmap

- [tero-mcp/docs/ASSESSMENT.md](https://github.com/tzervas/tero-mcp/blob/main/docs/ASSESSMENT.md) (if present)
- [tero-mcp/docs/ROADMAP.md](https://github.com/tzervas/tero-mcp/blob/main/docs/ROADMAP.md) (if present)