# calculadora.py
# Autor: Joel Garcia
# Descripció: Mòdul amb funcions bàsiques de càlcul (suma, resta, multiplicació i divisió)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacio(a, b):
    return a * b

def divisio(a, b):
    if b != 0:
        return a / b
    else:
        return "No es pot dividir per zero"