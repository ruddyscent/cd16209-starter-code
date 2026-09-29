# Retired cloud deployment instructions

The former Heroku/DVC workflow is retired for this project. Do not add buildpacks,
remote-storage pulls, or startup cleanup code from earlier versions of this file.

Use the preinstalled Workspace workflow in [README.md](README.md).
[ENVIRONMENT.md](ENVIRONMENT.md) separates image provisioning from optional
local/reviewer setup. [SUBMISSION.md](SUBMISSION.md) defines the required model,
fitted preprocessing, and other deliverables for Workspace submission (default)
and optional GitHub or ZIP alternatives.
