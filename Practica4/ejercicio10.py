import random
"""
Crea una aplicación que permita adivinar un número.
La aplicación genera un número aleatorio del 1 al 100.
A continuación va pidiendo números y va respondiendo si el número a
adivinar es mayor o menor que el introducido, además de los intentos
que te quedan (tienes 10 intentos para acertarlo). El programa termina
cuando se acierta el número (además te dice en cuantos intentos lo has
acertado), si se llega al límite de intentos te muestra el número que
había generado.
"""

guess=0
numb = random.randrange(1, 100)
count = 10

## Se utiliza un bucle 'while' para continuar la adivinanza mientras el número ingresado por el usuario.
while numb != guess and count > 0:

    guess = int(input("Introduzca el numero que crees que es: "))
    if numb > guess:
        print("!Error!, Es mayor")
    if numb < guess:
        print("!Error!, Es menor")
    count -= 1
    print("Te quedan", count, "intentos")

if numb == guess:
    print("Correcto")











