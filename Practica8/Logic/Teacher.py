from Practica8.Logic.Person import Person
from Practica8.Logic.Subject import Subject
from Practica8.Logic.Department import Department
from Practica8.Logic.Location import Location
from datetime import datetime


class Teacher(Person):
    def __init__(self, dni: str, name: str, age: int, gender: str, location: Location, salary: float,
                 startingDate: datetime, subject: Subject, department: Department):
        super().__init__(dni, name, age, gender, location)
        self.__salary = salary
        self.__startingDate = startingDate
        self.__subject = subject
        self.__department = department

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_startingDate(self):
        return self.__startingDate

    def set_startingDate(self, startingDate):
        self.__startingDate = startingDate

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject):
        self.__subject = subject

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department


from Practica8.Logic.Person import Person
from Practica8.Logic.Subject import Subject
from Practica8.Logic.Department import Department
from Practica8.Logic.Location import Location
from datetime import datetime


class Teacher(Person):
    def __init__(self, dni: str, name: str, age: int, gender: str, location: Location, salary: float,
                 startingDate: datetime, subject: Subject, department: Department):
        super().__init__(dni, name, age, gender, location)
        self.__salary = salary
        self.__startingDate = startingDate
        self.__subject = subject
        self.__department = department

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_startingDate(self):
        return self.__startingDate

    def set_startingDate(self, startingDate):
        self.__startingDate = startingDate

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject):
        self.__subject = subject

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def __str__(self):
        return f"Teacher({super().__str__()}, salary={self.get_salary()}, startingDate={self.get_startingDate()}, subject={self.get_subject()}, department={self.get_department()})"

    def net_salary(self, retention: float) -> float:
        return self.__salary * (1 - retention)

    @staticmethod
    @property
    def calculate_years_teachers(self) -> int:
        current_year = datetime.now().year
        years_old = current_year - self
        return years_old
