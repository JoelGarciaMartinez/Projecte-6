# --------------------------------------------------------
# Nom del fitxer: P6_RA1_1.2_1_calculadora.py
# Autor: Joel
# Data de creació: 25/04/2025
# Descripció: Aquesta calculadora demana dos números i realitza les operacions bàsiques (+, -, *, /).
# --------------------------------------------------------

# Demanar els dos números a l'usuari
num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))

# Demanar l'operació a realitzar
operacio = input("Quina operació vols realitzar (+, -, *, /)? ")

# Realitzar l'operació corresponent
if operacio == "+":
    resultat = num1 + num2
    print("El resultat de la suma és:", resultat)
elif operacio == "-":
    resultat = num1 - num2
    print("El resultat de la resta és:", resultat)
elif operacio == "*":
    resultat = num1 * num2
    print("El resultat de la multiplicació és:", resultat)
elif operacio == "/":
    if num2 != 0:
        resultat = num1 / num2
        print("El resultat de la divisió és:", resultat)
    else:
        print("No es pot dividir per zero!")
else:
    print("Operació no vàlida!")
