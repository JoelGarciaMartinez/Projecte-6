# exercici10_persones.py
# Autor: Joel Garcia
# Descripció: Mostra persones de més de 30 anys

from persona import Persona

def majors_de_30(persones):
    for p in persones:
        if p.edat > 30:
            p.presentar_se()

llista = [
    Persona("Joan", 25),
    Persona("Laura", 35),
    Persona("Víctor", 40)
]

majors_de_30(llista)
