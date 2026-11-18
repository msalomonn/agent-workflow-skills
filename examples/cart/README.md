# Local debugging and continuity demo

This fixture deliberately contains a bug. Run it in a disposable copy so the toolkit's example stays reproducible. It uses Python's standard library; there are no external services or credentials.

## Prepare

From the toolkit checkout:

```sh
WORKFLOW_DEMO_DIR=$(mktemp -d)
cp -R examples/cart "$WORKFLOW_DEMO_DIR/cart"
cd "$WORKFLOW_DEMO_DIR/cart"
python3 -m unittest -v
```

Expected baseline: **4 tests run, 2 fail**, because the total ignores item quantities. Unit prices are integer cents and quantities are non-negative integers, validated by the caller. Acceptance: empty cart returns zero; each item's contribution respects its quantity; the result remains an integer. Adding payment services or input-validation features is outside this exercise.

Install the exported skills in this disposable project's skill directory, then open an agent session there. A Git repository is optional; initialize one locally if you want to practice diff review. There is no remote target to publish to.

## Exercise

1. Ask: “Use workflow-debug to diagnose the failing cart tests. Record the failing command and cause; stop before changing code.”
2. Ask: “Use workflow-handoff to save a checkpoint with the remaining fix, acceptance criteria, and current evidence.”
3. Start a fresh agent session with the project files and checkpoint. Ask: “Resume from the checkpoint with workflow-execute. Fix the authorized cart bug, preserve unrelated files, and verify the result with workflow-verify.”

Expected result: all **4 tests pass**; the fix is limited to the quantity calculation; the report distinguishes local verification from deployment. The agent should reconcile the checkpoint with current files rather than repeat an already completed implementation.

To make reconciliation meaningful, add an unrelated `personal-note.txt` between sessions and check that it survives. A separate `workflow-audit` request can review the resulting diff without editing it.

## What this demonstrates

The fixture gives a deterministic before/after check and a small continuity task. Passing it does not establish performance on larger codebases, complete agent compatibility, or a productivity improvement. Record agent/client version and actual outcomes when you run the workflow; see [evaluation scenarios](../../docs/evaluations.md).
