"""
Un alumno desea saber cuál será su calificación final
 en la materia de Algoritmos Dicha calificación se compone
 de los siguientes porcentajes:

* 60% del promedio de sus prácticas.
* 30% de la calificación del examen final.
 * 10% actitud.
"""

averagePractices = float(input("¿Cual es tu nota media de practicas?: "))
exam = float(input("¿Cual es su nota de examen?: "))
attitude = float(input("¿Cual es su nota de actitud?: "))
# Calcular la nota final utilizando los porcentajes dados (60% prácticas, 30% examen, 10% actitud)
grade = (averagePractices * 0.6) + (exam * 0.3) + (attitude * 0.1)

print("Su nota final es: ", grade)
