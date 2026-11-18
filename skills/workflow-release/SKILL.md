---
name: workflow-release
description: "Prepare or publish a versioned software release with revision-specific checks, change notes, and recovery information, following the repository release policy."
---

# workflow-release

Read the [working agreement](../../workflow/agreement.md). Determine whether the user requested preparation, a draft, or publication. Inspect the repository's version source, tag convention, release process, required reviews, and target commit; do not impose a branch topology.

1. Compare the intended target with the previous release. Account for breaking behavior, migrations, configuration changes, and fixes. Propose the version using project policy and the requested scope.
2. Check relevant tests and reviews against the actual target. Identify incomplete checks and required decisions. Preparing release files may proceed while publication conditions remain unresolved.
3. Update version metadata and notes consistently. Preserve historical entries. Review generated artifacts and exclude secrets or local-only material. Use the [release checklist](../../workflow/templates/release.md) where a project equivalent is absent.
4. Immediately before an authorized publication, recheck the target commit, required conditions, and whether the intended tag or release already exists. If it exists, inspect its target and assets; do not move or replace it silently.
5. Publish only within the requested authority and repository policy. After an uncertain response, query the release or tag before retrying. Stop retries that could duplicate or replace artifacts until the actual state is known.
6. Verify the resulting tag, release status, target revision, and relevant artifacts. Deployment and production verification are separate unless explicitly part of the release task.

Deliver the version, commit, notes or release URL, checks and limitations, and recovery guidance appropriate to the change. Distinguish prepared, draft, published, and deployed states.
