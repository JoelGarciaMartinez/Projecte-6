# --------------------------------------------------
# Nom del fitxer: P6_RA1_1.1_1_edad_major.py
# Autor: Joel
# Data de creació: 24/04/2025
# Descripció: Aquest programa declara una variable numerica que operant amb el % agafem el residu i si es 0 es defineix com parell i si no com a senar
# --------------------------------------------------

edat1 = int(input("Introduir edad del primer:",))

edat2 = int(input("Introduir edad del primer:",))

if edat1 > edat2:
    print("La primera persona és més gran")
elif edat1 < edat2:
    print("La segona persona és més gran")
else:
    print("Tenen la mateixa edat")
