# Data: liikenneonnettomuudet Helsingissä

`onnettomuudet.csv` on Helsingin kaupungin avoin aineisto liikenneonnettomuuksista
vuosilta 2000–2025. Tiedostoa ei muokata; käsitelty tulos syntyy tiedostoon
`public/report.json`.

- Lähde: Helsingin kaupunki, Liikenneonnettomuudet Helsingissä,
  https://www.hel.fi/static/avoindata/kymp/liikenneonnettomuudet_Helsingissa.csv
- Lisenssi: CC BY 4.0 (mainitse lähde, kun käytät tai julkaiset tuloksia)
- Ladattu: 12.11.2026
- Muoto: puolipisteellä erotettu CSV, 54 496 riviä, yksi rivi = yksi onnettomuus

## Sarakkeet

| Sarake | Merkitys |
|---|---|
| `LAJI` | Onnettomuuslaji heikoimman osallisen mukaan: `MA` moottoriajoneuvo, `PP` polkupyörä, `JK` jalankulkija, `MP` mopo tai moottoripyörä |
| `pohj_etrs` | Pohjoiskoordinaatti, ETRS-GK25 (EPSG:3879) |
| `ita_etrs` | Itäkoordinaatti, ETRS-GK25 (EPSG:3879) |
| `VAKAV_A` | Vakavuus: `1` = vain omaisuusvahinkoja, `2` = johti loukkaantumiseen tai kuolemaan |
| `VV` | Vuosi |

Esimerkkirivit:

```
LAJI;pohj_etrs;ita_etrs;VAKAV_A;VV
JK;6675786.73;25501661.91;1;2022
JK;6674533.32;25502790.94;2;2022
MA;6675802.54;25494566.15;2;2025
```

## Tunnetut luvut tarkistusta varten

- Koko aineistossa 11 504 / 54 496 onnettomuutta (21 %) johti loukkaantumiseen tai kuolemaan.
- Vuonna 2024 onnettomuuksia oli 755, joista 289 johti loukkaantumiseen tai kuolemaan.

## Tiedossa olevat rajoitukset

- Lähteen mukaan rekisteri on täysin kattava vain kuolemantapausten osalta. Puutteita on
  erityisesti lievissä henkilövahingoissa sekä jalankulkija-, pyörä- ja mopo-onnettomuuksissa.
- Onnettomuuksien kokonaismäärä putoaa 1 718:sta (2019) 905:een (2020). Pudotus on lähes
  kokonaan omaisuusvahinkoja; syytä (esim. kirjaamistavan muutos) ei ole selvitetty.
- Datassa ei ole katujen nimiä, risteyksiä eikä päivämääriä, vain koordinaatit ja vuosi.
- Muutamalta riviltä puuttuvat koordinaatit.
