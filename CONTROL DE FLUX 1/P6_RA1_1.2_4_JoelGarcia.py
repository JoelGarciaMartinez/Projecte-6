# --------------------------------------------------------
# Nom del fitxer: P6_RA1_1.2_4_JoelGarcia.py
# Autor: Joel
# Data de creació: 25/04/2025
# Descripció: Aquest programa demana un número entre 1 i 10 i diu si està aprovat o suspès.
# --------------------------------------------------------

# Demanar el número entre 1 i 10
nota = int(input("Introdueix una nota entre l'1 i el 10: "))

# Comprovar si la nota és aprovada o suspesa
if nota >= 5:
    print("Aprovat")
else:
    print("Suspès")
