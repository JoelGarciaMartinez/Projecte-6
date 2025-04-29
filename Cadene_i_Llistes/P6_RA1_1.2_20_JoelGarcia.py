# P6_RA1_1.2_20_JoelGarcia.py
# Data: 25/04/2025
# Descripció: El programa demana una llista de paraules i crea una nova llista amb només les paraules que comencen per vocal.

# Demanem una llista de paraules a l'usuari
paraules = input("Introdueix una llista de paraules separades per espai: ").split()

# Llista de paraules que comencen per vocal
paraules_vocal = [paraula for paraula in paraules if paraula[0].lower() in 'aeiou']

# Mostrem el resultat
print("Paraules que comencen per vocal:", paraules_vocal)
