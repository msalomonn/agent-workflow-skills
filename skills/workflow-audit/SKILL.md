---
name: workflow-audit
description: "Review a code diff or pull request against its intended behavior and relevant risks, reporting actionable findings without modifying the change."
---

# workflow-audit

Read the [working agreement](../../workflow/agreement.md). Establish the reviewed base, head, requested scope, and acceptance criteria. A snippet supports only a partial review.

1. Read changed code and the surrounding paths needed to understand its behavior. Prioritize execution errors, regressions, contract violations, and risks relevant to this change.
2. Validate a potential finding through a triggering input, execution path, or reproduction. Separate pre-existing problems and style preferences from introduced defects.
3. For each confirmed finding, report impact, file and verified line or exact expression, triggering condition, consequence, and evidence. Express unresolved uncertainty as a question or coverage gap.
4. Compare verification with acceptance criteria. A passing build may leave behavior, migration, visual, or production checks uncovered. Judge evidence rather than a confidence score or number of review rounds.
5. Return findings ordered by impact, reviewed revision, and coverage limits. If none are confirmed, say that without implying the absence of bugs or formal approval.

A review request does not itself authorize editing code, posting comments externally, approving a PR as the user, or merging it. Preserve any separate authorization already given.
