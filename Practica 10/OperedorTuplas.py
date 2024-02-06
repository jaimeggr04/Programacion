class TupleOperator:
    def __init__(self, tupla):
        self.tupla = tupla

    def traverse_tupla(self):
        print("Recorriendo elementos de la tupla:")
        for element in self.tupla:
            print(element)

    def generate_subtuplas_dos_en_dos(self):
        if len(self.tupla) % 2 == 0:
            print("Generando subtuplas de dos en dos:")
            for i in range(0, len(self.tupla), 2):
                print(self.tupla[i:i+2])
        else:
            print("No se puede generar subtuplas de dos en dos, la tupla tiene una longitud impar.")


tupla_ejemplo = (1, 2, 3, 4, 5, 6, 7, 8, 9)
operador = TupleOperator(tupla_ejemplo)

operador.traverse_tupla()
operador.generate_subtuplas_dos_en_dos()
