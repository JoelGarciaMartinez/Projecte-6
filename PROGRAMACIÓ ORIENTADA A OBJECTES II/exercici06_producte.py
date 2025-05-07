# exercici06_producte.py
# Autor: Joel Garcia
# Descripció: Classe Producte amb nom públic i preu privat controlat (>0).

class Producte:
    def __init__(self, nom, preu):
        self.nom = nom
        self.__preu = preu

    def obtenir_preu(self):
        return self.__preu

    def modificar_preu(self, nou_preu):
        if nou_preu > 0:
            self.__preu = nou_preu
