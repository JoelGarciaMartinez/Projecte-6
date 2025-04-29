# Fitxer: P6_RA1_1.2_5_JoelGarcia.py
# Data: 25/04/2025
# Descripció: Demana un nombre enter i imprimeix tots els nombres primers des de 2 fins a aquest número

# Funció per comprovar si un nombre és primer
def es_primer(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Comprovem fins a la arrel quadrada del número
        if n % i == 0:
            return False
    return True

try:
    # Demanem un número enter positiu a l'usuari
    numero = int(input("Introdueix un número enter positiu: "))
    
    # Comprovem que el número sigui positiu
    if numero >= 2:
        print(f"Nombres primers des de 2 fins a {numero}:")
        for i in range(2, numero + 1):  # Iterem des de 2 fins al número introduït
            if es_primer(i):  # Comprovem si el número és primer
                print(i)
    else:
        print("Error: Has d'introduir un nombre enter positiu major o igual a 2.")

except ValueError:
    print("Error: Has d'introduir un nombre enter positiu.")
