"""Luo virtuaaliympäristön ja asentaa riippuvuudet. Toimii macOS:llä, Linuxilla ja Windowsilla.

Käyttö:
    python scripts/setup.py            asenna
    python scripts/setup.py --verify   tarkista asennus
"""

import subprocess
import sys
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV = ROOT / ".venv"
VENV_PYTHON = VENV / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")


def setup() -> None:
    if sys.version_info < (3, 11):
        sys.exit(f"Python 3.11 tai uudempi vaaditaan, nyt {sys.version.split()[0]}.")
    if not VENV_PYTHON.exists():
        print(f"Luodaan virtuaaliympäristö: {VENV}")
        venv.create(VENV, with_pip=True)
    subprocess.run(
        [str(VENV_PYTHON), "-m", "pip", "install", "--upgrade", "pip"], check=True
    )
    subprocess.run(
        [str(VENV_PYTHON), "-m", "pip", "install", "-e", str(ROOT)], check=True
    )
    print("Valmis. Tarkista asennus: python scripts/setup.py --verify")


def verify() -> None:
    code = (
        "import pandas, plotly, streamlit; "
        "print(f'pandas {pandas.__version__}, plotly {plotly.__version__}, "
        "streamlit {streamlit.__version__} toimivat')"
    )
    subprocess.run([str(VENV_PYTHON), "-c", code], check=True)


if __name__ == "__main__":
    verify() if "--verify" in sys.argv else setup()
