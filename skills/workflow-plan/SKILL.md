---
name: workflow-plan
description: "Turn agreed software scope into executable steps with dependencies and verification, or reconcile an existing plan with completed work."
---

# workflow-plan

Read the [working agreement](../../workflow/agreement.md), current acceptance criteria, and relevant code interfaces. A plan should be as small as the change allows.

1. Check the current repository, branch, working changes, and existing plan. Compare completed steps with evidence before adding work.
2. Divide the remaining scope into reviewable outcomes. Each step needs a stable ID, dependencies, affected paths or interfaces, expected result, and a relevant verification.
3. Resolve blocking uncertainty early. Leave dependent steps conditional when a necessary decision is missing; do not invent an irreversible design to fill the gap.
4. Include review and delivery conditions that apply to this project. Distinguish implementation from deployment or acceptance when those are separate outcomes.
5. Check that every acceptance criterion is covered, dependencies are possible, and file paths exist or are explicitly proposed as new. Avoid writing the entire implementation in the plan.

Use the [plan template](../../workflow/templates/plan.md) or the project's equivalent. Deliver the next executable step and explicit blockers. Planning does not expand permission to publish, merge, or contact other people.
