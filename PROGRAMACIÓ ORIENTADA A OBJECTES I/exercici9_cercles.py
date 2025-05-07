# exercici9_cercles.py
# Autor: Joel Garcia
# Descripció: Mostra cercles amb àrea superior a 50

from cercle import Cercle

cercles = [
    Cercle(3),
    Cercle(5),
    Cercle(10)
]

for c in cercles:
    if c.area() > 50:
        print(f"Radi: {c.radi} - Àrea: {c.area():.2f}")
