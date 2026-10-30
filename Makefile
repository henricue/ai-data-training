PYTHON ?= python3
VENV_PYTHON := .venv/bin/python

.PHONY: setup verify data

# Windowsilla ilman makea: python scripts/setup.py
setup:
	$(PYTHON) scripts/setup.py

verify:
	$(PYTHON) scripts/setup.py --verify

data:
	$(VENV_PYTHON) scripts/prepare_data.py
