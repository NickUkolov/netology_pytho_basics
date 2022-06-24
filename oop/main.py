class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_courses(self, course):
        self.finished_courses.append(course)
        self.courses_in_progress.remove(course)

    def add_course(self, course):
        self.courses_in_progress.append(course)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached and grade < 11:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def av_student_rate(self):
        sum_grade = []
        for course, grade in self.grades.items():
            sum_grade += grade
        return round(sum(sum_grade) / len(sum_grade), 1)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.av_student_rate()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __le__(self, other):
        if not isinstance(other, Student):
            return f'Это не студент!'
        return self.av_student_rate() <= other.av_student_rate()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return f'Это не студент!'
        return self.av_student_rate() >= other.av_student_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Средняя оценка за лекции: {self.av_lecture_rate()}'
        return res

    def av_lecture_rate(self):
        sum_grade = []
        for course, grade in self.grades.items():
            sum_grade += grade
        return round(sum(sum_grade) / len(sum_grade), 1)

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return f'Это не лектор!'
        return self.av_lecture_rate() <= other.av_lecture_rate()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return f'Это не лектор!'
        return self.av_lecture_rate() >= other.av_lecture_rate()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress and grade < 11:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Data
student_1 = Student('Alla', 'Puggacheva', 'F')
student_2 = Student('Boris', 'Eltsin', 'M')
students_list = [student_1, student_2]
lecturer_1 = Lecturer('Nikola', 'Tesla')
lecturer_2 = Lecturer('Elon', 'Musk')
lecturers_list = [lecturer_1, lecturer_2]
reviewer_1 = Reviewer('Jacob', 'Mahroff')
reviewer_2 = Reviewer('John', 'Weak')
student_1.add_course('Python')
student_2.add_course('Python')
lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Python']
reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Python']
student_1.rate_lecturer(lecturer_1, 'Python', 7)
student_1.rate_lecturer(lecturer_2, 'Python', 6)
student_2.rate_lecturer(lecturer_1, 'Python', 5)
student_2.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_2, 'Python', 4)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 6)
reviewer_2.rate_hw(student_1, 'Python', 4)


def av_student_course_rate(course, *students):
    res = []
    for student in students:
        if student.grades.get(course):
            res.extend(student.grades[course])
    return round(sum(res) / len(res), 1)


def av_lecturer_course_rate(course, *lecturers):
    res = []
    for lecturer in lecturers:
        if lecturer.grades.get(course):
            res.extend(lecturer.grades[course])
    return round(sum(res) / len(res), 1)


print(student_1, end='\n\n')
print(student_2, end='\n\n')
print(lecturer_1, end='\n\n')
print(lecturer_2, end='\n\n')
print(reviewer_1, end='\n\n')
print(reviewer_2, end='\n\n')

print(student_1 <= student_2)
print(student_1 >= student_2)
print(lecturer_1 >= lecturer_2)
print(lecturer_1 <= lecturer_2, end='\n\n')

course_ = 'Python'
print(f'Средняя оценка за домашние задания по всем студентам в курсе {course_}:')
print(av_student_course_rate(course_, student_1, student_2))
print(f'Средняя оценка за лекции всех лекторов в курсе {course_}:')
print(av_lecturer_course_rate(course_, lecturer_1, lecturer_2))
