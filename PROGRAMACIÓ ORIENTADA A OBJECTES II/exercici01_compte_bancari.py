# exercici01_compte_bancari.py
# Autor: Joel Garcia
# Descripció: Classe CompteBancari amb atribut privat __saldo i mètodes per ingressar, retirar i consultar el saldo.

class CompteBancari:
    def __init__(self):
        self.__saldo = 0

    def ingressar(self, quantitat):
        self.__saldo += quantitat

    def retirar(self, quantitat):
        if quantitat <= self.__saldo:
            self.__saldo -= quantitat

    def consultar_saldo(self):
        return self.__saldo
