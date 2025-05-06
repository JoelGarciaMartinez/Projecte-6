# cientifica.py
# Autor: Joel Garcia
# Descripció: Mòdul que combina funcions bàsiques de calculadora amb funcions alternatives a math

import calculadora

def suma_cientifica(a, b):
    return calculadora.suma(a, b)

def resta_cientifica(a, b):
    return calculadora.resta(a, b)

def multiplicacio_cientifica(a, b):
    return calculadora.multiplicacio(a, b)

def divisio_cientifica(a, b):
    return calculadora.divisio(a, b)

def sqrt_cientifica(a):
    """ Calcula l'arrel quadrada utilitzant l'operador exponent. """
    return a ** 0.5

def potencia_cientifica(a, b):
    """ Calcula la potència a elevat a b. """
    return a ** b

def sin_cientifica(a):
    """ Aproximació de la funció sine per valors petits utilitzant la sèrie de Taylor.
        Per valors més grans, caldria una funció més precisa.
    """
    # Aproximació sin(x) = x - (x^3)/6 + (x^5)/120 - ...
    a = a % 360  # Convertem l'angle en graus entre 0 i 360 per evitar valors grans
    radian = a * (3.14159265359 / 180)  # Convertim graus a radians
    sine = radian - (radian**3)/6 + (radian**5)/120
    return sine
