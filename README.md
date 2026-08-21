# Agenttinen koodaus data-analyytikoille

Tämä repositorio toimii agenttisen koodauksen koulutuksen työympäristönä. Jokainen harjoitus on omassa hakemistossaan.

## Harjoitukset

- [Harjoitus 1: Peruskäyttö](harjoitukset/01-munakello/README.md)
- [Harjoitus 2: Datan lataus ja esikäsittely](harjoitukset/02-datan-esikasittely/README.md)
- [Harjoitus 3: Eksploratiivinen analyysi](harjoitukset/03-eksploratiivinen-analyysi/README.md)
- [Harjoitus 4: Visualisointien laatiminen](harjoitukset/04-visualisoinnit/README.md)
- [Harjoitus 5: Tilastollisten mallien laatiminen](harjoitukset/05-tilastolliset-mallit/README.md)
- [Harjoitus 6: Raportointi](harjoitukset/06-raportointi/README.md)

Harjoituksissa 2–6 tutkitaan kysymystä:

> Miten sää vaikuttaa kaupunkipyörien kysyntään?

## Käyttöönotto

### 1. Kloonaa repositorio

Kloonaa repositorio ja siirry sen hakemistoon:

```bash
git clone https://github.com/henricue/ai-data-training.git
cd ai-data-training
```

### 2. Avaa repositorio Codexissa ja editorissa

Avaa Codex-sovellus, valitse **Open Folder** ja valitse kloonaamasi
`ai-data-training`-hakemisto.

Avaa hakemisto myös VSCodessa muutosten helpompaa tarkastelua varten:

```bash
code .
```

Voit käyttää myös muuta editoria. Jos komento ei toimi, avaa editori ja valitse
**Open Folder** tai **Avaa kansio**, ja valitse `ai-data-training`-hakemisto.

### 3. Asenna työkalut

Tarvitset Python 3.11:n tai uudemman sekä `make`-komennon. Avaa editorin
terminaali ja suorita:

```bash
make setup
```

Komento luo Python-virtuaaliympäristön ja asentaa harjoituksissa tarvittavat
Python-riippuvuudet sekä Typstin.

### 4. Tarkista asennus

```bash
make verify
```

### 5. Aktivoi ympäristö

Aktivoi virtuaaliympäristö aina, kun aloitat uuden työskentelysession:

```bash
source .venv/bin/activate
```

Typstiä käytetään harjoituksessa 6 diaesitysmuotoisen PDF-raportin
tuottamiseen. Sen erillistä asentamista ei tarvita.
