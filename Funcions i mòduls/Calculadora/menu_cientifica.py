# menu_cientifica.py
# Autor: Joel Garcia
# Descripció: Menú interactiu per escollir el tipus de càlcul que es vol realitzar

import cientifica

def mostrar_menu():
    print("\nMenú Calculadora Científica:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicació")
    print("4. Divisió")
    print("5. Arrel quadrada")
    print("6. Potència")
    print("7. Sine")
    print("8. Sortir")

def obtenir_opcio():
    opcio = input("\nTria una opció (1-8): ")
    return opcio

def executar_opcio(opcio):
    if opcio == '1':
        a = float(input("Introdueix el primer número: "))
        b = float(input("Introdueix el segon número: "))
        print(f"{a} + {b} = {cientifica.suma_cientifica(a, b)}")
    elif opcio == '2':
        a = float(input("Introdueix el primer número: "))
        b = float(input("Introdueix el segon número: "))
        print(f"{a} - {b} = {cientifica.resta_cientifica(a, b)}")
    elif opcio == '3':
        a = float(input("Introdueix el primer número: "))
        b = float(input("Introdueix el segon número: "))
        print(f"{a} * {b} = {cientifica.multiplicacio_cientifica(a, b)}")
    elif opcio == '4':
        a = float(input("Introdueix el primer número: "))
        b = float(input("Introdueix el segon número: "))
        if b != 0:
            print(f"{a} / {b} = {cientifica.divisio_cientifica(a, b)}")
        else:
            print("Error: No es pot dividir per 0.")
    elif opcio == '5':
        a = float(input("Introdueix el número: "))
        print(f"Arrel quadrada de {a} = {cientifica.sqrt_cientifica(a)}")
    elif opcio == '6':
        a = float(input("Introdueix la base: "))
        b = float(input("Introdueix l'exponent: "))
        print(f"{a} elevat a {b} = {cientifica.potencia_cientifica(a, b)}")
    elif opcio == '7':
        a = float(input("Introdueix l'angle en graus: "))
        print(f"Sine de {a}° = {cientifica.sin_cientifica(a)}")
    elif opcio == '8':
        print("Sortint...")
        return False
    else:
        print("Opció invàlida.")
    return True

def main():
    while True:
        mostrar_menu()
        opcio = obtenir_opcio()
        if not executar_opcio(opcio):
            break

if __name__ == "__main__":
    main()
