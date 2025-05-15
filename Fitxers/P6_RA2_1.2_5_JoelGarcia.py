# -----------------------------------------------------------------------------
# Fitxer: P6_RA2_1.2_5_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Llegeix i afegeix una línia a un fitxer sense esborrar-lo (r+)
# -----------------------------------------------------------------------------

with open("sortida.txt", "r+") as fitxer:
    contingut = fitxer.read()
    print(contingut)
    fitxer.write("\nNova línia afegida amb r+")
