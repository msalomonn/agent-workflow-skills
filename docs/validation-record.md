# Initial validation record

Historical record: the subsequent [readiness review](validation-runs/2026-11-18.md) adds independent behavioral evaluation and native discovery results.

Date: 2026-11-18. Package: 0.1.0.

This file records local checks performed while preparing the initial repository. Hosted CI results are tracked separately by commit in GitHub Actions.

- Python 3.9.6 on macOS: repository package checks and export tests executed successfully.
- All 12 skill entry points passed the skill-creator frontmatter validator.
- Full export verified against its SHA-256 manifest; tests also remove the source checkout before verifying an independent installation.
- Cart fixture: four tests, two expected failures before correction; four passing tests after applying the quantity correction in a disposable copy. The repository fixture remains intentionally broken.
- Skill instructions reviewed for scope, activation boundaries, local resource availability, continuation behavior, and clear separation of implementation, publication, and acceptance.

Limits: no independent-agent behavioral evaluation was executed; no desktop discovery run, other-client end-to-end run, or production deployment was used to validate this release. The scenario suite remains a reproducible evaluation plan rather than a completed benchmark.
