# --------------------------------------------------------
# Nom del fitxer: P6_RA1_1.2_1_area_cercle.py
# Autor: Joel
# Data de creació: 25/04/2025
# Descripció: Aquest programa calcula l'àrea d'un cercle donat el seu radi utilitzant una constant PI.
# --------------------------------------------------------

import math

PI = 3.1416  # Constant: PI és una constant amb el valor fix de 3.1416.

def calcular_area(radi):  # Funció: calcular_area és una funció que rep un argument, radi, i retorna l'àrea del cercle.
  return PI * radi ** 2  # Aquesta línia calcula l'àrea del cercle.

radi = float(input("Introdueix el radi: "))  # Línia que llegeix dades de l'usuari: es demana el radi al usuario.
area = calcular_area(radi)  # Variable: 'radi' es passa com a paràmetre a la funció calcular_area, i 'area' desa el resultat.
print("L'àrea del cercle és:", area)  # Línia que mostra el resultat: imprimeix l'àrea calculada del cercle.
