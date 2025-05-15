# -----------------------------------------------------------------------------
# Fitxer: P6_RA2_1.2_7_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Gestiona l’error si no es pot escriure en el fitxer
# -----------------------------------------------------------------------------

try:
    with open("resultats.txt", "w") as fitxer:
        fitxer.write("Resultat escrit correctament.")
except PermissionError:
    print("Error: No tens permisos per escriure en aquest fitxer.")
