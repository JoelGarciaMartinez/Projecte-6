# exercici4_compte.py
# Autor: Joel Garcia
# Descripció: Simula operacions bancàries

from compte_bancari import CompteBancari

compte = CompteBancari(100)
compte.ingressar(50)
compte.retirar(30)
compte.retirar(200)  # Retirada superior al saldo
print("Saldo final:", compte.veure_saldo())