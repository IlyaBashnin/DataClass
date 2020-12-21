'''
    This is Home Work 4
    Создать абстрактный базовый класс Person, описывающий
    обычного человека. Создайте производный класс Student, описывающий
    типичного студента. От класса Student наследуйте класс GradStudent,
    описывающий типичного аспиранта. Все классы должны содержать функции
    получения и изменения всех полей. Написать программу, позволяющую
    получать сведения о студентах и аспирантах.
'''

from dataclasses import dataclass
import json
from pprint import pprint

BASE_PATH = 'Baze.json'
BASE_GRANT = 100


@dataclass
class Person:
    id: int
    first_name: str
    second_name: str
    age: int
    city: str

    def whomi(self):
        print(f"id: {self.id} || I'm {self.first_name} {self.second_name}, from {self.city}.({self.age} y.o.)")

    def change_name(self, new_data: list) -> None:
        old_name = [self.first_name, self.second_name]
        self.first_name = new_data[0]
        self.second_name = new_data[1]
        print(f"id: {self.id} || {old_name} change to - {self.first_name} {self.second_name}.")


@dataclass
class Student(Person):
    institute: str
    years: int
    rating: float
    grants: float

    def get_stud_data(self) -> list:
        try:
            with open(BASE_PATH, encoding='utf-8') as filestudent:
                students = []
                data = json.load(filestudent)
                for student in data['students']:
                    students.append(Student(student['id'], student['first_name'], student['second_name'],
                                            student['age'], student['city'], student['institute'],
                                            student['years'], float(student['rating']), float(student['grants'])
                                            ))
                print('|| Students base loaded ||')
        except IOError as Error:
            print('Operation failed: %s' % Error.strerror)
        return students

    def count_rating(self, gradelist: list) -> None:
        rating = round(sum(gradelist) / len(gradelist), 1)
        self.rating = rating
        if rating >= 10:
            grants = 2.00
        elif 10 > rating >= 9:
            grants = 1.75
        elif 9 > rating >= 8:
            grants = 1.50
        elif 8 > rating >= 7:
            grants = 1.25
        elif 7 > rating >= 6:
            grants = 1.00
        else:
            grants = 0.00
        self.grants = grants

    def get_grant(self):
        print(f"id: {self.id} || {self.first_name} {self.second_name} "
              f"grant: {BASE_GRANT * self.grants}({self.grants} rate) ")


@dataclass
class GrandStudent(Student):
    conferences: list = []
    publications: list = []
    stud_progress: int

    def get_gstud_data(self) -> list:
        try:
            with open(BASE_PATH, encoding='utf-8') as filegstudent:
                grand_students = []
                data = json.load(filegstudent)
                for gstudent in data['gstudents']:
                    grand_students.append(GrandStudent(gstudent['id'], gstudent['first_name'],
                                                       gstudent['second_name'], gstudent['age'],
                                                       gstudent['city'], gstudent['institute'],
                                                       gstudent['years'], float(gstudent['rating']),
                                                       float(gstudent['grants']), gstudent['conferences'],
                                                       gstudent['publications'], int(gstudent['stud_progress']))
                                                       )
                print('|| Grand Students base loaded... ||')
        except IOError as Error:
            print('Operation failed: %s' % Error.strerror)
        return grand_students

    def new_conferense(self, conference_name: str) -> None:
        self.conferences.append(conference_name)
        self.stud_progress += 1

    def new_publication(self, publication_title: str) -> None:
        self.publications.append(publication_title)
        self.stud_progress += 1

    def get_progress(self) -> None:
        if self.stud_progress >= 10:
            print(f"id: {self.id} || {self.first_name} {self.second_name} ready to defend the candidate work."
                  f"Admission conditions met: "
                  f"Grand Student participated in {len(self.conferences)} conferences: {self.conferences}"
                  f"Grand Student student published {len(self.publications)} articles: {self.publications}"
                  )
        else:
            print(f"id: {self.id} || {self.first_name} {self.second_name} not ready to defend the candidate work.")

if __name__ == '__main__':
    students = Student.get_stud_data(Student)
    grand_students = GrandStudent.get_gstud_data(GrandStudent)
    for student in students:
        student.whomi()
        student.get_grant()
    for grand_student in grand_students:
        grand_student.whomi()
        grand_student.get_grant()
        grand_student.get_progress()
    students[4].count_rating([3,4,4,10])
    students[4].get_grant()
    for i in range(10):
        grand_students[4].new_publication('Publication')
    grand_students[4].get_progress()

