# Python 3.13 environment

Python 3.13 is the supported, tested interpreter for this project. The default
Workspace uses its preinstalled `ml` environment; learners do not install packages
or create a virtual environment. Optional local/reviewer setup uses the pinned
requirements and commands in [ENVIRONMENT.md](ENVIRONMENT.md). The metadata minimum
Python version does not establish compatibility with later interpreters.

The supplied preprocessing in `starter/ml/data.py` uses
`OneHotEncoder(sparse_output=False, handle_unknown="ignore")`, matching the
pinned scikit-learn API. The learner still implements training, inference, and
the FastAPI application; environment compatibility is not proof of a completed
project or passing learner tests.

[README.md](README.md) describes the local workflow, and
[SUBMISSION.md](SUBMISSION.md) defines required deliverables for every submission route. No separate
notebook, cloud, or DVC dependency installation is required by that workflow.
