# calcula_força.py
# Autor: Joel Garcia
# Descripció: Exemple d'ús del mòdul constants.py per calcular la força gravitatòria

import constants

def calcular_força(massa, altura):
    """
    Calcula la força gravitatòria a partir de la massa i l'altura.
    La fórmula per la força gravitatòria és: F = m * g
    on m és la massa (kg) i g és l'acceleració de la gravetat (m/s^2).
    """
    return massa * constants.GRAVETAT

massa = float(input("Introdueix la massa (kg): "))
altura = float(input("Introdueix l'altura (m): "))

força = calcular_força(massa, altura)
print(f"La força gravitatòria a una alçada de {altura} metres per una massa de {massa} kg és {força:.2f} N.")
