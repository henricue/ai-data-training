"""Laskee onnettomuusraportin datasta ja tallentaa sen tiedostoon public/report.json."""
import csv
import json
from collections import Counter

# Path to the data file
DATA_FILE = "data/onnettomuudet.csv"
# Path to the output file
OUTPUT_FILE = "public/report.json"

TYPE_LABELS = {
    "MA": "Moottoriajoneuvo",
    "PP": "Polkupyörä",
    "JK": "Jalankulkija",
    "MP": "Mopo tai moottoripyörä",
}


class DataSource:
    """Base class for all data sources."""

    def __init__(self, path):
        # Store the path
        self.path = path

    def read(self):
        """Read the data. Subclasses must implement this."""
        raise NotImplementedError


class CsvDataSource(DataSource):
    """A data source that reads CSV files."""

    delimiter = ","

    def read(self):
        # Open the file
        with open(self.path, encoding="utf-8", newline="") as f:
            # Return all rows as dictionaries
            return list(csv.DictReader(f, delimiter=self.delimiter))


class AccidentDataSource(CsvDataSource):
    """A data source for traffic accident data."""

    delimiter = ";"


def format_percentage(value):
    """Format a share between 0 and 1 as a percentage string."""
    return f"{value * 100:.1f} %"


def parse_location(row):
    """Return the accident location as (north, east) coordinates."""
    # Convert the coordinates to numbers
    return float(row["pohj_etrs"]), float(row["ita_etrs"])


def build_report(rows):
    """Build the report dictionary from the rows."""
    totals_by_year = Counter()
    injuries_by_year = Counter()
    totals_by_type = Counter()
    injuries_by_type = Counter()
    locations = []  # TODO: alueellinen tarkastelu (backlog 0004)

    # loop over all rows
    for row in rows:
        year = int(row["VV"])
        accident_type = row["LAJI"]
        # Check if the accident caused an injury
        injury = row["VAKAV_A"] == "1"
        # Read the location
        locations.append(parse_location(row))

        # Increment the totals
        totals_by_year[year] += 1
        totals_by_type[accident_type] += 1
        if injury:
            injuries_by_year[year] += 1
            injuries_by_type[accident_type] += 1

    total = sum(totals_by_year.values())
    return {
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
        "injury_share": round(sum(injuries_by_year.values()) / total, 4),
    }


def main():
    # Create the data source
    source = AccidentDataSource(DATA_FILE)
    # Read the rows
    rows = source.read()
    # Build the report
    report = build_report(rows)
    # Write the report to the output file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"Raportti kirjoitettu: {OUTPUT_FILE} ({len(rows)} riviä)")


if __name__ == "__main__":
    main()
