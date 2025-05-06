# calcula_arees.py
# Autor: Joel Garcia
# Descripció: Script per calcular àrees de figures geomètriques amb dades de l’usuari

import geometria

print("Calculadora d'àrees\n")

costat = float(input("Introdueix el costat del quadrat: "))
print("Àrea del quadrat:", geometria.area_quadrat(costat))

radi = float(input("\nIntrodueix el radi del cercle: "))
print("Àrea del cercle:", geometria.area_cercle(radi))

base = float(input("\nIntrodueix la base del rectangle: "))
altura = float(input("Introdueix l'altura del rectangle: "))
print("Àrea del rectangle:", geometria.area_rectangle(base, altura))
