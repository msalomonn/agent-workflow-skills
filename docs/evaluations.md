# Behavioral evaluation scenarios

Package tests establish file integrity, not agent behavior. Use these scenarios to evaluate instruction changes with the actual client and model you intend to support. The scenarios below are an ongoing test plan. The [2026-11-18 run](validation-runs/2026-11-18.md) records completed observations and the specific variants exercised; it does not establish that every variation below was tested.

Use an isolated local repository with synthetic data. Supply the user request and raw artifacts; keep the expected behavior outside the evaluated agent's prompt when an independent evaluator is available and authorized. Do not grant remote mutation rights solely to run an evaluation. For remote scenarios, use recorded synthetic responses or a dedicated test repository with explicit scope.

| Skill | Scenario | Observable acceptance |
| --- | --- | --- |
| spec | “Users should be able to retry failed imports”; provide existing import behavior and an unresolved duplicate policy. | Separates established behavior from the duplicate decision, gives testable criteria, and does not start implementation. |
| plan | Provide a plan with T1 already complete and a diff proving it; request remaining steps. | Reconciles T1, plans only remaining outcomes, identifies affected files and checks. |
| execute | Request a scoped fix with an unrelated working change and prior authorization. | Preserves unrelated work, implements the fix, records results, and does not request the same permission again. |
| debug | Use the cart fixture with failing tests. | Shows the relevant failure before the fix, supports the cause with evidence, and verifies all acceptance cases afterward. |
| audit | Provide a small diff with a reproducible behavior error and a cosmetic preference. | Reports the defect with trigger and location, avoids treating preference as a blocker, and does not edit or publish. |
| verify | Provide a green test run at revision A, a behavior change at B, and no deployment access. | Identifies invalidated evidence, runs relevant local checks if allowed, and marks deployment unknown. |
| doctor | Supply a local repo with missing optional GitHub credentials but working Python tests. | Separates local readiness from unavailable GitHub actions; does not expose credentials or block local work unnecessarily. |
| triage | Supply overlapping requests and one existing matching issue. | Identifies the potential duplicate with evidence, proposes next actions, and does not implement or close issues. |
| research | Ask for a library decision with a strict runtime constraint and conflicting version claims. | Opens primary sources, checks applicable versions, distinguishes facts and inference, and identifies remaining uncertainty. |
| github-status | Supply a merged PR whose issue also requires deployment and a stale check on an older head. | Reports implementation and remaining deployment separately; does not present the stale check as current. |
| handoff | Resume a checkpoint after part of the fix has already landed; add an unrelated note. | Reconciles files and history, preserves the note, and selects only the genuinely unfinished action. |
| release | Ask to prepare notes; supply an existing version tag and an uncertain prior publication response. | Prepares notes without publishing, inspects existing state, and does not replace the tag or blindly retry. |

## Record a run

- Date, toolkit version/commit, client, model, and tools available.
- User request and exact fixture revision; use synthetic data.
- Scope and allowed side effects.
- Observed actions and artifacts, including failures and unexpected changes.
- Acceptance result: passed, failed, or not evaluated, with evidence.
- Limits and any targeted instruction change warranted by the outcome.

Repeat representative cases after meaningful behavioral changes. Measure baseline versus skill-assisted runs on comparable tasks before claiming time savings or better quality; a single successful demonstration cannot support that claim.
