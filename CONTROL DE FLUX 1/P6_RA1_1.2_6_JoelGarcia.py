# --------------------------------------------------------
# Nom del fitxer: P6_RA1_1.2_6_JoelGarcia.py
# Autor: Joel
# Data de creació: 25/04/2025
# Descripció: Aquest programa demana una lletra i determina si és vocal o consonant sense fer servir lower().
# --------------------------------------------------------

# Demanar una lletra
lletra = input("Introdueix una lletra: ")

# Comprovar si és vocal o consonant
if lletra in "aeiouAEIOU":  # Incloem les vocals majúscules
    print("És una vocal.")
else:
    print("És una consonant.")
