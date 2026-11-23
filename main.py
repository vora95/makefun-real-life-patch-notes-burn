#!/usr/bin/env python3
"""Real-Life Patch Notes (burn): write one patch-note line to /output/entry.txt.

Validation (added after first run): the entry must be a single line of
1-160 characters with no trailing newline; the file is read back and
checked byte-identical before the program exits.
"""
import os

ENTRY = "v4.0.1: fixed a bug where the snooze button spawned nine extra alarms instead of silence."

assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} out of range"
assert "\n" not in ENTRY, "entry must be a single line"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

with open(path, "rb") as f:
    data = f.read()
assert data == ENTRY.encode("utf-8"), "read-back mismatch"
assert not data.endswith(b"\n"), "trailing newline found"
