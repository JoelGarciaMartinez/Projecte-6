# exercici07_rellotge.py
# Autor: Joel Garcia
# Descripció: Classe Rellotge amb hores privades (0-23) i format “HH:00”.

class Rellotge:
    def __init__(self):
        self.__hores = 0

    @property
    def hores(self):
        return self.__hores

    @hores.setter
    def hores(self, valor):
        if 0 <= valor <= 23:
            self.__hores = valor

    def mostrar_format(self):
        return f"{self.__hores:02d}:00"
