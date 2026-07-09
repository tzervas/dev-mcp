# dev-mcp — Tero Index (Layer 1)

> **Honesty:** Empirical/Declared — lite heading/line heuristic over markdown in dev-mcp via tero-mcp/scripts/generate_lite_index.py; source files are ground truth. Generated 2026-07-09.
> Use this index to find where to Read, not as authoritative ground truth.

- **Items:** 62
- **Flagged:** 0
- **item_tag:** `Empirical/Declared`
- **Machine index:** [`index.json`](./index.json)
- **Manifest:** [`MANIFEST.toml`](./MANIFEST.toml)

## doc (62 entries)

| Anchor | Kind | Id | Title | File:Line | Status | Summary |
|---|---|---|---|---|---|---|
| `agents` | section | — | AGENTS.md — standing up the MCP family locally | `AGENTS.md:1` | — | This is the umbrella bring-up guide: how an agent (or a human) clones, builds, and registers the |
| `agents--1.-prerequisites` | section | — | 1. Prerequisites | `AGENTS.md:7` | — | - git |
| `agents--2.-clone-each-server` | section | — | 2. Clone each server | `AGENTS.md:15` | — | Pick a working directory (e.g. ~/dev/mcp/) and clone the servers you need. Not every server is |
| `agents--tero-mcp-not-yet-published-clone-once-it-exists-see-servers-tero-mcp.md` | other | — | tero-mcp: not yet published — clone once it exists (see servers/tero-mcp.md) | `AGENTS.md:27` | — | All current family members are Rust crates; build each with cargo: |
| `agents--3.-build-each-server` | section | — | 3. Build each server | `AGENTS.md:30` | — | All current family members are Rust crates; build each with cargo: |
| `agents--4.-register-with-your-mcp-client` | section | — | 4. Register with your MCP client | `AGENTS.md:47` | — | Merge the snippets from [servers/.md](servers/) into your client's MCP config |
| `agents--5.-verify` | section | — | 5. Verify | `AGENTS.md:76` | — | Restart your MCP client and confirm each server shows as connected. Each server's own repo has |
| `agents--notes-for-agents-doing-this-work` | section | — | Notes for agents doing this work | `AGENTS.md:82` | — | - This repo indexes the family; it doesn't vendor or rebuild their code. Don't copy server |
| `contributing` | section | — | Contributing to dev-mcp | `CONTRIBUTING.md:1` | — | dev-mcp is a documentation-first umbrella/index repo for the tzervas MCP server family. There |
| `contributing--what-belongs-here` | section | — | What belongs here | `CONTRIBUTING.md:7` | — | - Updates to the [server inventory](README.md#server-inventory) (new server, status change, repo |
| `contributing--what-does-not-belong-here` | section | — | What does *not* belong here | `CONTRIBUTING.md:16` | — | - Server implementation code. If you want to change how a server behaves, open the PR in that |
| `contributing--adding-a-new-server-to-the-inventory` | section | — | Adding a new server to the inventory | `CONTRIBUTING.md:22` | — | 1. Add a row to the table in [README.md](README.md#server-inventory): name, one-line purpose, |
| `contributing--workflow` | section | — | Workflow | `CONTRIBUTING.md:30` | — | - Branch from main, open a PR — no direct pushes to main. |
| `contributing--reporting-issues` | section | — | Reporting issues | `CONTRIBUTING.md:37` | — | Issues about a specific server's behavior belong in that server's own repo. Issues about the |
| `contributing--license` | section | — | License | `CONTRIBUTING.md:42` | — | By contributing, you agree your contributions are licensed under this repo's [MIT license](LICENSE). |
| `readme` | other | — | dev-mcp | `README.md:1` | — | The umbrella index for the tzervas MCP (Model Context Protocol) server family. |
| `readme--server-inventory` | section | — | Server inventory | `README.md:11` | — | Per-server details (purpose, install, .mcp.json registration snippet) live under |
| `readme--why-links-not-submodules` | section | — | Why links, not submodules | `README.md:23` | — | Each server above is linked, not vendored as a git submodule. The family spans independent |
| `readme--what-this-repo-is-for` | section | — | What this repo is for | `README.md:31` | — | - Discovery — one place to see every MCP server in the family, its purpose, and its status. |
| `readme--what-this-repo-is-not-for` | section | — | What this repo is *not* for | `README.md:39` | — | - Server implementation code (that lives in each server's own repo). |
| `readme--contributing` | section | — | Contributing | `README.md:44` | — | See [CONTRIBUTING.md](CONTRIBUTING.md). |
| `readme--license` | section | — | License | `README.md:48` | — | MIT — see [LICENSE](LICENSE). Matches the licensing of the sibling server repos. |
| `readme--status-roadmap` | section | — | Status & roadmap | `README.md:52` | — | - [Assessment & gaps](docs/ASSESSMENT.md) |
| `assessment` | note | — | dev-mcp — Assessment & Gap Analysis | `docs/ASSESSMENT.md:1` | — | Date: 2026-07-08 |
| `assessment--1.-what-it-is` | section | — | 1. What it is | `docs/ASSESSMENT.md:9` | — | Index + onboarding for: |
| `assessment--2.-gaps` | section | — | 2. Gaps | `docs/ASSESSMENT.md:24` | — | — |
| `assessment--3.-maturity-as-umbrella-3-5-after-refresh` | section | — | 3. Maturity as umbrella: **3 / 5** after refresh | `docs/ASSESSMENT.md:36` | — | Useful discovery; must track reality of leaf repos’ docs/ASSESSMENT.md + docs/ROADMAP.md. |
| `roadmap` | note | — | dev-mcp — Product Roadmap | `docs/ROADMAP.md:1` | Living (2026-07-08) | Status: Living (2026-07-08) |
| `roadmap--waves` | section | — | Waves | `docs/ROADMAP.md:10` | — | — |
| `roadmap--wave-a-truth-pass-now` | section | — | Wave A — Truth pass (now) | `docs/ROADMAP.md:12` | — | — |
| `roadmap--wave-b-onboarding-ux` | section | — | Wave B — Onboarding UX | `docs/ROADMAP.md:21` | — | — |
| `roadmap--wave-c-optional-automation` | section | — | Wave C — Optional automation | `docs/ROADMAP.md:29` | — | dev-mcp exposes no runtime API. |
| `roadmap--api-plan` | section | — | API plan | `docs/ROADMAP.md:38` | — | dev-mcp exposes no runtime API. |
| `roadmap--name` | other | — | <name> | `docs/ROADMAP.md:52` | — | Status: ... |
| `roadmap--pr-plan` | section | — | PR plan | `docs/ROADMAP.md:63` | — | 1. Assessment + roadmap (this) |
| `roadmap--family-clone-layout-canonical` | section | — | Family clone layout (canonical) | `docs/ROADMAP.md:72` | — | $GITPARENT/ |
| `readme-2` | other | — | Servers index | `servers/README.md:1` | — | One stub per server in the family — purpose, repo, install, and the .mcp.json snippet to |
| `readme--submodules-vs.-links` | section | — | Submodules vs. links | `servers/README.md:14` | — | This directory links to each server's repo rather than checking it out as a git submodule. That |
| `agent-mcp` | section | — | agent-mcp | `servers/agent-mcp.md:1` | — | Multi-LLM orchestration. |
| `agent-mcp--status` | section | — | Status | `servers/agent-mcp.md:9` | — | Active development. |
| `agent-mcp--repo` | section | — | Repo | `servers/agent-mcp.md:13` | — | <https://github.com/tzervas/agent-mcp> |
| `agent-mcp--install` | section | — | Install | `servers/agent-mcp.md:17` | — | git clone https://github.com/tzervas/agent-mcp |
| `agent-mcp--register-in-.mcp.json` | section | — | Register in `.mcp.json` | `servers/agent-mcp.md:25` | — | { |
| `context-mcp` | section | — | context-mcp | `servers/context-mcp.md:1` | — | RAG context store. |
| `context-mcp--status` | section | — | Status | `servers/context-mcp.md:11` | — | Production-ready for context storage and lightweight RAG; APIs stable. |
| `context-mcp--repo` | section | — | Repo | `servers/context-mcp.md:15` | — | <https://github.com/tzervas/context-mcp> |
| `context-mcp--install` | section | — | Install | `servers/context-mcp.md:19` | — | cargo install context-mcp |
| `context-mcp--or-build-from-source` | other | — | or build from source | `servers/context-mcp.md:23` | — | git clone https://github.com/tzervas/context-mcp |
| `context-mcp--register-in-.mcp.json` | section | — | Register in `.mcp.json` | `servers/context-mcp.md:31` | — | { |
| `security-mcp` | section | — | security-mcp | `servers/security-mcp.md:1` | — | Content screening. |
| `security-mcp--status` | section | — | Status | `servers/security-mcp.md:10` | — | Alpha / active development — rules and thresholds will evolve. |
| `security-mcp--repo` | section | — | Repo | `servers/security-mcp.md:14` | — | <https://github.com/tzervas/security-mcp> |
| `security-mcp--install` | section | — | Install | `servers/security-mcp.md:18` | — | cargo install security-mcp |
| `security-mcp--or-build-from-source` | other | — | or build from source | `servers/security-mcp.md:22` | — | git clone https://github.com/tzervas/security-mcp |
| `security-mcp--register-in-.mcp.json` | section | — | Register in `.mcp.json` | `servers/security-mcp.md:28` | — | { |
| `tero-mcp` | section | — | tero-mcp | `servers/tero-mcp.md:1` | — | Transparent, cited-memory MCP server. |
| `tero-mcp--status` | section | — | Status | `servers/tero-mcp.md:9` | — | New. This is the newest member of the family — the repo (tzervas/tero-mcp) has not been |
| `tero-mcp--repo` | section | — | Repo | `servers/tero-mcp.md:15` | — | <https://github.com/tzervas/tero-mcp> (not yet published) |
| `tero-mcp--install` | section | — | Install | `servers/tero-mcp.md:19` | — | git clone https://github.com/tzervas/tero-mcp |
| `tero-mcp--once-published` | other | — | once published: | `servers/tero-mcp.md:22` | — | git clone https://github.com/tzervas/tero-mcp |
| `tero-mcp--build-steps-tbd-update-once-the-repos-own-readme-specifies-its-toolchain` | other | — | build steps TBD — update once the repo's own README specifies its toolchain | `servers/tero-mcp.md:25` | — | { |
| `tero-mcp--register-in-.mcp.json` | section | — | Register in `.mcp.json` | `servers/tero-mcp.md:28` | — | { |

