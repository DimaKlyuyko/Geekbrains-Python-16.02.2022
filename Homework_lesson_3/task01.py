# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(dividend, divider):
    """
    Возврат результата деления в формате целого числа без остатка
    :param dividend: Делимое
    :param divider: Делитель
    :return: Результат деления
    :rtype: int
    """
    try:
        result = dividend // divider
        if result == 0:
            print("Делитель больше делимого числа!!!")
        else:
            print(result)
    except ZeroDivisionError:
        print("Деление на 0 невозможно.")


x = int(input("Введите целое число >>> "))
y = int(input("Введите целое число >>> "))

division(x, y)
