# --------------------------------------------------------
# Nom del fitxer: P6_RA1_1.2_6_JoelGarcia.py
# Autor: Joel
# Data de creació: 25/04/2025
# Descripció: Aquest programa defineix una funció que multiplica tots els nombres.
# --------------------------------------------------------
def multiplica_tot(*nombres):
    resultat = 1
    for n in nombres:
        resultat *= n
    return resultat