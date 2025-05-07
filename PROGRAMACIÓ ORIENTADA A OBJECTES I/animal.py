# Nom del fitxer: animal.py
# Autor: Joel Garcia
# Descripció: Classe Animal amb mètode per fer un soroll genèric.

class Animal:
    def __init__(self, nom, especie):
        self.nom = nom
        self.especie = especie

    def fer_soroll(self):
        print(f"{self.nom} fa un soroll")
