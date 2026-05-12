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

### Article Template

Use this template to structure notebooks and articles. It follows the organization used in `portfolio_ml_trails_no_phacking_testing.ipynb`.

- **Title & Abstract**: brief title and 2–4 sentence abstract describing the question and main takeaway.
- **Introduction**: motivation, related work, and contributions.
- **Notebook Setup**: environment, imports, and reproducibility (seed, package versions).
- **Data / Simulation**: describe data sources or the synthetic data-generating process and parameters.
- **Methods / Theory**: clear derivations with math using `$...$` or `$$...$$`; list assumptions (IID, stationarity, etc.).
- **Experiments / Results**: runnable code, tables, and plots presenting core findings.
- **Diagnostics & Robustness**: leverage, residuals, heteroskedasticity checks, bootstraps, robust SEs.
- **Discussion & Limitations**: interpretation, caveats, and next steps.
- **Reproducibility & Commands**: how to run the notebook and export outputs (example commands).
- **References**: include bibliographic links to PDFs in `papers/` and external sources.

Tip: keep markdown academic and concise; prefer reproducible code blocks and avoid heavy formatting. Place mathematical expressions between `$` or `$$` as appropriate.

Remove LLM glyphs. 62 em-dashes, 8 arrows, plus ≤ ≥ × Δ σ ▼ ▲ § … were swept out. Replacements are plain: -, ->, <=, >=, x, delta, sigma, down, up, section, ....