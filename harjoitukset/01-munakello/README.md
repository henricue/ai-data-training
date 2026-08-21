# Harjoitus 1: Peruskäyttö

Tässä harjoituksessa rakennat agentin avulla selaimessa toimivan munakellon.
Harjoituksen tärkein tavoite ei ole itse sovellus vaan agentin kanssa
työskentelyn perusprosessi: vaatimukset, speksin tarkennus, suunnitelma,
toteutus ja tarkistus.

## Oppimistavoitteet

Harjoituksen jälkeen osaat:

- antaa agentille tehtävän vaatimukset
- pyytää agenttia tunnistamaan speksin epäselvät kohdat
- tarkentaa ja tallentaa speksin
- pyytää toteutussuunnitelman ja tallentaa sen tiedostoon
- jatkaa työtä uudessa sessiossa tiedostoihin tallennetun kontekstin avulla
- pyytää agentilta apua ongelmatilanteessa
- tarkistaa toteutuksen vaatimuksia vasten

## Tehtävä

Luo selaimessa toimiva munakello.

- Sovelluksen kaikki HTML, CSS ja JavaScript ovat yhdessä `index.html`-tiedostossa.
- Sovelluksessa on kolme nappia: Start, Pause ja Reset.
- Käyttäjä voi säätää kellon kestoa.
- Ulkoisia kirjastoja ei käytetä.

Tarkemmat lähtövaatimukset ovat tiedostossa [SPEC.md](SPEC.md).

## Työvaiheet

### 1. Tutustu speksiin

Pyydä agenttia lukemaan `SPEC.md` ja etsimään siitä epäselviä kohtia. Pyydä
sitä olemaan vielä toteuttamatta sovellusta.

Voit aloittaa esimerkiksi näin:

> Lue tämän hakemiston SPEC.md. Älä toteuta sovellusta vielä. Kerro, mitkä
> vaatimukset ovat epäselviä, ja kysy minulta enintään viisi tarkentavaa
> kysymystä.

### 2. Tarkenna speksiä

Vastaa agentin kysymyksiin ja pyydä sitä päivittämään `SPEC.md` päätöstesi
perusteella. Tarkista itse, että päivitetty tiedosto vastaa ajatustasi.

### 3. Tee suunnitelma

Pyydä agenttia laatimaan toteutussuunnitelma, mutta älä anna sen vielä
kirjoittaa sovellusta. Pyydä tallentamaan suunnitelma tämän hakemiston
`PLAN.md`-tiedostoon.

Voit käyttää esimerkiksi tätä kehotetta:

> Laadi päivitetyn SPEC.md:n pohjalta toteutussuunnitelma. Älä implementoi
> vielä. Tallenna suunnitelma tiedostoon PLAN.md.

### 4. Ota uusi sessio ja toteuta

Avaa agentin kanssa uusi sessio. Uusi sessio ei tunne aiempaa keskustelua,
joten ohjaa agentti tiedostoihin tallennetun kontekstin äärelle:

> Lue tämän hakemiston SPEC.md ja PLAN.md. Toteuta suunnitelma tiedostoon
> index.html. Tarkista lopuksi toteutus vaatimuksia vasten.

### 5. Kokeile selaimessa

Avaa `index.html` selaimessa ja kokeile ainakin seuraavat asiat:

- Kestoa voi säätää.
- Start käynnistää kellon.
- Pause pysäyttää kellon ja siitä voi jatkaa.
- Reset toimii sovitulla tavalla.
- Ajan päättyminen toimii speksin mukaisesti.
- Napin painaminen useita kertoja ei riko kelloa.

Jos jokin ei toimi, kuvaile havainto agentille mahdollisimman täsmällisesti ja
pyydä sitä selvittämään syy.

### 6. Tee yksi jatkokehitys

Kun perusversio toimii, valitse yksi pieni parannus. Voit esimerkiksi:

- muuttaa värejä
- lisätä merkkiäänen
- lisätä valmiita kestovalintoja
- parantaa näppäimistökäyttöä

Kerro agentille haluttu lopputulos ennen kuin pyydät muutosta. Tarkista myös,
että alkuperäiset toiminnot toimivat edelleen.

## Valmis, kun

- `SPEC.md` sisältää harjoituksen aikana tekemäsi päätökset
- `PLAN.md` sisältää toteutussuunnitelman
- `index.html` toimii selaimessa ilman asennuksia tai käännösvaihetta
- sovellus täyttää speksin vaatimukset
- olet testannut sovelluksen itse
