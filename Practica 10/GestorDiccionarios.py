class GestorDiccionarios:
    def __init__(self):
        self.dictionary = {}

    def add_element(self, key, value):
        self.dictionary[key] = value
        print("Element added successfully.")

    def update_element(self, key, new_value):
        if key in self.dictionary:
            self.dictionary[key] = new_value
            print("Elemento actualizado con exito.")


    def delete_element(self, key):
        if key in self.dictionary:
            del self.dictionary[key]
            print("Elemento eliminado correctramente")

    def show_elements(self):
        if self.dictionary:
            print("Elementos en el diccionario:")
            for key, value in self.dictionary.items():
                print(f"Key: {key}, Value: {value}")

    def iterate_dictionary(self):
        if self.dictionary:
            for key, value in self.dictionary.items():
                print(f"Key: {key}, Value: {value}")



gestor = GestorDiccionarios()

gestor.add_element("a", 1)
gestor.add_element("b", 2)
gestor.add_element("c", 3)

gestor.show_elements()

gestor.update_element("b", 4)
gestor.show_elements()

gestor.delete_element("c")
gestor.show_elements()