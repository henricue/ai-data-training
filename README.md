# Agenttinen koodaus data-analyytikoille

Tämä repositorio toimii kahden päivän koulutusympäristönä data-analyytikoille,
jotka kokeilevat agenttista koodausta ensimmäisiä kertoja. Harjoituksissa
käytetään Pythonia, pandas-kirjastoa ja HSL:n avointa dataa.

Repo on vasta alkuvaiheessa. Muut harjoitukset, esimerkkidata ja muu
koulutusmateriaali lisätään myöhemmin.

## Harjoitukset

- [Harjoitus 1: Peruskäyttö](harjoitukset/01-munakello/README.md)

## Koulutuksen runko

### 1. aamupäivä

- Aamupala ja avaus
- Esitys: AI-työkalujen käytön perusperiaatteet ja hyödyt
- Harjoitus 1: AI:n peruskäyttö ja eri moodit
- Harjoitus 2: Datan lataus ja esikäsittely
- Demo: Itsepalveluanalytiikka
- Harjoitus 3: Eksploratiivinen analyysi
- Lopetus: Reaktorin opit eri projekteista ja päivän kertaus

### 2. aamupäivä

- Aamupala ja avaus
- Esitys: Laadunvarmistus ja miltä uusi arki näyttää
- Harjoitus 4: Visualisointien laatiminen
- Harjoitus 5: Tilastollisten mallien teko
- Demo: Usean agentin käyttö rinnakkain
- Harjoitus 6: Raportointi
- Lopetus: Päivän kertaus ja itsenäisen oppimisen jatkaminen

Jokainen harjoitus alkaa ohjeistuksella ja päättyy yhteiseen yhteenvetoon.
Harjoitukset suunnitellaan siten, että osallistuja voi tarvittaessa osallistua
vain osaan päivän ohjelmasta.

## Käyttöönotto

Tarvitset Python 3.11:n tai uudemman sekä `make`-komennon.

Luo virtuaaliympäristö ja asenna riippuvuudet:

```bash
make setup
```

Tarkista asennus:

```bash
make verify
```

Aktivoi ympäristö omaa työskentelyä varten:

```bash
source .venv/bin/activate
```

## Data

Koulutuksessa käytettävä aineisto valitaan HSL:n avoimista aineistoista.
Aineiston lähde, käyttöehdot ja käsittelyvaiheet dokumentoidaan ennen sen
lisäämistä repoon. Lisätietoja on [HSL:n avoimen datan sivulla](https://www.hsl.fi/hsl/avoin-data).
