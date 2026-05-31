"""env_checker.py — sanity-check the rag-reference environment.

Verifies two things, both read dynamically from the project's own files:
  1. Every variable declared in .env.example is present and filled in (not a
     placeholder) in your local .env.
  2. Every package declared in pyproject.toml is installed in the current venv.

Nothing is hardcoded: add a key to .env.example or a dependency to
pyproject.toml and it is picked up automatically.

Usage:
    uv run python env_checker.py          # prints a report, exits non-zero on failure

Or from a notebook:
    from env_checker import run_checks
    run_checks()                          # prints report, returns True/False

This module has no hard dependencies: it uses python-dotenv when installed but
falls back to a tiny built-in parser, so it works on a fresh venv.
"""

from __future__ import annotations

import importlib.metadata
import importlib.util
import re
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

# ── Sources of truth ─────────────────────────────────────────────────────────

ROOT = Path(__file__).parent
ENV_PATH = ROOT / ".env"
ENV_TEMPLATE_PATH = ROOT / ".env.example"
PYPROJECT_PATH = ROOT / "pyproject.toml"

_OK, _FAIL = "✓", "✗"


@dataclass
class CheckResult:
    ok: bool
    label: str
    detail: str = ""

    def render(self) -> str:
        mark = _OK if self.ok else _FAIL
        line = f"  {mark} {self.label}"
        return f"{line}  — {self.detail}" if self.detail else line


# ── .env parsing ─────────────────────────────────────────────────────────────

def _parse_env_file(path: Path) -> dict[str, str]:
    """Return KEY=VALUE pairs from an env file (uses python-dotenv if present)."""
    if not path.exists():
        return {}

    if importlib.util.find_spec("dotenv") is not None:
        from dotenv import dotenv_values

        return {k: v for k, v in dotenv_values(path).items() if v is not None}

    values: dict[str, str] = {}
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        values[key.strip()] = val.strip().strip('"').strip("'")
    return values


def required_env_keys() -> list[str]:
    """Keys the project expects, taken from .env.example (or .env as a fallback)."""
    source = ENV_TEMPLATE_PATH if ENV_TEMPLATE_PATH.exists() else ENV_PATH
    return list(_parse_env_file(source).keys())


# ── pyproject parsing ────────────────────────────────────────────────────────

# Grab the distribution name at the start of a requirement string, e.g.
# "langchain-openai>=1.0; python_version>='3.10'" -> "langchain-openai".
_REQ_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*")


def required_packages() -> list[str]:
    """Distribution names from pyproject.toml: project deps + all dependency groups."""
    if not PYPROJECT_PATH.exists():
        return []

    data = tomllib.loads(PYPROJECT_PATH.read_text())
    requirements: list[str] = list(data.get("project", {}).get("dependencies", []))
    for group_deps in data.get("dependency-groups", {}).values():
        # entries may be strings or {include-group: ...} tables; keep the strings
        requirements += [d for d in group_deps if isinstance(d, str)]

    names: list[str] = []
    for req in requirements:
        match = _REQ_NAME.match(req.strip())
        if match and match.group() not in names:
            names.append(match.group())
    return names


# ── Checks ───────────────────────────────────────────────────────────────────

def _is_placeholder(value: str) -> bool:
    """Heuristic for an unfilled value: empty or ends with the template '...'."""
    return value == "" or value.endswith("...")


def check_env_vars() -> list[CheckResult]:
    keys = required_env_keys()
    if not keys:
        return [CheckResult(False, "env template", f"no keys found (looked in {ENV_TEMPLATE_PATH.name}/{ENV_PATH.name})")]

    if not ENV_PATH.exists():
        return [CheckResult(False, ".env file", f"not found at {ENV_PATH}")]

    values = _parse_env_file(ENV_PATH)
    results: list[CheckResult] = []
    for key in keys:
        value = values.get(key)
        if value is None:
            results.append(CheckResult(False, key, "missing from .env"))
        elif _is_placeholder(value):
            results.append(CheckResult(False, key, "still a placeholder — not filled in"))
        else:
            results.append(CheckResult(True, key, "set"))
    return results


def check_packages() -> list[CheckResult]:
    names = required_packages()
    if not names:
        return [CheckResult(False, "pyproject.toml", "no dependencies found")]

    results: list[CheckResult] = []
    for name in names:
        try:
            version = importlib.metadata.version(name)  # normalizes name per PEP 503
            results.append(CheckResult(True, name, f"installed ({version})"))
        except importlib.metadata.PackageNotFoundError:
            results.append(CheckResult(False, name, f"missing — run: uv add {name}"))
    return results


# ── Report ───────────────────────────────────────────────────────────────────

def run_checks() -> bool:
    """Run all checks, print a report, and return True if everything passed."""
    env_results = check_env_vars()
    pkg_results = check_packages()

    print(f"Environment variables (from {ENV_TEMPLATE_PATH.name})")
    for r in env_results:
        print(r.render())

    print(f"\nRequired packages (from {PYPROJECT_PATH.name})")
    for r in pkg_results:
        print(r.render())

    all_results = (*env_results, *pkg_results)
    all_ok = all(r.ok for r in all_results)

    print()
    if all_ok:
        print(f"{_OK} All checks passed.")
    else:
        failed = sum(not r.ok for r in all_results)
        print(f"{_FAIL} {failed} check(s) failed — see above.")

    return all_ok


def main() -> int:
    return 0 if run_checks() else 1


if __name__ == "__main__":
    sys.exit(main())
