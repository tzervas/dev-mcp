# webpuppet-rs-mcp

**Browser automation MCP server.**

Exposes [webpuppet-rs](https://github.com/tzervas/webpuppet-rs) browser automation as MCP tools:
AI provider prompting through a real browser, screenshots, navigation, content extraction, permission
checks, and human-in-the-loop pause/resume for captchas and 2FA. JSON-RPC 2.0 over stdio.

## Status

Published and usable. Binary crate `webpuppet-mcp` (package name in repo may differ — see repo README).

## Repo

<https://github.com/tzervas/webpuppet-rs-mcp>

## Install

```bash
git clone https://github.com/tzervas/webpuppet-rs-mcp
cd webpuppet-rs-mcp
cargo build --release
# or, from repo root per upstream README:
cargo install --path .
```

Requires a supported browser (Brave/Chrome/Chromium) on the host. See the repo for policy flags
(`--policy secure|readonly|permissive`).

## Register in `.mcp.json`

```jsonc
{
  "mcpServers": {
    "webpuppet": {
      "command": "webpuppet-mcp",
      "args": ["--stdio"]
    }
  }
}
```

Or run via `cargo` from a checkout (see repo README). Prefer the server's own docs for tool names
(`webpuppet_prompt`, `webpuppet_screenshot`, `webpuppet_session_open`, …).

## Assessment / roadmap

- [webpuppet-rs-mcp/docs/ASSESSMENT.md](https://github.com/tzervas/webpuppet-rs-mcp/blob/main/docs/ASSESSMENT.md) (if present)
- [webpuppet-rs-mcp/docs/ROADMAP.md](https://github.com/tzervas/webpuppet-rs-mcp/blob/main/docs/ROADMAP.md) (if present)