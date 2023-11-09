"""
Introducir una cadena de caracteres e indicar si es un palíndromo.
Una palabra palíndroma es aquella que se lee igual adelante que atrás.
"""

cad = input("Introduzca una cadena: ")
palindromo = True
i = 0
pal1 = ""
ppal2 = ""
j = len(cad) - 1

# Usar un bucle 'while' para verificar si la cadena es un palíndromo
while i < len(cad):
    pal1 = cad[i]
    pal2 = cad[j]
    if pal1 != pal2:
        palindromo = False
    i += 1
    j -= 1
if palindromo:
    print("La palabra es un palindromo")
else:
    print("No es un palindromo")
