# Submission contract

Workspace is the default submission path. GitHub and ZIP are optional
alternatives; every route must include the same required deliverables below.
Workspace and ZIP need no external account. Complete the learner implementation
first; the pristine starter is not a complete submission.

Use `python` in the preinstalled Workspace Python 3.13 `ml` environment. No learner
installation or new virtual environment is required there. Local developers and
reviewers can install and activate an isolated environment using ENVIRONMENT.md.

## Required layout

All paths below are relative to the project root. Only the optional ZIP route
uses a top-level `submission/` directory.

| Path | Required content |
| --- | --- |
| `README.md`, `ENVIRONMENT.md`, `SUBMISSION.md` | Project setup, inference instructions, and this contract |
| `requirements.txt`, `setup.py`, `pyproject.toml` | Dependencies and package configuration |
| `main.py` | Completed FastAPI application |
| `starter/**/*.py` | Completed training, preprocessing, and model source |
| `tests/**/*.py` | Completed model and API tests; retain at least three of each |
| `scripts/check.py`, `scripts/package_submission.py` | Local validation and packaging commands |
| `request.py` | Local HTTP request script using `requests` |
| `data/census.csv` | Bundled project data |
| `model/` | Trained model and every fitted preprocessing artifact required for inference |
| `model_card.md` | Completed model card |
| `slice_output.txt` | Model metrics by categorical slice |
| `evidence/validation.txt` | Command, pytest and flake8 output, and successful exit status |
| `evidence/http.txt` | GET and inference POST requests to the running local server, including status codes and response bodies |
| `evidence/openapi.json` | Exported API OpenAPI schema showing the request example and aliases |
| `submission_files.txt` | Explicit list of artifacts and additional supporting files |

The helper includes the named files above and Python files under `starter/` and
`tests/`. List every model/preprocessing file and any additional supporting module,
configuration, or test fixture in `submission_files.txt`, one project-relative
file path per line using `/`. Blank lines and lines beginning with `#` are ignored;
directories and globs are not supported. For example, if these are your artifact
names:

```text
model/model.pkl
model/encoder.pkl
model/lb.pkl
```

These names and the pickle format are examples, not requirements. A single file
may contain the model and fitted preprocessing together. The list must match the
files loaded by your API; document that mapping in README.md. Model artifacts are
included directly from disk even when Git ignores them. Add supporting files
explicitly; do not list unrelated files. No file list can establish that the model
or tests are correct, so review the contents as well as the paths.

## Validate and capture evidence

Run `python scripts/check.py` and save its output and exit status in
`evidence/validation.txt`. Only claim success after verifying exit status zero;
a redirection or logging command is not itself proof of a passing check. The
runner is local validation, not hosted CI/CD.

Start the completed API with `python -m uvicorn main:app --host 127.0.0.1 --port 8000`.
In another terminal run `python request.py`. Implement that script to
call GET `/` and your documented inference POST route at `http://127.0.0.1:8000`,
print status codes and response bodies, and exit nonzero on an unexpected result.
Save the output and commands in `evidence/http.txt`. TestClient results alone do
not establish that an HTTP server ran. Export the running API's `/openapi.json`
to `evidence/openapi.json`; ensure it includes your input example and field aliases.

## Choose the submission route

### Workspace (default)

Keep all required deliverables in the project root and use the Workspace
submission control. Review the submitted file selection or available preview,
including generated files under `model/` and `evidence/`; do not assume Git-ignored
files are included automatically. If the available submission flow cannot include
all files, use the optional ZIP upload route or ask course support. Save and
back up your work. Default-image and submission reset validation remain separate
maintenance tasks, not claims established by this document.

### GitHub (optional)

This route requires your own GitHub access and a repository accessible to the
reviewer. Include the same files and document the project root. Check the actual
tracked files: the default ignore rules omit trained artifacts. If necessary,
use `git add -f` only with the explicit artifact paths listed in
`submission_files.txt`, after reviewing each file. Do not add environments,
caches, credentials, or unrelated files. No particular Git history, protected
branch, hosted CI/CD, or public API endpoint is required.

### ZIP (optional)

From the project root, run:

```sh
python scripts/package_submission.py submission.zip
```

The helper requires a new output path and refuses to overwrite an existing file.
Its source root is determined by its own location; the output path is relative
to the current working directory. It uses an explicit file selection rather than
`git archive` or recursively zipping the project. It rejects symlinks, unsafe
paths, common credential filenames, and environment/cache directories. Review
all selected files for embedded credentials or unrelated/private content: the
helper does not inspect file contents for secrets. Stable ordering and timestamps
make repeated packaging reproducible for identical inputs and Python/zlib runtime.

## Check reproducibility

For ZIP, extract into a fresh directory and enter `submission/`. For Workspace
or GitHub, use a separate copy of the submitted project root. A reviewer can
install an isolated environment using `ENVIRONMENT.md`; this installation is
not a learner step in the preinstalled Workspace. Run the validation command, start Uvicorn, and run `request.py`
from this root. The API must load the submitted trained model and fitted
preprocessing using project-relative paths; it must not train, fit new encoders,
download assets, contact remote storage, or require the author's absolute path.
Document any extra local inference command in README.md. Confirm the extracted
copy works without the original checkout before submitting.

Packaging verifies selected paths and archive structure, not model quality,
evidence authenticity, safe deserialization, or successful inference. Full
trained-model inference verification is part of final project QA.
