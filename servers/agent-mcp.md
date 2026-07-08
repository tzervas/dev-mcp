# agent-mcp

**Multi-LLM orchestration.**

MCP server for orchestrating prompts across multiple AI providers: routes to the best provider for
a task, runs providers in parallel, builds consensus answers across providers, and manages
multi-step workflows. Ships with built-in content screening and rate limiting hooks.

## Status

Active development.

## Repo

<https://github.com/tzervas/agent-mcp>

## Install

```bash
git clone https://github.com/tzervas/agent-mcp
cd agent-mcp
cargo build -p embeddenator-agent-mcp --release
```

## Register in `.mcp.json`

```jsonc
{
  "mcpServers": {
    "agent-mcp": {
      "command": "/path/to/agent-mcp",
      "args": ["--visible"]
    }
  }
}
```

`--visible` runs the browser-driven providers (Claude, ChatGPT, Gemini, Grok, Perplexity,
NotebookLM) in non-headless mode; drop it for headless. See the repo's own README for the full
tool list (`agent_prompt`, `agent_parallel_prompt`, `agent_consensus`, `agent_workflow_*`, …).
