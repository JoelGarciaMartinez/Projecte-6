# -----------------------------------------------------------------------------
# Fitxer: P6_RA2_1.2_8_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Evita bloquejar el programa si una línia no és un enter vàlid
# -----------------------------------------------------------------------------

with open("nombres.txt", "r") as fitxer:
    for linia in fitxer:
        try:
            numero = int(linia.strip())
            print(f"Nombre: {numero}")
        except ValueError:
            print(f"Error: '{linia.strip()}' no és un enter vàlid.")
