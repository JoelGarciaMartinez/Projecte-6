# exercici09_joc_puntuacio.py
# Autor: Joel Garcia
# Descripció: Classe Joc amb puntuació privada, mètodes per sumar i reiniciar.

class Joc:
    def __init__(self):
        self.__puntuacio = 0

    def sumar_punts(self, punts):
        self.__puntuacio += punts

    def reiniciar(self):
        self.__puntuacio = 0

    def obtenir_puntuacio(self):
        return self.__puntuacio