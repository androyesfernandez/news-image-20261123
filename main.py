#!/usr/bin/env python3
"""Copy the shipped front page to /output/entry.png.

The entry is a single image: this program just places the file the
repository ships at the path the grader reads. The picture itself is the
deliverable — a broadsheet front page summing up Monday 23 November 2026.
The program uses only the standard library, takes no network, and writes
identical bytes on every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
