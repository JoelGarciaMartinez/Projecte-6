# P6_RA1_1.2_9_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa divideix una frase en paraules i les mostra una per una.

frase = input("Escriu una frase: ")

# Divideix la frase en paraules utilitzant el mètode split()
paraules = frase.split()

# Mostra cada paraula una per una
for paraula in paraules:
    print(paraula)
