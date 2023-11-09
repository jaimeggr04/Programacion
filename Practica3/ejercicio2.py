"""
Calcular el perimetro y área de un rectángulo dada su base y su altura.

"""
# Solicitar al usuario que ingrese la base del rectángulo
base = int(input("Escriba la base: "))
# Solicitar al usuario que ingrese la altura del rectángulo
heigth = int(input("Escriba la altura "))
# Calcular el perímetro del rectángulo (2 veces la suma de la base y la altura)
perimeter = base * 2 + heigth * 2
# Calcular el área del rectángulo (base multiplicada por la altura)
area = base * heigth

print("Este es el perimetro: ", base)
print("Este es el perimetro: ", area)
