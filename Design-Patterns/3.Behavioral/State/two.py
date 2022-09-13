from abc import ABCMeta, abstractmethod


class State(metaclass = ABCMeta):

    @abstractmethod
    def action(self):
        pass


# Concrete
class OpenState(State):

    def action(self):
        print("Darb baste shod")


class CloseState(State):

    def action(self):
        print("Darb baz shod")


class DoorContext(State):

    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def action(self):
        self.state.action()


context = DoorContext()
context.getState()
open_state = OpenState()
close_state = CloseState()
context.setState(close_state)
context.action()
