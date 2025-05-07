# exercici7_gos.py
# Autor: Joel Garcia
# Descripció: Classe Gos que hereta d'Animal

from animal import Animal

class Gos(Animal):
    def fer_soroll(self):
        print(f"{self.nom} diu: Bup bup!")

rex = Gos("Rex", "Caní")
rex.fer_soroll()

