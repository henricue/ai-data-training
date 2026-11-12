# Onnettomuusraportti

Raportti Helsingin liikenneonnettomuuksista selaimessa. Vastaa suomeksi.

- `data/` – lähdeaineisto ja sen kuvaus
- `backend/` – Python-skripti, joka laskee raportin tiedostoon `public/report.json`
- `public/` – selaimessa avattava raporttisivu

## Säännöt
- Tarkista raportin luvut `data/README.md`:n tunnettuja lukuja vasten ennen kuin sanot työn valmiiksi.
- Älä kirjoita URL-parametreja tai datan arvoja sivulle `innerHTML`:llä, käytä `textContent`ia.
- Tehtävät ovat `backlog/`-kansiossa; päivitä tila samassa commitissa kuin työ.
- Älä muuta raakadataa (`data/onnettomuudet.csv`).
