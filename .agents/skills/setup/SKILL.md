---
name: setup
description: Set up and verify this training repository on Windows or macOS. Use when a participant asks to install, initialize, repair, or check the course environment.
---

# Set up the training environment

Prepare the repository for the exercises without requiring the participant to
know platform-specific commands.

## Before changing anything

1. Work from the repository root containing `pyproject.toml` and
   `scripts/setup.py`.
2. Read `scripts/setup.py` and `pyproject.toml`. The script is the canonical,
   cross-platform setup path; do not replace it with hand-written steps.
3. Detect the operating system. Support Windows and macOS. On another system,
   explain that this skill currently supports only those platforms and point
   the participant to `scripts/setup.py`.
4. Confirm that a Python 3.11 or newer interpreter is available. On Windows,
   prefer the `py` launcher and fall back to `python`. On macOS, prefer
   `python3`. If no suitable interpreter exists, stop and give a concise
   installation instruction (Windows: Microsoft Store or python.org with
   "Install for current user", no administrator rights needed); do not
   install Python automatically.

## Install

Run the installation in a background terminal when the current surface
supports it, but wait for it to finish before reporting success. Respect all
approval and network-access prompts.

Reuse an existing `.venv`; do not delete it. The script creates it only when
its Python executable is missing.

- Windows: `py scripts/setup.py` (or `python scripts/setup.py`)
- macOS: `python3 scripts/setup.py` (`make setup` does the same)

`make` is not required, and no administrator rights are needed. Do not install
anything globally and do not edit PowerShell execution policy.

## Verify and report

Verify using the executable inside `.venv`:

- Windows: `py scripts/setup.py --verify`
- macOS: `python3 scripts/setup.py --verify`

The check imports pandas, plotly, and streamlit from `.venv` and prints their
versions.

Do not run the Makefile's `data` target during environment setup. It references
`scripts/prepare_data.py`, which belongs to a later exercise state, and setup
must not modify training data.

If a step fails, preserve the existing environment and report the failed
command and a short diagnosis. Do not claim partial setup succeeded.

On success, report the detected platform, Python version, and the pandas,
plotly, and streamlit versions. Explain that activation is optional: commands
can be run directly with the environment's Python, which also works when
PowerShell blocks the activation script:

- Windows: `.venv\Scripts\python -m streamlit run harjoitukset/03-visualisoinnit/app.py`
- macOS: `.venv/bin/python -m streamlit run harjoitukset/03-visualisoinnit/app.py`

Optional activation:

- Windows PowerShell: `.\.venv\Scripts\Activate.ps1` (may require a permissive
  execution policy; the direct commands above avoid this)
- macOS: `source .venv/bin/activate`
