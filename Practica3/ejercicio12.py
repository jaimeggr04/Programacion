"""
Pide al usuario dos pares de números x1,y2 y x2,y2, que representen
dos puntos en el plano. Calcula y muestra la distancia entre ellos.
"""

x1 = float(input("Escriba el numero x1: "))
x2 = float(input("Escriba el numero x2: "))
y1 = float(input("Escriba el numero y1: "))
y2 = float(input("Escriba el numero y2: "))
# Calcular la distancia entre los dos puntos en el plano utilizando la fórmula de distancia euclidiana
distance = (x1 - y1) + (x2 - y2)
print("La distancia entre los dos puntos es: ", distance)
