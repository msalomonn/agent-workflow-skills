# Agent Workflow Skills

**Reusable skills for coding agents: define the work, resume with context, and verify what shipped.**

[Español](README.es.md) · [Download v0.1.1](https://github.com/msalomonn/agent-workflow-skills/releases/tag/v0.1.1) · [Installation](docs/installation.md) · [Usage examples](#usage-examples) · [Try the demo](examples/cart/README.md) · [Validation](docs/validation.md) · [MIT License](LICENSE)

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

| Skill | Useful when you need to… | Example |
| --- | --- | --- |
| [workflow-spec](skills/workflow-spec/SKILL.md) | Define observable behavior and acceptance criteria. | [View example](#workflow-spec) |
| [workflow-plan](skills/workflow-plan/SKILL.md) | Turn agreed scope into reviewable steps. | [View example](#workflow-plan) |
| [workflow-execute](skills/workflow-execute/SKILL.md) | Implement or resume authorized work. | [View example](#workflow-execute) |
| [workflow-debug](skills/workflow-debug/SKILL.md) | Reproduce a failure and test its cause. | [View example](#workflow-debug) |
| [workflow-audit](skills/workflow-audit/SKILL.md) | Review a diff and report substantiated defects. | [View example](#workflow-audit) |
| [workflow-verify](skills/workflow-verify/SKILL.md) | Check evidence before declaring completion. | [View example](#workflow-verify) |
| [workflow-doctor](skills/workflow-doctor/SKILL.md) | Diagnose setup, missing tools, or integration access. | [View example](#workflow-doctor) |
| [workflow-triage](skills/workflow-triage/SKILL.md) | Classify requests and select the next action. | [View example](#workflow-triage) |
| [workflow-research](skills/workflow-research/SKILL.md) | Investigate a technical decision with sources. | [View example](#workflow-research) |
| [workflow-github-status](skills/workflow-github-status/SKILL.md) | Reconcile issues, PRs, checks, and remaining work. | [View example](#workflow-github-status) |
| [workflow-handoff](skills/workflow-handoff/SKILL.md) | Save or resume a recoverable checkpoint. | [View example](#workflow-handoff) |
| [workflow-release](skills/workflow-release/SKILL.md) | Prepare or publish a release within project policy. | [View example](#workflow-release) |

A typical feature might use spec → plan → execute → audit → verify. A clear bug can start at debug. Handoff supports either flow. These are entry points, not a mandatory sequence.

## Usage examples

Install each named skill before using its example; the starter command above installs only debug, verify, and handoff. The [installation guide](docs/installation.md) explains exporting the full collection or a selection. Paste the prompts into your coding agent, replacing illustrative filenames, versions, and repository names with your project's actual context.

A useful request identifies the outcome, relevant files or issue, constraints, and whether you want analysis or implementation. Add available tests, logs, or acceptance criteria. The outputs below describe the intended deliverable; its detail depends on the task and available tools.

### workflow-spec

Use it when a request needs clearer behavior before implementation. Supply the current behavior, user need, constraints, and any existing specification. It examines the implementation to avoid specifying work that is already done.

```text
Use workflow-spec to define retries for failed CSV imports.
Inspect importer.py and the existing requirements. A failed import can leave
some rows saved; we have not decided whether retries skip or replace them.
Define acceptance criteria and failure cases, and identify that decision.
Write the proposal in docs/import-retries.md; do not implement it yet.
```

**Expected result:** observable behavior, testable acceptance criteria, exclusions, dependencies, and unresolved decisions. If one decision blocks only part of the work, the specification identifies that boundary.

### workflow-plan

Use it to turn agreed scope into implementation steps or update an existing plan. Supply the acceptance criteria and current plan, if one exists. The skill checks actual progress before scheduling more work.

```text
Use workflow-plan with docs/import-retries.md and docs/plan.md.
The CSV reader may already be implemented; verify that in the repository.
Plan the remaining work with step IDs, dependencies, affected interfaces,
and a check for each outcome. Keep unresolved retry decisions explicit.
Update docs/plan.md without implementing the feature.
```

**Expected result:** a concise plan that preserves completed work, covers acceptance criteria, identifies conditional steps, and names the next executable action.

### workflow-execute

Use it when the change is clear and implementation is authorized. Supply the agreed scope, relevant plan or checkpoint, and verification command when known. It reconciles those artifacts with current code and preserves unrelated edits.

```text
Use workflow-execute to implement the agreed input-size limit in
docs/import-retries.md. Inspect docs/plan.md and continue the unfinished step.
Preserve my unrelated UI changes. Add the relevant boundary tests and run
the importer tests. Keep the change local and update the checkpoint.
```

**Expected result:** the scoped implementation, verification results tied to the current change, and a checkpoint describing completed and remaining work. PR preparation is included only when sharing a PR is part of the request.

### workflow-debug

Use it for a reproducible bug or an intermittent failure with available evidence. Supply expected versus actual behavior, triggering input, environment, and logs or tests. Say whether you want diagnosis only or a correction.

For this example, prepare the disposable project described in the [cart demo](examples/cart/README.md), install the skill there, and open your agent in that project.

```text
Use workflow-debug in this cart project. Quantities above one produce the wrong
total, and a zero-quantity item must contribute zero.
Reproduce with python3 -B -m unittest -v from the project root, identify the
cause, and fix it. Preserve the existing input contract and verify all cases.
```

**Expected result:** a reproduction, evidence supporting the cause, the authorized fix, and before/after results. For an unresolved failure, it reports the remaining uncertainty and the observation needed next.

### workflow-audit

Use it to review a diff or PR for actionable defects. Supply the base and target revision or PR link, intended behavior, and acceptance criteria. A full diff and surrounding code provide more coverage than an isolated snippet.

```text
Use workflow-audit to review the current branch against origin/main.
The change should apply percentage discounts using integer cents.
Check rounding and boundary inputs, and reproduce suspected regressions.
Report findings with file, line, trigger, impact, and supporting evidence.
Keep this a review only; do not edit code or post GitHub comments.
```

**Expected result:** confirmed findings ordered by impact, the reviewed revision, and coverage gaps. Style preferences are separated from defects; an absence of findings is not formal approval or proof that no bugs exist.

### workflow-verify

Use it before declaring work complete. Supply the acceptance criteria, target revision, and available test, review, or deployment evidence. It checks whether that evidence still applies and runs missing checks within scope.

```text
Use workflow-verify to assess the import change against
docs/import-retries.md. Check whether the recorded tests cover the current
HEAD and run missing local checks. The PR is merged, but production has
not been inspected. Report what is verified, failed, or still pending.
Do not deploy or close the issue.
```

**Expected result:** a criterion-by-criterion evidence table, explicit failures or gaps, and the next action. Implementation, merge, deployment, and acceptance remain separate claims.

### workflow-doctor

Use it when onboarding or when setup, tooling, or access blocks a task. State what you are trying to do and include the failure message if available. The skill checks only the capabilities that task needs.

```text
Use workflow-doctor to check whether this repository is ready for local
Python development. Inspect repository instructions, runtime, documented
test commands, and installed workflow skill resources.
GitHub access is optional for this task. Diagnose setup without changing
configuration, and report the smallest remedy for each blocker.
```

**Expected result:** checks marked ready, failed, unknown, or not applicable, with evidence and remedies. It distinguishes missing tools, wrong targets, authentication failures, and network errors without exposing credential values.

### workflow-triage

Use it to organize incoming requests or a backlog before starting work. Supply the queue, existing issues, and known impact. It looks for duplicates and selects the next useful action without inventing urgency or ownership.

```text
Use workflow-triage on requests.md and the existing issues in backlog.json.
Two requests ask to retry failed imports; another asks for progress updates.
Identify likely duplicates, missing context, and the next action for each.
Return a table with evidence and suggested priority. Do not create or close
tickets, assign people, or start implementation.
```

**Expected result:** a compact table of requests, classifications, evidence, suggested priorities, related items, and next actions. Missing impact or incomplete queue access is stated explicitly.

### workflow-research

Use it when a technical choice needs evidence. Supply the decision, runtime or dependency constraints, and existing implementation. The skill compares viable options using primary sources and bounded experiments where useful.

```text
Use workflow-research to choose a CSV parsing approach for this project.
We require Python 3.9+, quoted commas and newlines, and no third-party
runtime dependencies. Inspect the current reader and compare it with the
suggestion to split lines on commas. Consult version-relevant official docs
and run a small parsing experiment. Recommend an approach without changing
the application or installing dependencies.
```

**Expected result:** a recommendation, alternatives, linked sources, documented facts versus inferences, and the smallest remaining experiment. Research does not automatically begin implementation.

### workflow-github-status

Use it for an evidence-based view of a specific repository's issues, PRs, checks, and blockers. Supply the exact repository and scope or time range. Live status requires a configured GitHub connector or CLI with read access; supplied snapshots support a limited report.

```text
Use workflow-github-status for owner/repository, focusing on open issues
and PRs merged during the last seven days. Inspect linked checks and
remaining acceptance criteria. Separate merged code from deployment and
verified delivery. Include links, observation time, blockers, and next
actions. Keep this read-only; do not update issues or send a standup.
```

**Expected result:** a status summary separating completed outcomes, ongoing work, dependencies, and unknowns. It checks whether green results cover the current revision and states pagination or access limits.

### workflow-handoff

Use it to save progress or resume an authorized task in a fresh session. Supply the task and current artifacts when saving, or the checkpoint when resuming. A checkpoint records evidence; current repository state determines what remains.

```text
Use workflow-handoff to save this task in docs/checkpoint.md.
Record HEAD, uncommitted changes, decisions, completed checks, remaining
work, and the first next action. Use repository-relative artifact paths.
```

In a later session:

```text
Use workflow-handoff to resume docs/checkpoint.md and finish the local fix.
Compare the checkpoint with the current branch and working tree first;
another contributor may have completed part of the work. Preserve unrelated
edits and rerun only checks invalidated by the changes or still missing.
```

**Expected result:** a recoverable checkpoint, or a reconciliation note followed by the next authorized unfinished step. Saving context alone does not send it to anyone or authorize future implementation.

### workflow-release

Use it to prepare a versioned release or publish one when explicitly requested. Supply the intended version or outcome, target revision, and project release policy. The skill distinguishes preparation, draft, publication, and deployment.

```text
Use workflow-release to prepare the next patch release from the current
HEAD. Inspect the project's versioning policy and previous release.
Update version metadata and changelog, check tests and reviews against the
target commit, and prepare release notes with recovery guidance.
Do not create a remote tag, publish a release, or deploy.
```

**Expected result:** consistent version metadata and notes, target commit, readiness checks, and unresolved publication conditions. When publication is separately requested, it checks existing tags/releases first and verifies the resulting target and assets afterward.

## Combine skills around an outcome

| Situation | Useful sequence | What each step adds |
| --- | --- | --- |
| An ambiguous feature | spec → plan → execute → audit → verify | Agreed behavior, actionable steps, implementation, defect review, and acceptance evidence. |
| A broken calculation | debug → verify | Reproduction and correction, then a check against the full acceptance criteria. |
| Work interrupted between sessions | handoff → execute → verify | Reconciled context, only the unfinished implementation, and current evidence. |
| A release candidate | audit → verify → release | Findings, revision-specific readiness, and release preparation or authorized publication. |

Use only the steps the task needs. Existing decisions and still-valid test results carry forward; naming a sequence does not grant permission to publish or deploy.

## How it fits your project

- **Project conventions stay in the project.** No required branch names, tracker, cloud provider, or team structure.
- **Context survives a session.** Optional templates capture acceptance, decisions, observed revision, evidence, and the next action.
- **Skills remain independent.** Export all 12 or a selection; no dependency on another installed skill.
- **Tools remain yours.** GitHub-specific operations use an available connector or CLI. Other skills can work locally.
- **Permissions remain explicit.** Instructions do not grant credentials or replace the agent host's controls. Existing user authorization is reused.

This is an instruction toolkit, not an autonomous service, an enforcement system, or a model. Results depend on the agent, tools, repository, and task. Version 0.1.1 includes 21 package tests, observations from four independent agent sessions covering all 12 skills, and a native Codex discovery check. These results do not establish a measured productivity improvement or universal client compatibility. See [validation and limits](docs/validation.md).

## Develop and contribute

```sh
python3 scripts/check_repository.py
```

Edit `skills/` and `workflow/`, then export again. Generated bundles belong in `dist/` and are not committed. The [contribution guide](CONTRIBUTING.md) explains how to propose a focused change and evaluate it.

Created and maintained by [Manuel Salomon](https://github.com/msalomonn). Free to use, modify, and share under the [MIT license](LICENSE).
