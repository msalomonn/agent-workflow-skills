# Agent Workflow Skills

**Reusable skills for coding agents: define the work, resume with context, and verify what shipped.**

[Español](README.es.md) · [Installation](docs/installation.md) · [Try the demo](examples/cart/README.md) · [Validation](docs/validation.md) · [MIT License](LICENSE)

Agent Workflow Skills is a collection of 12 focused instructions for everyday software work. Each exported skill carries its own references and templates. Use one skill for a specific task, or combine them around your existing development process.

The toolkit keeps acceptance criteria, repository state, and verification connected. It helps an agent distinguish a completed implementation from a merged PR, a deployment, or an accepted delivery—and resume work without treating yesterday's checkpoint as today's truth.

## Start small

Requirements: Git and Python 3.9+ to prepare the package, and a coding agent that supports `SKILL.md` folders. The export tool uses only the Python standard library and makes no network requests. Your agent supplies its own tools and credentials.

```sh
git clone https://github.com/msalomonn/agent-workflow-skills.git
cd agent-workflow-skills
python3 scripts/export_skills.py --output dist/starter \
  --skill workflow-debug --skill workflow-verify --skill workflow-handoff
python3 scripts/export_skills.py --verify dist/starter
```

Copy the **complete exported skill folders** into your agent's project skill directory. For Codex, that directory is `.agents/skills/`. Check for existing folders before copying; retain any customizations. Follow the [installation guide](docs/installation.md) for a full package, existing installations, updates, and compatibility limits.

Then ask, for example:

```text
Use workflow-debug to reproduce and fix the failing total in this project.
Keep the change scoped to the bug and record before/after verification.
```

The [cart demo](examples/cart/README.md) provides a small local task with a real failing test. No account, API key, or hosted demo is needed for that exercise.

## Choose a skill

| Skill | Useful when you need to… |
| --- | --- |
| [workflow-spec](skills/workflow-spec/SKILL.md) | Define observable behavior and acceptance criteria. |
| [workflow-plan](skills/workflow-plan/SKILL.md) | Turn agreed scope into reviewable steps. |
| [workflow-execute](skills/workflow-execute/SKILL.md) | Implement or resume authorized work. |
| [workflow-debug](skills/workflow-debug/SKILL.md) | Reproduce a failure and test its cause. |
| [workflow-audit](skills/workflow-audit/SKILL.md) | Review a diff and report substantiated defects. |
| [workflow-verify](skills/workflow-verify/SKILL.md) | Check evidence before declaring completion. |
| [workflow-doctor](skills/workflow-doctor/SKILL.md) | Diagnose setup, missing tools, or integration access. |
| [workflow-triage](skills/workflow-triage/SKILL.md) | Classify requests and select the next action. |
| [workflow-research](skills/workflow-research/SKILL.md) | Investigate a technical decision with sources. |
| [workflow-github-status](skills/workflow-github-status/SKILL.md) | Reconcile issues, PRs, checks, and remaining work. |
| [workflow-handoff](skills/workflow-handoff/SKILL.md) | Save or resume a recoverable checkpoint. |
| [workflow-release](skills/workflow-release/SKILL.md) | Prepare or publish a release within project policy. |

A typical feature might use spec → plan → execute → audit → verify. A clear bug can start at debug. Handoff supports either flow. These are entry points, not a mandatory sequence.

## How it fits your project

- **Project conventions stay in the project.** No required branch names, tracker, cloud provider, or team structure.
- **Context survives a session.** Optional templates capture acceptance, decisions, observed revision, evidence, and the next action.
- **Skills remain independent.** Export all 12 or a selection; no dependency on another installed skill.
- **Tools remain yours.** GitHub-specific operations use an available connector or CLI. Other skills can work locally.
- **Permissions remain explicit.** Instructions do not grant credentials or replace the agent host's controls. Existing user authorization is reused.

This is an instruction toolkit, not an autonomous service, an enforcement system, or a model. Results depend on the agent, tools, repository, and task. Version 0.1.0 includes package integrity checks and evaluation scenarios; it does not claim a measured productivity improvement or universal client compatibility. See [validation and limits](docs/validation.md).

## Develop and contribute

```sh
python3 scripts/check_repository.py
```

Edit `skills/` and `workflow/`, then export again. Generated bundles belong in `dist/` and are not committed. The [contribution guide](CONTRIBUTING.md) explains how to propose a focused change and evaluate it.

Created and maintained by [Manuel Salomon](https://github.com/msalomonn). Free to use, modify, and share under the [MIT license](LICENSE).
