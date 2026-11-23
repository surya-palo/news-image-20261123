#!/usr/bin/env python3
"""news-image-20261123 entrypoint.

Copies the pre-rendered poster (entry.png, drawn by render_poster.py)
to the output directory and verifies its SHA-256 so both graded runs
produce byte-identical output. Standard library only, no network.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"

# SHA-256 of entry.png as rendered and visually checked on 23 Nov 2026.
EXPECTED_SHA256 = (
    "71b3ed1f3e28890953fe558edef0f4f9ff08d89e961dfb53a992bb1434dfb266"
)
EXPECTED_BYTES = 144677
MAX_BYTES = 1048576
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"

    data = SOURCE.read_bytes()
    if not data.startswith(PNG_MAGIC):
        print("error: entry.png is not a PNG file", file=sys.stderr)
        return 1
    if len(data) > MAX_BYTES:
        print(f"error: entry.png exceeds 1 MiB: {len(data)}", file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"error: entry.png sha256 mismatch: {digest}", file=sys.stderr)
        return 1
    if len(data) != EXPECTED_BYTES:
        print(f"error: entry.png size mismatch: {len(data)}", file=sys.stderr)
        return 1

    shutil.copyfile(SOURCE, target)
    check = hashlib.sha256(target.read_bytes()).hexdigest()
    if check != EXPECTED_SHA256:
        print("error: copied file sha256 mismatch", file=sys.stderr)
        return 1
    print(f"wrote {target} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
