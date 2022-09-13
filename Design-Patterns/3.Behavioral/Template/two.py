from abc import ABCMeta, abstractclassmethod


class AbstractClass(metaclass = ABCMeta):

    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def operation_1(self):
        pass

    @abstractclassmethod
    def operation_2(self):
        pass

    @abstractclassmethod
    def operation_3(self):
        pass

    def template_method(self):
        print(
            "The order of operations is as follows: first:\
            operation2, second: operation3, third: operation1"
        )
        self.operation_2()
        self.operation_3()
        self.operation_1()


class ConcreteClass(AbstractClass):

    def operation_1(self):
        print("operation_1 anjam shod")

    def operation_2(self):
        print("operation_2 anjam shod")

    def operation_3(self):
        print("operation_3 anjam shod")


#Client
class Client():

    def action(self):
        self.concreteClass = ConcreteClass()
        self.concreteClass.template_method()


client = Client()
client.action()
