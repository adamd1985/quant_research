# Agents

## NotebookExportAgent
Purpose: export notebooks to HTML, PDF, and DOCX using nbconvert and pandoc.

Usage:
- `python scripts/export_notebook.py --notebook dont_get_fooled_by_chance.ipynb --output-dir exports`
- `powershell -ExecutionPolicy Bypass -File scripts\export_notebook.ps1 -Notebook dont_get_fooled_by_chance.ipynb -OutDir exports`

Dependencies:
- `jupyter nbconvert` available in the Python environment
- `pandoc` on PATH
- a TeX engine (e.g., `xelatex`) for PDF output
