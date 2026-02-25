# v2.2 Release Notes

This document describes all new features and changes in the release. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Release Overview

<!-- towncrier release notes start -->
## [v2.2.2 (2025-10-15)](https://github.com/nautobot/nautobot-app-dev-example/releases/tag/v2.2.2)

### Housekeeping

- [#555](https://github.com/nautobot/nautobot-app-dev-example/issues/555) - Added support for `--constrain-python-ver` (accepting X.Y or X.Y.Z) in `invoke lock`.
- Rebaked from the cookie `nautobot-app-v2.5.1`.
- Rebaked from the cookie `nautobot-app-v2.6.0`.
- Updated release process into separate workflow and added support for publishing to Artifactory.

## [v2.2.1 (2025-09-09)](https://github.com/nautobot/nautobot-app-dev-example/releases/tag/v2.2.1)

### Changed

- [#104](https://github.com/nautobot/nautobot-app-dev-example/issues/104) - Changed max length of CharFields to `nautobot.apps.constants.CHARFIELD_MAX_LENGTH`.

### Documentation

- [#104](https://github.com/nautobot/nautobot-app-dev-example/issues/104) - Removed `docs/requirements.txt` and updated readthedocs config to install dependencies from Poetry.
- [#104](https://github.com/nautobot/nautobot-app-dev-example/issues/104) - Added `pymdownx.details` markdown extension to mkdocs config.

### Housekeeping

- [#101](https://github.com/nautobot/nautobot-app-dev-example/issues/101) - Implement DJLint for Django Template Linting.
- [#104](https://github.com/nautobot/nautobot-app-dev-example/issues/104) - Updated CI to use ubuntu-latest image.
- [#104](https://github.com/nautobot/nautobot-app-dev-example/issues/104) - Changed CI SLACK_WEBHOOK_URL secret to OSS_PYPI_SLACK_WEBHOOK_URL.

## [v2.2.0 (2025-08-26)](https://github.com/nautobot/nautobot-app-dev-example/releases/tag/v2.2.0)

### Changed

- [#95](https://github.com/nautobot/nautobot-app-dev-example/issues/95) - Updated Poetry version in CI and pyproject.toml build-system.requires to 2.1.3.
- [#98](https://github.com/nautobot/nautobot-app-dev-example/issues/98) - Updated pymarkdownlnt to version 0.9.30 and changed the pymarkdown configuration in pyproject.toml.

### Dependencies

- [#93](https://github.com/nautobot/nautobot-app-dev-example/issues/93) - Dropped support for Python 3.8 and Nautobot <2.4.11.
- [#95](https://github.com/nautobot/nautobot-app-dev-example/issues/95) - Pinned Django debug toolbar to ~5.2.0.

### Documentation

- [#87](https://github.com/nautobot/nautobot-app-dev-example/issues/87) - Added Analytics GTM template override only to RTD docs build.

### Housekeeping

- [#93](https://github.com/nautobot/nautobot-app-dev-example/issues/93) - Implemented Nautobot UI Component Framework.
- [#215](https://github.com/nautobot/nautobot-app-dev-example/issues/215) - Add default labels to issue templates.
- [#517](https://github.com/nautobot/nautobot-app-dev-example/issues/517) - Added searchable models to AppConfig.
- Rebaked from the cookie `nautobot-app-v2.5.0`.
