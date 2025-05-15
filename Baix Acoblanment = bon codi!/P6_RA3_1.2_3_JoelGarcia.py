# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_3_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Aplicació del patró Estratègia per desacoblar la lògica de descompte 
# de la classe CarretCompra.
# -----------------------------------------------------------------------------

class Descompte20:
    def aplicar(self, total):
        # Aplica un descompte del 20%
        return total * 0.8

class CarretCompra:
    def __init__(self, descompte):
        # La lògica de descompte es passa com estratègia
        self.productes = []
        self.descompte = descompte

    def afegir_producte(self, preu):
        self.productes.append(preu)

    def calcular_total(self):
        total = sum(self.productes)
        return self.descompte.aplicar(total)
