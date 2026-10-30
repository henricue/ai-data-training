# Agenttinen koodaus data-analyytikoille

Tämä repositorio toimii agenttisen koodauksen koulutuksen työympäristönä. Jokainen harjoitus on omassa hakemistossaan.

## Harjoitukset

- [Harjoitus 0: Peruskäyttö](harjoitukset/00-warmup-munakello/README.md)
- [Harjoitus 1: Datan lataus ja esikäsittely](harjoitukset/01-datan-esikasittely/README.md)
- [Harjoitus 2: Eksploratiivinen analyysi](harjoitukset/02-eksploratiivinen-analyysi/README.md)
- [Harjoitus 3: Visualisointien laatiminen](harjoitukset/03-visualisoinnit/README.md)

Harjoituksissa 1–X tutkitaan kysymystä:

> Missä verkko pätkii?

## Valmistelut

### 1. Kloonaa repositorio

Avaa PowerShell tai terminaali ja suorita:

```powershell
git clone https://github.com/henricue/ai-data-training.git
cd ai-data-training
```

### 2. Avaa repositorio VSCodessa

Avaa VSCode, valitse **Open Folder** ja valitse kloonaamasi
`ai-data-training`-hakemisto.

Tai vaihtoehtoisesti terminaalissa:

```powershell
code .
```

## Käyttöönotto

Valitse käyttöjärjestelmäsi mukainen ohje:

- [Windows](#windows)
- [macOS / Linux](#macos--linux)

Molemmissa tarvitset Python 3.11:n tai uudemman. Asennus ei vaadi
järjestelmänvalvojan oikeuksia.

## Windows

### 1. Asenna Python

Jos Pythonia ei ole, asenna se Microsoft Storesta tai osoitteesta
python.org (valitse "Install for current user").

### 2. Asenna työkalut

Avaa editorin terminaali ja suorita:

```powershell
py scripts/setup.py
```

Jos `py` ei toimi, käytä komentoa `python scripts/setup.py`. Komento luo
Python-virtuaaliympäristön `.venv` ja asentaa harjoituksissa tarvittavat
riippuvuudet.

### 3. Tarkista asennus

```powershell
py scripts/setup.py --verify
```

### 4. Käytä ympäristöä

Aja komennot suoraan ympäristön Pythonilla. Aktivointia ei tarvita, ja se
toimii myös silloin, kun PowerShell estää aktivointiskriptin:

```powershell
.venv\Scripts\python -m streamlit run harjoitukset/03-visualisoinnit/app.py
```

## macOS / Linux

### 1. Asenna työkalut

Avaa editorin terminaali ja suorita:

```bash
make setup
```

Komento luo Python-virtuaaliympäristön `.venv` ja asentaa harjoituksissa tarvittavat
riippuvuudet.

### 2. Tarkista asennus

```bash
make verify
```

### 3. Käytä ympäristöä

Aktivoi virtuaaliympäristö:

```bash
source .venv/bin/activate
```
