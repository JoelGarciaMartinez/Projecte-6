# validacions.py
# Autor: Joel Garcia
# Descripció: Mòdul amb funcions per validar emails i números de telèfon

import re

def es_email_valid(email):
    """
    Valida un email amb una expressió regular.
    """
    patró_email = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return re.match(patró_email, email) is not None

def es_telefon_valid(telefon):
    """
    Valida un número de telèfon (exemple: +34 612 345 678).
    """
    patró_telefon = r"^\+?\d{1,4}[\s-]?\(?\d{1,3}\)?[\s-]?\d{3}[\s-]?\d{3}$"
    return re.match(patró_telefon, telefon) is not None
