PYTHON ?= python3
VENV := .venv
VENV_PYTHON := $(VENV)/bin/python
TYPST := $(VENV)/bin/typst
TYPST_VERSION ?= 0.15.1

.PHONY: setup verify data

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV_PYTHON) -m pip install -e .
	bash scripts/install_typst.sh $(TYPST) $(TYPST_VERSION)

verify:
	$(VENV_PYTHON) -c "import pandas as pd; print(f'pandas {pd.__version__} toimii')"
	$(TYPST) --version

data:
	$(VENV_PYTHON) scripts/prepare_data.py
