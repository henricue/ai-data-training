# Harjoitus 1: Datan lataus ja esikäsittely

Tutkimuskysymys:

> Missä verkko pätkii?

## Tehtävä

1. Pyydä agenttia lataamaan tarvittava data:
   - [Bittimittarin tulokset 09/2026](https://opendata.traficom.fi/Content/Bittimittari/Bittimittari-2026-09.zip)
   - [Kuntien väestötiedot](https://pxdata.stat.fi/PxWeb/pxweb/fi/Kuntien_avainluvut/Kuntien_avainluvut__2026/kuntien_avainluvut_2026_viimeisin.px)
2. Yhdistä aineistot yhteen taulukkoon.
3. Tarkista puuttuvat arvot ja aineiston käyttökelpoisuus.
4. Koosta työvaiheista uudelleenajettava Python-skripti.

Noudata [aineistosopimusta](DATA_CONTRACT.md), jotta lopputulos toimii myös
seuraavissa harjoituksissa.

## Lopputulos

Harjoituksen lopussa sinulla tulee olla:

- `scripts/prepare_data.py`
- `data/processed/network_speed.csv`
- skriptin tulostama yhteenveto aineiston laadusta

Tarkista lopuksi, että skriptin voi ajaa uudelleen ja että CSV:ssä on odotetut
sarakkeet ja arvot.
