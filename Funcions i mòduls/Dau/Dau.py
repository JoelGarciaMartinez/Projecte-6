# dau.py
# Autor: Joel Garcia
# Descripció: Simula el llançament d’un dau utilitzant el mòdul random

import random

def llençar_dau():
    return random.randint(1, 6)

def llançar_varis(n):
    total = 0
    for _ in range(n):
        tirada = llençar_dau()
        print("Tirada:", tirada)
        total += tirada
    mitjana = total / n
    return mitjana

# Part principal del programa
print("Simulació de llançament de dau 🎲")

n = int(input("Quantes vegades vols llençar el dau? "))
mitjana = llançar_varis(n)
print(f"\nMitjana de les {n} tirades: {mitjana:.2f}")
