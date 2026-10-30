# Aineistosopimus

Valmiissa aineistossa on yksi rivi kuntaa ja verkko-operaattoria kohden.
Avain on (`municipality_code`, `operator`).

## Rajaus

- Mittausjakso: syyskuu 2026
- Mittaukset: Traficomin Bittimittari (`Bittimittari-2026-09.csv`)
- Väkiluku: Tilastokeskus, Kuntien avainluvut 2026, tieto `M411`
  (väkiluku 2025)
- Tavoitetiedosto: `data/processed/network_speed.csv`
- Referenssi (oikea vastaus tarkistukseen): `data/reference/network_speed.csv`

## Sarakkeet

| Sarake | Kuvaus |
| --- | --- |
| `municipality_code` | Kuntanumero, kolmimerkkinen teksti (esim. `005`) |
| `municipality` | Kunnan nimi |
| `region` | Maakunta |
| `operator` | Verkko-operaattori (`DNA`, `Elisa`, `Telia`, ...) |
| `measurement_count` | Mittausten lukumäärä ryhmässä |
| `latency_median_ms` | Mediaaniviiveen (`MediaaniViive ms`) mediaani, ms |
| `download_mbps_median` | Latausnopeuden mediaani, Mbit/s |
| `upload_mbps_median` | Lähetysnopeuden mediaani, Mbit/s |
| `population` | Kunnan väkiluku 2025 |

## Käsittelysäännöt

- Lähdetiedosto: erotin `;`, desimaalierotin `,`, merkistö UTF-8 (BOM).
- Rivit, joilta puuttuu kunta tai operaattori, jätetään pois ja niiden määrä
  raportoidaan. Kunta puuttuu esimerkiksi kaikilta selainmittauksilta
  (`Palvelun selainversio`), eikä sitä päätellä viereisiltä riveiltä:
  tyhjiä kenttiä **ei** täytetä edellisen rivin arvolla.
- Ryhmät, joissa on alle 10 mittausta, jätetään pois, koska mediaani on silloin
  epäluotettava.
- Kunnat yhdistetään väkilukuun kunnan nimellä. Yhdistämättä jäävät kunnat
  raportoidaan.
- Tulostiedostossa ei saa olla puuttuvia arvoja eikä kaksoisavaimia.

Raakadata säilytetään muuttamattomana `data/raw`-hakemistossa. Muut
puuttuvien arvojen käsittelyt dokumentoidaan skriptissä tai sen tulosteessa.
