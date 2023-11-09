"""
Escribir un programa que lea un año indicar si es bisiesto.
Nota: un año es bisiesto si es un número divisible por 4, pero no si es
divisible por 100, excepto que también sea divisible por 400.

"""

year = int(input("Indique el año: "))
# Verificar si el año ingresado es un año bisiesto
if year%4==0 and year%100 != 0 or year%400==0:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")