from abc import ABCMeta, abstractclassmethod

"""
Observer Pattern  
"""
# Subject
class Publisher:

    def __init__(self):
        self.__subscribers = []
        self.__latestBooks = None
    
    def register(self, subscribers):
        self.__subscribers.append(subscribers)

    def deregister(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(s).__name__ for s in self.__subscribers]
    
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addBooks(self, books):
        self.__latestBooks = books
    
    def getBooks(self):
        return "New books per week", self.__latestBooks


# Observer
class Subscribe(metaclass = ABCMeta):

    @abstractclassmethod
    def update(self):
        pass


# ConcreteObserver
class SmsSubscribe:

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)

    def update(self):
        print(type(self).__name__, self.publisher.getBooks())


# ConcreteObserver 2
class EmailSubscribe:

    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)

    def update(self):
        print(type(self).__name__, self.publisher.getBooks())


# ConcreteObserver 3
class AnyOtherSubscribe:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.register(self)

    def update(self):
        print(type(self).__name__, self.publisher.getBooks())


# Client
if __name__ == '__main__':
    pub = Publisher()
    for Subscribers in [SmsSubscribe, EmailSubscribe, AnyOtherSubscribe]:
        Subscribers(pub)

    print("\nSubscribers: ", pub.subscribers())
    pub.addBooks("Advanced Python")
    pub.notifySubscribers()
    print("\n Unregister: ", type(pub.deregister()).__name__)
    print("\n Subscribers: ", pub.subscribers)
