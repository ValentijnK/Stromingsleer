# Stromingsleer
De meeste formules uit het dictaat over de stromingsleer zijn omgezet in dit programma. 

**Verwerkte formules:**
* snelheid in een leiding 
* Kengetal van Reynolds
* Frictiefactoren
* Wrijvingscoëfficïent
* Weerstandswet van Blasius
* Uitgebreide wet van Bernoulli (voor het berekenen van pompdruk en drukval in ronde leidingsegmenten.)



## Hoe gebruik ik het?
Het programma is geschreven in Python. Als je het programma wil draaien moet je een interpreter gebruiken. 

Geen ervaring met programmeren? 
[Klik hier voor een online variant.](https://repl.it/languages/python3) 

Kopieer en plak de inhoud van 'main.py' in deze omgeving en klik op run.

## Functies gebruiken
Onderaan de code is een blok te vinden met verschillende functies. Al deze functies kunnen worden aangeroepen door het '#' teken weg te halen. 

**Let op:** Sommige functies hebben een parameter nodig om te werken. Zie hieronder een voorbeeld.
```` 
# Kies hier welke functies je wilt aanroepen

# reynolds_number(velocity) #Getal van reynolds berekenen. Parameter = snelheid in m/s
frictie_factor(119420) # Frictie factor berekenen of invoeren. Parameter = reynolds getal
# velocity() # snelheid berekenen
# pressure_loss() # Drukval in leiding berekenen
# pressure_system() # Drukval door compleet leidingsegment berekenen met appendages.
# friction_coefficient() # Wrijvings coefficient berekenen
````

## vragen
Vragen of bugs? [Rapporteer](https://github.com/ValentijnK/Stromingsleer/issues) ze hier.

## License
GNU General Public License v3.0