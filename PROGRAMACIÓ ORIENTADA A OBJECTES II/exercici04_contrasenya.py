# exercici04_contrasenya.py
# Autor: Joel Garcia
# Descripció: Classe Usuari amb contrasenya privada i mètodes per canviar-la i verificar-la.

class Usuari:
    def __init__(self, contrasenya):
        self.__contrasenya = contrasenya

    def canviar_contrasenya(self, nova):
        if len(nova) >= 8:
            self.__contrasenya = nova

    def verificar_contrasenya(self, clau):
        return clau == self.__contrasenya
