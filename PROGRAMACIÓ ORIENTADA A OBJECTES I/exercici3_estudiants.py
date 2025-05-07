# exercici3_estudiants.py
# Autor: Joel Garcia
# Descripció: Mostra els estudiants que han aprovat

from estudiant import Estudiant

estudiants = [
    Estudiant("Anna", 7),
    Estudiant("Pau", 4.5),
    Estudiant("Marc", 9)
]

print("Aprovats:")
for e in estudiants:
    if e.ha_aprovat():
        print(e.nom)
