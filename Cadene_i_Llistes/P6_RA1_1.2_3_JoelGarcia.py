# P6_RA1_1.2_3_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa defineix una funció que rep una cadena i la retorna invertida.

def invertir_cadena(cadena):
    return cadena[::-1]

text = input("Escriu una cadena: ")
text_invertit = invertir_cadena(text)
print("Cadena invertida:", text_invertit)
