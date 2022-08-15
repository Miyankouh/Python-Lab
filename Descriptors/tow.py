"""
 __get__  ,  __set__,  __delete__,  __set_name__
"""

class One:
    def __set_name__(self, owner, name):
        print(name)
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('value must be string')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        instance.__dict__[self.name] = None


class Person:
    name = One()
    car = One()

    def __init__(self, name, car):
        self.name = name
        self.car = car


p = Person('majid', 'pride')
