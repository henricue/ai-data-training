# Onnettomuusraportti

## Tavoite

Selaimessa toimiva raportti Helsingin liikenneonnettomuuksista: kuinka paljon onnettomuuksia
on, miten määrä on kehittynyt ja millaisiin onnettomuuksiin ne liittyvät. Raportista on tarkoitus
tulla pohja myöhemmille kysymyksille, esimerkiksi pyöräilystä ja alueista.

## Tila

- Raportti laskee onnettomuudet vuosittain ja lajeittain (backlog 0001).
- Sivu näyttää tunnusluvut, vuosikaavion ja lajitaulukon (0002) sekä lajisuodattimen (0003).
- Data on päivitetty vuoteen 2025 asti (`data/README.md`).
- Koordinaatit luetaan (0004); kolmelta riviltä puuttuva koordinaatti ohitetaan. Alueellinen tarkastelu on vielä tekemättä.
- Luvut on tarkistettu `data/README.md`:n tunnettuja lukuja vasten (0006).

## Päätökset

- Python ilman lisäkirjastoja, jotta raportti toimii kaikilla koneilla ilman asennuksia.
- Backend kirjoittaa tiedoston `public/report.json`, ja sivu lukee sen. Myöhemmin JSON voidaan
  korvata rajapinnalla.
- Raakadataa ei muokata.

## Mistä jatketaan

- Raportti on ajettu uudelleen korjausten jälkeen, ja `public/report.json` on ajan tasalla.
- Seuraavaksi pyöräilykysymys: backlog 0007–0010 (toimeksianto 1).
