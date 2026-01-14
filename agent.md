# Agent Profile

## Purpose
Assist with quantitative research notebooks, statistical validation, and clear academic-style writing for ML/quant finance.

## Environment
- OS: Windows
- Shell: PowerShell
- Repo root: C:\Users\adamd\workspace\quant_research
- Active file focus: `dont_get_fooled_by_chance.ipynb`
- Notebook format: Jupyter `.ipynb`

## Tools and Workflow
- Use ripgrep (`rg`) for fast search; fall back only if unavailable.
- Prefer Python scripts for structured edits in notebooks.
- Keep edits minimal and targeted; avoid touching unrelated cells.
- Validate code paths in-place; do not add auto-formatters unless asked.

## Style and Writing
- Academic, precise, and direct; avoid fluff.
- Favor terms: ?candidate model?, ?in-sample evaluation?, ?sampling variability?.
- Frame results in ML pipeline terms when relevant (AutoML, hyperparameter search).
- Explicitly note limitations (IID assumptions, non-stationarity, economic significance).
- Keep math notation consistent; keep frequency/annualization explicit.

## Technical Preferences
- Use ASCII by default; only introduce non-ASCII if file already uses it.
- Add brief comments only where logic is non-obvious.
- In notebooks, keep markdown concise and structured.

## Testing and Validation
- Run notebook cells only when requested or when validating critical changes.
- For statistical routines, add simple sanity checks if requested.
- Avoid long-running simulations unless requested.

## Dependency Management
- Prefer existing `requirements.txt` or `environment.yml`.
- Installing packages should be explicit and minimal; document any new dependencies.
- Use `pip` only when asked or required to reproduce a bug.

## File and Output Conventions
- Keep outputs deterministic (seed RNG where applicable).
- Use clear section headers and descriptive cell titles.
- For tables/plots, keep labels explicit about units and sampling frequency.
## Linting (Ruff)
- Use Ruff for Python linting when requested.
- Prefer `ruff check .` for repo-wide checks.
- For auto-fixes, use `ruff check . --fix` only when explicitly asked.
- Install via `pip install ruff` (or add to `requirements.txt`) when setup is requested.

