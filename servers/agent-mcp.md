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

## W2 Usage Notes

Agent orchestration (future) will consume W2 StructuredResponse + CommonMemoryAdapter for domain-scoped orch hints (orchestration field) + cited memory from cabal facade / memory-gate + context. See plan.md §2 w2-rollout, dev-docs/schemas/W2-STRUCTURED-SCHEMAS.md (orchestration: subtasks/next_action), cabal-devmelopner/core/agent.py, wsfull-wave-2026-07-09-compact.md. Cross-repo with cabal + memory-gate-rs.
Tero cites to plan/wsfull.
