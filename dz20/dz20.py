
"""
ЗАДАНИЕ 1 (обязательное)
для данного класса создать метод по возврату билета, данный метод должен уменьшаться __passagers на единицу

"""

class Airplane:

    def __init__(self, name: str, capacity: int, flight: str):
        # поля  класса - характеристики
        self.__name = name  # self.__name - только Airplane может что-то изменить внутри
        self.__capacity = capacity  # вместимость сколько может сесть пассажиров
        self.__flight = flight
        self.__passagers = 0  # кол-во пассажиров

    # метод(поведение или действие объекта) - показать характеристики самолета
    def show(self):
        print(self.__name, self.__capacity, self.__flight, self.__passagers)

    # увелечение кол-во пассажиров
    def buy_ticket(self, count=1):  # если не задали count, то 1
        empty_places = self.__capacity - self.__passagers  # 200 -150 = 50
        if empty_places > 0 and empty_places >= count:  # 50>0 and 50>=3
            self.__passagers += count  # кол-во пассажиров 150+50 =200

    # ДОБАВИТЬ МЕТОД ВОЗРАТА БИЛЕТА
    def return_ticket(self, count=1):
        if self.__passagers > 0:
            self.__passagers -= count


Airbus = Airplane('Аэробус', 200, 'Томск-Москва')

Airbus.show()
Airbus.buy_ticket(10)
Airbus.show()
Airbus.return_ticket(10)
Airbus.show()
