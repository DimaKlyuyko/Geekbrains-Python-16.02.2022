# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.

start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
finish_list = []

for i in start_list:
    if start_list.index(i) != 0:
        if i > start_list[start_list.index(i)-1]:
            finish_list.append(i)

print(finish_list)
