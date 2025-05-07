# Nom del fitxer: estudiant.py
# Autor: Joel Garcia
# Descripció: Classe Estudiant que informa si ha aprovat o no.

class Estudiant:
    def __init__(self, nom, nota):
        self.nom = nom
        self.nota = nota

    def ha_aprovat(self):
        return self.nota >= 5
