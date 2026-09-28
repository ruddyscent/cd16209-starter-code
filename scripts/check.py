"""Run the learner project's local test and lint gates."""

from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parent.parent
    for arguments in (("pytest",), ("flake8", "--extend-exclude", ".venv")):
        print(f"Running {' '.join(arguments)}", flush=True)
        result = subprocess.run(
            [sys.executable, "-m", *arguments], cwd=root, check=False
        )
        if result.returncode:
            print(f"{arguments[0]} failed (exit {result.returncode}).")
            return result.returncode
    print("Local tests and lint passed.", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
