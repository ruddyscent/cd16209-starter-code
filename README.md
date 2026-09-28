# Building and Serving an ML Model with FastAPI

Train and evaluate a Census income classifier, examine its performance across
categorical data slices, test the model and API, and serve real predictions with
FastAPI. Complete this project in a Udacity Workspace or equivalent local Python
environment. The data and model-card template are bundled; no third-party service
account, hosted runtime, remote repository, or public URL is required. Package
installation during setup requires access to a Python package index. Local Git
is optional.

## 1. Set up the environment

Open a terminal in the project root: the directory containing `requirements.txt`,
`setup.py`, `main.py`, and `data/census.csv`. Keep all commands below in this root.
`starter/` is the Python package; for example, preprocessing lives at
`starter.ml.data`.

Use Python 3.13. On Linux or macOS:

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pip install -e .
.venv/bin/python -m pip check
```

On Windows use a Python 3.13 interpreter to create the environment and replace
`.venv/bin/python` with `.venv\Scripts\python.exe` in subsequent commands.
[ENVIRONMENT.md](ENVIRONMENT.md) describes the dependency and provisioning scope.
Use the pinned requirements, including pytest and flake8, rather than installing
an unrelated set of latest packages.

## 2. Complete the model and evaluation

The starter is intentionally unfinished. Complete `starter/train_model.py` and
the functions in `starter/ml/model.py`; use the provided preprocessing in
`starter/ml/data.py` and add your own supporting code as needed.

- Inspect `data/census.csv` and clean incidental whitespace in headers and values.
  Preserve the feature names, including their hyphens, and the meaning of values.
- Split data for training and evaluation (or use appropriate cross-validation).
  Fit preprocessing on training data only; transform held-out data with those
  fitted objects to avoid leakage.
- Train a classifier and report precision, recall, and F1 on held-out data.
- Choose at least one categorical feature and report precision, recall, and F1
  for each distinct value in the evaluation data. Write these slice results to
  `slice_output.txt`, identifying the feature and value for each slice.
- Save the trained model and all fitted preprocessing objects needed for inference
  under `model/`. A combined artifact or separate files are both acceptable.
  Document their filenames and loading procedure in your submitted README.
- Complete `model_card.md` using the bundled `model_card_template.md`, including
  the model's intended use, evaluation results, and limitations.

After implementing the training path, run:

```sh
.venv/bin/python -m starter.train_model
```

Training must produce the artifacts used by the API. Inference must load these
artifacts without retraining or fitting new preprocessing. Include the artifacts
in the final ZIP even if Git ignores them.

## 3. Complete the API and tests

Implement the FastAPI application named `app` in `main.py`:

- GET `/` returns a welcome message.
- A separate POST route accepts features and returns a real model prediction.
  Choose and document the route and response format.
- Use type hints and a Pydantic request model with an example. Use field aliases
  for hyphenated Census names rather than renaming those features in the dataset.
- Load the saved model and fitted preprocessing using paths relative to the
  project, without remote storage or absolute paths from your own machine.

Write completed tests under `tests/`: unit tests covering at least three
model-related functions, and at least three API tests. The API tests must check
GET status/body and separate POST cases for each prediction class. Both POST
tests must exercise the actual trained model and preprocessing, not a mocked or
hard-coded prediction. Check response status and prediction content.

Run the local quality gate:

```sh
.venv/bin/python scripts/check.py
```

It runs pytest and then flake8, stopping on failure (including no tests). Fix
failures in your implementation; do not weaken tests or exclude unfinished code
to obtain a pass. The pristine starter is not expected to pass. This is local
automated quality validation, not hosted CI/CD or automatic cloud deployment.
`sanitycheck.py` is an optional interactive, heuristic advisory tool and is not
part of this gate.

## 4. Run and query the local API

After training and implementing the API, start the server:

```sh
.venv/bin/python -m uvicorn main:app --host 127.0.0.1 --port 8000
```

Leave it running. In a second terminal at the same project root, run the
`request.py` script you implement:

```sh
.venv/bin/python request.py
```

Use `requests` in that script and implement a `--base-url` argument defaulting
to `http://127.0.0.1:8000`. For example, the following invocation must use the
specified server: `.venv/bin/python request.py --base-url http://127.0.0.1:8000`.
Call GET `/` and your inference POST route with valid input,
print each HTTP status and response body (including the inference result), and
exit nonzero on an unexpected result. Use a timeout so a failed server does not
leave the script waiting indefinitely. This script must call the running server;
TestClient tests alone do not demonstrate real HTTP execution.

The API's local `/docs` page can help inspect the request model. Export its
`/openapi.json` schema and verify that your input example and aliases appear.

## 5. Capture evidence and submit

Follow [SUBMISSION.md](SUBMISSION.md), the canonical archive manifest. Create:

- `evidence/validation.txt`: validation command, pytest/flake8 output, and exit
  status zero; check the actual status before recording success.
- `evidence/http.txt`: local GET and POST commands, HTTP status codes, and bodies.
- `evidence/openapi.json`: the exported schema with request example and aliases.
- `submission_files.txt`: explicit project-relative paths for every model and
  preprocessing artifact and any additional supporting files not auto-included.

After completing every required file and reviewing the selected contents, run:

```sh
.venv/bin/python scripts/package_submission.py submission.zip
```

The helper includes ignored artifacts listed in `submission_files.txt` and refuses
to overwrite an existing ZIP; choose a new filename for a revised submission.
Review the archive for unrelated files or embedded credentials.

Extract into a fresh directory and enter its `submission/` root. Install the
environment there, run `scripts/check.py`, start Uvicorn, and run `request.py`.
Verify inference loads the submitted artifacts without running training and
without accessing the original checkout. Submit that self-contained ZIP.
