#!/usr/bin/env python3
"""news-image-20261124 entry: write the front page to /output/entry.png.

The image (entry.png, committed next to this file) is the broadsheet front
page for Tuesday, 24 November 2026, rendered in the build session from the
day's curated news. This program only copies it, so both runs write
byte-identical output. Standard library only; no network, no randomness.

Layout of the source file is resolved from MAKEFUN_BOT_DIR (the directory
the harness mounts the repository at), never from the working directory.
"""
import hashlib
import os
import shutil

BOT_DIR = os.environ.get("MAKEFUN_BOT_DIR", "/bot")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(BOT_DIR, "entry.png")
DST = os.path.join(OUT_DIR, "entry.png")

# sha256 of the committed entry.png; the copy is verified against it.
EXPECTED_SHA256 = (
    "c2b3ac534ff30c8d4fd38b1e56553ada7111e1b4b8af360c210922513d3c6e79"
)


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(SRC, "rb") as fh:
        magic = fh.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise SystemExit("entry.png is not a PNG file")
    shutil.copyfile(SRC, DST)
    digest = sha256_of(DST)
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"entry.png sha256 mismatch: got {digest}, "
            f"expected {EXPECTED_SHA256}"
        )
    size = os.path.getsize(DST)
    if size > 1_048_576:
        raise SystemExit(f"entry.png too large: {size} bytes")
    print(f"wrote {DST} ({size} bytes, sha256 {digest[:16]}...)")


if __name__ == "__main__":
    main()
