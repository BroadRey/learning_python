class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Person fullname is {self.fullname}\n'
              f'Person age is {self.age}\n'
              f'Is person married? {self.is_married}')


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_mark(self):
        return sum(self.marks.values()) / len(self.marks)


class Teacher(Person):
    salary = 15000

    def __init__(self, fullname, age, is_married, experience=1):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        final_salary = self.salary

        if self.experience > 3:
            final_salary = final_salary + final_salary * \
                0.05 * (self.experience - 3)

        return final_salary


olga = Teacher('Olga Pavlovna', 27, True, 5)
olga.introduce_myself()
print(f'Olga salary is {olga.calculate_salary()}\n')


def create_students():
    vovochka = Student('Vova Vovochkin', 18, False,
                       {'Алгебра': 3, 'Физика': 4})
    natasha = Student('Natalia Sergeevna', 19, True,
                      {'Алгебра': 5, 'Физика': 5})
    ekaterina = Student('Ekaterina Vladimirovna', 20,
                        False, {'Алгебра': 4, 'Физика': 2})

    return [vovochka, natasha, ekaterina]


for student in create_students():
    student.introduce_myself()
    print(f'Marks in all subjects: {student.marks}')
    print(f'Average mark in all subjects {student.average_mark()}\n')