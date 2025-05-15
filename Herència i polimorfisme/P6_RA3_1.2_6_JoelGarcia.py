# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_6_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Exemple de polimorfisme amb sons d’animals.
# -----------------------------------------------------------------------------

class Animal:
    def fer_soroll(self):
        return "..."

class Gat(Animal):
    def fer_soroll(self):
        return "Miau"

class Vaca(Animal):
    def fer_soroll(self):
        return "Muuu"

def reproduir_soroll(animal):
    # Accepta qualsevol animal que tingui el mètode fer_soroll()
    print(animal.fer_soroll())
