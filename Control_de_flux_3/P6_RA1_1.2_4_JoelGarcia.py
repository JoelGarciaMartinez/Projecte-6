# Fitxer: P6_RA1_1.2_4_JoelGarcia.py
# Data: 25/04/2025
# Descripció: Demana un nombre enter i imprimeix els nombres parells des de 0 fins a aquest nombre

try:
    # Demanem un número enter positiu a l'usuari
    numero = int(input("Introdueix un número enter positiu: "))
    
    # Comprovem que el número sigui positiu
    if numero >= 0:
        # Imprimim tots els nombres parells des de 0 fins al número
        print(f"Nombres parells des de 0 fins a {numero}:")
        for i in range(0, numero + 1, 2):  # range(0, n+1, 2) per obtenir parells
            print(i)
    else:
        print("Error: Has d'introduir un nombre enter positiu.")

except ValueError:
    print("Error: Has d'introduir un nombre enter positiu.")
