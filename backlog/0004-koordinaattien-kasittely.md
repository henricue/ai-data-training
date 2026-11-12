---
status: done
---
# Koordinaattien käsittely alueellista tarkastelua varten

Lue onnettomuuksien koordinaatit, jotta raporttiin voi myöhemmin lisätä alueellisen tarkastelun.

## Notes
- 2026-11-06: aloitin `parse_location`-funktion, mutta jätin sen kesken. Tuloksia ei vielä
  käytetä, eikä raporttia ole ajettu uudelleen. Jatka vasta, kun 0005 on tehty.
- 2026-11-17: korjattu. Koordinaatit luetaan, ja kolmelta riviltä puuttuva koordinaatti
  ohitetaan. Varsinainen alueellinen tarkastelu on erillinen tehtävä.
