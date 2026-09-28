# Project environment provisioning

Use Python 3.13 for this project. Run the following from the repository root on
Linux or macOS; dependency installation requires access to a Python package index.
Project execution does not require an external service account.

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip install -e .
.venv/bin/python -m pip check
```

Use the virtual environment's Python and tools for subsequent project commands.
For Windows, replace `.venv/bin/python` with `.venv\Scripts\python.exe`.
`pyproject.toml` declares the setuptools backend needed to build the local package,
including editable installs in a clean environment. The tested interpreter is
Python 3.13; the package metadata minimum is not a claim that newer versions have
been verified. Direct dependencies are pinned; transitive dependencies are not a
complete environment lock.

## Dependency scope

The environment includes NumPy, pandas, and scikit-learn for preprocessing and
model development; FastAPI, Pydantic, and Uvicorn for a JSON HTTP API; pytest and
httpx for model and synchronous TestClient tests; requests for real HTTP calls;
and flake8 for linting. Existing compatible versions are retained, with flake8
added. Basic Uvicorn serves the project without its optional `standard` extras.

No project imports use aequitas, Flask/Flask-Bootstrap, altair, matplotlib, seaborn,
jupyter, ipykernel, nbformat, httplib2, python-multipart, or pytest-asyncio. These
are omitted from the required environment: slice metrics use scikit-learn, the
API accepts JSON rather than forms, and synchronous API tests use TestClient.
Notebook infrastructure, if provided by a Workspace image, is separate from
project dependencies. Older learner instructions are being revised separately.

## Bundled files and Workspace boundary

Provision the full repository source tree, including `data/census.csv`,
`model_card_template.md`, `main.py`, and `starter/`, alongside the environment
files. These assets are already tracked; no dataset download, DVC remote, or
trained answer artifact is needed. Installing the Python package alone does not
copy the root-level dataset or template. Preserve the incomplete learner stubs.

This repository does not contain a Udacity Workspace image definition. The exact
externally managed image/launch configuration source has not been verified.
Apply these commands to the provided source tree; do not
assume editing requirements automatically rebuilds the Workspace image.

Verification should check imports, bundled file paths, and dependency consistency.
The unfinished training script and API are learner work, so environment smoke
checks do not establish that a completed submission passes its tests.
