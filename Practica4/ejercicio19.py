import random
"""
Programa que generará 20 números enteros aleatorios.
Estos números se deben introducir en un array de 4 filas por 5 columnas.
El programa mostrará las sumas parciales de filas y columnas
igual que si de una hoja de cálculo se tratara.
La suma total debe aparecer en la esquina inferior derecha.
"""



matriz = [[random.randint(1, 100) for _ in range(5)] for _ in range(4)]

for row in matriz:
    print(row, sum(row))

# Inicializamos variables para sumar las columnas
col1 = 0
col2 = 0
col3 = 0
col4 = 0
col5 = 0

# Recorrer la matriz para sumar los elementos de cada columna
for col in matriz:
    col1 += col[0]
    col2 += col[1]
    col3 += col[2]
    col4 += col[3]
    col5 += col[4]
col = col1+col2+col3+col4+col5
print("Esta es la matriz", col1,col2,col3,col4,col5,col)