"""
Pide una cadena y dos caracteres por teclado (valida que sea un carácter),
sustituye la aparición del primer carácter en la cadena por el segundo
carácter.
"""

cad = input("Introduce una cadena de texto: ")
char = input("Introduce el caracter a sustituir: ")

# Utilizar un bucle "while" para verificar que el usuario haya ingresado solo un carácter
while len(char) > 1:
while len(char) > 1:
    char = input("Carácter invalido, introduce un solo caracter: ")
char2 = input("Introduce el carácter el caracter a sustituir: ")
while len(char2) > 1:
    char2 = input("Carácter invalido,introduce un solo caracter: ")
cad = cad.replace(char, char2)
print(cad)

