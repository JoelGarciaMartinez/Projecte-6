# Fitxer: P6_RA1_1.2_4_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa genera un número aleatori entre 1 i 100 i demana a l'usuari que
# l'endevini, donant pistes de si el número introduït és massa alt o massa baix.

import random

secreta = random.randint(1, 100)
endevina = 0

while endevina != secreta:
    endevina = int(input("Endevina el número (entre 1 i 100): "))
    if endevina < secreta:
        print("Massa baix!")
    elif endevina > secreta:
        print("Massa alt!")

print("Correcte! Has endevinat el número! 🎉")
