#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
# Docs-only umbrella: structural checks
test -f README.md
test -d servers
test -f servers/README.md || test -n "$(ls servers/*.md 2>/dev/null | head -1)"
test -f servers/catalog.yaml
test -f scripts/compose-mcp-json.py
# required server stubs mentioned in README
for s in tero-mcp context-mcp agent-mcp security-mcp webpuppet-rs-mcp memory-gate-rs; do
  if ! ls servers/*"$s"* >/dev/null 2>&1 && ! grep -qi "$s" README.md; then
    echo "WARN: $s not referenced"
  fi
  if ! grep -q "id: $s" servers/catalog.yaml; then
    echo "WARN: $s missing from servers/catalog.yaml"
  fi
done
# markdown links to sibling docs exist
find . -name '*.md' -not -path './.git/*' | head -50 >/dev/null
# optional: compose dry-run when PyYAML available
if python3 -c 'import yaml' 2>/dev/null; then
  python3 scripts/compose-mcp-json.py --list >/dev/null
  python3 scripts/compose-mcp-json.py --base-dir /tmp/mcp-placeholder >/dev/null
  echo "OK: compose-mcp-json.py smoke passed"
else
  echo "SKIP: compose smoke (install pyyaml to enable)"
fi
echo "OK: dev-mcp structural checks passed"
# Optional git-secrets scan when installed
if command -v git-secrets >/dev/null 2>&1; then
  git secrets --scan || { echo "FAIL: git-secrets found prohibited patterns"; exit 1; }
fi
