# dev-mcp — Product Roadmap

**Status:** Living (2026-07-08)  
**North star:** Single accurate map of the MCP family — clone paths, doctor commands, status honesty, links to each repo’s assessment/roadmap.

Companion: [ASSESSMENT.md](ASSESSMENT.md).

---

## Waves

### Wave A — Truth pass (now)

| ID | Work |
|----|------|
| D-A1 | Rewrite server inventory table (tero live; context ≠ RAG; add webpuppet-rs-mcp, search-box) |
| D-A2 | Link each `servers/*.md` to leaf `docs/ROADMAP.md` |
| D-A3 | AGENTS.md: cold-start tero + family clone list |
| D-A4 | `scripts/doctor-all.sh` sketch (optional): run `grok mcp doctor` / binary `--help` |

### Wave B — Onboarding UX

| ID | Work |
|----|------|
| D-B1 | One-page “local secure defaults” (stdio, loopback, tokens) |
| D-B2 | cabal-devmelopner consumption matrix (which MCP at which wave) |
| D-B3 | Version badge / last-reviewed date per server row |

### Wave C — Optional automation

| ID | Work |
|----|------|
| D-C1 | CI that checks links to sibling repos resolve |
| D-C2 | Generate inventory from a YAML source of truth |

---

## API plan

dev-mcp exposes **no runtime API**.  

**Doc “API”:** stable paths leaf repos should keep:

```text
docs/ASSESSMENT.md   # status + gaps
docs/ROADMAP.md      # waves + API plans
```

Umbrella `servers/<name>.md` template:

```markdown
# <name>
Status: ...
Repo: ...
Install: ...
Doctor: ...
Assessment: <repo>/docs/ASSESSMENT.md
Roadmap: <repo>/docs/ROADMAP.md
```

---

## PR plan

1. Assessment + roadmap (this)  
2. Inventory truth pass  
3. AGENTS cold-start + cabal matrix  
4. Optional doctor script  

---

## Family clone layout (canonical)

```text
$GIT_PARENT/
  dev-mcp/
  tero-mcp/
  context-mcp/
  security-mcp/
  agent-mcp/
  webpuppet-rs/
  webpuppet-rs-mcp/
  search-box/
  cabal-devmelopner/   # consumer
  mycelium/            # default tero index

## W2 Rollout Docs Wiring (chore/w2-rollout-docs-wiring)

- Appended W2 usage notes (cabal facade ex, cross-repo cabal+memory) to servers/*.md , README, ASSESSMENT, this ROADMAP.
- Context: session as W2 consumer (domain CONTEXT in CommonMemory facade).
- Memory-gate: facade evolution refs.
- Cites (to plan/wsfull): plan.md §2 w2-rollout (W2 StructuredResponse/CommonMemoryAdapter + AgentDomain M1 mirrors), wsfull-wave-2026-07-09-compact.md (W2 Common Memory + schemas), dev-docs/schemas/W2-STRUCTURED-SCHEMAS.md .
- Follow-on: tero update per leaf; hygiene; land --no-ff to dev then main; propagate; verify tero "W2|facade|Structured|CommonMemory".

See plan.md:44, dev-docs/waves/wsfull-*.md .

## Orch Wiring Inventory Truth (chore/orch-wiring-devmcp)

Appended to advance orch in dev per plan.md §3 (orch-wiring): cabal consumption matrix + inventory truth (W2 facade, memory-gate domains).

- D-A1/D-A2 progress: server inventory table (README) + servers/README.md now links leaf ROADMAP.md (e.g. memory-gate-rs, cabal as consumer) + ASSESSMENT cross-refs; added orch matrix.
- D-B2: cabal-devmelopner consumption matrix realized in servers/README.md#orch-inventory-truth (cabal as primary leaf for dev-mcp tasks; W2 facade matrix rows for consumers + domains).
- memory-gate domains (M1): listed + referenced (TERO primary for tero L1 in cabal facade; CONTEXT etc).
- Doctor notes: sketched (per-server --help + future doctor-all.sh); links in servers/README.
- Cabal as consumer: explicit (family clone + matrix); cabal uses dev-mcp for onboarding, registers servers, consumes as leaf executor (tools + W2 orch).
- Tero cites (pre-edit): dev-mcp text_search "orch inventory w2 cabal" (hits: memory-gate-rs--w2-mirror-to-cabal-tero, readme--server-inventory, roadmap--w2..., assessment--w2..., agent-mcp--w2-usage-notes); global workspacecabalteroreadiness--leaf-orch-review-tranche-wsfull + plan.md §3.
- Cross: cabal AGENTS (appends on dev-mcp orch use), docs/ROADMAP (as leaf).

Next (Wave B/C): doctor script, CI link check, consumption badges. Land --no-ff dev/main + propagate + verify tero hits. See ASSESSMENT update, servers/README for matrix.

Refs: plan.md:60 (dev-mcp critical paths), wsfull-wave-2026-07-09-compact.md, WORKSPACE_CABAL_TERO_READINESS.md. Append-only.
```
## Semver baseline (appended 2026-07-10)

Per plan + user: start with toolchain + dev support semver + releases.

- dev-mcp baseline v0.1.0.
- See AGENTS.md for details, cites, local GHCR preference (podman, no Actions).
- Extracted dev tooling from mycelium.

Cites: plan.md, tero (dev support mentions).
