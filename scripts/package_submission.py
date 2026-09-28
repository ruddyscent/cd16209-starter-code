"""Package an explicit set of learner submission files using only stdlib."""

import argparse
from pathlib import Path, PurePosixPath
import sys
import zipfile


REQUIRED = (
    "README.md", "ENVIRONMENT.md", "SUBMISSION.md", "main.py", "request.py",
    "requirements.txt", "setup.py", "pyproject.toml", "data/census.csv",
    "model_card.md", "slice_output.txt", "scripts/check.py",
    "scripts/package_submission.py", "submission_files.txt",
    "evidence/validation.txt", "evidence/http.txt", "evidence/openapi.json",
)
BLOCKED_PARTS = {
    ".git", ".venv", "venv", "env", "__pycache__", ".pytest_cache",
    ".mypy_cache", ".ruff_cache", ".tox", ".nox", ".cache", ".aws", ".ssh",
    ".azure", ".config", "node_modules", "credentials", "secrets",
}


def checked_file(root, name):
    """Reject unsafe archive names, sensitive paths, and symbolic links."""
    relative = PurePosixPath(name)
    if (not name or "\\" in name or ":" in name or relative.is_absolute()
            or relative.as_posix() != name
            or any(part in (".", "..") for part in relative.parts)):
        raise ValueError(f"Invalid relative file path: {name!r}")
    for part in relative.parts:
        lower = part.lower()
        if (lower in BLOCKED_PARTS or lower.startswith(".env")
                or lower.startswith("credentials.")
                or lower.startswith("secrets.")
                or lower in ("id_rsa", "id_ed25519", ".netrc", ".pypirc")
                or lower.endswith((".pem", ".key", ".pyc", ".pyo"))):
            raise ValueError(f"Excluded path: {name}")
    path = root
    for part in relative.parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f"Symbolic links are not allowed: {name}")
    if not path.is_file():
        raise ValueError(f"Required file is missing or not a file: {name}")
    return path


def selected_files(root):
    manifest = checked_file(root, "submission_files.txt")
    names = set(REQUIRED)
    for line in manifest.read_text(encoding="utf-8").splitlines():
        name = line.strip()
        if name and not name.startswith("#"):
            names.add(name)
    # Include only Python source, never every file under these directories.
    for directory in ("starter", "tests"):
        base = root / directory
        if base.is_symlink():
            raise ValueError(f"Symbolic links are not allowed: {directory}")
        for path in base.rglob("*.py"):
            names.add(path.relative_to(root).as_posix())
    if not any(name.startswith("tests/") and name.endswith(".py")
               for name in names):
        raise ValueError("Include completed learner tests under tests/.")
    if not any(name.startswith("model/") for name in names):
        raise ValueError("List trained inference artifacts under model/.")
    names.update(("starter/__init__.py", "starter/ml/__init__.py",
                  "starter/ml/data.py", "starter/ml/model.py",
                  "starter/train_model.py"))
    return [(name, checked_file(root, name)) for name in sorted(names)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "output", help="New ZIP path relative to your current directory"
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    output = Path(args.output)
    try:
        files = selected_files(root)
        # Exclusive creation preserves existing submissions and other files.
        stream = output.open("xb")
        try:
            with stream, zipfile.ZipFile(stream, "w") as archive:
                for name, path in files:
                    info = zipfile.ZipInfo(f"submission/{name}")
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, path.read_bytes())
        except Exception:
            output.unlink()
            raise
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Packaging failed: {error}", file=sys.stderr)
        return 1
    print(f"Created {output} with {len(files)} files under submission/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
