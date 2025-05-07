# exercici5_productes.py
# Autor: Joel Garcia
# Descripció: Aplica un descompte del 10% a una llista de productes

from producte import Producte

def aplicar_descompte_10(productes):
    for p in productes:
        p.aplicar_descompte(10)

productes = [
    Producte("Llibreta", 5),
    Producte("Bolígraf", 2),
    Producte("Mochila", 25)
]

aplicar_descompte_10(productes)

for p in productes:
    print(f"{p.nom} - Preu: {p.preu:.2f}€")