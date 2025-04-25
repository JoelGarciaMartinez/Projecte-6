# --------------------------------------------------------
# Nom del fitxer: P6_RA1_1.1_1_preu_iva.py
# Autor: Joel
# Data de creació: 24/04/2025
# Descripció: Aquest programa demana el preu d’un producte
# i calcula el preu final amb un IVA del 21%.
# --------------------------------------------------------

preu = float(input("Introdueix el preu del producte (sense IVA): "))
iva = preu * 0.21
preu_total = preu + iva

print(f"El preu amb IVA és: {preu_total} €")
