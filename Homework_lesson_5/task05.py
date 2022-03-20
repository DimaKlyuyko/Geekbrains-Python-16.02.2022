# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('for_task_05.txt', 'w') as stream:
    stream.write(input("Введите набор чисел, разделённых пробелами >>> "))

result = 0

with open('for_task_05.txt') as stream2:
    for el in stream2.read().replace(' ', ''):
        result += int(el)

    print(result)
