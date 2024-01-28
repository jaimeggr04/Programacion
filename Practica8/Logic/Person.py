from Practica8.Logic.Location import Location


class Person:
    def __init__(self, dni: str, name: str, age: int, gender: str, location: Location):
        self.__dni = dni
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__location = location

    def get_dni(self) -> str:
        return self.__dni

    def set_dni(self, dni: str):
        self.__dni = dni

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        self.__age = age

    def get_gender(self) -> str:
        return self.__gender

    def set_gender(self, gender: str):
        self.__gender = gender

    def get_location(self) -> Location:
        return self.__location

    def set_location(self, location: Location):
        self.__location = location

    def __str__(self):
        return f"Person(dni={self.get_dni()}, name={self.get_name()}, age={self.get_age()}, gender={self.get_gender()}, location={self.get_location()})"