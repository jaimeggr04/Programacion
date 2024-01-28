from Practica8.Logic.Location import Location
from Practica8.Logic.Course import Course


class School:
    def __init__(self, name: str, cif: int, location: Location, courses: [Course]):
        self.__name = name
        self.__cif = cif
        self.__location = location
        self.__courses = courses

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_cif(self) -> int:
        return self.__cif

    def set_cif(self, cif: int):
        self.__cif = cif

    def get_location(self) -> Location:
        return self.__location

    def set_location(self, location: Location):
        self.__location = location

    def get_courses(self) -> [Course]:
        return self.__courses

    def set_courses(self, courses: [Course]):
        self.__courses = courses

    def __str__(self):
        return f"School(name={self.get_name()}, cif={self.get_cif()}, location={self.get_location()}, courses={self.get_courses()})"
