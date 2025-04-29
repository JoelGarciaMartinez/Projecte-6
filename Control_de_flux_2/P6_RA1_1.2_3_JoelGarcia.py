# Fitxer: P6_RA1_1.2_3_JoelGarcia.py
# Data: 25/04/2025
# Descripció: Programa que demana a l'usuari un número enter i mostra la seva taula
# de multiplicar del 1 al 10.

num = int(input("Introdueix un número enter: "))

print(f"Taula de multiplicar del {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
