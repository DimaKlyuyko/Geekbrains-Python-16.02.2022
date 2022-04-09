"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    date: str

    def __init__(self, date: str):
        Date.date = date

    @classmethod
    def extract(cls, x: int):
        if x == 1:  # извлекаем день
            return int(cls.date[:cls.date.find("-")])
        elif x == 2:  # извлекаем месяц
            return int(cls.date[cls.date.find("-") + 1:cls.date.find("-", cls.date.find("-") + 1)])
        elif x == 3:  # извлекаем год
            return int(cls.date[cls.date.find("-", cls.date.find("-") + 1) + 1:])
        else:
            return "Argument is out of range [1, 2, 3]."

    @staticmethod
    def validation(x: int, n: int):
        if n == 1:  # проверка дня
            if x in [y for y in range(1, 32)]:
                return "Validation is OK"
            else:
                return "Validation is WRONG"
        elif n == 2:  # проверка месяца
            if x in [y for y in range(1, 13)]:
                return "Validation is OK"
            else:
                return "Validation is WRONG"
        elif n == 3:  # проверка года
            if x in [y for y in range(1990, 2101)]:
                return "Validation is OK"
            else:
                return "Validation is WRONG"
        else:
            return "Incorrect argument."


my_date = Date("30-05-2022")

print(Date.date, type(Date.date))

print(Date.extract(1), type(Date.extract(1)))
print(Date.extract(2), type(Date.extract(2)))
print(Date.extract(3), type(Date.extract(3)))

print(Date.validation(5, 1))
print(Date.validation(50, 2))
print(Date.validation(int(Date.extract(3)), 3))
