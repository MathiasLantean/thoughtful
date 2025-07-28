# FDE Technical Screen

## ⚙️ Requirements for running locally

### 🐍 Python

Make sure you have Python installed.  
I recommend installing it manually from the [official Python website](https://www.python.org/downloads/).

> Check the `pyproject.toml` file to confirm the exact Python version required (e.g. `3.11`).

### 📦 Poetry

This project uses [Poetry](https://python-poetry.org/) for dependency management and packaging.


## 💻 Installation

To install the project locally, the easiest way is to run the build script located in the project root directory.

The build script takes care of installing all the project dependencies, running tests, performing code validation,
and running linters.

```shell
./build.sh
```

## 🤖 Use of LLM (Large Language Model)

The solution and its test were implemented within the time constraints provided.

An LLM (ChatGPT) was used exclusively to:
- Validate test scenarios for the `package_sort` logic using Gherkin syntax
- Double-check that all edge cases and classification branches (standard, special, rejected) were covered
- Write this README file

The core logic, code structure, and implementation were written manually.  
The use of LLM was limited to ensuring completeness in test coverage and avoiding blind spots.

This approach was intended to maintain full ownership of the solution while using available tools responsibly to validate completeness.

## 📄 About This README and Build Script

In the spirit of transparency:  
**The `README.md` and the `build.sh` script were not written during the initial timebox.**  
They were added *after* the core functionality was completed, to improve clarity and usability of the project.

