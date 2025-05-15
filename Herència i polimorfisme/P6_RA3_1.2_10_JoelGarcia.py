# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_10_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Exemple de polimorfisme amb diferents tipus de transport.
# -----------------------------------------------------------------------------

class Vehicle:
    def moure(self):
        pass

class Cotxe(Vehicle):
    def moure(self):
        print("El cotxe circula per la carretera")

class Bicicleta(Vehicle):
    def moure(self):
        print("La bicicleta pedaleja pel carril bici")

class Barca(Vehicle):
    def moure(self):
        print("La barca navega pel riu")

def simular_moviment(vehicles):
    for v in vehicles:
        v.moure()
