"""
Realiza un programa que pida por teclado el resultado (dato entero)
obtenido al lanzar un dado de seis caras y muestre por pantalla el número
en letras (dato cadena) de la cara opuesta al resultado obtenido.

"""
full_dice = int(input("Introduzca el numero del dado: "))
#Asociar el número del dado con el resultado del lanzamiento del dado
if full_dice == 1:
    print("Seis")
elif full_dice == 2:
    print("Cinco")
elif full_dice == 3:
    print("Cuatro")
elif full_dice ==4:
    print("Tres")
elif full_dice == 5:
    print("Dos")
elif full_dice == 6:
    print("Uno")
else:
    print("ERROR: número incorrecto")