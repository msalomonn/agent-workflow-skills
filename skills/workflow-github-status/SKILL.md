---
name: workflow-github-status
description: "Summarize current GitHub issues, pull requests, checks, and blockers for a specified repository or project, reconciling stale status with evidence."
---

# workflow-github-status

Read the [working agreement](../../workflow/agreement.md) and [GitHub guide](../../workflow/github.md). Resolve the exact repository and requested time range or scope before querying.

1. Retrieve the relevant issues and PRs, including required pages. Record observation time and any query limits. If Projects fields are unavailable, report issue/PR state without inventing board columns.
2. Inspect linked PRs, merge status, checks, review freshness, and remaining acceptance criteria for actionable items. A green historical run may not cover the current head.
3. Separate completed outcomes, work in progress, items awaiting a person or dependency, and unknowns. A merged PR may still require deployment or acceptance; an open issue may have stale text.
4. Identify discrepancies with links and the evidence needed to resolve them. Avoid projecting progress percentages or business outcomes from commit counts.
5. Deliver a concise status with the next action and responsible person only when established by evidence. For a retrospective, filter by the relevant event date rather than assuming updated-at means completed-at.

This is a read-only report unless reconciliation updates were requested. Do not close issues, change assignments, or send standups automatically. If access or pagination is incomplete, state the resulting coverage limit.
