# -----------------------------------------------------------------------------
# Fitxer: P6_RA2_1.2_6_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Comprova si un fitxer existeix abans de llegir-lo
# -----------------------------------------------------------------------------

import os

if os.path.exists("dades.txt"):
    with open("dades.txt", "r") as fitxer:
        print(fitxer.read())
else:
    print("Error: El fitxer 'dades.txt' no existeix.")
