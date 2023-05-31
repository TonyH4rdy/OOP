# Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:
# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy

# У лекторов:
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9

# У студентов :
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование

# 2) Реализуйте возможность сравнивать (через операторы сравнения)
# между собой лекторов по средней оценке за лекции и студентов по
# средней оценке за домашние задания.

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades_dict_lecturer = {}
        self.average_grade = 0


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_dict_student = {}
        self.average_grade = 0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def average_grade_student(self):
        grade_list = []
        for val in self.grades_dict_student.values():
            grade_list.extend(val)
        sum_ = sum(grade_list)
        self.average_grade = round(sum_/len(grade_list), 2)
        return self.average_grade

    def add_grades_lecturer(self, lecturer, course, grades):

        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and course in self.courses_in_progress:
            if course in lecturer.grades_dict_lecturer:
                lecturer.grades_dict_lecturer[course] += [grades]
            else:
                lecturer.grades_dict_lecturer[course] = [grades]
        else:
            print(f'Ошибка. Проверте , является ли  {lecturer.name} {lecturer.surname} экземпляром'
                  f' класса Student , входит ли "{course}" в список курсов , которые на данный момент'
                  f' изучает студент {lecturer.name} {lecturer.surname} '
                  f' и  является ли "{course}" - курсом , на котором преподаёт'
                  f' {self.name} {self.surname}')

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия : {self.surname}\nСредняя ' \
              f'оценка за ДЗ: {self.average_grade_student()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade < other.average_grade


class Lecturer(Mentor):

    def average_grade_lectures(self):
        grade_list = []
        for val in self.grades_dict_lecturer.values():
            grade_list.extend(val)
        sum_ = sum(grade_list)
        self.average_grade = round(sum_/len(grade_list), 2)
        return self.average_grade

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grade < other.average_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия : {self.surname}\nСредняя ' \
              f'оценка за лекции: {self.average_grade_lectures()}'
        return res


class Reviewer(Mentor):

    def add_grades_student(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades_dict_student:
                student.grades_dict_student[course] += [grades]
            else:
                student.grades_dict_student[course] = [grades]
        else:
            print(f'Ошибка. Проверте , является ли  {student.name} {student.surname} экземпляром'
                  f' класса Student , входит ли "{course}" в список курсов , которые на данный момент'
                  f' изучает студент {student.name} {student.surname} '
                  f' и  является ли "{course}" - курсом , на котором преподаёт'
                  f' {self.name} {self.surname}')

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


reviewer_1 = Reviewer('Some', 'Buddy')
print(reviewer_1)

(lecturer_1) = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached.append('Python')
lecturer_2 = Lecturer('Some', 'Buddy')
lecturer_2.courses_attached.append('Python')

student_1 = Student('Ruoy', 'Eman', 'gender')
student_1.courses_in_progress.append('Python')
student_2 = Student('name', 'surname', 'gender')
student_2.courses_in_progress.append('Python')
student_3 = Student('name', 'surname', 'gender')
student_3.courses_in_progress.append('Python')

student_1.add_grades_lecturer(lecturer_1, 'Python', 9)
student_2.add_grades_lecturer(lecturer_1, 'Python', 9)
student_3.add_grades_lecturer(lecturer_1, 'Python', 10)

student_1.add_grades_lecturer(lecturer_2, 'Python', 9)
student_2.add_grades_lecturer(lecturer_2, 'Python', 8)
student_3.add_grades_lecturer(lecturer_2, 'Python', 8)
print(lecturer_1)

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached.append('Python')

reviewer_1.add_grades_student(student_1, 'Python', 10)
reviewer_1.add_grades_student(student_1, 'Python', 9)
reviewer_1.add_grades_student(student_1, 'Python', 10)

reviewer_1.add_grades_student(student_2, 'Python', 8)
reviewer_1.add_grades_student(student_2, 'Python', 9)
reviewer_1.add_grades_student(student_2, 'Python', 9)


student_1.courses_in_progress.append('Git')
print(student_1.courses_in_progress)

student_1.finished_courses.append('Введение в программирование')
print(student_1)

# Средние оценки лекторов:
lecturer_1.average_grade = lecturer_1.average_grade_lectures()
lecturer_2.average_grade = lecturer_2.average_grade_lectures()

if lecturer_1 < lecturer_2:
    print('lecture_1 is a winner!')
else:
    print('lecturer_2 should not be upset!')


# Средние оценки студентов 1 и 2 :
student_1.average_grade = student_1.average_grade_student()
student_2.average_grade = student_2.average_grade_student()

if student_1 < student_2:
    print('student_2 is a winner!')
else:
    print('student_1 need to try better!')
