# exercici02_estudiant_nota.py
# Autor: Joel Garcia
# Descripció: Classe Estudiant amb atribut protegit _nota i mètodes per llegir i modificar-la.

class Estudiant:
    def __init__(self, nota):
        self._nota = nota

    def llegir_nota(self):
        return self._nota

    def modificar_nota(self, nova_nota):
        if 0 <= nova_nota <= 10:
            self._nota = nova_nota