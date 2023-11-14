class usuario:


    "Creamos el constructor"
    def __init__(self, name, subName, pCode, address, email, password):
        self.name = name
        self.subName = subName
        self.pCode = pCode
        self.address = address
        self.email = email
        self.password = password


    "Creamos los metodos"
    def mostrarUsuario(self):
        return self.name+", "+self.subName+", "+str(self.pCode)+", "+self.address+", "+self.email+", "+self.password

    "Creamos el check"
    def check(self):
        res = "Nombre y contraseña incorrectos"
        n = input("Introduzca su nombre: ")
        p = input("Introduzca su contraseña: ")
        if n == self.name and p == self.password:
            res = "Has inicaido sesion correctamente"
        print(res)
