class ListOperator:
    def __init__(self):
        self.list_data = []

    def add_element(self, element):
        self.list_data.append(element)
        print("Element added successfully.")

    def show_elements(self):
        if self.list_data:
            print("Elements in the list:")
            for element in self.list_data:
                print(element)
        else:
            print("The list is empty.")


class DictManager:
    def __init__(self):
        self.dict_data = {}

    def add_element(self, key, value):
        self.dict_data[key] = value
        print("Element added successfully.")

    def show_elements(self):
        if self.dict_data:
            print("Elements in the dictionary:")
            for key, value in self.dict_data.items():
                print(f"Key: {key}, Value: {value}")
        else:
            print("The dictionary is empty.")


class TupleOperator:
    def __init__(self):
        self.tuple_data = ()

    def show_elements(self):
        if self.tuple_data:
            print("Elements in the tuple:")
            for element in self.tuple_data:
                print(element)
        else:
            print("The tuple is empty.")


class SetOperator:
    def __init__(self):
        self.set_data = set()

    def add_element(self, element):
        self.set_data.add(element)
        print("Element added successfully.")

    def show_elements(self):
        if self.set_data:
            print("Elements in the set:")
            for element in self.set_data:
                print(element)
        else:
            print("The set is empty.")


class MixOperator:
    def __init__(self):
        self.list_data = []
        self.dict_data = {}

    def add_to_list(self, element):
        self.list_data.append(element)
        print("Element added to the list successfully.")

    def add_to_dict(self, key, value):
        self.dict_data[key] = value
        print("Key-value pair added to the dictionary successfully.")

    def get_dict_values(self):
        return list(self.dict_data.values())


def main():
    list_operator = ListOperator()
    dict_manager = DictManager()
    tuple_operator = TupleOperator()
    set_operator = SetOperator()
    mix_operator = MixOperator()

    while True:
        print("\nMenu:")
        print("1. Gestor de Listas")
        print("2. Gestor de Diccionarios")
        print("3. Operador de Tuplas")
        print("4. Operador de Conjuntos")
        print("5. Gestor Mixto")
        print("6. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            print("\n Gestor de Listas:")
            list_operator.add_element(input("Ingrese un elemento: "))
            list_operator.show_elements()

        elif choice == "2":
            print("\nGestor de Diccionarios:")
            key = input("Ingrese la clave: ")
            value = input("Ingrese el valor: ")
            dict_manager.add_element(key, value)
            dict_manager.show_elements()

        elif choice == "3":
            print("\nOperador de Tuplas:")
            tuple_operator.show_elements()

        elif choice == "4":
            print("\nOperador de Conjuntos:")
            set_operator.add_element(input("Ingrese un elemento: "))
            set_operator.show_elements()

        elif choice == "5":
            print("\nGestor Mixto:")
            mix_operator.add_to_list(input("Ingrese un elemento para la lista: "))
            key = input("Ingrese la clave para el diccionario: ")
            value = input("Ingrese el valor para el diccionario: ")
            mix_operator.add_to_dict(key, value)
            print("Valores del diccionario:", mix_operator.get_dict_values())

        elif choice == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()