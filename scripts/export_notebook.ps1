param(
    [string]$Notebook = "dont_get_fooled_by_chance.ipynb",
    [string]$OutDir = "exports",
    [string]$PdfEngine = "xelatex"
)

$script = Join-Path $PSScriptRoot "export_notebook.py"
python $script --notebook $Notebook --output-dir $OutDir --pdf-engine $PdfEngine
