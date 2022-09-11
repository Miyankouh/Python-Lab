from abc import ABCMeta, abstractclassmethod

"""  
Simple factory pattern
"""

class Book(metaclass = ABCMeta):
    
    @abstractclassmethod
    def num_of_pages(self):
        pass


class Head_First_Python(Book):

    def num_of_pages(self):
        print("500")


class Python_CookBook(Book):

    def num_of_pages(self):
        print("300")


# Publication Factory
class PublicationFactory():

    def book_publicator(self, object_type):
        return eval(object_type) ().num_of_pages()


# Client code
if __name__ == '__main__':
    pf = PublicationFactory()
    book = input('What book should I print?, Head_First_Python Or Python_CookBook? : ')
    pf.book_publicator(book) 