# Validation and limits

Version 0.1.1 separates package checks, behavioral observations, and client discovery. The [readiness review](validation-runs/2026-11-18.md) records the observed results and their limits.

## Automated package checks

Run `python3 scripts/check_repository.py`. This validates the repository's constrained frontmatter format, skill names, local inline Markdown resource links, export completeness, and the package tests.

The tests exercise:

- Independent all-skill and selected-skill exports after removing the source checkout.
- Included helpers, data files, client metadata, executable permissions, and license files.
- Protection of existing destinations, including dangling symbolic links.
- Rejection of source symlinks, reserved-path collisions, unrecognized skill-root files, missing references, and escaping resource paths.
- Detection of changed, missing, or additional exported files against the manifest.
- Command-line export and verification behavior.
- Controlled rejection of malformed manifest metadata.
- Exclusion of local drafts, environments, and previous exports from source documentation checks, while retaining checks on maintained documentation.

The exporter uses Python's standard library and does not fetch external links. Local runs are recorded in [the initial validation record](validation-record.md); GitHub Actions runs the same package checks on Python 3.9 and 3.13. A configured workflow is not evidence of a passing hosted run; inspect the actual Actions result for the commit you use.

## Reproducible fixture

The [cart exercise](../examples/cart/README.md) deliberately fails two of four tests before its correction. It supplies concrete acceptance cases for debugging and continuation. Its tests are separate from package CI because preserving the broken fixture is intentional.

A deterministic before/after run verifies that the fixture detects its bug. It does not measure whether a fresh agent chooses the right actions.

## Agent behavior and compatibility

[Twelve evaluation scenarios](evaluations.md) cover the skills' intended decisions. Four independent agent sessions exercised all 12 skills across three synthetic local projects: diagnosing and resuming a cart fix, planning CSV retries, and reviewing an incomplete delivery. The observed acceptance checks passed; the [run record](validation-runs/2026-11-18.md) identifies which scenario variants were exercised. These are demonstrations, not a statistical benchmark or exhaustive execution of every variant in the scenario plan.

Codex CLI 0.160.0 discovered and enabled all 12 skills installed from the published ZIP into a disposable project's `.agents/skills/` directory. This checks native discovery; it does not establish automatic skill selection from arbitrary prompts. The agent sessions explicitly named their skills.

No cross-provider end-to-end compatibility claim or productivity benchmark is made. GitHub and release behavior was evaluated against synthetic snapshots without external writes or a production deployment. Instructions support an existing model and tools; they do not enforce permissions or guarantee outcomes.
