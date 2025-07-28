#!/usr/bin/env bash

set -e

if [[ -z "$(which python3.11)" ]]; then
  echo "Could not find python 3.11 installed"
else
  echo "Using python3.11 for installation"
  poetry env use "$(which python3.11)"
fi

# install latest dependencies
echo "Installing dependencies"
poetry install --no-root

# check format
echo "Checking ruff formatting"
poetry run ruff check .

echo "Checking Gherkin files formatting"
poetry run reformat-gherkin --check features

# get feature files coverage and create report
echo "Running tests and collecting coverage"
poetry run coverage run -a --source='.' -m behave --format progress
poetry run coverage report --skip-covered --fail-under=95 -m

