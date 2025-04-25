# v2.1 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Lots of housekeeping and preparation for app cookiecutter v2.5.0.

## [v2.1.1 (2025-04-25)](https://github.com/nautobot/nautobot-app-dev-example/releases/tag/v2.1.1)

### Fixed

- [#77](https://github.com/nautobot/nautobot-app-dev-example/issues/77) - Fixed release workflow.

## [v2.1.0 (2025-04-24)](https://github.com/nautobot/nautobot-app-dev-example/releases/tag/v2.1.0)

### Added

- [#46](https://github.com/nautobot/nautobot-app-dev-example/issues/46) - Added ability to trigger upstream testing manually.
- [#49](https://github.com/nautobot/nautobot-app-dev-example/issues/49) - Added docs view to fix the link on the "Installed Apps" page.
- [#50](https://github.com/nautobot/nautobot-app-dev-example/issues/50) - Added pylint django migrations checker to the `invoke pylint` command.
- [#53](https://github.com/nautobot/nautobot-app-dev-example/issues/53) - Added the ability to pass service name to `invoke cli`
- [#61](https://github.com/nautobot/nautobot-app-dev-example/issues/61) - Added Environment variable to control the Celery Beat Log Level.

### Changed

- [#60](https://github.com/nautobot/nautobot-app-dev-example/issues/60) - Disabled coverage reporting on invoke unittest unless --coverage is used.

### Fixed

- [#44](https://github.com/nautobot/nautobot-app-dev-example/issues/44) - Fixed build failing when `NAUTOBOT_VER` doesn't exist in PyPi, for example when using a branch name.
- [#47](https://github.com/nautobot/nautobot-app-dev-example/issues/47) - Fixed output on `invoke lock` command.
- [#54](https://github.com/nautobot/nautobot-app-dev-example/issues/54) - Fixed `invoke tests` exiting early even when tests pass.

### Dependencies

- [#58](https://github.com/nautobot/nautobot-app-dev-example/issues/58) - Pinned mkdocs-autorefs.
- [#69](https://github.com/nautobot/nautobot-app-dev-example/issues/69) - Updated towncrier dependency to >=23.6.0,<=24.8.0

### Housekeeping

- [#37](https://github.com/nautobot/nautobot-app-dev-example/issues/37) - Updated docs dependencies to latest versions and pinned griffe due to repeated breaking of docs builds.
- [#40](https://github.com/nautobot/nautobot-app-dev-example/issues/40) - Rebaked from the cookie `nautobot-app-v2.3.2`.
- [#48](https://github.com/nautobot/nautobot-app-dev-example/issues/48) - Enabled `LOG_DEPRECATION_WARNINGS` setting.
- [#56](https://github.com/nautobot/nautobot-app-dev-example/issues/56) - Pin Poetry to 1.8.5.
- [#56](https://github.com/nautobot/nautobot-app-dev-example/issues/56) - Move Pull Request Template to the proper location.
- [#58](https://github.com/nautobot/nautobot-app-dev-example/issues/58) - Added app_name to assist with Django URL resolver.
- [#65](https://github.com/nautobot/nautobot-app-dev-example/issues/65) - Added Code Coverage Report to the CI.
- [#67](https://github.com/nautobot/nautobot-app-dev-example/issues/67) - Added `--format` argument to `invoke backup-db` to support exporting in tar format to support Nautobot Cloud snapshots.
- [#68](https://github.com/nautobot/nautobot-app-dev-example/issues/68) - Add docs back into the wheel files.
- [#69](https://github.com/nautobot/nautobot-app-dev-example/issues/69) - Pinned github actions to their commit refs instead of tags/branches.
- [#69](https://github.com/nautobot/nautobot-app-dev-example/issues/69) - Removed jQuery from mkdocs configuration.
- [#70](https://github.com/nautobot/nautobot-app-dev-example/issues/70) - Updates from the cookiecutter nautobot app standards.
- [#71](https://github.com/nautobot/nautobot-app-dev-example/issues/71) - Updated postgres docker image to version 17 and mysql docker image to lts.
- [#72](https://github.com/nautobot/nautobot-app-dev-example/issues/72) - Added markdownlint task and CI check.
- Rebaked from the cookie `nautobot-app-v2.3.0`.
- Rebaked from the cookie `nautobot-app-v2.4.0`.
- Rebaked from the cookie `nautobot-app-v2.4.1`.
- Rebaked from the cookie `nautobot-app-v2.4.2`.
