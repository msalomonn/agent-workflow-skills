---
name: workflow-verify
description: "Check evidence before claiming a change is implemented, merged, deployed, or accepted, and identify precisely what remains unverified."
---

# workflow-verify

Read the [working agreement](../../workflow/agreement.md) and current acceptance criteria. Use this at delivery or closure; do not repeat a full suite after every message.

1. Identify the claims being made and the evidence each needs. Implementation, review/merge, deployment, and acceptance can have different conditions.
2. Inspect actual results, affected revision or diff, environment, and date. Check whether subsequent edits invalidate any result. Reuse still-valid evidence with its limits.
3. Run only missing or invalidated checks that are in scope. Checking deployment status is not a request to deploy. Missing access produces an explicit verification gap.
4. Map criterion to evidence and outcome: verified, failed, pending, or not applicable with a reason. Read completion and exit status; a started command is not a passing test.
5. Report failures and their impact alongside successful checks. Apply the [GitHub guide](../../workflow/github.md) before updating or closing an issue; closure depends on all its criteria, including post-merge work if required.

Deliver a concise evidence table and next action. Save a [checkpoint](../../workflow/templates/checkpoint.md) when work will resume later. Do not transform an earlier checkpoint or an informal review into proof of current completion.
