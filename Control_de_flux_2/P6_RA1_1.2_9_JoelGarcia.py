# Fitxer: P6_RA1_1.2_9_JoelGarcia.py
# Data: 25/04/2025
# Descripció: Troba el número màxim d'una llista donada per l'usuari.

llista = []

for i in range(5):
    numero = float(input(f"Introdueix el número {i+1}: "))
    llista.append(numero)

maxim = max(llista)

print("El número màxim de la llista és:", maxim)
