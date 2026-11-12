# 🚦 Onnettomuusraportti – Helsingin liikenneturvallisuus datan valossa

Tervetuloa Onnettomuusraportti-projektiin! Tämä projekti on kattava, moderni ja helppokäyttöinen
ratkaisu Helsingin liikenneonnettomuuksien analysointiin ja visualisointiin. Projektin avulla
kuka tahansa voi saada nopeasti ja vaivattomasti arvokkaita näkemyksiä liikenneturvallisuudesta.

## 📌 Sisällysluettelo

1. Johdanto
2. Projektin tausta
3. Ominaisuudet
4. Arkkitehtuuri
5. Asennus
6. Käyttö
7. Ajaminen
8. Data
9. Hakemistorakenne
10. Usein kysytyt kysymykset
11. Tulevaisuuden visio
12. Kiitokset

## 1. Johdanto

Liikenneturvallisuus on tärkeä asia. Onnettomuuksien ymmärtäminen auttaa tekemään parempia
päätöksiä. Tämä projekti auttaa ymmärtämään onnettomuuksia datan avulla. Data on tärkeää, ja
siksi tämä projekti hyödyntää dataa monipuolisesti.

Projektin tavoitteena on tarjota selkeä, luotettava ja visuaalisesti miellyttävä näkymä
Helsingin liikenneonnettomuuksiin. Raportti on suunniteltu sekä asiantuntijoille että
satunnaisille käyttäjille.

## 2. Projektin tausta

Projekti sai alkunsa tarpeesta ymmärtää paremmin liikenneonnettomuuksia. Aiemmin tieto oli
hajallaan, ja sen kokoaminen vei aikaa. Nyt kaikki tieto on yhdessä paikassa.

Data kattaa vuodet 2000–2023, ja se päivitetään kerran vuodessa. Raportti näyttää kaikki
poliisin tietoon tulleet onnettomuudet.

## 3. Ominaisuudet

- ✅ Onnettomuuksien määrä vuosittain
- ✅ Onnettomuudet lajeittain
- ✅ Loukkaantumiseen tai kuolemaan johtaneiden onnettomuuksien osuus
- ✅ Interaktiivinen vuosikaavio
- ✅ Lajisuodatin URL-parametrilla
- ✅ Nopea ja kevyt
- ✅ Ei riippuvuuksia
- ✅ Toimii kaikilla moderneilla selaimilla
- ✅ Helppo laajentaa

## 4. Arkkitehtuuri

Projekti noudattaa modernia, kerroksellista arkkitehtuuria:

1. **Datakerros:** `data/onnettomuudet.csv` sisältää lähdeaineiston.
2. **Käsittelykerros:** `backend/build_report.py` lukee datan ja laskee raportin.
3. **Rajapintakerros:** `public/report.json` toimii rajapintana backendin ja frontendin välillä.
4. **Esityskerros:** `public/index.html` ja `public/app.js` näyttävät raportin selaimessa.

Tämä arkkitehtuuri mahdollistaa kerrosten itsenäisen kehittämisen, testaamisen ja
skaalaamisen. Kerrokset ovat löyhästi kytkettyjä, mikä tekee järjestelmästä joustavan.

## 5. Asennus

Projekti ei vaadi asennuksia. Tarvitset vain Pythonin (versio 3.11 tai uudempi) ja selaimen.

Tarkista Python-versio:

```
python3 --version
```

Windowsissa komento on `python --version` tai `py --version`.

## 6. Käyttö

Laske raportti:

```
python3 backend/build_report.py
```

Käynnistä palvelin:

```
python3 -m http.server --bind 127.0.0.1 --directory public 8000
```

Avaa selaimessa http://localhost:8000.

## 7. Ajaminen

Raportin ajaminen tapahtuu kahdessa vaiheessa. Ensin lasketaan raportti:

```
python3 backend/build_report.py
```

Sitten käynnistetään palvelin:

```
python3 -m http.server --bind 127.0.0.1 --directory public 8000
```

Lopuksi avataan selaimessa osoite http://localhost:8000.

## 8. Data

Data on peräisin Helsingin kaupungin avoimesta datasta. Lisätietoja datasta löytyy
tiedostosta `data/README.md`. Data on julkaistu lisenssillä CC BY 4.0.

## 9. Hakemistorakenne

```
.
├── AGENTS.md
├── PROJECT.md
├── README.md
├── backend/
│   └── build_report.py
├── backlog/
├── data/
│   ├── README.md
│   └── onnettomuudet.csv
├── public/
│   ├── app.js
│   ├── index.html
│   └── report.json
└── toimeksiannot/
```

## 10. Usein kysytyt kysymykset

**Miksi sivu ei aukea, kun avaan index.html-tiedoston suoraan?**
Selain ei lataa `report.json`-tiedostoa suoraan tiedostojärjestelmästä. Käynnistä palvelin
kohdan 7 ohjeiden mukaan.

**Voinko käyttää omaa dataani?**
Kyllä, kunhan data on samassa muodossa.

**Onko projekti valmis?**
Projekti kehittyy jatkuvasti.

## 11. Tulevaisuuden visio

Tulevaisuudessa projektista voi kasvaa kattava liikenneturvallisuusalusta, joka hyödyntää
tekoälyä, reaaliaikaista dataa ja edistyneitä visualisointeja. Mahdollisia laajennuksia ovat
esimerkiksi interaktiivinen kartta, ennustemallit, mobiilisovellus ja integraatiot muihin
järjestelmiin. Visiona on tehdä liikenneturvallisuusdatasta kaikkien saatavilla olevaa.

## 12. Kiitokset

Kiitos kaikille projektiin osallistuneille ja Helsingin kaupungille avoimesta datasta! 🙏
