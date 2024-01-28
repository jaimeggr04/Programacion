from Practica8.Logic.Person import Person
from Practica8.Logic.Course import Course
from Practica8.Logic.Location import Location


class Student(Person):
    def __init__(self, dni: str, name: str, age: int, gender: str, location: Location, email: str, course: Course,):
        super().__init__(dni, name, age, gender, location)
        self.__email = email
        self.__course = course


    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    def get_course(self) -> Course:
        return self.__course

    def set_course(self, course: Course):
        self.__course = course



    def __str__(self):
        return f"Student({super().__str__()}, email={self.get_email()}, course={self.get_course()})"
