# data_hora.py
# Autor: Joel Garcia
# Descripció: Mostra la data i hora actual formatada i calcula els dies fins a una data futura

import datetime

# Mostra la data i hora actual formatada
data_hora_actual = datetime.datetime.now()
data_hora_formatada = data_hora_actual.strftime("%d/%m/%Y %H:%M")
print("Data i hora actual:", data_hora_formatada)

# Calcular quants dies falten fins a una data específica (exemple: Nadal)
nadal = datetime.datetime(data_hora_actual.year, 12, 25)  # Nadal d'aquest any

# Si la data d'avui és després del 25 de desembre, calculem per Nadal de l'any següent
if data_hora_actual > nadal:
    nadal = datetime.datetime(data_hora_actual.year + 1, 12, 25)

dies_falten = (nadal - data_hora_actual).days
print(f"\nQueden {dies_falten} dies per Nadal.")
