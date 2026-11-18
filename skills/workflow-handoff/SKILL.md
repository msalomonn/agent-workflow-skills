---
name: workflow-handoff
description: "Save a recoverable work checkpoint or resume from one by reconciling repository changes, decisions, evidence, and remaining steps."
---

# workflow-handoff

Read the [working agreement](../../workflow/agreement.md). Determine whether the request is to save progress, transfer context, or resume an already authorized task.

When saving, use the [checkpoint template](../../workflow/templates/checkpoint.md) or the existing format. Record observed HEAD, working changes, decisions with their source, completed steps with evidence, missing checks, next action, and where artifacts are actually available. Include a portable diff or committed changes when sharing is authorized; a path on one machine is not a shared artifact.

When resuming:

1. Read the checkpoint and the current repository instructions. Inspect actual branch, HEAD, changes, and relevant remote issue/PR state when available.
2. Reconcile differences. Preserve unrelated edits. If the task was merged or changed scope, inspect that outcome before applying old steps.
3. Reuse valid decisions, authorization, and evidence. Mark exactly which verification was invalidated by subsequent changes and why.
4. Select the first genuinely unfinished step within the current request. Resume only the work that remains authorized; a saved plan is context, not a new authorization.
5. Append a short reconciliation note and keep prior evidence available. Indicate stale remote observations when offline.

Do not embed secrets, personal chat transcripts, or ephemeral absolute paths as the sole source of context. Preparing a handoff does not authorize messaging another person or agent.
