"""
Escribe un programa que dados dos números, uno real (base)
y un entero positivo (exponente), saque por pantalla el resultado
de la potencia. No se puede utilizar el operador de potencia.
"""

base = float(input("Introduzco el numero de la base"))
exponent = float(input("Introduzca el numero del exponente"))

base = float(input("Introduza la base: "))
exponent = int(input("Introduzca el exponente: "))
res = base
cont = exponent
# Usar un bucle 'while' para calcular la potencia
while cont > 1:
    res *= base
    cont -= 1
print(base, "^", exponent, "=", res)
