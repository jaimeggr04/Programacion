"""
Suponiendo que hemos introducido una cadena por teclado
que representa una frase (palabras separadas por espacios), realiza
un programa que cuente cuántas palabras tiene.
"""

cad = input("Introduzca una frase de varias palabras: ")
print("La cadena tiene", cad.count(" ") + 1, "palabras")
