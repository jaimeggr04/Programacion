"""
Realiza un programa que pida el dí­a de la semana
(del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.

"""

day_of_week = int(input("Escriba un dia de la semana (1-7): "))
#Creamos una lista con los dias de la semana
list = ["Error", "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

print("El dia de la semana es: ", list[day_of_week])

