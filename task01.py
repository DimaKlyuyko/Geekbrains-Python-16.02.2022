# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# parameters = 168 8 100

from sys import argv

filename, x, y, z = argv


def salary(hours, money_per_hour, bonus):
    return int(hours) * int(money_per_hour) + int(bonus)


print(salary(x, y, z))
