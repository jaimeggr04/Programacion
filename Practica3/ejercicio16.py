
"""
Diseñar un algoritmo que nos diga el dinero que tenemos
(en euros y céntimos) después de pedirnos cuantas monedas tenemos
de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

"""

one = int(input("Introduce la cantidad de monedas de 2 euros: "))
two = int(input("Introduce la cantidad de monedas de 1 euro: "))
half = int(input("Introduce la cantidad de monedas de 50 centimos: "))
fifth = int(input("Introduce la cantidad de monedas de 20 centimos: "))
tenth = int(input("Introduce la cantidad de monedas de 10 centimos: "))
# Calcular el total de dinero en euros y céntimos
total = two * 2 + one + float(half * 0.5) + float(0.2) + float(tenth * 0.1)

print("Tienes", total, "€")



