"""
Escribe un programa que pida un número entero entre uno y doce e
imprima el número de días que tiene el mes correspondiente.
Si introducimos otro número nos da un error.
"""

numb = int(input("Introduce un numero entre 1 y 12: "))
#Creamos otra lista igual que el anterior ejercicio, pero con los mesesd el año.
list = ["Error", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Novimiembre", "Diciembre" ]
print("El mes es: ", list[numb])