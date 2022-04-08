# oop - object oriented programming
# optional data type

class Student:
    def __init__(self, name, family, email=None):
        self.n = name
        self.f = family
        self.e = email

    def get_full_name(self):
        return self.n + ' ' + self.f


students_1 = Student('Mehrdad', 'mobiny', 'mehrad@gmail')
students_2 = Student('Pari', 'shah', 'p.sa@gmail')

print(students_1.get_full_name())
print(students_2.get_full_name())
