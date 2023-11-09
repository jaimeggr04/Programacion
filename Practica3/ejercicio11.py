import math
"""
Realizar un algoritmo que lea un número y que muestre
 su raíz cuadrada y su raíz cúbica
"""

numb = float(input("Escriba un numero: "))
# Calcular la raíz cuadrada del número utilizando la función 'sqrt' de 'math'
sqrt = math.sqrt(numb)
# Calcular la raíz cúbica del número elevando el número a 1/3
sqrt3 = numb**(1/3)

print("La raiz cuadrada de su numero es: ", sqrt)
print("La raiz cubica de su numero es: ", sqrt3)
