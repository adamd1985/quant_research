#!/usr/bin/env python
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> None:
    print(">>", " ".join(cmd))
    subprocess.check_call(cmd)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a Jupyter notebook to HTML, PDF, and DOCX.")
    parser.add_argument("--notebook", default="dont_get_fooled_by_chance.ipynb", help="Input notebook path")
    parser.add_argument("--output-dir", default="exports", help="Output directory")
    parser.add_argument("--output-name", default=None, help="Base name for outputs (defaults to notebook stem)")
    parser.add_argument("--pdf-engine", default="xelatex", help="Pandoc PDF engine (requires TeX)")
    args = parser.parse_args()

    notebook = Path(args.notebook).resolve()
    if not notebook.exists():
        raise SystemExit(f"Notebook not found: {notebook}")

    out_dir = Path(args.output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    base = args.output_name or notebook.stem

    # Export HTML and Markdown via nbconvert
    run([
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "html",
        "--output", base,
        "--output-dir", str(out_dir),
        str(notebook),
    ])

    run([
        sys.executable, "-m", "jupyter", "nbconvert",
        "--to", "markdown",
        "--output", base,
        "--output-dir", str(out_dir),
        str(notebook),
    ])

    md_path = out_dir / f"{base}.md"
    if not md_path.exists():
        raise SystemExit(f"Markdown export not found: {md_path}")

    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise SystemExit("pandoc not found in PATH")

    # DOCX via pandoc
    run([pandoc, "-s", str(md_path), "-o", str(out_dir / f"{base}.docx")])

    # PDF via pandoc (requires LaTeX)
    pdf_cmd = [pandoc, "-s", str(md_path), "-o", str(out_dir / f"{base}.pdf")]
    if args.pdf_engine:
        pdf_cmd.extend(["--pdf-engine", args.pdf_engine])
    run(pdf_cmd)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
