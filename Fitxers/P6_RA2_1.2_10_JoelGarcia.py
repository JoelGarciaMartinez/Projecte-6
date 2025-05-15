# -----------------------------------------------------------------------------
# Fitxer: P6_RA2_1.2_10_JoelGarcia.py
# Autor: Joel Garcia
# Descripció: Assegura el tancament del fitxer fins i tot si hi ha error de lectura
# -----------------------------------------------------------------------------

fitxer = None
try:
    fitxer = open("dades.txt", "r")
    dades = fitxer.read()
    print(dades)
except Exception as e:
    print(f"S’ha produït un error: {e}")
finally:
    if fitxer:
        fitxer.close()
