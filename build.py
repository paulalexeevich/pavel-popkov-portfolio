#!/usr/bin/env python3
"""Assemble portfolio-pavel-popkov.html from src/shell.html + src/cases.html + src/agents.html.

Usage: python3 build.py
"""
import io
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "portfolio-pavel-popkov.html")


def read(name):
    with io.open(os.path.join(SRC, name), encoding="utf-8") as f:
        return f.read()


def main():
    shell = read("shell.html")
    cases = read("cases.html")
    agents = read("agents.html")

    missing = [tag for tag in ("<!--{{CASES}}-->\n\n", "<!--{{AGENTS}}-->\n\n") if tag not in shell]
    if missing:
        raise SystemExit(f"shell.html is missing placeholder(s): {missing}")

    html = shell.replace("<!--{{CASES}}-->\n\n", cases).replace("<!--{{AGENTS}}-->\n\n", agents)

    with io.open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"wrote {OUT} ({len(html)} bytes)")


if __name__ == "__main__":
    main()
