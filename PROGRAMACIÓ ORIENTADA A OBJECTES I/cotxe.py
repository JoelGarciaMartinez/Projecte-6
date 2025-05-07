# Nom del fitxer: cotxe.py
# Autor: Joel Garcia
# Descripció: Classe Cotxe amb atributs marca, model i any, i mètode per mostrar la informació del cotxe.

class Cotxe:
    def __init__(self, marca, model, any):
        self.marca = marca
        self.model = model
        self.any = any

    def mostrar_info(self):
        print(f"Cotxe: {self.marca} {self.model}, Any: {self.any}")