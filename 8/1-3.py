# oop - object oriented programming
# 1. class
# self


class Math:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def additions(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2


my_math = Math(20, 10)
my_math2 = Math(200, 100)

print(my_math.additions())
print(my_math.subtraction())

print(my_math2.additions())
print(my_math2.subtraction())