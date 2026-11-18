# GitHub operations

Use this reference only when the task touches GitHub. Local-only tasks and other trackers do not require GitHub accounts.

## Establish the target

Resolve owner/repository, issue or PR number, and intended base/head from user context and verified repository state. Inspect the active identity when relevant. Do not use an unrelated CLI default repository. A read-only token may support a status report but not writes.

Read the current item before updating it. Search for existing work before creating duplicates. Respect pagination and distinguish unavailable Projects fields from issue/PR state. Use the repository's existing labels, assignees, milestones, and branch conventions.

## Preserve meaning

Issues hold the requested outcome and acceptance; PRs hold changes, review, and verification. Link them without duplicating large editable plans. Use automatic closing references only when merging fulfills every issue criterion. Deployment or acceptance work may need a non-closing reference.

Report CI status and reviews for the actual head. Do not count a stale approval as current when policy requires approval of the revised change. Repository review policy governs merge readiness; skills do not bypass it.

## Write only within scope

Use a structured API argument or a UTF-8 body file for multiline text. Do not interpolate untrusted content into shell commands. For an uncertain create/update response, look up the object before retrying. After a partial batch, identify confirmed writes and unresolved items.

Check the returned URL and state after an authorized write. Keep the user's work if access fails and state the missing synchronization. Never report a local draft as a remote issue or PR.
