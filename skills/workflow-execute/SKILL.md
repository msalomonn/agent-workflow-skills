---
name: workflow-execute
description: "Implement or resume an authorized software change, preserving existing work and recording verification and the next actionable checkpoint."
---

# workflow-execute

Read the [working agreement](../../workflow/agreement.md), accepted scope, sufficient existing plan, and any checkpoint. Do not restart specification for a change that is already clear.

1. Inspect repository instructions, branch, HEAD, working changes, and relevant issue or PR state. Reconcile the checkpoint with current evidence. Preserve unrelated changes; isolate conflicting work before editing.
2. Select the first genuinely unfinished outcome. Implement within the agreed scope using this repository's branch and contribution conventions. Record newly discovered scope without silently absorbing it.
3. Run verification appropriate to the changed behavior. Diagnose failures before retrying edits; distinguish a regression from an existing environmental failure. Record the command, exit result, revision or diff, and environment.
4. Review the final diff for unintended edits and sensitive data. If sharing a PR is in scope and tools are available, prepare it with behavior, evidence, and remaining work. Apply the [GitHub guide](../../workflow/github.md) when operating there.
5. At a meaningful pause or delivery, record a [checkpoint](../../workflow/templates/checkpoint.md). Preserve valid decisions and approvals; identify what is local versus shared.

Report implemented behavior, verification, actual branch or PR, and the next action. An uncertain API response needs a state lookup before retrying. Do not report a local draft as a published PR, or a merged change as deployed.
