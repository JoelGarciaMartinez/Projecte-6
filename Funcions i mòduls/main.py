# main.py
# Autor: Joel Garcia
# Descripció: Ús del paquet 'utilitats' amb conversions de temps i moneda

from Utilitats import temps, moneda

# Temps
segons = 7200
print(f"{segons} segons són {temps.segons_a_minuts(segons)} minuts")
print(f"{segons} segons són {temps.segons_a_hores(segons)} hores")

# Moneda
euros = 50
print(f"{euros}€ són {moneda.euros_a_dolars(euros):.2f} $")
dolars = 100
print(f"{dolars}$ són {moneda.dolars_a_euros(dolars):.2f} €")
