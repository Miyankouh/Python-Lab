from abc import ABCMeta, abstractclassmethod


# Command
class Command(metaclass = ABCMeta):

    def __init__(self, rec):
        self.rec = rec
    
    @abstractclassmethod
    def execute(self):
        pass


# Concrete Command
class ConcreteCommand(Command):
    
    def __init__(self, rec):
        self.rec = rec
    
    def execute(self):
        self.rec.action()


# Receiver
class Receiver():

    def action(self):
        print("action")


# Invoker
class Invoker:
    def command(self, com):
        self.com = com
    
    def execute(self):
        self.com.execute()


# Client
if __name__ == "__main__":
    rec = Receiver()
    com = ConcreteCommand(rec)
    invoker = Invoker()
    invoker.command(com)
    invoker.execute()
    