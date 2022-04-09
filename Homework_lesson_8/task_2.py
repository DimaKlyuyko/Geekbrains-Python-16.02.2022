"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.

При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionException(Exception):
    def __init__(self, dividend: int, divisor: int):
        self.dividend = dividend
        self.divisor = divisor

    def __str__(self):
        return f"Error. You are trying to divide {self.dividend} by {self.divisor} (zero)."


x = int(input("Введите делимое >>> "))
y = int(input("Введите делитель >>> "))

try:
    if y == 0:
        raise MyZeroDivisionException(x, y)
    else:
        print(x / y)
except MyZeroDivisionException:
    print(f"Error. You are trying to divide {x} by {y} (zero).")
