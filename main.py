# https://repl.it/languages/python3
# verschillende functies kunnen worden aangesproken door onderaan de pagina de "#" weg te halen.

import math
from fractions import Fraction as Frac

a = float(input("Wat is de diameter in cm?"))
rho = float(input("Wat is de rho in kg/m3?"))


def reynolds_number(v):  # berekenen van getal van Reynolds
    viscoAns = str(input("Viscositeit in Pa of mPa? (Pa/mPa)"))
    if viscoAns == "Pa":
        visco = float(input("Wat is de viscositeit in Pa?"))
        re = (v * rho * (a * 10 ** -2)) / visco
    else:
        visco = float(input("Wat is de viscositeit in mPa?"))
        re = (v * rho * (a * 10 ** -2)) / (visco * 10 ** -3)

    print("Reynoldsgetal is ", round(re, 2))
    if re < 2000:
        print("Stroming is laminair")
    elif re > 3000:
        print("Stroming is turbulent")
    elif 2000 > re < 3000:
        print("Stroming is in overgangsgebied")

    return re


def frictie_factor(re):  # Opvragen van frictie factor
    # re = re
    if re > 3000:
        q = str(input("Mag je uit gaan van een wrijvingsloze toestand? (ja/nee) "))
        if q == "ja":
            ff = 0.3164 / re ** Frac(1, 4)
        elif q == "nee":
            q2 = str(input("Valt de frictiefactor af te lezen van het Moody Diagram? (ja/nee)"))
            if q2 == "ja":
                ff = float(input("Wat is de frictie factor?"))
            elif q2 == "nee":
                r = float(input("Wat is de relatieve randruwheid?"))
                ff = 0.25 / math.log10((r/3.7 * a + (5.74 / (re**0.9))))**2  # Swamee-jain vergelijking
    elif re < 2000:
        ff = 64 / re
    print("Frictie factor = ", round(ff, 4))

    return round(ff, 4)


def velocity():  # berekenen van snelheid in m/s
    ans = str(input("volumedebiet in L/min? (ja/nee)"))
    if ans == "ja":
        vb = float(input("Wat is het volumedebiet in L/min?"))
        v = ((vb/60)*10**-3) / ((math.pi / 4) * ((a*10**-2)**2))

    elif ans == "nee":
        vb = float(input("Wat is het volumedebiet in m3/uur?"))
        v = (vb / 3600) / (0.25 * math.pi * ((a*10**-2)**2))
    print("Snelheid =", round(v, 3), "m/s")
    return round(v, 2)


def pressure_loss():  # Berekenen van drukval in leiding.
    v = velocity()
    re = reynolds_number(v)
    l = float(input("Wat is de lengte van de buis in meter?"))

    if re > 3000:
        p = frictie_factor(re) * 0.5 * rho * v**2 * (l / (a*10**-2))
        print("drukval =", p, "Pa" "\t", (p/10**5), "bar")


def pressure_system():  # Berekenen van drukval in leidingsegmenten met appendages
    v = velocity()
    re = reynolds_number(v)
    ff = frictie_factor(re)
    appendages = float(input("Wat is de som van de appendages?"))
    rPipe = float(input("Wat is de weerstand van de leiding?"))
    l = float(input("Wat is de lengte van de leiding in meter?"))

    ploss = (appendages * 0.5 * rho * v**2) + rPipe + ff * 0.5 * rho * v**2 * (l / a)

    print("Totale drukverlies met appendages = ", ploss, "Pa \t", (ploss/10**5), "bar")
    return ploss


def friction_coefficient():
    f = float(input("Wat is de frictie factor?"))
    l = float(input("Wat is de lengte van de buis?"))

    fc = f * (l / (a*10**-2))

    print("Wrijvings coefficient = ", round(fc, 3))
    return round(fc, 3)


# Kies hier welke functies je wilt aanroepen

# reynolds_number() # Getal van reynolds berekenen
# frictie_factor(22382)  # Frictie factor berekenen of invoeren.
# velocity() #  snelheid berekenen
pressure_loss()  # Drukval in leiding berekenen
# pressure_system()  # Drukval door compleet leidingsegment berekenen.
# friction_coefficient()  # Wrijvings coefficient berekenen.
# Press the green button in the gutter to run the script.
# Copyright (C) 2020  Valentijn Kilian
