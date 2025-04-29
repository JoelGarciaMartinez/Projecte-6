# Fitxer: P6_RA1_1.2_1_JoelGarcia.py
# Data: 25/04/2025
# Descripció: Genera una seqüència de nombres des de 0 fins al nombre introduït per l'usuari.

try:
    # Demanem un nombre enter a l'usuari
    nombre = int(input("Introdueix un nombre enter: "))
    
    # Generem la seqüència des de 1 fins a nombre i calculem la suma
    suma = sum(range(1, nombre + 1))  # range(1, n+1) per incloure el nombre
    print("La suma dels nombres de 1 a", nombre, "és:", suma)

except ValueError:
    print("Error: Has d'introduir un nombre enter.")
