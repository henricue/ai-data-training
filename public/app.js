// Lataa report.json ja piirtää raportin sivulle.

const SVG_NS = "http://www.w3.org/2000/svg";

function formatNumber(value) {
  return value.toLocaleString("fi-FI");
}

function showKpis(report) {
  const total = report.years.reduce((sum, year) => sum + year.total, 0);
  document.getElementById("kpi-total").textContent = formatNumber(total);
  document.getElementById("kpi-injury-share").textContent = Math.round(report.injury_share * 100) + " %";
}

function drawYears(report) {
  const svg = document.getElementById("years");
  const width = 900, height = 300, left = 40, bottom = 24;
  const max = Math.max(...report.years.map(year => year.total));
  const step = (width - left) / report.years.length;
  const y = value => height - bottom - (value / max) * (height - bottom - 10);

  report.years.forEach((year, i) => {
    const x = left + i * step + 2;
    for (const [value, color] of [[year.total, "#c9d6e8"], [year.injury, "#2a78d6"]]) {
      const bar = document.createElementNS(SVG_NS, "rect");
      bar.setAttribute("x", x);
      bar.setAttribute("y", y(value));
      bar.setAttribute("width", step - 4);
      bar.setAttribute("height", y(0) - y(value));
      bar.setAttribute("fill", color);
      const title = document.createElementNS(SVG_NS, "title");
      title.textContent = `${year.year}: ${formatNumber(year.total)} onnettomuutta, joista ${formatNumber(year.injury)} johti loukkaantumiseen tai kuolemaan`;
      bar.append(title);
      svg.append(bar);
    }
    if (i % 5 === 0 || i === report.years.length - 1) {
      const label = document.createElementNS(SVG_NS, "text");
      label.setAttribute("x", x + (step - 4) / 2);
      label.setAttribute("y", height - 6);
      label.setAttribute("text-anchor", "middle");
      label.setAttribute("font-size", "12");
      label.setAttribute("fill", "#57606a");
      label.textContent = year.year;
      svg.append(label);
    }
  });
}

function showTypes(report) {
  // Lajin voi valita linkillä, esim. ?laji=PP
  const laji = new URLSearchParams(location.search).get("laji");
  const match = laji && report.by_type.find(type => type.code === laji.toUpperCase());
  const types = match ? [match] : report.by_type;

  if (laji) {
    const selected = document.getElementById("selected");
    selected.innerHTML = "Valittu laji: " + (match ? match.label : laji);
    selected.hidden = false;
  }

  const body = document.querySelector("#types tbody");
  for (const type of types) {
    const row = document.createElement("tr");
    for (const value of [type.label, formatNumber(type.total), formatNumber(type.injury)]) {
      const cell = document.createElement("td");
      cell.textContent = value;
      row.append(cell);
    }
    body.append(row);
  }
}

async function main() {
  try {
    const response = await fetch("./report.json");
    const report = await response.json();
    showKpis(report);
    drawYears(report);
    showTypes(report);
  } catch (error) {
    const message = document.getElementById("message");
    message.textContent = "Raporttia ei voitu ladata. Avaa sivu palvelimen kautta: http://localhost:8000 (ks. .github/instructions/report.instructions.md).";
    message.hidden = false;
  }
}

main();
