# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_1_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Refactorització per aconseguir baix acoplament entre Factura 
# i Impressora mitjançant injecció de dependències.
# -----------------------------------------------------------------------------

class Impressora:
    def imprimir(self, text):
        # Mostra el text per consola (simulació d’impressió)
        print(text)

class Factura:
    def __init__(self, impressora):
        # L’objecte Impressora és injectat des de fora
        self.impressora = impressora
        self.productes = []

    def afegir_producte(self, nom, preu):
        self.productes.append((nom, preu))

    def total(self):
        return sum(preu for _, preu in self.productes)

    def imprimir_factura(self):
        text = "Factura:\n"
        for nom, preu in self.productes:
            text += f"{nom}: {preu}€\n"
        text += f"Total: {self.total()}€"
        self.impressora.imprimir(text)
