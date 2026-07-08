# Contributing to dev-mcp

`dev-mcp` is a documentation-first umbrella/index repo for the `tzervas` MCP server family. There
is no server code here to contribute to directly — most contributions will fall into one of these
categories.

## What belongs here

- Updates to the [server inventory](README.md#server-inventory) (new server, status change, repo
  move).
- Additions/fixes to a server's stub under [`servers/`](servers/) (install instructions, `.mcp.json`
  registration snippet).
- Updates to [`AGENTS.md`](AGENTS.md) — the local bring-up instructions for the whole family.
- Cross-cutting conventions shared by the family (naming, licensing, MCP registration format).

## What does *not* belong here

- Server implementation code. If you want to change how a server behaves, open the PR in that
  server's own repo (linked from the inventory table).
- Vendored copies of another repo's source.

## Adding a new server to the inventory

1. Add a row to the table in [`README.md`](README.md#server-inventory): name, one-line purpose,
   repo link, status.
2. Add a stub file under `servers/<name>.md` following the existing stubs' shape (purpose, repo,
   install, `.mcp.json` snippet).
3. If it changes what "stand up the whole family" means, update [`AGENTS.md`](AGENTS.md).

## Workflow

- Branch from `main`, open a PR — no direct pushes to `main`.
- Keep changes scoped: a status update or a new server stub is a small, reviewable diff.
- Be honest about status. If a server is planned but not yet published, say so — don't imply it's
  further along than it is.

## Reporting issues

Issues about a specific server's *behavior* belong in that server's own repo. Issues about the
*index itself* (a stale link, a wrong status, a missing server) belong here.

## License

By contributing, you agree your contributions are licensed under this repo's [MIT license](LICENSE).
