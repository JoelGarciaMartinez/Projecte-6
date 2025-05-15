# -----------------------------------------------------------------------------
# Fitxer: P6_RA2_1.2_1_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Llegeix i mostra el contingut d’un fitxer anomenat missatge.txt
# -----------------------------------------------------------------------------

with open("missatge.txt", "r") as fitxer:
    contingut = fitxer.read()
    print(contingut)
