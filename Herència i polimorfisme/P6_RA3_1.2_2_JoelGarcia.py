# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_2_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Exemple d'herència on una subclasse afegeix funcionalitat extra.
# -----------------------------------------------------------------------------

class Vehicle:
    def __init__(self, marca):
        self.marca = marca

    def arrencar(self):
        print(f"El vehicle {self.marca} ha arrencat.")

class Cotxe(Vehicle):
    def tocar_claxon(self):
        print("Pip pip!")
