# P6_RA1_1.2_4_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa demana una paraula i comprova si és un palíndrom.

paraula = input("Escriu una paraula: ")

# Comprovem si la paraula és igual a la seva versió invertida
if paraula == paraula[::-1]:
    print("És un palíndrom!")
else:
    print("No és un palíndrom.")
