import math
"""
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
"""

cat1 = int(input("Escriba la hipotenusa 1: "))
cat2 = int(input("Escriba la hipotenusa 2: "))

# Calcular la hipotenusa utilizando el teorema de Pitágoras
hipotenusa = float(math.sqrt(cat1**2)+(cat2**2))

print("Su hipotenusa es: ", hipotenusa)
