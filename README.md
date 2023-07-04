# llm-markov

[![PyPI](https://img.shields.io/pypi/v/llm-markov.svg)](https://pypi.org/project/llm-markov/)
[![Changelog](https://img.shields.io/github/v/release/simonw/llm-markov?include_prereleases&label=changelog)](https://github.com/simonw/llm-markov/releases)
[![Tests](https://github.com/simonw/llm-markov/workflows/Test/badge.svg)](https://github.com/simonw/llm-markov/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/llm-markov/blob/main/LICENSE)

Plugin for [LLM](https://llm.datasette.io/) adding a Markov chain generating model

> ⚠️ This plugin is in development, and will not work until the next release of LLM. See [this PR](https://github.com/simonw/llm/pull/65) for progress.

## Installation

Install this plugin in the same environment as LLM.

    llm install llm-markov

## Usage

This plugin adds a model called `markov`. You can execute it like this:

```bash
llm -m markov "The quick brown fox jumps over the lazy dog"
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd llm-markov
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
