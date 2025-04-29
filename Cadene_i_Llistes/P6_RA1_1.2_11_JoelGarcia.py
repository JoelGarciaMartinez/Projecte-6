# P6_RA1_1.2_11_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa crea una llista amb 5 nombres i imprimeix el major i el menor.

# Creem la llista amb 5 números
numeros = [int(input("Introdueix el primer número: ")),
           int(input("Introdueix el segon número: ")),
           int(input("Introdueix el tercer número: ")),
           int(input("Introdueix el quart número: ")),
           int(input("Introdueix el cinquè número: "))]

# Trobar el major i el menor número de la llista
major = max(numeros)
menor = min(numeros)

# Mostrar el resultat
print("El nombre més gran és:", major)
print("El nombre més petit és:", menor)
