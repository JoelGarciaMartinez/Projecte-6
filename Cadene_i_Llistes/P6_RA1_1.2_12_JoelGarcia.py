# P6_RA1_1.2_12_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa demana a l'usuari 5 paraules i les emmagatzema en una llista.

# Creem una llista buida per emmagatzemar les paraules
paraules = []

# Demanem 5 paraules a l'usuari i les afegim a la llista
for i in range(5):
    paraula = input(f"Introdueix la paraula {i + 1}: ")
    paraules.append(paraula)

# Mostrar la llista amb les paraules
print("Les paraules introduïdes són:", paraules)
