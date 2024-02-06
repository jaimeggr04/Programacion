class SetOperator:
    def __init__(self):
        self.set_data = set()

    def add_element(self, element):
        self.set_data.add(element)
        print("Elemento añadido correctamente.")

    def update_element(self, old_element, new_element):
        if old_element in self.set_data:
            self.set_data.remove(old_element)
            self.set_data.add(new_element)
            print("Elemento actualizado correctamente.")

    def delete_element(self, element):
        if element in self.set_data:
            self.set_data.remove(element)
            print("Elemento eliminado correctamente")

    def show_elements(self):
        if self.set_data:
            for element in self.set_data:
                print(element)


    def union_sets(self, other_set):
        union_result = self.set_data.union(other_set)
        return union_result


set_operator = SetOperator()

set_operator.add_element(1)
set_operator.add_element(2)
set_operator.add_element(3)

set_operator.show_elements()

set_operator.update_element(2, 4)
set_operator.show_elements()

set_operator.delete_element(3)
set_operator.show_elements()

set2 = {3, 4, 5}
union_result = set_operator.union_sets(set2)
