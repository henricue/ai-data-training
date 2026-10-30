# Harjoitus 3: Visualisointien laatiminen

Tutkimuskysymys:

> Missä verkko pätkii?

## Tehtävä

1. Laadi selaimeen aukeava kuvaaja olennaisista muuttujista
2. Tee kuvaajasta interaktiivinen
3. Tyylittele sovellus ja kuvaajat DNA:n brändivärien mukaisesti
4. Huolehdi, että kuvaajissa näkyvät selkeät otsikot, yksiköt ja lähteet

Käytä toteutukseen Streamlitiä ja Plotlyä. Nykyinen aineisto sisältää yhden
kuukauden, joten voit toteuttaa porautumisen esimerkiksi valitun
kunnan operaattorikohtaiseen näkymään.

## Vinkki

Käynnistä sreamlit-sovellus:

```bash
streamlit run polku/tiedostoon.py
```

## Bonustehtävä: Maantieteellinen esittäminen

1. Lataa kuntien hallinnolliset rajat koneellesi
   - [paikkatietoikkuna](https://www.paikkatietohakemisto.fi/geonetwork/srv/api/records/b4693808-0f3b-4d5e-b366-c410b680ac19?language=all)
2. Muuta tämän tehtävän visualisointi paikkatietomuotoon
   - Saatko sekä verkon nopeuden että asukasluvun esitettyä samassa kuvassa?
