# P6_RA1_1.2_8_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa defineix una funció que elimina tots els espais d'una cadena.

def elimina_espais(cadena):
    return cadena.replace(" ", "")  # Substitueix els espais per una cadena buida

cadena = input("Escriu una cadena amb espais: ")
nova_cadena = elimina_espais(cadena)

print("La cadena sense espais és:", nova_cadena)
