# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

numbers = input("Введите значения >>> ")

if not numbers.isdigit():
    print("Введено не целое число.")
    exit()

numbers = list(numbers)

length = len(numbers)
circles = length // 2
zero_circle = 0
x, y = 0, 1
new_list = []

if (length % 2) == 0:
    while zero_circle != circles:
        numbers[x], numbers[y] = numbers[y], numbers[x]
        new_list.append(numbers[x])
        new_list.append(numbers[y])
        x += 2
        y += 2
        zero_circle += 1

    print(*new_list, sep="")
else:
    while zero_circle != circles:
        numbers[x], numbers[y] = numbers[y], numbers[x]
        new_list.append(numbers[x])
        new_list.append(numbers[y])
        x += 2
        y += 2
        zero_circle += 1

    new_list.append(numbers[length - 1])
    print(*new_list, sep="")
