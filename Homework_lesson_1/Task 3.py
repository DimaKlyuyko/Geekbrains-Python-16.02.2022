# Задание 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = int(input("Введите целое число >>> "))

result1 = n + (n * 10 + n) + (n * 100 + n * 10 + n)
print(result1)  # Первый вариант решения

result2 = n + int(f"{n}{n}") + int(f"{n}{n}{n}")
print(result2)  # Второй вариант решения
