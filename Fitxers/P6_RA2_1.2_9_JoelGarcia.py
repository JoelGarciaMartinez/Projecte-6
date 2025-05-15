# -----------------------------------------------------------------------------
# Fitxer: P6_RA2_1.2_9_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Crea un fitxer si no existeix i hi escriu un missatge per defecte
# -----------------------------------------------------------------------------

try:
    with open("registre.txt", "r") as fitxer:
        print(fitxer.read())
except FileNotFoundError:
    with open("registre.txt", "w") as nou_fitxer:
        nou_fitxer.write("Fitxer creat automàticament\n")
