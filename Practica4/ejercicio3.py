"""
Algoritmo que pida dos números 'nota' y 'edad' y un carácter 'sexo' y muestre el mensaje 'ACEPTADA'
si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es 'F'. En caso
de que se cumpla lo mismo, pero el sexo sea 'M', debe imprimir 'POSIBLE'. Si no se cumplen dichas
condiciones se debe mostrar 'NO ACEPTADA'.
"""

grade = int(input("¿Cual es su nota?: "))
age = int(input("¿Cual es su edad?: "))
gender = str(input("¿Cual es su genero?"))

# Verificar si la nota es mayor o igual a 5, la edad es mayor o igual a 18 y el género es "F"
if grade >= 5 and age >= 18 and gender == "F":
    print("ACEPTADA")
# Verificar si la nota es mayor o igual a 5, la edad es mayor o igual a 18 y el género es "M"
if grade >= 5 and age >= 18 and gender == "M":
    print("POSIBLE")
else:
    print("NO ACEPTADA")
