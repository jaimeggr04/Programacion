"""
Algoritmo que pida tres números y los
muestre ordenados (de mayor a menor)
"""

numb1 = int(input("Escribe el numero 1: "))
numb2 = int(input("Escribe el numero 2: "))
numb3 = int(input("Escribe el numero 3: "))
# Comprobar las posibles combinaciones de orden de los números e imprimir el resultado
if numb1>=numb2 and numb2>=numb3:
    print("Este seria el orden de los numeros", numb1,numb2,numb3)
if numb1>=numb3 and numb3>numb2:
    print("Este seria el orden de los numeros", numb1,numb3,numb2)
if numb2>numb1 and numb1>=numb3:
     print("Este seria el orden de los numeros", numb2,numb1,numb3)
if numb2>=numb3 and numb3>numb1:
     print("Este seria el orden de los numeros", numb2,numb3,numb1)
if numb3>numb1 and numb1>=numb2:
     print("Este seria el orden de los numeros", numb3,numb1,numb2)
if numb3>numb2 and numb2>numb1:
     print("Este seria el orden de los numeros", numb3,numb2,numb1)
