# Python 3.13 environment

Python 3.13 is the supported, tested interpreter for this project. Install the
pinned dependencies from `requirements.txt` and the local package using the
commands in [ENVIRONMENT.md](ENVIRONMENT.md). The package metadata's minimum
Python version does not establish compatibility with later interpreters.

The supplied preprocessing in `starter/ml/data.py` uses
`OneHotEncoder(sparse_output=False, handle_unknown="ignore")`, matching the
pinned scikit-learn API. The learner still implements training, inference, and
the FastAPI application; environment compatibility is not proof of a completed
project or passing learner tests.

[README.md](README.md) describes the local workflow, and
[SUBMISSION.md](SUBMISSION.md) defines the required ZIP contents. No separate
notebook, cloud, or DVC dependency installation is required by that workflow.
