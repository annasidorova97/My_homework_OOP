student_list = []
lecturer_list = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        student_list.append(self)

    def average_rating(self):
        all_grades = []
        if self.grades == {}:
            return 'у студента пока нет оценок'
        else:
            for key, value in self.grades.items():
                all_grades += value
            return f'{sum(all_grades) / len(all_grades)}'

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.average_rating()}
Курсы в процессе изучения: {', '.join(self.courses_in_progress)}
Завершенные курсы: {', '.join(self.finished_courses)}'''
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.average_rating() < other.average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturer_list.append(self)

    def average_rating(self):
        all_grades = []
        if self.grades == {}:
            return 'У лектора пока нет оценок'
        else:
            for key, value in self.grades.items():
                all_grades += value
            return f'{sum(all_grades) / len(all_grades)}'

    def __str__(self):
        text = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_rating()}'''
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.average_rating() < other.average_rating()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f'Имя: {self.name}\nФамилия: {self.surname}'
        return text


student1 = Student('Anna', 'Sidorova', 'f')
student2 = Student('Bob', 'Stanford', 'm')
lecturer1 = Lecturer('Tom', 'Ford')
lecturer2 = Lecturer('Shane', 'Helen')
reviewer1 = Reviewer('Vera', 'Stone')
reviewer2 = Reviewer('Sara', 'Robinson')

student1.add_courses('Git')
student1.courses_in_progress += ['Python', 'C++']

student2.courses_in_progress += ['Python', 'Git']

lecturer1.courses_attached += ['Python', 'C++', 'CSS']
lecturer2.courses_attached += ['Python', 'Git']

reviewer1.courses_attached += ['Python', 'C++', 'CSS']
reviewer2.courses_attached += ['Python', 'Git']

student1.rate_lec(lecturer1, 'Python', 7)
student1.rate_lec(lecturer1, 'C++', 7)
student2.rate_lec(lecturer1, 'C++', 1)   #не выполняется, т.к. у студента 2 нет в активных курсах С++
student2.rate_lec(lecturer1, 'Python', 10)
student2.rate_lec(lecturer2, 'Python', 3)
student1.rate_lec(lecturer2, 'Python', 6)
student1.rate_lec(lecturer2, 'С++', 5)   #не выполняется, т.к. у лектора 2 нет в активных курсах С++

# print(lecturer1)
# print(lecturer2)
# print(lecturer1.__dict__)
# print(lecturer2.__dict__)
# print(lecturer1 > lecturer2)
# print(lecturer1 < lecturer2)

reviewer1.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'Python', 3)
reviewer2.rate_hw(student1, 'Git', 7) #не выполняется, т.к. у студента 1 нет в активных курсах Git
reviewer1.rate_hw(student1, 'C++', 5)
reviewer1.rate_hw(student1, 'C++', 5)
reviewer1.rate_hw(student2, 'Python', 5)
reviewer1.rate_hw(student2, 'Git', 2) #не выполняется, т.к. у проверяющего 1 нет в активных курсах Git
reviewer2.rate_hw(student2, 'Git', 7)
reviewer2.rate_hw(student2, 'Git', 3)

# print(student1)
# print(student2)
# print(student1.__dict__)
# print(student2.__dict__)
# print(student1 > student2)
# print(student1 < student2)


def all_student_on_course_average_rating(input_list, course):
    all_grades = []
    for student in input_list:
        if course in student.grades:
            all_grades += student.grades[course]
    print(f'Средняя оценка за домашние задания по всем студентам в рамках курса {course}: {sum(all_grades) / len(all_grades)}')

def all_lecrurer_on_course_average_rating(input_list, course):
    all_grades = []
    for lecturer in input_list:
        if course in lecturer.grades:
            all_grades += lecturer.grades[course]
    print(f'Средняя оценка за лекции всех лекторов в рамках курса {course}: {sum(all_grades) / len(all_grades)}')


# all_student_on_course_average_rating(student_list, 'C++')
# all_lecrurer_on_course_average_rating(lecturer_list, 'Python')