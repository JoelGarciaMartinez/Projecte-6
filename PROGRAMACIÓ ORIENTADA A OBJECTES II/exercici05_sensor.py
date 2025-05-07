# exercici05_sensor.py
# Autor: Joel Garcia
# Descripció: Classe Sensor amb valor privat limitat entre 0 i 100.

class Sensor:
    def __init__(self):
        self.__valor = 0

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor
