# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

# Я понимаю, что моё решение с технической точки зрения слишком сложное,

list1 = [10, 7, 5, 3, 2]
list1.reverse()

user_number = input("Введите целое положительное число >>> ")

if not user_number.isdigit():
    print("Введено некорректное число.")
    exit()
else:
    user_number = int(user_number)

try:  # если число есть, подставить его следом за таким же числом
    if list1.index(user_number) >= 0:
        pos = list1.index(user_number)
        list1.insert(pos, user_number)
        list1.reverse()
        print(list1)

except ValueError:
    if user_number > max(list1):  # если числа нет и оно больше максимального, подставить в начало
        list1.append(user_number)
        list1.reverse()
        print(list1)
    elif user_number < min(list1):  # если числа нет и оно меньше минимального, подставить в конец
        list1.insert(0, user_number)
        list1.reverse()
        print(list1)
    elif min(list1) < user_number < max(list1):  # если числа нет и оно находится в диапазоне от мин до макс
        x = 0
        y = 1
        while list1[x] < user_number > list1[y]:
            x += 1
            y += 1

        list1.insert(y, user_number)
        list1.reverse()
        print(list1)
