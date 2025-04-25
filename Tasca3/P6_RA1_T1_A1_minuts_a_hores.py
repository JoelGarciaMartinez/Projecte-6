# --------------------------------------------------------
# Nom del fitxer: P6_RA1_T1_A1_minuts_a_hores.py
# Autor: Joel
# Data de creació: 25/04/2025
# Descripció: Aquest programa demana el nombre de minuts
# i els converteix a hores i minuts.
# --------------------------------------------------------

minuts = int(input("Introdueix el nombre de minuts: "))

hores = minuts // 60  # Divideix els minuts per 60 per obtenir les hores
minuts_restants = minuts % 60  # El que queda després de dividir per 60 són els minuts restants

print(f"{minuts} minuts són {hores} hores i {minuts_restants} minuts.")
