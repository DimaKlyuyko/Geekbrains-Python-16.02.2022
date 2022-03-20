# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_list = ["Odin", "Dwa", "Tri", "Chetiri"]
c = 0
new_list = []

with open('for_task_04.txt') as stream:
    for line in stream.readlines():
        n = int(line.find(" "))
        new_list.append(
            line.replace(
                line[0:n],
                my_list[c])
        )
        c += 1

with open('new_file_for_task_4.txt', 'w') as stream2:
    stream2.writelines(new_list)

with open('new_file_for_task_4.txt') as stream3:
    print(stream3.read())
