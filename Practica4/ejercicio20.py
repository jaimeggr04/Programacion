import random
import statistics
"""
Muestra 50 números enteros aleatorios entre 100 y 199 (ambos incluidos)
separados por espacios. Muestra también el máximo, el mínimo, la moda, 
la media, la mediana y la desviación típica de esos números.

"""

i = 0
list = []
# Usar un bucle 'while' para generar 50 números aleatorios entre 100 y 199 y agregarlos a la lista 'lis'
while i < 50:
    list.append(random.randint(100, 199))
    i += 1
print(list)
print("Maximo", max(list))
print("Minimo", min(list))
print("Moda", statistics.mode(list))
print("Media", statistics.mean(list))
print("Mediana", statistics.median(list))
print("Desviacion tipica", statistics.stdev(list))