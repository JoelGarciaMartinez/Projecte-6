# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_1_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Exemple bàsic d'herència amb classes d'animals.
# -----------------------------------------------------------------------------

class Animal:
    def parlar(self):
        # Mètode que serà sobreescrit per les subclasses
        print("...")

class Gos(Animal):
    def parlar(self):
        print("Bup bup!")

class Gat(Animal):
    def parlar(self):
        print("Miau!")
