#!/usr/bin/env python3
"""
Generate docs/index.md with Colab links for every notebook in colab-notebooks/.

Usage:
  python3 scripts/generate_index.py --owner dr-rachel-bg-teaching --repo CBE3610 --branch main

Run this from the repo root.
"""
import argparse
from pathlib import Path
import sys

TEMPLATE_TOP = """# CBE3610 — Course Materials

Welcome — this page lists the lecture Colab notebooks for CBE3610. Click any notebook to open it directly in Google Colab.

Notebooks (open in Colab)
"""

TEMPLATE_BOTTOM = """

Notes
- These links point to the `{branch}` branch. If you merge your PR to that branch the links will be live for students.
- If you add/remove notebooks later, re-run this script to update this file automatically.
"""

def make_colab_link(owner, repo, branch, relpath):
    # relpath is like "colab-notebooks/00_xxx.ipynb"
    return f"https://colab.research.google.com/github/{owner}/{repo}/blob/{branch}/{relpath}"

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--owner", required=True, help="GitHub owner/org (default: dr-rachel-bg-teaching)")
    p.add_argument("--repo", required=True, help="Repository name (default: CBE3610)")
    p.add_argument("--branch", default="main", help="Target branch used in URLs (default: main)")
    p.add_argument("--notebook-dir", default="colab-notebooks", help="Directory containing notebooks")
    p.add_argument("--out", default="docs/index.md", help="Output markdown file")
    args = p.parse_args()

    nb_dir = Path(args.notebook_dir)
    if not nb_dir.exists():
        print(f"Error: {nb_dir} does not exist. Run this from the repository root.", file=sys.stderr)
        sys.exit(1)

    notebooks = sorted(nb_dir.glob("*.ipynb"), key=lambda p: p.name.lower())
    if not notebooks:
        print(f"No notebooks found in {nb_dir}", file=sys.stderr)
        sys.exit(1)

    out_lines = [TEMPLATE_TOP]
    for nb in notebooks:
        rel = f"{nb_dir}/{nb.name}"
        url = make_colab_link(args.owner, args.repo, args.branch, rel)
        out_lines.append(f"- [{nb.name}]({url})")
    out_lines.append(TEMPLATE_BOTTOM.format(branch=args.branch))

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(out_lines))
    print(f"Wrote {out_path} ({len(notebooks)} notebooks)")

if __name__ == "__main__":
    main()
