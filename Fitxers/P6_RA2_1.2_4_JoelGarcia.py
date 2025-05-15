# -----------------------------------------------------------------------------
# Fitxer: P6_RA2_1.2_4_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Compta quantes línies té un fitxer
# -----------------------------------------------------------------------------

with open("sortida.txt", "r") as fitxer:
    linies = fitxer.readlines()
    print(f"Nombre de línies: {len(linies)}")
