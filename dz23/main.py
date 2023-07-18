"""
СОздать класс студент
атрибуты:
имя
группа
средний балл

Создать список из 10 студентов
показать всех студентов из одной группы,
отсортировать студентов по среднему баллу
осортировать студенту по имени

"""
from Students import *
import random as r

students_list = []
name_list = ['Ivan Ivanov', 'Petr Petrov', 'Vanya Ivanov']
group_list = ['p123', 'q24', 'q333', 't96']
id_studs = []
quant_studs = 10


def id_generator(quant_studs: int = 0):
    for id in range(1, quant_studs + 1):
        id_studs.append(id)


id_generator(quant_studs)

for i in range(quant_studs):
    student = Student(name_list[r.randint(0, 2)],
                      group_list[r.randint(0, 3)],
                      r.randint(0, 100), id_studs[i])
    students_list.append(student)
groups = []

# groups_for_search = 'p123'
# for student in students_list:
#     if student.group == groups_for_search:
#         student.show()
#         print('\n')

students_gpa = []

# for j in range(len(students_list) - 1):
#     for i in range(len(students_list) - 1):
#         if students_list[i].gpa < students_list[i + 1].gpa:
#             students_list[i], students_list[i + 1] = students_list[i + 1], students_list[i]

for j in range(len(students_list) - 1):
    for i in range(len(students_list) - 1):
        if students_list[i].id < students_list[i + 1].id:
            students_list[i], students_list[i + 1] = students_list[i + 1], students_list[i]
for student in students_list:
    student.show()
