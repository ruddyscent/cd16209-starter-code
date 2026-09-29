# Project environment

## Default Udacity Workspace

The target Workspace provides Python 3.13 and all project dependencies in the
`ml` environment. Learners do not run pip or create a virtual environment. The
terminal's `python` and the editor must use `/opt/conda/envs/ml/bin/python`, with
`/workspace/cd16209-starter-code` as the project root. Run project commands with
`python`, including `python scripts/check.py` and `python -m uvicorn main:app`.

If that source or environment is missing, ask course support to provision the
updated image. A successful installation in one live session does not establish
that the default image has been updated. Image delivery belongs to #25 and reset
verification to #18; those checks remain pending until their evidence is recorded.

## Optional local development and reviewer setup

Use Python 3.13. From the supplied project's root on Linux or macOS:

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip install -e .
.venv/bin/python -m pip check
source .venv/bin/activate
```

After activation, use `python` for the project commands in README.md. On Windows,
create the environment with your Python 3.13 interpreter, use
`.venv\Scripts\python.exe` for installation, and activate with
`.venv\Scripts\Activate.ps1` in PowerShell. Installation may access a Python
package index; execution uses local data and artifacts. This is optional
local/reviewer provisioning, not a Workspace learner requirement.

`pyproject.toml` declares the setuptools backend for local/editable installation.
Python 3.13 is the tested interpreter; the metadata minimum does not establish
later-version compatibility. Direct dependencies are pinned in requirements.txt;
transitive dependencies are not a complete environment lock.

## Dependency scope

NumPy, pandas, and scikit-learn support model development; FastAPI, Pydantic, and
Uvicorn provide the JSON API; pytest and httpx support model and TestClient tests;
requests makes real HTTP calls; flake8 checks source. Basic Uvicorn does not need
its optional standard extras. No project imports require legacy aequitas/Flask,
plotting, notebook, multipart, or async-test packages. Workspace editor/notebook
infrastructure is separate from this project environment.

## Image maintainer handoff (#25)

Use [WORKSPACE_IMAGE_HANDOFF.md](WORKSPACE_IMAGE_HANDOFF.md) for the concrete
update plan for the existing image, selected starter SHA, and evidence return.

Provision the full starter tree at `/workspace/cd16209-starter-code`, including
`data/census.csv`, `model_card_template.md`, `main.py`, `starter/`, both scripts,
and README.md, ENVIRONMENT.md, and SUBMISSION.md. Installing the Python package
alone does not copy the root-level data or documentation. Do not include a
reference solution, learner tests, or trained answer artifacts.

The selected starter revision is
`7f29e1afa46af42507fc0cc8ac31879dcbf8c026`, containing the merged #23 support-file
lint fixes and #24 documentation changes. Record it in the image update evidence.
This is a source commit, not an image digest; image publication and reset
verification remain pending. The current maintainer
source is [ruddyscent/cd16209-starter-code](https://github.com/ruddyscent/cd16209-starter-code).
This is a maintainer input, not a required learner download. Confirm any separate
official Udacity starter link before substituting it; its availability is not
established by this repository document.

Configure terminal and editor Python as `/opt/conda/envs/ml/bin/python` and the
initial editor folder as `/workspace/cd16209-starter-code`. Install the following
exact direct dependencies from requirements.txt into that environment:

| Package | Version |
| --- | --- |
| fastapi | 0.117.1 |
| uvicorn | 0.36.0 |
| pydantic | 2.11.9 |
| numpy | 2.3.3 |
| pandas | 2.3.2 |
| scikit-learn | 1.7.2 |
| pytest | 8.4.2 |
| flake8 | 7.3.0 |
| httpx | 0.28.1 |
| requests | 2.32.5 |

During image construction, from the project root:

```sh
/opt/conda/envs/ml/bin/python -m pip install -r requirements.txt
/opt/conda/envs/ml/bin/python -m pip install -e .
/opt/conda/envs/ml/bin/python -m pip check
```

The observed external binding is the [Mocha Project Workspace atom](https://mocha.udacity.com/libraries/courses/cd16209/en-us/1.0/lessons/01616363-8ab9-407d-9898-38a8aebc41af/pages/d83ee412-606a-4e92-84c9-e0d6194cfe3f).
Earlier inspection found config `cd0582-vscode` and default path
`/?folder=/workspace/nd0821-c3-starter-code/`. These are historical observations,
not the desired new root. The underlying image recipe is managed externally;
changing this repository does not rebuild it.

After a real image reset, the maintainer should run from the intended root:

```sh
pwd
python --version
python -c "import sys; print(sys.executable)"
python -m pip check
python -m pytest --version
python -m flake8 --version
python -m uvicorn --version
python - <<'PY'
from pathlib import Path
import importlib
import importlib.metadata
import pandas as pd
for name in ('fastapi', 'uvicorn', 'pydantic', 'numpy', 'pandas', 'sklearn',
             'pytest', 'flake8', 'httpx', 'requests', 'starter.ml.data',
             'starter.ml.model'):
    importlib.import_module(name)
for line in Path('requirements.txt').read_text().splitlines():
    if '==' in line and not line.startswith('#'):
        name, version = line.strip().split('==')
        assert importlib.metadata.version(name) == version, name
for name in ('README.md', 'ENVIRONMENT.md', 'SUBMISSION.md', 'main.py',
             'model_card_template.md', 'data/census.csv', 'scripts/check.py',
             'scripts/package_submission.py', 'starter/train_model.py'):
    assert Path(name).is_file(), name
assert pd.read_csv('data/census.csv').shape == (32561, 15)
print('Imports, direct versions, bundled files and dataset shape passed.')
PY
```

Record reset source SHA, image identity, interpreter path, package versions,
commands, and results. Confirm the editor uses the same interpreter and root.
These smoke checks do not prove a complete learner solution or submission flow;
actual end-to-end reset and submission verification remains #18.

## Local quality validation

After completing the learner implementation and tests, run `python scripts/check.py`
from the project root. It uses the same interpreter for pytest and flake8, stops
on failure (including no tests), and prints success only after both pass.
The optional local `.venv` is excluded from linting, not unfinished source.
The pristine starter is intentionally incomplete and is not expected to pass.
`sanitycheck.py` remains optional interactive heuristic guidance, not a gate.
This is automated local quality validation, not hosted CI/CD or cloud deployment.
