# Nom del fitxer: persona.py
# Autor: Joel Garcia
# Descripció: Classe Persona que es presenta amb nom i edat.

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def presentar_se(self):
        print(f"Hola, soc {self.nom} i tinc {self.edat} anys")
