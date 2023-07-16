"""

ЗАДАНИЕ 1
Выбрать класс и описать его на Python, а также создать 2 разных экземпляра класса(объекта)
1.	Класс Покупатель: Фамилия, Имя, Отчество, Адрес, счет; Методы: вывод информации, пополнение счета, списание счета.
2.	Описать класс, представляющий треугольник. Предусмотреть методы  вычисления площади,
 периметра и точки пересечения медиан. Описать свойства для получения состояния объекта.

"""


class Buyer:

    def __init__(self, first_name: str, second_name: str, last_name: str, address: str, balance: int):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__last_name = last_name
        self.__address = address
        self.__balance = balance

    def show(self):
        print(
            f'Имя: {self.__first_name}\nФамилия: {self.__second_name}\nОтчество: {self.__last_name}\n'
            f'Адрес: {self.__address}\nБаланс: {self.__balance}\n')

    def write_off_from_balance(self, amount: int = 0):
        self.__balance -= amount

    def replenishment_balance(self, amount: int = 0):
        self.__balance += amount


first_man = Buyer('Владислав', 'Александров', 'Сергеевич', 'Томск', 10000)
second_man = Buyer('Пётр', 'Петров', 'Петрович', 'Москва', 5000)

first_man.show()
first_man.write_off_from_balance(1000)
first_man.show()
first_man.replenishment_balance(50000)
first_man.show()
