# -----------------------------------------------------------------------------
# Fitxer: P6_RA3_1.2_3_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Exemple d'herència amb atributs i mètodes personalitzats.
# -----------------------------------------------------------------------------

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def saludar(self):
        print(f"Hola, sóc {self.nom}")

class Treballador(Persona):
    def __init__(self, nom, edat, feina):
        super().__init__(nom, edat)
        self.feina = feina

    def mostrar_feina(self):
        print(f"Treballo com a {self.feina}")
