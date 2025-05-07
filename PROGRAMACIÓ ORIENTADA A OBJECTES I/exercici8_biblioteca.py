# exercici8_biblioteca.py
# Autor: Joel Garcia
# Descripció: Afegeix llibres a una biblioteca i els mostra

from llibre import Llibre

class Biblioteca:
    def __init__(self):
        self.llibres = []

    def afegir_llibre(self, llibre):
        self.llibres.append(llibre)

    def mostrar_llibres(self):
        for l in self.llibres:
            l.mostrar_info()

biblio = Biblioteca()
biblio.afegir_llibre(Llibre("1984", "George Orwell", 1949))
biblio.afegir_llibre(Llibre("Crim i càstig", "Fiódor Dostoievski", 1866))
biblio.mostrar_llibres()
