# exercici03_termostat.py
# Autor: Joel Garcia
# Descripció: Classe Termostat amb getter/setter que controla els valors de temperatura (10-30°C).

class Termostat:
    def __init__(self):
        self.__temperatura = 20

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if 10 <= valor <= 30:
            self.__temperatura = valor
