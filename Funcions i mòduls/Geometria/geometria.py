# geometria.py
# Autor: Joel Garcia
# Descripció: Mòdul amb funcions per calcular àrees de figures geomètriques

import math

def area_quadrat(costat):
    return costat ** 2

def area_cercle(radi):
    return math.pi * radi ** 2

def area_rectangle(base, altura):
    return base * altura
