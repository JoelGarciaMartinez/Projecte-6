# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_7_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Exemple de polimorfisme amb figures que es dibuixen diferent.
# -----------------------------------------------------------------------------

class Figura:
    def dibuixar(self):
        print("Dibuixant figura genèrica")

class Cercle(Figura):
    def dibuixar(self):
        print("Dibuixant un cercle")

class Quadrat(Figura):
    def dibuixar(self):
        print("Dibuixant un quadrat")

class Triangle(Figura):
    def dibuixar(self):
        print("Dibuixant un triangle")
