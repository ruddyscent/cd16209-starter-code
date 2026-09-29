# CD16209 Workspace image maintainer handoff — issue #25

## Ownership and requested outcome

The Workspace image maintainer owns updating the current image, publishing a
new version, and confirming its association with CD16209. Modify the existing
image rather than building an unrelated replacement from scratch. This handoff does not modify an image or claim publication.
Learners should open the preinstalled Workspace and work with `python` without
running pip, creating a venv, cloning source, or using an external account.

#18 owns actual reset survival, terminal/editor verification, complete learner
and reviewer execution, and artifact delivery through Workspace, GitHub, and ZIP
submission routes. A successful build or an existing live session does not prove
those outcomes. The current #18 acceptance items remain unchecked.

## Record the existing image before updating

Record the current image identifier/version, project binding `cd0582-vscode`,
interpreter configuration, and startup folder. Preserve platform integration
and unrelated image tooling. Use the normal update process with a recoverable
previous version; do not blindly delete folders, environments, or packages.
Inspect identified QA residue and stale project files before targeted cleanup.

## Exact source and target layout

- Source: https://github.com/ruddyscent/cd16209-starter-code
- Selected merged commit: `7f29e1afa46af42507fc0cc8ac31879dcbf8c026`.
- Project root: `/workspace/cd16209-starter-code`.
- Python: 3.13, environment `ml`.
- Terminal and editor interpreter: `/opt/conda/envs/ml/bin/python`.
- Initial editor folder: `/workspace/cd16209-starter-code`.

Ancestry checks confirm the selected commit includes #23's support-file lint
commit `bb8e906978f0f60f4ed22c3f3c6c89c35c659385` and #24's documentation commit
`a9307c68b0578e8a45a935fa03ce2154054319c2`. This supplies the exact source revision
that ENVIRONMENT.md previously deferred until #24 publication.

The learner starter SHA is fixed. The commit/PR publishing this handoff is
separate documentation provenance, not a replacement starter SHA; the image
requirement is not self-referential.

Update the bundled source to this exact tracked revision using the normal
existing-image update process, not a copied developer workspace. Account for
existing files and preserve unrelated platform content. Preserve the full source tree,
requirements/package metadata, data/census.csv, model_card_template.md and docs.
Record the SHA in build metadata even if the deployed tree omits `.git`.
A separate official Udacity starter lookup has not been resolved; do not replace
this source with an assumed equivalent or legacy checkout without verification.

## Required direct dependencies

Install requirements.txt as supplied; no learner installation step is needed.

| Package | Exact version |
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

Within the existing image, update its current ml environment after placing
the selected source at its final root. Do not create a learner venv:

```sh
cd /workspace/cd16209-starter-code
/opt/conda/envs/ml/bin/python -m pip install -r requirements.txt
/opt/conda/envs/ml/bin/python -m pip install -e .
/opt/conda/envs/ml/bin/python -m pip check
/opt/conda/envs/ml/bin/python -m pip freeze
```

Package downloads are allowed during provisioning. Record resolved transitive
versions too: direct pins are not a full environment lock. Configure terminal
activation/PATH and the editor's Python selection to the same interpreter through
the image's normal configuration mechanism. Confirm that `python` resolves there;
do not rely on an interactive manual activation that disappears after reset.

## Keep the image a starter

Inspect the final image tree, not only the repository. Exclude reference solutions,
trained answer models, QA scripts/results, temporary files, partial virtual
environments, and developer credentials. Do not copy `/tmp/issue18-*`, reviewer
copies, or locally created `.venv` directories into the image.

Source inspection performed for the selected commit: all 25 tracked paths were
listed; model/ and screenshots/ contain only .gitkeep; no tracked learner test
suite, request.py solution, serialized model, QA directory, or venv exists.
main.py is an API placeholder, train_model/inference retain pass stubs, and
starter/train_model.py still contains learner TODOs. This is tracked-source and
specific-stub inspection, not a full image filesystem or secret-content audit.

Census data SHA256:
`9e7ddeec23b4b1304f138cee41d8a309e987cdf6dc1632033f73dfe28fff814b`.
The source contains 32,561 rows and 15 columns as previously smoke-tested; the
reset check below verifies the bundled image copy again.

