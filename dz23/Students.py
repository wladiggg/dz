class Student:
    def __init__(self, name, group, gpa, id):
        self.__name = name
        self.__group = group
        self.__gpa = gpa
        self.__id = id

    def show(self):
        print('id:', self.__id, self.__name, self.__group, self.__gpa)

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
        if type(group) == str:
            self.__group = group
        else:
            raise 'Аттрибут должен быть строкой'

    # @property
    # def gpa(self):
    #     return self.__gpa
    #
    # @gpa.setter
    # def gpa(self, gpa):
    #     if type(gpa) == int:
    #         self.__gpa = gpa
    #     else:
    #         raise 'Аттрибут должен быть целым числом'

    @property
    def id(self):
        return self.__id
