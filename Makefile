PYTHON ?= python3
VENV := .venv
VENV_PYTHON := $(VENV)/bin/python

.PHONY: setup verify data

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV_PYTHON) -m pip install -e .

verify:
	$(VENV_PYTHON) -c "import pandas as pd; print(f'pandas {pd.__version__} toimii')"

data:
	$(VENV_PYTHON) scripts/prepare_data.py
