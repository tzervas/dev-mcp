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
