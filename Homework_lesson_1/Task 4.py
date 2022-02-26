# Задание 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_input = input("Введите целое число >>> ")

if not user_input.isdigit():  # проверка, что было введено целое число
    print("Вы ввели что-то не то...")
    exit()

number = int(user_input)
max_number = 0

while number and max_number != 9:  # переменная number просто должна существовать, т.е. быть > 0
    current = number % 10  # запоминаю первую цифру справа
    number = number // 10  # уменьшаю число на 1 цифру справа
    max_number = current if current > max_number else max_number  # переприсваиваю большую цифру

print(max_number)
