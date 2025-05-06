# --------------------------------------------------------
# Nom del fitxer: P6_RA1_1.2_9_JoelGarcia.py
# Autor: Joel
# Data de creació: 25/04/2025
# Descripció: Aquest programa defineix una funció estat_persona segons l'edat.
# --------------------------------------------------------
def estat_persona(edat):
    if edat < 18:
        return "Menor d'edat", "Encara no és adult."
    elif edat < 65:
        return "Adult", "Persona en edat laboral."
    else:
        return "Jubilat", "Persona retirada."