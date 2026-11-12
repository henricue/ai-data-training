"""Laskee onnettomuusraportin datasta ja tallentaa sen tiedostoon public/report.json."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "onnettomuudet.csv"
OUTPUT_FILE = ROOT / "public" / "report.json"

TYPE_LABELS = {
    "MA": "Moottoriajoneuvo",
    "PP": "Polkupyörä",
    "JK": "Jalankulkija",
    "MP": "Mopo tai moottoripyörä",
}
# VAKAV_A: 1 = vain omaisuusvahinkoja, 2 = loukkaantuminen tai kuolema (data/README.md)
INJURY = "2"


def read_rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter=";"))


def parse_location(row):
    """Palauttaa sijainnin (pohjoinen, itä) tai None, jos koordinaatti puuttuu."""
    if not row["pohj_etrs"].strip() or not row["ita_etrs"].strip():
        return None
    return float(row["pohj_etrs"]), float(row["ita_etrs"])


def build_report(rows):
    """Palauttaa raportin ja niiden rivien määrän, joilta puuttuu koordinaatti."""
    totals_by_year, injuries_by_year = Counter(), Counter()
    totals_by_type, injuries_by_type = Counter(), Counter()
    locations = []  # alueellinen tarkastelu, backlog 0004
    missing_location = 0

    for row in rows:
        location = parse_location(row)
        if location is None:
            missing_location += 1
        else:
            locations.append(location)

        year, accident_type = int(row["VV"]), row["LAJI"]
        totals_by_year[year] += 1
        totals_by_type[accident_type] += 1
        if row["VAKAV_A"] == INJURY:
            injuries_by_year[year] += 1
            injuries_by_type[accident_type] += 1

    report = {
        "title": "Liikenneonnettomuudet Helsingissä",
        "source": "Helsingin kaupunki, Liikenneonnettomuudet Helsingissä",
        "license": "CC BY 4.0",
        "years": [
            {"year": year, "total": totals_by_year[year], "injury": injuries_by_year[year]}
            for year in sorted(totals_by_year)
        ],
        "by_type": [
            {"code": code, "label": label, "total": totals_by_type[code], "injury": injuries_by_type[code]}
            for code, label in TYPE_LABELS.items()
        ],
        "injury_share": round(sum(injuries_by_year.values()) / len(rows), 4),
    }
    return report, missing_location


def main():
    rows = read_rows(DATA_FILE)
    report, missing_location = build_report(rows)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"Raportti kirjoitettu: {OUTPUT_FILE.relative_to(ROOT)} ({len(rows)} riviä)")
    if missing_location:
        print(f"Sijaintitiedoista ohitettu {missing_location} riviä, joilta puuttuu koordinaatti "
              "(ne lasketaan silti mukaan määriin).")


if __name__ == "__main__":
    main()
