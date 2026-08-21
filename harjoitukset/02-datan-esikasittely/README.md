# Harjoitus 2: Datan lataus ja esikäsittely

Tutkimuskysymys:

> Miten sää vaikuttaa kaupunkipyörien kysyntään?

## Tehtävä

1. Pyydä agenttia lataamaan tarvittava data:
   - [HSL:n avoin data](https://www.hsl.fi/hsl/avoin-data)
   - [Ilmatieteen laitoksen säähavainnot](https://opendata.fmi.fi/wfs?request=GetCapabilities)
2. Yhdistä aineistot päivätasolla.
3. Tarkista puuttuvat arvot ja aineiston käyttökelpoisuus.
4. Koosta työvaiheista uudelleenajettava Python-skripti.

Noudata [aineistosopimusta](DATA_CONTRACT.md), jotta lopputulos toimii myös
seuraavissa harjoituksissa.

## Lopputulos

Harjoituksen lopussa sinulla tulee olla:

- `scripts/prepare_data.py`
- `data/processed/citybike_weather_daily.csv`
- skriptin tulostama yhteenveto aineiston laadusta

Tarkista lopuksi, että skriptin voi ajaa uudelleen ja että CSV:ssä on odotetut
sarakkeet, päivämäärät ja arvot.
