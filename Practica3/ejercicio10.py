"""
Pide al usuario dos números y muestra la "distancia" entre ellos
(el valor absoluto de su diferencia, de modo que el resultado sea
siempre positivo).
"""
numb1 = float(input("Escribe el numero 1: "))
numb2 = float(input("Escribe el numero 2: "))
# Calcular la "distancia" entre los dos números como el valor absoluto de su diferencia
distance = abs(numb1-numb2)

print("La distancia entre el numero 1 y el numero 2 es: ",distance)

