# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_8_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Exemple de polimorfisme amb empleats i càlculs de sou diferents.
# -----------------------------------------------------------------------------

class Empleat:
    def calcular_sou(self):
        return 0

class Fixe(Empleat):
    def __init__(self, sou_base):
        self.sou_base = sou_base

    def calcular_sou(self):
        return self.sou_base

class Autonom(Empleat):
    def __init__(self, hores, preu_hora):
        self.hores = hores
        self.preu_hora = preu_hora

    def calcular_sou(self):
        return self.hores * self.preu_hora

def mostrar_sous(llista_empleats):
    for e in llista_empleats:
        print(e.calcular_sou())
