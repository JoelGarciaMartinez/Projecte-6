# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_2_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Refactorització per desacoblar la classe Comanda del Notificador,
# utilitzant injecció de dependències al constructor.
# -----------------------------------------------------------------------------

class Notificador:
    def enviar(self, missatge):
        print(f"Notificació: {missatge}")

class Comanda:
    def __init__(self, notificador):
        # El notificador és injectat per dependència
        self.productes = []
        self.notificador = notificador

    def afegir_producte(self, producte):
        self.productes.append(producte)

    def confirmar(self):
        # Es delega la notificació al component injectat
        self.notificador.enviar("Comanda confirmada.")
