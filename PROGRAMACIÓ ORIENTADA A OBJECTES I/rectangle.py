# Nom del fitxer: rectangle.py
# Autor: Joel Garcia
# Descripció: Classe Rectangle amb càlculs d'àrea i perímetre.

class Rectangle:
    def __init__(self, amplada, alçada):
        self.amplada = amplada
        self.alçada = alçada

    def area(self):
        return self.amplada * self.alçada

    def perimetre(self):
        return 2 * (self.amplada + self.alçada)
