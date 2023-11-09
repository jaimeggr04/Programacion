"""
Una tienda ofrece un descuento del 15% sobre el total de la compra
y un cliente desea saber cuánto deberá pagar finalmente por su compra.
"""

total = float(input("Escriba el total de su compra: "))
# Calcular el descuento, que es el 15% del total de la compra
discount = (15 / 100) * total
print("Debera pagar cone el descuento lo siguiente: ", discount)
