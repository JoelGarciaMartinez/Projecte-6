# Nom del fitxer: compte_bancari.py
# Autor: Joel Garcia
# Descripció: Classe CompteBancari amb operacions d’ingrés, retirada i consulta de saldo.

class CompteBancari:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def ingressar(self, quantitat):
        self.saldo += quantitat

    def retirar(self, quantitat):
        if quantitat <= self.saldo:
            self.saldo -= quantitat
        else:
            print("Saldo insuficient")

    def veure_saldo(self):
        return self.saldo
