"""
Algoritmo que pida un número y diga si es positivo, negativo o 0

"""

numb1 = float(input("Escribe el numero: "))

if numb1 == 0:
    print("Es un 0")
if numb1 > 0:
    print("Es un numero positivo")
if numb1 < 0:
    print("Es un numero negativo")