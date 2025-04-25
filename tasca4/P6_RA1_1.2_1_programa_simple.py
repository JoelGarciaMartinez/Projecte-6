# --------------------------------------------------------
# Nom del fitxer: P6_RA1_1.2_1_programa_simple.py
# Autor: Joel
# Data de creació: 25/04/2025
# Descripció: Aquest programa utilitza una constant, una funció, una entrada de l'usuari i una sortida per pantalla.
# --------------------------------------------------------

# a. Definim una constant
PI = 3.1416

# b. Funció per calcular l'àrea d'un cercle
def calcula_area(radi):
    return PI * radi * radi

# c. Entrada de l'usuari
radi = float(input("Introdueix el radi del cercle: "))

# d. Sortida per pantalla
area = calcula_area(radi)
print("L'àrea del cercle és:", area)
