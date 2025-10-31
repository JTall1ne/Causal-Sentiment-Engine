# Contributing to Causal-Sentiment-Engine

Thank you for considering contributing! Pull requests are welcome. By participating, you agree to abide by our Code of Conduct.

## Getting Started

- Fork the repository and create your feature branch (`git checkout -b feat/your-feature`).
- Install dependencies and the package in editable mode using `pip install -e .`.
- Copy `.env.template` to `.env` and set the required API keys and tokens.
- Run the test suite with `pytest` to ensure your changes don’t break existing functionality.
- Run linters (such as `ruff` or `flake8`) to check code style. Use `black` to format code if applicable.

## Development Guidelines

- Write clear and concise commit messages following the Conventional Commits format.
- Add tests for any new functionality or bug fixes.
- Document public functions and classes with docstrings.
- Do not include API keys or credentials in your code; use environment variables instead.
- For new models or datasets, ensure licensing and usage rights are compatible with this project.

## Pull Requests

- Submit your pull request against the `develop` or a feature branch.
- Describe your changes and the motivation in the PR description.
- Link to any related issues.
- Ensure CI checks pass before requesting review.

## Code of Conduct

This project adheres to the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this standard.
