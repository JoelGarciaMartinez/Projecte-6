# --------------------------------------------------------
# Nom del fitxer: P6_RA1_1.2_1_positiu_negatiu_zero.py
# Autor: Joel
# Data de creació: 25/04/2025
# Descripció: Aquest programa demana a l'usuari un número i determina si és positiu, negatiu o zero, 
# i imprimeix "Gràcies!" al final.
# --------------------------------------------------------

numero = float(input("Introdueix un número: "))  # Demana un número a l'usuari

if numero > 0:  # Si el número és més gran que zero
    print("El número és positiu.")
elif numero < 0:  # Si el número és menor que zero
    print("El número és negatiu.")
else:  # Si el número és zero
    print("El número és zero.")

print("Gràcies!")  # Imprimeix "Gràcies!" al final
