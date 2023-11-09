"""
Crea un programa que pida al usuario dos números y muestre su división
si el segundo no es cero, o un mensaje de aviso en caso contrario.

"""

numb1 = int(input("Escriba el numero 1: "))
numb2 = int(input("Escriba el numero 2: "))

if numb2 == 0:
    print("El segundo numero ws 0 y no se puede hacer la division")
else:
    div = float(numb1 / numb2)
    print("El resultado es: ", numb1, "/", numb2, "=", div)
