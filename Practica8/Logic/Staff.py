from Practica8.Logic.Person import Person
from Practica8.Logic.Location import Location
from datetime import datetime
from datetime import datetime

class Staff(Person):
    def __init__(self, dni: str, name: str, age: int, gender: str, location: Location, role: str, salary: float, startingDate: datetime):
        super().__init__(dni, name, age, gender, location)
        self.__role = role
        self.__salary = salary
        self.__startingDate = startingDate

    def get_role(self) -> str:
        return self.__role

    def set_role(self, role: str):
        self.__role = role

    def get_salary(self) -> float:
        return self.__salary

    def set_salary(self, salary: float):
        self.__salary = salary

    def get_startingDate(self) -> datetime:
        return self.__startingDate

    def set_startingDate(self, startingDate: datetime):
        self.__startingDate = startingDate

    @property
    def __str__(self):
        return f"Staff({super().__str__()}, role={self.get_role()}, salary={self.get_salary()}, startingDate={self.get_startingDate()})"


def net_salary(self, retention: float) -> float:
    return self.__salary * (1 - retention)

def calculate_years_teachers(self) -> int:
        current_year = datetime.now().year
        years_old = current_year - self
        return years_old