## Updated-image smoke and reset handoff commands

Run these when validating the image update and have #18 repeat them after a real reset:

```sh
cd /workspace/cd16209-starter-code
pwd
python --version
python -c "import sys; print(sys.executable); assert sys.version_info[:2] == (3, 13); assert sys.executable == '/opt/conda/envs/ml/bin/python'"
python -m pip check
python -m pytest --version
python -m flake8 --version
python -m uvicorn --version
python -m flake8 sanitycheck.py starter/ml/data.py starter/__init__.py starter/ml/__init__.py
python - <<'PY'
from pathlib import Path
import hashlib
import importlib
import importlib.metadata
import pandas as pd
assert Path.cwd() == Path('/workspace/cd16209-starter-code')
for name in ('fastapi', 'uvicorn', 'pydantic', 'numpy', 'pandas', 'sklearn',
             'pytest', 'flake8', 'httpx', 'requests', 'starter.ml.data',
             'starter.ml.model'):
    importlib.import_module(name)
for line in Path('requirements.txt').read_text().splitlines():
    if '==' in line and not line.startswith('#'):
        name, expected = line.strip().split('==')
        actual = importlib.metadata.version(name)
        assert actual == expected, (name, actual, expected)
        print(name, actual)
for name in ('README.md', 'ENVIRONMENT.md', 'SUBMISSION.md', 'main.py',
             'model_card_template.md', 'data/census.csv', 'scripts/check.py',
             'scripts/package_submission.py', 'starter/train_model.py'):
    assert Path(name).is_file(), name
assert pd.read_csv('data/census.csv').shape == (32561, 15)
assert hashlib.sha256(Path('data/census.csv').read_bytes()).hexdigest() == (
    '9e7ddeec23b4b1304f138cee41d8a309e987cdf6dc1632033f73dfe28fff814b')
print('Imports, direct versions, bundled paths and Census data passed.')
PY
```

Do not run unfinished training as an image smoke check. The completed-project
quality gate intentionally does not pass on the pristine starter: no learner
tests exist and exercise placeholders remain. Support-file lint can be verified
separately as above without weakening or suppressing the learner checks.

At runtime, completed solutions should use only local artifacts and local HTTP
services. Swagger UI may request CDN assets; exported OpenAPI evidence is an
accepted way to inspect request examples without treating CDN availability as a
model-serving requirement. Stronger network-isolation and complete runtime tests
belong to #18; build smoke alone does not demonstrate them.

If filesystem write stalls recur, capture affected path, operation, timing,
filesystem state and logs before retrying or attributing the failure. Do not label
a stall as dependency incompatibility without supporting evidence.

## Publish, associate, and return evidence

Save and publish a new version of the existing image through the normal process.
Confirm the project points to that updated version while preserving platform
integration. Relevant authoring location:
https://mocha.udacity.com/libraries/courses/cd16209/en-us/1.0/lessons/01616363-8ab9-407d-9898-38a8aebc41af/pages/d83ee412-606a-4e92-84c9-e0d6194cfe3f

The last saved Workspace configuration used cd0582-vscode with the startup path
`/?folder=/workspace/cd16209-starter-code/`. That configuration is not proof of
updated image contents or reset behavior. Return:

```text
Existing image identifier/version before update:
Updated version/digest of that image:
Published timestamp:
CD16209 association/config identifier and saved-state evidence:
Starter SHA: 7f29e1afa46af42507fc0cc8ac31879dcbf8c026
Source provenance/update method:
Handoff documentation commit/PR (separate from starter SHA):
Default project root:
Terminal Python path/version:
Editor Python path/version:
Direct versions and full pip freeze attachment:
Provisioning commands, exit statuses, pip check/import/smoke logs:
Final-image inspection for answers/artifacts/QA envs:
Filesystem stall observations or none observed:
Known limitations:
Ready for #18 reset verification (yes/no):
```

All four issue #25 acceptance items remain open until the maintainer supplies evidence of installed
packages, configured terminal/editor/root/data, a clean starter image, and its
published project association. No image build, publish, reset, or external post
was performed while preparing this handoff. Existing local checks and historical
live-Workspace package verification establish feasibility only; they do not
replace checks on the newly published image.
