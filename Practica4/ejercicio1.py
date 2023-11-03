"""
Escribe un programa que pida un nombre de usuario y una
contraseña y si se ha introducido "pepe" y "asdasd" se indica
"Has entrado al sistema", sino se da un error.
"""
#Utilizamos input para que nos pida por teclado.
user = input("Escriba el usuario:")
password = input("Escriba su contraseña:")
#Usamos if para comprobar que el usaurio y contraseña sean correctas
if user=="pepe" and password=="asdasd":
    print("Has entrado al sistema")
else:
    print("Error")

