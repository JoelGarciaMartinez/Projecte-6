# -----------------------------------------------------------------------------
# Fitxer: P6_RA2_1.2_3_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Afegeix una línia nova al final de sortida.txt
# -----------------------------------------------------------------------------

with open("sortida.txt", "a") as fitxer:
    fitxer.write("Línia afegida\n")
