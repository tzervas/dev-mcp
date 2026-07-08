# AGENTS.md — standing up the MCP family locally

This is the umbrella bring-up guide: how an agent (or a human) clones, builds, and registers the
whole `tzervas` MCP server family on one machine. `dev-mcp` itself has nothing to build — this is
about the servers it indexes.

## 1. Prerequisites

- `git`
- `cargo` / Rust toolchain (agent-mcp, context-mcp, security-mcp are Rust crates)
- `uv` (if/when a Python-based server joins the family — none currently is)
- An MCP client to register the servers with: Claude Desktop, VS Code + GitHub Copilot, or any
  other MCP-compatible client

## 2. Clone each server

Pick a working directory (e.g. `~/dev/mcp/`) and clone the servers you need. Not every server is
required for every use case — see the [inventory](README.md#server-inventory) for what each one
does.

```bash
mkdir -p ~/dev/mcp && cd ~/dev/mcp

git clone https://github.com/tzervas/context-mcp
git clone https://github.com/tzervas/agent-mcp
git clone https://github.com/tzervas/security-mcp
# tero-mcp: not yet published — clone once it exists (see servers/tero-mcp.md)
```

## 3. Build each server

All current family members are Rust crates; build each with `cargo`:

```bash
cd ~/dev/mcp/context-mcp  && cargo build --release
cd ~/dev/mcp/agent-mcp    && cargo build -p embeddenator-agent-mcp --release
cd ~/dev/mcp/security-mcp && cargo build --release
```

Some servers also publish to crates.io — `cargo install <name>` is often faster than a from-source
build if you don't need a specific branch. Check each server's own README/INSTALL docs; details
can drift, and that repo is the source of truth for its own build.

If/when a Python-based server joins the family, its bring-up step is `uv sync` per this repo's
sibling `mycelium` conventions (`uv sync --group <group>`) rather than `cargo build`.

## 4. Register with your MCP client

Merge the snippets from [`servers/*.md`](servers/) into your client's MCP config
(`.mcp.json`, `claude_desktop_config.json`, or your editor's MCP settings). Example combining the
built family:

```jsonc
{
  "mcpServers": {
    "context-mcp": {
      "command": "/path/to/context-mcp/target/release/context-mcp",
      "args": ["--stdio"]
    },
    "agent-mcp": {
      "command": "/path/to/agent-mcp/target/release/agent-mcp",
      "args": ["--visible"]
    },
    "security-mcp": {
      "type": "stdio",
      "command": "/path/to/security-mcp/target/release/security-mcp",
      "args": ["--stdio"]
    }
  }
}
```

Point `command` at each built binary's actual path, or the `cargo install`ed name if it's on
`$PATH`.

## 5. Verify

Restart your MCP client and confirm each server shows as connected. Each server's own repo has
its own test suite (`cargo test`) — run those in-repo, not here; `dev-mcp` has no build/test step
of its own.

## Notes for agents doing this work

- This repo **indexes** the family; it doesn't vendor or rebuild their code. Don't copy server
  source into `dev-mcp` — link to it (see [`servers/README.md`](servers/README.md#submodules-vs-links)
  for the submodule-vs-link tradeoff).
- If a server's actual install/registration steps have drifted from what's documented under
  `servers/`, prefer the server's own repo as ground truth and send a small PR here to reconcile.
- `tero-mcp` is listed as **New** because the repo doesn't exist yet — don't invent build
  instructions for it beyond the placeholder in `servers/tero-mcp.md`.
