# Nom del fitxer: producte.py
# Autor: Joel Garcia
# Descripció: Classe Producte amb descompte aplicable sobre el preu.

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.preu = preu

    def aplicar_descompte(self, percentatge):
        descompte = self.preu * (percentatge / 100)
        self.preu -= descompte
