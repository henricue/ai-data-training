# Harjoitus 6: Raportointi

Tutkimuskysymys:

> Miten sää vaikuttaa kaupunkipyörien kysyntään?

## Tehtävä

1. Laadi johdolle raportti analyysin keskeisistä tuloksista. Sisällytä raporttiin
   johdanto, toimenpidesuositus, perustelut, menetelmät ja liitteet.
2. Tuota raportista diaesitysmuotoinen PDF Typstillä. Säilytä myös raportin
   `.typ`-lähdetiedosto.
3. Tyylittele raportti [HSL:n tyylioppaan](https://tyyliopas.hsl.fi) mukaisesti.
4. Pyydä agenttia arvioimaan raportti
   [REPORT_REVIEW_TEMPLATE.md](REPORT_REVIEW_TEMPLATE.md)-pohjan avulla.
5. Korjaa raportin tärkeimmät puutteet ja tarkista valmis PDF sivu sivulta.

Hyödynnä aiempien harjoitusten analyysejä, malleja ja visualisointeja. Tallenna
lopputulokset esimerkiksi näin:

```text
reports/
├── management_report.typ
├── management_report.pdf
└── report_review.md
```

Kun olet aktivoinut virtuaaliympäristön, voit kääntää raportin komennolla:

```bash
typst compile reports/management_report.typ reports/management_report.pdf
```
