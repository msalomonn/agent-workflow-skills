# Installation and updates

The repository contains skill **sources**. Export them first: the exporter rewrites shared-reference paths and includes the referenced files and license inside each skill. Copying only a source `SKILL.md` is incomplete.

## Export

You can also download the pre-exported ZIP from [release v0.1.1](https://github.com/msalomonn/agent-workflow-skills/releases/tag/v0.1.1). Extract it into a new directory: it contains the complete skill folders and integrity manifest. The source checkout is needed only if you want to regenerate the bundle or run the verifier. A SHA-256 checksum file accompanies the ZIP.

From the repository root, with Python 3.9+:

```sh
python3 scripts/export_skills.py --list
python3 scripts/export_skills.py --output dist/all
python3 scripts/export_skills.py --verify dist/all
```

Select only what you need by repeating `--skill`:

```sh
python3 scripts/export_skills.py --output dist/review \
  --skill workflow-audit --skill workflow-verify
```

The output directory must not already exist, even if empty. The exporter stages and checks the package before reserving the destination. It rejects symbolic links and missing resources. An interrupted final copy can leave a partial destination; the command reports failure, and manifest verification must pass before use. Retry into a new directory.

## Install in a project

For Codex, copy each complete exported `workflow-*` folder into `.agents/skills/` in the target project. This project directory is documented in the [official OpenAI CLI skill installation guide](https://developers.openai.com/api/reference/cli). Skills contain instructions and optional resources, as described in the [official skills documentation](https://developers.openai.com/plugins/concepts/skills). Documentation checked on 2026-11-18.

Example for a new folder, from the toolkit checkout; replace `/path/to/your-project` with the actual destination:

```sh
mkdir -p /path/to/your-project/.agents/skills
```

Before copying, inspect that directory. If `workflow-audit` is absent, copy the complete `dist/review/workflow-audit` directory there. If it already exists, compare versions and preserve local edits instead of overwriting it. Repeat for the other selected skills.

Start a new agent session in the target project and verify it discovers the skill. Ask it to use the named skill on a small local task such as the [cart demo](../examples/cart/README.md). If discovery differs in your client, consult that client's current documentation; packaging checks do not prove UI discovery.

For another agent supporting `SKILL.md`, use its documented skill directory and invocation method. The instructions avoid hardcoded tool names, but each client's discovery, instruction handling, and tools require their own verification. No other client is claimed as end-to-end tested in this release.

## Runtime requirements

The current skills are Markdown instructions and templates; they do not execute bundled hooks or background services. The host provides the model and tools. Python is needed for exporting and checking the package, and for the optional demo. GitHub operations need an authenticated connector or CLI with the relevant access; local workflows do not.

Do not copy the toolkit's source `workflow/` into the target project as a second task board. Installed references already include optional templates. Place actual task records in locations appropriate to the project's existing conventions.

## Verify, update, and remove

The bundle includes `workflow-manifest.json` with file hashes. `--verify` detects changed, missing, or extra files in the **export bundle**. It is an integrity check, not a signature or proof that the instructions will produce correct behavior. Keep the manifest with the export; it need not be put into the agent's skill directory.

To update, export to a new directory, compare against the installed folders, and carry forward intentional local changes. Replace only the selected folders after review. To remove, delete only the installed `workflow-*` folders you selected, preserving any customized resources you still need. Neither action needs a global agent configuration change.
