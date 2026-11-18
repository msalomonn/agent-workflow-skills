---
name: workflow-spec
description: "Define observable behavior and acceptance criteria for an ambiguous software change. Reuse an existing specification when it already covers the request."
---

# workflow-spec

Start from the request, existing behavior, repository instructions, and any agreed scope. Read the [working agreement](../../workflow/agreement.md).

1. Separate observed facts, assumptions, and unresolved decisions. Inspect the relevant implementation before proposing behavior that already exists.
2. Describe who does what and the observable result. Include failure cases and boundaries that affect acceptance. A bug report needs expected versus actual behavior; its cause may still be unknown.
3. Give each acceptance criterion a concrete observation or test. Identify exclusions and dependencies. Include data handling or reversal requirements when the change actually needs them.
4. Resolve routine choices from available context. Ask only for decisions that materially change scope or acceptance and cannot be inferred. Continue independent work while those decisions are pending.
5. Update the existing issue or specification within the authorized scope. Keep one authoritative set of acceptance criteria; link supporting design documents instead of duplicating editable copies.

Deliver the behavior, criteria, exclusions, dependencies, and remaining decisions. Mark partial readiness when a decision blocks only part of the work. Specification work alone does not request implementation.

Use the [project context](../../workflow/templates/project.md) only when equivalent context is missing.
