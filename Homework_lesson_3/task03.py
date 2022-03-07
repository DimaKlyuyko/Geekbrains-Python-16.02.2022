# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(x, y, z):
    list1 = [x, y, z]
    max1 = max(list1)
    list1.remove(max1)
    max2 = max(list1)
    print(max1 + max2)


my_func(5, 8, 1)
