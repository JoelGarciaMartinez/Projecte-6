# P6_RA1_1.2_7_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa demana una cadena i compta quantes vegades apareix una lletra concreta.

cadena = input("Escriu una cadena: ")
lletra = input("Quina lletra vols comptar? ")

# Comptem quantes vegades apareix la lletra
count = cadena.count(lletra)

print(f"La lletra '{lletra}' apareix {count} vegades en la cadena.")
