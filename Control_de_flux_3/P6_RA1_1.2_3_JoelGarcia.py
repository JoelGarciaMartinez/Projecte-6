# Fitxer: P6_RA1_1.2_3_JoelGarcia.py
# Data: 25/04/2025
# Descripció: Demana un número i mostra la seva taula de multiplicar (del 1 al 10)

try:
    # Demanem un número enter a l'usuari
    numero = int(input("Introdueix un número per mostrar la seva taula de multiplicar: "))
    
    # Mostrem la taula de multiplicar utilitzant range(1, 11)
    print(f"Taula de multiplicar de {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        
except ValueError:
    print("Error: Has d'introduir un nombre enter.")
