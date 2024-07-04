# v1.0 Release Notes

This document describes all new features and changes in the release `1.0`. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

- Major features or milestones
- Achieved in this `x.y` release
- Changes to compatibility with Nautobot and/or other apps, libraries etc.

## [v1.0.0 (2024-07-04)](https://github.com/nautobot/nautobot-app-dev-example/releases/tag/v1.0.0)

### Changed

- [#1](https://github.com/nautobot/nautobot-app-dev-example/issues/1) - Cleaned up the baked cookie.
- [#21](https://github.com/nautobot/nautobot-app-dev-example/issues/21) - Updated steps to create releases.
- [#21](https://github.com/nautobot/nautobot-app-dev-example/issues/21) - Changed CI changelog step to ignore branch names starting with "release".

### Fixed

- [#20](https://github.com/nautobot/nautobot-app-dev-example/issues/20) - Removed deprecated default-authentication-plugin setting for mysql containers.

### Housekeeping

- [#6](https://github.com/nautobot/nautobot-app-dev-example/issues/6) - Fixed the documentation to explain the app usage.
- [#7](https://github.com/nautobot/nautobot-app-dev-example/issues/7) - Bumped `networktocode/gh-action-setup-poetry-environment` from `v5` to `v6`.
- [#7](https://github.com/nautobot/nautobot-app-dev-example/issues/7) - Bumped `actions/setup-python` from `v4` to `v5`.
- [#8](https://github.com/nautobot/nautobot-app-dev-example/issues/8), [#9](https://github.com/nautobot/nautobot-app-dev-example/issues/9) - Re-baked from the latest template.
- [#10](https://github.com/nautobot/nautobot-app-dev-example/issues/10) - Fixed NTC link in `README.md`.
- [#14](https://github.com/nautobot/nautobot-app-dev-example/issues/14) - Fully integrated ruff as a (partial) replacement for the other linters.
- [#16](https://github.com/nautobot/nautobot-app-dev-example/issues/16) - More additions on ruff integration.
