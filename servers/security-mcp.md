# security-mcp

**Content screening.**

MCP server intended to sit in front of other tools/servers so inputs and outputs get screened
consistently: input screening (prompt-injection patterns, suspicious encodings) and output
screening (PII/secrets patterns, high-entropy tokens). Batch scanning is CPU-parallel (`rayon`).
Today's detection is heuristic/pattern-based, not full DLP-grade.

## Status

Alpha / active development — rules and thresholds will evolve.

## Repo

<https://github.com/tzervas/security-mcp>

## Install

```bash
cargo install security-mcp
# or build from source
git clone https://github.com/tzervas/security-mcp
cd security-mcp
cargo build --release
```

## Register in `.mcp.json`

```jsonc
{
  "mcpServers": {
    "security-mcp": {
      "type": "stdio",
      "command": "security-mcp",
      "args": ["--stdio"]
    }
  }
}

## W2 Cross Notes

Security screening integrates in W2 orch paths (cabal facade + StructuredResponse before/after agent calls). See dev-mcp cross-repo (cabal + memory), plan.md:44 w2-rollout.
```

The `--stdio` flag is required for MCP-client integration — without it the server defaults to HTTP
mode on port 3001.
