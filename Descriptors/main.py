"""  
    property, getter, setter, deleter
"""

class Person:
    def __init__(self, name, car):
        self._name = name
        self._car = car

    @property # getter
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('Value must be string')
        self._name = value

    @name.deleter
    def name(self):
        self._name = None
    """  
        The problem with using this
        (property,getter, setter, deleter) is that it causes repetition in the code
    """
    # Car
    @property # getter
    def car(self):
        return self._car

    @car.setter
    def car(self, value):
        if not isinstance(value, str):
            raise ValueError('Value must be string')
        self._car = value

    @car.deleter
    def car(self):
        self._car = None


new = Person('miyankouh', 'bmw')
# del new.name   # None


if __name__ == "__main__":
    print(new.name)
    print(new.car)
