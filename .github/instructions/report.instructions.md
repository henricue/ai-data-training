---
applyTo: "backend/**,public/**,data/**"
description: "How to build the report and open it in the browser"
---
# Running the report

Run commands from the repository root. Use `python` on Windows (or `py` if
`python` is not found) and `python3` on macOS.

- Show the report in the browser: start the server in the background with
  `python -m http.server --bind 127.0.0.1 --directory public 8000`
  and open http://localhost:8000
- Opening `public/index.html` directly (file://) does not work: the browser
  refuses to load `report.json` from the file system.
- If port 8000 is already in use, use 8001 instead (and http://localhost:8001).
- `public/report.json` is committed. Rebuild it only after changing `data/` or
  `backend/`: `python backend/build_report.py` (reads `data/onnettomuudet.csv`,
  writes `public/report.json`).
