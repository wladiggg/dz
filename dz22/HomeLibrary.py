#class HomeLibrary:
#
#   def __int__(self, quantity):
#       self.__quantity = quantity


class Book:

    def __init__(self, name, author):
        self.__name = name
        self.__author = author

    def show(self):
        print(self.__name, self.__author)

    @property
    def book(self):
        return [self.__name, self.__author]
