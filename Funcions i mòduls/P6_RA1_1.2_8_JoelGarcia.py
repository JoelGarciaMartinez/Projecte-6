# --------------------------------------------------------
# Nom del fitxer: P6_RA1_1.2_8_JoelGarcia.py
# Autor: Joel
# Data de creació: 25/04/2025
# Descripció: Aquest programa defineix una funció recursiva que calcula el factorial.
# --------------------------------------------------------
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)