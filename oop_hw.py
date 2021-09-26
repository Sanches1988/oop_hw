class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_score = 0
        stud_lst.append(self.__dict__)

    def __lt__(self, other): 
        if not isinstance(other, Student):
            print('Нет такого студента')
            return
        return self.average_score < other.average_score

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.average_score} \n' \
               f'Курсы в процессе изучения: {self.courses_in_progress} \n' \
               f'Завершенные курсы: {self.finished_courses}'

    def rate_lecture(self, lekture, course, grade):
        if isinstance(lekture, Lecturer) and course in self.courses_in_progress and course in lekture.courses_attached:
            lekture.grades += [grade]
            lekture.average_score = round(sum(lekture.grades) / len(lekture.grades), 1)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        self.grades = []
        self.average_score = 0
        super().__init__(name, surname)
        lekt_lst.append(self.__dict__)

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {self.average_score}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.average_score < other.average_score

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            sum_hw = 0
            counter = 0
            for k, v in student.grades.items():
                sum_hw += sum(v) / len(v)
                counter += 1
            student.average_score = round(sum_hw / counter, 1)


def average_grade_hw(students, courses):
    sum_gh = 0
    counter = 0
    for student in students:
        for key, value in student['grades'].items():
            if courses in key:
                sum_gh += sum(value) / len(value)
                counter += 1
    return round(sum_gh / counter, 1)

def average_grade_lecture(lecturers, courses):
    sum_gl = 0
    counter = 0
    for lekture in lecturers:
        if courses in lekture["courses_attached"]:
           sum_gl += sum(lekture["grades"]) / len(lekture["grades"])
           counter += 1
    return round(sum_gl / counter, 1)

stud_lst = []
lekt_lst = []

first_student = Student('George', 'Bush', 'male')
first_student.courses_in_progress += ['C++']
first_student.finished_courses += ['Java']
second_student = Student('Nicola', 'Sarkozi', 'male')
second_student.courses_in_progress += ['Java']
second_student.courses_in_progress += ['C++']


first_lecturer = Lecturer('Condoleezza', 'Rice')
first_lecturer.courses_attached += ['C++']

second_lecturer = Lecturer('Angela', 'Merkel')
second_lecturer.courses_attached += ['Java']

first_reviewer = Reviewer('Barak', 'Obama')
first_reviewer.courses_attached += ['Java']

second_reviewer= Reviewer('Donald', 'Tramp')
second_reviewer.courses_attached += ['C++']


first_reviewer.rate_hw(first_student, 'Java', 7)
first_reviewer.rate_hw(first_student, 'Java', 6)
first_reviewer.rate_hw(first_student, 'Java', 9)
first_reviewer.rate_hw(second_student, 'Java', 8)

second_reviewer.rate_hw(first_student, 'C++', 9)
second_reviewer.rate_hw(first_student, 'C++', 7)
second_reviewer.rate_hw(first_student, 'C++', 5)
second_reviewer.rate_hw(first_student, 'C++', 6)

first_student.rate_lecture(first_lecturer, 'C++', 6)
first_student.rate_lecture(first_lecturer, 'C++', 8)
second_student.rate_lecture(first_lecturer, 'C++', 7)
second_student.rate_lecture(first_lecturer, 'C++', 8)

first_student.rate_lecture(second_lecturer, 'Java', 8)
first_student.rate_lecture(second_lecturer, 'Java', 5)
second_student.rate_lecture(second_lecturer, 'Java', 4)
second_student.rate_lecture(second_lecturer, 'Java', 7)


print(first_student)
print(second_student)
print(second_lecturer)
print(first_lecturer)
print(first_reviewer)
print(second_reviewer)
print('--------------------------------------------')
print(f"Средняя оценка за домашние задания по всем студентам в рамках конкретного курса: {average_grade_hw(stud_lst, 'C++')}")
print(f"Средняя оценка за лекции всех лекторов в рамках курса: {average_grade_lecture(lekt_lst, 'Java')}")
print('--------------------------------------------')
print(first_lecturer < second_lecturer)
print(second_student > first_student)