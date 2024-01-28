from Practica8.Logic.Course import Course
from Practica8.Logic.Department import Department
from Practica8.Logic.Grade import Grade
from Practica8.Logic.Location import Location
from Practica8.Logic.Person import Person
from Practica8.Logic.School import School
from Practica8.Logic.Staff import Staff
from Practica8.Logic.Student import Student
from Practica8.Logic.Subject import Subject
from Practica8.Logic.Teacher import Teacher
from Practica8.Data.Populate import *
from Practica8.Data.Create import *
#Llamado a funciones de Create y Populate
def presentable():
    courses, departments, grades, locations, students, persons, staffs, subjects, teachers, schools = populate()
    l = Location("Main Street", 123, 12345, "City", "Michigan")
    p = Person("78106667R", "Pablo", 21, "M", l)
    print(p.__str__())
    subject1 = Subject("Matemáticas I", 101, "Introducción al cálculo y álgebra", 4.0)
    location1 = Location("Calle A", 123, 12345, "Ciudad A", "Provincia A")
    department1 = Department(1, "Departamento de Matemáticas")
    teacher1 = Teacher("123456789", "Juan Pérez", 35, "Masculino", location1, 60000.0, datetime(2021, 9, 1), subject1,
                       department1)
    print(teacher1.net_salary(0.3))

    print("Las opciones posibles que tienes son estas: \n")
    print("- Crear Profesor")
    print ("- Crear alumno")


    orden = input("Que orden quieres hacer: ")
    if orden == "Crear profesor":
        create_teacher(teachers, locations, subjects, departments)
    elif orden == "Crear Escuela":
        create_school(schools, locations, courses)
    elif orden == "Crear Profesor":
        create_teacher(teachers, locations, subjects, departments)
    elif orden == "Crear curso":
        create_course(courses)
    elif orden == "Crear departamento":
        create_department(departments)
    elif orden == "Crear grado":
        create_grade(grades, subjects)
    elif orden == "Crear localizacion":
        create_location(locations)












