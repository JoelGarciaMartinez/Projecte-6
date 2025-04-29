# Fitxer: P6_RA1_1.2_2_JoelGarcia.py
# Data: 25/04/2025
# Descripció: Demana un nombre enter positiu i calcula la suma de tots els números des de 1 fins al nombre introduït.

try:
    # Demanem un nombre enter positiu a l'usuari
    nombre = int(input("Introdueix un nombre enter positiu: "))
    
    # Comprovem que el nombre sigui positiu
    if nombre <= 0:
        raise ValueError("El nombre ha de ser positiu.")

    # Generem la seqüència des de 1 fins a nombre i calculem la suma
    suma = sum(range(1, nombre + 1))  # range(1, n+1) per incloure el nombre
    print("La suma dels nombres de 1 a", nombre, "és:", suma)

except ValueError as e:
    print("Error:", e)

