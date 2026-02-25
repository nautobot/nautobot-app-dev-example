# v3.0 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Added support for Nautobot 3.0.
- Added support for Python 3.13.

<!-- towncrier release notes start -->
## [v3.0.1 (2026-02-25)](https://github.com/nautobot/nautobot-app-dev-example/releases/tag/v3.0.1)

### Added

- [#134](https://github.com/nautobot/nautobot-app-dev-example/issues/134) - Added mkdocs plugin glightbox and included media files to provide examples when loaded on readthedocs

### Changed

- [#114](https://github.com/nautobot/nautobot-app-dev-example/issues/114) - Added breaking category to towncrier.

### Dependencies

- [#117](https://github.com/nautobot/nautobot-app-dev-example/issues/117) - Set minimum version of pylint-django to `>=2.5.4`.
- [#117](https://github.com/nautobot/nautobot-app-dev-example/issues/117) - Set minimum version of pylint-nautobot to `>=0.3.1`.

### Housekeeping

- [#109](https://github.com/nautobot/nautobot-app-dev-example/issues/109) - Automate release notes when using invoke generate-release-notes.
- [#127](https://github.com/nautobot/nautobot-app-dev-example/issues/127) - Move branch logic into upstream_testing.yml.
- [#128](https://github.com/nautobot/nautobot-app-dev-example/issues/128) - Updated CI workflow to always regenerate poetry lockfile.
- [#135](https://github.com/nautobot/nautobot-app-dev-example/issues/135) - Added Prepare Release workflow to automate releases.
- Rebaked from the cookie `nautobot-app-v2.7.0`.
- Rebaked from the cookie `nautobot-app-v2.7.1`.
- Rebaked from the cookie `nautobot-app-v3.0.0`.

## [v3.0.0 (2025-11-06)](https://github.com/nautobot/nautobot-app-dev-example/releases/tag/v3.0.0)

### Added

- Added support for Nautobot 3.0.
- Added support for Python 3.13.
