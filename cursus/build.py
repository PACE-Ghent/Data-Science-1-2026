"""Bouw de cursusteksten (PDF) voor de labo's.

Elke bron in `sources/` is LaTeX met Python-blokken:

    \\begin{python}            code tonen, uitvoeren en de uitvoer tonen
    \\begin{python}[noout]     code tonen en uitvoeren, geen uitvoer tonen
    \\begin{python}[hide]      alleen uitvoeren (bv. voorbereiding)
    \\begin{python}[outonly]   uitvoeren en alleen de uitvoer tonen
    \\begin{python}[noeval]    alleen tonen, niet uitvoeren
    \\begin{python}[error]     uitvoeren en de foutmelding tonen
    \\begin{python}[fig=naam]  uitvoeren en de variabele `fig` als figuur tonen

De blokken van één bron draaien na elkaar in dezelfde namespace, zoals
cellen in een notebook. Zo komt elke getoonde uitvoer echt uit de data.

Gebruik:  python build.py [labo3 labo4 ...]
Vereist:  pandas, plotly, kaleido, pygments en tectonic (of xelatex).
"""

import contextlib
import io
import os
import re
import shutil
import subprocess
import sys
import traceback
from pathlib import Path

import pandas as pd
from pygments import highlight
from pygments.formatters import LatexFormatter
from pygments.lexers import PythonLexer

HERE = Path(__file__).resolve().parent
SRC = HERE / "sources"
BUILD = HERE / "build"
DATA_DIR = str(HERE.parent / "data")

FORMATTER = LatexFormatter(commandprefix="PY", commandchars=True)
BLOCK = re.compile(r"\\begin\{python\}(?:\[(?P<opt>[^\]]*)\])?\n(?P<code>.*?)\\end\{python\}", re.S)

pd.set_option("display.width", 78)
pd.set_option("display.max_columns", 8)
pd.set_option("display.max_colwidth", 30)


def show(value):
    """Tekstweergave van de laatste expressie van een blok, zoals in een notebook."""
    if value is None:
        return ""
    if hasattr(value, "item") and getattr(value, "ndim", None) == 0:
        value = value.item()  # numpy-getal tonen als gewoon Python-getal
    if isinstance(value, pd.DataFrame):
        return value.to_string(max_rows=12, max_cols=8)
    if isinstance(value, pd.Series):
        return value.to_string(max_rows=14) + (f"\nName: {value.name}, dtype: {value.dtype}" if value.name is not None else f"\ndtype: {value.dtype}")
    return repr(value)


def run(code, ns):
    """Voer een blok uit; geef (stdout + waarde van de laatste expressie) terug."""
    import ast

    tree = ast.parse(code)
    last = tree.body.pop() if tree.body and isinstance(tree.body[-1], ast.Expr) else None
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        exec(compile(tree, "<cel>", "exec"), ns)
        value = eval(compile(ast.Expression(last.value), "<cel>", "eval"), ns) if last else None
    text = out.getvalue()
    shown = show(value)
    return (text + shown).rstrip("\n")


def verbatim(text, kind):
    if kind == "code":
        body = highlight(text, PythonLexer(), FORMATTER)
        body = body.replace("\\begin{Verbatim}[commandchars=\\\\\\{\\}]", "\\begin{Verbatim}[commandchars=\\\\\\{\\},breaklines]")
        return "\\begin{codeblok}\n" + body + "\\end{codeblok}\n"
    return "\\begin{uitvoer}\n\\begin{Verbatim}[breaklines]\n" + text + "\n\\end{Verbatim}\n\\end{uitvoer}\n"


def process(name):
    src = (SRC / f"{name}.tex").read_text()
    figdir = BUILD / "fig"
    figdir.mkdir(parents=True, exist_ok=True)
    ns = {"DATA_DIR": DATA_DIR, "__name__": "__cursus__"}

    def replace(m):
        opts = dict((o.split("=") + [True])[:2] for o in (m.group("opt") or "").split(",") if o)
        code = m.group("code").rstrip("\n")
        shown = "" if ("hide" in opts or "outonly" in opts) else verbatim(code, "code")
        if "noeval" in opts:
            return shown
        try:
            result = run(code, ns)
        except Exception as e:
            if "error" not in opts:
                print(f"\n--- fout in {name} ---\n{code}\n", file=sys.stderr)
                raise
            last = traceback.format_exception_only(type(e), e)[-1].strip()
            return shown + verbatim(last, "out")
        if "error" in opts:
            raise RuntimeError(f"blok in {name} gaf geen fout:\n{code}")
        if "fig" in opts:
            path = figdir / f"{name}_{opts['fig']}.png"
            ns["fig"].write_image(str(path), width=900, height=480, scale=2)
            return shown + f"\\figuur{{fig/{path.name}}}\n"
        if "noout" in opts or "hide" in opts or not result:
            return shown
        return shown + verbatim(result, "out")

    (BUILD / f"{name}.tex").write_text(BLOCK.sub(replace, src))


def compile_pdf(name):
    engine = shutil.which("tectonic") or os.environ.get("TECTONIC")
    if engine:
        cmd = [engine, "-X", "compile", f"{name}.tex"]
    else:
        cmd = ["latexmk", "-xelatex", "-interaction=nonstopmode", f"{name}.tex"]
    subprocess.run(cmd, cwd=BUILD, check=True)
    shutil.copy(BUILD / f"{name}.pdf", HERE / f"{name}.pdf")


def main():
    BUILD.mkdir(exist_ok=True)
    shutil.copy(HERE / "cursus.sty", BUILD / "cursus.sty")
    (BUILD / "pygments.tex").write_text(FORMATTER.get_style_defs())
    names = sys.argv[1:] or sorted(p.stem for p in SRC.glob("*.tex"))
    for name in names:
        print(f"== {name}")
        process(name)
        compile_pdf(name)


if __name__ == "__main__":
    main()
