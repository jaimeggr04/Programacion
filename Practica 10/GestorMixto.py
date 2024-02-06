class GestorMixto:
    def __init__(self):
        self.list = []
        self.index = {}

    def add_element_list(self, element):
        self.index.append(element)
        print("Elemento agregado a la lista correctamente.")

    def add_par_keys_value_index(self, clave, valor):
        self.index[clave] = valor
        print("Par clave-valor agregado al diccionario correctamente.")

    def get_values_index(self):
        return list(self.index.values())

gestor = GestorMixto()

gestor.add_element_list(1)
gestor.add_element_list(2)
gestor.add_element_list(3)

gestor.add_par_keys_value_index("a", 10)
gestor.add_par_keys_value_index("b", 20)
gestor.add_par_keys_value_index("c", 30)

print("Valores del diccionario:", gestor.get_values_index())