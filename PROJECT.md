# Onnettomuusraportti

## Tavoite

Selaimessa toimiva raportti Helsingin liikenneonnettomuuksista: kuinka paljon onnettomuuksia
on, miten määrä on kehittynyt ja millaisiin onnettomuuksiin ne liittyvät. Raportista on tarkoitus
tulla pohja myöhemmille kysymyksille, esimerkiksi pyöräilystä ja alueista.

## Tila

- Raportti laskee onnettomuudet vuosittain ja lajeittain (backlog 0001).
- Sivu näyttää tunnusluvut, vuosikaavion ja lajitaulukon (0002) sekä lajisuodattimen (0003).
- Data on päivitetty vuoteen 2025 asti (`data/README.md`).
- Koordinaattien käsittely on aloitettu (0004), mutta se on kesken.

## Päätökset

- Python ilman lisäkirjastoja, jotta raportti toimii kaikilla koneilla ilman asennuksia.
- Backend kirjoittaa tiedoston `public/report.json`, ja sivu lukee sen. Myöhemmin JSON voidaan
  korvata rajapinnalla.
- Raakadataa ei muokata.

## Mistä jatketaan

- Aloitin koordinaattien käsittelyn alueellista tarkastelua varten (backlog 0004).
  Raporttia ei ole ajettu uudelleen tämän muutoksen jälkeen, joten `public/report.json` on vielä
  edellisen ajon tulos.
- Seuraava pieni tehtävä on 0005: lähde ja lisenssi sivun alaosaan.
