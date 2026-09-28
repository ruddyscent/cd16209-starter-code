# Retired cloud deployment instructions

The former Heroku/DVC workflow is retired for this project. Do not add buildpacks,
remote-storage pulls, or startup cleanup code from earlier versions of this file.

Use the account-free local FastAPI workflow in [README.md](README.md), provision
its environment with [ENVIRONMENT.md](ENVIRONMENT.md), and submit the model and
fitted preprocessing artifacts in the ZIP defined by [SUBMISSION.md](SUBMISSION.md).
