# P6_RA1_1.2_14_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa demana 10 números i crea dues llistes: una amb els parells i una altra amb els senars.

pares = []
senars = []

for i in range(10):
    numero = int(input("Introdueix un número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        senars.append(numero)

print("Números parells:", pares)
print("Números senars:", senars)
