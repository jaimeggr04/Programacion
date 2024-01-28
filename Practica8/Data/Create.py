from Practica8.Logic.Course import Course
from Practica8.Logic.Department import Department
from Practica8.Logic.Grade import Grade
from Practica8.Logic.Staff import Staff
from Practica8.Logic.Student import Student
from Practica8.Logic.Subject import Subject
from Practica8.Logic.Teacher import Teacher
from Practica8.Logic.Location import Location
from Practica8.Logic.Person import Person
from Practica8.Logic.School import School
from datetime import datetime

def create_student(students, locations, courses, subjects):
    dni = input("Introduce el DNI: ")
    name = input("Introduce tu nombre: ")
    age = int(input("Introduce tu edad: "))
    gender = input("¿Cual es tu genero?: ")
    id_location = input("Introduce tu id direccion: ")
    location = check_location(id_location, locations)
    if location is None:
        location =create_location(locations)
    email = input("introduce tu Email: ")
    code_course = input("introduce el id del curso")
    course = check_course(code_course, courses)
    if course is None:
        course = create_course(courses)
    student = Student(dni, name, age, gender, location, email, course, subjects, )
    students.add(dni, student)
    return student

def check_student(dni, students):
    res = None
    for k in students:
        if dni == k.key():
            res = k.value
        return res

def create_location(locations):
    id_location = input("Introduce tu id direccion: ")
    street = input("Introduce tu calle: ")
    number = int(input("Introduce tu numero de tu calle: "))
    postalcode= int(input("Introduce tu codigo postal"))
    place = input("Introduce tu ciudad: ")
    province = input("Introduce tu provincia: ")
    location = Location(street, number, postalcode, place, province)
    locations.add(id, location)
    return location

def check_location(id, locations):
    res = None
    for k in locations:
        if id == k.key():
            res = k.value
        return res

def create_school(schools, locations, courses):
    cif = input("Introduce tu cif: ")
    id_location = input("Introduce tu id direccion: ")
    location = check_location(id_location, locations)
    if location is None:
        location = create_location(locations)

    code_course = input("introduce el id del curso")
    course = check_course(code_course, courses)
    if course is None:
        course = create_course(courses)
    school = School(cif, location, course)
    schools.add(cif, school)
    return school

def check_teacher(cif, locations):
    res = None
    for k in locations:
        if cif == k.key():
            res = k.value
        return res


def create_course(courses):
    type = input("Elige tu tipo: ")
    year = int(input("Introduce el año: "))
    description = input("Escriba la descripcion: ")
    code = int(input("Introduce el codigo: "))

    course = Course(type, year, description, code)
    courses.add(code, course)
    return course

def check_course(code, courses):
    res = None
    for k in courses:
        if code == k.key():
            res = k.value
        return res

def create_subject(subjects):
    name = input("Introduce tu nombre: ")
    id = int(input("Intruduce el id: "))
    description = input("Escriiba la descripcion: ")
    credits = float(input("Escriba el codigo: "))

    subject = Subject(name, id, description, credits)
    subjects.add(id, subject)
    return subject

def check_subject(id, subjects):
    res = None
    for k in subjects:
        if id == k.key():
            res = k.value
        return res

def create_staff(staffs, locations):
    dni = input("Introduce un dni: ")
    name = input("Introduce un nombre: ")
    age = int(input("Introduce una edad: "))
    gender = input("Introduce un genero: ")
    id_location = input("Introduce una direccion: ")
    location = check_location(id_location, locations)
    if location is None:
        location = create_location(locations)
    role = input("Introduce un rol: ")
    salary = float(input("Introduce una direccion: "))
    starting_date = datetime.strptime(input("Introduce una fecha: "), '%Y-%m-%d')
    staff = Staff(dni, name, age, gender, location, role, salary, starting_date)
    staffs.add(dni, staff)
    return staff

def check_staff(dni, staffs):
    res = None
    for k in staffs:
        if dni == k.key():
            res = k.value
        return res


def create_teacher(teachers, locations, subjects, departments):
    dni = input("Introduce un dni: ")
    name = input("Introduce un nombre: ")
    age = int(input("Introduce una edad: "))
    gender = input("Introduce un genero: ")
    id_location = input("Introduce una direccion: ")
    location = check_location(id_location, locations)
    if location is None:
        location = check_location(locations)
    salary = float(input("Introduce una direccion: "))
    starting_date = datetime.strptime(input("Introduce una fecha: "), '%Y-%m-%d')
    code_subject = input("Introduce el codigo de asignatura: ")
    subject = check_subject(code_subject, subjects)
    if subject is None:
        subject = create_subject(subjects)
    id_departament = input("Introduce su departamento: ")
    departament = check_departament(id_departament, departments)
    if departament is None:
        departament = create_department(departments)
    teacher = Teacher(dni, name, age, gender, location, salary, starting_date, subject, departament)
    teachers.add(dni, teacher)
    return teacher

def check_teacher(dni, teachers):
    res = None
    for k in teachers:
        if dni == k.key():
            res = k.value
        return res
def create_grade(grades, subjects):
    id = int(input("Intruduce el id: "))
    student = input("Introduce un estudiante: ")
    code_subject = input("Introduce el codigo de asignatura: ")
    subject = check_subject(code_subject, subjects)
    if subject is None:
        subject = create_subject(subjects)
    calification = float(input("Introduce una calificacion: "))
    grade = Grade(student, subject, calification)
    grades.add(id, grade)
    return grade

def check_grade(id, grades):
    res = None
    for k in grades:
        if id == k.key():
            res = k.value
        return res

def create_department(departments):
    id = int(input("Introduce un id: "))
    name = input("Introduce un nombre: ")
    department = Department(id, name)
    departments.add(id, department)
    return department

def check_departament(id, departaments):
    res = None
    for k in departaments:
        if id == k.key():
            res = k.value
        return res
