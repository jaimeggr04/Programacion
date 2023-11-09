import math
"""
Escribe un programa que diga si un número introducido por teclado
es o no primo. Un número primo es aquel que sólo es divisible entre
él mismo y la unidad.
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si
es divisible por algún otro número6.

"""

numb = float(input("Introduce el numero a verificar: "))

sqrnum = math.sqrt(numb)

i = 2

prim = True
# Usar un bucle "while" para verificar si el número es primo
while i <= sqrnum:
    if numb % i == 0:
        prim = False
    i +=1

if prim:
    print("El numero es primo")
else:
    print("El numero no es primo")

