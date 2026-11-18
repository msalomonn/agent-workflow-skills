---
name: workflow-doctor
description: "Diagnose repository setup, skill resources, tooling, or integration access when onboarding or troubleshooting a blocked development workflow."
---

# workflow-doctor

Read the [working agreement](../../workflow/agreement.md). Determine the target repository from the user's request and working directory, not from the directory containing this skill.

Check only capabilities required by the intended task:

- Repository identity, remote, current branch, working changes, and contribution instructions.
- Availability of the relevant runtime and documented verification commands.
- Presence of the installed skill and its linked resources. Detect conflicting skill names when observable; do not assume a skill is loaded merely because its file exists.
- For required external services, verify the connected account and target with an appropriate read operation. A successful read establishes that read capability, not write access.
- Missing project context or configuration, using the [project template](../../workflow/templates/project.md) only where useful.

Report each necessary check as ready, failed, unknown, or not applicable, with observed evidence and the smallest remedy. Distinguish absent tools, authentication failures, wrong target, and network errors.

Diagnosis is read-only. If setup or repair is also requested, make the concrete in-scope corrections and verify them. Preserve unrelated configuration and use existing authorization; do not introduce blanket approval ceremonies. Never print credential values. A missing optional integration should not block local work.
