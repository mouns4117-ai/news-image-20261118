#!/usr/bin/env python3
"""Write the 18 November 2026 world-news image to /output/entry.png.

The finished poster lives in this repository as news.png. This program
copies it byte for byte, so every run produces identical output. It uses
only the Python standard library and needs no network.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "news.png"


def output_dir() -> Path:
    """Where the image goes: /output, or MAKEFUN_OUTPUT_DIR when set."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    if not SOURCE.is_file():
        raise SystemExit(f"missing image next to this program: {SOURCE}")
    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    # The run is only valid if the copy is exact: same size, same bytes.
    if target.stat().st_size != SOURCE.stat().st_size:
        raise SystemExit("copy size mismatch: entry.png is not byte-identical")
    print(f"wrote {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
