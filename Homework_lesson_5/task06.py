# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных,практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно
# были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

# мой файл
# Informatika: 100(lekcia) 50(praktika) 20(lab)
# Fizika: 30(lekcia) 10(lab)
# Fizkultura: 30(praktika)
# Matematika: 70(lekcia) 20(praktika)
# Biologia: 70(lekcia) 10(lab)

with open('for_task_06.txt') as stream:
    new_dict = {}
    for line in stream.readlines():
        temp_list = line.replace('\n', '').split()
        exercises = [x for x in temp_list[1:]]
        new_list = []
        for i in exercises:
            new_list.append(int(i[0:int(i.find('('))]))
        new_dict[temp_list[0]] = sum(new_list)

    print(new_dict)
