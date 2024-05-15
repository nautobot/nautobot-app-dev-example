# Release Checklist

This document is intended for app maintainers and covers the steps to perform when releasing new versions of the app.

## Minor Version Bumps

### Update Requirements

Every minor version release should refresh `poetry.lock`, so that it lists the most recent stable release of each package. To do this:

0. Run `poetry update --dry-run` to have Poetry automatically tell you what package updates are available and the versions it would upgrade to. This requires an existing environment created from the lock file (i.e. via `poetry install`).
1. Review each requirement's release notes for any breaking or otherwise noteworthy changes.
2. Run `poetry update <package>` to update the package versions in `poetry.lock` as appropriate.
3. If a required package requires updating to a new release not covered in the version constraints for a package as defined in `pyproject.toml`, (e.g. `Django ~3.1.7` would never install `Django >=4.0.0`), update it manually in `pyproject.toml`.
4. Run `poetry install` to install the refreshed versions of all required packages.
5. Run all tests (`poetry run invoke tests`) and check that the UI and API function as expected.

### Update Documentation

Commit any resulting changes from the following sections to the documentation before proceeding with the release.

!!! tip
    Fire up the documentation server in your development environment with `poetry run mkdocs serve`! This allows you to view the documentation site locally (the link is in the output of the command) and automatically rebuilds it as you make changes.

#### Link to the Release Notes Page

A new minor version requires the creation of a new release notes page in the documentation (e.g. `docs/admin/release_notes/version_X.Y.md`). Add this new page to the table of contents within `mkdocs.yml`.

### Verify the Installation and Upgrade Steps

Follow the [installation instructions](../admin/install.md) to perform a new production installation of the app. If possible, also test the [upgrade process](../admin/upgrade.md) from the previous released version.

The goal of this step is to walk through the entire install process *as documented* to make sure nothing there needs to be changed or updated, to catch any errors or omissions in the documentation, and to ensure that it is current with each release.

---

## All Releases

### Verify CI Build Status

Ensure that continuous integration testing on the `develop` branch is completing successfully.

### Bump the Version

Update the package version using `poetry version` if necessary. This command shows the current version of the project or bumps the version of the project and writes the new version back to `pyproject.toml` if a valid bump rule is provided.

The new version must be a valid semver string or a valid bump rule: `patch`, `minor`, `major`, `prepatch`, `preminor`, `premajor`, `prerelease`. Always try to use a bump rule when you can.

Display the current version with no arguments:

```no-highlight
> poetry version
nautobot-dev-example 1.0.0-beta.2
```

Bump pre-release versions using `prerelease`:

```no-highlight
> poetry version prerelease
Bumping version from 1.0.0-beta.2 to 1.0.0-beta.3
```

For major versions, use `major`:

```no-highlight
> poetry version major
Bumping version from 1.0.0-beta.2 to 1.0.0
```

For patch versions, use `minor`:

```no-highlight
> poetry version minor
Bumping version from 1.0.0 to 1.1.0
```

And lastly, for patch versions, you guessed it, use `patch`:

```no-highlight
> poetry version patch
Bumping version from 1.1.0 to 1.1.1
```

Please see the [official Poetry documentation on `version`](https://python-poetry.org/docs/cli/#version) for more information.

### Update the Changelog

!!! important
    The changelog must adhere to the [Keep a Changelog](https://keepachangelog.com/) style guide.

This example uses 1.4.2, but change the version number to match the version you bumped to in the previous step. First, create a release branch off of `develop` (`git switch -c release-1.4.2 develop`).

Generate release notes with `invoke generate-release-notes --version 1.4.2` and answer `yes` to the prompt `Is it okay if I remove those files? [Y/n]:`. This will update the release notes in `docs/admin/release_notes/version_1.4.md`, stage that file in git, and `git rm` all the fragments that have now been incorporated into the release notes.

Check the git diff to verify the changes are correct (`git diff --cached`).

Commit and push the staged changes.

### Submit Release Pull Request

Submit a pull request to merge your release branch into `develop`. Once merged, submit another pull request titled `**"Release vX.Y.Z"**` to merge the `develop` branch into `main`. Copy the documented release notes into the pull request's body.

Once CI has completed on the PR, merge it.

!!! important
    Do not squash merge this branch into `main`. Make sure to select `Create a merge commit` when merging in GitHub.

### Create a New Release in GitHub

Draft a [new release](https://github.com/nautobot/nautobot-app-dev-example/releases/new) with the following parameters.

* **Tag:** Current version (e.g. `v1.4.2`)
* **Target:** `main`
* **Title:** Version and date (e.g. `v1.4.2 - 2024-04-02`)

Click "Generate Release Notes" and keep the `Full Changelog` section (delete everything else). Copy the description from the pull request to the release.

### Create a PR from `main` back to `develop`

Create a new branch from `main` called `release-1.4.2-to-develop` and use `poetry version prepatch` to bump the development version to the next release.

For example, if you just released `v1.4.2`:

```no-highlight
> git switch -c release-1.4.2-to-develop main
Switched to a new branch 'release-1.4.2-to-develop'

> poetry version prepatch
Bumping version from 1.4.2 to 1.4.3a1
```

Open a new PR from `release-1.4.2-to-develop` against `develop`, wait for CI to pass, and merge it.

!!! important
    Do not squash merge this branch into `develop`. Make sure to select `Create a merge commit` when merging in GitHub.
