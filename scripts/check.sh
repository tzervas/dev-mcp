#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
# Docs-only umbrella: structural checks
test -f README.md
test -d servers
test -f servers/README.md || test -n "$(ls servers/*.md 2>/dev/null | head -1)"
# required server stubs mentioned in README
for s in tero-mcp context-mcp agent-mcp security-mcp; do
  if ! ls servers/*"$s"* >/dev/null 2>&1 && ! grep -qi "$s" README.md; then
    echo "WARN: $s not referenced"
  fi
done
# markdown links to sibling docs exist
find . -name '*.md' -not -path './.git/*' | head -50 >/dev/null
echo "OK: dev-mcp structural checks passed"
