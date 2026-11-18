# Contributing

Start with a concrete task the skill handles poorly or an observable packaging problem. Explain the current result, desired result, and a small reproduction. Use sanitized examples and never attach credentials or private project material.

## Changes

- Skill sources live in `skills/<name>/SKILL.md`. Names start with `workflow-` to reduce collisions.
- Use a short activation description. This repository encodes descriptions as JSON-quoted YAML strings so its standard-library checker can validate the constrained frontmatter format.
- Shared procedures and templates live in `workflow/`. Link them from the skill with relative Markdown links. Keep essential instructions short and load supporting detail only when useful.
- Put skill-specific helpers in `scripts/`, templates in `assets/`, references in `references/`, or client metadata in `agents/`. `references/workflow/` is reserved for generated shared resources.
- Preserve the user's scope, repository conventions, valid prior decisions, and host permissions. A new template should support missing context rather than force a new ceremony.

Run:

```sh
python3 scripts/check_repository.py
```

For behavioral changes, run the relevant scenario from [the evaluation guide](docs/evaluations.md) in an isolated project and report the agent/client, inputs, observed result, and limits. Do not describe a static check as an agent evaluation. Fix demonstrated failures with targeted instructions rather than expanding every skill.

Open a pull request explaining the problem, resulting behavior, and verification. Avoid committing generated `dist/` bundles or private session histories. New dependencies and automatic external actions need a clear reason.

Contributions are distributed under the repository's [MIT license](LICENSE). Submit only material you can share under that license and preserve any required third-party notices.
