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
```
