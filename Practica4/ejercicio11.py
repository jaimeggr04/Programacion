"""
Realizar un algoritmo que pida números (se pedirá por teclado la
cantidad de números a introducir). El programa debe informar de
cuantos números introducidos son mayores que 0, menores que 0 e iguales a 0.
"""

long = int(input("Escriba el numero de la lista: "))
zero = 0
low = 0
high = 0
# Utilizar un bucle 'while' para recopilar números y contarlos según su valor, hasta que la longitud llegue a 0
while long > 0:
    num = int(input("Añada un numero a la lista: "))
    if num > 0:
        high += 1
    elif num < 0:
        low += 1
    else:
        zero += 1
    long -= 1
print("Hay", high, "numeros positivos,", low, "numeros negativos", zero, "numeros igual a cero")