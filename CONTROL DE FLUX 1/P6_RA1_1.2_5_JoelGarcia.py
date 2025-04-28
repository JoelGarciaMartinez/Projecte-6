# --------------------------------------------------------
# Nom del fitxer: P6_RA1_1.2_5_JoelGarcia.py
# Autor: Joel
# Data de creació: 25/04/2025
# Descripció: Aquest programa calcula l'edat d'una persona segons la seva data de naixement i verifica si és major d'edat.
# --------------------------------------------------------

from datetime import datetime

# Demanar la data de naixement
dia_naixement = int(input("Introdueix el dia de naixement (dd): "))
mes_naixement = int(input("Introdueix el mes de naixement (mm): "))
any_naixement = int(input("Introdueix l'any de naixement (aaaa): "))

# Obtenir la data actual
data_actual = datetime.now()

# Calcular l'edat
edat = data_actual.year - any_naixement - ((data_actual.month, data_actual.day) < (mes_naixement, dia_naixement))

# Mostrar l'edat i si és major d'edat
print(f"Tens {edat} anys.")
if edat >= 18:
    print("Ets major d'edat.")
else:
    print("Ets menor d'edat.")
