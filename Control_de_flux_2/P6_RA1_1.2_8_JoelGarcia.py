# Fitxer: P6_RA1_1.2_8_JoelGarcia.py
# Data: 25/04/2025
# Descripció: Demana a l'usuari una frase i compta quantes vocals conté.

frase = input("Introdueix una frase: ")
vocals = "aeiouAEIOU"
count = sum(1 for lletra in frase if lletra in vocals)

print("La frase conté", count, "vocals.")
