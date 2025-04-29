# Fitxer: P6_RA1_1.2_5_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa demana a l'usuari un número enter positiu i comprova si és un nombre primer.

num = int(input("Introdueix un número enter positiu: "))

if num < 2:
    print("No és un nombre primer.")
else:
    es_primer = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primer = False
            break
    if es_primer:
        print("És un nombre primer.")
    else:
        print("No és un nombre primer.")
