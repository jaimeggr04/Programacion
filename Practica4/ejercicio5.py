"""
Programa que lea 3 datos de entrada A, B y C.
Estos corresponden a las dimensiones de los lados de un triángulo.
El programa debe determinar qué tipo de triángulo es, teniendo en cuenta:
"""

A = float(input("Escriba un numero:"))
B = float(input("Escriba un numero:"))
C = float(input("Escriba un numero:"))

# Verificar si los valores de A, B y C forman un triángulo rectángulo
if A**2 == (B**2 + C**2):
    print("Es un triangulo rectangulo")
if A == B or A == C or C == B:
    print("Es un triangulo isoceles")
if A == B and B == C:
    print("Es un triangulo equilatero")
else:
    print("Es un triangulo escaleno")


