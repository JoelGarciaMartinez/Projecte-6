# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_5_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Exemple d'herència amb sobrescriptura de mètodes.
# -----------------------------------------------------------------------------

class Llibre:
    def __init__(self, titol, autor):
        self.titol = titol
        self.autor = autor

    def mostrar_info(self):
        print(f"{self.titol}, per {self.autor}")

class LlibrePaper(Llibre):
    def __init__(self, titol, autor, n_pagines):
        super().__init__(titol, autor)
        self.n_pagines = n_pagines

    def mostrar_info(self):
        print(f"{self.titol}, per {self.autor} - {self.n_pagines} pàgines")

class LlibreDigital(Llibre):
    def __init__(self, titol, autor, format):
        super().__init__(titol, autor)
        self.format = format

    def mostrar_info(self):
        print(f"{self.titol}, per {self.autor} - Format: {self.format}")
