# tero-mcp

**Transparent, cited-memory MCP server.**

Serves provenance-carrying answers about a project's decisions, issues, docs, and changelog over
MCP (or HTTP). Every answer carries a resolvable citation (anchor + `file:line` + guarantee tag);
a query that finds nothing citable returns a typed refusal rather than a silent empty answer.

## Status

**New.** This is the newest member of the family — the repo (`tzervas/tero-mcp`) has not been
published yet. This stub is a placeholder so the inventory and install instructions are ready the
moment it lands; update the repo link and the sections below once it exists.

## Repo

<https://github.com/tzervas/tero-mcp> (not yet published)

## Install

```bash
# once published:
git clone https://github.com/tzervas/tero-mcp
cd tero-mcp
# build steps TBD — update once the repo's own README specifies its toolchain
```

## Register in `.mcp.json`

```jsonc
{
  "mcpServers": {
    "tero-mcp": {
      "command": "tero-mcp",
      "args": ["--stdio"]
    }
  }
}
```

Update this snippet once the real binary name / flags are published in the server's own README.

## W2 Usage Notes (cites + facade)

Tero-mcp serves L1 for W2: provides cited results consumed into StructuredResponse.citations via CommonMemoryAdapter (cabal + mirrors). Domain scoping (AgentDomain.TERO) in facade.query feeds tero text_search. See plan.md w2-rollout, dev-docs/schemas/ (examples for StructuredResponse), cabal schemas, memory-gate types.rs M1 domains, wsfull-wave-2026-07-09-compact.md. Cross-repo wiring: cabal facade + memory + context.
