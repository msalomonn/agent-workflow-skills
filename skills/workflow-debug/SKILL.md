---
name: workflow-debug
description: "Investigate a reproducible failure or intermittent incident using falsifiable hypotheses; apply a fix when the request includes correction."
---

# workflow-debug

Read the [working agreement](../../workflow/agreement.md). Gather the symptom, expected result, environment, affected revision, and available evidence. Missing reproduction limits the conclusion; it does not justify guessing a cause.

1. Establish impact and triggering conditions. Reproduce in an appropriate environment or reconstruct from sanitized logs. In an active incident, an authorized reversible mitigation may precede root-cause analysis; label the two separately.
2. Trace the input to the failing boundary and compare with a successful case. Examine recent changes and contracts between components.
3. State a falsifiable hypothesis and choose the smallest observation that distinguishes it from alternatives. Record the result before revising the explanation. If a retry yields no new evidence, change the investigation or identify the missing observation.
4. Explain how the confirmed cause produces the symptom. A diagnosis-only request ends with findings and a proposed correction. When correction is authorized, implement the smallest adequate fix.
5. For a code bug, demonstrate a test failing for the relevant reason before the fix and passing afterward, with nearby cases as needed. For visual or configuration faults, use the corresponding observable check and describe its limits.

Deliver reproduction, facts versus hypotheses, cause or remaining uncertainty, fix or mitigation, before/after evidence, and residual work. A mitigation alone does not establish a permanent fix.
