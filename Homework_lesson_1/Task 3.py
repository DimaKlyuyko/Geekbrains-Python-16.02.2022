# Задание 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

# Мой вариант
# n = int(input("Введите целое число >>> "))
#
# result1 = n + (n * 10 + n) + (n * 100 + n * 10 + n)
# print(result1)  # Первый вариант решения
#
# result2 = n + int(f"{n}{n}") + int(f"{n}{n}{n}")
# print(result2)  # Второй вариант решения


# решение от преподавателя
# через строку
# user_input = input("Введите число >>> ")
#
# if not user_input.isdigit():
#     print("Неверный формат числа")
#     exit()
#
# result = 0
# for x in range(1, 4):
#     result += int(user_input * x) # '3' * 2 = 33
#
# print(result)

# через число
user_input = input("Введите число >>> ")

user_number = int(user_input)
characters_count = 0
temp_number = user_number

while temp_number:
    temp_number //= 10
    characters_count += 1

first_level_multiplication = (10 ** characters_count) + 1
second_level_multiplication = (10 ** (characters_count * 2)) + first_level_multiplication

result = user_number + (user_number * first_level_multiplication) + (user_number * second_level_multiplication)

print(result)
