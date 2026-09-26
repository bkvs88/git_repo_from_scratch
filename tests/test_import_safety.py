"""Guards against the two import-time defects that have broken this project.

1. `readdata.py` used to call `input()` at module scope, and every operation
   module imported it at import time. `import addition` therefore blocked on
   stdin and raised EOFError when there was no input.

2. A long-lived branch merged into main later resurrected a deleted
   `from readdata import a, b` line, which made `main` fail to import with
   `ImportError: cannot import name 'a' from 'readdata'`.

Both are invisible to unit tests that import modules casually, so they are
asserted here against a real subprocess with no stdin attached.
"""

import ast
import pathlib
import subprocess
import sys

import pytest

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
MODULES = [
    "addition",
    "substraction",
    "multiplication",
    "division",
    "power",
    "readdata",
]


def run_python(code):
    return subprocess.run(
        [sys.executable, "-c", code],
        cwd=REPO_ROOT,
        stdin=subprocess.DEVNULL,
        capture_output=True,
        text=True,
        timeout=30,
    )


@pytest.mark.parametrize("module", MODULES)
def test_module_imports_without_stdin(module):
    """Importing any module must not read from stdin."""
    result = run_python(f"import {module}")
    assert result.returncode == 0, (
        f"import {module} failed with no stdin:\n{result.stderr}"
    )


@pytest.mark.parametrize("module", MODULES)
def test_module_import_is_side_effect_free(module):
    """Importing a module must not print anything or hang waiting for input."""
    result = run_python(f"import {module}")
    assert result.stdout == "", f"import {module} printed: {result.stdout!r}"
    assert result.stderr == "", f"import {module} wrote to stderr: {result.stderr!r}"


def test_calculator_module_imports_without_stdin():
    """Importing calculator must not prompt; only running main() may."""
    result = run_python("import calculator")
    assert result.returncode == 0, result.stderr
    assert "Enter first number" not in result.stdout


def test_no_module_imports_names_from_readdata():
    """`readdata` exposes only `read_data`; nobody may import `a` or `b`.

    This is the precise check for the ImportError regression. It inspects the
    AST rather than grepping text, so it cannot be fooled by a name appearing
    inside a function body or a string.
    """
    readdata_names = set()
    for path in sorted(REPO_ROOT.glob("*.py")):
        tree = ast.parse(path.read_text(), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom) and node.module == "readdata":
                readdata_names.update(alias.name for alias in node.names)

    assert readdata_names <= {"read_data"}, (
        "only `read_data` may be imported from readdata, "
        f"but found: {sorted(readdata_names)}"
    )


def test_readdata_has_no_module_level_input_calls():
    """`input()` must live inside a function, never at module scope."""
    source = (REPO_ROOT / "readdata.py").read_text()
    tree = ast.parse(source)
    function_bodies = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            function_bodies.update(
                child
                for stmt in node.body
                for child in ast.walk(stmt)
            )

    module_level_calls = [
        node
        for node in tree.body
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call)
    ]
    for stmt in module_level_calls:
        assert stmt not in function_bodies, (
            "readdata.py must not execute calls at module scope"
        )

    assert not module_level_calls, (
        "readdata.py has module-level statements; prompts must be inside "
        "read_data()"
    )
