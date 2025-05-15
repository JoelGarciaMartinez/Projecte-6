# -----------------------------------------------------------------------------
# Fitxer: P6_RA2_1.2_2_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Escriu tres línies a sortida.txt. El contingut anterior es sobreescriu.
# -----------------------------------------------------------------------------

with open("sortida.txt", "w") as fitxer:
    fitxer.write("Primera línia\n")
    fitxer.write("Segona línia\n")
    fitxer.write("Tercera línia\n")
