# v3.1 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Major features or milestones
- Changes to compatibility with Nautobot and/or other apps, libraries etc.

<!-- towncrier release notes start -->

## [v3.1.0 (2026-05-15)](https://github.com/nautobot/nautobot-app-dev-example/releases/tag/v3.1.0)

### Added

- [#158](https://github.com/nautobot/nautobot-app-dev-example/issues/158) - Added a starting point for generating test data.

### Fixed

- [#162](https://github.com/nautobot/nautobot-app-dev-example/issues/162) - Updates the CI pipeline so that we auto increment post-release versions when creating a release from main, develop, next, and ltm- branches.

### Housekeeping

- [#149](https://github.com/nautobot/nautobot-app-dev-example/issues/149) - Fixed the sizing of the logo in the footer as well as adjusted it to be inline with the text.
- [#159](https://github.com/nautobot/nautobot-app-dev-example/issues/159) - Housekeeping update Prepare-Release workflow to use a token when creating a PR so that GitHub Actions run.
- [#160](https://github.com/nautobot/nautobot-app-dev-example/issues/160) - Fixed the prepare release workflow bumping the version on prereleases resulting in a version number that is 2 ahead of the last release.
- [#161](https://github.com/nautobot/nautobot-app-dev-example/issues/161) - Added previous_version prompt to prepare-release workflow.
- [#164](https://github.com/nautobot/nautobot-app-dev-example/issues/164) - Added a release workflow job to sync release notes from `ltm` branches back to `develop` via an automated pull request.
- Rebaked from the cookie `nautobot-app-v3.1.3`.
