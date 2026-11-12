# Onnettomuusraportti

Selaimessa toimiva raportti Helsingin liikenneonnettomuuksista vuosilta 2000–2025:
onnettomuudet vuosittain ja lajeittain sekä niiden osuus, jotka johtivat loukkaantumiseen
tai kuolemaan.

## Ajaminen

Tarvitset Pythonin 3.11+ (Macissa `python3`, Windowsissa `python` tai `py`) ja selaimen.

```
python backend/build_report.py
python -m http.server --bind 127.0.0.1 --directory public 8000
```

Avaa http://localhost:8000. Sivu ei toimi avattuna suoraan tiedostosta.

## Rakenne

- `data/` – lähdeaineisto; kuvaus, tunnetut luvut ja rajoitukset tiedostossa `data/README.md`
- `backend/build_report.py` – laskee raportin tiedostoon `public/report.json`
- `public/` – raporttisivu
- `backlog/` – tehtävät
- `PROJECT.md` – tavoite, tila ja mistä jatketaan

Data: Helsingin kaupunki, Liikenneonnettomuudet Helsingissä, CC BY 4.0.
