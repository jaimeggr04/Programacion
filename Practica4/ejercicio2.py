"""
Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
"""

# Usamos input para pedir por teclado un valor.
letter = input("Escriba:")
# Usamos if par comprobar si hay alguna mayuscula

if letter.isupper():
    print("Tiene mayuscula")
else:
    print("Tiene minuscula")
