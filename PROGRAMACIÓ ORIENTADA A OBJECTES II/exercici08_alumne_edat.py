# exercici08_alumne_edat.py
# Autor: Joel Garcia
# Descripció: Classe Alumne amb edat privada i control de valors no negatius.

class Alumne:
    def __init__(self, edat):
        self.__edat = edat

    @property
    def edat(self):
        return self.__edat

    @edat.setter
    def edat(self, nova_edat):
        if nova_edat >= 0:
            self.__edat = nova_edat
