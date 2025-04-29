# Fitxer: P6_RA1_1.2_6_JoelGarcia.py
# Data: 25/04/2025
# Descripció: Mostra els primers 10 termes de la seqüència de Fibonacci.

a, b = 0, 1
print("Primers 10 termes de la seqüència de Fibonacci:")

for _ in range(10):
    print(a)
    a, b = b, a + b
