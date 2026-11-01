# Public publishing checks

Run `python scripts/install_hooks.py` after cloning to enable this checkout's pre-commit and pre-push audits. Git does not install hooks automatically when cloning. CI runs the same tree audit.

Pre-commit audits the complete staged Git tree, including staged content that differs from working files. Pre-push audits every outgoing commit, including a new branch's history; deleting a private file in a later commit does not make its earlier publication safe. A failed audit stops the commit or push and names the blocked path/category without printing the secret value.

The policy accepts only the catalogue, referenced creature/diagram artwork, provenance, named documentation, exporter/audit code and CI/hooks. It rejects unrelated paths, catch/location/credential fields, common credential patterns, local user paths, symlinks/submodules and external-content SVGs.

These checks cannot determine whether an otherwise valid illustration depicts something private or whether every factual change is relevant. Review changed artwork and catalogue text before committing. Keep private notes, catches and backups outside this repository. Do not bypass failing hooks; fix the staged/outgoing content first.
