import random
"""
Realiza un programa que vaya generando números aleatorios pares
entre 0 y 100 y que no termine de generar números
hasta que no saque el 24. El  programa deberá decir al final cuántos números se han generado.
"""

randomNumb = random.randint(1, 50) * 2
i = 0
while randomNumb != 24:
    i += 1
    randomNumb = random.randint(1, 50) * 2

print("Numeros generados", i)
