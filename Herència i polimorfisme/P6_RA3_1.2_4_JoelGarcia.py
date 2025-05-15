# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_4_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Exemple d'herència amb càlculs geomètrics.
# -----------------------------------------------------------------------------

import math

class Figura:
    def area(self):
        print("Àrea no definida")

class Quadrat(Figura):
    def __init__(self, costat):
        self.costat = costat

    def area(self):
        return self.costat ** 2

class Cercle(Figura):
    def __init__(self, radi):
        self.radi = radi

    def area(self):
        return math.pi * (self.radi ** 2)
