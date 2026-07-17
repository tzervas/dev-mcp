#!/usr/bin/env python3
"""Compose a client .mcp.json from servers/catalog.yaml.

Stub / utility for the dev-mcp umbrella index. Does not install or build servers;
it only emits MCP client registration JSON from the machine-readable catalog.

Usage:
  python3 scripts/compose-mcp-json.py
  python3 scripts/compose-mcp-json.py --base-dir ~/dev/mcp --out .mcp.json
  python3 scripts/compose-mcp-json.py --only tero-mcp,context-mcp
  python3 scripts/compose-mcp-json.py --list

Requires: PyYAML (pip install pyyaml) OR a stdlib-only fallback that only
supports a tiny subset — prefer PyYAML. If PyYAML is missing, the script
prints install hints and exits non-zero.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CATALOG = ROOT / "servers" / "catalog.yaml"


def load_catalog(path: Path) -> dict:
    try:
        import yaml  # type: ignore
    except ImportError as e:
        print(
            "compose-mcp-json.py: PyYAML required. Install with:\n"
            "  pip install pyyaml\n"
            "  # or: uv pip install pyyaml",
            file=sys.stderr,
        )
        raise SystemExit(2) from e
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "servers" not in data:
        raise SystemExit(f"invalid catalog: {path}")
    return data


def expand(value: str, base_dir: str) -> str:
    return (
        value.replace("{base_dir}", base_dir)
        .replace("${MCP_BASE_DIR}", base_dir)
        .replace("$HOME", os.path.expanduser("~"))
    )


def expand_obj(obj, base_dir: str):
    if isinstance(obj, str):
        return expand(obj, base_dir)
    if isinstance(obj, list):
        return [expand_obj(x, base_dir) for x in obj]
    if isinstance(obj, dict):
        return {k: expand_obj(v, base_dir) for k, v in obj.items()}
    return obj


def compose(catalog: dict, base_dir: str, only: set[str] | None) -> dict:
    servers_out: dict = {}
    for entry in catalog.get("servers", []):
        sid = entry.get("id") or entry.get("name")
        if only and sid not in only and entry.get("name") not in only:
            continue
        mcp = entry.get("mcp")
        if not mcp:
            continue  # library-only (e.g. memory-gate-rs)
        key = mcp.get("key") or sid
        block: dict = {}
        if mcp.get("type"):
            block["type"] = mcp["type"]
        if mcp.get("command"):
            block["command"] = expand(str(mcp["command"]), base_dir)
        if mcp.get("args"):
            block["args"] = expand_obj(mcp["args"], base_dir)
        if mcp.get("env"):
            block["env"] = expand_obj(mcp["env"], base_dir)
        servers_out[key] = block
    return {"mcpServers": servers_out}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    p.add_argument(
        "--catalog",
        type=Path,
        default=DEFAULT_CATALOG,
        help=f"path to catalog.yaml (default: {DEFAULT_CATALOG})",
    )
    p.add_argument(
        "--base-dir",
        default=os.environ.get("MCP_BASE_DIR", os.path.expanduser("~/dev/mcp")),
        help="root where sibling server repos are cloned (default: ~/dev/mcp or $MCP_BASE_DIR)",
    )
    p.add_argument(
        "--only",
        default="",
        help="comma-separated server ids to include (default: all with mcp blocks)",
    )
    p.add_argument("--out", type=Path, help="write JSON to this path (default: stdout)")
    p.add_argument(
        "--list",
        action="store_true",
        help="list catalog servers (id, status, repo) and exit",
    )
    args = p.parse_args(argv)

    catalog = load_catalog(args.catalog)

    if args.list:
        for entry in catalog.get("servers", []):
            mcp = "mcp" if entry.get("mcp") else "lib-only"
            print(
                f"{entry.get('id'):20}  {entry.get('status', '?'):24}  "
                f"{mcp:8}  {entry.get('repo', '')}"
            )
        return 0

    only = {s.strip() for s in args.only.split(",") if s.strip()} or None
    base_dir = os.path.expanduser(args.base_dir.rstrip("/"))
    doc = compose(catalog, base_dir, only)
    text = json.dumps(doc, indent=2) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
        print(f"wrote {args.out} ({len(doc.get('mcpServers', {}))} servers)", file=sys.stderr)
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
