class GestorListas:
    def __init__(self):
        self.list = []

    def add_element(self, element):
        self.list.append(element)
        print("Elemento añadidio con exito.")

    def update_element(self, index, new_element):
        if 0 <= index < len(self.list):
            self.list[index] = new_element
            print("Elemento actualizado con exito.")


    def delete_element(self, index):
        if 0 <= index < len(self.list):
            del self.list[index]
            print("Elemento borrado con exito.")

    def show_elements(self):
        if self.list:
            print("El elemento esta en la lista:")
            for element in self.list:
                print(element)


    def square_elements(self):
        squared_list = [element ** 2 for element in self.list]
        return squared_list


# Función para manejar la interacción con el usuario
def interact_with_list_manager():
    manager = GestorListas()
    while True:
        print("\n1. Introduce un nuevo elemento")
        print("2. Actualiza el elemento")
        print("3. DElimina el elemento")
        print("4. Muestra el elemento")
        print("5. Eleva el elemento")
        print("6. Salir")
        option = input("Select an option: ")

        if option == "1":
            element = int(input("Escribe el elemento para añadirlo: "))
            manager.add_element(element)
        elif option == "2":
            index = int(input("Escribe el indice para que se actualize: "))
            new_element = int(input("Ingresa el nuevo valor: "))
            manager.update_element(index, new_element)
        elif option == "3":
            index = int(input("Ingrese el indice del elemento a eliminar: "))
            manager.delete_element(index)
        elif option == "4":
            manager.show_elements()
        elif option == "5":
            squared_elements = manager.square_elements()
            print("List con elementos al cuadrado: ", squared_elements)
        elif option == "6":
            print("Salir...")
            break
        else:
            print("Opcion incorrecta: ")



gestor = GestorListas()

gestor.add_element(2)
gestor.add_element(4)
gestor.add_element(6)

gestor.show_elements()

gestor.update_element(1, 8)

gestor.show_elements()

gestor.delete_element(2)

gestor.show_elements()

nueva_lista_cuadrados = gestor.square_elements()
print("Lista con elementos elevados al cuadrado:", nueva_lista_cuadrados)

