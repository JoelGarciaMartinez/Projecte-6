# --------------------------------------------------------
# Nom del fitxer: velocitat_mitjana.py
# Autor: Joel
# Data de creació: 25/04/2025
# Descripció: Aquest programa demana la distància (en km)
# i el temps (en hores), i calcula la velocitat mitjana.
# --------------------------------------------------------

distancia = float(input("Introdueix la distància (en km): "))
temps = float(input("Introdueix el temps (en hores): "))

velocitat = distancia / temps

print(f"La velocitat mitjana és: {velocitat} km/h")
