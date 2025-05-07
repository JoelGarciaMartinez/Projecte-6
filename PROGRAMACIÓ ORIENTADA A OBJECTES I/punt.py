# Nom del fitxer: punt.py
# Autor: Joel Garcia
# Descripció: Classe Punt amb càlcul de distància entre dos punts en un pla.

import math

class Punt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, altre_punt):
        return math.sqrt((self.x - altre_punt.x) ** 2 + (self.y - altre_punt.y) ** 2)
