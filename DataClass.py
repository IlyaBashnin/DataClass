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
BASE_GRANT = 100500

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
                                            student['years'], student['rating'], student['grants']
                                            ))
                print('|| Students base loaded ||')
        except IOError as Error:
            print('Operation failed: %s' % Error.strerror)
        return students

    def count_studentrating(self, gradelist: list) -> None:
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

    def get_student_grant(self):
        pass;

@dataclass
class GrandStudent(Student):
    conferences: list
    publications: list
    aspirat_progress: int


    def get_gstud_data(self) -> list:
        try:
            with open(BASE_PATH, encoding='utf-8') as filegstudent:
                grand_students = []
                data = json.load(filegstudent)
                for gstudent in data['gstudents']:
                    grand_students.append(GradStudent(gstudent['id'], gstudent['first_name'], gstudent['second_name'],
                                            gstudent['age'], gstudent['city'], gstudent['institute'],
                                            gstudent['years'], gstudent['rating'], gstudent['grants'],
                                            gstudent['conferences'], gstudent['publications'], gstudent['aspirant_progress']
                                            ))
                print('|| Grand Students base loaded... ||')
        except IOError as Error:
            print('Operation failed: %s' % Error.strerror)
        return grand_students

    def new_conferense(self, conference_name: str) -> None:
        pass

    def new_publication(self, publication_name: str) -> None:
        pass

    def __update_progress(self) -> None:
        pass

    def get_progress(self):
        pass



if __name__ == '__main__':
    students = Student.get_stud_data(Student)
    grand_students = GrandStudent.get_gstud_data(GrandStudent)
    for student in students:
        student.whomi()
    for grand_student in grand_students:
        grand_student.whomi()

    pprint(students)
    pprint(grand_students)