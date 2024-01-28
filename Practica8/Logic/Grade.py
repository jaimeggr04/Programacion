from Practica8.Logic.Student import Student
from Practica8.Logic.Subject import Subject


class Grade:
    def __init__(self, student: Student, subject: Subject, calification: float):
        self.__student = student
        self.__subject = subject
        self.__calification = calification

    def get_student(self) -> Student:
        return self.__student

    def set_student(self, student: Student):
        self.__student = student

    def get_subject(self) -> Subject:
        return self.__subject

    def set_subject(self, subject: Subject):
        self.__subject = subject

    def get_calification(self) -> float:
        return self.__calification

    def set_calification(self, calification: float):
        self.__calification = calification

    def __str__(self):
        return f"Grade(student={self.get_student()}, subject={self.get_subject()}, calification={self.get_calification()})"
