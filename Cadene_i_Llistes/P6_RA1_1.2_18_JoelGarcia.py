# P6_RA1_1.2_18_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa crea una funció que retorna una llista al revés (sense usar reverse()).

def llista_reversa(llista):
    llista_invertida = []
    for element in llista:
        llista_invertida.insert(0, element)  # Inserim cada element al principi de la nova llista
    return llista_invertida

# Exemple d'ús
llista_original = [1, 2, 3, 4, 5]
llista_invertida = llista_reversa(llista_original)
print("Llista original:", llista_original)
print("Llista invertida:", llista_invertida)
