from Practica8.Logic.Subject import Subject
class Course:
    def __init__(self, type: str, year: int, description: str, code: int,  subjects:[Subject]):
        self.__type = type
        self.__year = year
        self.__description = description
        self.__code = code
        self.__subjects = subjects


    def get_subjects(self) -> [Subject]:
        return self.__subjects

    def set_subjects(self, subjects: [Subject]):
        self.__subjects = subjects

    def get_type(self) -> str:
        return self.__type

    def set_type(self, type: str):
        self.__type = type

    def get_year(self) -> int:
        return self.__year

    def set_year(self, year: int):
        self.__year = year

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str):
        self.__description = description

    def get_code(self) -> int:
        return self.__code

    def set_code(self, code: int):
        self.__code = code

    def __str__(self):
        return f"Course(type={self.get_type()}, year={self.get_year()}, description={self.get_description()}, code={self.get_code()})"
