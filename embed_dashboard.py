#!/usr/bin/env python3
"""Gzip dashboard.html and emit dashboard_index.h for the ESP32 web server."""

from __future__ import annotations

import gzip
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "dashboard.html"
HEADER = ROOT / "dashboard_index.h"
ARRAY_NAME = "dashboard_html_gz"


def bytes_to_c_array(data: bytes, name: str) -> str:
    lines = []
    for i in range(0, len(data), 16):
        chunk = data[i : i + 16]
        hexes = ", ".join(f"0x{b:02X}" for b in chunk)
        lines.append(f"  {hexes},")
    body = "\n".join(lines)
    return (
        f"// Auto-generated from dashboard.html — do not edit by hand.\n"
        f"// Regenerate: python3 embed_dashboard.py\n"
        f"// Size: {len(data)} bytes (gzip)\n"
        f"#define {name}_len {len(data)}\n"
        f"const uint8_t {name}[] = {{\n"
        f"{body}\n"
        f"}};\n"
    )


def main() -> int:
    if not HTML.exists():
        print(f"Missing {HTML}", file=sys.stderr)
        return 1

    raw = HTML.read_bytes()
    gz = gzip.compress(raw, compresslevel=9, mtime=0)
    HEADER.write_text(bytes_to_c_array(gz, ARRAY_NAME), encoding="utf-8")
    print(f"Wrote {HEADER.name}: {len(raw)} bytes HTML -> {len(gz)} bytes gzip")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
