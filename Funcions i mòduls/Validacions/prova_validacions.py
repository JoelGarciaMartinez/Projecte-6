# prova_validacions.py
# Autor: Joel Garcia
# Descripció: Script per provar les funcions de validació de emails i telèfons

import validacions

# Proves amb emails vàlids i no vàlids
emails = [
    "joel@exemple.com",      # Vàlid
    "joel@exemple",          # No vàlid
    "joel.exemple.com",      # No vàlid
    "joel@exemple.co.uk"     # Vàlid
]

for email in emails:
    if validacions.es_email_valid(email):
        print(f"{email} és vàlid.")
    else:
        print(f"{email} no és vàlid.")

# Proves amb números de telèfon vàlids i no vàlids
telefons = [
    "+34 612 345 678",       # Vàlid
    "612345678",             # No vàlid
    "+1 234-567-8901",       # Vàlid
    "12345"                  # No vàlid
]

for telefon in telefons:
    if validacions.es_telefon_valid(telefon):
        print(f"{telefon} és vàlid.")
    else:
        print(f"{telefon} no és vàlid.")
