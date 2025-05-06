# prova_textos.py
# Autor: Joel Garcia
# Descripció: Script per provar funcions del mòdul textos.py usant un àlies

import textos as tx

frase = "això és una prova de TEXT."

print("Text original:", frase)
print("En majúscules:", tx.a_majuscules(frase))
print("En minúscules:", tx.a_minuscules(frase))
print("Capitalitzat:", tx.capitalitzar(frase))
