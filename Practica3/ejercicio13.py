"""
Dadas dos variables numéricas A y B, que el usuario debe teclear,
se pide realizar un algoritmo que intercambie los valores de ambas
variables y muestre cuánto valen al final las dos variables.
"""

A = float(input("Escribe la variable A: "))
B = float(input("Escribe la variable B: "))

x = A
A = B
B = x

print("El valor A es: ", A)
print("El valor B es: ", B)


