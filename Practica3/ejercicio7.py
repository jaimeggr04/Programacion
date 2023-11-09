"""
Realiza un programa que reciba una cantidad de minutos y muestre por
pantalla cuantas horas y minutos corresponde.
"""

minutes = int(input("Escriba los minutos: "))
# Calcular las horas equivalentes a los minutos ingresados (1 hora = 60 minutos)
hours = minutes / 60
print("El resultado en horas es: ", hours)

