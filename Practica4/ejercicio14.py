"""
Pide una cadena y un carácter por teclado (valida que sea un carácter)
y muestra cuántas veces aparece el carácter en la cadena.
"""

cad = input("Introduce una cadena de texto: ")
char = input("Introduce el caracter a contar: ")

# Utilizar un bucle "while" para asegurarse de que el usuario haya ingresado solo un carácter
while len(char) > 1:
    char = input("Caracter invalido, por favor introduce un solo caracter: ")

print("El caracter aparece", cad.count(char), "vez/veces en la cadena.")
