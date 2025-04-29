# P6_RA1_1.2_2_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa demana una frase i compta quantes vocals conté.

frase = input("Escriu una frase: ")
vowels = "aeiouAEIOU"
compte = 0

for lletra in frase:
    if lletra in vowels:
        compte += 1

print("La frase conté", compte, "vocals.")
